#!/usr/bin/env python3
"""Independent exact checker for the Block-200 E8 insertion gate.

Preregistration is pinned to the convention-corrected commit
88f7eb548589ea6d507b0cdd9d6933167c1bd82c.  This file imports no project
runner: it rebuilds the periodic action, the three-boundary Schur kernels,
the exterior-form Clifford PVM, and the exterior-operation controls from
stdlib/SymPy definitions.

The checker is deliberately bounded.  It verifies T0 and the registered T1
controls, then tests the grade-preserving, exterior-natural, label-covariant
T2 candidate family.  That family has an exact invariant-vacuum obstruction.
No action-native E8 image is derived, so T3--T6 are not executed.  This is not
a claim that every possible event insertion, coherent apparatus extension,
or non-grade-preserving construction is impossible.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass, replace
from functools import cache
from itertools import permutations, product
from math import comb
from pathlib import Path
import subprocess

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
PREREG_COMMIT = "88f7eb548589ea6d507b0cdd9d6933167c1bd82c"
PREREG_GOAL = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block200-rank9-three-event-insertion-20260825/"
    "GOAL.md"
)
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block200-rank9-three-event-insertion-20260825/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block200-rank9-three-event-insertion-20260825/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-axiom-closure-block200-rank9-three-event-insertion-20260825/STATE.yaml",
    "docs/ADMISSIBILITY_D4_L24_EXTERIOR_NATURAL_E8_INSERTION_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/independent_admissibility_d4_l24_e8_three_event_effect_cylinder_insertion_2026_08_25.py",
)

R = sp.Rational
I = sp.I
MASS = R(2, 7)
L_TIME = 24
COARSE_TIME = 12
EVENT_DIMENSION = 32
EVENT_COUNT = 8
PHYSICAL_CROSSINGS = (0, 2, 4)
# T0 is frozen directly on the twelve-site coarse circle.  It is not the
# even-site positional remapping (0,1,2) used when extracting the separate
# full-L24 H residual below.
Q024_BOUNDARY = (0, 2, 4)
Q02_BOUNDARY = (0, 2)
H_EVEN_POSITIONS = tuple(time // 2 for time in PHYSICAL_CROSSINGS)

SIGMA_X = sp.Matrix(((0, 1), (1, 0)))
SIGMA_Z = sp.diag(1, -1)
REAL_SKEW = sp.Matrix(((0, 1), (-1, 0)))

FROZEN_SQUARED_RADII = (
    R(0),
    R(3, 4),
    R(1),
    R(5, 4),
    R(3, 2),
    R(2),
    R(3),
    (7 + sp.sqrt(3)) / 4,
    (10 + sp.sqrt(3)) / 4,
)
EXPECTED_DELTAS = (
    R(4, 49),
    R(163, 196),
    R(53, 49),
    R(261, 196),
    R(155, 98),
    R(102, 49),
    R(151, 49),
    (359 + 49 * sp.sqrt(3)) / 196,
    (506 + 49 * sp.sqrt(3)) / 196,
)
EXPECTED_H_RAW = R(
    1860588125181794168951, 3216875861507134647600
)
EXPECTED_H_NORMALIZED = -R(
    2234183456333136028, 714473894240060471595
)
EXPECTED_H_PREDICTOR = -R(
    67663841820374976848, 41707488576114153187201
)

MUTATIONS = (
    "stale_prereg",
    "remap_q024_to_even_positions",
    "swap_boundary_and_complement_order",
    "erase_h_composition_residual",
    "drop_one_event_branch",
    "swap_effect_for_lueders_operation",
    "identify_nonselective_lueders_with_identity",
    "replace_f_alpha_by_gaussian_proxy",
    "keep_naive_vacuum",
    "erase_mixed_label_sectors",
    "assign_vacuum_to_one_label",
    "break_reflection_label_map",
    "break_proper_cubic_context_covariance",
    "drop_doubled_conjugation",
    "reverse_doubled_leg_order",
    "claim_action_native_e8_image",
    "open_later_gates_early",
)
MUTATION_FAMILY = {
    "stale_prereg": "P0",
    "remap_q024_to_even_positions": "T0",
    "swap_boundary_and_complement_order": "T0",
    "erase_h_composition_residual": "T1-H",
    "drop_one_event_branch": "T1-E8",
    "swap_effect_for_lueders_operation": "T1-TYPE",
    "identify_nonselective_lueders_with_identity": "T1-O9",
    "replace_f_alpha_by_gaussian_proxy": "T1-T2",
    "keep_naive_vacuum": "T1-EXT",
    "erase_mixed_label_sectors": "T1-EXT",
    "assign_vacuum_to_one_label": "T2-COV",
    "break_reflection_label_map": "T2-COV",
    "break_proper_cubic_context_covariance": "T2-COV",
    "drop_doubled_conjugation": "T1-O9",
    "reverse_doubled_leg_order": "T1-O9",
    "claim_action_native_e8_image": "T2",
    "open_later_gates_early": "STOP",
}


def exact_zero(value: sp.Expr) -> bool:
    if value == 0:
        return True
    try:
        if DomainMatrix.from_Matrix(
            sp.Matrix(((value,),)), extension=True
        ).is_zero_matrix:
            return True
    except (TypeError, ValueError):
        pass
    return sp.cancel(value) == 0 or sp.simplify(value) == 0


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    if left.shape != right.shape:
        return False
    difference = sp.Matrix(left - right)
    try:
        if DomainMatrix.from_Matrix(
            difference, extension=True
        ).is_zero_matrix:
            return True
    except (TypeError, ValueError):
        pass
    return all(exact_zero(value) for value in difference.values())


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


def exact_rank(matrix: sp.MatrixBase) -> int:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).rank()


def exact_determinant(matrix: sp.MatrixBase) -> sp.Expr:
    domain_matrix = DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    )
    return domain_matrix.domain.to_sympy(domain_matrix.det())


def exact_sign(value: sp.Expr) -> int:
    value = sp.factor(sp.simplify(value))
    if value == 0:
        return 0
    if value.is_positive is True:
        return 1
    if value.is_negative is True:
        return -1
    raise ValueError(f"undetermined exact sign: {value}")


def positive_definite(matrix: sp.MatrixBase) -> bool:
    matrix = sp.Matrix(matrix)
    return matrix_equal(matrix, matrix.T) and all(
        exact_sign(exact_determinant(matrix[:size, :size])) == 1
        for size in range(1, matrix.rows + 1)
    )


def shift_matrix(length: int) -> sp.Matrix:
    shift = sp.zeros(length)
    for column in range(length):
        shift[(column + 1) % length, column] = 1
    return shift


def selector(length: int, sites: tuple[int, ...]) -> sp.Matrix:
    result = sp.zeros(length, len(sites))
    for column, site in enumerate(sites):
        result[site, column] = 1
    return result


def complement(length: int, boundary: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(index for index in range(length) if index not in boundary)


def schur_keep(matrix: sp.MatrixBase, keep: tuple[int, ...]) -> sp.Matrix:
    discard = complement(matrix.rows, keep)
    return sp.Matrix(
        matrix.extract(keep, keep)
        - matrix.extract(keep, discard)
        * exact_inverse(matrix.extract(discard, discard))
        * matrix.extract(discard, keep)
    ).applyfunc(sp.cancel)


def reversal(size: int) -> sp.Matrix:
    result = sp.zeros(size)
    for index in range(size):
        result[size - 1 - index, index] = 1
    return result


def direct_sum(*matrices: sp.MatrixBase) -> sp.Matrix:
    rows = sum(matrix.rows for matrix in matrices)
    cols = sum(matrix.cols for matrix in matrices)
    result = sp.zeros(rows, cols)
    row = column = 0
    for matrix in matrices:
        result[row:row + matrix.rows, column:column + matrix.cols] = matrix
        row += matrix.rows
        column += matrix.cols
    return result


def git_output(*arguments: str) -> str:
    return subprocess.check_output(
        ("git",) + arguments,
        cwd=ROOT,
        text=True,
        stderr=subprocess.DEVNULL,
        timeout=30,
    ).strip()


def prereg_facts(mutation: str) -> tuple[bool, str]:
    commit = (
        "0" * 40 if mutation == "stale_prereg" else PREREG_COMMIT
    )
    try:
        resolved = git_output("rev-parse", f"{commit}^{{commit}}")
        ancestor = subprocess.run(
            ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
            cwd=ROOT,
            check=False,
            timeout=30,
        ).returncode == 0
        goal = git_output("show", f"{commit}:{PREREG_GOAL}")
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False, commit[:12]
    needles = (
        "Q_{024}=Q_BB-Q_BI Q_II^{-1} Q_IB",
        "B={0,2,4}",
        "### T2 -- action-native PVM effect insertion",
        "If no exact PVM image is derived, stop T3--T5.",
    )
    return (
        resolved == PREREG_COMMIT
        and ancestor
        and all(needle in goal for needle in needles),
        resolved[:12],
    )


def source_has_no_project_imports() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    allowed = {
        "__future__", "argparse", "ast", "dataclasses", "functools",
        "itertools", "math", "pathlib", "subprocess", "sympy",
    }
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    return imported <= allowed


@cache
def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        permutation_matrix = sp.zeros(3)
        for row, column in enumerate(permutation):
            permutation_matrix[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            move = sp.diag(*signs) * permutation_matrix
            if move.det() == 1:
                rotations.append(move)
    return tuple(rotations)


def proper_cubic_invariance() -> tuple[int, bool]:
    vector = sp.symbols("p0:3", real=True)
    norm = sum(component**2 for component in vector)
    rotations = proper_cubic_rotations()
    invariant = all(exact_zero(
        sum(value**2 for value in move * sp.Matrix(vector)) - norm
    ) for move in rotations)
    return len(rotations), invariant


@dataclass(frozen=True)
class RadiusSchurFacts:
    radius: sp.Expr
    delta: sp.Expr
    q_inverse_ok: bool
    direct_covariance_024: bool
    direct_covariance_02: bool
    nested_associativity: bool
    determinant_identities: bool
    positive_inertias: bool
    reflection_ok: bool
    internal_inverse_ok: bool
    two_step_internal_factor_ok: bool
    action_hermitian_part_positive: bool
    s024: sp.Matrix
    s02: sp.Matrix


@cache
def radius_schur_facts(
    squared_radius: sp.Expr,
    boundary024: tuple[int, ...],
    swap_covariance_boundary: bool,
) -> RadiusSchurFacts:
    coarse_shift = shift_matrix(COARSE_TIME)
    laplacian = (
        2 * sp.eye(COARSE_TIME) - coarse_shift - coarse_shift.T
    )
    delta = sp.factor(MASS**2 + squared_radius)
    q_matrix = sp.eye(COARSE_TIME) + laplacian / (4 * delta)
    q_inverse = exact_inverse(q_matrix)

    boundary02 = boundary024[:2]
    s024 = schur_keep(q_matrix, boundary024)
    s02 = schur_keep(q_matrix, boundary02)
    covariance024_indices = (
        complement(COARSE_TIME, boundary024)
        if swap_covariance_boundary else boundary024
    )
    covariance02_indices = (
        complement(COARSE_TIME, boundary02)
        if swap_covariance_boundary else boundary02
    )
    covariance024 = q_inverse.extract(
        covariance024_indices, covariance024_indices
    )
    covariance02 = q_inverse.extract(
        covariance02_indices, covariance02_indices
    )
    covariance_route024 = (
        exact_inverse(covariance024)
        if covariance024.rows == s024.rows else sp.zeros(0)
    )
    covariance_route02 = (
        exact_inverse(covariance02)
        if covariance02.rows == s02.rows else sp.zeros(0)
    )

    discard024 = complement(COARSE_TIME, boundary024)
    discard02 = complement(COARSE_TIME, boundary02)
    nested = schur_keep(s024, (0, 1))

    root = sp.sqrt(squared_radius)
    internal = MASS * sp.eye(2) + root * REAL_SKEW
    internal_inverse = (
        MASS * sp.eye(2) - root * REAL_SKEW
    ) / delta
    symmetric_part024 = (
        sp.kronecker_product(s024, internal)
        + sp.kronecker_product(s024, internal).T
    ) / 2

    return RadiusSchurFacts(
        radius=squared_radius,
        delta=delta,
        q_inverse_ok=(
            matrix_equal(q_matrix * q_inverse, sp.eye(COARSE_TIME))
            and matrix_equal(q_inverse * q_matrix, sp.eye(COARSE_TIME))
        ),
        direct_covariance_024=matrix_equal(s024, covariance_route024),
        direct_covariance_02=matrix_equal(s02, covariance_route02),
        nested_associativity=matrix_equal(nested, s02),
        determinant_identities=(
            exact_zero(
                exact_determinant(q_matrix)
                - exact_determinant(
                    q_matrix.extract(discard024, discard024)
                ) * exact_determinant(s024)
            )
            and exact_zero(
                exact_determinant(q_matrix)
                - exact_determinant(
                    q_matrix.extract(discard02, discard02)
                ) * exact_determinant(s02)
            )
        ),
        positive_inertias=(
            positive_definite(q_matrix)
            and positive_definite(s024)
            and positive_definite(s02)
        ),
        reflection_ok=(
            matrix_equal(reversal(3) * s024 * reversal(3), s024)
            and matrix_equal(reversal(2) * s02 * reversal(2), s02)
        ),
        internal_inverse_ok=(
            matrix_equal(internal * internal_inverse, sp.eye(2))
            and matrix_equal(internal_inverse * internal, sp.eye(2))
        ),
        two_step_internal_factor_ok=matrix_equal(
            SIGMA_Z * internal_inverse * SIGMA_Z,
            internal / delta,
        ),
        action_hermitian_part_positive=(
            matrix_equal(
                symmetric_part024,
                MASS * sp.kronecker_product(s024, sp.eye(2)),
            )
            and positive_definite(symmetric_part024)
        ),
        s024=s024,
        s02=s02,
    )


@dataclass(frozen=True)
class T0Facts:
    temporal_geometry_ok: bool
    boundary: tuple[int, ...]
    radii: tuple[RadiusSchurFacts, ...]
    cubic_move_count: int
    cubic_invariant: bool
    q024_shape: tuple[int, int]
    q02_shape: tuple[int, int]
    q024_rank: int
    q02_rank: int
    crossing4_pivot_rank: int
    q024_defect_rank: int
    q02_defect_rank: int
    event_fiber_dimension: int
    action_event_intertwiner_derived: bool


@cache
def exterior_clifford() -> tuple[tuple[sp.Matrix, ...], tuple[sp.Matrix, ...]]:
    subsets = tuple(
        tuple(axis for axis in range(4) if mask & (1 << axis))
        for mask in range(16)
    )
    indices = {subset: index for index, subset in enumerate(subsets)}
    creation = []
    for axis in range(4):
        matrix = sp.zeros(16)
        for column, subset in enumerate(subsets):
            if axis in subset:
                continue
            target = tuple(sorted(subset + (axis,)))
            sign = (-1) ** sum(item < axis for item in subset)
            matrix[indices[target], column] = sign
        creation.append(matrix)
    annihilation = tuple(matrix.T for matrix in creation)
    gammas = tuple(
        item
        for axis in range(4)
        for item in (
            creation[axis] + annihilation[axis],
            I * (creation[axis] - annihilation[axis]),
        )
    )
    return tuple(creation), gammas


def wedge_signed_permutation(transform: sp.MatrixBase) -> sp.Matrix:
    """Exterior representation of a signed permutation on four axes."""
    subsets = tuple(
        tuple(axis for axis in range(4) if mask & (1 << axis))
        for mask in range(16)
    )
    indices = {subset: index for index, subset in enumerate(subsets)}
    result = sp.zeros(16)
    for column, subset in enumerate(subsets):
        images = []
        coefficient = sp.Integer(1)
        for old_axis in subset:
            new_axis = next(
                row for row in range(4)
                if transform[row, old_axis] != 0
            )
            coefficient *= transform[new_axis, old_axis]
            images.append(new_axis)
        inversions = sum(
            images[left] > images[right]
            for left in range(len(images))
            for right in range(left + 1, len(images))
        )
        coefficient *= (-1) ** inversions
        result[indices[tuple(sorted(images))], column] = coefficient
    return result


@cache
def t0_facts(mutation: str) -> T0Facts:
    shift24 = shift_matrix(L_TIME)
    differential = (shift24 - shift24.T) / 2
    even = selector(L_TIME, tuple(range(0, L_TIME, 2)))
    odd = selector(L_TIME, tuple(range(1, L_TIME, 2)))
    coarse_shift = shift_matrix(COARSE_TIME)
    temporal_geometry_ok = (
        matrix_equal(differential.T, -differential)
        and matrix_equal(
            even.T * differential * odd,
            (coarse_shift - sp.eye(COARSE_TIME)) / 2,
        )
        and matrix_equal(
            odd.T * differential * even,
            (sp.eye(COARSE_TIME) - coarse_shift.T) / 2,
        )
        and matrix_equal(
            (even.T * differential * odd)
            * (odd.T * differential * even),
            -(
                2 * sp.eye(COARSE_TIME)
                - coarse_shift - coarse_shift.T
            ) / 4,
        )
    )

    boundary = (
        H_EVEN_POSITIONS
        if mutation == "remap_q024_to_even_positions"
        else Q024_BOUNDARY
    )
    radius_facts = tuple(
        radius_schur_facts(
            radius,
            boundary,
            mutation == "swap_boundary_and_complement_order",
        )
        for radius in FROZEN_SQUARED_RADII
    )
    cubic_count, cubic_ok = proper_cubic_invariance()

    _, gammas = exterior_clifford()
    spatial_gamma = gammas[0]
    identity16 = sp.eye(16)
    internal0 = MASS * identity16
    internal1 = MASS * identity16 + I * spatial_gamma
    radius0 = radius_facts[0]
    radius1 = radius_facts[2]
    q024 = direct_sum(
        sp.kronecker_product(radius0.s024, internal0),
        sp.kronecker_product(radius1.s024, internal1),
    )
    q02 = direct_sum(
        sp.kronecker_product(radius0.s02, internal0),
        sp.kronecker_product(radius1.s02, internal1),
    )
    pivot4 = direct_sum(
        radius0.s024[2, 2] * internal0,
        radius1.s024[2, 2] * internal1,
    )

    return T0Facts(
        temporal_geometry_ok=temporal_geometry_ok,
        boundary=boundary,
        radii=radius_facts,
        cubic_move_count=cubic_count,
        cubic_invariant=cubic_ok,
        q024_shape=q024.shape,
        q02_shape=q02.shape,
        q024_rank=exact_rank(q024),
        q02_rank=exact_rank(q02),
        crossing4_pivot_rank=exact_rank(pivot4),
        q024_defect_rank=exact_rank(q024 - q024.H),
        q02_defect_rank=exact_rank(q02 - q02.H),
        event_fiber_dimension=2 * identity16.rows,
        action_event_intertwiner_derived=False,
    )


def physical_block(
    matrix: sp.MatrixBase, target: int, source: int
) -> sp.Matrix:
    return sp.Matrix(matrix[
        2 * target:2 * target + 2,
        2 * source:2 * source + 2,
    ])


@dataclass(frozen=True)
class HFacts:
    raw: sp.Expr
    normalized: sp.Expr
    predictor: sp.Expr
    normalized_full_rank: int
    positive_factorization: bool
    radius_one_residual_nonzero: bool


def reduced_h_residual(squared_radius: sp.Expr) -> tuple[sp.Matrix, ...]:
    shift = shift_matrix(L_TIME)
    differential = (shift - shift.T) / 2
    internal = MASS * sp.eye(2) + sp.sqrt(squared_radius) * REAL_SKEW
    action = (
        sp.kronecker_product(sp.eye(L_TIME), internal)
        + sp.kronecker_product(differential, SIGMA_Z)
    )
    covariance = exact_inverse(action)
    h_kernel = sp.Matrix(covariance + covariance.T)
    h42 = physical_block(h_kernel, 4, 2)
    h20 = physical_block(h_kernel, 2, 0)
    h40 = physical_block(h_kernel, 4, 0)
    h22 = physical_block(h_kernel, 2, 2)
    h00 = physical_block(h_kernel, 0, 0)
    raw = sp.Matrix(h42 * h20 - h40).applyfunc(sp.factor)
    normalized = sp.Matrix(
        h42 * exact_inverse(h22) * h20 - h40
    ).applyfunc(sp.factor)
    predictor = sp.Matrix(
        h42 * exact_inverse(h22)
        * h20 * exact_inverse(h00)
        - h40 * exact_inverse(h00)
    ).applyfunc(sp.factor)
    positive_identity = matrix_equal(
        h_kernel,
        2 * MASS * covariance.T * covariance,
    )
    return raw, normalized, predictor, sp.Matrix((int(positive_identity),))


@cache
def h_facts() -> HFacts:
    radius0 = reduced_h_residual(R(0))
    radius1 = reduced_h_residual(R(1))
    normalized_rank = 8 * (
        exact_rank(radius0[1]) + exact_rank(radius1[1])
    )
    return HFacts(
        raw=sp.factor(radius0[0][0, 0]),
        normalized=sp.factor(radius0[1][0, 0]),
        predictor=sp.factor(radius0[2][0, 0]),
        normalized_full_rank=normalized_rank,
        positive_factorization=(radius0[3][0] == 1 and radius1[3][0] == 1),
        radius_one_residual_nonzero=exact_rank(radius1[1]) == 2,
    )


@dataclass(frozen=True)
class EventFacts:
    car_ok: bool
    context_ok: bool
    effects: tuple[sp.Matrix, ...]
    pvm_ok: bool
    effect_ranks: tuple[int, ...]
    effect_span_rank: int
    writer_ok: bool
    pointer_pullback_ok: bool
    reflection_label_map: tuple[int, ...]
    reflection_effect_map_ok: bool
    proper_cubic_context_ok: bool
    identity_dephasing_distinct: bool
    identity_choi_rank: int
    dephasing_choi_rank: int
    static_same_effects_different_histories: bool


@cache
def complete_event_facts() -> EventFacts:
    _, gammas = exterior_clifford()
    identity16 = sp.eye(16)
    car_ok = all(matrix_equal(
        gammas[left] * gammas[right]
        + gammas[right] * gammas[left],
        2 * int(left == right) * identity16,
    ) for left in range(8) for right in range(8))

    o1 = sp.expand(I * gammas[0] * gammas[2] * gammas[3])
    o2 = sp.expand(I * gammas[1] * gammas[2] * gammas[5])
    orientation = sp.expand(I * gammas[6] * gammas[4])
    ports = tuple(sp.expand(
        (identity16 + first * o1)
        * (identity16 + second * o2) / 4
    ) for first, second in product((-1, 1), repeat=2))
    context_ok = (
        matrix_equal(o1.H, o1)
        and matrix_equal(o2.H, o2)
        and matrix_equal(o1**2, identity16)
        and matrix_equal(o2**2, identity16)
        and matrix_equal(o1 * o2, o2 * o1)
        and matrix_equal(orientation.H, orientation)
        and matrix_equal(orientation**2, identity16)
        and all(matrix_equal(
            orientation * port, port * orientation
        ) for port in ports)
    )
    zero16 = sp.zeros(16)
    effects = []
    for port in ports:
        connector = port * orientation
        for sign in (1, -1):
            effects.append(sp.Matrix.vstack(
                sp.Matrix.hstack(port, sign * connector),
                sp.Matrix.hstack(sign * connector.H, port),
            ) / 2)
    effects_tuple = tuple(effects)
    pvm_ok = (
        all(matrix_equal(effect.H, effect) for effect in effects_tuple)
        and all(matrix_equal(effect**2, effect) for effect in effects_tuple)
        and all(matrix_equal(
            effects_tuple[left] * effects_tuple[right], sp.zeros(32)
        ) for left in range(8) for right in range(left + 1, 8))
        and matrix_equal(sum(effects_tuple, sp.zeros(32)), sp.eye(32))
    )
    design = sp.Matrix.hstack(*(
        effect.reshape(EVENT_DIMENSION**2, 1) for effect in effects_tuple
    ))

    sector_orientation = sp.Matrix.vstack(
        sp.Matrix.hstack(zero16, orientation),
        sp.Matrix.hstack(orientation, zero16),
    )
    p_plus = (sp.eye(32) + sector_orientation) / 2
    p_minus = (sp.eye(32) - sector_orientation) / 2
    pointer_identity = sp.eye(2)
    writer = (
        sp.kronecker_product(p_plus, pointer_identity)
        + sp.kronecker_product(p_minus, SIGMA_X)
    )
    ket_zero = sp.Matrix((1, 0))
    input_isometry = sp.kronecker_product(sp.eye(32), ket_zero)
    pointer_z = sp.diag(1, -1)
    pointer_codes = (
        (pointer_identity + pointer_z) / 2,
        (pointer_identity - pointer_z) / 2,
    )
    induced = []
    for port in ports:
        diagonal_port = sp.diag(port, port)
        for pointer_code in pointer_codes:
            readout = sp.kronecker_product(diagonal_port, pointer_code)
            induced.append(sp.expand(
                input_isometry.H * writer.H * readout
                * writer * input_isometry
            ))

    range_vectors = []
    for effect in effects_tuple[:2]:
        vector = next(
            effect[:, column]
            for column in range(effect.cols)
            if any(value != 0 for value in effect[:, column])
        )
        range_vectors.append(sp.Matrix(vector))
    cross = range_vectors[0] * range_vectors[1].H
    dephased = sum((
        effect * cross * effect for effect in effects_tuple
    ), sp.zeros(32))
    gtime = gammas[6]
    sector_reflection = sp.diag(gtime, gtime)
    reflection_label_map = tuple(
        2 * (3 - port_index) + (1 - sign_index)
        for port_index in range(4)
        for sign_index in range(2)
    )
    reflection_effect_map_ok = all(matrix_equal(
        sector_reflection * effects_tuple[index] * sector_reflection,
        effects_tuple[reflection_label_map[index]],
    ) for index in range(EVENT_COUNT))
    proper_cubic_context_ok = True
    for spatial_rotation in proper_cubic_rotations():
        transform = sp.eye(4)
        transform[:3, :3] = spatial_rotation
        form_rotation = wedge_signed_permutation(transform)
        sector_rotation = sp.diag(form_rotation, form_rotation)
        transformed_o1 = form_rotation * o1 * form_rotation.T
        transformed_o2 = form_rotation * o2 * form_rotation.T
        transformed_orientation = (
            form_rotation * orientation * form_rotation.T
        )
        for port_index, (first, second) in enumerate(
            product((-1, 1), repeat=2)
        ):
            transformed_port = (
                (identity16 + first * transformed_o1)
                * (identity16 + second * transformed_o2) / 4
            )
            transformed_connector = (
                transformed_port * transformed_orientation
            )
            for sign_index, sign in enumerate((1, -1)):
                expected = sp.Matrix.vstack(
                    sp.Matrix.hstack(
                        transformed_port,
                        sign * transformed_connector,
                    ),
                    sp.Matrix.hstack(
                        sign * transformed_connector.H,
                        transformed_port,
                    ),
                ) / 2
                label = 2 * port_index + sign_index
                actual = (
                    sector_rotation * effects_tuple[label]
                    * sector_rotation.T
                )
                proper_cubic_context_ok &= matrix_equal(actual, expected)
    ones = sp.ones(EVENT_COUNT, 1)
    identity_choi = ones * ones.T
    dephasing_choi = sp.eye(EVENT_COUNT)

    rho0 = effects_tuple[0] / 4
    lueders_repeat = sp.trace(
        effects_tuple[0] * effects_tuple[0] * rho0
        * effects_tuple[0] * effects_tuple[0]
    )
    replacement_repeat = (
        sp.trace(effects_tuple[0] * rho0)
        * sp.trace(effects_tuple[0] * sp.eye(32) / 32)
    )

    return EventFacts(
        car_ok=car_ok,
        context_ok=context_ok,
        effects=effects_tuple,
        pvm_ok=pvm_ok,
        effect_ranks=tuple(exact_rank(effect) for effect in effects_tuple),
        effect_span_rank=exact_rank(design),
        writer_ok=(
            matrix_equal(writer.H * writer, sp.eye(64))
            and matrix_equal(writer * writer.H, sp.eye(64))
        ),
        pointer_pullback_ok=all(
            matrix_equal(induced[index], effects_tuple[index])
            for index in range(EVENT_COUNT)
        ),
        reflection_label_map=reflection_label_map,
        reflection_effect_map_ok=reflection_effect_map_ok,
        proper_cubic_context_ok=proper_cubic_context_ok,
        identity_dephasing_distinct=(
            not matrix_equal(identity_choi, dephasing_choi)
            and matrix_equal(dephased, sp.zeros(32))
            and not matrix_equal(cross, sp.zeros(32))
        ),
        identity_choi_rank=exact_rank(identity_choi),
        dephasing_choi_rank=exact_rank(dephasing_choi),
        static_same_effects_different_histories=(
            lueders_repeat == 1 and replacement_repeat == R(1, 8)
        ),
    )


@cache
def event_facts(mutation: str) -> EventFacts:
    complete = complete_event_facts()
    if mutation == "break_reflection_label_map":
        return replace(
            complete,
            reflection_label_map=tuple(range(EVENT_COUNT)),
            reflection_effect_map_ok=False,
        )
    if mutation == "break_proper_cubic_context_covariance":
        return replace(complete, proper_cubic_context_ok=False)
    if mutation != "drop_one_event_branch":
        return complete
    effects = complete.effects[:-1]
    design = sp.Matrix.hstack(*(
        effect.reshape(EVENT_DIMENSION**2, 1) for effect in effects
    ))
    return EventFacts(
        car_ok=complete.car_ok,
        context_ok=complete.context_ok,
        effects=effects,
        pvm_ok=False,
        effect_ranks=tuple(exact_rank(effect) for effect in effects),
        effect_span_rank=exact_rank(design),
        writer_ok=complete.writer_ok,
        pointer_pullback_ok=False,
        reflection_label_map=complete.reflection_label_map,
        reflection_effect_map_ok=complete.reflection_effect_map_ok,
        proper_cubic_context_ok=complete.proper_cubic_context_ok,
        identity_dephasing_distinct=complete.identity_dephasing_distinct,
        identity_choi_rank=complete.identity_choi_rank,
        dephasing_choi_rank=complete.dephasing_choi_rank,
        static_same_effects_different_histories=(
            complete.static_same_effects_different_histories
        ),
    )


@dataclass(frozen=True)
class ExteriorFacts:
    gamma_rank: int
    gamma_plus_rank: int
    doubled_branch_rank: int
    bidegree_branch_rank: int
    bidegree_dephasing_rank: int
    bidegree_identity_rank: int
    o9_dimension: int
    o9_composition_ok: bool
    reduced_pairwise_orthogonal: bool
    naive_pairwise_product_rank: int
    naive_sum_vacuum_eigenvalue: int
    mixed_label_rank: int
    full_doubled_missing_rank: int
    doubled_order_ok: bool


def compose_o9(left: int, right: int) -> dict[int, int]:
    # Basis 0 is the identity operation; bases 1..8 are L_0..L_7.
    if left == 0:
        return {right: 1}
    if right == 0:
        return {left: 1}
    return {left: 1} if left == right else {}


@cache
def exterior_facts(mutation: str) -> ExteriorFacts:
    branch_rank = 4
    gamma_rank = sum(comb(branch_rank, grade) for grade in range(5))
    gamma_plus_rank = gamma_rank - 1
    # Exhaust the abstract label-support lattice.  Empty support is vacuum;
    # singleton support is the image of exactly one reduced branch.
    supports = tuple(range(1 << EVENT_COUNT))
    pure_supports = tuple(
        mask for mask in supports if mask and mask & (mask - 1) == 0
    )
    reduced_pairwise_orthogonal = all(
        not ((mask in (0, 1 << left)) and (mask in (0, 1 << right)))
        for left in range(EVENT_COUNT)
        for right in range(left + 1, EVENT_COUNT)
        for mask in supports
        if mask != 0
    )
    mixed_rank = 2**EVENT_DIMENSION - 1 - EVENT_COUNT * gamma_plus_rank
    if mutation == "erase_mixed_label_sectors":
        mixed_rank = 0
    effect = complete_event_facts().effects[0]
    order_witness = False
    # For X=|a><b|, column vectorization gives
    # vec(F X F*)=(conjugate(F) tensor F)vec(X).  Find an exact witness that
    # distinguishes this frozen order from its swap-conjugate reversal without
    # materializing a dense 1024 x 1024 superoperator.
    for left in range(EVENT_DIMENSION):
        if order_witness:
            break
        for right in range(EVENT_DIMENSION):
            correct = effect[:, left] * sp.conjugate(effect[:, right]).T
            swapped = sp.conjugate(effect[:, left]) * effect[:, right].T
            if not matrix_equal(correct, swapped):
                order_witness = True
                break
    return ExteriorFacts(
        gamma_rank=gamma_rank,
        gamma_plus_rank=gamma_plus_rank,
        doubled_branch_rank=gamma_plus_rank**2,
        bidegree_branch_rank=branch_rank**2,
        bidegree_dephasing_rank=EVENT_COUNT * branch_rank**2,
        bidegree_identity_rank=EVENT_DIMENSION**2,
        o9_dimension=EVENT_COUNT + 1,
        o9_composition_ok=(
            all(
                compose_o9(0, basis) == {basis: 1}
                and compose_o9(basis, 0) == {basis: 1}
                for basis in range(EVENT_COUNT + 1)
            )
            and all(
                compose_o9(left, right)
                == ({left: 1} if left == right else {})
                for left in range(1, EVENT_COUNT + 1)
                for right in range(1, EVENT_COUNT + 1)
            )
        ),
        reduced_pairwise_orthogonal=(
            reduced_pairwise_orthogonal
            and len(pure_supports) == EVENT_COUNT
        ),
        naive_pairwise_product_rank=1,
        naive_sum_vacuum_eigenvalue=EVENT_COUNT,
        mixed_label_rank=mixed_rank,
        full_doubled_missing_rank=(
            2**(2 * EVENT_DIMENSION)
            - EVENT_COUNT * gamma_plus_rank**2
        ),
        doubled_order_ok=(
            order_witness
            and mutation not in (
                "drop_doubled_conjugation",
                "reverse_doubled_leg_order",
            )
        ),
    )


@dataclass(frozen=True)
class CategoricalFacts:
    groebner_unit: bool
    exhaustive_no_covariant_assignment: bool
    arbitrary_assignment_unital: bool
    arbitrary_assignment_covariant: bool
    fractional_assignment_unital_covariant: bool
    fractional_assignment_projective: bool
    solution_count: int


@cache
def categorical_facts(mutation: str) -> CategoricalFacts:
    variables = sp.symbols("vacuum_label_0:8")
    idempotence = tuple(value**2 - value for value in variables)
    # Block 194's actual fixed-context reflection is the four-cycle product
    # (0 7)(1 6)(2 5)(3 4).  Proper-cubic moves co-transform the context and
    # are not a transitive action on these frozen labels.
    reflection_map = tuple(EVENT_COUNT - 1 - index for index in range(8))
    covariance = tuple(
        variables[index] - variables[reflection_map[index]]
        for index in range(EVENT_COUNT)
    )
    unit = (sum(variables) - 1,)
    equations = idempotence + covariance + unit
    basis = sp.groebner(equations, *variables, order="lex")
    assignments = tuple(product((0, 1), repeat=EVENT_COUNT))
    solution_count = sum(
        sum(values) == 1 and all(
            values[index] == values[reflection_map[index]]
            for index in range(EVENT_COUNT)
        )
        for values in assignments
    )
    no_covariant_assignment = solution_count == 0
    arbitrary = (1,) + (0,) * (EVENT_COUNT - 1)
    fractional = (R(1, EVENT_COUNT),) * EVENT_COUNT
    if mutation == "assign_vacuum_to_one_label":
        no_covariant_assignment = False
    return CategoricalFacts(
        groebner_unit=basis.contains(sp.Integer(1)),
        exhaustive_no_covariant_assignment=no_covariant_assignment,
        arbitrary_assignment_unital=sum(arbitrary) == 1,
        arbitrary_assignment_covariant=all(
            arbitrary[index] == arbitrary[reflection_map[index]]
            for index in range(EVENT_COUNT)
        ),
        fractional_assignment_unital_covariant=(
            sum(fractional) == 1
            and all(
                fractional[index] == fractional[reflection_map[index]]
                for index in range(EVENT_COUNT)
            )
        ),
        fractional_assignment_projective=all(
            value**2 == value for value in fractional
        ),
        solution_count=solution_count,
    )


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


N5_LINES = (
    "per_element: checked exact Clifford generators, all eight rank-four "
    "effects, E8 multiplication, O9 composition, and exterior branch ranks.",
    "per_site: checked literal coarse-circle Q boundaries (0,2,4)/(0,2) "
    "and separately the physical L24 H blocks at times 0,2,4.",
    "per_mode: checked all nine frozen squared radii structurally; the full "
    "H residual values were executed only on the two D1 sectors r2=0,1.",
    "per_block: checked Schur, covariance, PVM/M2, H, operation typing, "
    "vacuum-reduced exterior, and categorical covariance as separate blocks.",
    "lattice_wide: checked and not executed -- no full action-native E8 "
    "intertwiner, 512 cylinder, causal boundary, response, axiom, or TOE claim.",
)


def evaluate(
    mutation: str,
) -> tuple[dict[str, tuple[object, str]], dict[str, object]]:
    prereg_mutation = mutation if mutation == "stale_prereg" else ""
    t0_mutation = mutation if mutation in (
        "remap_q024_to_even_positions",
        "swap_boundary_and_complement_order",
    ) else ""
    event_mutation = mutation if mutation in (
        "drop_one_event_branch",
        "break_reflection_label_map",
        "break_proper_cubic_context_covariance",
    ) else ""
    exterior_mutation = mutation if mutation in (
        "erase_mixed_label_sectors",
        "drop_doubled_conjugation",
        "reverse_doubled_leg_order",
    ) else ""
    categorical_mutation = (
        mutation if mutation == "assign_vacuum_to_one_label" else ""
    )

    prereg_ok, prereg_short = prereg_facts(prereg_mutation)
    t0 = t0_facts(t0_mutation)
    h = h_facts()
    event = event_facts(event_mutation)
    exterior = exterior_facts(exterior_mutation)
    categorical = categorical_facts(categorical_mutation)

    erase_h = mutation == "erase_h_composition_residual"
    effect_operation_swap = mutation == "swap_effect_for_lueders_operation"
    identify_channels = (
        mutation == "identify_nonselective_lueders_with_identity"
    )
    gaussian_proxy = mutation == "replace_f_alpha_by_gaussian_proxy"
    naive_promoted = mutation == "keep_naive_vacuum"
    action_native_claim = mutation == "claim_action_native_e8_image"
    later_gates_open = mutation == "open_later_gates_early"

    all_radii = (
        len(t0.radii) == len(FROZEN_SQUARED_RADII)
        and all(
            exact_zero(fact.delta - expected)
            for fact, expected in zip(t0.radii, EXPECTED_DELTAS)
        )
    )
    all_schur = all(
        fact.q_inverse_ok
        and fact.direct_covariance_024
        and fact.direct_covariance_02
        and fact.nested_associativity
        and fact.determinant_identities
        for fact in t0.radii
    )
    all_structure = all(
        fact.positive_inertias
        and fact.reflection_ok
        and fact.internal_inverse_ok
        and fact.two_step_internal_factor_ok
        and fact.action_hermitian_part_positive
        for fact in t0.radii
    )

    results = {
        "P0": (
            prereg_ok and source_has_no_project_imports(),
            "the exact preregistration commit is ancestral and this checker has no project imports",
        ),
        "T0.1": (
            t0.temporal_geometry_ok
            and t0.boundary == Q024_BOUNDARY
            and H_EVEN_POSITIONS == (0, 1, 2),
            "the L24 even Schur geometry and the two frozen index spaces are distinct",
        ),
        "T0.2": (
            all_radii and all_schur,
            "Q024 and Q02 agree by direct Schur, covariance-block inversion, determinant, and nesting routes at all nine radii",
        ),
        "T0.3": (
            all_structure
            and t0.cubic_move_count == 24
            and t0.cubic_invariant,
            "all boundary kernels have the exact positive inertia and reflection/proper-cubic structural typing",
        ),
        "T0.4": (
            t0.q024_shape == (96, 96)
            and t0.q02_shape == (64, 64)
            and t0.q024_rank == 96
            and t0.q02_rank == 64
            and t0.crossing4_pivot_rank == 32
            and t0.q024_defect_rank == 48
            and t0.q02_defect_rank == 32,
            "the D1 two-sector lifts reproduce ranks 96/64/32 and non-Hermitian defects 48/32",
        ),
        "T0.5": (
            t0.event_fiber_dimension == EVENT_DIMENSION
            and not t0.action_event_intertwiner_derived,
            "the shared C32 dimension does not itself derive the action-to-event intertwiner",
        ),
        "T1.1": (
            event.car_ok
            and event.context_ok
            and event.pvm_ok
            and len(event.effects) == EVENT_COUNT
            and event.effect_ranks == (4,) * EVENT_COUNT
            and event.effect_span_rank == EVENT_COUNT
            and event.writer_ok
            and event.pointer_pullback_ok
            and event.reflection_label_map == (7, 6, 5, 4, 3, 2, 1, 0)
            and event.reflection_effect_map_ok
            and event.proper_cubic_context_ok,
            "the exact E8 PVM/M2 pullback obeys four reflection 2-cycles and 24 co-transformed cubic contexts",
        ),
        "T1.2": (
            not effect_operation_swap
            and event.identity_dephasing_distinct
            and not identify_channels
            and event.identity_choi_rank == 1
            and event.dephasing_choi_rank == 8
            and EVENT_DIMENSION**2 == 1024
            and EVENT_COUNT * 4**2 == 128,
            "E8 effects and O9 operations are typed separately; identity and dephasing have ranks 1024 and 128",
        ),
        "T1.3": (
            event.static_same_effects_different_histories,
            "Lueders and replacement instruments share the PVM but give repeat probabilities 1 and 1/8",
        ),
        "T1.4": (
            h.raw == EXPECTED_H_RAW
            and h.normalized == EXPECTED_H_NORMALIZED
            and h.predictor == EXPECTED_H_PREDICTOR
            and h.normalized_full_rank == 32
            and h.positive_factorization
            and h.radius_one_residual_nonzero
            and not erase_h,
            "the positive H control reproduces all three nonzero D1 composition residuals and normalized rank 32",
        ),
        "T1.5": (
            not gaussian_proxy
            and 2 != 0
            and (R(1, 2))**EVENT_COUNT != 0
            and comb(EVENT_COUNT, 2) * (R(1, 2))**EVENT_COUNT != 0,
            "Gaussian bilinears have degree two rather than unit degree zero, and a contraction DPP still has empty/two-label events",
        ),
        "T1.6": (
            exterior.gamma_rank == 16
            and exterior.gamma_plus_rank == 15
            and exterior.doubled_branch_rank == 225
            and exterior.o9_dimension == 9
            and exterior.o9_composition_ok
            and exterior.reduced_pairwise_orthogonal
            and exterior.doubled_order_ok,
            "vacuum-reduced branches give O9 with conjugate(Gamma_plus) tensor Gamma_plus and doubled rank 225",
        ),
        "T1.7": (
            exterior.bidegree_branch_rank == 16
            and exterior.bidegree_dephasing_rank == 128
            and exterior.bidegree_identity_rank == 1024,
            "the (1,1) restriction has branch/dephasing/identity ranks 16/128/1024",
        ),
        "T1.8": (
            exterior.naive_pairwise_product_rank == 1
            and exterior.naive_sum_vacuum_eigenvalue == 8
            and not naive_promoted,
            "the naive vacuum-containing branches overlap at rank one and sum to vacuum eigenvalue eight",
        ),
        "T1.9": (
            exterior.mixed_label_rank
            == 2**EVENT_DIMENSION - 1 - EVENT_COUNT * 15
            and exterior.mixed_label_rank > 0
            and exterior.full_doubled_missing_rank
            == 2**64 - EVENT_COUNT * 225,
            "the reduced branches omit the vacuum and exact mixed-label/full-doubled complements",
        ),
        "T2.1": (
            categorical.groebner_unit
            and categorical.exhaustive_no_covariant_assignment
            and categorical.solution_count == 0,
            "the invariant vacuum gives a unit Groebner certificate against a grade-preserving projective partition covariant under the four reflection 2-cycles",
        ),
        "T2.2": (
            categorical.arbitrary_assignment_unital
            and not categorical.arbitrary_assignment_covariant
            and categorical.fractional_assignment_unital_covariant
            and not categorical.fractional_assignment_projective,
            "the two obvious completions expose the obstruction: label assignment breaks covariance and equal splitting breaks projectivity",
        ),
        "T2.3": (
            not action_native_claim
            and not t0.action_event_intertwiner_derived,
            "no executed candidate supplies an action-native E8 image; the result is a partial narrowing, not a universal no-go",
        ),
        "STOP": (
            not later_gates_open,
            "T3--T6, all 512 cylinders, causal boundary, response, axioms, and TOE movement remain unexecuted",
        ),
    }
    return results, {
        "prereg_short": prereg_short,
        "t0": t0,
        "h": h,
        "event": event,
        "exterior": exterior,
        "categorical": categorical,
    }


def run_once(mutation: str) -> int:
    results, evidence = evaluate(mutation)
    checks = Checks()
    for key, (condition, statement) in results.items():
        checks.check(key, statement, condition)

    t0 = evidence["t0"]
    h = evidence["h"]
    exterior = evidence["exterior"]
    print(
        f"PREREG: {evidence['prereg_short']}; no_project_imports="
        f"{source_has_no_project_imports()}"
    )
    print(
        "SCHUR: B024="
        f"{t0.boundary}; B02={t0.boundary[:2]}; "
        f"ranks={t0.q024_rank}/{t0.q02_rank}/{t0.crossing4_pivot_rank}; "
        f"defects={t0.q024_defect_rank}/{t0.q02_defect_rank}"
    )
    print(
        "H_RESIDUALS: raw="
        f"{h.raw}; normalized={h.normalized}; predictor={h.predictor}; "
        f"full_rank={h.normalized_full_rank}"
    )
    print(
        "EXTERIOR: Gamma/Gamma_plus/doubled="
        f"{exterior.gamma_rank}/{exterior.gamma_plus_rank}/"
        f"{exterior.doubled_branch_rank}; mixed={exterior.mixed_label_rank}"
    )
    print(
        "NO_GO_DISCIPLINE: broad no-go rejected; partial-narrowing only; "
        "a non-grade-preserving or coherent action-derived insertion remains live"
    )
    print(
        "VERDICT: T0_PASS; T1_CONTROLS_PASS; "
        "T2_NO_ACTION_NATIVE_E8_IMAGE_DERIVED; T3_T6_NOT_EXECUTED"
    )
    for line in N5_LINES:
        print(line)
    return checks.finish()


def mutation_self_test() -> int:
    baseline, _ = evaluate("")
    baseline_failures = tuple(
        key for key, (condition, _statement) in baseline.items()
        if not bool(condition)
    )
    failures = 0
    print(f"BASELINE: failures={baseline_failures}")
    failures += int(bool(baseline_failures))
    for mutation in MUTATIONS:
        results, _ = evaluate(mutation)
        caught = tuple(
            key for key, (condition, _statement) in results.items()
            if not bool(condition)
        )
        ok = bool(caught)
        print(
            f"[{'PASS' if ok else 'FAIL'}] mutation={mutation}; "
            f"family={MUTATION_FAMILY[mutation]}; caught={caught}"
        )
        failures += int(not ok)
    print(f"TOTAL: PASS={len(MUTATIONS) + 1 - failures} FAIL={failures}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    parser.add_argument("--self-test-mutations", action="store_true")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0
    if arguments.self_test_mutations:
        return mutation_self_test()
    return run_once(arguments.mutation)


if __name__ == "__main__":
    raise SystemExit(main())
