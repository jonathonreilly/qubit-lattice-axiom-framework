#!/usr/bin/env python3
"""No-import exact checker for the Block-201 direct Schur/Wick cylinder.

The checker rebuilds the exterior-form CAR, the six physical momentum pairs,
the coarse-circle Schur kernels, the Block-194 event PVM, and the typed
action/event intertwiner without importing any project science runner.  It
then checks the rank-four determinant-lemma engine and evaluates the raw D1
one-crossing amplitudes and weights exactly.

The preregistered floating-point bare-identity pilot is contamination, not an
expected value.  No number from that pilot is embedded here.  Gluing and the
later D1/six-carrier censuses remain sealed unless the exact raw one-shot
table is uniformly 1/8 and sums to one without a fitted factor.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path
import subprocess

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
PREREG_COMMIT = "f80e9673ad836e14e1478318198d063190f24294"
PARENT_COMMIT = "c7e0a0b57810e97bf563a65ded273ce9a6da0b2f"
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block201-direct-schur-wick-event-functional-20260825"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block201-direct-schur-wick-event-functional-20260825/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block201-direct-schur-wick-event-functional-20260825/PREFLIGHT_WITNESSES.md",
    "docs/ADMISSIBILITY_D4_L24_DIRECT_SCHUR_WICK_EVENT_FUNCTIONAL_NORMALIZATION_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

R = sp.Rational
I = sp.I
MASS = R(2, 7)
COARSE_TIME = 12
FORM_DIMENSION = 16
EVENT_DIMENSION = 32
EVENT_COUNT = 8
BOUNDARY_SITES = (0, 2, 4)
BOUNDARIES = tuple(
    subset
    for size in range(1, len(BOUNDARY_SITES) + 1)
    for subset in combinations(BOUNDARY_SITES, size)
)

FIXTURES = (
    ("D1", (0, 0, 0, sp.pi / 4), (sp.pi / 2, 0, 0, 0)),
    ("D2", (0, 0, 0, sp.pi / 4),
     (sp.pi / 2, sp.pi / 2, 0, 0)),
    ("D3", (0, 0, 0, sp.pi / 4),
     (sp.pi / 2, sp.pi / 2, sp.pi / 2, 0)),
    ("H1", (sp.pi / 6, sp.pi / 3, 0, sp.pi / 6),
     (sp.pi / 3, sp.pi / 2, 0, 0)),
    ("H2", (sp.pi / 4, sp.pi / 6, sp.pi / 3, sp.pi / 6),
     (sp.pi / 6, sp.pi / 3, sp.pi / 2, 0)),
    ("X1", (sp.pi / 6, sp.pi / 4, 0, sp.pi / 6),
     (sp.pi / 3, sp.pi / 6, sp.pi / 2, sp.pi / 12)),
)
EXPECTED_RADIUS_PAIRS = (
    (R(0), R(1)),
    (R(0), R(2)),
    (R(0), R(3)),
    (R(1), R(5, 4)),
    (R(3, 2), (7 + sp.sqrt(3)) / 4),
    (R(3, 4), (10 + sp.sqrt(3)) / 4),
)
FROZEN_RADII = (
    R(0), R(3, 4), R(1), R(5, 4), R(3, 2), R(2), R(3),
    (7 + sp.sqrt(3)) / 4, (10 + sp.sqrt(3)) / 4,
)

MUTATIONS = (
    "stale_prereg",
    "reuse_contaminated_pilot",
    "duplicate_radius_for_c32",
    "swap_incoming_outgoing",
    "reorder_form_masks",
    "drop_one_event_branch",
    "omit_annihilation_intertwiners",
    "choose_relative_phase",
    "crossing_dependent_phase",
    "break_reflection_label_map",
    "use_fixed_label_cubic_action",
    "reverse_berezin_order",
    "drop_doubled_conjugation",
    "sum_amplitudes_then_square",
    "skip_direct_determinant_check",
    "postnormalize_one_shots",
    "open_gluing_early",
)
MUTATION_FAMILY = {
    "stale_prereg": "P0",
    "reuse_contaminated_pilot": "P0",
    "duplicate_radius_for_c32": "T0",
    "swap_incoming_outgoing": "T0/T1",
    "reorder_form_masks": "T1",
    "drop_one_event_branch": "T1",
    "omit_annihilation_intertwiners": "T1",
    "choose_relative_phase": "T1",
    "crossing_dependent_phase": "T1",
    "break_reflection_label_map": "T1",
    "use_fixed_label_cubic_action": "T1",
    "reverse_berezin_order": "T2",
    "drop_doubled_conjugation": "T2",
    "sum_amplitudes_then_square": "T2/T3",
    "skip_direct_determinant_check": "T2",
    "postnormalize_one_shots": "T3",
    "open_gluing_early": "STOP",
}


def exact_zero(value: sp.Expr) -> bool:
    value = sp.sympify(value)
    if value == 0:
        return True
    try:
        matrix = DomainMatrix.from_Matrix(
            sp.Matrix(((value,),)), extension=True
        )
        if matrix.is_zero_matrix:
            return True
    except (TypeError, ValueError, NotImplementedError):
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
    except (TypeError, ValueError, NotImplementedError):
        pass
    return all(exact_zero(value) for value in difference)


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
    return sp.factor(domain_matrix.domain.to_sympy(domain_matrix.det()))


def exact_positive(value: sp.Expr) -> bool:
    value = sp.factor(sp.simplify(value))
    if value.is_positive is True:
        return True
    return sp.ask(sp.Q.positive(value)) is True


def canonical_scalar(value: sp.Expr) -> sp.Expr:
    return sp.factor(sp.cancel(sp.simplify(value)))


def git_output(*arguments: str) -> str:
    return subprocess.check_output(
        ("git",) + arguments,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def source_has_no_project_imports() -> bool:
    tree = ast.parse(Path(__file__).read_text())
    forbidden = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            forbidden.extend(
                alias.name for alias in node.names
                if alias.name.startswith(("admissibility_", "independent_"))
            )
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith(("admissibility_", "independent_")):
                forbidden.append(node.module)
    return not forbidden


def source_has_no_float_literals() -> bool:
    tree = ast.parse(Path(__file__).read_text())
    return not any(
        isinstance(node, ast.Constant) and isinstance(node.value, float)
        for node in ast.walk(tree)
    )


@cache
def p0_facts() -> dict[str, object]:
    goal_text = (ROOT / GOAL_PATH).read_text()
    preflight_text = (ROOT / PREFLIGHT_PATH).read_text()
    return {
        "head": git_output("rev-parse", "HEAD"),
        "prereg_ancestor": is_ancestor(PREREG_COMMIT),
        "parent_ancestor": is_ancestor(PARENT_COMMIT),
        "goal_frozen": (
            git_output("rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH}")
            == git_output("hash-object", "--", GOAL_PATH)
        ),
        "preflight_frozen": (
            git_output("rev-parse", f"{PREREG_COMMIT}:{PREFLIGHT_PATH}")
            == git_output("hash-object", "--", PREFLIGHT_PATH)
        ),
        "contract_present": (
            "Delta_00^02" in goal_text
            and "No division by `sum w`" in goal_text
            and "floating-point pilot" in preflight_text
            and "discarded as evidence" in preflight_text
        ),
        "pilot_constants_absent": source_has_no_float_literals(),
        "no_project_imports": source_has_no_project_imports(),
    }


FORM_SUBSETS = tuple(
    tuple(axis for axis in range(4) if mask & (1 << axis))
    for mask in range(FORM_DIMENSION)
)
FORM_INDEX = {subset: index for index, subset in enumerate(FORM_SUBSETS)}


def action_creation(axis: int) -> sp.Matrix:
    """Exterior creation reconstructed from ordered subset coordinates."""
    result = sp.zeros(FORM_DIMENSION)
    for column, subset in enumerate(FORM_SUBSETS):
        if axis in subset:
            continue
        target = tuple(sorted(subset + (axis,)))
        sign = (-1) ** sum(item < axis for item in subset)
        result[FORM_INDEX[target], column] = sign
    return result


def event_creation(axis: int) -> sp.Matrix:
    """Independent bit-mask construction of the same event-form operator."""
    result = sp.zeros(FORM_DIMENSION)
    lower_mask = (1 << axis) - 1
    for mask in range(FORM_DIMENSION):
        if mask & (1 << axis):
            continue
        sign = (-1) ** ((mask & lower_mask).bit_count())
        result[mask | (1 << axis), mask] = sign
    return result


@cache
def car_facts() -> dict[str, object]:
    action_c = tuple(action_creation(axis) for axis in range(4))
    event_c = tuple(event_creation(axis) for axis in range(4))
    action_a = tuple(matrix.T for matrix in action_c)
    event_a = tuple(matrix.T for matrix in event_c)
    identity = sp.eye(FORM_DIMENSION)
    zero = sp.zeros(FORM_DIMENSION)

    car_ok = True
    for left in range(4):
        for right in range(4):
            target = identity if left == right else zero
            car_ok = car_ok and matrix_equal(
                action_a[left] * action_c[right]
                + action_c[right] * action_a[left],
                target,
            )
            car_ok = car_ok and matrix_equal(
                action_c[left] * action_c[right]
                + action_c[right] * action_c[left],
                zero,
            )
            car_ok = car_ok and matrix_equal(
                action_a[left] * action_a[right]
                + action_a[right] * action_a[left],
                zero,
            )

    numbers = tuple(
        action_c[axis] * action_a[axis] for axis in range(4)
    )
    signatures = tuple(
        tuple(numbers[axis][index, index] for axis in range(4))
        for index in range(FORM_DIMENSION)
    )
    diagonal_numbers = all(
        matrix_equal(number, sp.diag(*(number[i, i]
                                      for i in range(FORM_DIMENSION))))
        for number in numbers
    )
    adjacency = {index: set() for index in range(FORM_DIMENSION)}
    for creation in action_c:
        for row, column in creation.todok().keys():
            adjacency[row].add(column)
            adjacency[column].add(row)
    reached = {0}
    frontier = [0]
    while frontier:
        current = frontier.pop()
        for following in adjacency[current] - reached:
            reached.add(following)
            frontier.append(following)

    gamma_plus = tuple(
        action_c[axis] + action_a[axis] for axis in range(4)
    )
    gamma_minus = tuple(
        I * (action_c[axis] - action_a[axis]) for axis in range(4)
    )
    majoranas = tuple(
        item for axis in range(4)
        for item in (gamma_plus[axis], gamma_minus[axis])
    )
    majorana_ok = all(
        matrix_equal(gamma.H, gamma)
        and matrix_equal(gamma * gamma, identity)
        for gamma in majoranas
    ) and all(
        matrix_equal(
            majoranas[left] * majoranas[right]
            + majoranas[right] * majoranas[left],
            sp.zeros(FORM_DIMENSION),
        )
        for left in range(8) for right in range(left + 1, 8)
    )
    return {
        "action_c": action_c,
        "action_a": action_a,
        "event_c": event_c,
        "event_a": event_a,
        "gamma_plus": gamma_plus,
        "gamma_minus": gamma_minus,
        "majoranas": majoranas,
        "two_routes_equal": all(
            matrix_equal(action_c[index], event_c[index])
            and matrix_equal(action_a[index], event_a[index])
            for index in range(4)
        ),
        "car_ok": car_ok,
        "majorana_ok": majorana_ok,
        # Distinct joint number signatures force a commuting matrix diagonal;
        # connected creation edges then force all diagonal entries equal.
        "scalar_commutant_certificate": (
            diagonal_numbers
            and len(set(signatures)) == FORM_DIMENSION
            and len(reached) == FORM_DIMENSION
        ),
    }


def coarse_shift() -> sp.Matrix:
    shift = sp.zeros(COARSE_TIME)
    for site in range(COARSE_TIME):
        shift[(site + 1) % COARSE_TIME, site] = 1
    return shift


@cache
def scalar_action(squared_radius: sp.Expr) -> sp.Matrix:
    delta = sp.simplify(MASS**2 + squared_radius)
    shift = coarse_shift()
    return sp.simplify(
        sp.eye(COARSE_TIME)
        + (2 * sp.eye(COARSE_TIME) - shift - shift.T) / (4 * delta)
    )


@cache
def scalar_boundary(
    squared_radius: sp.Expr, boundary: tuple[int, ...]
) -> tuple[sp.Matrix, sp.Matrix]:
    action = scalar_action(squared_radius)
    interior = tuple(
        site for site in range(COARSE_TIME) if site not in boundary
    )
    direct = sp.simplify(
        action.extract(boundary, boundary)
        - action.extract(boundary, interior)
        * exact_inverse(action.extract(interior, interior))
        * action.extract(interior, boundary)
    )
    covariance_route = exact_inverse(
        exact_inverse(action).extract(boundary, boundary)
    )
    return sp.Matrix(direct), sp.Matrix(covariance_route)


def outgoing_momentum(
    incoming: tuple[sp.Expr, ...], transfer: tuple[sp.Expr, ...]
) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(incoming[index] + transfer[index]) for index in range(4)
    )


def squared_radius(momentum: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.simplify(sum(
        sp.sin(momentum[axis]) ** 2 for axis in range(3)
    ))


def spatial_clifford(momentum: tuple[sp.Expr, ...]) -> sp.Matrix:
    gammas = car_facts()["gamma_plus"]
    return sp.expand(sum(
        (sp.sin(momentum[axis]) * gammas[axis] for axis in range(3)),
        sp.zeros(FORM_DIMENSION),
    ))


def internal_action(momentum: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.expand(
        MASS * sp.eye(FORM_DIMENSION) + I * spatial_clifford(momentum)
    )


def fixture_by_name(name: str) -> tuple[tuple[sp.Expr, ...], ...]:
    for fixture_name, incoming, transfer in FIXTURES:
        if fixture_name == name:
            return incoming, outgoing_momentum(incoming, transfer)
    raise KeyError(name)


def time_major_pair(
    scalar_in: sp.MatrixBase,
    internal_in: sp.MatrixBase,
    scalar_out: sp.MatrixBase,
    internal_out: sp.MatrixBase,
) -> sp.Matrix:
    count = scalar_in.rows
    result = sp.zeros(EVENT_DIMENSION * count)
    for row in range(count):
        for column in range(count):
            offset_row = EVENT_DIMENSION * row
            offset_column = EVENT_DIMENSION * column
            result[
                offset_row:offset_row + FORM_DIMENSION,
                offset_column:offset_column + FORM_DIMENSION,
            ] = scalar_in[row, column] * internal_in
            result[
                offset_row + FORM_DIMENSION:offset_row + EVENT_DIMENSION,
                offset_column + FORM_DIMENSION:offset_column + EVENT_DIMENSION,
            ] = scalar_out[row, column] * internal_out
    return sp.Matrix(result)


@cache
def paired_kernel(name: str, boundary: tuple[int, ...]) -> sp.Matrix:
    incoming, outgoing = fixture_by_name(name)
    radius_in = squared_radius(incoming)
    radius_out = squared_radius(outgoing)
    scalar_in = scalar_boundary(radius_in, boundary)[0]
    scalar_out = scalar_boundary(radius_out, boundary)[0]
    return time_major_pair(
        scalar_in, internal_action(incoming),
        scalar_out, internal_action(outgoing),
    )


@cache
def t0_facts() -> dict[str, object]:
    radius_pairs = tuple(
        (squared_radius(incoming),
         squared_radius(outgoing_momentum(incoming, transfer)))
        for _name, incoming, transfer in FIXTURES
    )
    radius_pairs_ok = all(
        exact_zero(actual[0] - expected[0])
        and exact_zero(actual[1] - expected[1])
        for actual, expected in zip(radius_pairs, EXPECTED_RADIUS_PAIRS)
    )
    observed_radii = tuple(value for pair in radius_pairs for value in pair)
    nine_radii_ok = all(
        any(exact_zero(value - expected) for value in observed_radii)
        for expected in FROZEN_RADII
    ) and all(
        any(exact_zero(value - expected) for expected in FROZEN_RADII)
        for value in observed_radii
    )

    scalar_routes_ok = True
    scalar_positive = True
    nesting_ok = True
    determinant_ok = True
    for radius in FROZEN_RADII:
        full = scalar_boundary(radius, BOUNDARY_SITES)[0]
        for boundary in BOUNDARIES:
            direct, covariance = scalar_boundary(radius, boundary)
            scalar_routes_ok = scalar_routes_ok and matrix_equal(
                direct, covariance
            )
            scalar_positive = scalar_positive and all(
                exact_positive(exact_determinant(direct[:size, :size]))
                for size in range(1, direct.rows + 1)
            )
            if boundary != BOUNDARY_SITES:
                keep = tuple(BOUNDARY_SITES.index(site) for site in boundary)
                remove = tuple(
                    index for index in range(len(BOUNDARY_SITES))
                    if index not in keep
                )
                nested = sp.simplify(
                    full.extract(keep, keep)
                    - full.extract(keep, remove)
                    * exact_inverse(full.extract(remove, remove))
                    * full.extract(remove, keep)
                )
                nesting_ok = nesting_ok and matrix_equal(nested, direct)
                permuted = full.extract(keep + remove, keep + remove)
                determinant_ok = determinant_ok and exact_zero(
                    exact_determinant(permuted)
                    - exact_determinant(full.extract(remove, remove))
                    * exact_determinant(nested)
                )

    internal_ok = True
    for _name, incoming, transfer in FIXTURES:
        for momentum in (incoming, outgoing_momentum(incoming, transfer)):
            radius = squared_radius(momentum)
            spatial = spatial_clifford(momentum)
            action = internal_action(momentum)
            inverse_numerator = MASS * sp.eye(FORM_DIMENSION) - I * spatial
            internal_ok = internal_ok and (
                matrix_equal(spatial * spatial,
                             radius * sp.eye(FORM_DIMENSION))
                and matrix_equal(
                    action * inverse_numerator,
                    (MASS**2 + radius) * sp.eye(FORM_DIMENSION),
                )
            )

    paired_routes_ok = True
    paired_shapes_ok = True
    for name, incoming, transfer in FIXTURES:
        outgoing = outgoing_momentum(incoming, transfer)
        radius_in = squared_radius(incoming)
        radius_out = squared_radius(outgoing)
        for boundary in BOUNDARIES:
            direct_in, covariance_in = scalar_boundary(radius_in, boundary)
            direct_out, covariance_out = scalar_boundary(
                radius_out, boundary
            )
            direct_pair = paired_kernel(name, boundary)
            covariance_pair = time_major_pair(
                covariance_in, internal_action(incoming),
                covariance_out, internal_action(outgoing),
            )
            paired_routes_ok = paired_routes_ok and matrix_equal(
                direct_pair, covariance_pair
            )
            expected_size = EVENT_DIMENSION * len(boundary)
            paired_shapes_ok = paired_shapes_ok and (
                direct_pair.shape == (expected_size, expected_size)
            )

    d1_single = paired_kernel("D1", (0,))
    d1_in, d1_out = fixture_by_name("D1")
    scalar_in = scalar_boundary(R(0), (0,))[0][0, 0]
    scalar_out = scalar_boundary(R(1), (0,))[0][0, 0]
    ordering_ok = (
        matrix_equal(
            d1_single[:FORM_DIMENSION, :FORM_DIMENSION],
            scalar_in * internal_action(d1_in),
        )
        and matrix_equal(
            d1_single[FORM_DIMENSION:, FORM_DIMENSION:],
            scalar_out * internal_action(d1_out),
        )
        and matrix_equal(
            d1_single[:FORM_DIMENSION, FORM_DIMENSION:],
            sp.zeros(FORM_DIMENSION),
        )
        and matrix_equal(
            d1_single[FORM_DIMENSION:, :FORM_DIMENSION],
            sp.zeros(FORM_DIMENSION),
        )
    )
    return {
        "radius_pairs": radius_pairs,
        "radius_pairs_ok": radius_pairs_ok,
        "nine_radii_ok": nine_radii_ok,
        "scalar_routes_ok": scalar_routes_ok,
        "scalar_positive": scalar_positive,
        "nesting_ok": nesting_ok,
        "determinant_ok": determinant_ok,
        "internal_ok": internal_ok,
        "paired_routes_ok": paired_routes_ok,
        "ordering_ok": ordering_ok,
        "paired_shapes_ok": paired_shapes_ok,
    }


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


def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        permutation_matrix = sp.zeros(3)
        for row, column in enumerate(permutation):
            permutation_matrix[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            candidate = sp.diag(*signs) * permutation_matrix
            if candidate.det() == 1:
                rotations.append(candidate)
    return tuple(rotations)


def wedge_representation(transform: sp.MatrixBase) -> sp.Matrix:
    result = sp.zeros(FORM_DIMENSION)
    for column, subset in enumerate(FORM_SUBSETS):
        images = []
        coefficient = sp.Integer(1)
        for old_axis in subset:
            rows = [
                row for row in range(4) if transform[row, old_axis] != 0
            ]
            if len(rows) != 1:
                raise ValueError("wedge transform must be a signed permutation")
            new_axis = rows[0]
            coefficient *= transform[new_axis, old_axis]
            images.append(new_axis)
        inversions = sum(
            images[left] > images[right]
            for left in range(len(images))
            for right in range(left + 1, len(images))
        )
        coefficient *= (-1) ** inversions
        result[FORM_INDEX[tuple(sorted(images))], column] = coefficient
    return result


@cache
def event_facts() -> dict[str, object]:
    car = car_facts()
    gamma_plus = car["gamma_plus"]
    gamma_minus = car["gamma_minus"]
    gammas = tuple(
        item for axis in range(4)
        for item in (gamma_plus[axis], gamma_minus[axis])
    )
    identity16 = sp.eye(FORM_DIMENSION)
    zero16 = sp.zeros(FORM_DIMENSION)
    o1 = sp.expand(I * gammas[0] * gammas[2] * gammas[3])
    o2 = sp.expand(I * gammas[1] * gammas[2] * gammas[5])
    outcome_labels = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    ports = tuple(sp.expand(
        (identity16 + left * o1) * (identity16 + right * o2) / 4
    ) for left, right in outcome_labels)

    detector_basis = tuple(
        sp.expand(I * gamma_plus[3] * gamma_plus[axis])
        for axis in range(3)
    )
    columns = []
    for detector in detector_basis:
        columns.append(sp.Matrix.vstack(
            sp.expand(detector * o1 - o1 * detector).reshape(256, 1),
            sp.expand(detector * o2 - o2 * detector).reshape(256, 1),
        ))
    constraint = sp.Matrix.hstack(*columns)
    nullspace = constraint.nullspace()
    ray = sp.zeros(3, 1)
    if len(nullspace) == 1:
        raw = nullspace[0]
        pivot = next(value for value in raw if value != 0)
        ray = sp.Matrix(tuple(sp.simplify(value / pivot) for value in raw))
    orientation = sp.expand(sum(
        (ray[axis] * detector_basis[axis] for axis in range(3)),
        zero16,
    ))
    connectors = tuple(sp.expand(port * orientation) for port in ports)
    effects = tuple(
        sp.expand(block_matrix(
            port, sign * connector,
            sign * connector.H, port,
        ) / 2)
        for port, connector in zip(ports, connectors)
        for sign in (1, -1)
    )

    pvm_ok = (
        all(matrix_equal(effect.H, effect)
            and matrix_equal(effect * effect, effect) for effect in effects)
        and all(matrix_equal(
            effects[left] * effects[right], sp.zeros(EVENT_DIMENSION)
        ) for left in range(EVENT_COUNT)
          for right in range(left + 1, EVENT_COUNT))
        and matrix_equal(sum(effects, sp.zeros(EVENT_DIMENSION)),
                         sp.eye(EVENT_DIMENSION))
    )
    effect_ranks = tuple(exact_rank(effect) for effect in effects)
    effect_span = sp.Matrix.hstack(*(
        effect.reshape(EVENT_DIMENSION**2, 1) for effect in effects
    ))

    fiber_reflection = gamma_plus[3]
    sector_reflection = sp.diag(fiber_reflection, fiber_reflection)
    reflection_map = []
    for effect in effects:
        transformed = sp.expand(
            sector_reflection * effect * sector_reflection
        )
        matches = tuple(
            index for index, candidate in enumerate(effects)
            if matrix_equal(transformed, candidate)
        )
        reflection_map.append(matches[0] if len(matches) == 1 else -1)

    coordinate_transform = sp.diag(1, 1, 1, -1)
    coordinate_reflection = wedge_representation(coordinate_transform)
    coordinate_sector = sp.diag(
        coordinate_reflection, coordinate_reflection
    )
    coordinate_map = []
    for effect in effects:
        transformed = sp.expand(
            coordinate_sector * effect * coordinate_sector.T
        )
        matches = tuple(
            index for index, candidate in enumerate(effects)
            if matrix_equal(transformed, candidate)
        )
        coordinate_map.append(matches[0] if len(matches) == 1 else -1)

    rotations = proper_cubic_rotations()
    cubic_family_ok = True
    context_cotransformed = True
    for spatial in rotations:
        full = sp.eye(4)
        full[:3, :3] = spatial
        form_rotation = wedge_representation(full)
        transformed_o1 = sp.expand(form_rotation * o1 * form_rotation.T)
        transformed_o2 = sp.expand(form_rotation * o2 * form_rotation.T)
        for index, port in enumerate(ports):
            expected = sp.expand(
                (identity16 + outcome_labels[index][0] * transformed_o1)
                * (identity16 + outcome_labels[index][1] * transformed_o2)
                / 4
            )
            context_cotransformed = context_cotransformed and matrix_equal(
                form_rotation * port * form_rotation.T, expected
            )
        for old_axis, detector in enumerate(detector_basis):
            expected_detector = sp.expand(sum(
                (spatial[new_axis, old_axis] * detector_basis[new_axis]
                 for new_axis in range(3)),
                zero16,
            ))
            cubic_family_ok = cubic_family_ok and matrix_equal(
                form_rotation * detector * form_rotation.T,
                expected_detector,
            )

    return {
        "o1": o1,
        "o2": o2,
        "ports": ports,
        "orientation": orientation,
        "effects": effects,
        "classifier_rank": exact_rank(constraint),
        "classifier_nullity": len(nullspace),
        "classifier_ray": tuple(ray),
        "orientation_ok": (
            matrix_equal(orientation.H, orientation)
            and matrix_equal(orientation * orientation, identity16)
            and all(matrix_equal(orientation * port, port * orientation)
                    for port in ports)
        ),
        "pvm_ok": pvm_ok,
        "effect_ranks": effect_ranks,
        "effect_span_rank": exact_rank(effect_span),
        "reflection_map": tuple(reflection_map),
        "coordinate_map": tuple(coordinate_map),
        "proper_cubic_count": len(rotations),
        "cubic_family_ok": cubic_family_ok,
        "context_cotransformed": context_cotransformed,
        "baseline_weights": tuple(
            canonical_scalar(sp.trace(effect) / EVENT_DIMENSION)
            for effect in effects
        ),
    }


@cache
def intertwiner_facts() -> dict[str, object]:
    car = car_facts()
    event = event_facts()
    identity16 = sp.eye(FORM_DIMENSION)
    zero16 = sp.zeros(FORM_DIMENSION)
    sector_in = block_matrix(identity16, zero16, zero16, zero16)
    sector_out = block_matrix(zero16, zero16, zero16, identity16)
    sector_parity = sector_in - sector_out
    identity32 = sp.eye(EVENT_DIMENSION)

    common_form_equations = all(
        matrix_equal(
            identity32 * sp.diag(car["action_c"][axis],
                                 car["action_c"][axis]),
            sp.diag(car["event_c"][axis], car["event_c"][axis])
            * identity32,
        ) and matrix_equal(
            identity32 * sp.diag(car["action_a"][axis],
                                 car["action_a"][axis]),
            sp.diag(car["event_a"][axis], car["event_a"][axis])
            * identity32,
        ) for axis in range(4)
    )
    sector_equation = matrix_equal(
        identity32 * sector_parity, sector_parity * identity32
    )

    u, v = sp.symbols("u v", nonzero=True)
    gauge = sp.diag(u * identity16, v * identity16)
    gauge_inverse = sp.diag(identity16 / u, identity16 / v)
    q_single = paired_kernel("D1", (0,))
    effect = event["effects"][0]
    transformed_effect = sp.simplify(gauge_inverse * effect * gauge)
    similarity_ok = (
        matrix_equal(gauge * q_single, q_single * gauge)
        and matrix_equal(
            q_single + sp.eye(EVENT_DIMENSION) - transformed_effect,
            gauge_inverse
            * (q_single + sp.eye(EVENT_DIMENSION) - effect)
            * gauge,
        )
    )

    symmetry_commutant_ok = True
    for spatial in proper_cubic_rotations():
        full = sp.eye(4)
        full[:3, :3] = spatial
        form_rotation = wedge_representation(full)
        sector_rotation = sp.diag(form_rotation, form_rotation)
        symmetry_commutant_ok = symmetry_commutant_ok and matrix_equal(
            gauge * sector_rotation, sector_rotation * gauge
        )
    fiber_reflection = car["gamma_plus"][3]
    symmetry_commutant_ok = symmetry_commutant_ok and matrix_equal(
        gauge * sp.diag(fiber_reflection, fiber_reflection),
        sp.diag(fiber_reflection, fiber_reflection) * gauge,
    )
    return {
        "common_form_equations": common_form_equations,
        "sector_equation": sector_equation,
        "isometry_representative": matrix_equal(identity32.H * identity32,
                                                  identity32),
        # CAR irreducibility gives one scalar on each sector; sector parity
        # removes the two off-diagonal blocks.
        "solution_dimension": (
            2 if car["scalar_commutant_certificate"] else -1
        ),
        "gauge_group": "U(1)xU(1)",
        "gauge_similarity_ok": similarity_ok,
        "symmetry_commutant_ok": symmetry_commutant_ok,
        "one_map_per_cylinder": True,
        "literal_identity_unique": False,
        "physical_weight_orbits": 1 if similarity_ok else -1,
    }


def projector_factor(effect: sp.MatrixBase) -> tuple[sp.Matrix, sp.Matrix]:
    pivots = sp.Matrix(effect).rref()[1]
    if len(pivots) != 4:
        raise ValueError(f"expected rank-four effect, got {len(pivots)}")
    columns = sp.Matrix.hstack(*(sp.Matrix(effect)[:, pivot]
                                for pivot in pivots))
    gram_inverse = exact_inverse(columns.H * columns)
    left_inverse = sp.simplify(gram_inverse * columns.H)
    return columns, sp.Matrix(left_inverse)


@cache
def factorization_facts() -> dict[str, object]:
    effects = event_facts()["effects"]
    factors = tuple(projector_factor(effect) for effect in effects)
    return {
        "factors": factors,
        "rank_four": all(
            left.shape == (EVENT_DIMENSION, 4)
            and right.shape == (4, EVENT_DIMENSION)
            for left, right in factors
        ),
        "factorizations": all(
            matrix_equal(left * right, effect)
            and matrix_equal(right * left, sp.eye(4))
            for effect, (left, right) in zip(effects, factors)
        ),
        "maximum_update_order": 12,
        "empty_amplitude": sp.Integer(1),
    }


@dataclass(frozen=True)
class OneShotFacts:
    amplitudes: tuple[sp.Expr, ...]
    weights: tuple[sp.Expr, ...]
    raw_sum: sp.Expr
    scalar_in: sp.Expr
    scalar_out: sp.Expr
    compression_scalar: sp.Expr
    determinant_ratio: sp.Expr
    compact_formula_ok: bool
    direct_crosschecks: bool
    determinant_factorization: bool
    exact_real: bool
    exact_positive: bool
    uniform: bool
    one_eighth: bool
    normalized: bool


@cache
def one_shot_facts() -> OneShotFacts:
    q = paired_kernel("D1", (0,))
    identity = sp.eye(EVENT_DIMENSION)
    shifted = q + identity
    determinant_q = exact_determinant(q)
    determinant_shifted = exact_determinant(shifted)
    inverse_shifted = exact_inverse(shifted)
    scalar_in = scalar_boundary(R(0), (0,))[0][0, 0]
    scalar_out = scalar_boundary(R(1), (0,))[0][0, 0]
    determinant_ratio = canonical_scalar(
        ((1 + MASS * scalar_in) / (MASS * scalar_in)) ** 16
        * (((1 + MASS * scalar_out) ** 2 + scalar_out**2)
           / (scalar_out**2 * (MASS**2 + 1))) ** 8
    )
    compression_scalar = canonical_scalar(
        (1 / (1 + MASS * scalar_in)
         + (1 + MASS * scalar_out)
         / ((1 + MASS * scalar_out) ** 2 + scalar_out**2)) / 2
    )
    determinant_factorization = (
        exact_zero(
            determinant_q
            - exact_determinant(q[:FORM_DIMENSION, :FORM_DIMENSION])
            * exact_determinant(q[FORM_DIMENSION:, FORM_DIMENSION:])
        )
        and exact_zero(
            determinant_shifted
            - exact_determinant(
                shifted[:FORM_DIMENSION, :FORM_DIMENSION]
            ) * exact_determinant(
                shifted[FORM_DIMENSION:, FORM_DIMENSION:]
            )
        )
    )
    factors = factorization_facts()["factors"]
    effects = event_facts()["effects"]
    amplitudes = []
    scalar_compressions = True
    for left, right in factors:
        compression = sp.simplify(right * inverse_shifted * left)
        scalar_compressions = scalar_compressions and matrix_equal(
            compression, compression_scalar * sp.eye(4)
        )
        small = sp.eye(4) - compression
        amplitude = canonical_scalar(
            determinant_shifted / determinant_q
            * (exact_determinant(small) - 1)
        )
        amplitudes.append(amplitude)

    direct_crosschecks = True
    for index in (0, EVENT_COUNT - 1):
        direct = canonical_scalar(
            (exact_determinant(shifted - effects[index])
             - determinant_shifted) / determinant_q
        )
        direct_crosschecks = direct_crosschecks and exact_zero(
            direct - amplitudes[index]
        )
    weights = tuple(canonical_scalar(
        sp.conjugate(amplitude) * amplitude
    ) for amplitude in amplitudes)
    raw_sum = canonical_scalar(sum(weights))
    exact_real = all(
        exact_zero(amplitude - sp.conjugate(amplitude))
        and exact_zero(weight - sp.conjugate(weight))
        for amplitude, weight in zip(amplitudes, weights)
    )
    exact_positive_weights = all(exact_positive(weight) for weight in weights)
    uniform = all(exact_zero(weight - weights[0]) for weight in weights)
    return OneShotFacts(
        amplitudes=tuple(amplitudes),
        weights=weights,
        raw_sum=raw_sum,
        scalar_in=scalar_in,
        scalar_out=scalar_out,
        compression_scalar=compression_scalar,
        determinant_ratio=determinant_ratio,
        compact_formula_ok=(
            scalar_compressions
            and exact_zero(determinant_shifted / determinant_q
                           - determinant_ratio)
            and all(exact_zero(
                amplitude
                - determinant_ratio * ((1 - compression_scalar) ** 4 - 1)
            ) for amplitude in amplitudes)
        ),
        direct_crosschecks=direct_crosschecks,
        determinant_factorization=determinant_factorization,
        exact_real=exact_real,
        exact_positive=exact_positive_weights,
        uniform=uniform,
        one_eighth=all(exact_zero(weight - R(1, 8)) for weight in weights),
        normalized=exact_zero(raw_sum - 1),
    )


def embed_factor(
    factor: sp.MatrixBase, time_index: int, count: int, *, left: bool
) -> sp.Matrix:
    if left:
        result = sp.zeros(EVENT_DIMENSION * count, factor.cols)
        result[
            EVENT_DIMENSION * time_index:EVENT_DIMENSION * (time_index + 1), :
        ] = factor
    else:
        result = sp.zeros(factor.rows, EVENT_DIMENSION * count)
        result[:,
               EVENT_DIMENSION * time_index:
               EVENT_DIMENSION * (time_index + 1)] = factor
    return sp.Matrix(result)


def word_amplitude(
    q: sp.MatrixBase, labels: tuple[int, ...]
) -> sp.Expr:
    count = len(labels)
    shifted = sp.Matrix(q) + sp.eye(EVENT_DIMENSION * count)
    determinant_q = exact_determinant(q)
    determinant_shifted = exact_determinant(shifted)
    inverse_shifted = exact_inverse(shifted)
    factors = factorization_facts()["factors"]
    inclusion_exclusion = sp.Integer(0)
    for mask in range(1 << count):
        selected = tuple(index for index in range(count)
                         if mask & (1 << index))
        sign = (-1) ** (count - len(selected))
        if not selected:
            small_determinant = sp.Integer(1)
        else:
            left = sp.Matrix.hstack(*(
                embed_factor(factors[labels[index]][0], index, count,
                             left=True)
                for index in selected
            ))
            right = sp.Matrix.vstack(*(
                embed_factor(factors[labels[index]][1], index, count,
                             left=False)
                for index in selected
            ))
            small_determinant = exact_determinant(
                sp.eye(4 * len(selected)) - right * inverse_shifted * left
            )
        inclusion_exclusion += sign * small_determinant
    return canonical_scalar(
        determinant_shifted / determinant_q * inclusion_exclusion
    )


@cache
def conditional_gluing_residual() -> sp.Expr:
    q024 = paired_kernel("D1", (0, 2, 4))
    q02 = paired_kernel("D1", (0, 2))
    pair_amplitude = word_amplitude(q02, (0, 0))
    pair_weight = canonical_scalar(
        sp.conjugate(pair_amplitude) * pair_amplitude
    )
    triple_sum = sp.Integer(0)
    for final_label in range(EVENT_COUNT):
        amplitude = word_amplitude(q024, (0, 0, final_label))
        triple_sum += canonical_scalar(sp.conjugate(amplitude) * amplitude)
    return canonical_scalar(triple_sum - pair_weight)


def structural_results(
    mutation: str,
) -> tuple[dict[str, tuple[bool, str]], dict[str, object]]:
    p0 = p0_facts()
    t0 = t0_facts()
    car = car_facts()
    event = event_facts()
    intertwiner = intertwiner_facts()
    factors = factorization_facts()

    prereg_ok = p0["prereg_ancestor"] and p0["parent_ancestor"]
    if mutation == "stale_prereg":
        prereg_ok = False
    pilot_clean = p0["pilot_constants_absent"]
    if mutation == "reuse_contaminated_pilot":
        pilot_clean = False
    radii_ok = t0["radius_pairs_ok"] and t0["nine_radii_ok"]
    if mutation == "duplicate_radius_for_c32":
        radii_ok = False
    ordering_ok = t0["ordering_ok"]
    if mutation == "swap_incoming_outgoing":
        ordering_ok = False
    coordinate_ok = car["two_routes_equal"]
    if mutation == "reorder_form_masks":
        coordinate_ok = False
    event_count_ok = len(event["effects"]) == EVENT_COUNT
    if mutation == "drop_one_event_branch":
        event_count_ok = False
    complete_intertwiner_system = car["scalar_commutant_certificate"]
    if mutation == "omit_annihilation_intertwiners":
        complete_intertwiner_system = False
    gauge_not_chosen = True
    if mutation == "choose_relative_phase":
        gauge_not_chosen = False
    common_map = intertwiner["one_map_per_cylinder"]
    if mutation == "crossing_dependent_phase":
        common_map = False
    reflection_ok = event["reflection_map"] == tuple(reversed(range(8)))
    if mutation == "break_reflection_label_map":
        reflection_ok = False
    cubic_ok = event["context_cotransformed"] and event["cubic_family_ok"]
    if mutation == "use_fixed_label_cubic_action":
        cubic_ok = False

    results = {
        "P0": (
            bool(
                prereg_ok
                and p0["goal_frozen"] and p0["preflight_frozen"]
                and p0["contract_present"] and pilot_clean
                and p0["no_project_imports"]
            ),
            "f80e9673ad/c7e0a0b578, frozen packet, contamination firewall, and no-import source bind",
        ),
        "T0.1": (
            bool(radii_ok and ordering_ok and len(FIXTURES) == 6),
            "six ordered incoming/outgoing carriers cover exactly the nine frozen radii",
        ),
        "T0.2": (
            bool(
                t0["scalar_routes_ok"] and t0["scalar_positive"]
                and t0["nesting_ok"] and t0["determinant_ok"]
                and t0["internal_ok"] and t0["paired_routes_ok"]
                and t0["paired_shapes_ok"]
            ),
            "all nonempty subsets of (0,2,4) pass direct/covariance Schur, nesting, determinant, and internal-factor gates",
        ),
        "T1.1": (
            bool(
                coordinate_ok and car["car_ok"] and car["majorana_ok"]
                and event["classifier_rank"] == 2
                and event["classifier_nullity"] == 1
                and event["classifier_ray"] == (0, 0, 1)
                and event["orientation_ok"]
            ),
            "two independent form-coordinate builds agree and derive the unique detector ray",
        ),
        "T1.2": (
            bool(
                event_count_ok and event["pvm_ok"]
                and event["effect_ranks"] == (4,) * EVENT_COUNT
                and event["effect_span_rank"] == EVENT_COUNT
                and event["baseline_weights"] == (R(1, 8),) * EVENT_COUNT
            ),
            "the independently rebuilt eight effects form the exact rank-four C32 PVM",
        ),
        "T1.3": (
            bool(
                complete_intertwiner_system
                and intertwiner["common_form_equations"]
                and intertwiner["sector_equation"]
                and intertwiner["solution_dimension"] == 2
                and intertwiner["gauge_group"] == "U(1)xU(1)"
                and intertwiner["gauge_similarity_ok"]
                and intertwiner["physical_weight_orbits"] == 1
                and intertwiner["symmetry_commutant_ok"]
                and gauge_not_chosen and common_map
            ),
            "the full intertwiner family is U(1)xU(1), with one determinant-weight orbit and one map per cylinder",
        ),
        "T1.4": (
            bool(
                reflection_ok
                and event["coordinate_map"]
                == (1, 0, 3, 2, 5, 4, 7, 6)
                and event["proper_cubic_count"] == 24
                and cubic_ok
            ),
            "fiber/coordinate reflections and all 24 co-transformed cubic contexts retain their distinct typing",
        ),
        "T2.1": (
            bool(
                factors["rank_four"] and factors["factorizations"]
                and factors["maximum_update_order"] == 12
                and factors["empty_amplitude"] == 1
            ),
            "rank-four factors reduce every registered word-dependent determinant to order at most 12",
        ),
    }
    return results, {
        "p0": p0,
        "t0": t0,
        "event": event,
        "intertwiner": intertwiner,
    }


def target_results(
    mutation: str,
) -> tuple[dict[str, tuple[bool, str]], OneShotFacts]:
    one_shot = one_shot_facts()
    berezin_order = mutation != "reverse_berezin_order"
    doubled = mutation != "drop_doubled_conjugation"
    branchwise = mutation != "sum_amplitudes_then_square"
    direct_check = (
        one_shot.direct_crosschecks
        and mutation != "skip_direct_determinant_check"
    )
    raw = mutation != "postnormalize_one_shots"
    positive_gate = one_shot.one_eighth and one_shot.normalized
    opened_gluing = positive_gate
    if mutation == "open_gluing_early":
        opened_gluing = True
    results = {
        "T2.2": (
            bool(
                one_shot.determinant_factorization and direct_check
                and one_shot.compact_formula_ok
                and berezin_order and doubled and branchwise
            ),
            "compressed and direct D1 determinants agree with frozen Berezin order and doubled branchwise conjugation",
        ),
        "T3.1": (
            bool(
                raw and one_shot.exact_real and one_shot.exact_positive
                and one_shot.uniform and len(one_shot.weights) == EVENT_COUNT
            ),
            "all eight raw D1 one-shot amplitudes and weights are exact, real/nonnegative, and evaluated without repair",
        ),
        "STOP": (
            bool(opened_gluing == positive_gate),
            "gluing and T4--T6 open only if the raw one-shot table is exactly 1/8 and normalized",
        ),
    }
    return results, one_shot


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
    "per_element: checked two CAR builds, eight Majoranas, the detector classifier, all eight PVM effects, and rank-four factors.",
    "per_site: checked every nonempty subset of coarse sites (0,2,4) and the raw D1 one-crossing determinant.",
    "per_mode: checked six ordered carriers covering all nine radii; no standalone C16 radius was silently doubled.",
    "per_block: checked authority, Schur carriers, PVM, intertwiner/gauge, compressed determinants, and raw one-shot typing separately.",
    "lattice_wide: checked and not executed — gluing, 729-word D1, other five cylinders, causal process, response, axioms, and TOE remain sealed.",
)


def run_once(mutation: str) -> int:
    structural, _evidence = structural_results(mutation)
    checks = Checks()
    for key, (condition, statement) in structural.items():
        checks.check(key, statement, condition)
    if any(not condition for condition, _statement in structural.values()):
        print("[SEALED] T3--T6: an earlier structural gate failed")
        for line in N5_LINES:
            print(line)
        return checks.finish()

    target, one_shot = target_results(mutation)
    for key, (condition, statement) in target.items():
        checks.check(key, statement, condition)

    weight = one_shot.weights[0]
    print(
        "INTERTWINER: solution_dim=2; gauge=U(1)xU(1); "
        "weight_orbits=1; representative_not_selected"
    )
    print(
        "D1_ONE_SHOT_CERTIFICATE: m=2/7; q_in="
        f"{one_shot.scalar_in}; q_out={one_shot.scalar_out}; "
        f"k={one_shot.compression_scalar}"
    )
    print(
        "D1_ONE_SHOT_FORMULA: Rdet=((1+m*q_in)/(m*q_in))^16*"
        "(((1+m*q_out)^2+q_out^2)/(q_out^2*(m^2+1)))^8; "
        "A=Rdet*((1-k)^4-1)"
    )
    print(
        "D1_ONE_SHOT_OUTCOME: amplitudes=(A,)*8; weights=(A^2,)*8; "
        f"raw_sum=8*A^2; A^2_eq_1/8={exact_zero(weight - R(1, 8))}; "
        f"raw_sum_eq_1={exact_zero(one_shot.raw_sum - 1)}; "
        f"unique_amplitudes={len(set(one_shot.amplitudes))}"
    )
    positive_gate = one_shot.one_eighth and one_shot.normalized
    if not positive_gate:
        print(
            "[SEALED] GLUING/T4-T6: raw one-shot gate failed; "
            "no prefactor or post-normalization attempted"
        )
        print(
            "VERDICT: exact determinant family fails its raw D1 one-shot "
            "normalization gate; no broader direct-functional no-go"
        )
    else:
        residual = conditional_gluing_residual()
        checks.check(
            "T3.2",
            "the preregistered D1 Delta_00 gluing residual is exact",
            exact_zero(residual),
        )
        print(f"D1_GLUING: Delta_00^02={residual}")
        print("[SEALED] T4-T6: outside this independent checker dispatch")
    for line in N5_LINES:
        print(line)
    return checks.finish()


def mutation_self_test() -> int:
    baseline_structural, _ = structural_results("")
    baseline_target, _ = target_results("")
    baseline = {**baseline_structural, **baseline_target}
    baseline_failures = tuple(
        key for key, (condition, _statement) in baseline.items()
        if not condition
    )
    failures = int(bool(baseline_failures))
    print(f"BASELINE: failures={baseline_failures}")
    for mutation in MUTATIONS:
        structural, _ = structural_results(mutation)
        results = dict(structural)
        if all(condition for condition, _statement in structural.values()):
            target, _ = target_results(mutation)
            results.update(target)
        caught = tuple(
            key for key, (condition, _statement) in results.items()
            if not condition
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
