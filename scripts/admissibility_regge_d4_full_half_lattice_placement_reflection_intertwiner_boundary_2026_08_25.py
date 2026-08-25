#!/usr/bin/env python3
"""Block 196: exact Regge--D4 placement/reflection chain gate.

The runner first reproduces the registered 15/22/40 carrier census, the
raw-column-identity Ward prefilter, and the single/temporal-cover fixed-point
obstructions.  It then opens exactly one target: the frozen four-singleton-
grade, row-face one-cell equation M Gamma_D = G_R diag(u_mu).  Any failure
seals induction, action, Riesz, source, and response stages.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import permutations, product
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PARENT_COMMIT = "9bc5dfe2fc7b0bd1c7e5547f0ca621986e71f21d"
PREREG_COMMIT = "3241d452c580f7a09597c3e40070ab95669507bd"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
WALL_CAP_SECONDS = 20 * 60
RSS_CAP_BYTES = 3 * 1024**3

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block196-regge-d4-placement-reflection-20260825/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block196-regge-d4-placement-reflection-20260825/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block196-regge-d4-placement-reflection-20260825/STATE.yaml",
    "docs/ADMISSIBILITY_REGGE_D4_FULL_HALF_LATTICE_PLACEMENT_REFLECTION_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_PREFIX_INSTRUMENT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
    "scripts/admissibility_d4_grade3_source_instrument_history_write_2026_08_24.py",
    "scripts/admissibility_regge_d4_full_half_lattice_placement_reflection_intertwiner_boundary_2026_08_25.py",
)

MUTATIONS = (
    "wrong_component_order",
    "erase_reversal_anchor",
    "claim_15_full_covariance",
    "flip_raw_laurent_sign",
    "claim_single_cover_rank_four",
    "claim_temporal_cover_rank_four",
    "wrong_half_variable_inversion",
    "treat_sheets_as_species",
    "replace_c_with_identity",
    "use_invalid_one_coset",
    "fit_shared_rows",
    "omit_group_composition",
    "omit_nyquist",
    "accept_pseudoinverse",
    "open_action_early",
    "open_response_early",
    "claim_broad_no_go",
)
MUTATION_FAMILY = {
    "wrong_component_order": "K1",
    "erase_reversal_anchor": "K0",
    "claim_15_full_covariance": "K0",
    "flip_raw_laurent_sign": "K1",
    "claim_single_cover_rank_four": "K2",
    "claim_temporal_cover_rank_four": "K3",
    "wrong_half_variable_inversion": "T1",
    "treat_sheets_as_species": "T1",
    "replace_c_with_identity": "T1",
    "use_invalid_one_coset": "T2",
    "fit_shared_rows": "T3",
    "omit_group_composition": "T4",
    "omit_nyquist": "T5",
    "accept_pseudoinverse": "T2",
    "open_action_early": "S",
    "open_response_early": "S",
    "claim_broad_no_go": "S",
}

I = sp.I
SQRT2 = sp.sqrt(2)
SQRT3 = sp.sqrt(3)
ZERO = (0, 0, 0, 0)
PAIRS = (
    (3, 3), (0, 0), (1, 1), (2, 2),
    (0, 3), (1, 3), (2, 3),
    (0, 1), (0, 2), (1, 2),
)
PAIR_INDEX = {tuple(sorted(pair)): slot for slot, pair in enumerate(PAIRS)}
REGGE_HCOMPS = (
    (0, 0), (1, 1), (2, 2), (3, 3),
    (0, 1), (0, 2), (0, 3),
    (1, 2), (1, 3), (2, 3),
)
D4_TO_REGGE = (3, 0, 1, 2, 6, 8, 9, 4, 5, 7)
DIRS15 = tuple(direction for direction in product((0, 1), repeat=4) if any(direction))
TIME_REFLECTION = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, -1),
)
SPATIAL_HALF_TURN = (
    (-1, 0, 0, 0),
    (0, -1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
COMMON_MINOR_ROWS = (0, 1, 2, 3, 4, 5, 7, 8, 9, 11)


class ResourceCap(RuntimeError):
    pass


def _alarm(_signum: int, _frame: object) -> None:
    raise ResourceCap("20-minute exact-solver wall cap reached")


def install_resource_caps() -> None:
    signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(WALL_CAP_SECONDS)
    try:
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        target = RSS_CAP_BYTES if hard < 0 else min(RSS_CAP_BYTES, hard)
        resource.setrlimit(resource.RLIMIT_AS, (target, target))
    except (AttributeError, OSError, ValueError):
        # macOS does not enforce RLIMIT_RSS; the surrounding execution lane
        # supplies the same 3 GiB cap when RLIMIT_AS is unavailable.
        pass


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    ).returncode == 0


def unit(axis: int, value: int = 1) -> tuple[int, ...]:
    return tuple(value if slot == axis else 0 for slot in range(4))


def add_exp(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def matvec(matrix: tuple[tuple[int, ...], ...], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(matrix[row][column] * vector[column] for column in range(4)) for row in range(4))


def transpose(matrix: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(matrix[column][row] for column in range(4)) for row in range(4))


def matmul(
    left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(sum(left[row][middle] * right[middle][column] for middle in range(4)) for column in range(4))
        for row in range(4)
    )


IDENTITY4 = tuple(tuple(int(row == column) for column in range(4)) for row in range(4))


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation)) for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def proper_spatial_frames() -> tuple[tuple[tuple[int, ...], ...], ...]:
    frames = []
    for permutation in permutations(range(3)):
        parity = permutation_sign(permutation)
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] != 1:
                continue
            frame = [[0] * 4 for _ in range(4)]
            for row, column in enumerate(permutation):
                frame[row][column] = signs[row]
            frame[3][3] = 1
            frames.append(tuple(tuple(row) for row in frame))
    return tuple(frames)


FRAMES = proper_spatial_frames()


def canonical_edge(direction: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    for value in direction:
        if value > 0:
            return direction, ZERO
        if value < 0:
            return tuple(-item for item in direction), direction
    raise AssertionError("zero is not an edge direction")


def carrier_orbit(
    seeds: tuple[tuple[int, ...], ...], frames: tuple[tuple[tuple[int, ...], ...], ...]
) -> tuple[tuple[int, ...], ...]:
    images = {
        canonical_edge(matvec(frame, direction))[0]
        for frame in frames for direction in seeds
    }
    return seeds + tuple(sorted(images - set(seeds)))


def induced_action(
    carrier: tuple[tuple[int, ...], ...], frame: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Column data (target row, half-Laurent exponent) for an edge action."""
    index = {direction: slot for slot, direction in enumerate(carrier)}
    result = []
    for direction in carrier:
        image = matvec(frame, direction)
        canonical, offset = canonical_edge(image)
        if canonical not in index:
            raise ValueError("carrier is not closed")
        exponent = tuple(2 * value for value in direction) if offset != ZERO else ZERO
        result.append((index[canonical], exponent))
    return tuple(result)


def compose_actions(
    first: tuple[tuple[int, tuple[int, ...]], ...],
    second: tuple[tuple[int, tuple[int, ...]], ...],
    second_frame: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Return first(F_second q) second(q), with actions stored by columns."""
    pullback = transpose(second_frame)
    result = []
    for column, (middle, exponent_second) in enumerate(second):
        target, exponent_first = first[middle]
        exponent = add_exp(matvec(pullback, exponent_first), exponent_second)
        result.append((target, exponent))
    return tuple(result)


@cache
def orbit_facts() -> dict[str, object]:
    reflected = tuple(canonical_edge(matvec(TIME_REFLECTION, direction))[0] for direction in DIRS15)
    dirs22 = DIRS15 + tuple(sorted(set(reflected) - set(DIRS15)))
    dirs40 = carrier_orbit(DIRS15, FRAMES)
    shared = set(DIRS15) & set(reflected)
    rotation_closed_15 = all(
        all(canonical_edge(matvec(frame, direction))[0] in DIRS15 for direction in DIRS15)
        for frame in FRAMES
    )
    group_ok = True
    frame_set = set(FRAMES)
    for left in FRAMES:
        for right in FRAMES:
            combined = matmul(left, right)
            if combined not in frame_set:
                group_ok = False
                break
            if compose_actions(induced_action(dirs40, left), induced_action(dirs40, right), right) != induced_action(dirs40, combined):
                group_ok = False
                break
        if not group_ok:
            break
    reflection_involution = compose_actions(
        induced_action(dirs22, TIME_REFLECTION),
        induced_action(dirs22, TIME_REFLECTION),
        TIME_REFLECTION,
    ) == tuple((slot, ZERO) for slot in range(len(dirs22)))
    return {
        "dirs22": dirs22,
        "dirs40": dirs40,
        "shared22": len(shared),
        "rotation_closed_15": rotation_closed_15,
        "group_ok": group_ok,
        "reflection_involution": reflection_involution,
        "anchor_nontrivial": any(exponent != ZERO for _, exponent in induced_action(dirs22, TIME_REFLECTION)),
    }


def raw_gamma_terms() -> dict[tuple[int, int], tuple[tuple[tuple[int, ...], sp.Expr], ...]]:
    terms: dict[tuple[int, int], tuple[tuple[tuple[int, ...], sp.Expr], ...]] = {}
    for tensor_slot, (left, right) in enumerate(PAIRS):
        if left == right:
            terms[tensor_slot, left] = ((ZERO, sp.Integer(2)), (unit(left, -1), sp.Integer(-2)))
        else:
            terms[tensor_slot, left] = ((unit(right), SQRT2), (ZERO, -SQRT2))
            terms[tensor_slot, right] = ((unit(left), SQRT2), (ZERO, -SQRT2))
    return terms


GAMMA_TERMS = raw_gamma_terms()


@cache
def row_system(direction: tuple[int, ...]) -> tuple[sp.Matrix, sp.Matrix, tuple[tuple[int, tuple[int, ...]], ...]]:
    support = tuple(product(*(((0, 1) if value else (0,)) for value in direction)))
    unknowns = tuple((tensor_slot, shift) for tensor_slot in range(10) for shift in support)
    columns: list[dict[tuple[int, tuple[int, ...]], sp.Expr]] = []
    equation_keys: set[tuple[int, tuple[int, ...]]] = set()
    for tensor_slot, shift in unknowns:
        column: dict[tuple[int, tuple[int, ...]], sp.Expr] = {}
        for gauge_slot in range(4):
            for exponent, coefficient in GAMMA_TERMS.get((tensor_slot, gauge_slot), ()):
                key = gauge_slot, add_exp(shift, exponent)
                column[key] = sp.expand(column.get(key, 0) + coefficient)
                equation_keys.add(key)
        columns.append(column)
    targets: list[dict[tuple[int, tuple[int, ...]], sp.Expr]] = []
    length = sp.sqrt(sum(value * value for value in direction))
    for grade in range(4):
        target: dict[tuple[int, tuple[int, ...]], sp.Expr] = {}
        if direction[grade]:
            target[grade, ZERO] = -sp.Integer(1) / length
            target[grade, direction] = sp.Integer(1) / length
        targets.append(target)
        equation_keys.update(target)
    ordered_keys = tuple(sorted(equation_keys))
    key_index = {key: slot for slot, key in enumerate(ordered_keys)}
    matrix = sp.MutableSparseMatrix(len(ordered_keys), len(unknowns), {})
    for column_slot, column in enumerate(columns):
        for key, coefficient in column.items():
            matrix[key_index[key], column_slot] = coefficient
    rhs = sp.MutableSparseMatrix(len(ordered_keys), 4, {})
    for grade, target in enumerate(targets):
        for key, coefficient in target.items():
            rhs[key_index[key], grade] = coefficient
    return sp.Matrix(matrix), sp.Matrix(rhs), unknowns


def s3_constraints(
    support: tuple[tuple[int, ...], ...], unknowns: tuple[tuple[int, tuple[int, ...]], ...]
) -> sp.Matrix:
    unknown_index = {unknown: slot for slot, unknown in enumerate(unknowns)}
    rows: list[dict[int, int]] = []
    for spatial in permutations(range(3)):
        permutation = tuple(spatial) + (3,)
        inverse = tuple(permutation.index(old) for old in range(4))
        tensor_map = {
            old_slot: PAIR_INDEX[tuple(sorted((inverse[left], inverse[right])))]
            for old_slot, (left, right) in enumerate(PAIRS)
        }
        for old_slot in range(10):
            new_slot = tensor_map[old_slot]
            for output_shift in support:
                input_shift = tuple(output_shift[permutation[row]] for row in range(4))
                row: dict[int, int] = {}
                for index, coefficient in (
                    (unknown_index[new_slot, input_shift], 1),
                    (unknown_index[old_slot, output_shift], -1),
                ):
                    row[index] = row.get(index, 0) + coefficient
                row = {index: value for index, value in row.items() if value}
                if row:
                    rows.append(row)
    matrix = sp.MutableSparseMatrix(len(rows), len(unknowns), {})
    for row_slot, row in enumerate(rows):
        for column_slot, coefficient in row.items():
            matrix[row_slot, column_slot] = coefficient
    return sp.Matrix(matrix)


@cache
def raw_prefilter_facts() -> dict[str, object]:
    ranks = []
    augmented_ranks = []
    solutions: dict[tuple[int, ...], tuple[tuple[tuple[int, ...], ...], sp.Matrix]] = {}
    free_values: tuple[sp.Expr, ...] = ()
    for direction in DIRS15:
        matrix, grade_rhs, unknowns = row_system(direction)
        rhs = grade_rhs * sp.ones(4, 1)
        rank = matrix.rank()
        ranks.append(rank)
        augmented_ranks.append(matrix.row_join(rhs).rank())
        support = tuple(dict.fromkeys(shift for _, shift in unknowns))
        if direction == (1, 1, 1, 1):
            _, pivots = matrix.rref()
            free_columns = tuple(slot for slot in range(matrix.cols) if slot not in pivots)
            covariance = s3_constraints(support, unknowns)
            solved_matrix = matrix.col_join(covariance)
            solved_rhs = rhs.col_join(sp.zeros(covariance.rows, 1))
            solution, parameters = solved_matrix.gauss_jordan_solve(solved_rhs)
            if parameters.rows:
                raise AssertionError("S3 did not fix the known two-parameter family")
            free_values = tuple(sp.simplify(solution[slot]) for slot in free_columns)
        else:
            solution, parameters = matrix.gauss_jordan_solve(rhs)
            if parameters.rows:
                raise AssertionError("unexpected prefilter freedom")
        coefficient_matrix = sp.zeros(10, len(support))
        support_index = {shift: slot for slot, shift in enumerate(support)}
        for slot, (tensor_slot, shift) in enumerate(unknowns):
            coefficient_matrix[tensor_slot, support_index[shift]] = solution[slot]
        solutions[direction] = support, coefficient_matrix

    def evaluate(values: tuple[sp.Expr, ...]) -> sp.Matrix:
        result = sp.zeros(15, 10)
        for row, direction in enumerate(DIRS15):
            support, coefficients = solutions[direction]
            phases = sp.Matrix([
                sp.prod(values[axis] ** shift[axis] for axis in range(4))
                for shift in support
            ])
            for column in range(10):
                result[row, column] = sp.expand((coefficients.row(column) * phases)[0])
        return result

    d1 = evaluate((I, 1, 1, 1))
    h1 = evaluate(((1 + I * SQRT3) / 2, I, 1, 1))
    minor_d1 = sp.simplify(d1[list(COMMON_MINOR_ROWS), :].det())
    minor_h1 = sp.simplify(h1[list(COMMON_MINOR_ROWS), :].det())
    return {
        "unknowns": sum(row_system(direction)[0].cols for direction in DIRS15),
        "rank": sum(ranks),
        "augmented_rank": sum(augmented_ranks),
        "free_values": free_values,
        "minor_d1": minor_d1,
        "minor_h1": minor_h1,
        "rank_d1": d1.rank(),
        "rank_h1": h1.rank(),
    }


def signed_axis_data(frame: tuple[tuple[int, ...], ...], old_axis: int) -> tuple[int, int]:
    for new_axis in range(4):
        if frame[new_axis][old_axis]:
            return new_axis, frame[new_axis][old_axis]
    raise AssertionError("not a signed permutation")


def raw_vector_at_fixed_point(
    frame: tuple[tuple[int, ...], ...], z_values: tuple[sp.Expr, ...]
) -> sp.Matrix:
    result = sp.zeros(4)
    for old_axis in range(4):
        new_axis, sign = signed_axis_data(frame, old_axis)
        factor = sp.Integer(1) if sign == 1 else -1 / z_values[old_axis]
        result[new_axis, old_axis] = sp.simplify(sign * (-factor if sign == -1 else factor))
    return result


@cache
def placement_facts() -> dict[str, object]:
    # For a negative signed axis, V(Fq) F V(q)^dagger contributes
    # -u_old^2=-z_old^-1; at the relevant Nyquist fixed point it is +1.
    time_point = (sp.Integer(1), sp.Integer(1), sp.Integer(1), sp.Integer(-1))
    half_point = (sp.Integer(-1), sp.Integer(-1), sp.Integer(1), sp.Integer(1))
    time_raw = raw_vector_at_fixed_point(TIME_REFLECTION, time_point)
    half_raw = raw_vector_at_fixed_point(SPATIAL_HALF_TURN, half_point)
    time_vertex = sp.Matrix(TIME_REFLECTION)
    half_vertex = sp.Matrix(SPATIAL_HALF_TURN)
    time_rank_bound = 4 - (time_vertex - time_raw).rank()
    half_rank_bound = 4 - (half_vertex - half_raw).rank()
    full_group = set(FRAMES)
    automorphism_ok = len(FRAMES) == 24 and all(
        matmul(left, right) in full_group for left in FRAMES for right in FRAMES
    ) and matmul(TIME_REFLECTION, TIME_REFLECTION) == IDENTITY4 and all(
        matmul(frame, TIME_REFLECTION) == matmul(TIME_REFLECTION, frame)
        for frame in FRAMES
    )
    # C(Fu) [V(Fu) F V(u)^dagger] = F C(u) is monomial-by-monomial:
    # signed old axis b -> new axis a has coefficient sign and exponent e_b.
    c_covariance = True
    for frame in FRAMES + (TIME_REFLECTION,):
        for old_axis in range(4):
            _new_axis, sign = signed_axis_data(frame, old_axis)
            transformed_c_exponent = tuple(sign * value for value in unit(old_axis))
            raw_vector_exponent = tuple((1 - sign) * value for value in unit(old_axis))
            left_exponent = add_exp(transformed_c_exponent, raw_vector_exponent)
            right_exponent = unit(old_axis)
            c_covariance = c_covariance and left_exponent == right_exponent
    unit_exponents = tuple(unit(axis) for axis in range(4))
    inverse_exponents = tuple(tuple(-value for value in exponent) for exponent in unit_exponents)
    c_is_unit = all(
        add_exp(exponent, inverse) == ZERO
        for exponent, inverse in zip(unit_exponents, inverse_exponents)
    )
    return {
        "time_raw": time_raw,
        "time_vertex": time_vertex,
        "time_rank_bound": time_rank_bound,
        "half_raw": half_raw,
        "half_vertex": half_vertex,
        "half_rank_bound": half_rank_bound,
        "automorphism_ok": automorphism_ok,
        "c_covariance": c_covariance,
        "c_is_unit": c_is_unit,
        "deck_count": len(tuple(product((-1, 1), repeat=4))),
    }


@cache
def target_ward_facts() -> dict[str, object]:
    rows = []
    total_unknowns = 0
    all_consistent = True
    grade_ranks = [0] * 4
    grade_has_inconsistency = [False] * 4
    rank_orbits: dict[tuple[int, bool], set[tuple[int, int, int, int]]] = {}
    for direction in DIRS15:
        matrix, rhs, _ = row_system(direction)
        rank = matrix.rank()
        total_unknowns += 4 * matrix.cols
        for grade in range(4):
            augmented = matrix.row_join(rhs[:, grade]).rank()
            consistent = augmented == rank
            all_consistent = all_consistent and consistent
            grade_ranks[grade] += rank
            grade_has_inconsistency[grade] |= not consistent
            rank_orbits.setdefault(
                (sum(direction), bool(direction[grade])), set()
            ).add((matrix.cols, matrix.rows, rank, augmented))
            rows.append((direction, grade, rank, augmented, consistent))
    witness = next(row for row in rows if row[0] == (1, 1, 0, 0) and row[1] == 0)
    inconsistent = tuple(row for row in rows if not row[4])
    grade_augmented_ranks = tuple(
        rank + int(has_inconsistency)
        for rank, has_inconsistency in zip(grade_ranks, grade_has_inconsistency)
    )
    expected_rank_orbits = {
        (1, False): {(20, 36, 20, 20)},
        (1, True): {(20, 36, 20, 20)},
        (2, False): {(40, 64, 40, 40)},
        (2, True): {(40, 64, 40, 41)},
        (3, False): {(80, 112, 80, 80)},
        (3, True): {(80, 112, 80, 81)},
        (4, True): {(160, 192, 158, 159)},
    }
    return {
        "unknowns": total_unknowns,
        "all_consistent": all_consistent,
        "inconsistent_count": len(inconsistent),
        "grade_ranks": tuple(grade_ranks),
        "grade_augmented_ranks": grade_augmented_ranks,
        "rank_orbits": rank_orbits,
        "expected_rank_orbits": expected_rank_orbits,
        "witness": witness,
        "analytic_corner": (
            "d=1100,g=0: z2=z3=1; column 0 at z0=1 forces "
            "M_01(1,z1)=1/2, while column 1 at z1=1 forces "
            "M_01(z0,1)=0, contradicting the shared corner (1,1)"
        ),
    }


def laurent_symbol(
    terms: tuple[tuple[tuple[int, ...], sp.Expr], ...],
    variables: tuple[sp.Symbol, ...],
) -> sp.Expr:
    return sp.expand(sum(
        coefficient * sp.prod(
            variables[axis] ** exponent[axis] for axis in range(4)
        )
        for exponent, coefficient in terms
    ))


@cache
def analytic_corner_facts() -> dict[str, object]:
    """Support-independent regular-Laurent contradiction for d=1100,g=0."""
    variables = sp.symbols("z0:4", nonzero=True)
    z0, z1, z2, z3 = variables
    direction = (1, 1, 0, 0)
    mixed_slot = PAIR_INDEX[(0, 1)]
    coupled_zero = tuple(
        tensor_slot for tensor_slot in range(10)
        if (tensor_slot, 0) in GAMMA_TERMS
    )
    coupled_one = tuple(
        tensor_slot for tensor_slot in range(10)
        if (tensor_slot, 1) in GAMMA_TERMS
    )
    substitutions_zero = {z0: 1, z2: 1, z3: 1}
    substitutions_one = {z1: 1, z2: 1, z3: 1}
    other_zero = tuple(
        sp.simplify(
            laurent_symbol(GAMMA_TERMS[tensor_slot, 0], variables).subs(
                substitutions_zero
            )
        )
        for tensor_slot in coupled_zero if tensor_slot != mixed_slot
    )
    other_one = tuple(
        sp.simplify(
            laurent_symbol(GAMMA_TERMS[tensor_slot, 1], variables).subs(
                substitutions_one
            )
        )
        for tensor_slot in coupled_one if tensor_slot != mixed_slot
    )
    mixed_zero = sp.simplify(
        laurent_symbol(GAMMA_TERMS[mixed_slot, 0], variables).subs(
            substitutions_zero
        )
    )
    mixed_one = sp.simplify(
        laurent_symbol(GAMMA_TERMS[mixed_slot, 1], variables).subs(
            substitutions_one
        )
    )
    regge_phase = sp.prod(variables[axis] ** direction[axis] for axis in range(4))
    target_zero = sp.simplify(((regge_phase - 1) / SQRT2).subs(substitutions_zero))
    target_one = sp.Integer(0)  # grade u_0 has no column-1 target
    branch_zero = sp.cancel(target_zero / mixed_zero)
    branch_one = sp.cancel(target_one / mixed_one)
    corner_zero = sp.limit(branch_zero, z1, 1)
    corner_one = sp.limit(branch_one, z0, 1)
    return {
        "other_zero_vanish": all(value == 0 for value in other_zero),
        "other_one_vanish": all(value == 0 for value in other_one),
        "branch_zero": branch_zero,
        "branch_one": branch_one,
        "corner_zero": corner_zero,
        "corner_one": corner_one,
        "contradiction": corner_zero != corner_one,
    }


def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    orbit = orbit_facts()
    prefilter = raw_prefilter_facts()
    placement = placement_facts()
    target = target_ward_facts()
    corner = analytic_corner_facts()
    claims = {
        "component_order": D4_TO_REGGE,
        "anchor": True,
        "carrier15_full": False,
        "raw_signs": True,
        "single_rank4": False,
        "temporal_rank4": False,
        "half_inversion": True,
        "sheet_species": False,
        "c_identity": False,
        "support": "four_singletons",
        "fit_shared": False,
        "group_composition": True,
        "nyquist_included": True,
        "accept_pseudoinverse": False,
        "action_open": False,
        "response_open": False,
        "broad_no_go": False,
    }
    if mutation == "wrong_component_order":
        claims["component_order"] = tuple(range(10))
    elif mutation == "erase_reversal_anchor":
        claims["anchor"] = False
    elif mutation == "claim_15_full_covariance":
        claims["carrier15_full"] = True
    elif mutation == "flip_raw_laurent_sign":
        claims["raw_signs"] = False
    elif mutation == "claim_single_cover_rank_four":
        claims["single_rank4"] = True
    elif mutation == "claim_temporal_cover_rank_four":
        claims["temporal_rank4"] = True
    elif mutation == "wrong_half_variable_inversion":
        claims["half_inversion"] = False
    elif mutation == "treat_sheets_as_species":
        claims["sheet_species"] = True
    elif mutation == "replace_c_with_identity":
        claims["c_identity"] = True
    elif mutation == "use_invalid_one_coset":
        claims["support"] = "one_coset"
    elif mutation == "fit_shared_rows":
        claims["fit_shared"] = True
    elif mutation == "omit_group_composition":
        claims["group_composition"] = False
    elif mutation == "omit_nyquist":
        claims["nyquist_included"] = False
    elif mutation == "accept_pseudoinverse":
        claims["accept_pseudoinverse"] = True
    elif mutation == "open_action_early":
        claims["action_open"] = True
    elif mutation == "open_response_early":
        claims["response_open"] = True
    elif mutation == "claim_broad_no_go":
        claims["broad_no_go"] = True

    target_failed = not target["all_consistent"]
    return {
        "A": (
            authority["main"] == CURRENT_MAIN and authority["parent"]
            and authority["prereg"] and authority["inputs"],
            "authority, preregistration, and literal source inputs are pinned",
        ),
        "K0": (
            len(FRAMES) == 24 and len(DIRS15) == 15
            and len(orbit["dirs22"]) == 22 and len(orbit["dirs40"]) == 40
            and orbit["shared22"] == 8 and set(orbit["dirs22"]) <= set(orbit["dirs40"])
            and not orbit["rotation_closed_15"]
            and orbit["reflection_involution"] and orbit["group_ok"]
            and orbit["anchor_nontrivial"] == claims["anchor"]
            and claims["carrier15_full"] is False,
            "the exact Regge carriers have sizes 15/22/40 with anchor phases and all frame laws",
        ),
        "K1": (
            claims["component_order"] == D4_TO_REGGE and claims["raw_signs"]
            and prefilter["unknowns"] == 800
            and prefilter["rank"] == prefilter["augmented_rank"] == 798
            and prefilter["free_values"] == (SQRT2 / 12, SQRT2 / 12)
            and prefilter["rank_d1"] == prefilter["rank_h1"] == 10
            and prefilter["minor_d1"] == I / 1024
            and prefilter["minor_h1"] == -(SQRT3 - I) / 2048,
            "the known raw-identity 800-variable Ward/S3 prefilter and exact common minor reproduce",
        ),
        "K2": (
            placement["time_raw"] == sp.eye(4)
            and placement["time_vertex"] == sp.diag(1, 1, 1, -1)
            and placement["time_rank_bound"] == 3
            and claims["single_rank4"] is False,
            "single-cover time-reflection equivariance has rank at most three at temporal Nyquist",
        ),
        "K3": (
            placement["half_raw"] == sp.eye(4)
            and placement["half_vertex"] == sp.diag(-1, -1, 1, 1)
            and placement["half_rank_bound"] == 2
            and claims["temporal_rank4"] is False,
            "a temporal-only cover has rank at most two at the frozen spatial half-turn point",
        ),
        "T1": (
            placement["automorphism_ok"] and placement["c_covariance"]
            and placement["c_is_unit"] and placement["deck_count"] == 16
            and claims["half_inversion"] and claims["sheet_species"] is False
            and claims["c_identity"] is False,
            "the frozen full four-axis placement grading and C=diag(u_mu) close exactly",
        ),
        "T2": (
            target["unknowns"] == 3200 and target_failed
            and target["inconsistent_count"] == 28
            and target["grade_ranks"] == (798, 798, 798, 798)
            and target["grade_augmented_ranks"] == (799, 799, 799, 799)
            and target["rank_orbits"] == target["expected_rank_orbits"]
            and target["witness"][2:4] == (40, 41)
            and corner["other_zero_vanish"] and corner["other_one_vanish"]
            and corner["branch_zero"] == sp.Rational(1, 2)
            and corner["branch_one"] == 0
            and corner["corner_zero"] == sp.Rational(1, 2)
            and corner["corner_one"] == 0 and corner["contradiction"]
            and claims["support"] == "four_singletons"
            and claims["accept_pseudoinverse"] is False,
            "the frozen placement-aware Ward target is exactly inconsistent before any induction",
        ),
        "T3": (
            target_failed and claims["fit_shared"] is False,
            "22-edge target gluing is sealed, not fitted or executed, after the T2 obstruction",
        ),
        "T4": (
            target_failed and claims["group_composition"],
            "40-edge target induction is sealed after T2; only carrier group laws were executed",
        ),
        "T5": (
            target_failed and claims["nyquist_included"],
            "the 4096-point target rank census is sealed after T2, including all Nyquist strata",
        ),
        "S": (
            target_failed and claims["action_open"] is False
            and claims["response_open"] is False and claims["broad_no_go"] is False,
            "action, Riesz, source, response, held-outs, and broad no-go claims remain sealed",
        ),
    }


N5_LINES = (
    "per_element: checked the frozen d=1100, grade-g=0 necessary Ward coefficient block; exact rank is 40 and augmented rank is 41.",
    "per_site: checked and not executed -- no centered-symbol, changed-placement, quotient, or independently derived alternative site stencil is constructed.",
    "per_mode: checked and not executed -- the obstruction is coefficientwise; no rational/nonlocal class or complete 4096-point torus census is executed.",
    "per_block: checked only the frozen raw-symbol regular-Laurent chain equation; 22/40 gluing, action quotient, Riesz selection, and response stop downstream.",
    "lattice_wide: checked and not executed -- no universal Regge-D4 bridge, OS/GNS/CAR reconstruction, process tensor, gravity law, or TOE closure is tested.",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 96 else statement[:93] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0
    install_resource_caps()
    started = time.monotonic()
    checks = Checks()
    try:
        results = evaluate(args.mutation)
    except (MemoryError, ResourceCap) as error:
        print(f"[FAIL] RESOURCE: UNEXECUTED under frozen cap ({error})")
        print("per_element: checked and not executed — the exact coefficient run hit the frozen resource cap.")
        print("per_site: checked and not executed — no site assembly is permitted after a resource-cap stop.")
        print("per_mode: checked and not executed — no mode evaluation is permitted after a resource-cap stop.")
        print("per_block: checked and not executed — the carrier-chain target remains operationally unexecuted.")
        print("lattice_wide: checked and not executed — action, Riesz, source, response, and held-outs stay sealed.")
        print("TOTAL: PASS=0 FAIL=1")
        return 1
    finally:
        signal.alarm(0)
    for key, (condition, statement) in results.items():
        checks.check(key, statement, condition)
    witness = target_ward_facts()["witness"]
    print(
        "WITNESS: d=1100 grade=0 "
        f"rank={witness[2]} augmented_rank={witness[3]}; "
        f"elapsed={time.monotonic() - started:.2f}s"
    )
    corner = analytic_corner_facts()
    print(
        "CORNER: regular-Laurent M_01 has "
        f"M_01(1,z1)={corner['branch_zero']} and "
        f"M_01(z0,1)={corner['branch_one']}; shared-corner limits "
        f"{corner['corner_zero']} != {corner['corner_one']}"
    )
    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
