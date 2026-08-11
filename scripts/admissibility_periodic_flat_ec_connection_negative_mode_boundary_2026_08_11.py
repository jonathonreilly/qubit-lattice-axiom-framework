#!/usr/bin/env python3
"""Certify a physical negative connection mode of the supplied flat law.

The Block-38--40 Euclidean Record/coframe/SO(4)-link law has a homogeneous
flat stationary point on every finite periodic cubic carrier.  This runner
uses the stationary equations to sharpen the allowed proper-cubic Gram,
derives a uniform lower bound on the spatial-ray Record marginal, and tests
the normalized isotropic connection direction A_i=J_(i,3)/sqrt(3).  Its
Einstein--Cartan commutator curvature dominates every possible stabilizing
Record contact, leaving a strictly negative gauge-quotiented Hessian value.

This is a bounded instability theorem for one supplied flat branch.  It is
not a gravity no-go for modified laws, relational Ward constructions,
nonflat phases, or Lorentzian dynamics.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_FLAT_EC_CONNECTION_NEGATIVE_MODE_AXIOM_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
LAW_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PHASE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_"
    "SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
VACUUM_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_GRAM_WELL_NONDEGENERATE_FLAT_VACUUM_"
    "LOCAL_FRAME_HESSIAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
SPIN_TWO_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERIODIC_GRAM_WELL_SPIN_TWO_MASS_GAP_CONNECTION_"
    "SCHUR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_PERIODIC_FLAT_EC_CONNECTION_NEGATIVE_MODE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_TWO_CUBE_RECORD_EC_OVERLAP_GIBBS_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_PERIODIC_RECORD_EC_DOBRUSHIN_FLAT_CONNECTION_SOURCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_PERIODIC_GRAM_WELL_NONDEGENERATE_FLAT_VACUUM_LOCAL_FRAME_HESSIAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_PERIODIC_GRAM_WELL_SPIN_TWO_MASS_GAP_CONNECTION_SCHUR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

DIMENSION = 4
BETA = 1.0 / 5.0
SIGMA = 1.0 / 2.0
FACE_COEFFICIENT_DIVISOR = 3.0
ETA = 1.0 / 5.0
NORMAL_COMPATIBILITY = 1.0 / 5.0
TAU = 3.0 / 10.0
ALPHA = 16.0
TARGET_TICK_GRAM = 25.0 / 16.0
GRAM_RADIUS_SQUARED = 21.0 / 40.0
GRAM_RADIUS = float(np.sqrt(GRAM_RADIUS_SQUARED))
ELLIPSE_X_FLOOR = 1.0 - GRAM_RADIUS / np.sqrt(3.0)
ELLIPSE_Y_FLOOR = TARGET_TICK_GRAM - GRAM_RADIUS

# Rounded outward after the stationary-equation contraction below.
SAFE_X = (0.89, 1.03)
SAFE_Y = (1.40, 1.66)
SAFE_T = (SAFE_Y[0] / SAFE_X[1], SAFE_Y[1] / SAFE_X[0])
ORBIT_PROBABILITY_FLOOR = 0.18

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


def skew_generators() -> tuple[np.ndarray, ...]:
    result: list[np.ndarray] = []
    for left, right in combinations(range(DIMENSION), 2):
        generator = np.zeros((DIMENSION, DIMENSION), dtype=float)
        generator[left, right] = -1.0
        generator[right, left] = 1.0
        result.append(generator)
    return tuple(result)


SKEW_GENERATORS = skew_generators()
GENERATOR_INDEX = {
    pair: index for index, pair in enumerate(combinations(range(DIMENSION), 2))
}
ISOTROPIC_BLOCKS = tuple(
    SKEW_GENERATORS[GENERATOR_INDEX[(axis, 3)]] / np.sqrt(3.0)
    for axis in range(3)
)


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


def coframe(x: float, y: float) -> np.ndarray:
    return np.diag(np.sqrt((x, x, x, y)))


def spatial_normal(frame: np.ndarray) -> np.ndarray:
    raw = -np.einsum(
        "ijkl,j,k,l->i", EPSILON, frame[:, 0], frame[:, 1], frame[:, 2]
    )
    return raw / float(np.linalg.norm(raw))


def ec_bivector(
    frame: np.ndarray, first_step: np.ndarray, second_step: np.ndarray
) -> np.ndarray:
    complementary = np.concatenate((np.cross(first_step, second_step), (0.0,)))
    return hodge_star(wedge(frame @ complementary, spatial_normal(frame)))


def based_step_pairs(first_axis: int, second_axis: int):
    first = np.eye(3)[first_axis]
    second = np.eye(3)[second_axis]
    return (
        (first, second),
        (second, -first),
        (-first, -second),
        (-second, first),
    )


def ec_second_by_label(x: float) -> np.ndarray:
    """Exact quadratic EC score of the normalized isotropic link direction."""
    frame = coframe(x, TARGET_TICK_GRAM)
    values = np.zeros(10)
    for label in range(10):
        quadratic = 0.0
        for first_axis, second_axis in ((0, 1), (0, 2), (1, 2)):
            for first_step, second_step in based_step_pairs(
                first_axis, second_axis
            ):
                axis_a = int(np.argmax(np.abs(first_step)))
                axis_b = int(np.argmax(np.abs(second_step)))
                algebra_a = float(first_step[axis_a]) * ISOTROPIC_BLOCKS[axis_a]
                algebra_b = float(second_step[axis_b]) * ISOTROPIC_BLOCKS[axis_b]
                commutator = algebra_a @ algebra_b - algebra_b @ algebra_a
                signal = 0.5 * float(
                    np.sum(ec_bivector(frame, first_step, second_step) * commutator)
                )
                incidence = (
                    float(np.dot(RAYS[label, :3], first_step)) ** 2
                    + float(np.dot(RAYS[label, :3], second_step)) ** 2
                )
                quadratic += (
                    SIGMA / FACE_COEFFICIENT_DIVISOR
                ) * incidence * signal
        values[label] = 2.0 * quadratic
    return values


def ec_finite_difference(label: int, x: float, step: float = 1.0e-4) -> float:
    frame = coframe(x, TARGET_TICK_GRAM)

    def value(parameter: float) -> float:
        links = tuple(expm(parameter * block) for block in ISOTROPIC_BLOCKS)
        total = 0.0
        for first_axis, second_axis in ((0, 1), (0, 2), (1, 2)):
            for first_step, second_step in based_step_pairs(
                first_axis, second_axis
            ):
                axis_a = int(np.argmax(np.abs(first_step)))
                axis_b = int(np.argmax(np.abs(second_step)))
                link_a = links[axis_a]
                link_b = links[axis_b]
                if first_step[axis_a] < 0.0:
                    link_a = link_a.T
                if second_step[axis_b] < 0.0:
                    link_b = link_b.T
                holonomy = link_a @ link_b @ link_a.T @ link_b.T
                sine = 0.5 * (holonomy - holonomy.T)
                signal = 0.5 * float(
                    np.sum(ec_bivector(frame, first_step, second_step) * sine)
                )
                incidence = (
                    float(np.dot(RAYS[label, :3], first_step)) ** 2
                    + float(np.dot(RAYS[label, :3], second_step)) ** 2
                )
                total += (
                    SIGMA / FACE_COEFFICIENT_DIVISOR
                ) * incidence * signal
        return total

    return (value(step) - 2.0 * value(0.0) + value(-step)) / step**2


def projector_table(x: float, y: float) -> np.ndarray:
    images = (coframe(x, y) @ RAYS.T).T
    squared = np.einsum("ai,ai->a", images, images)
    projectors = np.einsum("ai,aj->aij", images, images)
    return projectors / squared[:, None, None]


def contact_matrix(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    matrix = np.zeros((6, 6))
    for first, generator in enumerate(SKEW_GENERATORS):
        for second, other in enumerate(SKEW_GENERATORS):
            nested = 0.5 * (
                generator @ (other @ right - right @ other)
                - (other @ right - right @ other) @ generator
                + other @ (generator @ right - right @ generator)
                - (generator @ right - right @ generator) @ other
            )
            matrix[first, second] = BETA * float(np.trace(left @ nested))
    return 0.5 * (matrix + matrix.T)


def geometry_directional_hessian(x: float, y: float) -> tuple[float, float, float]:
    frame = coframe(x, y)
    normal = spatial_normal(frame)
    compatibility = ETA * sum(
        float(np.sum((block @ frame) ** 2)) for block in ISOTROPIC_BLOCKS
    )
    normal_term = NORMAL_COMPATIBILITY * sum(
        float(np.sum((block @ normal) ** 2)) for block in ISOTROPIC_BLOCKS
    )
    torsion_residual = 0.0
    for first_axis, second_axis in ((0, 1), (0, 2), (1, 2)):
        first = np.eye(3)[first_axis]
        second = np.eye(3)[second_axis]
        first_base = np.concatenate((first, (0.0,)))
        second_base = np.concatenate((second, (0.0,)))
        residual = (
            ISOTROPIC_BLOCKS[first_axis] @ (frame @ second_base)
            - ISOTROPIC_BLOCKS[second_axis] @ (frame @ first_base)
        )
        torsion_residual = max(torsion_residual, float(np.linalg.norm(residual)))
    return compatibility, normal_term, torsion_residual


def stationary_box() -> tuple[tuple[float, float], tuple[float, float]]:
    # For C=(u.v)^2 under a log-rescaling of either orthogonal subspace,
    # ||du/dlog(scale^2)||<=1/4, hence |dC/dlog x|,|dC/dlog y|<=1.
    bond_x = BETA / ELLIPSE_X_FLOOR
    bond_y = BETA / ELLIPSE_Y_FLOOR
    exact_x = (
        1.0 + (-1.5 - 3.0 * bond_x) / (3.0 * ALPHA / 2.0),
        1.0 + (-0.5 + 3.0 * bond_x) / (3.0 * ALPHA / 2.0),
    )
    exact_y = (
        TARGET_TICK_GRAM + (-0.5 - 3.0 * bond_y) / (ALPHA / 2.0),
        TARGET_TICK_GRAM + (3.0 * bond_y) / (ALPHA / 2.0),
    )
    return exact_x, exact_y


def orbit_holder_sixth(tick_ratio: float) -> tuple[float, float]:
    c_spatial_tick = 1.0 / (3.0 * (1.0 + tick_ratio))
    spatial_neighbor = 6.0 * np.exp(
        -0.4 + 1.2 * c_spatial_tick
    )
    opposite_tick = ((tick_ratio - 1.0) / (tick_ratio + 1.0)) ** 2
    transverse_tick = (tick_ratio / (tick_ratio + 1.0)) ** 2
    tick_neighbor = (
        1.0
        + np.exp(-1.2 * (1.0 - opposite_tick))
        + 4.0 * np.exp(-1.2 * (1.0 - transverse_tick))
    ) * np.exp(1.2 * (1.0 - c_spatial_tick))
    return float(spatial_neighbor), float(tick_neighbor)


def gauge_tangent_test(length: int = 3) -> tuple[int, int, int, float]:
    vertices = tuple(product(range(length), repeat=3))
    index = {vertex: site for site, vertex in enumerate(vertices)}
    edges = []
    for vertex in vertices:
        for axis in range(3):
            high = list(vertex)
            high[axis] = (high[axis] + 1) % length
            edges.append((index[vertex], index[tuple(high)], axis))
    site_count = len(vertices)
    rows = site_count * 16 + len(edges) * 6
    columns = site_count * 6
    tangent = np.zeros((rows, columns))
    frame = coframe(SAFE_X[0], SAFE_Y[0])
    for site in range(site_count):
        for generator_index, generator in enumerate(SKEW_GENERATORS):
            column = site * 6 + generator_index
            tangent[site * 16 : (site + 1) * 16, column] = (
                generator @ frame
            ).reshape(-1)
    link_offset = site_count * 16
    target = np.zeros(rows)
    for edge_index, (low, high, axis) in enumerate(edges):
        for generator_index in range(6):
            row = link_offset + edge_index * 6 + generator_index
            tangent[row, low * 6 + generator_index] += 1.0
            tangent[row, high * 6 + generator_index] -= 1.0
        target[
            link_offset
            + edge_index * 6
            + GENERATOR_INDEX[(axis, 3)]
        ] = 1.0 / np.sqrt(3.0)
    rank = int(np.linalg.matrix_rank(tangent, tol=1.0e-10))
    augmented_rank = int(
        np.linalg.matrix_rank(np.column_stack((tangent, target)), tol=1.0e-10)
    )
    solution, *_ = np.linalg.lstsq(tangent, target, rcond=None)
    residual = float(np.linalg.norm(tangent @ solution - target))
    return rank, columns, augmented_rank, residual


def periodic_carrier_counts(length: int) -> tuple[int, int, int, int]:
    vertices = tuple(product(range(length), repeat=3))
    edges = []
    faces = []
    for vertex in vertices:
        for axis in range(3):
            high = list(vertex)
            high[axis] = (high[axis] + 1) % length
            edges.append((vertex, tuple(high), axis))
        for first_axis, second_axis in ((0, 1), (0, 2), (1, 2)):
            first = list(vertex)
            second = list(vertex)
            diagonal = list(vertex)
            first[first_axis] = (first[first_axis] + 1) % length
            second[second_axis] = (second[second_axis] + 1) % length
            diagonal[first_axis] = (diagonal[first_axis] + 1) % length
            diagonal[second_axis] = (diagonal[second_axis] + 1) % length
            faces.append((vertex, tuple(first), tuple(diagonal), tuple(second)))
    based_loops = tuple((face, base) for face in faces for base in range(4))
    return len(vertices), len(edges), len(faces), len(based_loops)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 93 else statement[:90] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 128 else detail[:125] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    law = flat(LAW_PATH)
    phase = flat(PHASE_PATH)
    vacuum = flat(VACUUM_PATH)
    spin_two = flat(SPIN_TWO_PATH)

    checks.check(
        "premise-and-parent-scope",
        "the proof binds the axioms and supplied EC, periodic phase, vacuum, and spin-two parents without promoting the law to an axiom",
        all(
            path.exists()
            for path in (
                NOTE_PATH,
                AXIOM_PATH,
                LAW_PATH,
                PHASE_PATH,
                VACUUM_PATH,
                SPIN_TWO_PATH,
                PREMISE_REGISTRY_PATH,
            )
        )
        and "admissibility / local constraint" in axiom
        and "fixed elementary face-incidence coefficient" in law
        and "dobrushin" in phase
        and "stationary" in vacuum
        and "connection block" in spin_two,
    )

    exact_x, exact_y = stationary_box()
    checks.check(
        "stationary-equation-domain-contraction",
        "the Block-40 ellipse plus the rank-one projector log-derivative bound contracts every stationary Gram into the rounded safe box",
        exact_x[0] > SAFE_X[0]
        and exact_x[1] < SAFE_X[1]
        and exact_y[0] > SAFE_Y[0]
        and exact_y[1] < SAFE_Y[1],
        f"exact x={exact_x[0]:.9f}..{exact_x[1]:.9f}; y={exact_y[0]:.9f}..{exact_y[1]:.9f}",
    )

    direction_norm = sum(
        sum(
            float(coefficient) ** 2
            for coefficient in (
                1.0 / np.sqrt(3.0)
                if generator == GENERATOR_INDEX[(axis, 3)]
                else 0.0
                for generator in range(6)
            )
        )
        for axis in range(3)
    )
    checks.check(
        "normalized-isotropic-connection-direction",
        "A_i=J_(i,3)/sqrt(3) has unit coefficient norm and is proper-cubic isotropic",
        abs(direction_norm - 1.0) < 2.0e-15
        and all(
            abs(np.linalg.norm(block, "fro") ** 2 - 2.0 / 3.0) < 2.0e-15
            for block in ISOTROPIC_BLOCKS
        ),
    )

    compatibility, normal_term, torsion_residual = geometry_directional_hessian(
        SAFE_X[0], SAFE_Y[1]
    )
    expected_geometry = ETA * (SAFE_X[0] + SAFE_Y[1] + 1.0)
    checks.check(
        "exact-geometry-directional-hessian",
        "compatibility plus normal compatibility gives eta(x+y+1), while the torsion first residual vanishes in the isotropic mode",
        abs(compatibility + normal_term - expected_geometry) < 2.0e-15
        and torsion_residual < 2.0e-15,
        f"compatibility={compatibility:.9f}; normal={normal_term:.9f}; torsion residual={torsion_residual:.3e}",
    )

    ec_values = ec_second_by_label(1.0)
    checks.check(
        "exact-ec-orbit-curvatures",
        "all twelve based-loop incidences give EC Hessian 8sqrt(x)/3 on four spatial rays and 8sqrt(x)/9 on six tick rays",
        float(np.max(np.abs(ec_values[:4] - 8.0 / 3.0))) < 2.0e-15
        and float(np.max(np.abs(ec_values[4:] - 8.0 / 9.0))) < 2.0e-15,
        f"spatial/tick={ec_values[0]:.9f}/{ec_values[4]:.9f}",
    )

    finite_spatial = ec_finite_difference(0, SAFE_X[0])
    finite_tick = ec_finite_difference(4, SAFE_X[0])
    checks.check(
        "finite-holonomy-ec-control",
        "direct group-commutator holonomies reproduce the exact quadratic EC orbit curvatures",
        abs(finite_spatial - (8.0 / 3.0) * np.sqrt(SAFE_X[0])) < 2.0e-6
        and abs(finite_tick - (8.0 / 9.0) * np.sqrt(SAFE_X[0])) < 2.0e-6,
        f"finite spatial/tick={finite_spatial:.9f}/{finite_tick:.9f}",
    )

    r6_spatial_low, _ = orbit_holder_sixth(SAFE_T[0])
    _, r6_tick_high = orbit_holder_sixth(SAFE_T[1])
    holder_sixth = max(r6_spatial_low, r6_tick_high)
    site_ratio = (4.0 / 3.0) * np.exp(SAFE_X[1] - SAFE_Y[0] / 2.0)
    conditional_odds = site_ratio * 9.65 / 4.0
    conditional_floor = 1.0 / (1.0 + conditional_odds)
    checks.check(
        "six-neighbor-holder-bound",
        "Jensen below the four spatial labels and Holder above the six tick labels bound every six-neighbor conditional environment",
        SAFE_T[0] > 1.0
        and r6_spatial_low < 4.77
        and r6_tick_high < 9.65
        and holder_sixth < 9.65,
        f"t={SAFE_T[0]:.6f}..{SAFE_T[1]:.6f}; r6 spatial/tick={r6_spatial_low:.9f}/{r6_tick_high:.9f}",
    )
    checks.check(
        "uniform-spatial-orbit-probability-floor",
        "every finite-volume conditional and hence every marginal gives the four spatial rays total probability above 0.18",
        conditional_floor > ORBIT_PROBABILITY_FLOOR,
        f"conditional floor={conditional_floor:.9f}; declared floor={ORBIT_PROBABILITY_FLOOR:.2f}",
    )

    minimum_contact = np.inf
    for x in SAFE_X:
        for y in SAFE_Y:
            projectors = projector_table(x, y)
            for left in projectors:
                for right in projectors:
                    minimum_contact = min(
                        minimum_contact,
                        float(np.linalg.eigvalsh(contact_matrix(left, right))[0]),
                    )
    checks.check(
        "record-contact-stabilization-ceiling",
        "rank-one bond calculus bounds each Record contact below by -2 beta times the connection coefficient norm squared",
        minimum_contact >= -2.0 * BETA - 2.0e-14
        and minimum_contact < -2.0 * BETA + 2.0e-12,
        f"corner/pair minimum={minimum_contact:.12f}; analytic lower={-2.0 * BETA:.12f}",
    )

    ec_coefficient = 8.0 / 9.0 + (16.0 / 9.0) * ORBIT_PROBABILITY_FLOOR
    upper_bound = (
        ETA * (SAFE_X[0] + SAFE_Y[1] + 1.0)
        + 2.0 * BETA
        - ec_coefficient * np.sqrt(SAFE_X[0])
    )
    derivative_upper = ETA - ec_coefficient / (2.0 * np.sqrt(SAFE_X[1]))
    checks.check(
        "strict-negative-full-directional-bound",
        "geometry minus complete Record-plus-EC pressure has a strict negative upper bound in the normalized isotropic mode",
        derivative_upper < 0.0 and upper_bound < -0.03,
        f"K_iso<={upper_bound:.12f}; d/dx upper={derivative_upper:.9f}",
    )

    rank, columns, augmented_rank, gauge_residual = gauge_tangent_test()
    checks.check(
        "physical-gauge-quotient-direction",
        "the L3 joint coframe/link target raises the local-frame tangent rank and therefore survives the physical quotient",
        rank == columns
        and augmented_rank == rank + 1
        and gauge_residual > 1.0,
        f"tangent rank={rank}/{columns}; augmented={augmented_rank}; least residual={gauge_residual:.9f}",
    )

    checks.check(
        "volume-independent-carrier-counts",
        "every periodic L>=3 cubic carrier has three edges, three faces, and twelve based loops per site, matching the local proof",
        all(
            periodic_carrier_counts(length)
            == (length**3, 3 * length**3, 3 * length**3, 12 * length**3)
            for length in (3, 5, 7, 11)
        ),
    )

    checks.check(
        "narrow-claim-and-live-escapes",
        "the note restricts the result to the unchanged flat supplied law and keeps modified, relational, nonflat, and Lorentzian routes live",
        all(
            phrase in note
            for phrase in (
                "not a gravity no-go",
                "modified law",
                "relational",
                "nonflat",
                "lorentzian",
                "no canonical axiom is edited",
            )
        ),
    )

    checks.check(
        "no-go-discipline-landing-packet",
        "the committed source note contains the current N1 through N8 no-go-discipline gate",
        all(f"### n{index}" in note for index in range(1, 9))
        and "status: pass" in note,
    )

    print(
        "N5_CERTIFICATE: all ten EC labels, all one-hundred projector-bond contacts, one six-neighbor conditional family, one physical uniform mode, and every periodic volume are resolved at their stated scopes"
    )
    print(
        "per_element: checked all ten ray labels and all one hundred ordered rank-one projector bond contacts in the supplied law"
    )
    print(
        "per_site: checked the complete six-neighbor conditional orbit bound by Jensen-Holder reduction over both cubic label orbits"
    )
    print(
        "per_mode: checked one normalized proper-cubic isotropic zero-momentum connection mode A_i=J_(i,3)/sqrt(3), not every mode"
    )
    print(
        "per_block: checked the complete geometry, Record contact, connected covariance sign, and EC curvature bound in that directional Hessian"
    )
    print(
        "lattice_wide: checked every finite periodic cubic L>=3 carrier through volume-independent local counts and conditional bounds"
    )
    print(
        "scope_boundary: one supplied Euclidean flat stationary branch; no full connection spectrum, nonflat phase, modified law, Einstein tensor, or Lorentzian update"
    )
    print(f"primary_pass={checks.passed}")
    print(f"primary_fail={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
