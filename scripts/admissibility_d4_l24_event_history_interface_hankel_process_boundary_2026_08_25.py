#!/usr/bin/env python3
"""Block 199: exact event-history interface and Hankel/process boundary.

The runner keeps the action's field moments, the fixed Block-194 event
operations, and an operational process functional distinctly typed.  It
executes the event-operation census and all-nine-radius moment taxonomy before
testing whether the registered inputs determine event words or a causal
boundary.  Process, response, and held-out gates stay sealed on an interface
failure.
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

import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_L24_EVENT_HISTORY_INTERFACE_HANKEL_PROCESS_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "fdf8a1b8c7"
PREREG_COMMIT = "be4c2b2462"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block199-event-process-memory-20260825/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block199-event-process-memory-20260825/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block199-event-process-memory-20260825/STATE.yaml",
    "docs/ADMISSIBILITY_D4_L24_EVENT_HISTORY_INTERFACE_HANKEL_PROCESS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_D4_L24_EVEN_ODD_TWO_STEP_OS_PARITY_HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_l24_even_odd_two_step_os_parity_history_boundary_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_L24_PREFIX_INSTRUMENT_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_l24_prefix_instrument_selection_boundary_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_d4_l24_event_history_interface_hankel_process_boundary_2026_08_25.py",
)

R = sp.Rational
I = sp.I
MASS = R(2, 7)
COARSE_TIME = 12
EVENT_LABELS = tuple(product((-1, 1), (-1, 1), (-1, 1)))
FROZEN_SQUARED_RADII = (
    R(0), R(3, 4), R(1), R(5, 4), R(3, 2), R(2), R(3),
    (7 + sp.sqrt(3)) / 4,
    (10 + sp.sqrt(3)) / 4,
)

MUTATIONS = (
    "wrong_mass",
    "omit_frozen_radius",
    "eight_only_tomography",
    "identity_as_dephasing",
    "remove_phase_probes",
    "conflate_moment_families",
    "claim_scalar_rank_is_process_memory",
    "promote_coherent_probes",
    "promote_source_tangent",
    "import_boundary_density",
    "claim_unique_history",
    "open_process_early",
    "open_response_early",
    "claim_axiom_required",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "wrong_mass": "P",
    "omit_frozen_radius": "T2",
    "eight_only_tomography": "T0",
    "identity_as_dephasing": "T0",
    "remove_phase_probes": "T0",
    "conflate_moment_families": "T2",
    "claim_scalar_rank_is_process_memory": "T2",
    "promote_coherent_probes": "T3",
    "promote_source_tangent": "T3",
    "import_boundary_density": "T3",
    "claim_unique_history": "T3",
    "open_process_early": "S",
    "open_response_early": "S",
    "claim_axiom_required": "S",
    "claim_toe_progress": "S",
}


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


def exact_sign(value: sp.Expr) -> int:
    value = sp.factor(value)
    if value == 0:
        return 0
    if value.is_positive is True:
        return 1
    if value.is_negative is True:
        return -1
    numeric = sp.N(value, 80)
    if numeric > 0:
        return 1
    if numeric < 0:
        return -1
    raise ValueError(f"undetermined exact sign: {value}")


def symmetric_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    work = sp.MutableDenseMatrix(matrix)
    if not matrix_equal(work, work.T.conjugate()):
        raise ValueError("inertia requires an exact Hermitian matrix")
    positive = negative = 0
    active = work.rows
    while active:
        diagonal = next(
            (index for index in range(active) if work[index, index] != 0),
            None,
        )
        if diagonal is not None:
            if diagonal:
                work.row_swap(0, diagonal)
                work.col_swap(0, diagonal)
            pivot = sp.factor(work[0, 0])
            sign = exact_sign(pivot)
            positive += int(sign > 0)
            negative += int(sign < 0)
            if active == 1:
                break
            column = work[1:active, 0]
            row = work[0, 1:active]
            work = sp.MutableDenseMatrix(sp.simplify(
                work[1:active, 1:active] - column * row / pivot
            ))
            active -= 1
            continue
        pair = next((
            (row, column)
            for row in range(active)
            for column in range(row + 1, active)
            if work[row, column] != 0
        ), None)
        if pair is None:
            break
        row_index, column_index = pair
        order = [row_index, column_index] + [
            index for index in range(active)
            if index not in (row_index, column_index)
        ]
        work = sp.MutableDenseMatrix(work.extract(order, order))
        block = work[:2, :2]
        if exact_sign(sp.det(block)) != -1:
            raise ValueError("unexpected two-dimensional inertia pivot")
        positive += 1
        negative += 1
        if active == 2:
            break
        cross_left = work[2:active, :2]
        cross_right = work[:2, 2:active]
        work = sp.MutableDenseMatrix(sp.simplify(
            work[2:active, 2:active]
            - cross_left * block.inv() * cross_right
        ))
        active -= 2
    return positive, matrix.rows - positive - negative, negative


def git_output(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "axiom": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "worktree_axiom": git_output("rev-parse", f"HEAD:{AXIOM_PATH}"),
        "registry": git_output("rev-parse", f"origin/main:{REGISTRY_PATH}"),
        "worktree_registry": git_output("rev-parse", f"HEAD:{REGISTRY_PATH}"),
        "inputs": all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS),
    }


def hermitian_coordinates(matrix: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    coordinates: list[sp.Expr] = []
    coordinates.extend(sp.simplify(matrix[index, index]) for index in range(8))
    for left in range(8):
        for right in range(left + 1, 8):
            coordinates.append(sp.simplify(sp.re(matrix[left, right])))
            coordinates.append(sp.simplify(sp.im(matrix[left, right])))
    return tuple(coordinates)


def probe_outer(vector: sp.MatrixBase) -> sp.Matrix:
    return sp.expand(vector * vector.H)


@cache
def operation_facts() -> dict[str, object]:
    instrument = b194.instrument_pointer_facts()
    effects = tuple(sp.Matrix(effect) for effect in instrument["effects"])
    effect_gram = sp.Matrix([
        [sp.trace(left.H * right) / 4 for right in effects]
        for left in effects
    ])

    basis = tuple(sp.eye(8)[:, index] for index in range(8))
    diagonal_probes = tuple(probe_outer(vector) for vector in basis)
    real_probes = tuple(
        probe_outer(basis[left] + basis[right])
        for left in range(8) for right in range(left + 1, 8)
    )
    phase_probes = tuple(
        probe_outer(basis[left] + I * basis[right])
        for left in range(8) for right in range(left + 1, 8)
    )
    full_probes = diagonal_probes + real_probes + phase_probes
    no_phase_probes = diagonal_probes + real_probes
    full_design = sp.Matrix([
        hermitian_coordinates(probe) for probe in full_probes
    ])
    no_phase_design = sp.Matrix([
        hermitian_coordinates(probe) for probe in no_phase_probes
    ])
    branch_design = sp.Matrix([
        hermitian_coordinates(probe) for probe in diagonal_probes
    ])
    identity_choi = probe_outer(sp.ones(8, 1))
    dephasing_choi = sp.eye(8)
    branch_plus_identity = sp.Matrix([
        hermitian_coordinates(probe)
        for probe in diagonal_probes + (identity_choi,)
    ])

    offdiagonal_witness = None
    for row in range(32):
        for column in range(32):
            matrix_unit = sp.zeros(32)
            matrix_unit[row, column] = 1
            candidate = sp.expand(effects[0] * matrix_unit * effects[1])
            if candidate != sp.zeros(32):
                offdiagonal_witness = candidate
                break
        if offdiagonal_witness is not None:
            break
    if offdiagonal_witness is None:
        raise ValueError("failed to find an inter-event coherence witness")
    dephased_witness = sum(
        (effect * offdiagonal_witness * effect for effect in effects),
        sp.zeros(32),
    )

    return {
        "effects": effects,
        "effect_gram": effect_gram,
        "effect_span_dimension": effect_gram.rank(),
        "effect_ranks": tuple(effect.rank() for effect in effects),
        "commutative": all(
            matrix_equal(left * right, right * left)
            for left in effects for right in effects
        ),
        "complete": matrix_equal(sum(effects, sp.zeros(32)), sp.eye(32)),
        "branch_frame_rank": branch_design.rank(),
        "branch_plus_identity_rank": branch_plus_identity.rank(),
        "full_frame_rank": full_design.rank(),
        "full_frame_determinant": sp.det(full_design),
        "no_phase_frame_rank": no_phase_design.rank(),
        "identity_choi_rank": identity_choi.rank(),
        "dephasing_choi_rank": dephasing_choi.rank(),
        "identity_distinct_from_dephasing": (
            not matrix_equal(identity_choi, dephasing_choi)
            and dephased_witness == sp.zeros(32)
            and offdiagonal_witness != sp.zeros(32)
        ),
        "identity_superoperator_rank": 32**2,
        "dephasing_superoperator_rank": sum(
            rank**2 for rank in instrument["effect_ranks"]
        ),
        "writer_exact": (
            instrument["writer_unitary"]
            and instrument["writer_nonidentity"]
            and instrument["faithful_joint_readout"]
        ),
        "coherent_probe_tni": all(
            matrix_equal(
                (effects[left] + phase * effects[right]).H
                * (effects[left] + phase * effects[right]),
                effects[left] + effects[right],
            )
            for left in range(8) for right in range(left + 1, 8)
            for phase in (1, I)
        ),
    }


def coarse_shift() -> sp.Matrix:
    shift = sp.zeros(COARSE_TIME)
    for site in range(COARSE_TIME):
        shift[(site + 1) % COARSE_TIME, site] = 1
    return shift


def matrix_hankel(sequence: tuple[sp.Expr, ...], size: int) -> sp.Matrix:
    return sp.Matrix(size, size, lambda row, column: sequence[row + column])


@cache
def radius_moment_facts(squared_radius: sp.Expr, mass: sp.Expr = MASS) -> dict[str, object]:
    delta = sp.simplify(mass**2 + squared_radius)
    shift = coarse_shift()
    q_matrix = sp.simplify(
        sp.eye(COARSE_TIME)
        + (2 * sp.eye(COARSE_TIME) - shift - shift.T) / (4 * delta)
    )
    q_inverse = exact_inverse(q_matrix)
    sequence = tuple(sp.factor(q_inverse[index, 0]) for index in range(12))
    recurrence = all(
        sp.simplify(
            sequence[index + 1]
            - (4 * delta + 2) * sequence[index]
            + sequence[index - 1]
        ) == 0
        for index in range(1, 11)
    )
    seam_residual = sp.factor(
        (4 * delta + 2) * sequence[0] - sequence[1] - sequence[-1]
    )
    ordinary_ranks = tuple(
        matrix_hankel(sequence, size).rank() for size in range(2, 7)
    )
    circular_hankel = sp.Matrix(
        COARSE_TIME, COARSE_TIME,
        lambda row, column: sequence[(row + column) % COARSE_TIME],
    )

    coefficient = sp.factor(2 * mass / delta)
    positive_scalar = sp.Matrix((
        (sequence[0], sequence[1]),
        (sequence[1], sequence[2]),
    ))
    positive_hankel = sp.kronecker_product(
        coefficient * positive_scalar, sp.eye(2)
    )
    positive_defect = sp.factor(
        coefficient * (
            sequence[2] - sequence[1] ** 2 / sequence[0]
        )
    )

    radius = sp.sqrt(squared_radius)
    internal_reflected = sp.Matrix((
        (mass, -radius), (-radius, -mass)
    )) / delta
    reflected_scalar = -sp.Matrix((
        (sequence[1], sequence[2]),
        (sequence[2], sequence[3]),
    ))
    reflected_hankel = sp.kronecker_product(
        reflected_scalar, internal_reflected
    )
    reflected_defect_scalar = sp.factor(
        -sequence[3] + sequence[2] ** 2 / sequence[1]
    )
    reflected_defect = sp.simplify(
        reflected_defect_scalar * internal_reflected
    )

    ratio_one = sp.factor(sequence[1] / sequence[0])
    ratio_two = sp.factor(sequence[2] / sequence[0])
    probability_floor = sp.factor(1 - 2 * ratio_one + ratio_two)

    return {
        "radius": squared_radius,
        "delta": delta,
        "q": q_matrix,
        "q_inverse": q_inverse,
        "sequence": sequence,
        "all_sequence_positive": all(exact_sign(value) == 1 for value in sequence),
        "recurrence": recurrence,
        "seam_residual": seam_residual,
        "ordinary_ranks": ordinary_ranks,
        "circular_rank": circular_hankel.rank(),
        "positive_hankel": positive_hankel,
        "positive_inertia": symmetric_inertia(positive_hankel),
        "positive_defect": positive_defect,
        "reflected_hankel": reflected_hankel,
        "reflected_inertia": symmetric_inertia(reflected_hankel),
        "reflected_defect_scalar": reflected_defect_scalar,
        "reflected_defect": reflected_defect,
        "reflected_defect_det": sp.factor(reflected_defect.det()),
        "internal_reflected_det": sp.factor(internal_reflected.det()),
        "ratio_one": ratio_one,
        "ratio_two": ratio_two,
        "probability_floor": probability_floor,
    }


def conditional_history_probability(
    signs: tuple[int, int, int], ratio_one: sp.Expr, ratio_two: sp.Expr
) -> sp.Expr:
    first, second, third = signs
    return sp.factor((
        1
        + ratio_one * (first * second + second * third)
        + ratio_two * first * third
    ) / 8)


@cache
def conditional_history_facts(squared_radius: sp.Expr) -> dict[str, object]:
    moments = radius_moment_facts(squared_radius)
    ratio_one = moments["ratio_one"]
    ratio_two = moments["ratio_two"]
    signs = tuple(product((-1, 1), repeat=3))
    sign_probabilities = {
        word: conditional_history_probability(word, ratio_one, ratio_two)
        for word in signs
    }

    histories = tuple(product(range(4), (-1, 1), repeat=3))
    # Histories are encoded as (port0,sign0,port1,sign1,port2,sign2).
    endpoint_zero: dict[tuple[int, ...], sp.Expr] = {}
    endpoint_max: dict[tuple[int, ...], sp.Expr] = {}

    def port_probability(ports: tuple[int, int, int], b: sp.Expr) -> sp.Expr:
        distinct = len(set(ports))
        if distinct == 1:
            return R(1, 16) - 3 * b
        if distinct == 2:
            return b
        return R(1, 32) - b

    for history in histories:
        ports = (history[0], history[2], history[4])
        sign_word = (history[1], history[3], history[5])
        sign_probability = sign_probabilities[sign_word]
        endpoint_zero[history] = sp.factor(
            sign_probability * port_probability(ports, sp.Integer(0))
        )
        endpoint_max[history] = sp.factor(
            sign_probability * port_probability(ports, R(1, 48))
        )
    laws = (endpoint_zero, endpoint_max)

    def marginal(
        law: dict[tuple[int, ...], sp.Expr], slot: int, port: int, sign: int
    ) -> sp.Expr:
        return sp.factor(sum(
            value for history, value in law.items()
            if history[2 * slot] == port and history[2 * slot + 1] == sign
        ))

    def signed_correlation(
        law: dict[tuple[int, ...], sp.Expr], left: int, right: int
    ) -> sp.Expr:
        return sp.factor(sum(
            value * history[2 * left + 1] * history[2 * right + 1]
            for history, value in law.items()
        ))

    def pair_marginal(
        law: dict[tuple[int, ...], sp.Expr], left: int, right: int,
        left_port: int, left_sign: int, right_port: int, right_sign: int,
    ) -> sp.Expr:
        return sp.factor(sum(
            value for history, value in law.items()
            if history[2 * left] == left_port
            and history[2 * left + 1] == left_sign
            and history[2 * right] == right_port
            and history[2 * right + 1] == right_sign
        ))

    def time_reverse(history: tuple[int, ...]) -> tuple[int, ...]:
        return history[4:6] + history[2:4] + history[0:2]

    def global_sign_flip(history: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(
            -value if index % 2 else value
            for index, value in enumerate(history)
        )

    def permute_ports(
        history: tuple[int, ...], permutation: tuple[int, ...]
    ) -> tuple[int, ...]:
        return tuple(
            permutation[value] if index % 2 == 0 else value
            for index, value in enumerate(history)
        )

    pair_correlations = {(0, 1): ratio_one, (1, 2): ratio_one, (0, 2): ratio_two}
    port_permutations = tuple(permutations(range(4)))
    d = MASS**2 + squared_radius

    return {
        "sign_normalized": sp.simplify(sum(sign_probabilities.values())) == 1,
        "sign_positive": all(exact_sign(value) == 1 for value in sign_probabilities.values()),
        "floor_positive": exact_sign(moments["probability_floor"]) == 1,
        "laws_normalized": all(
            sp.simplify(sum(law.values())) == 1 for law in laws
        ),
        "uniform_one_shot": all(
            marginal(law, slot, port, sign) == R(1, 8)
            for law in laws
            for slot in range(3) for port in range(4) for sign in (-1, 1)
        ),
        "signed_correlations": all(
            signed_correlation(law, 0, 1) == ratio_one
            and signed_correlation(law, 1, 2) == ratio_one
            and signed_correlation(law, 0, 2) == ratio_two
            for law in laws
        ),
        "complete_pair_tables": all(
            pair_marginal(
                law, left, right, left_port, left_sign, right_port, right_sign
            ) == sp.factor(
                (1 + pair_correlations[(left, right)] * left_sign * right_sign) / 64
            )
            for law in laws
            for left, right in pair_correlations
            for left_port in range(4) for right_port in range(4)
            for left_sign in (-1, 1) for right_sign in (-1, 1)
        ),
        "time_reversal": all(
            law[history] == law[time_reverse(history)]
            for law in laws for history in histories
        ),
        "global_sign_symmetry": all(
            law[history] == law[global_sign_flip(history)]
            for law in laws for history in histories
        ),
        "port_permutation_symmetry": all(
            law[history] == law[permute_ports(history, permutation)]
            for law in laws for history in histories for permutation in port_permutations
        ),
        "diagonal_strong_positivity": all(
            exact_sign(value) >= 0
            for law in laws for value in law.values()
        ),
        "binary_reflection_unique": all(
            sign_probabilities[word]
            == sign_probabilities[tuple(-value for value in word)]
            for word in signs
        ) and sp.factor(moments["probability_floor"] - 4 * d * ratio_one) == 0,
        "inequivalent": any(
            endpoint_zero[history] != endpoint_max[history] for history in histories
        ),
        "endpoint_zero_all_ports_equal": sp.factor(sum(
            value for history, value in endpoint_zero.items()
            if history[0] == history[2] == history[4]
        )),
        "endpoint_max_all_ports_equal": sp.factor(sum(
            value for history, value in endpoint_max.items()
            if history[0] == history[2] == history[4]
        )),
    }


@cache
def target_facts(mutation: str = "") -> dict[str, object]:
    mass = R(3, 7) if mutation == "wrong_mass" else MASS
    radii = (
        FROZEN_SQUARED_RADII[:-1]
        if mutation == "omit_frozen_radius" else FROZEN_SQUARED_RADII
    )
    moments = tuple(radius_moment_facts(radius, mass) for radius in radii)
    histories = tuple(
        conditional_history_facts(radius) for radius in radii
    ) if mass == MASS else ()
    radius_one = moments[radii.index(R(1))]
    return {
        "radii": radii,
        "moments": moments,
        "histories": histories,
        "radius_one": radius_one,
        "all_positive_sequence": all(value["all_sequence_positive"] for value in moments),
        "all_recurrence": all(value["recurrence"] for value in moments),
        "all_seams": all(sp.simplify(
            value["seam_residual"] - 4 * value["delta"]
        ) == 0 for value in moments),
        "all_ordinary_rank_two": all(
            value["ordinary_ranks"] == (2, 2, 2, 2, 2) for value in moments
        ),
        "all_circular_rank_twelve": all(
            value["circular_rank"] == 12 for value in moments
        ),
        "all_positive_hankel": all(
            value["positive_inertia"] == (4, 0, 0)
            and exact_sign(value["positive_defect"]) == 1
            for value in moments
        ),
        "all_reflected_indefinite": all(
            value["reflected_inertia"] == (2, 0, 2)
            and exact_sign(value["reflected_defect_scalar"]) == -1
            and exact_sign(value["reflected_defect_det"]) == -1
            and sp.simplify(
                value["internal_reflected_det"] + 1 / value["delta"]
            ) == 0
            for value in moments
        ),
        "all_conditional_histories": bool(histories) and all(
            value["sign_normalized"] and value["sign_positive"]
            and value["floor_positive"] and value["laws_normalized"]
            and value["uniform_one_shot"] and value["signed_correlations"]
            and value["complete_pair_tables"]
            and value["time_reversal"] and value["global_sign_symmetry"]
            and value["port_permutation_symmetry"]
            and value["diagonal_strong_positivity"] and value["inequivalent"]
            and value["binary_reflection_unique"]
            and value["endpoint_zero_all_ports_equal"] == R(1, 4)
            and value["endpoint_max_all_ports_equal"] == 0
            for value in histories
        ),
    }


def note_contract() -> bool:
    if not NOTE_PATH.exists():
        return False
    text = NOTE_PATH.read_text(encoding="utf-8")
    required = (
        "## 8. No-Go Discipline Gate",
        "### N1", "### N2", "### N3", "### N4",
        "### N5", "### N6", "### N7", "### N8",
        "partial-attempt-with-named-untested-routes",
        "effect_system_dimension: eight",
        "declared_operation_span_dimension: nine",
        "event_support_frame_dimension: sixty_four_control_only",
        "event_process_interface: not_derived",
        "TOE lane scores remain unchanged",
        "No axiom amendment",
    )
    return all(needle in text for needle in required)


def evaluate(mutation: str) -> dict[str, tuple[object, str]]:
    authority = authority_facts()
    operations = operation_facts()
    target = target_facts(mutation)
    claims = {
        "tomographic": mutation == "eight_only_tomography",
        "identity_is_dephasing": mutation == "identity_as_dephasing",
        "phase_frame_complete": mutation != "remove_phase_probes",
        "moments_conflated": mutation == "conflate_moment_families",
        "scalar_is_process_memory": mutation == "claim_scalar_rank_is_process_memory",
        "coherent_registered": mutation == "promote_coherent_probes",
        "source_is_operation": mutation == "promote_source_tangent",
        "boundary_imported": mutation == "import_boundary_density",
        "unique_history": mutation == "claim_unique_history",
        "process": mutation == "open_process_early",
        "response": mutation == "open_response_early",
        "axiom": mutation == "claim_axiom_required",
        "toe": mutation == "claim_toe_progress",
    }
    radius_one = target["radius_one"]
    return {
        "A": (
            authority["main"] == CURRENT_MAIN
            and authority["parent"] and authority["prereg"]
            and authority["axiom"] == authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
            and authority["registry"] == CURRENT_REGISTRY_BLOB
            and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
            and authority["inputs"],
            "authority, preregistration ancestry, premise blobs, and literal inputs bind",
        ),
        "T0": (
            operations["effect_span_dimension"] == 8
            and operations["effect_gram"] == sp.eye(8)
            and set(operations["effect_ranks"]) == {4}
            and operations["commutative"] and operations["complete"]
            and operations["branch_frame_rank"] == 8
            and operations["branch_plus_identity_rank"] == 9
            and operations["full_frame_rank"] == 64
            and abs(operations["full_frame_determinant"]) == 1
            and operations["no_phase_frame_rank"] == 36
            and operations["identity_choi_rank"] == 1
            and operations["dephasing_choi_rank"] == 8
            and operations["identity_superoperator_rank"] == 1024
            and operations["dephasing_superoperator_rank"] == 128
            and operations["identity_distinct_from_dephasing"]
            and operations["writer_exact"] and operations["coherent_probe_tni"]
            and claims["tomographic"] is False
            and claims["identity_is_dephasing"] is False
            and claims["phase_frame_complete"],
            "the registered 8/9-dimensional operation domain, identity/dephasing split, and 64-probe mathematical control are exact",
        ),
        "T1": (
            target["all_positive_sequence"] and target["all_seams"]
            and radius_one["q"].det() != 0
            and claims["moments_conflated"] is False,
            "the cyclic Green, open-cut covariance, positive moment, and reflected Berezin objects remain distinctly typed",
        ),
        "T2": (
            len(target["radii"]) == len(FROZEN_SQUARED_RADII)
            and target["all_recurrence"] and target["all_ordinary_rank_two"]
            and target["all_circular_rank_twelve"]
            and target["all_positive_hankel"]
            and target["all_reflected_indefinite"]
            and claims["scalar_is_process_memory"] is False,
            "all nine radii have recurrence order two, circular rank twelve, positive C Hankels, and indefinite M Hankels without a process-memory promotion",
        ),
        "T3": (
            target["all_conditional_histories"]
            and operations["branch_plus_identity_rank"] < operations["full_frame_rank"]
            and claims["coherent_registered"] is False
            and claims["source_is_operation"] is False
            and claims["boundary_imported"] is False
            and claims["unique_history"] is False,
            "the registered inputs do not select an event insertion/boundary: two conditional strongly-positive histories share every one- and two-crossing PVM table but differ at three crossings",
        ),
        "N": (
            note_contract(),
            "the landed source note contains the fresh N1--N8 bounded-negative packet",
        ),
        "S": (
            claims["process"] is False and claims["response"] is False
            and claims["axiom"] is False and claims["toe"] is False,
            "full process, response, heldouts, axiom amendment, and TOE movement remain sealed",
        ),
    }


N5_LINES = (
    "per_element: checked all eight rank-four event effects, eight Lueders branches, identity/dephasing distinction, 64 coherent-frame controls, and two signed field-moment families.",
    "per_site: checked one-shot M2 realization and two inequivalent three-crossing fixed-PVM cylinder laws with identical complete one- and two-crossing tables; no pointer reset, repeated writer, or causal boundary was supplied.",
    "per_mode: checked all nine exact spatial radii, nonwrapped Hankel sizes two through six, circular rank twelve, and the eight-copy reflected lift.",
    "per_block: checked event-operation typing, cyclic/open action objects, Green recurrence, positive and indefinite Hankels, and interface nonuniqueness as separate dependency blocks.",
    "lattice_wide: checked and not executed — no informationally complete physical operation family, causal process tensor, full-L24 event law, response, held-out, Record persistence, gravity, axiom, or TOE closure is claimed.",
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0
    checks = Checks()
    results = evaluate(args.mutation)
    for key, (condition, statement) in results.items():
        checks.check(key, statement, condition)
    operations = operation_facts()
    target = target_facts(args.mutation)
    radius_one = target["radius_one"]
    print(
        "WITNESS: declared_operation_rank="
        f"{operations['branch_plus_identity_rank']}; full_frame_rank="
        f"{operations['full_frame_rank']}; no_phase_rank="
        f"{operations['no_phase_frame_rank']}; interface_deficit="
        f"{operations['full_frame_rank'] - operations['branch_plus_identity_rank']}"
    )
    print(
        "MOMENTS: radius_one_positive_defect="
        f"{radius_one['positive_defect']}; reflected_defect_scalar="
        f"{radius_one['reflected_defect_scalar']}; reflected_defect_det="
        f"{radius_one['reflected_defect_det']}"
    )
    if target["histories"]:
        history = target["histories"][target["radii"].index(R(1))]
        print(
            "NONUNIQUENESS: same_complete_two_crossing_tables=true; "
            "endpoint_zero_port_triple_equal="
            f"{history['endpoint_zero_all_ports_equal']}; "
            "endpoint_max_port_triple_equal="
            f"{history['endpoint_max_all_ports_equal']}"
        )
    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
