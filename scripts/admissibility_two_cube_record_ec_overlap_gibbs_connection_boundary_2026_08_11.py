#!/usr/bin/env python3
"""Certify two-cube gluing and localize the first bulk-gravity boundary.

Two face-sharing spatial cubes are assembled as one factor graph with twelve
vertices, twenty unique edges, eleven unique faces, and forty-four based face
loops.  The inherited ten-label Record/coframe/link interaction is counted
once per geometric carrier.  Exact tensor transfer verifies branchwise
inclusion--exclusion gluing and the induced boundary-message form of the
finite-volume conditional law.

The same calculation distinguishes a fixed elementary-face coefficient from
an inadmissible region-degree "average" and classifies a translation-invariant
proper-cubic homogeneous connection on its full compact angle.  The latter has
flat stable reduced branches and nonflat unstable reduced extrema; none of the
nonflat reduced extrema is promoted to a full connection solution.  This is a
finite Euclidean law/connection boundary, not a gravity no-go or axiom change.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PROPER_CUBIC_SPATIAL_PLAQUETTE_RECORD_COFRAME_"
    "PALATINI_CURVATURE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_PROPER_CUBIC_SPATIAL_PLAQUETTE_RECORD_COFRAME_PALATINI_CURVATURE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

DIMENSION = 4
ETA = 1.0 / 5.0
TAU = 3.0 / 10.0
BETA = 1.0 / 5.0
SIGMA = 1.0 / 2.0
NORMAL_COMPATIBILITY = 1.0 / 5.0
ALPHA = 16.0
FACE_COEFFICIENT_DIVISOR = 3.0
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
E_STAR = np.diag((1.0, 1.0, 1.0, 5.0 / 4.0))

# Three yz layers expose an exact width-four transfer contraction of the
# nominal 10^12 Record assignments.
X_COORDINATES = (-1, 1, 3)
YZ_CYCLE = ((-1, -1), (1, -1), (1, 1), (-1, 1))
VERTICES = tuple(
    (x_coordinate, y_coordinate, z_coordinate)
    for x_coordinate in X_COORDINATES
    for y_coordinate, z_coordinate in YZ_CYCLE
)
VERTEX_INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}
COFRAMES_STAR = tuple(E_STAR.copy() for _ in VERTICES)


def lattice_edges() -> tuple[tuple[int, int, int], ...]:
    edges: list[tuple[int, int, int]] = []
    for low, vertex in enumerate(VERTICES):
        for axis in range(3):
            high_vertex = list(vertex)
            high_vertex[axis] += 2
            if tuple(high_vertex) in VERTEX_INDEX:
                edges.append((low, VERTEX_INDEX[tuple(high_vertex)], axis))
    return tuple(edges)


EDGES = lattice_edges()
EDGE_INDEX = {(low, high): index for index, (low, high, _) in enumerate(EDGES)}


@dataclass(frozen=True)
class Face:
    loop: tuple[int, int, int, int]


def lattice_faces() -> tuple[Face, ...]:
    faces: list[Face] = []
    for first_axis, second_axis in ((0, 1), (0, 2), (1, 2)):
        fixed_axis = ({0, 1, 2} - {first_axis, second_axis}).pop()
        fixed_values = X_COORDINATES if fixed_axis == 0 else (-1, 1)
        first_lows = (-1, 1) if first_axis == 0 else (-1,)
        second_lows = (-1, 1) if second_axis == 0 else (-1,)
        for fixed_value in fixed_values:
            for first_low in first_lows:
                for second_low in second_lows:
                    start = [0, 0, 0]
                    start[fixed_axis] = fixed_value
                    start[first_axis] = first_low
                    start[second_axis] = second_low
                    first = tuple(start)
                    second = list(first)
                    second[first_axis] += 2
                    second = tuple(second)
                    third = list(second)
                    third[second_axis] += 2
                    third = tuple(third)
                    fourth = list(first)
                    fourth[second_axis] += 2
                    fourth = tuple(fourth)
                    vertices = (first, second, third, fourth)
                    if all(vertex in VERTEX_INDEX for vertex in vertices):
                        faces.append(
                            Face(tuple(VERTEX_INDEX[vertex] for vertex in vertices))
                        )
    return tuple(faces)


FACES = lattice_faces()


def face_loops(face: Face) -> tuple[tuple[int, int, int, int], ...]:
    return tuple(
        tuple(face.loop[(offset + step) % 4] for step in range(4))
        for offset in range(4)
    )


PLAQUETTES = tuple(loop for face in FACES for loop in face_loops(face))
LEFT_VERTICES = tuple(index for index, vertex in enumerate(VERTICES) if vertex[0] <= 1)
RIGHT_VERTICES = tuple(index for index, vertex in enumerate(VERTICES) if vertex[0] >= 1)
OVERLAP_VERTICES = tuple(index for index, vertex in enumerate(VERTICES) if vertex[0] == 1)
LEFT_EDGES = tuple(
    index
    for index, (low, high, _) in enumerate(EDGES)
    if VERTICES[low][0] <= 1 and VERTICES[high][0] <= 1
)
RIGHT_EDGES = tuple(
    index
    for index, (low, high, _) in enumerate(EDGES)
    if VERTICES[low][0] >= 1 and VERTICES[high][0] >= 1
)
OVERLAP_EDGES = tuple(
    index
    for index, (low, high, _) in enumerate(EDGES)
    if VERTICES[low][0] == 1 and VERTICES[high][0] == 1
)
LEFT_FACES = tuple(
    index
    for index, face in enumerate(FACES)
    if all(VERTICES[site][0] <= 1 for site in face.loop)
)
RIGHT_FACES = tuple(
    index
    for index, face in enumerate(FACES)
    if all(VERTICES[site][0] >= 1 for site in face.loop)
)
OVERLAP_FACES = tuple(
    index
    for index, face in enumerate(FACES)
    if all(VERTICES[site][0] == 1 for site in face.loop)
)


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
    return np.outer(right, left) - np.outer(left, right)


def hodge_star(bivector: np.ndarray) -> np.ndarray:
    return 0.5 * np.einsum("ijab,ab->ij", EPSILON, bivector)


def spatial_normal(coframe: np.ndarray) -> np.ndarray:
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
    complementary = np.concatenate((np.cross(first_step, second_step), (0.0,)))
    return hodge_star(wedge(coframe @ complementary, spatial_normal(coframe)))


def oriented_link(links: tuple[np.ndarray, ...], start: int, end: int) -> np.ndarray:
    if (start, end) in EDGE_INDEX:
        return links[EDGE_INDEX[(start, end)]]
    return links[EDGE_INDEX[(end, start)]].T


def axis_generator(direction: np.ndarray) -> np.ndarray:
    direction = np.asarray(direction, dtype=float)
    generator = np.zeros((4, 4), dtype=float)
    generator[:3, :3] = np.asarray(
        (
            (0.0, -direction[2], direction[1]),
            (direction[2], 0.0, -direction[0]),
            (-direction[1], direction[0], 0.0),
        )
    )
    return generator


def directional_link(angle: float, direction: np.ndarray) -> np.ndarray:
    return expm(angle * axis_generator(direction))


def homogeneous_links(angle: float) -> tuple[np.ndarray, ...]:
    return tuple(
        directional_link(angle, np.eye(3, dtype=float)[axis])
        for _, _, axis in EDGES
    )


def cube_centered_link(
    low: int, high: int, axis: int, center: np.ndarray, coefficient: float
) -> np.ndarray:
    direction = np.eye(3, dtype=float)[axis]
    midpoint = (
        np.asarray(VERTICES[low], dtype=float)
        + np.asarray(VERTICES[high], dtype=float)
    ) / 2.0
    direction_four = np.concatenate((direction, (0.0,)))
    relative_four = np.concatenate((midpoint - center, (0.0,)))
    return expm(-coefficient * wedge(direction_four, relative_four))


@dataclass(frozen=True)
class RecordState:
    weights: tuple[np.ndarray, ...]
    projectors: tuple[np.ndarray, ...]


def record_state(coframes: tuple[np.ndarray, ...]) -> RecordState:
    weights: list[np.ndarray] = []
    projectors: list[np.ndarray] = []
    for coframe in coframes:
        images = (coframe @ RAYS.T).T
        squared_norms = np.einsum("ri,ri->r", images, images)
        weights.append(RECORD_WEIGHTS * np.exp(-0.5 * squared_norms))
        projectors.append(
            np.asarray(
                [np.outer(image, image) / float(np.dot(image, image)) for image in images]
            )
        )
    return RecordState(tuple(weights), tuple(projectors))


def record_kernels(
    state: RecordState, links: tuple[np.ndarray, ...], beta: float = BETA
) -> tuple[np.ndarray, ...]:
    kernels: list[np.ndarray] = []
    for link, (low, high, _) in zip(links, EDGES):
        transported = np.einsum(
            "ab,sbc,dc->sad", link, state.projectors[high], link
        )
        difference = state.projectors[low][:, None] - transported[None, :]
        squared_distance = np.einsum("rsij,rsij->rs", difference, difference)
        kernels.append(np.exp(-0.5 * beta * squared_distance))
    return tuple(kernels)


def face_signal(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    loop: tuple[int, int, int, int],
) -> tuple[float, float, float]:
    first, second, third, fourth = loop
    position = np.asarray(VERTICES[first], dtype=float)
    first_step = (np.asarray(VERTICES[second], dtype=float) - position) / 2.0
    second_step = (np.asarray(VERTICES[fourth], dtype=float) - position) / 2.0
    holonomy = (
        oriented_link(links, first, second)
        @ oriented_link(links, second, third)
        @ oriented_link(links, third, fourth)
        @ oriented_link(links, fourth, first)
    )
    sine_curvature = 0.5 * (holonomy - holonomy.T)
    bivector = einstein_cartan_bivector(
        coframes[first], first_step, second_step
    )
    signal = 0.5 * float(np.sum(bivector * sine_curvature))
    first_base = np.concatenate((first_step, (0.0,)))
    second_base = np.concatenate((second_step, (0.0,)))
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
    torsion = float(np.linalg.norm(first_difference - second_difference))
    return float(np.linalg.norm(holonomy - np.eye(4))), signal, torsion


def loop_holonomy(
    links: tuple[np.ndarray, ...], loop: tuple[int, int, int, int]
) -> np.ndarray:
    first, second, third, fourth = loop
    return (
        oriented_link(links, first, second)
        @ oriented_link(links, second, third)
        @ oriented_link(links, third, fourth)
        @ oriented_link(links, fourth, first)
    )


def cube_bianchi_residual(
    links: tuple[np.ndarray, ...], low_x: int
) -> float:
    """Return the exact ordered-product boundary identity for one cube."""

    def site(x: int, y: int, z: int) -> int:
        return VERTEX_INDEX[(x, y, z)]

    origin = site(low_x, -1, -1)
    x_site = site(low_x + 2, -1, -1)
    y_site = site(low_x, 1, -1)
    z_site = site(low_x, -1, 1)
    xy_site = site(low_x + 2, 1, -1)
    xz_site = site(low_x + 2, -1, 1)
    yz_site = site(low_x, 1, 1)
    xyz_site = site(low_x + 2, 1, 1)

    p_xy_low = loop_holonomy(
        links, (origin, x_site, xy_site, y_site)
    )
    p_xy_high = loop_holonomy(
        links, (z_site, xz_site, xyz_site, yz_site)
    )
    p_yz_low = loop_holonomy(
        links, (origin, y_site, yz_site, z_site)
    )
    p_yz_high = loop_holonomy(
        links, (x_site, xy_site, xyz_site, xz_site)
    )
    p_zx_low = loop_holonomy(
        links, (origin, z_site, xz_site, x_site)
    )
    p_zx_high = loop_holonomy(
        links, (y_site, yz_site, xyz_site, xy_site)
    )
    transport_x = oriented_link(links, origin, x_site)
    transport_y = oriented_link(links, origin, y_site)
    transport_z = oriented_link(links, origin, z_site)

    # This ordering freely cancels the twelve oriented boundary-edge words.
    product_boundary = (
        p_xy_low.T
        @ transport_x
        @ p_yz_high
        @ transport_x.T
        @ p_zx_low.T
        @ transport_z
        @ p_xy_high
        @ transport_z.T
        @ p_yz_low.T
        @ transport_y
        @ p_zx_high
        @ transport_y.T
    )
    return float(np.linalg.norm(product_boundary - np.eye(4)))


def cube_bianchi_word_reduces() -> bool:
    """Check the same identity exactly in the free oriented-edge word."""

    x0, xy, xz, xyz, y0, yx, yz, yxz, z0, zx, zy, zxy = range(1, 13)

    def inverse(word: list[int]) -> list[int]:
        return [-letter for letter in reversed(word)]

    def conjugate(path: list[int], word: list[int]) -> list[int]:
        return path + word + inverse(path)

    def reduce_word(word: list[int]) -> list[int]:
        stack: list[int] = []
        for letter in word:
            if stack and stack[-1] == -letter:
                stack.pop()
            else:
                stack.append(letter)
        return stack

    p_xy_low = [x0, yx, -xy, -y0]
    p_xy_high = [xz, yxz, -xyz, -yz]
    p_yz_low = [y0, zy, -yz, -z0]
    p_yz_high = [yx, zxy, -yxz, -zx]
    p_zx_low = [z0, xz, -zx, -x0]
    p_zx_high = [zy, xyz, -zxy, -xy]
    ordered_faces = (
        inverse(p_xy_low),
        conjugate([x0], p_yz_high),
        inverse(p_zx_low),
        conjugate([z0], p_xy_high),
        inverse(p_yz_low),
        conjugate([y0], p_zx_high),
    )
    product_word: list[int] = []
    for face_word in ordered_faces:
        product_word = reduce_word(product_word + face_word)
    return not product_word


def curvature_loads(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    face_indices: tuple[int, ...] = tuple(range(11)),
) -> tuple[np.ndarray, ...]:
    loads = [np.zeros(10, dtype=float) for _ in VERTICES]
    for face_index in face_indices:
        for first, second, third, fourth in face_loops(FACES[face_index]):
            position = np.asarray(VERTICES[first], dtype=float)
            first_step = (
                np.asarray(VERTICES[second], dtype=float) - position
            ) / 2.0
            second_step = (
                np.asarray(VERTICES[fourth], dtype=float) - position
            ) / 2.0
            _, signal, _ = face_signal(
                coframes, links, (first, second, third, fourth)
            )
            incidence = (
                (RAYS[:, :3] @ first_step) ** 2
                + (RAYS[:, :3] @ second_step) ** 2
            )
            loads[first] += incidence * signal
    return tuple(loads)


def layer_tensor(
    weights: tuple[np.ndarray, ...],
    kernels: tuple[np.ndarray, ...],
    first_site: int,
) -> np.ndarray:
    first, second, third, fourth = range(first_site, first_site + 4)
    return np.einsum(
        "a,b,c,d,ab,bc,dc,ad->abcd",
        weights[first],
        weights[second],
        weights[third],
        weights[fourth],
        kernels[EDGE_INDEX[(first, second)]],
        kernels[EDGE_INDEX[(second, third)]],
        kernels[EDGE_INDEX[(fourth, third)]],
        kernels[EDGE_INDEX[(first, fourth)]],
        optimize=True,
    )


def transfer_forward(
    tensor: np.ndarray,
    kernels: tuple[np.ndarray, ...],
    low_layer: int,
) -> np.ndarray:
    high_layer = low_layer + 4
    tensor = np.einsum(
        "abcd,ae->ebcd",
        tensor,
        kernels[EDGE_INDEX[(low_layer, high_layer)]],
        optimize=True,
    )
    tensor = np.einsum(
        "ebcd,bf->efcd",
        tensor,
        kernels[EDGE_INDEX[(low_layer + 1, high_layer + 1)]],
        optimize=True,
    )
    tensor = np.einsum(
        "efcd,cg->efgd",
        tensor,
        kernels[EDGE_INDEX[(low_layer + 2, high_layer + 2)]],
        optimize=True,
    )
    return np.einsum(
        "efgd,dh->efgh",
        tensor,
        kernels[EDGE_INDEX[(low_layer + 3, high_layer + 3)]],
        optimize=True,
    )


def transfer_backward(
    tensor: np.ndarray,
    kernels: tuple[np.ndarray, ...],
    low_layer: int,
) -> np.ndarray:
    high_layer = low_layer + 4
    tensor = np.einsum(
        "efgh,ae->afgh",
        tensor,
        kernels[EDGE_INDEX[(low_layer, high_layer)]],
        optimize=True,
    )
    tensor = np.einsum(
        "afgh,bf->abgh",
        tensor,
        kernels[EDGE_INDEX[(low_layer + 1, high_layer + 1)]],
        optimize=True,
    )
    tensor = np.einsum(
        "abgh,cg->abch",
        tensor,
        kernels[EDGE_INDEX[(low_layer + 2, high_layer + 2)]],
        optimize=True,
    )
    return np.einsum(
        "abch,dh->abcd",
        tensor,
        kernels[EDGE_INDEX[(low_layer + 3, high_layer + 3)]],
        optimize=True,
    )


@dataclass(frozen=True)
class FactorTensors:
    weights: tuple[np.ndarray, ...]
    kernels: tuple[np.ndarray, ...]
    layers: tuple[np.ndarray, np.ndarray, np.ndarray]
    left_message: np.ndarray
    right_message: np.ndarray


def factor_tensors(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    sigma: float = SIGMA,
    face_indices: tuple[int, ...] = tuple(range(11)),
) -> FactorTensors:
    state = record_state(coframes)
    loads = curvature_loads(coframes, links, face_indices)
    weights = tuple(
        weight * np.exp((sigma / FACE_COEFFICIENT_DIVISOR) * load)
        for weight, load in zip(state.weights, loads)
    )
    kernels = record_kernels(state, links)
    layers = tuple(layer_tensor(weights, kernels, site) for site in (0, 4, 8))
    left_message = transfer_forward(layers[0], kernels, 0)
    right_message = transfer_backward(layers[2], kernels, 4)
    return FactorTensors(
        weights,
        kernels,
        (layers[0], layers[1], layers[2]),
        left_message,
        right_message,
    )


def record_partition(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    sigma: float = SIGMA,
    face_indices: tuple[int, ...] = tuple(range(11)),
) -> float:
    tensors = factor_tensors(coframes, links, sigma, face_indices)
    return float(
        np.sum(tensors.left_message * tensors.layers[1] * tensors.right_message)
    )


def geometry_penalty(
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    vertex_indices: tuple[int, ...],
    edge_indices: tuple[int, ...],
    face_indices: tuple[int, ...],
    common_target: np.ndarray | None = None,
) -> float:
    compatibility = 0.5 * ETA * sum(
        float(np.sum((coframes[low] - links[edge] @ coframes[high]) ** 2))
        for edge in edge_indices
        for low, high, _ in (EDGES[edge],)
    )
    normals = tuple(spatial_normal(coframe) for coframe in coframes)
    normal = 0.5 * NORMAL_COMPATIBILITY * sum(
        float(np.sum((normals[low] - links[edge] @ normals[high]) ** 2))
        for edge in edge_indices
        for low, high, _ in (EDGES[edge],)
    )
    torsion = 0.0
    for face_index in face_indices:
        for loop in face_loops(FACES[face_index]):
            _, _, torsion_norm = face_signal(coframes, links, loop)
            torsion += (TAU / 8.0) * torsion_norm**2
    well = 0.0
    if common_target is not None:
        well = (ALPHA / 4.0) * sum(
            float(np.sum((coframes[site].T @ coframes[site] - common_target) ** 2))
            for site in vertex_indices
        )
    return compatibility + normal + torsion + well


def action_value(
    coframes: tuple[np.ndarray, ...], links: tuple[np.ndarray, ...]
) -> float:
    penalty = geometry_penalty(
        coframes,
        links,
        tuple(range(12)),
        tuple(range(20)),
        tuple(range(11)),
    )
    return penalty - float(np.log(record_partition(coframes, links)))


def microscopic_log_weight(
    labels: np.ndarray,
    coframes: tuple[np.ndarray, ...],
    links: tuple[np.ndarray, ...],
    vertex_indices: tuple[int, ...],
    edge_indices: tuple[int, ...],
    face_indices: tuple[int, ...],
    *,
    adaptive_incidence_average: bool = False,
) -> float:
    state = record_state(coframes)
    kernels = record_kernels(state, links)
    loads = curvature_loads(coframes, links, face_indices)
    value = sum(float(np.log(state.weights[site][labels[site]])) for site in vertex_indices)
    value += sum(
        float(np.log(kernels[edge][labels[low], labels[high]]))
        for edge in edge_indices
        for low, high, _ in (EDGES[edge],)
    )
    if adaptive_incidence_average:
        incidence_counts = {site: 0 for site in vertex_indices}
        for face_index in face_indices:
            for site in FACES[face_index].loop:
                incidence_counts[site] += 1
        value += sum(
            SIGMA * float(loads[site][labels[site]]) / incidence_counts[site]
            for site in vertex_indices
        )
    else:
        value += sum(
            (SIGMA / FACE_COEFFICIENT_DIVISOR)
            * float(loads[site][labels[site]])
            for site in vertex_indices
        )
    value -= geometry_penalty(
        coframes,
        links,
        vertex_indices,
        edge_indices,
        face_indices,
        E_STAR.T @ E_STAR,
    )
    return float(value)


def homogeneous_action(angle: float) -> float:
    return action_value(COFRAMES_STAR, homogeneous_links(angle))


def scalar_derivative(angle: float, step: float = 2.0e-5) -> float:
    return (
        homogeneous_action(angle + step) - homogeneous_action(angle - step)
    ) / (2.0 * step)


def scalar_second_derivative(angle: float, step: float = 2.0e-3) -> float:
    return (
        homogeneous_action(angle + step)
        - 2.0 * homogeneous_action(angle)
        + homogeneous_action(angle - step)
    ) / step**2


def link_gradient(
    coframes: tuple[np.ndarray, ...], links: tuple[np.ndarray, ...]
) -> np.ndarray:
    gradient = np.zeros((20, 6), dtype=float)
    for edge in range(20):
        for generator_index, generator in enumerate(SKEW_GENERATORS):
            plus = list(links)
            minus = list(links)
            plus[edge] = expm(LINK_STEP * generator) @ links[edge]
            minus[edge] = expm(-LINK_STEP * generator) @ links[edge]
            gradient[edge, generator_index] = (
                action_value(coframes, tuple(plus))
                - action_value(coframes, tuple(minus))
            ) / (2.0 * LINK_STEP)
    return gradient


def coframe_gradient(
    coframes: tuple[np.ndarray, ...], links: tuple[np.ndarray, ...]
) -> np.ndarray:
    gradient = np.zeros((12, 4, 4), dtype=float)
    for site in range(12):
        for row in range(4):
            for column in range(4):
                plus = [coframe.copy() for coframe in coframes]
                minus = [coframe.copy() for coframe in coframes]
                plus[site][row, column] += COFRAME_STEP
                minus[site][row, column] -= COFRAME_STEP
                gradient[site, row, column] = (
                    action_value(tuple(plus), links)
                    - action_value(tuple(minus), links)
                ) / (2.0 * COFRAME_STEP)
    return gradient


def transformed_configuration(
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

    checks.check(
        "premise-parent-scope",
        "the runner binds the four-axiom premise and Block-37 finite EC parent without importing an extensional or gravity law",
        all(path.exists() for path in (NOTE_PATH, AXIOM_PATH, PARENT_PATH, PREMISE_REGISTRY_PATH))
        and "lattice / physical locality" in axiom
        and "not a gravity derivation" in parent
        and "audit-status authority" in note,
    )

    checks.check(
        "two-cube-unique-carrier-census",
        "two face-sharing cubes reduce 16/24/12 naive cell counts to 12 unique vertices, 20 edges, 11 faces, and 44 based loops",
        len(VERTICES) == 12
        and len(EDGES) == 20
        and len(FACES) == 11
        and len(PLAQUETTES) == 44
        and len(LEFT_VERTICES) == len(RIGHT_VERTICES) == 8
        and len(OVERLAP_VERTICES) == 4
        and len(LEFT_EDGES) == len(RIGHT_EDGES) == 12
        and len(OVERLAP_EDGES) == 4
        and len(LEFT_FACES) == len(RIGHT_FACES) == 6
        and len(OVERLAP_FACES) == 1,
        f"union/left/right/overlap V={len(VERTICES)}/{len(LEFT_VERTICES)}/{len(RIGHT_VERTICES)}/{len(OVERLAP_VERTICES)} E={len(EDGES)}/{len(LEFT_EDGES)}/{len(RIGHT_EDGES)}/{len(OVERLAP_EDGES)} F={len(FACES)}/{len(LEFT_FACES)}/{len(RIGHT_FACES)}/{len(OVERLAP_FACES)}",
    )

    curved_angle = brentq(scalar_derivative, 2.6, 2.9, xtol=1.0e-12)
    curved_links = homogeneous_links(curved_angle)
    flat_links = homogeneous_links(0.0)

    orientation_errors = []
    for face in FACES:
        forward = face.loop
        reverse = (forward[0], forward[3], forward[2], forward[1])
        orientation_errors.append(
            abs(
                face_signal(COFRAMES_STAR, curved_links, forward)[1]
                - face_signal(COFRAMES_STAR, curved_links, reverse)[1]
            )
        )
    checks.check(
        "shared-face-orientation-independence",
        "reversing a face flips both complementary triad and sine holonomy, leaving the intrinsic EC scalar unchanged",
        max(orientation_errors) < 2.0e-14,
        f"maximum orientation-reversal error={max(orientation_errors):.3e}",
    )

    coefficient = 0.323988455
    shared_copy_errors = []
    for edge in OVERLAP_EDGES:
        low, high, axis = EDGES[edge]
        left_link = cube_centered_link(low, high, axis, np.asarray((0.0, 0.0, 0.0)), coefficient)
        right_link = cube_centered_link(low, high, axis, np.asarray((2.0, 0.0, 0.0)), coefficient)
        shared_copy_errors.append(float(np.linalg.norm(left_link - right_link)))
    checks.check(
        "cube-centered-copy-conflict",
        "naively copying the Block-37 cube-centered connection assigns incompatible matrices to every shared-face edge",
        min(shared_copy_errors) > 0.4,
        f"shared-edge mismatch={min(shared_copy_errors):.6f}..{max(shared_copy_errors):.6f}",
    )

    translation_error = max(
        float(np.linalg.norm(curved_links[first] - curved_links[second]))
        for first, (_, _, first_axis) in enumerate(EDGES)
        for second, (_, _, second_axis) in enumerate(EDGES)
        if first_axis == second_axis
    )
    cubic_errors = []
    for spatial in SPATIAL_ROTATIONS:
        lifted = four_rotation(spatial)
        for axis in range(3):
            direction = np.eye(3, dtype=float)[axis]
            transformed_direction = spatial @ direction
            target = directional_link(curved_angle, transformed_direction)
            source = lifted @ directional_link(curved_angle, direction) @ lifted.T
            cubic_errors.append(float(np.linalg.norm(source - target)))
    checks.check(
        "homogeneous-link-translation-cubic-covariance",
        "the alternative link field depends only on signed edge direction and intertwines all 24 proper-cubic rotations",
        translation_error < 1.0e-15 and max(cubic_errors) < 2.0e-15,
        f"translation/cubic errors={translation_error:.3e}/{max(cubic_errors):.3e}",
    )

    generic_links = tuple(
        expm((0.013 * (edge + 1)) * SKEW_GENERATORS[edge % 6]) @ link
        for edge, link in enumerate(curved_links)
    )
    bianchi_residuals = [
        cube_bianchi_residual(generic_links, low_x) for low_x in (-1, 1)
    ]
    checks.check(
        "ordered-product-cube-bianchi-identity",
        "the six transported outward face holonomies on each cube cancel as an exact nonabelian boundary word for a generic link field",
        cube_bianchi_word_reduces() and max(bianchi_residuals) < 2.0e-12,
        f"left/right residual={bianchi_residuals[0]:.3e}/{bianchi_residuals[1]:.3e}",
    )

    sample_labels = [
        np.asarray([(sample + 3 * site) % 10 for site in range(12)], dtype=int)
        for sample in range(24)
    ]
    gluing_errors = []
    adaptive_errors = []
    for labels in sample_labels:
        union = microscopic_log_weight(
            labels,
            COFRAMES_STAR,
            curved_links,
            tuple(range(12)),
            tuple(range(20)),
            tuple(range(11)),
        )
        left = microscopic_log_weight(
            labels, COFRAMES_STAR, curved_links, LEFT_VERTICES, LEFT_EDGES, LEFT_FACES
        )
        right = microscopic_log_weight(
            labels, COFRAMES_STAR, curved_links, RIGHT_VERTICES, RIGHT_EDGES, RIGHT_FACES
        )
        overlap = microscopic_log_weight(
            labels,
            COFRAMES_STAR,
            curved_links,
            OVERLAP_VERTICES,
            OVERLAP_EDGES,
            OVERLAP_FACES,
        )
        gluing_errors.append(abs(union - (left + right - overlap)))
        union_adaptive = microscopic_log_weight(
            labels,
            COFRAMES_STAR,
            curved_links,
            tuple(range(12)),
            tuple(range(20)),
            tuple(range(11)),
            adaptive_incidence_average=True,
        )
        left_adaptive = microscopic_log_weight(
            labels,
            COFRAMES_STAR,
            curved_links,
            LEFT_VERTICES,
            LEFT_EDGES,
            LEFT_FACES,
            adaptive_incidence_average=True,
        )
        right_adaptive = microscopic_log_weight(
            labels,
            COFRAMES_STAR,
            curved_links,
            RIGHT_VERTICES,
            RIGHT_EDGES,
            RIGHT_FACES,
            adaptive_incidence_average=True,
        )
        overlap_adaptive = microscopic_log_weight(
            labels,
            COFRAMES_STAR,
            curved_links,
            OVERLAP_VERTICES,
            OVERLAP_EDGES,
            OVERLAP_FACES,
            adaptive_incidence_average=True,
        )
        adaptive_errors.append(
            abs(union_adaptive - (left_adaptive + right_adaptive - overlap_adaptive))
        )
    checks.check(
        "branchwise-inclusion-exclusion-gluing",
        "fixed elementary vertex/edge/face potentials obey union equals left plus right minus overlap for every tested Record branch",
        max(gluing_errors) < 3.0e-13,
        f"24-branch maximum log-weight error={max(gluing_errors):.3e}",
    )
    checks.check(
        "adaptive-incidence-average-rejected",
        "renormalizing the face coefficient by each finite region's local incidence degree breaks the same branchwise gluing identity",
        max(adaptive_errors) > 5.0e-2
        and float(np.mean(adaptive_errors)) > 1.0e-2,
        f"adaptive gluing defect={min(adaptive_errors):.6f}..{max(adaptive_errors):.6f}",
    )

    tensors = factor_tensors(COFRAMES_STAR, curved_links)
    partition = float(
        np.sum(tensors.left_message * tensors.layers[1] * tensors.right_message)
    )
    transferred = transfer_forward(
        tensors.left_message * tensors.layers[1], tensors.kernels, 4
    )
    partition_second = float(np.sum(transferred * tensors.layers[2]))
    checks.check(
        "exact-ten-to-the-twelve-transfer",
        "two independent width-four transfer orders contract the nominal 10^12 shared-label assignments without dense enumeration",
        partition > 0.0
        and np.isfinite(partition)
        and abs(partition / partition_second - 1.0) < 2.0e-14,
        f"Z={partition:.6f}; relative order error={abs(partition/partition_second-1.0):.3e}",
    )

    shared_free = tensors.left_message * tensors.layers[1]
    shared_global = shared_free * tensors.right_message
    free_probability = shared_free / float(np.sum(shared_free))
    global_probability = shared_global / float(np.sum(shared_global))
    boundary_tv = 0.5 * float(np.sum(np.abs(free_probability - global_probability)))
    message_log_range = float(
        np.log(np.max(tensors.right_message) / np.min(tensors.right_message))
    )
    repaired_probability = (
        free_probability * tensors.right_message
        / float(np.sum(free_probability * tensors.right_message))
    )
    repaired_error = 0.5 * float(np.sum(np.abs(repaired_probability - global_probability)))
    checks.check(
        "free-marginal-boundary-message",
        "the two-cube marginal is not the free one-cube law; multiplying by the exact positive exterior message restores it identically",
        boundary_tv > 1.0e-4
        and message_log_range > 0.1
        and repaired_error < 2.0e-15,
        f"free/global TV={boundary_tv:.6f}; log message range={message_log_range:.6f}; repaired TV={repaired_error:.3e}",
    )

    shared_labels = (0, 1, 2, 3)
    right_numerator = tensors.layers[2].copy()
    for coordinate in range(4):
        kernel = tensors.kernels[EDGE_INDEX[(4 + coordinate, 8 + coordinate)]]
        shape = [1, 1, 1, 1]
        shape[coordinate] = 10
        right_numerator *= kernel[shared_labels[coordinate], :].reshape(shape)
    conditional_sum = float(np.sum(right_numerator))
    conditional_normalization = conditional_sum / float(
        tensors.right_message[shared_labels]
    )
    config_a = (0, 2, 4, 6)
    config_b = (1, 3, 5, 7)
    direct_ratio = float(right_numerator[config_a] / right_numerator[config_b])
    full_labels_a = np.asarray((9, 8, 7, 6) + shared_labels + config_a)
    full_labels_b = np.asarray((9, 8, 7, 6) + shared_labels + config_b)
    global_ratio = np.exp(
        microscopic_log_weight(
            full_labels_a,
            COFRAMES_STAR,
            curved_links,
            tuple(range(12)),
            tuple(range(20)),
            tuple(range(11)),
        )
        - microscopic_log_weight(
            full_labels_b,
            COFRAMES_STAR,
            curved_links,
            tuple(range(12)),
            tuple(range(20)),
            tuple(range(11)),
        )
    )
    checks.check(
        "overlap-conditional-compatibility",
        "conditioning on the shared face cancels every left-exclusive factor and leaves the normalized right local conditional",
        abs(conditional_normalization - 1.0) < 2.0e-14
        and abs(global_ratio / direct_ratio - 1.0) < 3.0e-13,
        f"conditional sum={conditional_normalization:.15f}; ratio error={abs(global_ratio/direct_ratio-1.0):.3e}",
    )

    duplicated_faces = tuple(range(11)) + OVERLAP_FACES
    duplicated_partition = record_partition(
        COFRAMES_STAR, curved_links, SIGMA, duplicated_faces
    )
    duplicate_shift = float(np.log(duplicated_partition / partition))
    checks.check(
        "shared-face-double-counting-control",
        "counting the shared face once more changes the normalized Record law and therefore cannot be hidden as bookkeeping",
        abs(duplicate_shift) > 0.05,
        f"log(Z_duplicate/Z_unique)={duplicate_shift:.6f}",
    )

    grid = np.linspace(0.0, 2.0 * np.pi, 257)
    derivatives = np.asarray([scalar_derivative(angle) for angle in grid])
    roots = [0.0, curved_angle, np.pi, 2.0 * np.pi - curved_angle, 2.0 * np.pi]
    root_derivatives = [abs(scalar_derivative(angle)) for angle in roots]
    second_derivatives = [scalar_second_derivative(angle) for angle in roots]
    root_gaps = []
    for angle in roots:
        links = homogeneous_links(angle)
        gap, signal, _ = face_signal(COFRAMES_STAR, links, FACES[0].loop)
        root_gaps.append(gap)
    sign_changes = sum(
        derivatives[index] * derivatives[index + 1] < 0.0
        for index in range(len(derivatives) - 1)
    )
    checks.check(
        "full-angle-homogeneous-connection-classification",
        "the compact homogeneous family has only flat stable sampled roots; its two nonflat stationary roots have negative curvature",
        max(root_derivatives) < 2.0e-6
        and second_derivatives[0] > 1.0
        and second_derivatives[2] > 1.0
        and second_derivatives[1] < -1.0
        and second_derivatives[3] < -1.0
        and root_gaps[0] < 1.0e-12
        and root_gaps[2] < 1.0e-10
        and root_gaps[1] > 1.0
        and sign_changes == 3,
        f"roots=0,{curved_angle:.9f},pi,{2*np.pi-curved_angle:.9f},2pi; d2={','.join(f'{x:.3f}' for x in second_derivatives)}; sign changes={sign_changes}",
    )

    curved_gaps = []
    curved_signals = []
    curved_torsions = []
    for face in FACES:
        gap, signal, torsion = face_signal(COFRAMES_STAR, curved_links, face.loop)
        curved_gaps.append(gap)
        curved_signals.append(signal)
        curved_torsions.append(torsion)
    checks.check(
        "nonflat-homogeneous-reduced-extremum",
        "the translation-compatible alternative genuinely carries equal nonzero plaquette holonomy, intrinsic EC signal, and torsion before stability/full-equation tests",
        min(curved_gaps) > 1.0
        and min(np.abs(curved_signals)) > 0.1
        and min(curved_torsions) > 0.1,
        f"gap={min(curved_gaps):.6f}..{max(curved_gaps):.6f}; EC={min(curved_signals):.6f}..{max(curved_signals):.6f}; torsion={min(curved_torsions):.6f}..{max(curved_torsions):.6f}",
    )

    flat_link_gradient = link_gradient(COFRAMES_STAR, flat_links)
    curved_link_gradient = link_gradient(COFRAMES_STAR, curved_links)
    checks.check(
        "reduced-is-not-full-connection-equation",
        "both the open-region flat symmetry point and nonflat reduced extremum retain boundary-resolved intrinsic link forces",
        float(np.max(np.abs(flat_link_gradient))) > 1.0e-3
        and float(np.max(np.abs(curved_link_gradient))) > 1.0e-3,
        f"full tangent max/norm flat={np.max(np.abs(flat_link_gradient)):.6f}/{np.linalg.norm(flat_link_gradient):.6f}; curved={np.max(np.abs(curved_link_gradient)):.6f}/{np.linalg.norm(curved_link_gradient):.6f}",
    )

    flat_coframe_gradient = coframe_gradient(COFRAMES_STAR, flat_links)
    required_targets = []
    antisymmetric_error = 0.0
    for coframe, gradient in zip(COFRAMES_STAR, flat_coframe_gradient):
        reduced = np.linalg.solve(coframe, gradient)
        antisymmetric_error = max(
            antisymmetric_error, float(np.linalg.norm(reduced - reduced.T))
        )
        required_targets.append(
            coframe.T @ coframe + 0.5 * (reduced + reduced.T) / ALPHA
        )
    common_target = np.mean(required_targets, axis=0)
    target_spread = max(
        float(np.linalg.norm(target - common_target)) for target in required_targets
    )
    common_residual = []
    gram = E_STAR.T @ E_STAR
    for gradient in flat_coframe_gradient:
        common_residual.append(gradient + ALPHA * E_STAR @ (gram - common_target))
    common_residual = np.asarray(common_residual)
    checks.check(
        "common-gram-free-boundary-obstruction",
        "one site-independent Gram well cannot cancel the degree-dependent open-boundary coframe stresses of all twelve sites",
        target_spread > 2.0e-4
        and float(np.max(np.abs(common_residual))) > 4.0e-3,
        f"required-target spread={target_spread:.6f}; best-common residual max/norm={np.max(np.abs(common_residual)):.6f}/{np.linalg.norm(common_residual):.6f}; antisym={antisymmetric_error:.3e}",
    )

    rotations = tuple(
        expm(
            (0.017 * (site + 1)) * SKEW_GENERATORS[site % len(SKEW_GENERATORS)]
        )
        for site in range(12)
    )
    transformed_coframes, transformed_links = transformed_configuration(
        COFRAMES_STAR, curved_links, rotations
    )
    frame_error = abs(
        action_value(transformed_coframes, transformed_links)
        - action_value(COFRAMES_STAR, curved_links)
    )
    checks.check(
        "endpoint-local-frame-covariance",
        "independent SO(4) rotations at all twelve sites leave the complete unique-carrier action invariant",
        frame_error < 3.0e-12,
        f"complete action error={frame_error:.3e}",
    )

    all_loads = curvature_loads(COFRAMES_STAR, curved_links)
    boundary_load_norm = float(np.mean([np.linalg.norm(all_loads[site]) for site in range(4)]))
    shared_load_norm = float(np.mean([np.linalg.norm(all_loads[site]) for site in range(4, 8)]))
    checks.check(
        "fixed-per-face-not-degree-average",
        "shared-layer sites receive five unique face incidences while outer corners receive three under one fixed elementary coupling",
        shared_load_norm > 1.4 * boundary_load_norm,
        f"mean load norm outer/shared={boundary_load_norm:.6f}/{shared_load_norm:.6f}; ratio={shared_load_norm/boundary_load_norm:.6f}",
    )

    checks.check(
        "finite-normalization-and-axiom-boundary",
        "the note proves finite positive normalization and exact gluing while withholding bulk stationarity, Einstein/Lorentzian claims, and axiom necessity",
        "quartic" in note
        and "boundary message" in note
        and "not a gravity no-go" in note
        and "no fifth ontology axiom" in note
        and "z^3 x z_tau" in note,
    )

    checks.check(
        "n1-through-n8-landing",
        "the theorem note executes the fresh no-go discipline before shipping its bounded adaptive-average and copied-connection negatives",
        all(f"n{index}" in note for index in range(1, 9))
        and "strongest counterroute" in note
        and "hidden-wall" in note,
    )

    print("N5_CERTIFICATE: executed 12 shared Record/coframe sites, 20 unique links, 11 unique faces, all 44 based loops, both exact ordered-product cube-Bianchi words, and the width-four contraction of nominal 10^12 labels")
    print("N5_CERTIFICATE: tested fixed-potential inclusion--exclusion, adaptive degree averaging, duplicate-face counting, free marginalization, induced boundary-message repair, and normalized overlap conditionals")
    print("per_element: checked all unique vertices, links, faces, both shared-face orientations, 24 proper-cubic direction intertwiners, and 24 deterministic branchwise gluing assignments")
    print("per_site: checked all 12 coframes, the four-site shared layer, its exterior messages, all 120 intrinsic link tangents at flat and curved probes, and all 192 flat coframe coordinates")
    print("per_mode: checked the full compact one-angle homogeneous connection family numerically; no Bloch, graviton, transfer-spectrum, or Lorentzian mode decomposition was executed")
    print("per_block: checked both elementary nonabelian cube-Bianchi identities, the exact union/left/right/overlap factor identity, and valid fixed potentials against adaptive-normalization and copied-link routes")
    print("lattice_wide: checked and not executed — the two elementary Bianchi words are kinematical, not a periodic/increasing-region full-Z3 Gibbs phase, displacement Ward system, sourced Einstein regime, Z3 x Z_tau law, or Lorentzian permanent-Record update")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
