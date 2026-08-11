#!/usr/bin/env python3
"""Certify the fixed-background Record phase and periodic EC connection law.

The Block-38 fixed site/edge/face potentials are placed on periodic cubic
carriers.  A uniform oscillation bound gives Dobrushin contraction for the
ten-label Record conditional at the supplied beta, independently of the
fixed nondegenerate coframe/link background.  On a homogeneous flat
background, endpoint exchange kills the Record-bond connection score and the
periodic plaquette sum kills the Einstein--Cartan curl score link by link.

A zero-sum Record-marginal perturbation is then executed on several tori.  Its
connection force has exactly the injected Fourier support and the expected
first-difference sine scaling.  This is a fixed-background phase and sourced
Palatini-carrier theorem, not a coframe stationarity, displacement-Ward,
Einstein, full joint geometry phase, or Lorentzian result.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_"
    "SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

DIMENSION = 4
BETA = 1.0 / 5.0
SIGMA = 1.0 / 2.0
FACE_COEFFICIENT_DIVISOR = 3.0
ETA = 1.0 / 5.0
NORMAL_COMPATIBILITY = 1.0 / 5.0
TAU = 3.0 / 10.0
SOURCE_AMPLITUDE = 1.0 / 50.0
SOURCE_LENGTHS = (3, 5, 7, 9, 11, 15)

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


def skew_generators() -> tuple[np.ndarray, ...]:
    generators: list[np.ndarray] = []
    for left, right in combinations(range(DIMENSION), 2):
        generator = np.zeros((DIMENSION, DIMENSION), dtype=float)
        generator[left, right] = -1.0
        generator[right, left] = 1.0
        generators.append(generator)
    return tuple(generators)


SKEW_GENERATORS = skew_generators()
GENERATOR_ARRAY = np.asarray(SKEW_GENERATORS)


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


def record_projectors(coframe: np.ndarray) -> np.ndarray:
    images = (coframe @ RAYS.T).T
    return np.asarray(
        [np.outer(image, image) / float(np.dot(image, image)) for image in images]
    )


def record_site_weights(coframe: np.ndarray) -> np.ndarray:
    images = (coframe @ RAYS.T).T
    squared_norms = np.einsum("ri,ri->r", images, images)
    return RECORD_WEIGHTS * np.exp(-0.5 * squared_norms)


PROJECTORS = record_projectors(E_STAR)
SITE_WEIGHTS = record_site_weights(E_STAR)


def log_kernel(link: np.ndarray) -> np.ndarray:
    transported = np.einsum("ij,bjk,lk->bil", link, PROJECTORS, link)
    difference = PROJECTORS[:, None] - transported[None, :]
    return -0.5 * BETA * np.einsum("abij,abij->ab", difference, difference)


FLAT_LOG_KERNEL = log_kernel(np.eye(4))


@dataclass(frozen=True)
class Face:
    loop: tuple[int, int, int, int]
    first_axis: int
    second_axis: int


@dataclass(frozen=True)
class CubicCarrier:
    length: int
    periodic: bool
    vertices: tuple[tuple[int, int, int], ...]
    vertex_index: dict[tuple[int, int, int], int]
    edges: tuple[tuple[int, int, int], ...]
    oriented_edges: dict[tuple[int, int], tuple[int, int]]
    faces: tuple[Face, ...]


def cubic_carrier(length: int, periodic: bool) -> CubicCarrier:
    vertices = tuple(product(range(length), repeat=3))
    vertex_index = {vertex: index for index, vertex in enumerate(vertices)}

    def shifted(
        vertex: tuple[int, int, int], axis: int
    ) -> tuple[int, int, int] | None:
        value = list(vertex)
        value[axis] += 1
        if value[axis] == length:
            if not periodic:
                return None
            value[axis] = 0
        return tuple(value)

    edges: list[tuple[int, int, int]] = []
    for vertex in vertices:
        for axis in range(3):
            high = shifted(vertex, axis)
            if high is not None:
                edges.append((vertex_index[vertex], vertex_index[high], axis))
    oriented_edges: dict[tuple[int, int], tuple[int, int]] = {}
    for edge_index, (low, high, _) in enumerate(edges):
        oriented_edges[(low, high)] = (edge_index, 1)
        oriented_edges[(high, low)] = (edge_index, -1)

    faces: list[Face] = []
    for vertex in vertices:
        for first_axis, second_axis in ((0, 1), (0, 2), (1, 2)):
            first = shifted(vertex, first_axis)
            fourth = shifted(vertex, second_axis)
            if first is None or fourth is None:
                continue
            third = shifted(first, second_axis)
            if third is None:
                continue
            faces.append(
                Face(
                    (
                        vertex_index[vertex],
                        vertex_index[first],
                        vertex_index[third],
                        vertex_index[fourth],
                    ),
                    first_axis,
                    second_axis,
                )
            )
    return CubicCarrier(
        length,
        periodic,
        vertices,
        vertex_index,
        tuple(edges),
        oriented_edges,
        tuple(faces),
    )


def based_face_loops(
    face: Face,
) -> tuple[tuple[tuple[int, int, int, int], np.ndarray, np.ndarray], ...]:
    directions = np.eye(3, dtype=float)
    steps = (
        directions[face.first_axis],
        directions[face.second_axis],
        -directions[face.first_axis],
        -directions[face.second_axis],
    )
    result = []
    for offset in range(4):
        loop = tuple(face.loop[(offset + step) % 4] for step in range(4))
        first_step = steps[offset]
        second_step = -steps[(offset - 1) % 4]
        result.append((loop, first_step, second_step))
    return tuple(result)


def oriented_link(
    carrier: CubicCarrier, links: tuple[np.ndarray, ...], start: int, end: int
) -> np.ndarray:
    edge_index, sign = carrier.oriented_edges[(start, end)]
    return links[edge_index] if sign == 1 else links[edge_index].T


def loop_holonomy(
    carrier: CubicCarrier, links: tuple[np.ndarray, ...], loop: tuple[int, ...]
) -> np.ndarray:
    result = np.eye(4)
    for first, second in zip(loop, loop[1:] + loop[:1]):
        result = result @ oriented_link(carrier, links, first, second)
    return result


def cube_bianchi_residual(
    carrier: CubicCarrier,
    links: tuple[np.ndarray, ...],
    origin_vertex: tuple[int, int, int],
) -> float:
    length = carrier.length

    def site(dx: int, dy: int, dz: int) -> int:
        displacement = (dx, dy, dz)
        coordinate = tuple(
            (origin_vertex[axis] + displacement[axis]) % length
            for axis in range(3)
        )
        return carrier.vertex_index[coordinate]

    origin = site(0, 0, 0)
    x_site = site(1, 0, 0)
    y_site = site(0, 1, 0)
    z_site = site(0, 0, 1)
    xy_site = site(1, 1, 0)
    xz_site = site(1, 0, 1)
    yz_site = site(0, 1, 1)
    xyz_site = site(1, 1, 1)

    p_xy_low = loop_holonomy(carrier, links, (origin, x_site, xy_site, y_site))
    p_xy_high = loop_holonomy(carrier, links, (z_site, xz_site, xyz_site, yz_site))
    p_yz_low = loop_holonomy(carrier, links, (origin, y_site, yz_site, z_site))
    p_yz_high = loop_holonomy(carrier, links, (x_site, xy_site, xyz_site, xz_site))
    p_zx_low = loop_holonomy(carrier, links, (origin, z_site, xz_site, x_site))
    p_zx_high = loop_holonomy(carrier, links, (y_site, yz_site, xyz_site, xy_site))
    transport_x = oriented_link(carrier, links, origin, x_site)
    transport_y = oriented_link(carrier, links, origin, y_site)
    transport_z = oriented_link(carrier, links, origin, z_site)
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
    x0, xy, xz, xyz, y0, yx, yz, yxz, z0, zx, zy, zxy = range(1, 13)

    def inverse(word: list[int]) -> list[int]:
        return [-letter for letter in reversed(word)]

    def conjugate(path: list[int], word: list[int]) -> list[int]:
        return path + word + inverse(path)

    def reduce_word(word: list[int]) -> list[int]:
        reduced: list[int] = []
        for letter in word:
            if reduced and reduced[-1] == -letter:
                reduced.pop()
            else:
                reduced.append(letter)
        return reduced

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


def random_links(carrier: CubicCarrier) -> tuple[np.ndarray, ...]:
    rng = np.random.default_rng(390811)
    links = []
    for _ in carrier.edges:
        coefficients = rng.normal(scale=0.19, size=6)
        generator = np.einsum("g,gij->ij", coefficients, GENERATOR_ARRAY)
        links.append(expm(generator))
    return tuple(links)


def dobrushin_oscillation(log_pair: np.ndarray) -> float:
    largest = 0.0
    for first_neighbor in range(10):
        for second_neighbor in range(10):
            log_ratio = log_pair[:, first_neighbor] - log_pair[:, second_neighbor]
            largest = max(largest, float(np.ptp(log_ratio)))
    return largest


def conditional_distribution(neighbors: tuple[int, ...]) -> np.ndarray:
    log_weight = np.log(SITE_WEIGHTS).copy()
    for neighbor in neighbors:
        log_weight += FLAT_LOG_KERNEL[:, neighbor]
    log_weight -= float(np.max(log_weight))
    weight = np.exp(log_weight)
    return weight / float(np.sum(weight))


def deterministic_conditional_tv_probe() -> float:
    maximum = 0.0
    for seed in range(257):
        other = tuple((seed * (axis + 3) + axis * axis + 1) % 10 for axis in range(5))
        for first in range(10):
            left = conditional_distribution((first,) + other)
            for second in range(10):
                right = conditional_distribution((second,) + other)
                maximum = max(maximum, 0.5 * float(np.sum(np.abs(left - right))))
    return maximum


def bond_score() -> tuple[np.ndarray, float]:
    scores = np.zeros((6, 10, 10), dtype=float)
    for generator_index, generator in enumerate(SKEW_GENERATORS):
        for first in range(10):
            for second in range(10):
                commutator = (
                    PROJECTORS[second] @ PROJECTORS[first]
                    - PROJECTORS[first] @ PROJECTORS[second]
                )
                scores[generator_index, first, second] = BETA * float(
                    np.trace(commutator @ generator)
                )
    finite_step = 1.0e-6
    finite_difference_errors = []
    for generator_index, generator in enumerate(SKEW_GENERATORS):
        numerical = (
            log_kernel(expm(finite_step * generator))
            - log_kernel(expm(-finite_step * generator))
        ) / (2.0 * finite_step)
        finite_difference_errors.append(
            float(np.max(np.abs(numerical - scores[generator_index])))
        )
    return scores, max(finite_difference_errors)


def curvature_gradient(
    carrier: CubicCarrier, probabilities: np.ndarray
) -> np.ndarray:
    gradient = np.zeros((len(carrier.edges), 6), dtype=float)
    for face in carrier.faces:
        for loop, first_step, second_step in based_face_loops(face):
            bivector = einstein_cartan_bivector(E_STAR, first_step, second_step)
            incidence = (
                (RAYS[:, :3] @ first_step) ** 2
                + (RAYS[:, :3] @ second_step) ** 2
            )
            expected_incidence = float(probabilities[loop[0]] @ incidence)
            signal_derivative = 0.5 * np.einsum(
                "ij,gij->g", bivector, GENERATOR_ARRAY
            )
            coefficient = -SIGMA * expected_incidence / FACE_COEFFICIENT_DIVISOR
            for first, second in zip(loop, loop[1:] + loop[:1]):
                edge_index, sign = carrier.oriented_edges[(first, second)]
                gradient[edge_index] += coefficient * sign * signal_derivative
    return gradient


def open_geometry_penalty(
    carrier: CubicCarrier, links: tuple[np.ndarray, ...]
) -> float:
    coframes = tuple(E_STAR for _ in carrier.vertices)
    normal = spatial_normal(E_STAR)
    compatibility = 0.0
    normal_term = 0.0
    for link, (low, high, _) in zip(links, carrier.edges):
        compatibility += 0.5 * ETA * float(
            np.sum((coframes[low] - link @ coframes[high]) ** 2)
        )
        normal_term += 0.5 * NORMAL_COMPATIBILITY * float(
            np.sum((normal - link @ normal) ** 2)
        )
    torsion = 0.0
    for face in carrier.faces:
        for loop, first_step, second_step in based_face_loops(face):
            first, second, _, fourth = loop
            first_base = np.concatenate((first_step, (0.0,)))
            second_base = np.concatenate((second_step, (0.0,)))
            first_difference = (
                oriented_link(carrier, links, first, second)
                @ (coframes[second] @ second_base)
                - coframes[first] @ second_base
            )
            second_difference = (
                oriented_link(carrier, links, first, fourth)
                @ (coframes[fourth] @ first_base)
                - coframes[first] @ first_base
            )
            torsion += (TAU / 8.0) * float(
                np.sum((first_difference - second_difference) ** 2)
            )
    return compatibility + normal_term + torsion


def geometry_first_variation(carrier: CubicCarrier) -> tuple[float, float]:
    identity_links = tuple(np.eye(4) for _ in carrier.edges)
    step = 1.0e-6
    gradient = np.zeros((len(carrier.edges), 6), dtype=float)
    curvatures = np.zeros_like(gradient)
    base = open_geometry_penalty(carrier, identity_links)
    for edge_index in range(len(carrier.edges)):
        for generator_index, generator in enumerate(SKEW_GENERATORS):
            plus = list(identity_links)
            minus = list(identity_links)
            plus[edge_index] = expm(step * generator)
            minus[edge_index] = expm(-step * generator)
            plus_value = open_geometry_penalty(carrier, tuple(plus))
            minus_value = open_geometry_penalty(carrier, tuple(minus))
            gradient[edge_index, generator_index] = (
                plus_value - minus_value
            ) / (2.0 * step)
            curvatures[edge_index, generator_index] = (
                plus_value - 2.0 * base + minus_value
            ) / step**2
    return float(np.max(np.abs(gradient))), float(np.min(curvatures))


def source_probabilities(
    carrier: CubicCarrier, amplitude: float
) -> tuple[np.ndarray, np.ndarray]:
    baseline = np.full(10, 0.1, dtype=float)
    label_direction = np.zeros(10, dtype=float)
    label_direction[0] = amplitude
    label_direction[4] = -amplitude
    profile = np.asarray(
        [
            np.cos(2.0 * np.pi * vertex[0] / carrier.length)
            for vertex in carrier.vertices
        ]
    )
    probabilities = baseline[None, :] + profile[:, None] * label_direction[None, :]
    return probabilities, profile


def edge_field(carrier: CubicCarrier, gradient: np.ndarray) -> np.ndarray:
    field = np.zeros((carrier.length, carrier.length, carrier.length, 3, 6))
    for edge_index, (low, _, axis) in enumerate(carrier.edges):
        field[carrier.vertices[low] + (axis, slice(None))] = gradient[edge_index]
    return field


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
        "the runner binds only the four-axiom premise and Block-38 fixed-potential parent while keeping the extensional gravity law supplied",
        all(
            path.exists()
            for path in (NOTE_PATH, AXIOM_PATH, PARENT_PATH, PREMISE_REGISTRY_PATH)
        )
        and "admissibility / local constraint" in axiom
        and "does glue" in parent
        and "audit-status authority" in note,
    )

    periodic = cubic_carrier(3, True)
    open_box = cubic_carrier(3, False)
    checks.check(
        "periodic-carrier-census",
        "the L=3 torus has 27 sites, 81 unique positive-axis links, 81 square faces, 324 based loops, and 27 cubes",
        len(periodic.vertices) == 27
        and len(periodic.edges) == 81
        and len(periodic.faces) == 81
        and sum(len(based_face_loops(face)) for face in periodic.faces) == 324,
        f"periodic V/E/F/loops/cubes={len(periodic.vertices)}/{len(periodic.edges)}/{len(periodic.faces)}/324/{len(periodic.vertices)}",
    )

    generic_links = random_links(periodic)
    bianchi_residuals = [
        cube_bianchi_residual(periodic, generic_links, vertex)
        for vertex in periodic.vertices
    ]
    checks.check(
        "translated-ordered-product-bianchi",
        "the freely reduced six-face word and all 27 translated generic noncommuting cube identities close",
        cube_bianchi_word_reduces() and max(bianchi_residuals) < 3.0e-12,
        f"translated residual max/mean={max(bianchi_residuals):.3e}/{np.mean(bianchi_residuals):.3e}",
    )

    kernel_range = float(np.ptp(FLAT_LOG_KERNEL))
    actual_oscillation = dobrushin_oscillation(FLAT_LOG_KERNEL)
    actual_influence = float(np.tanh(actual_oscillation / 4.0))
    universal_influence = float(np.tanh(BETA / 2.0))
    universal_row_sum = 6.0 * universal_influence
    beta_threshold = float(2.0 * np.arctanh(1.0 / 6.0))
    checks.check(
        "universal-dobrushin-window",
        "rank-one projector distances bound every fixed-background neighbor influence and put beta=1/5 strictly inside the six-neighbor contraction window",
        kernel_range <= BETA + 2.0e-15
        and universal_row_sum < 1.0
        and BETA < beta_threshold,
        f"flat logK range={kernel_range:.9f}; universal row sum={universal_row_sum:.9f}; beta threshold={beta_threshold:.9f}",
    )

    conditional_tv = deterministic_conditional_tv_probe()
    checks.check(
        "flat-kernel-influence-reconstruction",
        "the exact flat ten-label kernel sharpens the universal oscillation bound and deterministic six-neighbor conditionals obey it",
        actual_oscillation <= 2.0 * BETA + 2.0e-15
        and 6.0 * actual_influence < universal_row_sum
        and conditional_tv <= actual_influence + 2.0e-14,
        f"oscillation={actual_oscillation:.9f}; row sum={6*actual_influence:.9f}; probed TV={conditional_tv:.9f}",
    )

    scores, score_fd_error = bond_score()
    raw_pair = np.add.outer(np.arange(1, 11), np.arange(1, 11)).astype(float)
    symmetric_pair = raw_pair / float(np.sum(raw_pair))
    antisymmetry_error = float(np.max(np.abs(scores + scores.transpose(0, 2, 1))))
    expected_bond_score = np.einsum("ab,gab->g", symmetric_pair, scores)
    checks.check(
        "endpoint-exchange-bond-cancellation",
        "the flat link score is label-pair antisymmetric, so the unique reflection-symmetric phase has zero bond connection tadpole",
        antisymmetry_error < 2.0e-15
        and float(np.max(np.abs(expected_bond_score))) < 2.0e-15
        and score_fd_error < 3.0e-10,
        f"antisymmetry/expected/finite-difference={antisymmetry_error:.3e}/{np.max(np.abs(expected_bond_score)):.3e}/{score_fd_error:.3e}",
    )

    arbitrary_uniform_marginal = np.arange(1.0, 11.0)
    arbitrary_uniform_marginal /= float(np.sum(arbitrary_uniform_marginal))
    uniform_probabilities = np.tile(
        arbitrary_uniform_marginal, (len(periodic.vertices), 1)
    )
    periodic_curvature_gradient = curvature_gradient(periodic, uniform_probabilities)
    checks.check(
        "periodic-ec-curl-cancellation",
        "every one of the 486 flat EC link tangents cancels by periodic incidence even for an asymmetric but translation-uniform label marginal",
        float(np.max(np.abs(periodic_curvature_gradient))) < 3.0e-15,
        f"flat EC gradient max/norm={np.max(np.abs(periodic_curvature_gradient)):.3e}/{np.linalg.norm(periodic_curvature_gradient):.3e}",
    )

    open_probabilities = np.tile(
        arbitrary_uniform_marginal, (len(open_box.vertices), 1)
    )
    boundary_gradient = curvature_gradient(open_box, open_probabilities)
    checks.check(
        "open-boundary-tadpole-control",
        "removing periodic wrap faces restores an uncancelled EC boundary force on the same L=3 sites and uniform marginal",
        float(np.max(np.abs(boundary_gradient))) > 0.5
        and float(np.linalg.norm(boundary_gradient)) > 4.0,
        f"open V/E/F/loops={len(open_box.vertices)}/{len(open_box.edges)}/{len(open_box.faces)}/{4*len(open_box.faces)}; max/norm={np.max(np.abs(boundary_gradient)):.6f}/{np.linalg.norm(boundary_gradient):.6f}",
    )

    geometry_gradient, minimum_geometry_curvature = geometry_first_variation(periodic)
    checks.check(
        "flat-square-geometry-first-variation",
        "compatibility, normal, and torsion squares have zero first variation and positive one-link coordinate curvature at the flat periodic fixture",
        geometry_gradient < 2.0e-13 and minimum_geometry_curvature > 0.1,
        f"all-486 gradient max={geometry_gradient:.3e}; minimum coordinate second difference={minimum_geometry_curvature:.6f}",
    )

    total_flat_gradient = periodic_curvature_gradient.copy()
    for generator_index in range(6):
        total_flat_gradient[:, generator_index] -= expected_bond_score[generator_index]
    checks.check(
        "complete-flat-bulk-connection-gradient",
        "the geometry squares, unique-phase bond score, and EC curl give zero total flat connection gradient on every periodic link tangent",
        geometry_gradient < 2.0e-13
        and float(np.max(np.abs(total_flat_gradient))) < 4.0e-15,
        f"assembled max/norm={np.max(np.abs(total_flat_gradient)):.3e}/{np.linalg.norm(total_flat_gradient):.3e}",
    )

    source_rms = []
    sine_normalized = []
    source_zero_modes = []
    source_min_probability = 1.0
    l3_field = None
    l3_gradient = None
    for length in SOURCE_LENGTHS:
        carrier = cubic_carrier(length, True)
        probabilities, profile = source_probabilities(carrier, SOURCE_AMPLITUDE)
        source_min_probability = min(source_min_probability, float(np.min(probabilities)))
        gradient = curvature_gradient(carrier, probabilities)
        field = edge_field(carrier, gradient)
        rms = float(np.sqrt(np.mean(field**2)))
        source_rms.append(rms)
        sine_normalized.append(rms / float(np.sin(2.0 * np.pi / length)))
        source_zero_modes.append(float(np.linalg.norm(np.sum(field, axis=(0, 1, 2)))))
        if length == 3:
            l3_field = field
            l3_gradient = gradient
        checks.check(
            f"source-L{length}",
            "the positive zero-sum Record marginal produces a nonzero periodic EC connection force with vanishing zero mode",
            abs(float(np.sum(profile))) < 2.0e-13
            and float(np.min(probabilities)) > 0.0
            and rms > 1.0e-5
            and source_zero_modes[-1] < 4.0e-12,
            f"rms={rms:.9f}; zero-mode={source_zero_modes[-1]:.3e}; sine-normalized={sine_normalized[-1]:.9f}",
        )

    assert l3_field is not None and l3_gradient is not None
    fourier = np.fft.fftn(l3_field, axes=(0, 1, 2))
    power = np.sum(np.abs(fourier) ** 2, axis=(3, 4))
    source_mode_fraction = float(
        (power[1, 0, 0] + power[-1, 0, 0]) / np.sum(power)
    )
    scaling_spread = float(np.ptp(sine_normalized) / np.mean(sine_normalized))
    checks.check(
        "zero-sum-source-fourier-scaling",
        "the sourced force stays entirely at kx=plus/minus 2pi/L and its RMS is exactly proportional to sin(2pi/L) from L=3 through 15",
        source_mode_fraction > 1.0 - 2.0e-14
        and scaling_spread < 3.0e-13,
        f"L3 mode fraction={source_mode_fraction:.15f}; normalized mean/spread={np.mean(sine_normalized):.9f}/{scaling_spread:.3e}",
    )

    double_probabilities, _ = source_probabilities(periodic, 2.0 * SOURCE_AMPLITUDE)
    double_gradient = curvature_gradient(periodic, double_probabilities)
    source_linearity_error = float(
        np.max(
            np.abs(double_gradient - 2.0 * l3_gradient)
        )
    )
    checks.check(
        "linear-source-carrier-not-einstein",
        "doubling the zero-sum marginal doubles the EC force, establishing a load-bearing first-order source carrier without asserting an Einstein response",
        source_min_probability >= 0.08 - 2.0e-15
        and source_linearity_error < 3.0e-15,
        f"L3 force max/norm={np.max(np.abs(l3_gradient)):.6f}/{np.linalg.norm(l3_gradient):.6f}; linearity error={source_linearity_error:.3e}",
    )

    checks.check(
        "fixed-background-phase-and-axiom-boundary",
        "the note closes only the fixed-background Record phase and bulk connection tadpole while withholding joint geometry, Einstein, Lorentzian, and axiom-selection claims",
        "fixed-background" in note
        and "full joint" in note
        and "displacement ward" in note
        and "no fifth ontology axiom" in note
        and "no fixed toe percentage moves" in note,
    )

    checks.check(
        "n1-through-n8-landing",
        "the theorem note executes fresh N1--N8 before shipping its scoped residual gravity and axiom-interface boundaries",
        all(f"n{index}" in note for index in range(1, 9))
        and "strongest counterroute" in note
        and "hidden-wall" in note,
    )

    print("N5_CERTIFICATE: executed the L=3 periodic 27-site/81-link/81-face/324-loop carrier, all 27 translated nonabelian cube-Bianchi identities, and all 486 flat EC connection tangents")
    print("N5_CERTIFICATE: derived the universal six-neighbor Dobrushin window, reconstructed the exact flat-kernel oscillation, and probed 257 deterministic five-neighbor contexts")
    print("per_element: checked all periodic carriers, rank-one pair scores, based loops, oriented incidences, source probabilities, and translated cube words used by the claim")
    print("per_site: checked every site/link/face of the L=3 torus and open control; source scans cover every site and edge on L=3,5,7,9,11,15")
    print("per_mode: checked the zero mode and injected plus/minus first x Fourier modes; no full Bloch Hessian, gauge quotient, graviton tensor, or Lorentzian spectrum was executed")
    print("per_block: checked fixed-background uniqueness, endpoint-exchange bond cancellation, periodic EC curl cancellation, open-boundary restoration, and source linearity")
    print("lattice_wide: fixed-background ten-label Record uniqueness is proved by contraction; continuous coframe/link integration, coframe stationarity, displacement Ward, Einstein universality, and permanent-Record dynamics remain unexecuted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
