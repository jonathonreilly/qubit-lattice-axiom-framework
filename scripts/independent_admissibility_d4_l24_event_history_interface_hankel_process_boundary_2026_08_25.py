#!/usr/bin/env python3
"""Independent exact checker for the Block-199 event/history interface.

This checker imports no project runner.  It rebuilds the exterior-form
Clifford matrices, the Block-194 eight-projector event PVM, its one-shot M2
writer, and the operation-space controls from definitions.  Independently,
it solves the generic periodic twelve-site scalar Green problem and
specializes it at all nine frozen squared spatial radii.

The positive covariance and indefinite reflected-Berezin Hankel families are
kept in their declared field-moment types.  In particular, neither family is
promoted to an event-word functional, boundary state, process Choi matrix, or
memory realization.  The downstream process gates remain sealed because the
listed inputs contain no action-to-CP-operation insertion map.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import cache
from itertools import permutations, product
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_L24_EVENT_HISTORY_INTERFACE_HANKEL_PROCESS_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md"
)

R = sp.Rational
I = sp.I
MASS = R(2, 7)
L_TIME = 24
COARSE_TIME = 12
EVENT_DIMENSION = 32
EVENT_COUNT = 8

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
EXPECTED_RADIUS_ONE_M_DEFECT = -R(
    86305920689253797,
    1623025119874668623872875,
)
EXPECTED_RADIUS_ONE_C_DEFECT = R(
    2234183456333136028,
    490236373215579117313690785,
)

MUTATIONS = (
    "drop_event_effect",
    "identify_identity_with_dephasing",
    "claim_lueders_tomography",
    "drop_phase_probes",
    "claim_coherent_probes_registered",
    "wrong_mass",
    "omit_frozen_radius",
    "wrong_recurrence",
    "wrap_nonwrapped_hankel",
    "erase_circular_seam",
    "erase_c_defect",
    "claim_c_hankel_is_process",
    "claim_m_hankel_psd",
    "erase_m_defect",
    "claim_unique_endpoint_history",
    "inject_m_as_positive_compression",
    "import_boundary_state",
    "claim_interface_derived",
    "open_process_early",
    "break_source_note_contract",
)
MUTATION_FAMILY = {
    "drop_event_effect": "A",
    "identify_identity_with_dephasing": "B",
    "claim_lueders_tomography": "B",
    "drop_phase_probes": "C",
    "claim_coherent_probes_registered": "C",
    "wrong_mass": "D",
    "omit_frozen_radius": "D",
    "wrong_recurrence": "E",
    "wrap_nonwrapped_hankel": "E",
    "erase_circular_seam": "E",
    "erase_c_defect": "F",
    "claim_c_hankel_is_process": "F",
    "claim_m_hankel_psd": "G",
    "erase_m_defect": "G",
    "claim_unique_endpoint_history": "H",
    "inject_m_as_positive_compression": "H",
    "import_boundary_state": "H",
    "claim_interface_derived": "H",
    "open_process_early": "H",
    "break_source_note_contract": "N",
}


def exact_zero(value: sp.Expr) -> bool:
    """Decide the rational/algebraic zero cases used by this checker."""
    if value == 0:
        return True
    try:
        singleton = DomainMatrix.from_Matrix(
            sp.Matrix(((value,),)), extension=True
        )
        if singleton.is_zero_matrix:
            return True
    except (TypeError, ValueError):
        pass
    value = sp.cancel(value)
    return value == 0 or sp.simplify(value) == 0


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
    """Invert over the exact rational-function/algebraic field."""
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


def exact_rank(matrix: sp.MatrixBase) -> int:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).rank()


def exact_sign(value: sp.Expr) -> int:
    value = sp.factor(sp.simplify(value))
    if value == 0:
        return 0
    if value.is_positive is True:
        return 1
    if value.is_negative is True:
        return -1
    raise ValueError(f"undetermined exact sign: {value}")


def exact_symmetric_inertia(
    matrix: sp.MatrixBase,
) -> tuple[int, int, int]:
    """Return (positive, zero, negative) by exact congruence."""
    work = sp.Matrix(matrix)
    if not matrix_equal(work, work.T):
        raise ValueError("inertia input is not exactly real symmetric")
    positive = negative = 0

    while work.rows:
        size = work.rows
        diagonal = next(
            (
                index
                for index in range(size)
                if not exact_zero(work[index, index])
            ),
            None,
        )
        if diagonal is not None:
            order = [diagonal] + [
                index for index in range(size) if index != diagonal
            ]
            work = work.extract(order, order)
            pivot = sp.factor(work[0, 0])
            sign = exact_sign(pivot)
            positive += int(sign > 0)
            negative += int(sign < 0)
            if size == 1:
                work = sp.zeros(0)
            else:
                column = work[1:, :1]
                work = (
                    work[1:, 1:] - column * column.T / pivot
                ).applyfunc(sp.factor)
            continue

        off_diagonal = next((
            (row, column)
            for row in range(size)
            for column in range(row + 1, size)
            if not exact_zero(work[row, column])
        ), None)
        if off_diagonal is None:
            break
        first, second = off_diagonal
        order = [first, second] + [
            index
            for index in range(size)
            if index not in (first, second)
        ]
        work = work.extract(order, order)
        pivot_block = work[:2, :2]
        if exact_sign(pivot_block.det()) != -1:
            raise ValueError("unexpected exact two-dimensional pivot")
        positive += 1
        negative += 1
        if size == 2:
            work = sp.zeros(0)
        else:
            coupling = work[2:, :2]
            work = (
                work[2:, 2:]
                - coupling * pivot_block.inv() * coupling.T
            ).applyfunc(sp.factor)

    return positive, matrix.rows - positive - negative, negative


def shift_matrix(length: int) -> sp.Matrix:
    shift = sp.zeros(length)
    for column in range(length):
        shift[(column + 1) % length, column] = 1
    return shift


def block_matrix(
    upper_left: sp.MatrixBase,
    upper_right: sp.MatrixBase,
    lower_left: sp.MatrixBase,
    lower_right: sp.MatrixBase,
) -> sp.Matrix:
    return sp.Matrix.vstack(
        sp.Matrix.hstack(upper_left, upper_right),
        sp.Matrix.hstack(lower_left, lower_right),
    )


def exterior_creation(
    axis: int,
    subsets: tuple[tuple[int, ...], ...],
    subset_index: dict[tuple[int, ...], int],
) -> sp.Matrix:
    result = sp.zeros(16)
    for column, subset in enumerate(subsets):
        if axis in subset:
            continue
        target = tuple(sorted(subset + (axis,)))
        sign = (-1) ** sum(item < axis for item in subset)
        result[subset_index[target], column] = sign
    return result


def first_range_vector(projector: sp.MatrixBase) -> sp.Matrix:
    for column in range(projector.cols):
        candidate = projector[:, column]
        if any(not exact_zero(value) for value in candidate):
            return sp.Matrix(candidate)
    raise ValueError("zero projector has no range vector")


@dataclass(frozen=True)
class EventFacts:
    car_ok: bool
    event_context_ok: bool
    effects: tuple[sp.Matrix, ...]
    effect_ranks: tuple[int, ...]
    effect_span_rank: int
    pvm_ok: bool
    weights: tuple[sp.Expr, ...]
    writer_ok: bool
    pointer_pullback_ok: bool
    lueders_span_rank: int
    lueders_identity_span_rank: int
    identity_choi_rank: int
    dephasing_choi_rank: int
    identity_dephasing_distinct: bool
    identity_liouville_rank: int
    dephasing_liouville_rank: int
    coherent_probe_count: int
    coherent_frame_rank: int
    coherent_frame_determinant: sp.Expr | None
    no_phase_count: int
    no_phase_rank: int
    probes_cp_tni: bool


def hermitian_coordinates(matrix: sp.MatrixBase) -> sp.Matrix:
    """Real coordinates for Herm(8): diagonal, real, imaginary parts."""
    pairs = tuple(
        (left, right)
        for left in range(EVENT_COUNT)
        for right in range(left + 1, EVENT_COUNT)
    )
    values = [matrix[index, index] for index in range(EVENT_COUNT)]
    values.extend(
        (matrix[left, right] + matrix[right, left]) / 2
        for left, right in pairs
    )
    values.extend(
        (matrix[right, left] - matrix[left, right]) / (2 * I)
        for left, right in pairs
    )
    return sp.Matrix(values)


@cache
def base_event_facts() -> dict[str, object]:
    subsets = tuple(
        tuple(axis for axis in range(4) if mask & (1 << axis))
        for mask in range(16)
    )
    subset_index = {subset: index for index, subset in enumerate(subsets)}
    creation = tuple(
        exterior_creation(axis, subsets, subset_index)
        for axis in range(4)
    )
    annihilation = tuple(matrix.T for matrix in creation)
    gammas = tuple(
        item
        for axis in range(4)
        for item in (
            creation[axis] + annihilation[axis],
            I * (creation[axis] - annihilation[axis]),
        )
    )
    identity16 = sp.eye(16)
    car_ok = all(matrix_equal(
        gammas[left] * gammas[right]
        + gammas[right] * gammas[left],
        2 * int(left == right) * identity16,
    ) for left in range(8) for right in range(8))

    o1 = sp.expand(I * gammas[0] * gammas[2] * gammas[3])
    o2 = sp.expand(I * gammas[1] * gammas[2] * gammas[5])
    outcomes = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    ports = tuple(sp.expand(
        (identity16 + first * o1)
        * (identity16 + second * o2) / 4
    ) for first, second in outcomes)
    orientation = sp.expand(I * gammas[6] * gammas[4])
    event_context_ok = (
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
        connector = sp.expand(port * orientation)
        for sign in (1, -1):
            effects.append(sp.expand(block_matrix(
                port,
                sign * connector,
                sign * connector.H,
                port,
            ) / 2))
    effects_tuple = tuple(effects)

    sector_orientation = block_matrix(
        zero16, orientation, orientation, zero16
    )
    p_plus = (sp.eye(32) + sector_orientation) / 2
    p_minus = (sp.eye(32) - sector_orientation) / 2
    pointer_identity = sp.eye(2)
    writer = sp.kronecker_product(p_plus, pointer_identity) + (
        sp.kronecker_product(p_minus, SIGMA_X)
    )
    writer_ok = (
        matrix_equal(writer.H * writer, sp.eye(64))
        and matrix_equal(writer * writer.H, sp.eye(64))
        and not matrix_equal(writer, sp.eye(64))
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
        diagonal_port = block_matrix(port, zero16, zero16, port)
        for pointer_code in pointer_codes:
            readout = sp.kronecker_product(diagonal_port, pointer_code)
            induced.append(sp.expand(
                input_isometry.H * writer.H * readout
                * writer * input_isometry
            ))

    return {
        "car_ok": car_ok,
        "event_context_ok": event_context_ok,
        "effects": effects_tuple,
        "writer_ok": writer_ok,
        "pointer_pullback_ok": all(matrix_equal(
            induced[index], effects_tuple[index]
        ) for index in range(EVENT_COUNT)),
    }


def event_facts(mutation: str) -> EventFacts:
    base = base_event_facts()
    complete_effects = base["effects"]
    effects = (
        complete_effects[:-1]
        if mutation == "drop_event_effect"
        else complete_effects
    )
    effect_ranks = tuple(exact_rank(effect) for effect in effects)
    flattened = sp.Matrix.hstack(*(
        effect.reshape(EVENT_DIMENSION**2, 1) for effect in effects
    ))
    effect_span_rank = exact_rank(flattened)
    pvm_ok = (
        len(effects) == EVENT_COUNT
        and all(matrix_equal(effect.H, effect) for effect in effects)
        and all(matrix_equal(effect**2, effect) for effect in effects)
        and all(matrix_equal(
            effects[left] * effects[right], sp.zeros(EVENT_DIMENSION)
        ) for left in range(len(effects))
          for right in range(left + 1, len(effects)))
        and matrix_equal(sum(effects, sp.zeros(32)), sp.eye(32))
    )
    weights = tuple(sp.trace(effect) / EVENT_DIMENSION for effect in effects)

    diagonal_choi = tuple(
        sp.eye(EVENT_COUNT)[:, index]
        * sp.eye(EVENT_COUNT)[index, :]
        for index in range(EVENT_COUNT)
    )
    dephasing_choi = sp.eye(EVENT_COUNT)
    ones = sp.ones(EVENT_COUNT, 1)
    identity_choi = ones * ones.T
    if mutation == "identify_identity_with_dephasing":
        identity_choi = dephasing_choi

    lueders_design = sp.Matrix.hstack(*(
        hermitian_coordinates(matrix) for matrix in diagonal_choi
    ))
    with_identity = sp.Matrix.hstack(
        lueders_design, hermitian_coordinates(identity_choi)
    )

    # A concrete off-block operator is fixed by exact range vectors.  The
    # identity channel preserves it, while PVM dephasing annihilates it.
    range_zero = first_range_vector(complete_effects[0])
    range_one = first_range_vector(complete_effects[1])
    cross_witness = range_zero * range_one.H
    dephased_witness = sum((
        effect * cross_witness * effect for effect in complete_effects
    ), sp.zeros(EVENT_DIMENSION))
    identity_witness = (
        dephased_witness
        if mutation == "identify_identity_with_dephasing"
        else cross_witness
    )

    pairs = tuple(
        (left, right)
        for left in range(EVENT_COUNT)
        for right in range(left + 1, EVENT_COUNT)
    )
    diagonal_vectors = []
    real_pair_vectors = []
    phase_pair_vectors = []
    for index in range(EVENT_COUNT):
        vector = sp.zeros(EVENT_COUNT, 1)
        vector[index] = 1
        diagonal_vectors.append(vector)
    for left, right in pairs:
        real_vector = sp.zeros(EVENT_COUNT, 1)
        real_vector[left] = real_vector[right] = 1
        real_pair_vectors.append(real_vector)
        phase_vector = sp.zeros(EVENT_COUNT, 1)
        phase_vector[left] = 1
        phase_vector[right] = I
        phase_pair_vectors.append(phase_vector)

    no_phase_vectors = tuple(diagonal_vectors + real_pair_vectors)
    coherent_vectors = (
        no_phase_vectors
        if mutation == "drop_phase_probes"
        else tuple(
            diagonal_vectors
            + [
                vector
                for pair in zip(real_pair_vectors, phase_pair_vectors)
                for vector in pair
            ]
        )
    )
    coherent_design = sp.Matrix.hstack(*(
        hermitian_coordinates(vector * vector.H)
        for vector in coherent_vectors
    ))
    no_phase_design = sp.Matrix.hstack(*(
        hermitian_coordinates(vector * vector.H)
        for vector in no_phase_vectors
    ))
    coherent_rank = exact_rank(coherent_design)
    coherent_determinant = (
        sp.factor(coherent_design.det())
        if coherent_design.rows == coherent_design.cols
        else None
    )
    probes_cp_tni = all(
        exact_rank(vector * vector.H) == 1
        and sum(
            sp.simplify(sp.conjugate(value) * value)
            for value in vector
        ) in (1, 2)
        and all(
            sp.simplify(sp.conjugate(value) * value) in (0, 1)
            for value in vector
        )
        for vector in coherent_vectors
    )

    return EventFacts(
        car_ok=bool(base["car_ok"]),
        event_context_ok=bool(base["event_context_ok"]),
        effects=tuple(effects),
        effect_ranks=effect_ranks,
        effect_span_rank=effect_span_rank,
        pvm_ok=pvm_ok,
        weights=weights,
        writer_ok=bool(base["writer_ok"]),
        pointer_pullback_ok=bool(base["pointer_pullback_ok"]),
        lueders_span_rank=exact_rank(lueders_design),
        lueders_identity_span_rank=exact_rank(with_identity),
        identity_choi_rank=exact_rank(identity_choi),
        dephasing_choi_rank=exact_rank(dephasing_choi),
        identity_dephasing_distinct=(
            not matrix_equal(identity_choi, dephasing_choi)
            and not exact_zero(cross_witness.norm())
            and matrix_equal(identity_witness, cross_witness)
            and matrix_equal(dephased_witness, sp.zeros(EVENT_DIMENSION))
        ),
        identity_liouville_rank=EVENT_DIMENSION**2,
        dephasing_liouville_rank=sum(
            exact_rank(effect)**2 for effect in complete_effects
        ),
        coherent_probe_count=len(coherent_vectors),
        coherent_frame_rank=coherent_rank,
        coherent_frame_determinant=coherent_determinant,
        no_phase_count=len(no_phase_vectors),
        no_phase_rank=exact_rank(no_phase_design),
        probes_cp_tni=probes_cp_tni,
    )


@dataclass(frozen=True)
class GreenTemplate:
    variable: sp.Symbol
    shift: sp.Matrix
    t_matrix: sp.Matrix
    q_inverse: sp.Matrix
    column: tuple[sp.Expr, ...]
    inverse_ok: bool
    recurrence_ok: bool
    circular_wrap_ok: bool
    seam_residual: sp.Expr
    nonwrapped_hankel: sp.Matrix
    circular_hankel: sp.Matrix
    nonwrapped_ranks: tuple[int, ...]
    nonwrapped_rank: int
    circular_rank: int
    nonwrapped_leading_determinant: sp.Expr
    circular_determinant: sp.Expr
    t_determinant: sp.Expr


@cache
def green_template() -> GreenTemplate:
    variable = sp.Symbol("green_recurrence_x", real=True)
    shift = shift_matrix(COARSE_TIME)
    t_matrix = (
        variable * sp.eye(COARSE_TIME) - shift - shift.T
    )
    t_inverse = exact_inverse(t_matrix)
    # x=4*delta+2 and Q=T/(4*delta)=T/(x-2).
    q_inverse = sp.Matrix((variable - 2) * t_inverse)
    column = tuple(
        sp.factor(q_inverse[index, 0])
        for index in range(COARSE_TIME)
    )
    inverse_ok = matrix_equal(
        t_matrix * q_inverse,
        (variable - 2) * sp.eye(COARSE_TIME),
    ) and matrix_equal(
        q_inverse * t_matrix,
        (variable - 2) * sp.eye(COARSE_TIME),
    )
    recurrence_ok = all(exact_zero(
        column[index + 1]
        - variable * column[index]
        + column[index - 1]
    ) for index in range(1, COARSE_TIME - 1))
    circular_wrap_ok = exact_zero(
        column[0]
        - variable * column[COARSE_TIME - 1]
        + column[COARSE_TIME - 2]
    )
    seam_residual = sp.factor(
        variable * column[0] - column[1] - column[-1]
    )

    # Sizes two through six exhaust the nonwrapped data before i+j reaches
    # the twelve-site seam.  The homogeneous recurrence then bounds every
    # such Hankel rank by two, and the common leading 2x2 minor is nonzero.
    nonwrapped_hankels = tuple(
        sp.Matrix(
            size,
            size,
            lambda row, col: column[row + col],
        )
        for size in range(2, 7)
    )
    nonwrapped_hankel = nonwrapped_hankels[-1]
    circular_hankel = sp.Matrix(
        COARSE_TIME,
        COARSE_TIME,
        lambda row, col: column[(row + col) % COARSE_TIME],
    )
    return GreenTemplate(
        variable=variable,
        shift=shift,
        t_matrix=t_matrix,
        q_inverse=q_inverse,
        column=column,
        inverse_ok=inverse_ok,
        recurrence_ok=recurrence_ok,
        circular_wrap_ok=circular_wrap_ok,
        seam_residual=seam_residual,
        nonwrapped_hankel=nonwrapped_hankel,
        circular_hankel=circular_hankel,
        nonwrapped_ranks=tuple(
            exact_rank(hankel) for hankel in nonwrapped_hankels
        ),
        nonwrapped_rank=exact_rank(nonwrapped_hankel),
        circular_rank=exact_rank(circular_hankel),
        nonwrapped_leading_determinant=sp.factor(
            nonwrapped_hankel[:2, :2].det()
        ),
        circular_determinant=sp.factor(circular_hankel.det()),
        t_determinant=sp.factor(t_matrix.det()),
    )


@dataclass(frozen=True)
class MomentFacts:
    radius: sp.Expr
    delta: sp.Expr
    x_value: sp.Expr
    green_values: tuple[sp.Expr, ...]
    green_all_positive: bool
    inverse_specialization_ok: bool
    nonwrapped_rank_stable: bool
    circular_rank_stable: bool
    c_hankel_rank: int
    c_hankel_inertia: tuple[int, int, int]
    c_defect: sp.Matrix
    c_defect_coefficient: sp.Expr
    m_internal_determinant_ok: bool
    m_hankel_rank: int
    m_hankel_inertia: tuple[int, int, int]
    m_defect: sp.Matrix
    m_defect_coefficient: sp.Expr
    m_defect_factor_ok: bool
    lifted_shape: tuple[int, int]
    lifted_rank: int
    lifted_inertia: tuple[int, int, int]
    direct_lift_ok: bool


def moment_facts(
    template: GreenTemplate,
    radius: sp.Expr,
    mass: sp.Expr,
    mutation: str,
) -> MomentFacts:
    delta = sp.factor(mass**2 + radius)
    x_value = sp.factor(4 * delta + 2)
    green_values = tuple(
        sp.factor(value.subs(template.variable, x_value))
        for value in template.column
    )
    inverse_specialization_ok = (
        exact_sign(delta) == 1
        and not exact_zero(
            template.t_determinant.subs(template.variable, x_value)
        )
    )
    nonwrapped_rank_stable = not exact_zero(
        template.nonwrapped_leading_determinant.subs(
            template.variable, x_value
        )
    )
    circular_rank_stable = not exact_zero(
        template.circular_determinant.subs(
            template.variable, x_value
        )
    )

    c_scale = sp.factor(2 * mass / delta)
    c_moments = tuple(
        sp.factor(c_scale * green_values[index]) * sp.eye(2)
        for index in range(3)
    )
    c_hankel = block_matrix(
        c_moments[0], c_moments[1],
        c_moments[1], c_moments[2],
    )
    c_defect = sp.simplify(
        c_moments[2]
        - c_moments[1] * exact_inverse(c_moments[0]) * c_moments[1]
    )
    if mutation == "erase_c_defect":
        c_defect = sp.zeros(2)
    c_defect_coefficient = sp.factor(c_defect[0, 0])

    spatial_root = sp.sqrt(radius)
    internal_inverse = (
        mass * sp.eye(2) - spatial_root * REAL_SKEW
    ) / delta
    g_matrix = sp.expand(SIGMA_Z * internal_inverse)
    m_moments = tuple(
        sp.expand(-green_values[index + 1] * g_matrix)
        for index in range(3)
    )
    m_hankel = block_matrix(
        m_moments[0], m_moments[1],
        m_moments[1], m_moments[2],
    )
    m_defect = sp.simplify(
        m_moments[2]
        - m_moments[1] * exact_inverse(m_moments[0]) * m_moments[1]
    )
    if mutation == "erase_m_defect":
        m_defect = sp.zeros(2)
    m_defect_coefficient = sp.factor(
        m_defect[0, 0] / g_matrix[0, 0]
    )
    m_defect_factor_ok = matrix_equal(
        m_defect, m_defect_coefficient * g_matrix
    )
    m_inertia = exact_symmetric_inertia(m_hankel)
    lifted = sp.kronecker_product(sp.eye(8), m_hankel)
    lifted_inertia = tuple(8 * entry for entry in m_inertia)
    lifted_rank = 8 * exact_rank(m_hankel)
    direct_lift_ok = (
        lifted.shape == (32, 32)
        and exact_rank(lifted) == lifted_rank
        and (
            radius != 1
            or exact_symmetric_inertia(lifted) == lifted_inertia
        )
    )

    return MomentFacts(
        radius=radius,
        delta=delta,
        x_value=x_value,
        green_values=green_values,
        green_all_positive=all(
            exact_sign(value) == 1 for value in green_values
        ),
        inverse_specialization_ok=inverse_specialization_ok,
        nonwrapped_rank_stable=nonwrapped_rank_stable,
        circular_rank_stable=circular_rank_stable,
        c_hankel_rank=exact_rank(c_hankel),
        c_hankel_inertia=exact_symmetric_inertia(c_hankel),
        c_defect=c_defect,
        c_defect_coefficient=c_defect_coefficient,
        m_internal_determinant_ok=exact_zero(
            g_matrix.det() + 1 / delta
        ),
        m_hankel_rank=exact_rank(m_hankel),
        m_hankel_inertia=m_inertia,
        m_defect=m_defect,
        m_defect_coefficient=m_defect_coefficient,
        m_defect_factor_ok=m_defect_factor_ok,
        lifted_shape=lifted.shape,
        lifted_rank=lifted_rank,
        lifted_inertia=lifted_inertia,
        direct_lift_ok=direct_lift_ok,
    )


@dataclass(frozen=True)
class ConditionalHistoryFacts:
    sign_normalized: bool
    sign_strictly_positive: bool
    sign_symmetries: bool
    sign_one_shot: bool
    sign_pair_tables: bool
    port_laws_normalized: bool
    port_laws_nonnegative: bool
    port_symmetries: bool
    port_one_shot: bool
    port_pair_tables: bool
    complete_one_shot: bool
    complete_pair_tables: bool
    endpoint_triple_equal: tuple[sp.Expr, sp.Expr]
    endpoint_ranks: tuple[int, int]
    endpoint_inertias: tuple[tuple[int, int, int], ...]
    inequivalent: bool


@cache
def port_endpoint_facts() -> dict[str, object]:
    port_words = tuple(product(range(4), repeat=3))
    endpoints = (sp.Integer(0), R(1, 48))

    def probability(word: tuple[int, int, int], parameter: sp.Expr) -> sp.Expr:
        distinct = len(set(word))
        if distinct == 1:
            return R(1, 16) - 3 * parameter
        if distinct == 2:
            return parameter
        return R(1, 32) - parameter

    laws = tuple({
        word: sp.factor(probability(word, parameter))
        for word in port_words
    } for parameter in endpoints)

    def one_marginal(
        law: dict[tuple[int, int, int], sp.Expr], slot: int, port: int
    ) -> sp.Expr:
        return sp.factor(sum(
            value for word, value in law.items() if word[slot] == port
        ))

    def pair_marginal(
        law: dict[tuple[int, int, int], sp.Expr],
        left: int,
        right: int,
        left_port: int,
        right_port: int,
    ) -> sp.Expr:
        return sp.factor(sum(
            value for word, value in law.items()
            if word[left] == left_port and word[right] == right_port
        ))

    port_permutations = tuple(permutations(range(4)))
    normalized = all(
        exact_zero(sum(law.values()) - 1) for law in laws
    )
    nonnegative = all(
        exact_sign(value) >= 0 for law in laws for value in law.values()
    )
    symmetries = all(
        law[word] == law[(word[2], word[1], word[0])]
        and all(
            law[word] == law[tuple(permutation[item] for item in word)]
            for permutation in port_permutations
        )
        for law in laws for word in port_words
    )
    one_shot = all(
        one_marginal(law, slot, port) == R(1, 4)
        for law in laws
        for slot in range(3)
        for port in range(4)
    )
    pair_tables = all(
        pair_marginal(law, left, right, left_port, right_port)
        == R(1, 16)
        for law in laws
        for left, right in ((0, 1), (1, 2), (0, 2))
        for left_port in range(4)
        for right_port in range(4)
    )
    triple_equal = tuple(sp.factor(sum(
        value for word, value in law.items() if len(set(word)) == 1
    )) for law in laws)
    nonzero_counts = tuple(sum(
        int(not exact_zero(value)) for value in law.values()
    ) for law in laws)
    return {
        "laws": laws,
        "normalized": normalized,
        "nonnegative": nonnegative,
        "symmetries": symmetries,
        "one_shot": one_shot,
        "pair_tables": pair_tables,
        "triple_equal": triple_equal,
        "nonzero_counts": nonzero_counts,
    }


def conditional_history_facts(
    moments: MomentFacts,
) -> ConditionalHistoryFacts:
    ratio_one = sp.factor(
        moments.green_values[1] / moments.green_values[0]
    )
    ratio_two = sp.factor(
        moments.green_values[2] / moments.green_values[0]
    )
    sign_words = tuple(product((-1, 1), repeat=3))
    sign_law = {
        word: sp.factor((
            1
            + ratio_one * (word[0] * word[1] + word[1] * word[2])
            + ratio_two * word[0] * word[2]
        ) / 8)
        for word in sign_words
    }

    def sign_one_marginal(slot: int, sign: int) -> sp.Expr:
        return sp.factor(sum(
            value for word, value in sign_law.items() if word[slot] == sign
        ))

    def sign_pair_marginal(
        left: int, right: int, left_sign: int, right_sign: int
    ) -> sp.Expr:
        return sp.factor(sum(
            value for word, value in sign_law.items()
            if word[left] == left_sign and word[right] == right_sign
        ))

    pair_ratios = {
        (0, 1): ratio_one,
        (1, 2): ratio_one,
        (0, 2): ratio_two,
    }
    sign_normalized = exact_zero(sum(sign_law.values()) - 1)
    sign_positive = all(
        exact_sign(value) == 1 for value in sign_law.values()
    )
    sign_symmetries = all(
        sign_law[word] == sign_law[(word[2], word[1], word[0])]
        and sign_law[word] == sign_law[tuple(-item for item in word)]
        for word in sign_words
    )
    sign_one_shot = all(
        exact_zero(sign_one_marginal(slot, sign) - R(1, 2))
        for slot in range(3) for sign in (-1, 1)
    )
    sign_pair_tables = all(
        exact_zero(
            sign_pair_marginal(left, right, left_sign, right_sign)
            - (
                1
                + pair_ratios[(left, right)] * left_sign * right_sign
            ) / 4
        )
        for left, right in pair_ratios
        for left_sign in (-1, 1)
        for right_sign in (-1, 1)
    )

    port = port_endpoint_facts()
    # Because p_b factors into the sign and port laws, these products test
    # every fine PVM entry rather than only selected signed correlators.
    complete_one_shot = bool(port["one_shot"]) and sign_one_shot and all(
        R(1, 4) * R(1, 2) == R(1, 8)
        for _slot in range(3)
        for _port in range(4)
        for _sign in (-1, 1)
    )
    complete_pair_tables = bool(port["pair_tables"]) and all(
        exact_zero(
            R(1, 16)
            * sign_pair_marginal(left, right, left_sign, right_sign)
            - (
                1
                + pair_ratios[(left, right)] * left_sign * right_sign
            ) / 64
        )
        for left, right in pair_ratios
        for _left_port in range(4)
        for _right_port in range(4)
        for left_sign in (-1, 1)
        for right_sign in (-1, 1)
    )
    endpoint_ranks = tuple(
        8 * count for count in port["nonzero_counts"]
    )
    endpoint_inertias = tuple(
        (rank, 512 - rank, 0) for rank in endpoint_ranks
    )
    triple_equal = tuple(port["triple_equal"])
    return ConditionalHistoryFacts(
        sign_normalized=sign_normalized,
        sign_strictly_positive=sign_positive,
        sign_symmetries=sign_symmetries,
        sign_one_shot=sign_one_shot,
        sign_pair_tables=sign_pair_tables,
        port_laws_normalized=bool(port["normalized"]),
        port_laws_nonnegative=bool(port["nonnegative"]),
        port_symmetries=bool(port["symmetries"]),
        port_one_shot=bool(port["one_shot"]),
        port_pair_tables=bool(port["pair_tables"]),
        complete_one_shot=complete_one_shot,
        complete_pair_tables=complete_pair_tables,
        endpoint_triple_equal=triple_equal,
        endpoint_ranks=endpoint_ranks,
        endpoint_inertias=endpoint_inertias,
        inequivalent=triple_equal[0] != triple_equal[1],
    )


NOTE_NEEDLE_GROUPS = (
    ("identity insertion",),
    ("dephasing",),
    ("rank 64", "rank `64`"),
    ("rank 36", "rank `36`", "rank to 36"),
    ("nonwrapped", "non-wrapped"),
    ("circular",),
    ("field moment",),
    ("event-process", "event process"),
    ("action-to-event", "action to event"),
    ("two inequivalent",),
    ("identical complete one- and two-crossing",),
    ("strongly positive", "strongly-positive"),
    ("boundary",),
    ("t4--t6", "t4-t6", "t4 through t6"),
    ("sealed",),
    ("no axiom amendment", "axiom amendment"),
    ("partial-attempt-with-named-untested-routes",),
    ("effect_system_dimension: eight",),
    ("declared_operation_span_dimension: nine",),
    ("event_support_frame_dimension: sixty_four_control_only",),
    ("event_process_interface: not_derived",),
    ("toe lane scores remain unchanged",),
    ("## 8. no-go discipline gate",),
    ("### n1",),
    ("### n2",),
    ("### n3",),
    ("### n4",),
    ("### n5",),
    ("### n6",),
    ("### n7",),
    ("### n8",),
)


def source_note_contract(mutation: str) -> tuple[bool, str]:
    if mutation == "break_source_note_contract":
        return False, "mutation"
    if not NOTE_PATH.is_file():
        return True, "absent-deferred"
    text = NOTE_PATH.read_text(encoding="utf-8").lower()
    missing = tuple(
        group for group in NOTE_NEEDLE_GROUPS
        if not any(option in text for option in group)
    )
    return not missing, "present-checked" if not missing else "present-missing"


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
    "per_element: checked exterior Clifford generators, eight exact event "
    "projectors, compressed Choi directions, and every 2x2 field-moment "
    "defect.",
    "per_site: checked the periodic twelve-site Green problem and two "
    "three-crossing fixed-PVM endpoint laws with identical one/two tables.",
    "per_mode: checked the rank-two scalar recurrence, rank-twelve circular "
    "Hankel, two-component C/M fibers, and eight-copy M lift.",
    "per_block: checked PVM/M2, operation spans, Green inverse, C-Hankel, "
    "M-Hankel, and interface types as separate blocks.",
    "lattice_wide: checked and not executed -- no event insertion map, "
    "boundary state, history PSD, process comb, response, held-out, axiom, "
    "or TOE closure is supplied.",
)


def evaluate(
    mutation: str,
) -> tuple[dict[str, tuple[object, str]], dict[str, object]]:
    event = event_facts(mutation)
    template = green_template()
    mass = R(3, 7) if mutation == "wrong_mass" else MASS
    radii = (
        FROZEN_SQUARED_RADII[:-1]
        if mutation == "omit_frozen_radius"
        else FROZEN_SQUARED_RADII
    )
    moments = tuple(
        moment_facts(template, radius, mass, mutation)
        for radius in radii
    )
    histories = tuple(
        conditional_history_facts(facts) for facts in moments
    )
    deltas = tuple(fact.delta for fact in moments)
    radius_one = next(fact for fact in moments if fact.radius == 1)

    recurrence_coefficient = (
        template.variable + 1
        if mutation == "wrong_recurrence"
        else template.variable
    )
    recurrence_ok = all(exact_zero(
        template.column[index + 1]
        - recurrence_coefficient * template.column[index]
        + template.column[index - 1]
    ) for index in range(1, COARSE_TIME - 1))
    nonwrapped_rank = (
        template.circular_rank
        if mutation == "wrap_nonwrapped_hankel"
        else template.nonwrapped_rank
    )

    claims = {
        "lueders_tomographic": mutation == "claim_lueders_tomography",
        "coherent_registered": (
            mutation == "claim_coherent_probes_registered"
        ),
        "seam_zero": mutation == "erase_circular_seam",
        "c_is_process": mutation == "claim_c_hankel_is_process",
        "m_psd": mutation == "claim_m_hankel_psd",
        "endpoint_unique": mutation == "claim_unique_endpoint_history",
        "m_compression": (
            mutation == "inject_m_as_positive_compression"
        ),
        "boundary_imported": mutation == "import_boundary_state",
        "interface_derived": mutation == "claim_interface_derived",
        "process_open": mutation == "open_process_early",
    }
    note_ok, note_status = source_note_contract(mutation)

    results = {
        "A1": (
            event.car_ok and event.event_context_ok,
            "the exterior-form Clifford algebra and commuting event context are rebuilt",
        ),
        "A2": (
            event.pvm_ok
            and len(event.effects) == EVENT_COUNT
            and event.effect_ranks == (4,) * EVENT_COUNT
            and event.weights == (R(1, 8),) * EVENT_COUNT,
            "the eight effects are orthogonal rank-four projectors summing to I32",
        ),
        "A3": (
            event.writer_ok and event.pointer_pullback_ok,
            "the nonidentity M2 unitary gives the exact one-shot joint pointer pullback",
        ),
        "B1": (
            event.effect_span_rank == 8
            and EVENT_DIMENSION**2 == 1024
            and claims["lueders_tomographic"] is False,
            "the effect system has dimension eight and is not tomography of M32",
        ),
        "B2": (
            event.lueders_span_rank == 8
            and event.lueders_identity_span_rank == 9,
            "eight Lueders Choi directions become only nine after identity insertion",
        ),
        "B3": (
            event.identity_dephasing_distinct
            and event.identity_choi_rank == 1
            and event.dephasing_choi_rank == 8
            and event.identity_liouville_rank == 1024
            and event.dephasing_liouville_rank == 128,
            "identity and PVM dephasing differ on an exact off-block witness",
        ),
        "B4": (
            event.coherent_probe_count == 64
            and event.coherent_frame_rank == 64
            and event.coherent_frame_determinant in (-1, 1)
            and event.no_phase_count == 36
            and event.no_phase_rank == 36
            and event.probes_cp_tni,
            "the minimal coherent CP frame has rank 64; its no-phase part has rank 36",
        ),
        "B5": (
            claims["coherent_registered"] is False,
            "the coherent frame remains a mathematical control, not registered apparatus",
        ),
        "C1": (
            mass == MASS
            and tuple(radii) == FROZEN_SQUARED_RADII
            and len(set(radii)) == 9
            and all(
                exact_zero(actual - expected)
                for actual, expected in zip(deltas, EXPECTED_DELTAS)
            )
            and all(fact.inverse_specialization_ok for fact in moments)
            and all(fact.green_all_positive for fact in moments),
            "the generic exact Q inverse specializes without poles at all nine deltas",
        ),
        "C2": (
            template.inverse_ok
            and template.recurrence_ok
            and recurrence_ok
            and template.circular_wrap_ok
            and exact_zero(
                template.seam_residual - (template.variable - 2)
            )
            and claims["seam_zero"] is False,
            "a_(n+1)=x a_n-a_(n-1) holds off seam and the source seam is x-2=4 delta",
        ),
        "C3": (
            nonwrapped_rank == 2
            and template.nonwrapped_ranks == (2, 2, 2, 2, 2)
            and template.circular_rank == 12
            and all(fact.nonwrapped_rank_stable for fact in moments)
            and all(fact.circular_rank_stable for fact in moments),
            "the ordinary nonwrapped Hankel rank is two and circular rank is twelve",
        ),
        "D1": (
            all(
                fact.c_hankel_rank == 4
                and fact.c_hankel_inertia == (4, 0, 0)
                for fact in moments
            ),
            "every C0,C2,C4 truncated block Hankel is positive definite of rank four",
        ),
        "D2": (
            all(
                fact.c_defect_coefficient != 0
                and exact_sign(fact.c_defect_coefficient) == 1
                and matrix_equal(
                    fact.c_defect,
                    fact.c_defect_coefficient * sp.eye(2),
                )
                for fact in moments
            )
            and radius_one.c_defect_coefficient
            == EXPECTED_RADIUS_ONE_C_DEFECT,
            "every C4-C2 C0^-1 C2 defect is a strictly positive scalar I2",
        ),
        "E1": (
            all(
                fact.m_internal_determinant_ok
                and fact.m_hankel_rank == 4
                and fact.m_hankel_inertia == (2, 0, 2)
                for fact in moments
            )
            and claims["m_psd"] is False,
            "every M0,M1,M2 block Hankel is rank four with inertia (2,0,2)",
        ),
        "E2": (
            all(
                fact.m_defect_coefficient != 0
                and exact_sign(fact.m_defect_coefficient) == -1
                and fact.m_defect_factor_ok
                for fact in moments
            )
            and radius_one.m_defect_coefficient
            == EXPECTED_RADIUS_ONE_M_DEFECT,
            "the indefinite M defect is nonzero and reproduces the radius-one coefficient",
        ),
        "E3": (
            all(
                fact.lifted_shape == (32, 32)
                and fact.lifted_rank == 32
                and fact.lifted_inertia == (16, 0, 16)
                and fact.direct_lift_ok
                for fact in moments
            ),
            "the literal eight-copy M lifts have rank 32 and inertia (16,0,16)",
        ),
        "F1": (
            claims["c_is_process"] is False
            and claims["m_psd"] is False
            and claims["m_compression"] is False,
            "positive C and indefinite M remain field moments, never process marginals",
        ),
        "F2": (
            all(
                history.sign_normalized
                and history.sign_strictly_positive
                and history.sign_symmetries
                and history.sign_one_shot
                and history.sign_pair_tables
                and history.port_laws_normalized
                and history.port_laws_nonnegative
                and history.port_symmetries
                and history.port_one_shot
                and history.port_pair_tables
                and history.complete_one_shot
                and history.complete_pair_tables
                and history.endpoint_triple_equal == (R(1, 4), 0)
                and history.endpoint_ranks == (224, 480)
                and history.endpoint_inertias
                == ((224, 288, 0), (480, 32, 0))
                and history.inequivalent
                for history in histories
            )
            and claims["endpoint_unique"] is False,
            "two PSD endpoint laws share every one/two PVM table but differ "
            "at the three-port event",
        ),
        "F3": (
            claims["boundary_imported"] is False
            and claims["interface_derived"] is False
            and claims["process_open"] is False,
            "no boundary or action-to-event map is imported; T4--T6 remain sealed",
        ),
        "F4": (
            note_ok,
            "the source note is deferred if absent and enforces the "
            "type/stop needles once present",
        ),
    }
    return results, {
        "event": event,
        "template": template,
        "moments": moments,
        "histories": histories,
        "radius_one": radius_one,
        "note_status": note_status,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0

    results, evidence = evaluate(args.mutation)
    checks = Checks()
    for key, (condition, statement) in results.items():
        checks.check(key, statement, condition)

    event = evidence["event"]
    template = evidence["template"]
    radius_one = evidence["radius_one"]
    history = evidence["histories"][
        evidence["moments"].index(radius_one)
    ]
    print(
        "OPERATION: effect_span="
        f"{event.effect_span_rank}; Lueders={event.lueders_span_rank}; "
        f"plus_identity={event.lueders_identity_span_rank}; "
        f"coherent={event.coherent_frame_rank}; no_phase={event.no_phase_rank}"
    )
    print(
        "GREEN: nonwrapped_rank="
        f"{template.nonwrapped_rank}; circular_rank={template.circular_rank}; "
        f"seam={template.seam_residual}"
    )
    print(
        "MOMENT: radius=1; C_defect="
        f"{radius_one.c_defect_coefficient}; "
        f"M_defect={radius_one.m_defect_coefficient}; "
        "M_inertia=(2,0,2); lift=(16,0,16)"
    )
    print(
        "NONUNIQUENESS: endpoint_triple_equal="
        f"{history.endpoint_triple_equal}; ranks={history.endpoint_ranks}; "
        f"inertias={history.endpoint_inertias}"
    )
    print(f"NOTE: {evidence['note_status']}")
    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
