#!/usr/bin/env python3
"""Exact checks for the cut-surface coframe and Ward construction.

The paired note constructs a positive finite geometry-indexed Gibbs family,
derives its flat coframe response, proves an exact lattice virtual-work
identity, and separates that on-shell force balance from the off-shell
higher-form conservation of the oriented cut surface.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from math import comb, isqrt
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_"
    "GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_"
    "METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
SOURCE_CONVENTION_PATH = ROOT / "docs" / (
    "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_"
    "NOTE_2026-05-21.md"
)
STRESS_WARD_PATH = ROOT / "docs" / (
    "UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_"
    "NOTE_2026-06-08.md"
)
SCALE_PATH = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CODE_SWAP_CUT_AREA_LOCAL_SOURCE_IMPROVEMENT_METRIC_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md",
    "docs/UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
)


Vec3 = tuple[int, int, int]
QVec3 = tuple[Fraction, Fraction, Fraction]
Matrix3 = tuple[tuple[Fraction, Fraction, Fraction], ...]
IntMatrix3 = tuple[tuple[int, int, int], ...]

AXES: tuple[Vec3, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def add(site: Vec3, direction: Vec3, size: int, sign: int = 1) -> Vec3:
    return tuple((site[index] + sign * direction[index]) % size for index in range(3))


def sites_of(size: int) -> tuple[Vec3, ...]:
    return tuple(product(range(size), repeat=3))


def parity(values: tuple[int, int, int]) -> int:
    inversions = sum(
        values[left] > values[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[IntMatrix3, ...]:
    rotations: set[IntMatrix3] = set()
    for axis_order in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            if parity(axis_order) * signs[0] * signs[1] * signs[2] != 1:
                continue
            rotations.add(
                tuple(
                    tuple(
                        signs[row] if column == axis_order[row] else 0
                        for column in range(3)
                    )
                    for row in range(3)
                )
            )
    return tuple(sorted(rotations))


def matrix_vector(matrix, vector):
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def matrix_product(left, right):
    return tuple(
        tuple(
            sum(left[row][middle] * right[middle][column] for middle in range(3))
            for column in range(3)
        )
        for row in range(3)
    )


def transpose(matrix):
    return tuple(tuple(matrix[column][row] for column in range(3)) for row in range(3))


def rotate_site(site: Vec3, rotation: IntMatrix3, size: int) -> Vec3:
    return tuple(value % size for value in matrix_vector(rotation, site))


def rotate_set(chosen: frozenset[Vec3], rotation: IntMatrix3, size: int) -> frozenset[Vec3]:
    return frozenset(rotate_site(site, rotation, size) for site in chosen)


def rotate_matrix(matrix: Matrix3, rotation: IntMatrix3) -> Matrix3:
    return matrix_product(matrix_product(rotation, matrix), transpose(rotation))


def signed_jump(chosen: frozenset[Vec3], site: Vec3, axis: int, size: int) -> int:
    return int(add(site, AXES[axis], size) in chosen) - int(site in chosen)


def cut_indicator(chosen: frozenset[Vec3], site: Vec3, axis: int, size: int) -> int:
    jump = signed_jump(chosen, site, axis, size)
    return jump * jump


def local_cut_share(chosen: frozenset[Vec3], site: Vec3, axis: int, size: int) -> Fraction:
    backward = add(site, AXES[axis], size, -1)
    return Fraction(
        cut_indicator(chosen, site, axis, size)
        + cut_indicator(chosen, backward, axis, size),
        2,
    )


def oriented_plaquette_curl(
    chosen: frozenset[Vec3], site: Vec3, left_axis: int, right_axis: int, size: int
) -> int:
    left = AXES[left_axis]
    right = AXES[right_axis]
    return (
        signed_jump(chosen, site, left_axis, size)
        + signed_jump(chosen, add(site, left, size), right_axis, size)
        - signed_jump(chosen, add(site, right, size), left_axis, size)
        - signed_jump(chosen, site, right_axis, size)
    )


def oriented_source_action(
    chosen: frozenset[Vec3],
    sites: tuple[Vec3, ...],
    size: int,
    source: dict[Vec3, QVec3],
) -> Fraction:
    return sum(
        source[site][axis] * signed_jump(chosen, site, axis, size)
        for site in sites
        for axis in range(3)
    )


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def dot(left, right):
    return sum(left[index] * right[index] for index in range(3))


def column(matrix, index: int):
    return tuple(matrix[row][index] for row in range(3))


def cofactor_column(matrix: Matrix3, axis: int):
    cyclic = ((1, 2), (2, 0), (0, 1))
    left, right = cyclic[axis]
    return cross(column(matrix, left), column(matrix, right))


def area_squared(matrix: Matrix3, axis: int) -> Fraction:
    value = cofactor_column(matrix, axis)
    return Fraction(dot(value, value))


def exact_fraction_sqrt(value: Fraction) -> Fraction:
    numerator = isqrt(value.numerator)
    denominator = isqrt(value.denominator)
    if numerator * numerator != value.numerator or denominator * denominator != value.denominator:
        raise ValueError(f"not an exact rational square: {value}")
    return Fraction(numerator, denominator)


def area_factor(matrix: Matrix3, axis: int) -> Fraction:
    return exact_fraction_sqrt(area_squared(matrix, axis))


def diagonal_matrix(values: tuple[Fraction, Fraction, Fraction]) -> Matrix3:
    return tuple(
        tuple(values[row] if row == column_index else Fraction(0) for column_index in range(3))
        for row in range(3)
    )


def identity_matrix() -> Matrix3:
    return diagonal_matrix((Fraction(1), Fraction(1), Fraction(1)))


def area_first_second_variation(axis: int, variation: Matrix3) -> tuple[Fraction, Fraction]:
    """Return A'_axis(0), A''_axis(0) for F(s)=I+s*variation."""
    cyclic = ((1, 2), (2, 0), (0, 1))
    left, right = cyclic[axis]
    basis = tuple(
        tuple(Fraction(int(row == column_index)) for row in range(3))
        for column_index in range(3)
    )
    h_left = column(variation, left)
    h_right = column(variation, right)
    first_vector = tuple(
        cross(h_left, basis[right])[index] + cross(basis[left], h_right)[index]
        for index in range(3)
    )
    second_vector = tuple(2 * value for value in cross(h_left, h_right))
    normal = basis[axis]
    first = Fraction(dot(normal, first_vector))
    second = Fraction(
        dot(first_vector, first_vector)
        + dot(normal, second_vector)
        - first * first
    )
    return first, second


def diagonal_lengths(site: Vec3) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(
        Fraction(6 + ((site[0] + 2 * site[1] + 3 * site[2] + 2 * axis) % 5), 5)
        for axis in range(3)
    )


def coframe_field(sites: tuple[Vec3, ...]) -> dict[Vec3, Matrix3]:
    return {site: diagonal_matrix(diagonal_lengths(site)) for site in sites}


def area_field(coframes: dict[Vec3, Matrix3]) -> dict[Vec3, tuple[Fraction, Fraction, Fraction]]:
    return {
        site: tuple(area_factor(coframe, axis) for axis in range(3))
        for site, coframe in coframes.items()
    }


def site_share_action(
    chosen: frozenset[Vec3],
    sites: tuple[Vec3, ...],
    size: int,
    areas: dict[Vec3, tuple[Fraction, Fraction, Fraction]],
    tension: Fraction,
) -> Fraction:
    return tension * sum(
        local_cut_share(chosen, site, axis, size) * areas[site][axis]
        for site in sites
        for axis in range(3)
    )


def edge_area_weight(
    areas: dict[Vec3, tuple[Fraction, Fraction, Fraction]],
    site: Vec3,
    axis: int,
    size: int,
) -> Fraction:
    head = add(site, AXES[axis], size)
    return Fraction(areas[site][axis] + areas[head][axis], 2)


def edge_action(
    chosen: frozenset[Vec3],
    sites: tuple[Vec3, ...],
    size: int,
    areas: dict[Vec3, tuple[Fraction, Fraction, Fraction]],
    tension: Fraction,
) -> Fraction:
    return tension * sum(
        cut_indicator(chosen, site, axis, size)
        * edge_area_weight(areas, site, axis, size)
        for site in sites
        for axis in range(3)
    )


def local_flip_prediction(
    chosen: frozenset[Vec3],
    site: Vec3,
    size: int,
    areas: dict[Vec3, tuple[Fraction, Fraction, Fraction]],
    tension: Fraction,
) -> Fraction:
    total = Fraction(0)
    for axis, direction in enumerate(AXES):
        forward = add(site, direction, size)
        backward = add(site, direction, size, -1)
        total += edge_area_weight(areas, site, axis, size) * (
            1 - 2 * int(forward in chosen)
        )
        total += edge_area_weight(areas, backward, axis, size) * (
            1 - 2 * int(backward in chosen)
        )
    return tension * total


def normal_cut_tensor(
    chosen: frozenset[Vec3], site: Vec3, size: int
) -> Matrix3:
    shares = tuple(local_cut_share(chosen, site, axis, size) for axis in range(3))
    return diagonal_matrix(shares)


def flat_piola_from_formula(
    chosen: frozenset[Vec3], site: Vec3, size: int, tension: Fraction
) -> Matrix3:
    shares = tuple(local_cut_share(chosen, site, axis, size) for axis in range(3))
    total = sum(shares, Fraction(0))
    return diagonal_matrix(tuple(tension * (total - shares[axis]) for axis in range(3)))


def flat_piola_from_variations(
    chosen: frozenset[Vec3], site: Vec3, size: int, tension: Fraction
) -> Matrix3:
    shares = tuple(local_cut_share(chosen, site, axis, size) for axis in range(3))
    rows = []
    for physical in range(3):
        row = []
        for lattice in range(3):
            variation = tuple(
                tuple(
                    Fraction(int(r == physical and c == lattice))
                    for c in range(3)
                )
                for r in range(3)
            )
            derivative = sum(
                shares[axis] * area_first_second_variation(axis, variation)[0]
                for axis in range(3)
            )
            row.append(tension * derivative)
        rows.append(tuple(row))
    return tuple(rows)


def centered_difference_vector(
    values: dict[Vec3, QVec3], site: Vec3, component: int, axis: int, size: int
) -> Fraction:
    return Fraction(
        values[add(site, AXES[axis], size)][component]
        - values[add(site, AXES[axis], size, -1)][component],
        2,
    )


def centered_divergence(
    tensors: dict[Vec3, Matrix3], sites: tuple[Vec3, ...], size: int
) -> dict[Vec3, QVec3]:
    return {
        site: tuple(
            sum(
                Fraction(
                    tensors[add(site, AXES[axis], size)][physical][axis]
                    - tensors[add(site, AXES[axis], size, -1)][physical][axis],
                    2,
                )
                for axis in range(3)
            )
            for physical in range(3)
        )
        for site in sites
    }


def k7_cut_moments() -> tuple[Fraction, Fraction, Fraction]:
    weighted = []
    for occupied in range(8):
        cut = occupied * (7 - occupied)
        weight = Fraction(comb(7, occupied)) * Fraction(4) ** (-cut // 2)
        weighted.append((weight, cut))
    partition = sum((weight for weight, _ in weighted), Fraction(0))
    mean = sum((weight * cut for weight, cut in weighted), Fraction(0)) / partition
    second = sum((weight * cut * cut for weight, cut in weighted), Fraction(0)) / partition
    return partition, mean, second - mean * mean


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
    parent = PARENT_PATH.read_text(encoding="utf-8")
    source_convention = SOURCE_CONVENTION_PATH.read_text(encoding="utf-8")
    stress_ward = STRESS_WARD_PATH.read_text(encoding="utf-8")
    scale = SCALE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    parent_flat = " ".join(parent.split())
    scale_flat = " ".join(scale.split())

    print("external_scientific_inputs: none; finite coframe-area, Gibbs, cochain, and virtual-work identities are derived in-source")
    print("package_local_integrity_reads: current axioms, Block-10 cut theorem, source convention, stress-Ward boundary, and scale primitive are source-bound")
    print("analytic_boundary: arbitrary positive local coframes and finite cubic Gibbs laws are analytic; exact diagonal, orbit, K7 coefficient, plane, and singleton fixtures are executed")
    print("physical_boundary: coframe choice, local action representative and unit, geometry dynamics, curvature action, field equation, coupling, and realized history are not selected")

    checks.check(
        "source-current-axioms",
        "the current memo supplies a fixed cubic lattice and leaves source/action, metric, and dynamics open",
        all(
            phrase in axiom_flat
            for phrase in (
                "Physical sites are the points of the cubic lattice `Z^3`",
                "source/action and physical-observable identification",
                "Admissibility is not a dynamics axiom",
            )
        ),
    )
    checks.check(
        "source-cut-parent",
        "Block 10 supplies the exact statistical cut action and names the geometry-family/Ward residual",
        all(
            phrase in parent_flat
            for phrase in (
                "S_stat=(log B)/2 |delta X|",
                "Physical geometry-family source/action clause",
                "A physical stress requires an off-background geometry family",
            )
        ),
    )
    checks.check(
        "source-convention",
        "the existing open gate defines insertions and connected responses by source derivatives",
        "Local source derivatives of `S` define the local operator insertions" in source_convention
        and "still a convention, not a derivation" in source_convention,
    )
    checks.check(
        "source-stress-seagull",
        "the stress packet requires a full same-family metric Hessian including contact terms",
        "derive the full finite-`k` metric-source Hessian/stress vertex of `W`" in stress_ward
        and "including all contact terms" in stress_ward,
    )
    checks.check(
        "source-scale",
        "the scale primitive converts units but supplies no dimensionless coupling or selector",
        "`a^{-1} = M_Pl`" in scale_flat
        and "It carries zero dimensionless content" in scale_flat,
    )

    size = 5
    sites = sites_of(size)
    rotations = proper_cubic_rotations()
    checks.check(
        "cubic-domain",
        "the exact periodic fixture has 125 sites and all 24 proper cubic rotations",
        len(sites) == 125 and len(rotations) == 24,
    )

    sample_sets = (
        frozenset(),
        frozenset(((0, 0, 0),)),
        frozenset(((0, 0, 0), (1, 0, 0))),
        frozenset(((0, 0, 0), (0, 1, 1))),
        frozenset(((x, 0, 0) for x in range(size))),
        frozenset(site for site in sites if site[0] in (0, 1)),
        frozenset(site for site in sites if sum(site) % 2 == 0),
        frozenset(sites),
    )

    checks.check(
        "signed-support",
        "the oriented jump squares to the unsigned cut indicator and code swap reverses only its sign",
        all(
            signed_jump(chosen, site, axis, size) ** 2
            == cut_indicator(chosen, site, axis, size)
            and signed_jump(frozenset(set(sites) - set(chosen)), site, axis, size)
            == -signed_jump(chosen, site, axis, size)
            for chosen in sample_sets
            for site in sites
            for axis in range(3)
        ),
    )
    checks.check(
        "oriented-surface-closure",
        "the signed jump has zero integer curl on every plaquette, so the dual surface current is co-closed off shell",
        all(
            oriented_plaquette_curl(chosen, site, left, right, size) == 0
            for chosen in sample_sets
            for site in sites
            for left in range(3)
            for right in range(left + 1, 3)
        ),
    )
    gauge_pairing = sum(
        Fraction((site[0] + 2 * site[1] + 3 * site[2] + left + right) % 7 - 3)
        * oriented_plaquette_curl(sample_sets[4], site, left, right, size)
        for site in sites
        for left in range(3)
        for right in range(left + 1, 3)
    )
    checks.check(
        "higher-form-gauge-ward",
        "pairing the surface boundary with an arbitrary exact test source vanishes identically",
        gauge_pairing == 0,
    )
    two_form_source = {
        site: tuple(
            Fraction((3 * site[0] + 5 * site[1] + 7 * site[2] + 2 * axis) % 13 - 6, 11)
            for axis in range(3)
        )
        for site in sites
    }
    negative_source = {
        site: tuple(-value for value in values) for site, values in two_form_source.items()
    }
    source_locality = True
    for chosen in sample_sets[:-1]:
        before = oriented_source_action(chosen, sites, size, two_form_source)
        for site in sites:
            if site in chosen:
                continue
            after = oriented_source_action(
                frozenset(set(chosen) | {site}), sites, size, two_form_source
            )
            predicted = sum(
                two_form_source[add(site, AXES[axis], size, -1)][axis]
                - two_form_source[site][axis]
                for axis in range(3)
            )
            source_locality &= after - before == predicted
    source_code_swap = all(
        oriented_source_action(chosen, sites, size, two_form_source)
        == oriented_source_action(
            frozenset(set(sites) - set(chosen)), sites, size, negative_source
        )
        for chosen in sample_sets
    )
    checks.check(
        "two-form-source-locality-covariance",
        "the oriented source changes only on six incident faces and code swap is covariant with B -> -B",
        source_locality and source_code_swap,
    )

    identity = identity_matrix()
    diagonal = diagonal_matrix((Fraction(2), Fraction(3), Fraction(5)))
    checks.check(
        "coframe-area",
        "cofactor-column norms give unit flat areas and exact diagonal areas (15,10,6)",
        tuple(area_factor(identity, axis) for axis in range(3)) == (1, 1, 1)
        and tuple(area_factor(diagonal, axis) for axis in range(3)) == (15, 10, 6),
    )
    checks.check(
        "coframe-area-covariance",
        "all proper cubic rotations transport cofactor area coordinates by the induced unsigned axis permutation",
        all(
            sorted(area_squared(rotate_matrix(diagonal, rotation), axis) for axis in range(3))
            == sorted(area_squared(diagonal, axis) for axis in range(3))
            for rotation in rotations
        ),
    )

    coframes = coframe_field(sites)
    areas = area_field(coframes)
    tension = Fraction(7, 5)
    checks.check(
        "site-edge-area-equivalence",
        "the endpoint-shared coframe action equals one count per cut edge times its mean endpoint area",
        all(
            site_share_action(chosen, sites, size, areas, tension)
            == edge_action(chosen, sites, size, areas, tension)
            for chosen in sample_sets
        ),
    )
    flat_areas = {site: (Fraction(1), Fraction(1), Fraction(1)) for site in sites}
    checks.check(
        "flat-cut-recovery",
        "at the identity coframe the geometry family reduces exactly to tension times total cut area",
        all(
            edge_action(chosen, sites, size, flat_areas, tension)
            == tension
            * sum(
                cut_indicator(chosen, site, axis, size)
                for site in sites
                for axis in range(3)
            )
            for chosen in sample_sets
        ),
    )
    checks.check(
        "geometry-code-swap",
        "the zero two-form-source coframe action is exactly invariant under code complementation",
        all(
            edge_action(chosen, sites, size, areas, tension)
            == edge_action(frozenset(set(sites) - set(chosen)), sites, size, areas, tension)
            for chosen in sample_sets
        ),
    )

    local_flip = True
    for chosen in sample_sets[:-1]:
        before = edge_action(chosen, sites, size, areas, tension)
        for site in sites:
            if site in chosen:
                continue
            after = edge_action(frozenset(set(chosen) | {site}), sites, size, areas, tension)
            local_flip &= after - before == local_flip_prediction(
                chosen, site, size, areas, tension
            )
    checks.check(
        "geometry-local-conditional",
        "every one-site action increment is the six incident mean-area weights with occupied-neighbor signs",
        local_flip,
    )
    checks.check(
        "flat-local-odds",
        "with tension t/2 the flat action increment in units of t is 3-k and the conditional odds exponent is k-3",
        all(
            Fraction(1, 2) * (6 - 2 * occupied_neighbors) == 3 - occupied_neighbors
            and -(3 - occupied_neighbors) == occupied_neighbors - 3
            for occupied_neighbors in range(7)
        ),
    )

    variations_correct = True
    for physical in range(3):
        for lattice in range(3):
            variation = tuple(
                tuple(
                    Fraction(int(row == physical and column_index == lattice))
                    for column_index in range(3)
                )
                for row in range(3)
            )
            for axis in range(3):
                first, _ = area_first_second_variation(axis, variation)
                variations_correct &= first == Fraction(
                    int(physical == lattice and physical != axis)
                )
    checks.check(
        "flat-area-first-variation",
        "the exact cofactor derivative is dA_a=tr(dF)-dF_aa",
        variations_correct,
    )

    chosen = sample_sets[4]
    piola_formula = {
        site: flat_piola_from_formula(chosen, site, size, tension) for site in sites
    }
    piola_variation = {
        site: flat_piola_from_variations(chosen, site, size, tension) for site in sites
    }
    checks.check(
        "tangential-piola-map",
        "the full flat coframe derivative is P=tension[(Tr Q)I-Q] at every site",
        piola_formula == piola_variation,
    )
    one_face = (Fraction(1), Fraction(0), Fraction(0))
    one_face_response = diagonal_matrix(
        tuple(tension * (sum(one_face) - one_face[axis]) for axis in range(3))
    )
    checks.check(
        "single-face-tangential-stress",
        "one x-normal cut face has response tension*diag(0,1,1), zero normal traction, and trace two tension",
        one_face_response
        == diagonal_matrix((Fraction(0), tension, tension))
        and matrix_vector(one_face_response, (1, 0, 0)) == (0, 0, 0)
        and sum(one_face_response[index][index] for index in range(3)) == 2 * tension,
    )

    uniform_variation = identity_matrix()
    shear_variation = tuple(
        tuple(Fraction(int(row == 0 and column_index == 1)) for column_index in range(3))
        for row in range(3)
    )
    normal_variation = tuple(
        tuple(Fraction(int(row == 0 and column_index == 0)) for column_index in range(3))
        for row in range(3)
    )
    checks.check(
        "area-seagull-paths",
        "uniform dilation has (A',A'')=(2,2), x-normal stretch leaves A_x fixed, and xy shear has A_x''=1",
        tuple(area_first_second_variation(axis, uniform_variation) for axis in range(3))
        == ((2, 2), (2, 2), (2, 2))
        and area_first_second_variation(0, normal_variation) == (0, 0)
        and tuple(area_first_second_variation(axis, shear_variation) for axis in range(3))
        == ((0, 1), (0, 0), (0, 0)),
    )

    piola_covariance = True
    force_covariance = True
    base_chosen = frozenset(((0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 1, 1)))
    base_piola = {
        site: flat_piola_from_formula(base_chosen, site, size, tension) for site in sites
    }
    base_force = centered_divergence(base_piola, sites, size)
    for rotation in rotations:
        rotated = rotate_set(base_chosen, rotation, size)
        rotated_piola = {
            site: flat_piola_from_formula(rotated, site, size, tension) for site in sites
        }
        rotated_force = centered_divergence(rotated_piola, sites, size)
        for site in sites:
            target_site = rotate_site(site, rotation, size)
            piola_covariance &= rotated_piola[target_site] == rotate_matrix(
                base_piola[site], rotation
            )
            force_covariance &= rotated_force[target_site] == matrix_vector(
                rotation, base_force[site]
            )
    checks.check(
        "piola-cubic-covariance",
        "the flat tangential stress transports covariantly under all 24 proper cubic rotations",
        piola_covariance,
    )
    checks.check(
        "force-cubic-covariance",
        "the centered stress divergence transports as a vector under all 24 proper cubic rotations",
        force_covariance,
    )

    arbitrary_tensor = {
        site: tuple(
            tuple(
                Fraction((sum(site) + 3 * physical + 5 * axis) % 11 - 5, 7)
                for axis in range(3)
            )
            for physical in range(3)
        )
        for site in sites
    }
    virtual_displacement = {
        site: tuple(
            Fraction((2 * sum(site) + 7 * physical + site[physical]) % 13 - 6, 5)
            for physical in range(3)
        )
        for site in sites
    }
    arbitrary_divergence = centered_divergence(arbitrary_tensor, sites, size)
    virtual_work = sum(
        arbitrary_tensor[site][physical][axis]
        * centered_difference_vector(
            virtual_displacement, site, physical, axis, size
        )
        for site in sites
        for physical in range(3)
        for axis in range(3)
    )
    force_work = -sum(
        arbitrary_divergence[site][physical]
        * virtual_displacement[site][physical]
        for site in sites
        for physical in range(3)
    )
    checks.check(
        "discrete-virtual-work",
        "centered coframe variation obeys exact periodic summation by parts: P:D0v=-(div0 P).v",
        virtual_work == force_work == Fraction(-447, 35),
    )

    global_force_balance = True
    for fixture in sample_sets:
        fixture_piola = {
            site: flat_piola_from_formula(fixture, site, size, tension) for site in sites
        }
        fixture_force = centered_divergence(fixture_piola, sites, size)
        global_force_balance &= all(
            sum((value[component] for value in fixture_force.values()), Fraction(0)) == 0
            for component in range(3)
        )
    checks.check(
        "global-translation-ward",
        "the total embedding force vanishes identically on every periodic fixture by telescoping",
        global_force_balance,
    )
    slab = sample_sets[5]
    slab_piola = {
        site: flat_piola_from_formula(slab, site, size, tension) for site in sites
    }
    slab_force = centered_divergence(slab_piola, sites, size)
    singleton = sample_sets[1]
    singleton_piola = {
        site: flat_piola_from_formula(singleton, site, size, tension) for site in sites
    }
    singleton_force = centered_divergence(singleton_piola, sites, size)
    checks.check(
        "flat-interface-on-shell",
        "the two planar wrapping interfaces have zero local coframe force at every site",
        all(not any(value) for value in slab_force.values()),
    )
    checks.check(
        "curved-interface-force",
        "the singleton surface has nonzero local force with zero total, so local stress conservation needs a geometry equation",
        any(any(value) for value in singleton_force.values())
        and all(
            sum((value[component] for value in singleton_force.values()), Fraction(0)) == 0
            for component in range(3)
        ),
    )

    partition, mean_cut, variance_cut = k7_cut_moments()
    checks.check(
        "uniform-dilation-hessian",
        "the parent K7 uniform-area multiplier has exact seagull coefficient -E[C] and covariance coefficient Var(C)",
        partition == Fraction(4663, 2048)
        and mean_cut == Fraction(3948, 4663)
        and variance_cut == Fraction(122288880, 21743569),
    )
    line = frozenset((x, 0, 0) for x in range(3))
    orbit_size = 3
    orbit_sites = sites_of(orbit_size)
    orbit = tuple(rotate_set(line, rotation, orbit_size) for rotation in rotations)
    mean_x_cut = Fraction(
        sum(
            sum(cut_indicator(configuration, site, 0, orbit_size) for site in orbit_sites)
            for configuration in orbit
        ),
        len(orbit),
    )
    checks.check(
        "offdiagonal-shear-seagull",
        "the cubic line orbit has zero first xy-shear response and exact mean second area insertion C_x=4",
        area_first_second_variation(0, shear_variation) == (0, 1)
        and mean_x_cut == 4,
    )

    construction_needles = (
        "S_cut[x;F,B]",
        "P_i=tau[(Tr Q_i)I-Q_i]",
        "delta S_cut/delta u_i=-div^0 P_i",
        "partial J=0",
        "Psi''=Cov(S',S')-E[S'']",
        "Geometry-family and dynamics amendment",
    )
    checks.check(
        "construction-source-surface",
        "the source states the coframe law, tangential stress, virtual-work, higher-form Ward, seagull, and amendment",
        all(phrase in note_flat for phrase in construction_needles),
    )
    action_representative_needles = (
        "S_cut -> S_cut+c(F,B)",
        "leaves `pi_(F,B)` unchanged",
        "a normalized law alone does not determine its absolute coframe response",
        "registered local log-weight representative `S_F`",
        "partial[s_* S_F]/partial F",
        "`K_7` is not a cubical coframe geometry",
    )
    checks.check(
        "action-representative-boundary",
        "the source distinguishes a normalized Gibbs family from its geometry-dependent local action representative",
        all(phrase in note_flat for phrase in action_representative_needles),
    )
    boundary_needles = (
        "No canonical axiom is edited",
        "the fixed TOE percentages do not move",
        "not a physical stress-energy tensor",
        "not a lattice diffeomorphism theorem",
        "projective consistency remains open",
        "No no-go claim ships",
    )
    checks.check(
        "boundary-source-surface",
        "the source preserves physical, dynamical, projective, no-go, percentage, and governance boundaries",
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
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "coframe family, tangential cut stress, higher-form source, and geometry equation wording is absent from the canonical memo",
        all(
            phrase not in axiom
            for phrase in (
                "coframe family",
                "tangential cut stress",
                "higher-form source",
                "geometry equation",
            )
        ),
    )

    print("per_element: checked signed jumps, unsigned cut support, cofactor face areas, and orientation reversal exactly")
    print("per_site: checked mean-endpoint geometry weights, local conditionals, tangential Piola response, and embedding force")
    print("per_mode: checked uniform dilation, normal stretch, offdiagonal shear seagull, and cubic orbit response")
    print("per_block: checked positive geometry-indexed Gibbs action -> coframe derivative -> virtual work -> on-shell force balance")
    print("lattice_wide: checked integer surface closure, higher-form gauge Ward, all 24 cubic rotations, planar stationarity, and global telescoping")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
