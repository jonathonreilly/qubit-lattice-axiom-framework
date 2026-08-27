#!/usr/bin/env python3
"""Independent Block-208 two-time Clifford-cell compiler checker.

This checker does not import the primary Block-208 runner.  It rebuilds the
cell channel from its displayed Choi entries, obtains the endpoint moments by
finite signed-axis sums, reconstructs the H1 source from inherited Block-193/
206 raw action data, and forms the relay section equations directly from the
proper-cubic action.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import permutations, product
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as h1_fixture  # noqa: E402
import admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26 as raw_h1  # noqa: E402


B = h1_fixture.b190
I = sp.I
R = sp.Rational
I2 = sp.eye(2)
I3 = sp.eye(3)
I4 = sp.eye(4)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -I), (I, 0)))
Z = sp.diag(1, -1)

AUDIT_TIMEOUT_SEC = 180
NOTE = (
    "docs/ADMISSIBILITY_D4_H1_TWO_TIME_CLIFFORD_CELL_M2_RECORD_COMPILER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PRIMARY = (
    "scripts/admissibility_d4_h1_two_time_clifford_cell_m2_record_"
    "compiler_2026_08_26.py"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block208-two-time-clifford-schur-m2-compiler-"
    "20260826"
)
GOAL = f"{PACKET}/GOAL.md"
PREFLIGHT = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AXIOM = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = "docs/audit/data/axiom_premise_nodes.json"
PARENT = "70a6b2ed31d26b6864d2fbdeab0a9336b0663f5c"
PREREG = "3dbd70623b218c60b72be93584028edaef406e91"
MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "2f66b1a9eea17ee9d81b5ddbe81d4a6253d800f8"
PREFLIGHT_BLOB = "9cd09e74fec58c315dbf43896345d2cfc1568ebc"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_TWO_TIME_CLIFFORD_CELL_M2_RECORD_COMPILER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_two_time_clifford_cell_m2_record_compiler_2026_08_26.py",
    ".claude/science/physics-loops/toe-axiom-closure-block208-two-time-clifford-schur-m2-compiler-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block208-two-time-clifford-schur-m2-compiler-20260826/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_EDGE_COMPARISON_CELL_CORNER_T2_FACTORIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_edge_comparison_cell_corner_t2_factorization_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_edge_comparison_cell_corner_t2_factorization_2026_08_26.txt",
    "docs/ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_DESCENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.txt",
    "docs/COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md",
)

MUTATIONS = (
    "stale_authority",
    "drop_registration",
    "alter_registry",
    "hide_scope_packet",
    "alter_cell_spectrum",
    "break_cell_marginal",
    "claim_nonreciprocal_channel",
    "flip_cell_phase",
    "break_36_sum",
    "merge_output_records",
    "claim_output_readable",
    "erase_dot_cross_decoder",
    "claim_sharpness_selected",
    "lower_group_rank",
    "lower_atom_rank",
    "erase_forward_source",
    "erase_reverse_source",
    "erase_p_collision",
    "break_12_sum",
    "erase_displaced_stencil",
    "collapse_component_score",
    "lower_temporal_rank",
    "erase_reverse_temporal",
    "lower_covariant_rank",
    "claim_unique_section",
    "erase_positive_alternate",
    "claim_physical_ownership",
    "open_h2",
    "claim_obligation_retirement",
    "claim_toe_progress",
    "claim_retained_status",
)

CELL_C = R(5, 13)
CELL_D = sp.simplify(1 / (1 - CELL_C**2))
CELL_S = sp.simplify(1 + CELL_D)
CELL_A = sp.simplify(CELL_C * CELL_D / CELL_S)
CELL_B = sp.simplify((1 - CELL_D) / CELL_S)


def exact_rank(matrix: sp.MatrixBase) -> int:
    """Rank over the smallest exact algebraic extension containing entries."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix), extension=True).rank()


def git_text(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority_data() -> dict[str, object]:
    return {
        "main": git_text("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "prereg": ancestor(PREREG),
        "goal_registered": git_text("rev-parse", f"{PREREG}:{GOAL}"),
        "goal_now": git_text("hash-object", "--", GOAL),
        "preflight_registered": git_text("rev-parse", f"{PREREG}:{PREFLIGHT}"),
        "preflight_now": git_text("hash-object", "--", PREFLIGHT),
        "axiom_main": git_text("rev-parse", f"origin/main:{AXIOM}"),
        "axiom_now": git_text("hash-object", "--", AXIOM),
        "registry_main": git_text("rev-parse", f"origin/main:{REGISTRY}"),
        "registry_now": git_text("hash-object", "--", REGISTRY),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


def pauli_frame(orientation: int) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    return X, orientation * Y, Z


def bloch_matrix(vector: sp.MatrixBase, orientation: int) -> sp.Matrix:
    return sp.simplify(sum(
        (vector[index] * pauli_frame(orientation)[index] for index in range(3)),
        sp.zeros(2),
    ))


def density(vector: sp.MatrixBase, orientation: int) -> sp.Matrix:
    return sp.simplify((I2 + bloch_matrix(vector, orientation)) / 2)


def cell_choi(orientation: int) -> sp.Matrix:
    numerator = sp.Matrix((
        (1, 0, 0, 0),
        (0, CELL_D, -orientation * I * CELL_C * CELL_D, 0),
        (0, orientation * I * CELL_C * CELL_D, CELL_D, 0),
        (0, 0, 0, 1),
    ))
    return sp.simplify(numerator / CELL_S)


def choi_blocks(choi: sp.MatrixBase) -> tuple[tuple[sp.Matrix, ...], ...]:
    indices = ((0, 1), (2, 3))
    return tuple(tuple(
        sp.Matrix(choi).extract(rows, columns)
        for columns in indices
    ) for rows in indices)


def choi_marginals(choi: sp.MatrixBase) -> tuple[sp.Matrix, sp.Matrix]:
    blocks = choi_blocks(choi)
    input_marginal = sp.Matrix(2, 2, lambda row, column: sp.trace(
        blocks[row][column]
    ))
    output_marginal = blocks[0][0] + blocks[1][1]
    return sp.simplify(input_marginal), sp.simplify(output_marginal)


def apply_choi(choi: sp.MatrixBase, operator: sp.MatrixBase) -> sp.Matrix:
    blocks = choi_blocks(choi)
    return sp.simplify(sum(
        (operator[row, column] * blocks[row][column]
         for row in range(2) for column in range(2)),
        sp.zeros(2),
    ))


def transfer_matrix(choi: sp.MatrixBase, frame: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sp.Matrix(3, 3, lambda row, column: sp.simplify(
        sp.trace(frame[row] * apply_choi(choi, frame[column])) / 2
    ))


@cache
def cell_data() -> dict[str, object]:
    expected = {
        R(144, 313): 2,
        R(104, 313): 1,
        R(234, 313): 1,
    }
    expected_complement = {
        R(169, 313): 2,
        R(209, 313): 1,
        R(79, 313): 1,
    }
    spectra = tuple(cell_choi(sign).eigenvals() for sign in (1, -1))
    complements = tuple((I4 - cell_choi(sign)).eigenvals()
                        for sign in (1, -1))
    marginals = tuple(choi_marginals(cell_choi(sign)) for sign in (1, -1))
    physical_transfers = tuple(
        transfer_matrix(cell_choi(sign), pauli_frame(sign))
        for sign in (1, -1)
    )
    conventional_transfers = tuple(
        transfer_matrix(cell_choi(sign), (X, Y, Z))
        for sign in (1, -1)
    )
    expected_transfer = sp.Matrix((
        (0, -R(65, 313), 0),
        (-R(65, 313), 0, 0),
        (0, 0, -R(25, 313)),
    ))
    state = cell_choi(1) / 2
    diagonal = tuple(state[index, index] for index in range(4))
    return {
        "spectra": spectra,
        "expected_spectrum": expected,
        "complements": complements,
        "expected_complement": expected_complement,
        "marginals": marginals,
        "conjugate": cell_choi(-1) == sp.conjugate(cell_choi(1)),
        "physical_transfers": physical_transfers,
        "expected_transfer": expected_transfer,
        "reciprocal": all(matrix == matrix.T for matrix in physical_transfers),
        "two_orders_equal": (
            conventional_transfers[0] * conventional_transfers[1]
            == conventional_transfers[1] * conventional_transfers[0]
        ),
        "a": CELL_A,
        "b": CELL_B,
        "state_trace": sp.trace(state),
        "state_marginals": choi_marginals(state),
        "time_odd": sp.simplify(
            diagonal[0] + diagonal[1] - diagonal[2] - diagonal[3]
        ),
        "mixed": sp.simplify(
            diagonal[0] - diagonal[1] - diagonal[2] + diagonal[3]
        ),
    }


@cache
def cell_phase_data() -> dict[str, object]:
    delta = sp.symbols("delta", real=True)
    first_vector = sp.Matrix((1, 0, 0))
    second_vector = sp.Matrix((sp.cos(delta), sp.sin(delta), 0))
    forward = []
    swapped = []
    for orientation in (1, -1):
        first = density(first_vector, orientation)
        second = density(second_vector, orientation)
        forward.append(sp.trigsimp(sp.trace(
            cell_choi(orientation)
            * sp.kronecker_product(first, second)
        )))
        swapped.append(sp.trigsimp(sp.trace(
            cell_choi(orientation)
            * sp.kronecker_product(second, first)
        )))
    expected_forward = R(1, 2) - R(65, 626) * sp.sin(delta)
    expected_swapped = R(1, 2) + R(65, 626) * sp.sin(delta)
    return {
        "forward": tuple(forward),
        "swapped": tuple(swapped),
        "formula": all(sp.simplify(sp.expand_complex(
            value - expected_forward
        )) == 0
                       for value in forward),
        "swap_formula": all(sp.simplify(sp.expand_complex(
            value - expected_swapped
        )) == 0
                            for value in swapped),
        "contrast_coefficient": -R(65, 313),
    }


def signed_axes() -> tuple[sp.Matrix, ...]:
    return tuple(
        sign * I3[:, axis]
        for axis in range(3) for sign in (-1, 1)
    )


@cache
def proper_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        matrix = sp.zeros(3)
        for row, column in enumerate(permutation):
            matrix[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            candidate = sp.diag(*signs) * matrix
            if candidate.det() == 1:
                rotations.append(candidate)
    return tuple(rotations)


def endpoint_effect(axis: sp.MatrixBase, orientation: int,
                    sharpness: sp.Expr = sp.Integer(1)) -> sp.Matrix:
    return sp.simplify((I2 + sharpness * bloch_matrix(axis, orientation)) / 6)


def output_bloch(first: sp.MatrixBase, second: sp.MatrixBase) -> sp.Matrix:
    return sp.simplify((first + 2 * second + first.cross(second)) / 8)


def moment_decode(first: sp.MatrixBase, second: sp.MatrixBase,
                  sharpness: sp.Expr = sp.Integer(1)) -> tuple[sp.Expr, sp.Matrix]:
    dot = sp.Integer(0)
    cross = sp.zeros(3, 1)
    for left in signed_axes():
        for right in signed_axes():
            probability = sp.expand(
                (1 + sharpness * left.dot(first))
                * (1 + sharpness * right.dot(second)) / 36
            )
            dot += 9 * left.dot(right) * probability / sharpness**2
            cross += 9 * left.cross(right) * probability / sharpness**2
    return sp.simplify(dot), sp.simplify(cross)


@cache
def endpoint_instrument_data() -> dict[str, object]:
    axes = signed_axes()
    normalization = []
    ranks = []
    traces = []
    for orientation in (1, -1):
        local = tuple(endpoint_effect(axis, orientation) for axis in axes)
        joint = tuple(sp.kronecker_product(left, right)
                      for left in local for right in local)
        normalization.append(sum(joint, sp.zeros(4)) == I4)
        ranks.extend(effect.rank() for effect in joint)
        traces.extend(sp.trace(effect) for effect in joint)

    codes = tuple(output_bloch(left, right)
                  for left in axes for right in axes)
    code_keys = {tuple(vector) for vector in codes}
    norms = {sp.simplify(vector.dot(vector)) for vector in codes}
    states_by_orientation = tuple(
        tuple(density(vector, orientation) for vector in codes)
        for orientation in (1, -1)
    )
    output_states = sum(states_by_orientation, ())
    determinants = tuple(sp.factor(state.det()) for state in output_states)
    output_ranks = tuple(state.rank() for state in output_states)
    output_traces = {sp.trace(state) for state in output_states}
    output_overlaps = tuple(
        sp.simplify(sp.trace(left * right))
        for states in states_by_orientation
        for index, left in enumerate(states)
        for right in states[index + 1:]
    )
    pairwise_overlaps_positive = all(value > 0 for value in output_overlaps)

    r_symbols = sp.Matrix(sp.symbols("r0:3", real=True))
    s_symbols = sp.Matrix(sp.symbols("s0:3", real=True))
    decoded_dot, decoded_cross = moment_decode(r_symbols, s_symbols)

    covariance = all(
        output_bloch(rotation * left, rotation * right)
        == rotation * output_bloch(left, right)
        and (rotation * left).cross(rotation * right)
        == rotation * left.cross(right)
        for rotation in proper_rotations()
        for left in axes for right in axes
    )

    sample_left = sp.Matrix((1, 0, 0))
    sample_right = sp.Matrix((R(1, 2), sp.sqrt(3) / 2, 0))
    sharp = tuple(sp.simplify(
        (1 + n.dot(sample_left)) * (1 + m.dot(sample_right)) / 36
    ) for n in axes for m in axes)
    half = tuple(sp.simplify(
        (1 + n.dot(sample_left) / 2) * (1 + m.dot(sample_right) / 2) / 36
    ) for n in axes for m in axes)
    sharp_decode = moment_decode(sample_left, sample_right, 1)
    half_decode = moment_decode(sample_left, sample_right, R(1, 2))
    return {
        "outcomes": 36,
        "normalization": all(normalization),
        "ranks": tuple(ranks),
        "traces": set(traces),
        "distinct_codes": len(code_keys),
        "norms": norms,
        "positive_outputs": all(value > 0 for value in determinants),
        "output_ranks": output_ranks,
        "output_traces": output_traces,
        "pairwise_overlaps_positive": pairwise_overlaps_positive,
        "record_readout_derived": not pairwise_overlaps_positive,
        "dot_decode": sp.expand(decoded_dot - r_symbols.dot(s_symbols)) == 0,
        "cross_decode": sp.expand(decoded_cross - r_symbols.cross(s_symbols))
        == sp.zeros(3, 1),
        "rotations": len(proper_rotations()),
        "covariance": covariance,
        "sharp_unsharp_distinct": sharp != half,
        "calibrated_equal": sharp_decode == half_decode,
        "sharpness_selected": False,
    }


def reverse_laurent(polynomial: B.PolyMatrix) -> B.PolyMatrix:
    reversed_polynomial: B.PolyMatrix = {}
    for exponent, coefficient in polynomial.items():
        transformed = exponent[:4] + tuple(
            exponent[index] - exponent[4 + index] for index in range(4)
        )
        reversed_polynomial = B.poly_add(
            reversed_polynomial, {transformed: coefficient}
        )
    return reversed_polynomial


def evaluate_laurent(polynomial: B.PolyMatrix,
                     incoming: tuple[sp.Expr, ...],
                     transfer: tuple[sp.Expr, ...]) -> sp.Matrix:
    incoming_units = tuple(sp.cos(angle) + I * sp.sin(angle)
                           for angle in incoming)
    transfer_units = tuple(sp.cos(angle) + I * sp.sin(angle)
                           for angle in transfer)
    value = sp.zeros(16)
    for exponent, coefficient in polynomial.items():
        monomial = sp.prod(
            incoming_units[index] ** exponent[index] for index in range(4)
        ) * sp.prod(
            transfer_units[index] ** exponent[4 + index] for index in range(4)
        )
        value += monomial * coefficient
    return sp.simplify(sp.expand_complex(sp.expand(value)))


@cache
def record_phase_ratio(angle: sp.Expr, orientation: int) -> sp.Expr:
    first = sp.Matrix((1, 0, 0))
    second = sp.Matrix((sp.cos(angle), sp.sin(angle), 0))
    dot, cross = moment_decode(first, second)
    result = sp.simplify(dot + orientation * I * cross[2])
    expected = sp.cos(angle) + orientation * I * sp.sin(angle)
    if sp.trigsimp(result - expected) != 0:
        raise AssertionError("signed-axis outcome decoder failed")
    return expected


def source_from_records(incoming: tuple[sp.Expr, ...],
                        transfer: tuple[sp.Expr, ...],
                        orientation: int,
                        reverse: bool = False) -> sp.Matrix:
    outgoing = tuple(incoming[index] + transfer[index] for index in range(4))
    first = [record_phase_ratio(angle, orientation) for angle in incoming]
    second = [record_phase_ratio(angle, orientation) for angle in outgoing]
    if reverse:
        first, second = second, first

    cosines = tuple(sp.simplify(
        (second[index] + sp.conjugate(first[index])) / 2
    ) for index in range(4))
    first_sines = tuple(sp.simplify(
        (first[index] - sp.conjugate(first[index])) / (2 * orientation * I)
    ) for index in range(4))
    second_sines = tuple(sp.simplify(
        (second[index] - sp.conjugate(second[index])) / (2 * orientation * I)
    ) for index in range(4))

    right_derivative = sum(
        (first_sines[index] * B.CREATION[index] for index in range(4)),
        sp.zeros(16),
    )
    left_derivative = sum(
        (second_sines[index] * B.CREATION[index].T for index in range(4)),
        sp.zeros(16),
    )
    coefficients = h1_fixture.tt_source_coefficients("H1", 1)
    result = sp.zeros(16)
    for slot in (8, 9):
        left, right = B.PAIRS4[slot]
        hodge = -cosines[left] * cosines[right] / sp.sqrt(2) * (
            B.CREATION[left] * B.ANNIHILATION[right]
            + B.CREATION[right] * B.ANNIHILATION[left]
        )
        result += coefficients[slot] * (
            B.MASS * hodge
            + orientation * I * hodge * right_derivative
            + orientation * I * left_derivative * hodge
        )
    return sp.simplify(sp.expand_complex(sp.expand(result)))


def native_hodge(slot: int) -> B.PolyMatrix:
    left, right = B.PAIRS4[slot]
    scalar = B.poly_scale(B.poly_multiply(
        B.placed_cosine(left), B.placed_cosine(right)
    ), -1 / sp.sqrt(2))
    operator = (
        B.CREATION[left] * B.ANNIHILATION[right]
        + B.CREATION[right] * B.ANNIHILATION[left]
    )
    return B.poly_multiply(scalar, {B.ZERO_EXPONENT: operator})


def derivative_polynomials(axis: int) -> tuple[B.PolyMatrix, B.PolyMatrix]:
    incoming = {
        B.exponent({axis: 1}): B.CREATION[axis] / (2 * I),
        B.exponent({axis: -1}): -B.CREATION[axis] / (2 * I),
    }
    outgoing = {
        B.exponent({axis: 1}, {axis: 1}): B.CREATION[axis] / (2 * I),
        B.exponent({axis: -1}, {axis: -1}): -B.CREATION[axis] / (2 * I),
    }
    return incoming, outgoing


def grouped_features() -> tuple[tuple[str, B.PolyMatrix, sp.Expr], ...]:
    coefficients = h1_fixture.tt_source_coefficients("H1", 1)
    features = []
    for slot in (8, 9):
        hodge = native_hodge(slot)
        features.append((f"{slot}:mass", hodge,
                         B.MASS * coefficients[slot]))
        for axis in range(4):
            incoming, outgoing = derivative_polynomials(axis)
            features.append((
                f"{slot}:right:{axis}",
                B.poly_scale(B.poly_multiply(hodge, incoming), I),
                coefficients[slot],
            ))
            features.append((
                f"{slot}:left:{axis}",
                B.poly_scale(B.poly_multiply(
                    B.poly_transpose(outgoing), hodge
                ), I),
                coefficients[slot],
            ))
    return tuple(features)


def coefficient_design(columns: tuple[B.PolyMatrix, ...],
                       target: B.PolyMatrix) -> tuple[sp.Matrix, sp.Matrix]:
    zero = sp.zeros(16)
    rows = sorted({
        (exponent, row, column)
        for polynomial in columns + (target,)
        for exponent, matrix in polynomial.items()
        for row in range(16) for column in range(16)
        if matrix[row, column] != 0
    })
    design = sp.MutableSparseMatrix(len(rows), len(columns), {})
    vector = sp.zeros(len(rows), 1)
    for row_index, (exponent, matrix_row, matrix_column) in enumerate(rows):
        for column_index, polynomial in enumerate(columns):
            value = polynomial.get(exponent, zero)[matrix_row, matrix_column]
            if value != 0:
                design[row_index, column_index] = value
        vector[row_index] = target.get(exponent, zero)[matrix_row, matrix_column]
    return sp.Matrix(design), vector


@cache
def reconstruction_data() -> dict[str, object]:
    source = raw_h1.combined_raw_source()
    reversed_source = reverse_laurent(source)
    features = grouped_features()
    columns = tuple(item[1] for item in features)
    weights = sp.Matrix(tuple(item[2] for item in features))
    grouped_matrix, grouped_vector = coefficient_design(columns, source)

    atoms = []
    atom_weights = []
    for _name, polynomial, weight in features:
        for exponent, coefficient in polynomial.items():
            atoms.append({exponent: coefficient})
            atom_weights.append(weight)
    atom_matrix, atom_vector = coefficient_design(tuple(atoms), source)

    reversed_columns = tuple(reverse_laurent(column) for column in columns)
    reverse_matrix, reverse_vector = coefficient_design(
        reversed_columns, reversed_source
    )
    reversed_atoms = tuple(reverse_laurent(atom) for atom in atoms)
    reverse_atom_matrix, reverse_atom_vector = coefficient_design(
        reversed_atoms, reversed_source
    )

    temporal = tuple(item for item in features if item[0].endswith(":3"))
    spatial = tuple(item for item in features if not item[0].endswith(":3"))
    temporal_target = source
    for _name, polynomial, weight in spatial:
        temporal_target = B.poly_add(
            temporal_target, B.poly_scale(polynomial, -weight)
        )
    temporal_matrix, temporal_vector = coefficient_design(
        tuple(item[1] for item in temporal), temporal_target
    )
    temporal_weights = sp.Matrix(tuple(item[2] for item in temporal))

    reverse_temporal = tuple(
        (name, reverse_laurent(polynomial), weight)
        for name, polynomial, weight in temporal
    )
    reverse_temporal_target = reversed_source
    for _name, polynomial, weight in spatial:
        reverse_temporal_target = B.poly_add(
            reverse_temporal_target,
            B.poly_scale(reverse_laurent(polynomial), -weight),
        )
    reverse_temporal_matrix, reverse_temporal_vector = coefficient_design(
        tuple(item[1] for item in reverse_temporal), reverse_temporal_target
    )

    incoming, transfer = h1_fixture.POINTS["H1"]
    forward_target = evaluate_laurent(source, incoming, transfer)
    reverse_target = evaluate_laurent(reversed_source, incoming, transfer)
    orientation_results = {}
    for orientation in (1, -1):
        forward = source_from_records(incoming, transfer, orientation)
        reverse = source_from_records(incoming, transfer, orientation, True)
        expected_forward = (forward_target if orientation == 1
                            else sp.conjugate(forward_target))
        expected_reverse = (reverse_target if orientation == 1
                            else sp.conjugate(reverse_target))
        orientation_results[orientation] = (
            sum(value != 0 for value in sp.simplify(
                forward - expected_forward
            )),
            sum(value != 0 for value in sp.simplify(
                reverse - expected_reverse
            )),
        )

    witness_exponent = (-1, 0, -1, -1, 0, 0, 0, -1)
    return {
        "group_shape": grouped_matrix.shape,
        "group_rank": exact_rank(grouped_matrix),
        "group_augmented": exact_rank(grouped_matrix.row_join(grouped_vector)),
        "group_residual": sum(
            value != 0 for value in grouped_matrix * weights - grouped_vector
        ),
        "atom_shape": atom_matrix.shape,
        "atom_rank": exact_rank(atom_matrix),
        "atom_augmented": exact_rank(atom_matrix.row_join(atom_vector)),
        "atom_residual": sum(
            value != 0
            for value in atom_matrix * sp.Matrix(atom_weights) - atom_vector
        ),
        "reverse_rank": exact_rank(reverse_matrix),
        "reverse_augmented": exact_rank(reverse_matrix.row_join(reverse_vector)),
        "reverse_residual": sum(
            value != 0 for value in reverse_matrix * weights - reverse_vector
        ),
        "reverse_atom_rank": exact_rank(reverse_atom_matrix),
        "reverse_atom_augmented": exact_rank(
            reverse_atom_matrix.row_join(reverse_atom_vector)
        ),
        "reverse_atom_residual": sum(
            value != 0
            for value in reverse_atom_matrix * sp.Matrix(atom_weights)
            - reverse_atom_vector
        ),
        "orientations": orientation_results,
        "spatial_columns": len(spatial),
        "temporal_columns": len(temporal),
        "temporal_shape": temporal_matrix.shape,
        "temporal_rank": exact_rank(temporal_matrix),
        "temporal_augmented": exact_rank(
            temporal_matrix.row_join(temporal_vector)
        ),
        "temporal_residual": sum(
            value != 0
            for value in temporal_matrix * temporal_weights - temporal_vector
        ),
        "reverse_temporal_shape": reverse_temporal_matrix.shape,
        "reverse_temporal_rank": exact_rank(reverse_temporal_matrix),
        "reverse_temporal_augmented": exact_rank(
            reverse_temporal_matrix.row_join(reverse_temporal_vector)
        ),
        "reverse_temporal_residual": sum(
            value != 0
            for value in reverse_temporal_matrix * temporal_weights
            - reverse_temporal_vector
        ),
        "temporal_witness": sp.simplify(
            source[witness_exponent][1, 12]
        ),
    }


@cache
def collision_data() -> dict[str, object]:
    incoming, transfer = h1_fixture.POINTS["H1"]
    alternate = (sp.Integer(0), sp.Integer(0), sp.Integer(0), incoming[3])
    alternate_transfer = tuple(transfer)
    source = raw_h1.combined_raw_source()
    reverse_source = reverse_laurent(source)
    results = {}
    for orientation in (1, -1):
        main_forward = source_from_records(incoming, transfer, orientation)
        alt_forward = source_from_records(
            alternate, alternate_transfer, orientation
        )
        main_reverse = source_from_records(incoming, transfer, orientation, True)
        alt_reverse = source_from_records(
            alternate, alternate_transfer, orientation, True
        )
        forward_difference = sp.simplify(main_forward - alt_forward)
        reverse_difference = sp.simplify(main_reverse - alt_reverse)
        alt_target = evaluate_laurent(source, alternate, alternate_transfer)
        alt_reverse_target = evaluate_laurent(
            reverse_source, alternate, alternate_transfer
        )
        if orientation == -1:
            alt_target = sp.conjugate(alt_target)
            alt_reverse_target = sp.conjugate(alt_reverse_target)
        results[orientation] = {
            "forward_rank": exact_rank(forward_difference),
            "forward_nnz": sum(value != 0 for value in forward_difference),
            "reverse_rank": exact_rank(reverse_difference),
            "reverse_nnz": sum(value != 0 for value in reverse_difference),
            "alternate_forward_residual": sum(
                value != 0 for value in sp.simplify(alt_forward - alt_target)
            ),
            "alternate_reverse_residual": sum(
                value != 0
                for value in sp.simplify(alt_reverse - alt_reverse_target)
            ),
        }
    return {
        "same_transfer": transfer == alternate_transfer,
        "different_incoming": incoming != alternate,
        "orientations": results,
    }


def corners() -> tuple[sp.Matrix, ...]:
    return tuple(sp.Matrix(values) for values in product((-1, 1), repeat=3))


def edges() -> tuple[sp.Matrix, ...]:
    return tuple(
        sign * I3[:, axis]
        for axis in range(3) for sign in (1, -1)
    )


def shell_permutation(rotation: sp.MatrixBase,
                      shell: tuple[sp.Matrix, ...]) -> sp.Matrix:
    representation = sp.zeros(len(shell))
    for source, vector in enumerate(shell):
        transformed = sp.Matrix(rotation * vector)
        target = next(index for index, candidate in enumerate(shell)
                      if candidate == transformed)
        representation[target, source] = 1
    return representation


def shear_representation(rotation: sp.MatrixBase) -> sp.Matrix:
    basis = (
        sp.Matrix(((0, 1, 0), (1, 0, 0), (0, 0, 0))),
        sp.Matrix(((0, 0, 0), (0, 0, 1), (0, 1, 0))),
        sp.Matrix(((0, 0, 1), (0, 0, 0), (1, 0, 0))),
    )
    columns = []
    for tensor in basis:
        transformed = sp.Matrix(rotation * tensor * rotation.T)
        columns.append(sp.Matrix((
            transformed[0, 1], transformed[1, 2], transformed[0, 2]
        )))
    return sp.Matrix.hstack(*columns)


def odd_edge_decoder() -> sp.Matrix:
    decoder = sp.zeros(3, 18)
    for row, (first_axis, second_axis) in enumerate(((0, 1), (1, 2), (0, 2))):
        for edge, sign in ((2 * first_axis, 1), (2 * first_axis + 1, -1)):
            decoder[row, 3 * edge + second_axis] -= sign
        for edge, sign in ((2 * second_axis, 1), (2 * second_axis + 1, -1)):
            decoder[row, 3 * edge + first_axis] -= sign
    return decoder


def face_average() -> sp.Matrix:
    average = sp.zeros(18, 24)
    for edge_index, direction in enumerate(edges()):
        axis = next(index for index, value in enumerate(direction) if value)
        sign = direction[axis]
        for corner_index, corner in enumerate(corners()):
            if corner[axis] == sign:
                for component in range(3):
                    average[3 * edge_index + component,
                            3 * corner_index + component] = R(1, 4)
    return average


def radial_decoder() -> sp.Matrix:
    return sp.simplify(odd_edge_decoder() * face_average())


@cache
def relay_data() -> dict[str, object]:
    radial = radial_decoder()
    coefficients = h1_fixture.tt_source_coefficients("H1", 1)
    h = sp.Matrix((
        coefficients[7] / sp.sqrt(2),
        coefficients[9] / sp.sqrt(2),
        coefficients[8] / sp.sqrt(2),
    ))
    minimum_section = radial.T
    corner_field = sp.simplify(minimum_section * h)
    tensor = sp.Matrix((
        (0, h[0], h[2]),
        (h[0], 0, h[1]),
        (h[2], h[1], 0),
    ))
    geometric_field = sp.Matrix.vstack(*(
        -tensor * corner / 4 for corner in corners()
    ))
    corner_norms = tuple(sp.simplify(sum(
        corner_field[3 * index + component] ** 2
        for component in range(3)
    )) for index in range(8))

    effect_normalizations = []
    effect_ranks = []
    effect_values = []
    probability_formula = []
    for orientation in (1, -1):
        effects = []
        for time_sign in (-1, 1):
            time_projector = (I2 + time_sign * Z) / 2
            for axis in range(3):
                for outcome_sign in (-1, 1):
                    internal = (
                        I2 + outcome_sign * pauli_frame(orientation)[axis]
                    ) / 2
                    effects.append(
                        sp.kronecker_product(time_projector, internal) / 3
                    )
        effect_normalizations.append(sum(effects, sp.zeros(4)) == I4)
        effect_ranks.extend(effect.rank() for effect in effects)
        effect_values.extend(
            next(value for value in effect.eigenvals() if value != 0)
            for effect in effects
        )

        for corner_index in range(8):
            vector = corner_field[3 * corner_index:3 * corner_index + 3, :]
            state = sp.kronecker_product(I2 / 2, density(vector, orientation))
            cursor = 0
            for _time_sign in (-1, 1):
                for axis in range(3):
                    for outcome_sign in (-1, 1):
                        probability_formula.append(sp.simplify(
                            sp.trace(effects[cursor] * state)
                            - (1 + outcome_sign * vector[axis]) / 12
                        ) == 0)
                        cursor += 1

    z, u = sp.symbols("z u", nonzero=True)
    incoming_scores = []
    outgoing_scores = []
    incoming_stencils = []
    outgoing_stencils = []
    for component in corner_field:
        incoming = sp.simplify(sum(
            3 * time_sign * outcome_sign
            * (1 + outcome_sign * component) / 12
            * z**time_sign
            for time_sign in (-1, 1) for outcome_sign in (-1, 1)
        ))
        outgoing = sp.simplify(sum(
            3 * time_sign * outcome_sign
            * (1 + outcome_sign * component) / 12
            * (z * u) ** time_sign
            for time_sign in (-1, 1) for outcome_sign in (-1, 1)
        ))
        incoming_scores.append(incoming)
        outgoing_scores.append(outgoing)
        incoming_stencils.append(sp.simplify(
            incoming - component * (z - z**-1) / 2
        ))
        outgoing_stencils.append(sp.simplify(
            outgoing - component * (z * u - z**-1 * u**-1) / 2
        ))

    reverse_map = {z: z * u, u: u**-1}
    actual_reverse_intertwining = all(
        sp.simplify(incoming.subs(reverse_map, simultaneous=True) - outgoing)
        == 0
        and sp.simplify(
            outgoing.subs(reverse_map, simultaneous=True) - incoming
        ) == 0
        for incoming, outgoing in zip(incoming_scores, outgoing_scores)
    )

    cell = cell_data()
    reconstruction = reconstruction_data()
    return {
        "cell_trace": cell["state_trace"],
        "cell_marginals": cell["state_marginals"],
        "cell_time_odd": cell["time_odd"],
        "cell_mixed": cell["mixed"],
        "outcomes": 12,
        "normalization": all(effect_normalizations),
        "effect_ranks": tuple(effect_ranks),
        "effect_values": set(effect_values),
        "probability_formula": all(probability_formula),
        "radial_orthonormal": radial * radial.T == I3,
        "right_inverse": radial * minimum_section == I3,
        "field_formula": corner_field == geometric_field,
        "field_decode": radial * corner_field == h,
        "max_norm": max(corner_norms, key=lambda value: float(value)),
        "positive": all(value < 1 for value in corner_norms),
        "incoming_stencil": all(value == 0 for value in incoming_stencils),
        "outgoing_stencil": all(value == 0 for value in outgoing_stencils),
        "componentwise_symbol_count": (
            len(incoming_scores), len(outgoing_scores)
        ),
        "actual_reverse_intertwining": actual_reverse_intertwining,
        "spatial_columns": reconstruction["spatial_columns"],
        "temporal_columns": reconstruction["temporal_columns"],
        "temporal_shape": reconstruction["temporal_shape"],
        "temporal_rank": reconstruction["temporal_rank"],
        "temporal_augmented": reconstruction["temporal_augmented"],
        "temporal_residual": reconstruction["temporal_residual"],
        "reverse_temporal_shape": reconstruction["reverse_temporal_shape"],
        "reverse_temporal_rank": reconstruction["reverse_temporal_rank"],
        "reverse_temporal_augmented": reconstruction[
            "reverse_temporal_augmented"
        ],
        "reverse_temporal_residual": reconstruction[
            "reverse_temporal_residual"
        ],
        "temporal_witness": reconstruction["temporal_witness"],
    }


@cache
def section_data() -> dict[str, object]:
    corner_shell = corners()
    covariance_blocks = []
    for rotation in proper_rotations():
        corner_action = shell_permutation(rotation, corner_shell)
        domain = sp.kronecker_product(corner_action, rotation)
        target = shear_representation(rotation)
        covariance_blocks.append(
            sp.kronecker_product(domain, I3)
            - sp.kronecker_product(sp.eye(24), target.T)
        )
    covariance = sp.Matrix.vstack(*covariance_blocks)
    radial = radial_decoder()
    right_inverse_constraints = sp.kronecker_product(radial, I3)
    section_system = covariance.col_join(right_inverse_constraints)

    minimum_section = radial.T
    nullspace = section_system.nullspace(simplify=False)
    alternative = minimum_section + sp.Matrix(
        24, 3, list(nullspace[-1])
    ) / 32
    coefficients = h1_fixture.tt_source_coefficients("H1", 1)
    h = sp.Matrix((
        coefficients[7] / sp.sqrt(2),
        coefficients[9] / sp.sqrt(2),
        coefficients[8] / sp.sqrt(2),
    ))
    alternative_field = alternative * h
    norms = tuple(sp.simplify(sum(
        alternative_field[3 * index + component] ** 2
        for component in range(3)
    )) for index in range(8))
    return {
        "covariance_shape": covariance.shape,
        "covariance_rank": exact_rank(covariance),
        "section_shape": section_system.shape,
        "section_rank": exact_rank(section_system),
        "affine_dimension": 72 - exact_rank(section_system),
        "minimum_covariant": (
            covariance * sp.Matrix(list(minimum_section)) == sp.zeros(1728, 1)
        ),
        "minimum_right_inverse": radial * minimum_section == I3,
        "alternate_distinct": alternative != minimum_section,
        "alternate_covariant": (
            covariance * sp.Matrix(list(alternative)) == sp.zeros(1728, 1)
        ),
        "alternate_right_inverse": radial * alternative == I3,
        "alternate_positive": all(value < 1 for value in norms),
        "selected": False,
    }


@cache
def note_data() -> dict[str, object]:
    path = ROOT / NOTE
    if not path.is_file():
        return {"packet": False, "n1n8": False, "n5": False}
    text = path.read_text()
    return {
        "packet": all(phrase in text for phrase in (
            "claim_type: bounded_theorem",
            "complete_h1_physical_ownership: false",
            "obligation_retirement: 0",
            "toe_percentage_movement: 0",
            "typed compiler support",
            "action-to-`M2` state solder",
            "cell-corner tensor legs",
            "H2 remains sealed",
        )),
        "n1n8": all(f"### N{index}" in text for index in range(1, 9)),
        "n5": all(prefix in text for prefix in (
            "per_element:", "per_site:", "per_mode:",
            "per_block:", "lattice_wide:",
        )),
    }


N5_LINES = (
    "per_element: checked both conjugate cell matrices, all 36 endpoint effects and full-rank outputs, every positive pairwise overlap, all 12 relay effects, and exact normalization.",
    "per_site: checked the two-endpoint compiler and displaced one-site writes; checked and not executed — overlapping outputs do not supply a readable Record or action-to-M2 state solder.",
    "per_mode: checked all fixed H1 incoming/outgoing phase ratios, both orientations, actual reversal, and the same-q different-p collision; H2 was not opened.",
    "per_block: checked grouped and atom ranks 18/18 and 136/136, exact forward/reverse source equality, and full-minus-spatial 128-by-4 temporal targets in both directions.",
    "lattice_wide: checked all 24 proper-cubic transports and componentwise relay scores locally; checked and not executed — no global inverse, formation/history law, retained status, or TOE movement was claimed.",
)


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_data()
    cell = cell_data()
    phase = cell_phase_data()
    endpoint = endpoint_instrument_data()
    reconstruction = reconstruction_data()
    collision = collision_data()
    relay = relay_data()
    section = section_data()
    note = note_data()

    claims: dict[str, object] = {
        "main": MAIN,
        "registration": True,
        "registry": REGISTRY_WORKTREE_BLOB,
        "scope_packet": True,
        "cell_spectrum": cell["expected_spectrum"],
        "cell_marginal": True,
        "channel_reciprocal": True,
        "phase_coefficient": -R(65, 313),
        "endpoint_sum": True,
        "output_count": 36,
        "output_readable": False,
        "phase_decoder": True,
        "sharpness_selected": False,
        "group_rank": 18,
        "atom_rank": 136,
        "forward_residual": 0,
        "reverse_residual": 0,
        "collision_rank": 12,
        "relay_sum": True,
        "displaced": True,
        "component_count": (24, 24),
        "temporal_rank": 4,
        "reverse_temporal_residual": 0,
        "covariance_rank": 69,
        "section_dimension": 2,
        "positive_alternate": True,
        "physical_ownership": False,
        "h2_open": False,
        "obligation_retirement": 0,
        "toe_movement": 0,
        "retained": False,
    }
    mutation_map = {
        "stale_authority": ("main", "stale"),
        "drop_registration": ("registration", False),
        "alter_registry": ("registry", "altered"),
        "hide_scope_packet": ("scope_packet", False),
        "alter_cell_spectrum": ("cell_spectrum", {}),
        "break_cell_marginal": ("cell_marginal", False),
        "claim_nonreciprocal_channel": ("channel_reciprocal", False),
        "flip_cell_phase": ("phase_coefficient", R(65, 313)),
        "break_36_sum": ("endpoint_sum", False),
        "merge_output_records": ("output_count", 35),
        "claim_output_readable": ("output_readable", True),
        "erase_dot_cross_decoder": ("phase_decoder", False),
        "claim_sharpness_selected": ("sharpness_selected", True),
        "lower_group_rank": ("group_rank", 17),
        "lower_atom_rank": ("atom_rank", 135),
        "erase_forward_source": ("forward_residual", 1),
        "erase_reverse_source": ("reverse_residual", 1),
        "erase_p_collision": ("collision_rank", 0),
        "break_12_sum": ("relay_sum", False),
        "erase_displaced_stencil": ("displaced", False),
        "collapse_component_score": ("component_count", (1, 1)),
        "lower_temporal_rank": ("temporal_rank", 3),
        "erase_reverse_temporal": ("reverse_temporal_residual", 1),
        "lower_covariant_rank": ("covariance_rank", 68),
        "claim_unique_section": ("section_dimension", 0),
        "erase_positive_alternate": ("positive_alternate", False),
        "claim_physical_ownership": ("physical_ownership", True),
        "open_h2": ("h2_open", True),
        "claim_obligation_retirement": ("obligation_retirement", 1),
        "claim_toe_progress": ("toe_movement", 1),
        "claim_retained_status": ("retained", True),
    }
    if mutation:
        key, value = mutation_map[mutation]
        claims[key] = value

    authority_ok = (
        authority["main"] == claims["main"]
        and authority["parent"]
        and authority["prereg"] == claims["registration"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_now"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_now"] == PREFLIGHT_BLOB
        and authority["axiom_main"] == AXIOM_BLOB
        and authority["axiom_now"] == AXIOM_BLOB
        and authority["registry_main"] == REGISTRY_MAIN_BLOB
        and authority["registry_now"] == claims["registry"]
        and authority["inputs"]
    )
    cell_ok = (
        all(spectrum == claims["cell_spectrum"] for spectrum in cell["spectra"])
        and all(spectrum == cell["expected_complement"]
                for spectrum in cell["complements"])
        and (all(pair == (I2, I2) for pair in cell["marginals"])
             == claims["cell_marginal"])
        and cell["conjugate"]
        and all(matrix == cell["expected_transfer"]
                for matrix in cell["physical_transfers"])
        and cell["reciprocal"] == claims["channel_reciprocal"]
        and cell["two_orders_equal"]
    )
    phase_ok = (
        phase["formula"] and phase["swap_formula"]
        and phase["contrast_coefficient"] == claims["phase_coefficient"]
    )
    endpoint_ok = (
        endpoint["outcomes"] == 36
        and endpoint["normalization"] == claims["endpoint_sum"]
        and set(endpoint["ranks"]) == {1}
        and endpoint["traces"] == {R(1, 9)}
        and endpoint["distinct_codes"] == claims["output_count"]
        and endpoint["norms"] == {R(1, 64), R(3, 32), R(9, 64)}
        and endpoint["positive_outputs"]
        and set(endpoint["output_ranks"]) == {2}
        and endpoint["output_traces"] == {1}
        and endpoint["pairwise_overlaps_positive"]
        and endpoint["record_readout_derived"] == claims["output_readable"]
    )
    decoder_ok = (
        (endpoint["dot_decode"] and endpoint["cross_decode"])
        == claims["phase_decoder"]
        and endpoint["rotations"] == 24
        and endpoint["covariance"]
        and endpoint["sharp_unsharp_distinct"]
        and endpoint["calibrated_equal"]
        and endpoint["sharpness_selected"] == claims["sharpness_selected"]
    )
    reconstruction_ok = (
        reconstruction["group_rank"] == claims["group_rank"]
        and reconstruction["group_augmented"] == 18
        and reconstruction["group_residual"] == 0
        and reconstruction["atom_rank"] == claims["atom_rank"]
        and reconstruction["atom_augmented"] == 136
        and reconstruction["atom_residual"] == 0
        and reconstruction["reverse_rank"] == 18
        and reconstruction["reverse_augmented"] == 18
        and reconstruction["reverse_residual"] == 0
        and reconstruction["reverse_atom_rank"] == 136
        and reconstruction["reverse_atom_augmented"] == 136
        and reconstruction["reverse_atom_residual"] == 0
        and all(result[0] == claims["forward_residual"]
                and result[1] == claims["reverse_residual"]
                for result in reconstruction["orientations"].values())
    )
    collision_ok = (
        collision["same_transfer"]
        and collision["different_incoming"]
        and all(
            item["forward_rank"] == claims["collision_rank"]
            and item["reverse_rank"] == claims["collision_rank"]
            and item["forward_nnz"] == 56
            and item["reverse_nnz"] == 56
            and item["alternate_forward_residual"] == 0
            and item["alternate_reverse_residual"] == 0
            for item in collision["orientations"].values()
        )
    )
    relay_ok = (
        relay["cell_trace"] == 1
        and relay["cell_marginals"] == (I2 / 2, I2 / 2)
        and relay["cell_time_odd"] == 0
        and relay["cell_mixed"] == -R(25, 313)
        and relay["outcomes"] == 12
        and relay["normalization"] == claims["relay_sum"]
        and set(relay["effect_ranks"]) == {1}
        and relay["effect_values"] == {R(1, 3)}
        and relay["probability_formula"]
        and relay["radial_orthonormal"]
        and relay["right_inverse"]
        and relay["field_formula"] and relay["field_decode"]
        and relay["max_norm"] == (3 + sp.sqrt(2)) / 16
        and relay["positive"]
        and (relay["incoming_stencil"] and relay["outgoing_stencil"])
        == claims["displaced"]
        and relay["componentwise_symbol_count"] == claims["component_count"]
        and relay["actual_reverse_intertwining"]
        and relay["spatial_columns"] == 14
        and relay["temporal_columns"] == 4
        and relay["temporal_shape"] == (128, 4)
        and relay["temporal_rank"] == claims["temporal_rank"]
        and relay["temporal_augmented"] == 4
        and relay["temporal_residual"] == 0
        and relay["reverse_temporal_shape"] == (128, 4)
        and relay["reverse_temporal_rank"] == 4
        and relay["reverse_temporal_augmented"] == 4
        and relay["reverse_temporal_residual"]
        == claims["reverse_temporal_residual"]
        and relay["temporal_witness"] == R(1, 8)
    )
    section_ok = (
        section["covariance_shape"] == (1728, 72)
        and section["covariance_rank"] == claims["covariance_rank"]
        and section["section_shape"] == (1737, 72)
        and section["section_rank"] == 70
        and section["affine_dimension"] == claims["section_dimension"]
        and section["minimum_covariant"] and section["minimum_right_inverse"]
        and section["alternate_distinct"] and section["alternate_covariant"]
        and section["alternate_right_inverse"]
        and section["alternate_positive"] == claims["positive_alternate"]
        and section["selected"] is False
    )
    scope_ok = (
        note["packet"] == claims["scope_packet"]
        and note["n1n8"] and note["n5"]
        and claims["physical_ownership"] is False
        and claims["h2_open"] is False
        and claims["obligation_retirement"] == 0
        and claims["toe_movement"] == 0
        and claims["retained"] is False
    )
    return {
        "A": (authority_ok, "authority, immutable preregistration, and all audit inputs are pinned"),
        "B": (cell_ok, "both cell orientations have the strict Choi/effect spectra, unit marginals, reciprocal transfer, and commuting orders"),
        "C": (phase_ok, "the cell effect has contrast -(65/313) sin(delta), with endpoint swap and conjugate-reading checks"),
        "D": (endpoint_ok, "the 36 endpoint effects normalize and write distinct full-rank overlapping outputs without deriving readable Records"),
        "E": (decoder_ok, "finite outcome sums recover dot and cross exactly in all 24 cubic frames while sharpness remains unselected"),
        "F": (reconstruction_ok, "grouped/atom ranks and forward/actual-reverse H1 residuals agree exactly in both orientations"),
        "G": (collision_ok, "actual endpoint phases separate the same-q different-p control at rank/nnz 12/56 in both directions"),
        "H": (relay_ok, "the 12-outcome relay supplies componentwise displaced 128-by-4 full-minus-spatial targets in both time directions"),
        "I": (section_ok, "equivariant section ranks are 69/70 and a distinct strictly positive alternate right inverse survives"),
        "J": (scope_ok, "physical ownership, H2, retention, obligation retirement, and TOE movement remain outside the proved scope"),
    }


def mutation_sweep() -> int:
    survivors = []
    for mutation in MUTATIONS:
        if all(ok for ok, _message in evaluate(mutation).values()):
            survivors.append(mutation)
    passed = len(MUTATIONS) - len(survivors)
    print(f"MUTATION_TOTAL: PASS={passed} FAIL={len(survivors)}")
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
    print(f"TOTAL: PASS={passed} FAIL={len(survivors)}")
    return 1 if survivors else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()

    checks = evaluate(args.mutation)
    passed = 0
    for name, (ok, message) in checks.items():
        print(f"[{name}] {'PASS' if ok else 'FAIL'}: {message}")
        passed += int(bool(ok))
    print(
        "CELL: spectrum={144/313(x2),104/313,234/313}; partial traces=I2; "
        "transfer=(-65/313 swap_xy,-25/313 z); channel order reciprocal."
    )
    print(
        "ENDPOINT: outcomes=36; sum=I4; output norms="
        "{1/64,3/32,9/64}; full-rank overlaps>0; Record readout=open; "
        "dot/cross decoder exact."
    )
    print(
        "H1: grouped=18/18; atoms=136/136; forward/reverse residual=0/0 "
        "for eta=+/-; same-q collision rank/nnz=12/56."
    )
    print(
        "RELAY: outcomes=12; 24+24 component scores; full-minus-spatial "
        "forward/reverse designs=128x4 rank=4; section ranks=69/70; "
        "positive alternate=true."
    )
    print(
        "SCOPE: typed compiler support only; complete ownership=false; H2=false; "
        "obligation retirement=0; TOE movement=0."
    )
    for line in N5_LINES:
        print(line)
    failed = len(checks) - passed
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
