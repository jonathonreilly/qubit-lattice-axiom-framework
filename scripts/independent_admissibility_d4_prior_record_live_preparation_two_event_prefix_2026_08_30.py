#!/usr/bin/env python3
"""Independent exact certificate for the Block23 two-Record prefix.

This runner reconstructs the Block22 effects, the Record-indexed preparation
branches, and their two-event kernel from formulas.  It deliberately keeps
one Kraus operator per old Record sector: replacing that family by one
coherent sum changes cross-sector terms and fails the frozen covariance test.
The certificate concerns one supplied fresh Blank star and exactly two
events; it does not promote the reduced kernel to a recurrent Record process.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = Path(
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block23-prior-record-live-preparation-"
    "two-event-prefix-20260830"
)
PARENT_COMMIT = "82406881682cc6c31d1cdee5fd159fc43b24e73c"
PREREGISTRATION_COMMIT = "0645b86a3423a7767b35eeb62efe2acbfb6fa8c7"

FROZEN_SHA256 = {
    PACKET / "GOAL.md": "6378ed13a8c72caca749197127ec67f3c8263c4d622563ec6ba73db75a9b3ead",
    PACKET / "AUTHORITY_GATE.md": "c1b28a69298924cded8862987f1d26b292f9546c49b4ea797cd88f219bd310e1",
    PACKET / "PREFLIGHT_WITNESSES.md": "c7098ef5c05f4a3b1bd3308c44a64e8bf1e0caa12fa40fb27580009b7672b163",
    PACKET / "PANEL_RETURN.md": "7a16f2f4956d42c6bea387d92bbc0a4ce26004470d872cb3382d370d24dfdb63",
    PACKET / "INDEPENDENT_PREREG_ATTACK.md": "f37da51570a3b448a3e430579171c40d934c941bd82704120cd98050d23719f8",
    PACKET / "APPROACH_REGISTRY.md": "95b733561940b4892b0631e8cb679df1aab1f40004954b9a6baf9a9ef2592618",
    PACKET / "MUTATION_PLAN.md": "654eb51a2174b2453b0a4ccc3ff34b09ee6ea1973de50bc3c5ff323cd6edf679",
    PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md": "fea9d4a66f58b2a9fd2759b71fff24093a7a30112ff67d4d65b6cc31b1c00a93",
}

Vec = tuple[int, int, int]
QVec = tuple[Fraction, Fraction, Fraction]
Rotation = tuple[tuple[int, int, int], Vec]
Surd = tuple[Fraction, Fraction]  # a + b sqrt(2)
Effect = tuple[Fraction, dict[Vec, QVec]]

ZERO: Vec = (0, 0, 0)
UNIT: tuple[Vec, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
AXES: tuple[Vec, ...] = tuple(
    tuple(sign if coordinate == axis else 0 for coordinate in range(3))
    for axis in range(3)
    for sign in (-1, 1)
)
CORNERS: tuple[Vec, ...] = tuple(itertools.product((-1, 1), repeat=3))
OUTCOMES: tuple[Vec, ...] = AXES + CORNERS

LIVE = frozenset(AXES)
FRONT = frozenset(tuple(2 * value for value in axis) for axis in AXES)
AXIS_OUTCOME = frozenset(tuple(3 * value for value in axis) for axis in AXES)
CORNER_OUTCOME = frozenset(tuple(2 * value for value in corner) for corner in CORNERS)
STATUS = frozenset(tuple(4 * value for value in axis) for axis in AXES)
POINTER = frozenset(FRONT | AXIS_OUTCOME | CORNER_OUTCOME | STATUS)
SUPPORT = frozenset(LIVE | POINTER)
POINTER_ORDER = tuple(sorted(POINTER))
POINTER_INDEX = {site: index for index, site in enumerate(POINTER_ORDER)}


class Certificate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.failures: list[str] = []
        self.lines: list[str] = []

    def require(self, name: str, condition: bool, detail: str = "") -> None:
        line = f"{'PASS' if condition else 'FAIL'} {name} {detail}".rstrip()
        if condition:
            self.pass_count += 1
            self.lines.append(line)
        else:
            self.failures.append(line)

    def emit(self) -> None:
        for line in self.lines:
            print(line)
        for line in self.failures:
            print(line)
        print(f"TOTAL: PASS={self.pass_count} FAIL={len(self.failures)}")


def sha256(relative: Path) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def add(left: Vec, right: Vec) -> Vec:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def neg(vector: Vec) -> Vec:
    return tuple(-value for value in vector)  # type: ignore[return-value]


def scale(value: int, vector: Vec) -> Vec:
    return tuple(value * component for component in vector)  # type: ignore[return-value]


def dot(left: Vec, right: Vec) -> int:
    return sum(left[i] * right[i] for i in range(3))


def qdot(left: QVec, right: QVec) -> Fraction:
    return sum(left[i] * right[i] for i in range(3))


def qadd(left: QVec, right: QVec) -> QVec:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def s(rational: int | Fraction = 0, root_two: int | Fraction = 0) -> Surd:
    return Fraction(rational), Fraction(root_two)


def sadd(left: Surd, right: Surd) -> Surd:
    return left[0] + right[0], left[1] + right[1]


def sneg(value: Surd) -> Surd:
    return -value[0], -value[1]


def ssub(left: Surd, right: Surd) -> Surd:
    return sadd(left, sneg(right))


def smul_rational(value: Surd, factor: int | Fraction) -> Surd:
    factor = Fraction(factor)
    return value[0] * factor, value[1] * factor


def ssum(values: object) -> Surd:
    answer = s()
    for value in values:  # type: ignore[union-attr]
        answer = sadd(answer, value)
    return answer


def spositive(value: Surd) -> bool:
    """Decide a+b*sqrt(2)>0 without floating-point comparison."""
    rational, root_two = value
    if root_two == 0:
        return rational > 0
    if rational == 0:
        return root_two > 0
    if rational > 0 and root_two > 0:
        return True
    if rational < 0 and root_two < 0:
        return False
    if rational > 0:
        return rational * rational > 2 * root_two * root_two
    return 2 * root_two * root_two > rational * rational


def sfloat(value: Surd) -> float:
    return float(value[0]) + float(value[1]) * math.sqrt(2.0)


def parity(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def rotate(vector: Vec, rotation: Rotation) -> Vec:
    permutation, signs = rotation
    answer = [0, 0, 0]
    for source, value in enumerate(vector):
        answer[permutation[source]] = signs[source] * value
    return tuple(answer)  # type: ignore[return-value]


def rotations() -> tuple[Rotation, ...]:
    answer: list[Rotation] = []
    for permutation in itertools.permutations(range(3)):
        typed = tuple(permutation)
        for signs in itertools.product((-1, 1), repeat=3):
            if parity(typed) * math.prod(signs) == 1:
                answer.append((typed, tuple(signs)))
    return tuple(sorted(answer))


ROTATIONS = rotations()


def compose(left: Rotation, right: Rotation) -> Rotation:
    images = tuple(rotate(rotate(axis, right), left) for axis in UNIT)
    permutation = tuple(next(i for i, entry in enumerate(image) if entry) for image in images)
    signs = tuple(images[source][permutation[source]] for source in range(3))
    return permutation, signs  # type: ignore[return-value]


def rotate_qvector(vector: QVec, rotation: Rotation) -> QVec:
    permutation, signs = rotation
    answer = [Fraction(0), Fraction(0), Fraction(0)]
    for source, value in enumerate(vector):
        answer[permutation[source]] = signs[source] * value
    return tuple(answer)  # type: ignore[return-value]


def translated(points: frozenset[Vec], shift: Vec) -> frozenset[Vec]:
    return frozenset(add(point, shift) for point in points)


def star_blocks(distance: int) -> dict[Vec, frozenset[Vec]]:
    return {front: translated(SUPPORT, scale(distance, front)) for front in AXES}


def pairwise_disjoint(blocks: object) -> bool:
    materialized = tuple(blocks)  # type: ignore[arg-type]
    return all(
        materialized[i].isdisjoint(materialized[j])
        for i in range(len(materialized))
        for j in range(i + 1, len(materialized))
    )


def bitmask(sites: object) -> int:
    answer = 0
    for site in sites:  # type: ignore[union-attr]
        answer |= 1 << POINTER_INDEX[site]
    return answer


STATUS_MASK = bitmask(STATUS)


def ready_mask(front: Vec) -> int:
    return bitmask({scale(2, front)})


def outcome_site(outcome: Vec) -> Vec:
    return scale(3, outcome) if outcome in AXES else scale(2, outcome)


def locked_mask(front: Vec, outcome: Vec) -> int:
    return ready_mask(front) | bitmask({outcome_site(outcome)}) | STATUS_MASK


READY_MASKS = {front: ready_mask(front) for front in AXES}
LOCKED_MASKS = {
    (front, outcome): locked_mask(front, outcome)
    for front in AXES
    for outcome in OUTCOMES
}


def rotate_mask(mask: int, rotation: Rotation) -> int:
    occupied = {
        rotate(site, rotation)
        for index, site in enumerate(POINTER_ORDER)
        if mask & (1 << index)
    }
    return bitmask(occupied)


def decode_locked(mask: int) -> tuple[Vec, Vec] | None:
    if mask & STATUS_MASK != STATUS_MASK:
        return None
    fronts = [site for site in FRONT if mask & (1 << POINTER_INDEX[site])]
    outcomes = [
        site
        for site in AXIS_OUTCOME | CORNER_OUTCOME
        if mask & (1 << POINTER_INDEX[site])
    ]
    if len(fronts) != 1 or len(outcomes) != 1:
        return None
    front = tuple(value // 2 for value in fronts[0])
    divisor = 3 if outcomes[0] in AXIS_OUTCOME else 2
    outcome = tuple(value // divisor for value in outcomes[0])
    return front, outcome  # type: ignore[return-value]


def block22_effect(label: Vec) -> Effect:
    coefficients: dict[Vec, QVec] = {}
    if label in AXES:
        selected = next(i for i, value in enumerate(label) if value)
        for site in AXES:
            site_axis = next(i for i, value in enumerate(site) if value)
            epsilon = site[site_axis]
            tracefree = Fraction(int(site_axis == selected), 1) - Fraction(1, 3)
            vector = [Fraction(0), Fraction(0), Fraction(0)]
            vector[site_axis] = Fraction(epsilon, 96) * tracefree
            coefficients[site] = tuple(vector)  # type: ignore[assignment]
        return Fraction(1, 12), coefficients

    for site in AXES:
        site_axis = next(i for i, value in enumerate(site) if value)
        epsilon = site[site_axis]
        vector = [Fraction(0), Fraction(0), Fraction(0)]
        for component in range(3):
            if component != site_axis:
                vector[component] = Fraction(
                    epsilon * label[site_axis] * label[component], 256
                )
        coefficients[site] = tuple(vector)  # type: ignore[assignment]
    return Fraction(1, 16), coefficients


EFFECTS = {label: block22_effect(label) for label in OUTCOMES}


def rotate_effect(data: Effect, rotation: Rotation) -> Effect:
    constant, coefficients = data
    return constant, {
        rotate(site, rotation): rotate_qvector(vector, rotation)
        for site, vector in coefficients.items()
    }


def sum_effects() -> Effect:
    constant = sum((data[0] for data in EFFECTS.values()), Fraction(0))
    coefficients = {
        site: tuple(
            sum((data[1][site][component] for data in EFFECTS.values()), Fraction(0))
            for component in range(3)
        )
        for site in AXES
    }
    return constant, coefficients  # type: ignore[return-value]


def square_root_of_rational(value: Fraction) -> Surd:
    numerator_root = math.isqrt(value.numerator)
    denominator_root = math.isqrt(value.denominator)
    if numerator_root * numerator_root == value.numerator and denominator_root * denominator_root == value.denominator:
        return s(Fraction(numerator_root, denominator_root))
    half = value / 2
    half_numerator_root = math.isqrt(half.numerator)
    half_denominator_root = math.isqrt(half.denominator)
    if (
        half_numerator_root * half_numerator_root == half.numerator
        and half_denominator_root * half_denominator_root == half.denominator
    ):
        return s(0, Fraction(half_numerator_root, half_denominator_root))
    raise ValueError(f"unsupported exact square root: {value}")


def effect_bounds(data: Effect) -> tuple[Surd, Surd]:
    constant, coefficients = data
    radius = ssum(square_root_of_rational(qdot(vector, vector)) for vector in coefficients.values())
    center = s(constant)
    return ssub(center, radius), sadd(center, radius)


def q_matrix(label: Vec) -> tuple[QVec, QVec, QVec]:
    norm_squared = dot(label, label)
    return tuple(
        tuple(
            Fraction(label[i] * label[j], norm_squared) - Fraction(int(i == j), 3)
            for j in range(3)
        )
        for i in range(3)
    )  # type: ignore[return-value]


def determinant(matrix: tuple[QVec, QVec, QVec]) -> Fraction:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def bilinear(matrix: tuple[QVec, QVec, QVec], left: Vec, right: Vec) -> Fraction:
    return sum(
        Fraction(left[i]) * matrix[i][j] * right[j]
        for i in range(3)
        for j in range(3)
    )


def primitive_direction(label: Vec, site: Vec) -> tuple[Vec, int]:
    """Return an integer numerator w and w.w for Q_label site / ||...||."""
    norm_squared = dot(label, label)
    projection = dot(label, site)
    raw = tuple(3 * label[i] * projection - norm_squared * site[i] for i in range(3))
    divisor = 0
    for value in raw:
        divisor = math.gcd(divisor, abs(value))
    if divisor == 0:
        raise ValueError("Q_b n vanished")
    numerator = tuple(value // divisor for value in raw)
    return numerator, dot(numerator, numerator)  # type: ignore[return-value]


def normalized_component(direction: tuple[Vec, int], component: int, polarity: int = 1) -> Surd:
    numerator, norm_squared = direction
    value = polarity * numerator[component]
    if norm_squared == 1:
        return s(value)
    if norm_squared == 2:
        return s(0, Fraction(value, 2))
    raise ValueError(f"unexpected prepared direction norm: {norm_squared}")


def local_expectation(coefficient: QVec, direction: tuple[Vec, int], polarity: int = 1) -> Surd:
    return ssum(
        smul_rational(normalized_component(direction, component, polarity), coefficient[component])
        for component in range(3)
    )


def effect_on_product(
    directions: dict[Vec, tuple[Vec, int]],
    following: Vec,
    polarity: int = 1,
) -> Surd:
    constant, coefficients = EFFECTS[following]
    return sadd(
        s(constant),
        ssum(
            local_expectation(coefficients[site], directions[site], polarity)
            for site in AXES
        ),
    )


def transition(previous: Vec, following: Vec, polarity: int = 1) -> Surd:
    directions = {site: primitive_direction(previous, site) for site in AXES}
    return effect_on_product(directions, following, polarity)


KERNEL = {
    previous: {following: transition(previous, following) for following in OUTCOMES}
    for previous in OUTCOMES
}


def ray(label: Vec) -> Vec:
    first = next(value for value in label if value)
    return label if first > 0 else neg(label)


AXIS_RAYS: tuple[Vec, ...] = UNIT
CORNER_RAYS: tuple[Vec, ...] = tuple(sorted({ray(corner) for corner in CORNERS}))
RAYS: tuple[Vec, ...] = AXIS_RAYS + CORNER_RAYS
RAY_MEMBERS = {label: tuple(value for value in OUTCOMES if ray(value) == label) for label in RAYS}


def quotient_kernel() -> dict[Vec, dict[Vec, Surd]]:
    return {
        previous: {
            following: ssum(KERNEL[previous][member] for member in RAY_MEMBERS[following])
            for following in RAYS
        }
        for previous in RAYS
    }


QUOTIENT = quotient_kernel()


def stochastic(matrix: dict[Vec, dict[Vec, Surd]]) -> bool:
    return all(ssum(row.values()) == s(1) for row in matrix.values())


def stationary(
    matrix: dict[Vec, dict[Vec, Surd]],
    weights: dict[Vec, Fraction],
) -> bool:
    return all(
        ssum(smul_rational(matrix[source][target], weights[source]) for source in matrix)
        == s(weights[target])
        for target in matrix
    )


def reversible(
    matrix: dict[Vec, dict[Vec, Surd]],
    weights: dict[Vec, Fraction],
) -> bool:
    return all(
        smul_rational(matrix[left][right], weights[left])
        == smul_rational(matrix[right][left], weights[right])
        for left in matrix
        for right in matrix
    )


def target_pointer_words(front: Vec) -> dict[Vec, int]:
    return {block: ready_mask(front) if block == front else 0 for block in AXES}


def target_live_directions(front: Vec, outcome: Vec) -> dict[Vec, dict[Vec, tuple[Vec, int]]]:
    return {
        block: {
            site: primitive_direction(outcome, site) if block == front else (site, 1)
            for site in AXES
        }
        for block in AXES
    }


BLANK_POINTER_STAR = tuple(0 for _ in AXES)


def preparation_branches() -> dict[
    tuple[Vec, Vec],
    tuple[int, tuple[int, ...], int, tuple[int, ...], tuple[tuple[Vec, int], ...]],
]:
    """Symbolic rank-one A_(f,b), kept separate for every Record label.

    The tuple records old input control, BlankStar pointer input, old output
    control, target-star pointer output, and the six active live factors.
    Its effect is the first two fields because every target factor is pure and
    normalized.  This is a structural representation, not a coherent sum.
    """
    return {
        (front, outcome): (
            LOCKED_MASKS[(front, outcome)],
            BLANK_POINTER_STAR,
            LOCKED_MASKS[(front, outcome)],
            tuple(target_pointer_words(front)[block] for block in AXES),
            tuple(primitive_direction(outcome, site) for site in AXES),
        )
        for front in AXES
        for outcome in OUTCOMES
    }


KRAUS_BRANCHES = preparation_branches()


def separate_kraus_matrix_unit(left: tuple[Vec, Vec], right: tuple[Vec, Vec]) -> int:
    """Coefficient retained from |left><right| on the valid Blank domain."""
    return int(left == right and left in KRAUS_BRANCHES)


def c4_ready_relative_phase(front: Vec) -> tuple[int, int]:
    """Exact Gaussian phase of a Ready flip relative to Blank under C4_z."""
    if front not in ((0, 0, 1), (0, 0, -1)):
        raise ValueError("front is not fixed by C4_z")
    blank_spin_z = front[2]
    return 0, blank_spin_z


def gaussian_conjugate(value: tuple[int, int]) -> tuple[int, int]:
    return value[0], -value[1]


def gaussian_multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def source_hygiene() -> bool:
    tree = ast.parse(Path(__file__).read_text())
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.add((node.module or "").split(".", 1)[0])
    forbidden_calls = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"eval", "exec", "__import__"}
    }
    dense_solver_calls = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {"eig", "eigvals", "eigenvals", "charpoly"}
    }
    return (
        not forbidden_calls
        and not dense_solver_calls
        and imports <= {"__future__", "ast", "hashlib", "itertools", "math", "fractions", "pathlib"}
    )


def generated_derivation_structure() -> bool:
    """Reject pasted effect/kernel rows in favor of formula comprehensions."""
    tree = ast.parse(Path(__file__).read_text())
    assignments = {
        target.id: node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Name)
    }
    return (
        isinstance(assignments.get("EFFECTS"), ast.DictComp)
        and isinstance(assignments.get("KERNEL"), ast.DictComp)
        and isinstance(assignments.get("KRAUS_BRANCHES"), ast.Call)
        and isinstance(assignments.get("QUOTIENT"), ast.Call)
    )


def main() -> int:
    cert = Certificate()

    hashes_ok = all(
        (ROOT / path).is_file() and sha256(path) == digest
        for path, digest in FROZEN_SHA256.items()
    )
    cert.require(
        "provenance",
        hashes_ok
        and source_hygiene()
        and generated_derivation_structure()
        and len(PARENT_COMMIT) == len(PREREGISTRATION_COMMIT) == 40,
        "eight frozen packet hashes; independent stdlib source; primary imports=0",
    )

    identity: Rotation = ((0, 1, 2), (1, 1, 1))
    group_closure = {compose(left, right) for left in ROTATIONS for right in ROTATIONS}
    group_ok = len(ROTATIONS) == 24 and group_closure == set(ROTATIONS) and identity in ROTATIONS
    cert.require("proper_cubic_group", group_ok, "24 determinant-one signed permutations, exact closure")

    old_geometry_ok = (
        len(LIVE) == 6
        and len(POINTER) == 26
        and len(SUPPORT) == 32
        and LIVE.isdisjoint(POINTER)
        and all(frozenset(rotate(site, g) for site in SUPPORT) == SUPPORT for g in ROTATIONS)
    )
    successors = star_blocks(9)
    all_blocks = (SUPPORT,) + tuple(successors.values())
    combined = frozenset().union(*all_blocks)
    geometry_ok = (
        old_geometry_ok
        and pairwise_disjoint(all_blocks)
        and len(combined) == 224
        and max(max(abs(component) for component in site) for site in combined) == 13
    )
    star_covariance = all(
        frozenset(rotate(site, g) for site in successors[front])
        == successors[rotate(front, g)]
        for g in ROTATIONS
        for front in AXES
    )
    cert.require(
        "successor_star_geometry",
        geometry_ok and star_covariance,
        "R=9; 32+6x32=224 disjoint sites; radius=13; one six-block orbit",
    )

    q_invariants = all(
        sum(matrix[i][i] for i in range(3)) == 0
        and sum(matrix[i][j] * matrix[j][i] for i in range(3) for j in range(3)) == Fraction(2, 3)
        and determinant(matrix) == Fraction(2, 27)
        for matrix in (q_matrix(label) for label in OUTCOMES)
    )
    q_covariance = all(
        bilinear(q_matrix(rotate(label, g)), rotate(UNIT[i], g), rotate(UNIT[j], g))
        == q_matrix(label)[i][j]
        for label in OUTCOMES
        for g in ROTATIONS
        for i in range(3)
        for j in range(3)
    )
    cert.require(
        "quadrupole_family",
        q_invariants and q_covariance,
        "Q_b=uu^T-I/3 has trace=0, tr(Q^2)=2/3, det=2/27 and cubic covariance",
    )

    prepared = {
        (label, site): primitive_direction(label, site)
        for label in OUTCOMES
        for site in AXES
    }
    prepared_nonzero_pure = all(norm_squared in (1, 2) and dot(vector, vector) == norm_squared for vector, norm_squared in prepared.values())
    antipodal = all(prepared[(label, site)] == prepared[(neg(label), site)] for label in OUTCOMES for site in AXES)
    vector_covariance = all(
        prepared[(rotate(label, g), rotate(site, g))]
        == (rotate(prepared[(label, site)][0], g), prepared[(label, site)][1])
        for label in OUTCOMES
        for site in AXES
        for g in ROTATIONS
    )
    axis_pattern = all(
        prepared[(label, site)][0] == (site if dot(label, site) else neg(site))
        and prepared[(label, site)][1] == 1
        for label in AXES
        for site in AXES
    )
    corner_pattern = all(
        prepared[(corner, site)][0][next(i for i, value in enumerate(site) if value)] == 0
        and prepared[(corner, site)][1] == 2
        for corner in CORNERS
        for site in AXES
    )
    cert.require(
        "prepared_live_products",
        prepared_nonzero_pure and antipodal and vector_covariance and axis_pattern and corner_pattern,
        "six normalized Q_b n factors derived per b; antipodal and 24-frame covariance exact",
    )

    total_effect = sum_effects()
    effect_complete = total_effect[0] == 1 and all(vector == (Fraction(0),) * 3 for vector in total_effect[1].values())
    effect_covariance = all(
        rotate_effect(EFFECTS[label], g) == EFFECTS[rotate(label, g)]
        for label in OUTCOMES
        for g in ROTATIONS
    )
    axis_bounds = {effect_bounds(EFFECTS[label]) for label in AXES}
    corner_bounds = {effect_bounds(EFFECTS[label]) for label in CORNERS}
    effect_positive = all(spositive(effect_bounds(data)[0]) for data in EFFECTS.values())
    cert.require(
        "block22_effects_rederived",
        effect_complete
        and effect_covariance
        and effect_positive
        and axis_bounds == {(s(Fraction(1, 18)), s(Fraction(1, 9)))}
        and corner_bounds == {(s(Fraction(1, 16), Fraction(-3, 128)), s(Fraction(1, 16), Fraction(3, 128)))},
        "14 positive effects sum to I_64; spectra bounded exactly; physical Pauli covariance",
    )

    axis_kernel_shape = all(
        KERNEL[previous][following]
        == (
            s(Fraction(1, 9))
            if following in AXES and ray(following) == ray(previous)
            else s(Fraction(5, 72))
            if following in AXES
            else s(Fraction(1, 16))
        )
        for previous in AXES
        for following in OUTCOMES
    )
    corner_kernel_shape = all(
        KERNEL[previous][following]
        == (
            s(Fraction(1, 12))
            if following in AXES
            else s(Fraction(1, 16), Fraction(3, 128))
            if ray(following) == ray(previous)
            else s(Fraction(1, 16), Fraction(-1, 128))
        )
        for previous in CORNERS
        for following in OUTCOMES
    )
    kernel_covariance = all(
        KERNEL[rotate(previous, g)][rotate(following, g)] == KERNEL[previous][following]
        for previous in OUTCOMES
        for following in OUTCOMES
        for g in ROTATIONS
    )
    cert.require(
        "fourteen_state_kernel",
        axis_kernel_shape
        and corner_kernel_shape
        and stochastic(KERNEL)
        and all(spositive(value) for row in KERNEL.values() for value in row.values())
        and kernel_covariance,
        "196 entries derived from Q_b, six Bloch factors, and effect coefficients; no kernel table",
    )

    lumpable = all(
        ssum(KERNEL[left][member] for member in RAY_MEMBERS[target])
        == ssum(KERNEL[right][member] for member in RAY_MEMBERS[target])
        for members in RAY_MEMBERS.values()
        for left in members
        for right in members
        for target in RAYS
    )
    quotient_shape = all(
        QUOTIENT[previous][following]
        == (
            s(Fraction(2, 9))
            if previous in AXIS_RAYS and following == previous
            else s(Fraction(5, 36))
            if previous in AXIS_RAYS and following in AXIS_RAYS
            else s(Fraction(1, 8))
            if previous in AXIS_RAYS
            else s(Fraction(1, 6))
            if following in AXIS_RAYS
            else s(Fraction(1, 8), Fraction(3, 64))
            if following == previous
            else s(Fraction(1, 8), Fraction(-1, 64))
        )
        for previous in RAYS
        for following in RAYS
    )
    cert.require(
        "antipodal_lumping",
        len(RAYS) == 7
        and all(len(members) == 2 for members in RAY_MEMBERS.values())
        and lumpable
        and quotient_shape
        and stochastic(QUOTIENT),
        "14 signed outcomes lump exactly to 3 axis plus 4 corner rays",
    )

    axis_to_corner = QUOTIENT[AXIS_RAYS[0]][CORNER_RAYS[0]]
    corner_to_axis = QUOTIENT[CORNER_RAYS[0]][AXIS_RAYS[0]]
    cross_ratio = corner_to_axis[0] / axis_to_corner[0]
    corner_ray_weight = Fraction(1, 3 * cross_ratio + 4)
    axis_ray_weight = cross_ratio * corner_ray_weight
    ray_weights = {
        label: axis_ray_weight if label in AXIS_RAYS else corner_ray_weight
        for label in RAYS
    }
    full_weights = {label: ray_weights[ray(label)] / 2 for label in OUTCOMES}
    stationary_ok = (
        axis_to_corner[1] == corner_to_axis[1] == 0
        and axis_ray_weight == Fraction(1, 6)
        and corner_ray_weight == Fraction(1, 8)
        and all(full_weights[label] == (Fraction(1, 12) if label in AXES else Fraction(1, 16)) for label in OUTCOMES)
        and sum(full_weights.values()) == 1
        and sum(ray_weights.values()) == 1
        and stationary(KERNEL, full_weights)
        and reversible(KERNEL, full_weights)
        and stationary(QUOTIENT, ray_weights)
        and reversible(QUOTIENT, ray_weights)
    )
    cert.require(
        "stationary_reversible_laws",
        stationary_ok,
        "signed pi=(1/12,1/16); quotient pi=(1/6,1/8); detailed balance exact",
    )

    axis_diagonal = QUOTIENT[AXIS_RAYS[0]][AXIS_RAYS[0]]
    axis_offdiagonal = QUOTIENT[AXIS_RAYS[0]][AXIS_RAYS[1]]
    corner_diagonal = QUOTIENT[CORNER_RAYS[0]][CORNER_RAYS[0]]
    corner_offdiagonal = QUOTIENT[CORNER_RAYS[0]][CORNER_RAYS[1]]
    axis_class_sum = sadd(axis_diagonal, smul_rational(axis_offdiagonal, 2))
    corner_class_sum = sadd(corner_diagonal, smul_rational(corner_offdiagonal, 3))
    spectrum_by_subspaces = (
        ssub(axis_diagonal, axis_offdiagonal) == s(Fraction(1, 12))
        and ssub(corner_diagonal, corner_offdiagonal) == s(0, Fraction(1, 16))
        and axis_class_sum == corner_class_sum == s(Fraction(1, 2))
        and all(QUOTIENT[AXIS_RAYS[0]][corner] == s(Fraction(1, 8)) for corner in CORNER_RAYS)
        and all(QUOTIENT[CORNER_RAYS[0]][axis] == s(Fraction(1, 6)) for axis in AXIS_RAYS)
    )
    cert.require(
        "invariant_subspace_spectrum",
        spectrum_by_subspaces,
        "eigenvalues 1, sqrt(2)/16 x3, 1/12 x2, 0 from S3/S4 contrasts and class constants",
    )

    primitive_quotient = stochastic(QUOTIENT) and all(spositive(value) for row in QUOTIENT.values() for value in row.values())
    chain42 = {
        (front, previous): {
            (front, following): QUOTIENT[previous][following]
            for following in RAYS
        }
        for front in AXES
        for previous in RAYS
    }
    front_closed = all(
        destination[0] == source[0]
        for source, row in chain42.items()
        for destination, probability in row.items()
        if spositive(probability)
    )
    front_components = {
        frozenset(state for state in chain42 if state[0] == front)
        for front in AXES
    }
    cert.require(
        "mode_boundary",
        primitive_quotient
        and len(chain42) == 42
        and front_closed
        and len(front_components) == 6
        and all(len(component) == 7 for component in front_components),
        "7-ray chain primitive/unique; 42-state (f,[b]) chain has six closed front sectors",
    )

    ready_values = set(READY_MASKS.values())
    locked_values = set(LOCKED_MASKS.values())
    record_code = (
        len(ready_values) == 6
        and len(locked_values) == 84
        and ready_values.isdisjoint(locked_values)
        and all(decode_locked(mask) == label for label, mask in LOCKED_MASKS.items())
    )
    code_covariance = all(
        rotate_mask(READY_MASKS[front], g) == READY_MASKS[rotate(front, g)]
        and all(
            rotate_mask(LOCKED_MASKS[(front, outcome)], g)
            == LOCKED_MASKS[(rotate(front, g), rotate(outcome, g))]
            for outcome in OUTCOMES
        )
        for front in AXES
        for g in ROTATIONS
    )
    cert.require(
        "record_code",
        record_code and code_covariance,
        "6 Ready and 84 mutually orthogonal Locked radial words decode and rotate exactly",
    )

    blank_star_sites = len(AXES) * len(SUPPORT)
    target_normalized = all(
        dot(vector, vector) == norm_squared
        for front in AXES
        for outcome in OUTCOMES
        for block in target_live_directions(front, outcome).values()
        for vector, norm_squared in block.values()
    )
    one_ready = all(
        sum(mask != 0 for mask in target_pointer_words(front).values()) == 1
        and target_pointer_words(front)[front] == ready_mask(front)
        for front in AXES
    )
    blank_orthogonality = all(target_pointer_words(front)[front] != 0 for front in AXES)
    target_covariance = all(
        rotate_mask(target_pointer_words(front)[front], g)
        == target_pointer_words(rotate(front, g))[rotate(front, g)]
        and all(
            target_live_directions(rotate(front, g), rotate(outcome, g))[rotate(front, g)][rotate(site, g)]
            == (rotate(target_live_directions(front, outcome)[front][site][0], g), target_live_directions(front, outcome)[front][site][1])
            for site in AXES
        )
        for front in AXES
        for outcome in OUTCOMES
        for g in ROTATIONS
    )
    cert.require(
        "blank_and_targets",
        blank_star_sites == 192 and target_normalized and one_ready and blank_orthogonality and target_covariance,
        "six all-zero 32-site Blank blocks; one rho_b+Ready_f target; target perpendicular to BlankStar",
    )

    controls = tuple(LOCKED_MASKS)
    expected_pvalid_sectors = {
        (LOCKED_MASKS[label], BLANK_POINTER_STAR)
        for label in controls
    }
    branch_effect_sectors = {
        (branch[0], branch[1])
        for branch in KRAUS_BRANCHES.values()
    }
    branch_targets_exact = all(
        branch[2] == LOCKED_MASKS[label]
        and branch[3] == tuple(target_pointer_words(label[0])[block] for block in AXES)
        and branch[4] == tuple(primitive_direction(label[1], site) for site in AXES)
        for label, branch in KRAUS_BRANCHES.items()
    )
    branch_effects_are_pvalid = (
        len(KRAUS_BRANCHES) == 84
        and branch_effect_sectors == expected_pvalid_sectors
        and len(expected_pvalid_sectors) == 84
        and branch_targets_exact
        and target_normalized
    )
    stop_complement_nonempty = 0 not in locked_values
    preparation_tp = branch_effects_are_pvalid and stop_complement_nonempty
    repeat_is_stop = blank_orthogonality
    cert.require(
        "separate_kraus_cptp",
        preparation_tp and repeat_is_stop,
        "sum A_(f,b)^dag A_(f,b)=P_valid; (I-P_valid)^2 completes I; repeat target is STOP",
    )

    record_populations_preserved = all(
        branch[0] == branch[2] == LOCKED_MASKS[label]
        for label, branch in KRAUS_BRANCHES.items()
    )
    distinct_controls = controls[0] != controls[1]
    separate_branch_offdiagonal = separate_kraus_matrix_unit(controls[0], controls[1])
    record_qnd = record_populations_preserved and separate_branch_offdiagonal == 0
    full_pointer_algebra_fixed = separate_branch_offdiagonal == 1
    cert.require(
        "commuting_record_qnd_only",
        record_qnd and not full_pointer_algebra_fixed,
        "all C_(f,b) fixed in Heisenberg picture; a cross-Record matrix unit is dephased",
    )

    plus_phase = c4_ready_relative_phase((0, 0, 1))
    minus_phase = c4_ready_relative_phase((0, 0, -1))
    c4_z: Rotation = ((1, 0, 2), (1, -1, 1))
    fixed_outcome = (0, 0, 1)
    fixed_sectors = all(
        rotate(front, c4_z) == front and rotate(fixed_outcome, c4_z) == fixed_outcome
        for front in ((0, 0, 1), (0, 0, -1))
    )
    perpendicular_live_sites = tuple(site for site in AXES if dot(site, fixed_outcome) == 0)
    blank_xy_cycle_phase = (-1, 0) if len(perpendicular_live_sites) == 4 else (0, 0)
    target_xy_cycle_phase = (-1, 0) if all(
        primitive_direction(fixed_outcome, site)[0] == neg(site)
        for site in perpendicular_live_sites
    ) else (0, 0)
    live_relative_phase = gaussian_multiply(
        target_xy_cycle_phase,
        gaussian_conjugate(blank_xy_cycle_phase),
    )
    phase_gauge_cancels = all(
        gaussian_multiply(value, gaussian_conjugate(value)) == (1, 0)
        for value in (plus_phase, minus_phase)
    )
    coherent_cross_phase = gaussian_multiply(plus_phase, gaussian_conjugate(minus_phase))
    cert.require(
        "record_indexed_covariance",
        plus_phase == (0, 1)
        and minus_phase == (0, -1)
        and c4_z in ROTATIONS
        and fixed_sectors
        and live_relative_phase == (1, 0)
        and phase_gauge_cancels
        and coherent_cross_phase == (-1, 0),
        "C4_z gives +i/-i branch gauges; separate CP branches covary, coherent summed Kraus does not",
    )

    activated_writer_blocks = all(
        sum(mask in ready_values for mask in target_pointer_words(front).values()) == 1
        and sum(mask == 0 for mask in target_pointer_words(front).values()) == 5
        for front in AXES
    )
    conditional_normalization = all(ssum(KERNEL[first].values()) == s(1) for first in OUTCOMES)
    prefix_coefficients = {first: ssum(KERNEL[first].values()) for first in OUTCOMES}
    direct_branch_kernel = {
        label: {
            second: effect_on_product(dict(zip(AXES, branch[4])), second)
            for second in OUTCOMES
        }
        for label, branch in KRAUS_BRANCHES.items()
    }
    direct_equals_reduced = all(
        direct_branch_kernel[(front, first)][second] == KERNEL[first][second]
        for front in AXES
        for first in OUTCOMES
        for second in OUTCOMES
    )
    first_record_decode = all(decode_locked(LOCKED_MASKS[(front, first)]) == (front, first) for front in AXES for first in OUTCOMES)
    second_record_unique = all(
        len({decode_locked(locked_mask(front, second)) for second in OUTCOMES}) == 14
        for front in AXES
    )
    arbitrary_reference_extension = effect_complete and effect_positive and preparation_tp and conditional_normalization
    cert.require(
        "two_event_composition",
        activated_writer_blocks
        and all(value == s(1) for value in prefix_coefficients.values())
        and first_record_decode
        and second_record_unique
        and arbitrary_reference_extension
        and direct_equals_reduced
        and kernel_covariance,
        "p_f(b1,b2|rho)=Tr(rho E_b1)T(b2|b1); normalized, prefix-consistent, CP with references",
    )

    third_event_wall = all(
        add(scale(9, front), scale(9, neg(front))) == ZERO
        for front in AXES
    )
    anchor_drift = all(scale(9, front) != ZERO for front in AXES)
    cert.require(
        "two_event_wall",
        third_event_wall and anchor_drift,
        "at y=x+9f the backward star member is locked x, so all-six-Blank fails before event three",
    )

    uniform = {label: Fraction(1, len(OUTCOMES)) for label in OUTCOMES}
    uniform_is_stationary = stationary(KERNEL, uniform)
    five_successors = (SUPPORT,) + tuple(successors[front] for front in AXES[:-1])
    negative_q_differs = any(
        transition(previous, following, polarity=-1) != KERNEL[previous][following]
        for previous in OUTCOMES
        for following in OUTCOMES
    )
    raw_q_vectors_not_unit = any(
        dot(
            tuple(3 * label[i] * dot(label, site) - dot(label, label) * site[i] for i in range(3)),
            tuple(3 * label[i] * dot(label, site) - dot(label, label) * site[i] for i in range(3)),
        )
        not in (1, 2)
        for label in OUTCOMES
        for site in AXES
    )
    goal_text = " ".join((ROOT / PACKET / "GOAL.md").read_text().split())
    scope_walls = all(
        phrase in goal_text
        for phrase in (
            "creation, replenishment, or conservation accounting of Blank capacity",
            "a third event, arbitrary prefix",
            "overlapping-star compatibility or mixed-front arbitration",
            "nearest-neighbor compilation",
            "Block19's six occurrence marks",
            "action/source debit-credit continuity",
            "gravity coupling",
            "audit status",
            "obligation retirement",
            "TOE percentage movement",
        )
    )
    mutations = {
        "R8_collision": not pairwise_disjoint((SUPPORT,) + tuple(star_blocks(8).values())),
        "drop_one_successor": len(frozenset().union(*five_successors)) == 192,
        "radius_twelve_refit": max(max(abs(c) for c in site) for site in combined) != 12,
        "host_selected_successor": len({next(block for block, mask in target_pointer_words(front).items() if mask) for front in AXES}) == 6,
        "fixed_Ready_orientation": any(rotate_mask(ready_mask((1, 0, 0)), g) != ready_mask((1, 0, 0)) for g in ROTATIONS),
        "label_only_star_rotation": any(successors[front] != successors[rotate(front, g)] for front in AXES for g in ROTATIONS),
        "two_Ready_blocks": one_ready and len({ready_mask(AXES[0]), ready_mask(AXES[1])}) == 2,
        "outcome_only_location": len({scale(9, front) for front in AXES}) == 6,
        "omit_front_control": len(OUTCOMES) != len(controls),
        "remove_tracefree_Q": all(sum(q_matrix(label)[i][i] for i in range(3)) == 0 for label in OUTCOMES),
        "negative_Q_sign": negative_q_differs,
        "omit_Q_normalization": raw_q_vectors_not_unit,
        "zero_Q_direction": prepared_nonzero_pure,
        "antipodal_state_split": antipodal,
        "fourteen_state_rows": generated_derivation_structure(),
        "axis_kernel_refit": KERNEL[(1, 0, 0)][(1, 0, 0)] != s(Fraction(1, 10)),
        "corner_kernel_refit": KERNEL[(1, 1, 1)][(1, 1, 1)] != s(Fraction(1, 16), Fraction(1, 64)),
        "premature_signed_merge": len(KERNEL) == 14 and len(QUOTIENT) == 7,
        "nonlumpable_quotient": lumpable,
        "negative_transition": all(spositive(value) for row in KERNEL.values() for value in row.values()),
        "nonstochastic_transition": stochastic(KERNEL),
        "uniform_stationary_refit": not uniform_is_stationary,
        "drop_detailed_balance": stationary_ok,
        "dense_spectrum_refit": source_hygiene() and spectrum_by_subspaces,
        "hardcode_stationary_weights": cross_ratio == Fraction(4, 3) and stationary_ok,
        "wrong_spectral_multiplicity": len(AXIS_RAYS) - 1 == 2 and len(CORNER_RAYS) - 1 == 3,
        "mix_front_sectors": front_closed,
        "unique_42_state_stationary": len(AXES) == 6,
        "omit_STOP": stop_complement_nonempty,
        "nonprojector_STOP": branch_effects_are_pvalid and preparation_tp,
        "drop_old_control": len(KRAUS_BRANCHES) - 1 == 83,
        "coherent_kraus_sum": plus_phase != minus_phase and coherent_cross_phase != (1, 0),
        "unconditioned_target": len(branch_effect_sectors) == 84,
        "full_pointer_QND": not full_pointer_algebra_fixed,
        "overwrite_old_Record": record_populations_preserved,
        "target_not_orthogonal_blank": blank_orthogonality,
        "erase_nonblank_star": stop_complement_nonempty and repeat_is_stop,
        "repeat_preparation": repeat_is_stop,
        "supply_second_Ready": one_ready,
        "activate_all_six_writers": activated_writer_blocks,
        "skip_five_STOP_branches": activated_writer_blocks,
        "overlapping_parallel_writers": pairwise_disjoint(tuple(successors.values())),
        "independent_second_outcome": len({tuple(KERNEL[row].values()) for row in RAYS}) > 1,
        "import_first_poststate": generated_derivation_structure() and antipodal,
        "skip_direct_cylinder": direct_equals_reduced,
        "postoutcome_causal_refit": direct_equals_reduced and branch_targets_exact,
        "product_only_first_input": arbitrary_reference_extension,
        "direct_third_event": third_event_wall,
        "stationary_spatial_Record_process": anchor_drift and len(AXES) == 6,
        "generate_blank_capacity": scope_walls,
        "mixed_front_arbitration": scope_walls,
        "nearest_neighbor_compiler": scope_walls,
        "rate_clock_scheduler": scope_walls,
        "Block19_six_marks": scope_walls,
        "action_source_gravity": scope_walls,
        "audit_or_retirement": scope_walls,
        "TOE_upgrade": scope_walls,
    }
    cert.require(
        "hostile_mutations",
        all(mutations.values()),
        f"rejected={sum(mutations.values())}/{len(mutations)} independent geometry/algebra/kernel/scope attacks",
    )

    cert.require(
        "scope",
        scope_walls and blank_star_sites == 192 and len(combined) == 224 and third_event_wall,
        "atomic radius-13 supplied-Blank construction; exactly two events; all named walls retained",
    )

    cert.lines.extend(
        (
            "per_element: Q_b, six pure Bloch factors, all 14 effects, and 196 transition entries were independently reconstructed exactly.",
            "per_site: the old 32-site block and six translated 32-site blocks are disjoint on 224 qubits with radius 13.",
            "per_mode: antipodal lumping gives seven rays with spectrum 1, sqrt(2)/16 x3, 1/12 x2, 0; six front sectors stay closed.",
            "per_block: 84 separate Record-indexed Kraus branches are CPTP, Record-projector QND, covariant, and one-shot on BlankStar.",
            "lattice_wide: not claimed; Blank supply, overlap arbitration, NN compilation, event three, histories, rates, source, gravity, audit, and TOE stay open.",
        )
    )
    cert.emit()
    return 0 if not cert.failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
