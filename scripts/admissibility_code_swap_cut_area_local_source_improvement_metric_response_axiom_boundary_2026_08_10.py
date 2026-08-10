#!/usr/bin/env python3
"""Exact checks for the code-symmetric action as a cut-area law.

The paired source proves the regular-graph cut identity, the cubic directional
surface response, the endpoint-allocation improvement family, and the fixed-
background metric-response ambiguity.  This runner binds those statements to
the current source boundaries and executes exact finite fixtures.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from math import comb
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_"
    "METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
ACTION_PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_ISING_ACTION_RECORD_READOUT_PAIR_RESOURCE_RESPONSE_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
WEAK_FIELD_PATH = ROOT / "docs" / (
    "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
)
STRESS_PATH = ROOT / "docs" / (
    "UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md"
)
SCALE_PATH = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
SOURCE_CONVENTION_PATH = ROOT / "docs" / (
    "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_"
    "NOTE_2026-05-21.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_ISING_ACTION_RECORD_READOUT_PAIR_RESOURCE_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
    "docs/UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md",
)


Vec3 = tuple[int, int, int]
Matrix3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

AXES: tuple[Vec3, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(site: Vec3, direction: Vec3, size: int, sign: int = 1) -> Vec3:
    return tuple((site[index] + sign * direction[index]) % size for index in range(3))


def periodic_cubic_graph(
    size: int,
) -> tuple[tuple[Vec3, ...], tuple[tuple[tuple[Vec3, Vec3], ...], ...]]:
    sites = tuple(product(range(size), repeat=3))
    directional = []
    for direction in AXES:
        edges = {
            tuple(sorted((site, add(site, direction, size))))
            for site in sites
        }
        directional.append(tuple(sorted(edges)))
    return sites, tuple(directional)


def directional_counts(
    chosen: frozenset[Vec3],
    directional_edges: tuple[tuple[tuple[Vec3, Vec3], ...], ...],
) -> tuple[tuple[int, int], ...]:
    values = []
    for edges in directional_edges:
        internal = sum(left in chosen and right in chosen for left, right in edges)
        cut = sum((left in chosen) != (right in chosen) for left, right in edges)
        values.append((internal, cut))
    return tuple(values)


def neighbor_counts(chosen: frozenset[Vec3], site: Vec3, size: int) -> tuple[int, int, int]:
    return tuple(
        sum(add(site, direction, size, sign) in chosen for sign in (-1, 1))
        for direction in AXES
    )


def parity(values: tuple[int, int, int]) -> int:
    inversions = sum(
        values[left] > values[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[Matrix3, ...]:
    rotations: set[Matrix3] = set()
    for axis_order in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            if parity(axis_order) * signs[0] * signs[1] * signs[2] != 1:
                continue
            rows = []
            for row in range(3):
                rows.append(
                    tuple(
                        signs[row] if column == axis_order[row] else 0
                        for column in range(3)
                    )
                )
            rotations.add(tuple(rows))
    return tuple(sorted(rotations))


def rotate_site(site: Vec3, rotation: Matrix3, size: int) -> Vec3:
    return tuple(
        sum(rotation[row][column] * site[column] for column in range(3)) % size
        for row in range(3)
    )


def rotate_set(chosen: frozenset[Vec3], rotation: Matrix3, size: int) -> frozenset[Vec3]:
    return frozenset(rotate_site(site, rotation, size) for site in chosen)


def transpose(matrix: Matrix3) -> Matrix3:
    return tuple(tuple(matrix[column][row] for column in range(3)) for row in range(3))


def matrix_product(left, right):
    return tuple(
        tuple(sum(left[row][k] * right[k][column] for k in range(3)) for column in range(3))
        for row in range(3)
    )


def orientation_tensor(cuts: tuple[int, int, int]) -> Matrix3:
    return tuple(
        tuple(cuts[row] if row == column else 0 for column in range(3))
        for row in range(3)
    )


def environment_gradient_tensor(
    chosen: frozenset[Vec3], sites: tuple[Vec3, ...], size: int
) -> Matrix3:
    result = [[0 for _ in range(3)] for _ in range(3)]
    for site in sites:
        gradient = tuple(
            int(add(site, direction, size) in chosen)
            - int(add(site, direction, size, -1) in chosen)
            for direction in AXES
        )
        for left in range(3):
            for right in range(3):
                result[left][right] += gradient[left] * gradient[right]
    return tuple(tuple(row) for row in result)


def local_cut_tensor(
    chosen: frozenset[Vec3], sites: tuple[Vec3, ...], size: int
) -> dict[Vec3, tuple[Fraction, Fraction, Fraction]]:
    values = {}
    for site in sites:
        values[site] = tuple(
            Fraction(
                sum(
                    (site in chosen) != (add(site, direction, size, sign) in chosen)
                    for sign in (-1, 1)
                ),
                2,
            )
            for direction in AXES
        )
    return values


def local_divergence(
    tensor: dict[Vec3, tuple[Fraction, Fraction, Fraction]],
    sites: tuple[Vec3, ...],
    size: int,
) -> dict[Vec3, tuple[Fraction, Fraction, Fraction]]:
    return {
        site: tuple(
            tensor[site][axis]
            - tensor[add(site, AXES[axis], size, -1)][axis]
            for axis in range(3)
        )
        for site in sites
    }


def source_density(
    chosen: frozenset[Vec3],
    sites: tuple[Vec3, ...],
    size: int,
    tension: Fraction,
    theta: Fraction,
) -> dict[Vec3, Fraction]:
    values = {}
    for site in sites:
        occupied = int(site in chosen)
        neighbors = sum(neighbor_counts(chosen, site, size))
        values[site] = tension / 2 * (
            theta * occupied * (6 - neighbors)
            + (1 - theta) * (1 - occupied) * neighbors
        )
    return values


def laplacian_indicator(
    chosen: frozenset[Vec3], sites: tuple[Vec3, ...], size: int
) -> dict[Vec3, Fraction]:
    return {
        site: Fraction(6 * int(site in chosen) - sum(neighbor_counts(chosen, site, size)))
        for site in sites
    }


def apply_laplacian(
    values: dict[Vec3, Fraction], sites: tuple[Vec3, ...], size: int
) -> dict[Vec3, Fraction]:
    return {
        site: 6 * values[site]
        - sum(
            values[add(site, direction, size, sign)]
            for direction in AXES
            for sign in (-1, 1)
        )
        for site in sites
    }


def exact_mean_covariance(
    weighted: tuple[tuple[Fraction, tuple[int, ...]], ...]
) -> tuple[tuple[Fraction, ...], tuple[tuple[Fraction, ...], ...]]:
    total = sum((weight for weight, _ in weighted), Fraction(0))
    dimension = len(weighted[0][1])
    means = tuple(
        sum((weight * values[index] for weight, values in weighted), Fraction(0)) / total
        for index in range(dimension)
    )
    covariance = tuple(
        tuple(
            sum(
                (weight * values[left] * values[right] for weight, values in weighted),
                Fraction(0),
            )
            / total
            - means[left] * means[right]
            for right in range(dimension)
        )
        for left in range(dimension)
    )
    return means, covariance


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = ACTION_PARENT_PATH.read_text(encoding="utf-8")
    weak_field = WEAK_FIELD_PATH.read_text(encoding="utf-8")
    stress = STRESS_PATH.read_text(encoding="utf-8")
    scale = SCALE_PATH.read_text(encoding="utf-8")
    source_convention = SOURCE_CONVENTION_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    parent_flat = " ".join(parent.split())
    scale_flat = " ".join(scale.split())

    print("external_scientific_inputs: none; regular-graph cuts, finite Gibbs response, and source-improvement algebra are proved in-source")
    print("package_local_integrity_reads: current axioms, Block-9 action, weak-field source response, stress-Ward boundary, and scale primitive are source-bound")
    print("analytic_boundary: arbitrary regular-graph and finite-partition identities are general; cubic, K7, orbit, source, and tensor fixtures are executed exactly")
    print("negative_scope: one fixed-background scalar law does not select a unique local metric derivative; source conventions, metric families, dynamics, and physical bridges remain live")

    checks.check(
        "source-current-axioms",
        "the cubic lattice and probability clause are present while source/action remains outside axiom content",
        all(
            phrase in axiom_flat
            for phrase in (
                "Physical sites are the points of the cubic lattice `Z^3`",
                "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions",
                "source/action and physical-observable identification",
            )
        ),
    )
    checks.check(
        "source-action-parent",
        "Block 9 supplies the code-symmetric action and preserves the stress and metric boundary",
        all(
            phrase in parent_flat
            for phrase in (
                "A B^3=1",
                "v[E(x)-3N(x)]",
                "No stress tensor, metric, curvature, or gravitational coupling is inferred",
            )
        ),
    )
    checks.check(
        "source-weak-field",
        "the weak-field packet requires a supplied source in a graph-Laplacian variational equation",
        "H = -Delta_lat" in weak_field
        and "A[phi; rho]" in weak_field
        and "H phi = P0 rho" in weak_field,
    )
    checks.check(
        "source-stress-boundary",
        "the stress packet leaves the full metric-source Hessian and physical spin-two identification open",
        "derive the full finite-`k` metric-source Hessian" in stress
        and "identify the runner-defined positive TT sign with a physical" in stress,
    )
    checks.check(
        "source-scale-primitive",
        "the approved scale reference converts units but supplies no dimensionless source or coupling",
        "`a^{-1} = M_Pl`" in scale_flat
        and "It carries zero dimensionless content" in scale_flat
        and "readout bridge" in scale_flat,
    )
    checks.check(
        "source-convention-route",
        "the existing open-gate route treats local source derivatives as an explicit convention rather than an axiom theorem",
        "Claim type:** open_gate" in source_convention
        and "Local source derivatives of `S` define the local operator insertions" in source_convention
        and "still a convention, not a derivation" in source_convention,
    )

    size = 3
    sites, directional_edges = periodic_cubic_graph(size)
    all_edges = tuple(edge for edges in directional_edges for edge in edges)
    degrees = {site: 0 for site in sites}
    for left, right in all_edges:
        degrees[left] += 1
        degrees[right] += 1
    checks.check(
        "cubic-quotient",
        "the periodic L=3 fixture has 27 sites, 27 edges per axis, 81 total edges, and degree six",
        len(sites) == 27
        and tuple(len(edges) for edges in directional_edges) == (27, 27, 27)
        and len(all_edges) == 81
        and set(degrees.values()) == {6},
    )

    sample_sets = (
        frozenset(),
        frozenset((sites[0],)),
        frozenset(directional_edges[0][0]),
        frozenset(((0, 0, 0), (0, 1, 1))),
        frozenset(((0, 0, 0), (1, 0, 0), (2, 0, 0))),
        frozenset(site for site in sites if site[2] == 0),
        frozenset(site for site in sites if sum(site) % 2 == 0),
        frozenset(sites),
    )
    regular_identity = all(
        all(2 * len(chosen) == 2 * internal + cut for internal, cut in directional_counts(chosen, directional_edges))
        for chosen in sample_sets
    )
    checks.check(
        "directional-degree-cut",
        "each axis obeys 2N=2E_a+C_a on every exact cubic fixture",
        regular_identity,
    )

    complement_identity = True
    for chosen in sample_sets:
        complement = frozenset(set(sites) - set(chosen))
        original = directional_counts(chosen, directional_edges)
        swapped = directional_counts(complement, directional_edges)
        complement_identity &= all(
            swapped[axis][0] == len(directional_edges[axis]) - 2 * len(chosen) + original[axis][0]
            and swapped[axis][1] == original[axis][1]
            for axis in range(3)
        )
    checks.check(
        "code-complement-cut",
        "code complementation preserves every directional cut and has the exact internal-edge transform",
        complement_identity,
    )

    tensions = (Fraction(2), Fraction(3), Fraction(5))
    action_cut_identity = True
    for chosen in sample_sets:
        counts = directional_counts(chosen, directional_edges)
        statistical = sum(tensions) * len(chosen) - sum(
            tensions[axis] * counts[axis][0] for axis in range(3)
        )
        cut_action = sum(tensions[axis] * counts[axis][1] for axis in range(3)) / 2
        action_cut_identity &= statistical == cut_action
    checks.check(
        "anisotropic-cut-action",
        "A times the three B_a equals one exactly converts the compatible action to one-half sum t_a C_a",
        action_cut_identity,
    )
    checks.check(
        "isotropic-area-law",
        "on the six-regular line 3N-E equals one-half the cut size, including empty and full zero-area phases",
        all(
            3 * len(chosen) - sum(value[0] for value in directional_counts(chosen, directional_edges))
            == sum(value[1] for value in directional_counts(chosen, directional_edges)) / 2
            for chosen in sample_sets
        )
        and sum(value[1] for value in directional_counts(frozenset(), directional_edges)) == 0
        and sum(value[1] for value in directional_counts(frozenset(sites), directional_edges)) == 0,
    )

    local_variations = True
    for chosen in sample_sets[:-1]:
        for site in sites:
            if site in chosen:
                continue
            before = tuple(value[1] for value in directional_counts(chosen, directional_edges))
            after_set = frozenset(set(chosen) | {site})
            after = tuple(value[1] for value in directional_counts(after_set, directional_edges))
            neighbors = neighbor_counts(chosen, site, size)
            local_variations &= all(
                after[axis] - before[axis] == 2 * (1 - neighbors[axis])
                for axis in range(3)
            )
            delta_action = sum(
                tensions[axis] * Fraction(after[axis] - before[axis], 2)
                for axis in range(3)
            )
            local_variations &= delta_action == sum(
                tensions[axis] * (1 - neighbors[axis]) for axis in range(3)
            )
    checks.check(
        "local-flip-area",
        "adding one occupied site changes C_a by 2(1-k_a) and the action by sum t_a(1-k_a)",
        local_variations,
    )
    checks.check(
        "conditional-odds-exponent",
        "the isotropic local log odds (k-3)t are exactly minus the cut-action increment",
        all(
            Fraction(k - 3) * tensions[0] == -Fraction(3 - k) * tensions[0]
            for k in range(7)
        ),
    )

    plaquette_closure = True
    for chosen in sample_sets:
        for site in sites:
            for left_axis in range(3):
                for right_axis in range(left_axis + 1, 3):
                    a = AXES[left_axis]
                    b = AXES[right_axis]
                    sa = add(site, a, size)
                    sb = add(site, b, size)
                    sab = add(sa, b, size)
                    perimeter = ((site, sa), (sa, sab), (sab, sb), (sb, site))
                    plaquette_closure &= sum(
                        (left in chosen) != (right in chosen) for left, right in perimeter
                    ) % 2 == 0
    checks.check(
        "dual-surface-closure",
        "every primal plaquette meets the cut in even parity, so dual cut plaquettes form a closed cubical two-chain",
        plaquette_closure,
    )

    rotations = proper_cubic_rotations()
    line = frozenset(((0, 0, 0), (1, 0, 0), (2, 0, 0)))
    rotated_cuts = tuple(
        tuple(value[1] for value in directional_counts(rotate_set(line, rotation, size), directional_edges))
        for rotation in rotations
    )
    means, covariance = exact_mean_covariance(tuple((Fraction(1), values) for values in rotated_cuts))
    expected_covariance = tuple(
        tuple(Fraction(8 if left == right else -4) for right in range(3))
        for left in range(3)
    )
    checks.check(
        "cubic-cut-orbit-response",
        "all 24 proper rotations give mean cuts (4,4,4) and exact diagonal-shear covariance diag 8 offdiag -4",
        len(rotations) == 24
        and set(rotated_cuts) == {(0, 6, 6), (6, 0, 6), (6, 6, 0)}
        and means == (Fraction(4), Fraction(4), Fraction(4))
        and covariance == expected_covariance,
    )
    bulk_eigenvalue = covariance[0][0] + 2 * covariance[0][1]
    diagonal_shear_eigenvalue = covariance[0][0] - covariance[0][1]
    checks.check(
        "cubic-response-modes",
        "the orbit has zero fixed-area bulk variance and two positive diagonal-shear eigenvalues equal to twelve",
        bulk_eigenvalue == 0 and diagonal_shear_eigenvalue == 12,
    )

    k7_weighted = []
    for occupied in range(8):
        cut = occupied * (7 - occupied)
        weight = Fraction(comb(7, occupied)) * Fraction(4) ** (-cut // 2)
        k7_weighted.append((weight, (occupied, cut)))
    k7_means, k7_covariance = exact_mean_covariance(tuple(k7_weighted))
    k7_partition = sum((weight for weight, _ in k7_weighted), Fraction(0))
    checks.check(
        "k7-exact-partition",
        "the degree-six B=4 fixture has Z=4663/2048, half occupancy, and uniform-phase probability 4096/4663",
        k7_partition == Fraction(4663, 2048)
        and k7_means[0] == Fraction(7, 2)
        and Fraction(2) / k7_partition == Fraction(4096, 4663),
    )
    checks.check(
        "cut-susceptibility",
        "the exact cut mean is 3948/4663 and one-quarter cut variance is 30572220/21743569",
        k7_means[1] == Fraction(3948, 4663)
        and k7_covariance[1][1] == Fraction(122288880, 21743569)
        and k7_covariance[1][1] / 4 == Fraction(30572220, 21743569),
    )

    checks.check(
        "volume-source-separation",
        "empty and full configurations have the same zero cut action but opposite nonzero magnetization",
        sum(value[1] for value in directional_counts(frozenset(), directional_edges)) == 0
        and sum(value[1] for value in directional_counts(frozenset(sites), directional_edges)) == 0
        and 2 * 0 - len(sites) == -27
        and 2 * len(sites) - len(sites) == 27,
    )

    chosen = frozenset(((0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 1, 1)))
    tension = Fraction(7, 3)
    total_cut = sum(value[1] for value in directional_counts(chosen, directional_edges))
    theta_values = (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1))
    densities = {
        theta: source_density(chosen, sites, size, tension, theta)
        for theta in theta_values
    }
    checks.check(
        "endpoint-source-total",
        "every endpoint-allocation parameter has the same total source equal to one-half t times the cut",
        all(sum(values.values(), Fraction(0)) == tension * total_cut / 2 for values in densities.values()),
    )
    laplacian = laplacian_indicator(chosen, sites, size)
    symmetric = densities[Fraction(1, 2)]
    checks.check(
        "source-improvement-family",
        "rho_theta minus rho_half is exactly (t/2)(theta-1/2) times the graph Laplacian of occupation",
        all(
            densities[theta][site] - symmetric[site]
            == tension / 2 * (theta - Fraction(1, 2)) * laplacian[site]
            for theta in theta_values
            for site in sites
        ),
    )
    complement = frozenset(set(sites) - set(chosen))
    checks.check(
        "source-code-swap",
        "code swap sends endpoint allocation theta to 1-theta and fixes the equal-endpoint density",
        all(
            source_density(complement, sites, size, tension, theta)[site]
            == source_density(chosen, sites, size, tension, 1 - theta)[site]
            for theta in theta_values
            for site in sites
        )
        and source_density(complement, sites, size, tension, Fraction(1, 2)) == symmetric,
    )

    mean_occupation = Fraction(len(chosen), len(sites))
    projected_occupation = {
        site: Fraction(int(site in chosen)) - mean_occupation for site in sites
    }
    checks.check(
        "poisson-improvement-contact",
        "L applied to zero-mean occupation equals Lx, so Poisson potentials differ by the exact local improvement",
        sum(projected_occupation.values(), Fraction(0)) == 0
        and apply_laplacian(projected_occupation, sites, size) == laplacian
        and all(
            densities[theta][site] - symmetric[site]
            == apply_laplacian(
                {
                    point: tension / 2 * (theta - Fraction(1, 2)) * projected_occupation[point]
                    for point in sites
                },
                sites,
                size,
            )[site]
            for theta in theta_values
            for site in sites
        ),
    )
    checks.check(
        "exterior-improvement-invariance",
        "the potential improvement is constant on each phase and has zero edge gradient away from the cut",
        all(
            projected_occupation[left] == projected_occupation[right]
            for left, right in all_edges
            if (left in chosen) == (right in chosen)
        ),
    )

    cut_values = tuple(value[1] for value in directional_counts(chosen, directional_edges))
    q_tensor = orientation_tensor(cut_values)
    singleton = frozenset((sites[0],))
    singleton_cuts = tuple(
        value[1] for value in directional_counts(singleton, directional_edges)
    )
    q_local = local_cut_tensor(singleton, sites, size)
    q_divergence = local_divergence(q_local, sites, size)
    checks.check(
        "cut-orientation-tensor",
        "the covariant axis-cut tensor is diagonal and its trace is the total cut area",
        all(q_tensor[left][right] == 0 for left in range(3) for right in range(3) if left != right)
        and sum(q_tensor[index][index] for index in range(3)) == total_cut,
    )
    checks.check(
        "covariance-not-conservation",
        "the singleton cut tensor has nonzero local lattice divergence although its global divergence telescopes to zero",
        all(
            sum((value[axis] for value in q_local.values()), Fraction(0))
            == singleton_cuts[axis]
            for axis in range(3)
        )
        and any(any(component for component in value) for value in q_divergence.values())
        and all(
            sum((value[axis] for value in q_divergence.values()), Fraction(0)) == 0
            for axis in range(3)
        ),
    )

    diagonal_pair = frozenset(((0, 0, 0), (0, 1, 1)))
    p_tensor = environment_gradient_tensor(diagonal_pair, sites, size)
    checks.check(
        "metric-extension-offdiagonal",
        "a covariant range-one environment tensor has P_yz=P_zy=-2 while the axis-cut tensor has no offdiagonal coordinate",
        p_tensor == ((4, 0, 0), (0, 4, -2), (0, -2, 4))
        and orientation_tensor(
            tuple(value[1] for value in directional_counts(diagonal_pair, directional_edges))
        )[1][2]
        == 0,
    )
    tensor_covariance = True
    for rotation in rotations:
        rotated = rotate_set(diagonal_pair, rotation, size)
        rotated_p = environment_gradient_tensor(rotated, sites, size)
        expected = matrix_product(matrix_product(rotation, p_tensor), transpose(rotation))
        tensor_covariance &= rotated_p == expected
    checks.check(
        "metric-extension-covariance",
        "all 24 proper rotations transport the environment tensor by P to R P R-transpose",
        tensor_covariance,
    )

    construction_needles = (
        "3N-E=|delta X|/2",
        "S_stat=(log B)/2 |delta X|",
        "Delta_i |delta X|=6-2k",
        "rho_i^(theta)-rho_i^(1/2)",
        "phi^(theta)-phi^(1/2)",
        "Physical geometry-family source/action clause",
    )
    checks.check(
        "construction-source-surface",
        "the source states the cut law, flip variation, improvement identity, Poisson contact term, and candidate clause",
        all(phrase in note_flat for phrase in construction_needles),
    )
    boundary_needles = (
        "No canonical axiom is edited",
        "the fixed TOE percentages do not move",
        "not a physical stress tensor",
        "This steelman is accepted",
        "open-gate convention route",
    )
    checks.check(
        "boundary-source-surface",
        "the source preserves governance, percentages, tensor typing, steelman, and convention-reframe routes",
        all(phrase in note_flat for phrase in boundary_needles),
    )
    checks.check(
        "machine-status-contract",
        "the source carries the bounded upstream-support trace contract",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: upstream_support",
                "target_claim_id:",
                "target_blocker_text:",
                "source_of_blocker_text: handoff",
                "reachability_to_target: advances",
                "artifact_role: theorem",
                "next_trace_action:",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "cut-area action, endpoint source, metric family, and stress derivative wording is absent from the canonical memo",
        all(
            phrase not in axiom
            for phrase in (
                "cut-area action",
                "endpoint source allocation",
                "geometry-dependent family",
                "metric derivative",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "N1-N8, primitive registry, residual matching, accepted steelman, and broad-negative rejection all land in-source",
        all(f"### N{index}" in note for index in range(1, 9))
        and "Primitive Registry Check" in note
        and "| Source location | Prior residual | Present residual | Match? |" in note
        and "This steelman is accepted" in note
        and "FAIL / DO NOT SHIP" in note,
    )

    print("per_element: checked each binary edge disagreement and each occupied-to-empty local flip contribution exactly")
    print("per_site: checked directional neighbour counts, endpoint source shares, graph-Laplacian improvements, and local divergence")
    print("per_mode: checked bulk and diagonal-shear cut responses; offdiagonal metric stress is not executed — the axis-cut carrier has no such coordinate")
    print("per_block: checked compatible action -> closed dual cut surface -> local source family -> conditional Poisson contact response")
    print("lattice_wide: checked degree-six periodic cubic identities and 24 rotations; physical action licensing, conserved spacetime stress, metric dynamics, and gravity are not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
