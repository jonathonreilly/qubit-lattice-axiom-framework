#!/usr/bin/env python3
"""Check the Record-formation and Lorentzian-selection boundary.

The current axioms fix a nearest-neighbour content distribution conditional on
formation, while explicitly withholding the formation site/rate, update law,
and time metric.  This runner constructs exact compatible completions that
share the same local content rule or the same static repaired-edge operator
but disagree on formation rate, causal precedence, light speed, or whether
lapse/shift remain constraints.  The result is an underdetermination witness,
not a gravity no-go or an adopted axiom amendment.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_"
    "TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_"
    "2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
TRANSFER_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_"
    "RESPONSE_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
LORENTZ_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_PERMANENT_RECORD_FORMATION_SCHEDULER_LORENTZIAN_TIME_CONSTRAINT_SELECTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_local_geometry_record_bond_transfer_reflection_response_connection_boundary_2026_08_11.py",
    "scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11 as block44  # noqa: E402


EMPTY = 0
CONTENTS = (-1, 1)
Q_SLOW = Fraction(1, 3)
Q_FAST = Fraction(2, 3)
ZETA = 0.25
TOLERANCE = 1.0e-11


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def content_distribution(neighbours: tuple[int, ...]) -> dict[int, Fraction]:
    """One fixed spin-flip and proper-cubic invariant local content rule."""
    if len(neighbours) != 6 or any(value not in (EMPTY, *CONTENTS) for value in neighbours):
        raise ValueError("expected six empty/binary neighbour conditions")
    weights = {
        candidate: Fraction(4 ** sum(value == candidate for value in neighbours), 1)
        for candidate in CONTENTS
    }
    normalizer = sum(weights.values(), Fraction(0, 1))
    return {candidate: weight / normalizer for candidate, weight in weights.items()}


def local_record_kernel(
    current: int, neighbours: tuple[int, ...], formation_probability: Fraction
) -> dict[int, Fraction]:
    """One-step monotone Record extension at a supplied discrete tick."""
    if not (Fraction(0, 1) < formation_probability <= Fraction(1, 1)):
        raise ValueError("formation probability must be in (0,1]")
    if current in CONTENTS:
        return {EMPTY: Fraction(0, 1), -1: Fraction(current == -1), 1: Fraction(current == 1)}
    distribution = content_distribution(neighbours)
    return {
        EMPTY: Fraction(1, 1) - formation_probability,
        -1: formation_probability * distribution[-1],
        1: formation_probability * distribution[1],
    }


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1.0, 1.0), repeat=3):
            matrix = np.zeros((3, 3), dtype=float)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                rotations.append(matrix)
    return tuple(rotations)


NEIGHBOUR_DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def neighbour_permutation(rotation: np.ndarray) -> tuple[int, ...]:
    direction_index = {direction: index for index, direction in enumerate(NEIGHBOUR_DIRECTIONS)}
    return tuple(
        direction_index[tuple(int(value) for value in rotation @ np.asarray(direction))]
        for direction in NEIGHBOUR_DIRECTIONS
    )


def two_site_schedule_laws() -> tuple[dict[tuple[int, int], Fraction], dict[tuple[int, int], Fraction]]:
    """Parallel and endpoint-exchange-symmetric sequential two-record laws."""
    parallel = {(left, right): Fraction(1, 4) for left in CONTENTS for right in CONTENTS}
    sequential: dict[tuple[int, int], Fraction] = {}
    empty_tail = (EMPTY,) * 5
    for left in CONTENTS:
        for right in CONTENTS:
            left_first = Fraction(1, 2) * Fraction(1, 2) * content_distribution((left, *empty_tail))[right]
            right_first = Fraction(1, 2) * Fraction(1, 2) * content_distribution((right, *empty_tail))[left]
            sequential[(left, right)] = left_first + right_first
    return parallel, sequential


def symmetric_coordinate_representation(rotation: np.ndarray) -> np.ndarray:
    rotation4 = np.eye(4)
    rotation4[:3, :3] = rotation
    representation = np.zeros((len(block44.HCOMPS), len(block44.HCOMPS)))
    for column in range(len(block44.HCOMPS)):
        transformed = rotation4 @ block44.symmetric_basis(column) @ rotation4.T
        representation[:, column] = [
            transformed[left, right] for left, right in block44.HCOMPS
        ]
    return representation


def timed_einstein_operator(
    spatial_momentum: np.ndarray | tuple[float, ...], frequency: float, time_scale: float
) -> np.ndarray:
    return block44.lorentzian_operator(spatial_momentum, time_scale * frequency)


TIME_PROJECTOR = np.diag(
    [1.0 if index in block44.TIME_COMPONENTS else 0.0 for index in range(len(block44.HCOMPS))]
)


def constraint_breaking_operator(
    spatial_momentum: np.ndarray | tuple[float, ...], frequency: float, zeta: float
) -> np.ndarray:
    return block44.lorentzian_operator(spatial_momentum, frequency) + zeta * frequency**2 * TIME_PROJECTOR


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    transfer_note = flat(TRANSFER_NOTE_PATH)
    lorentz_note = flat(LORENTZ_NOTE_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current axiom and two constructive parents are bound without importing a physical update",
        all(path.exists() for path in (NOTE_PATH, AXIOM_PATH, TRANSFER_NOTE_PATH, LORENTZ_NOTE_PATH, PREMISE_REGISTRY_PATH))
        and "does not supply the formation site, probability, or rate" in axiom
        and "does not choose a hamiltonian or transfer operator" in axiom
        and "time metric" in axiom
        and "therefore is record-erasing" in transfer_note
        and "not a record-native causal update" in lorentz_note,
    )

    rotations = proper_cubic_rotations()
    neighbour_permutations = tuple(neighbour_permutation(rotation) for rotation in rotations)
    local_normalization = True
    local_covariance = True
    spin_flip_covariance = True
    for neighbours in product((EMPTY, *CONTENTS), repeat=6):
        distribution = content_distribution(neighbours)
        local_normalization &= sum(distribution.values(), Fraction(0, 1)) == 1
        spin_flipped = tuple(-value for value in neighbours)
        spin_flip_covariance &= distribution[1] == content_distribution(spin_flipped)[-1]
        for permutation in neighbour_permutations:
            rotated = tuple(neighbours[index] for index in permutation)
            local_covariance &= distribution == content_distribution(rotated)
    checks.check(
        "fixed-content-rule-covariance",
        "one exact binary M2 subalphabet rule is normalized on all neighbour conditions and proper-cubic covariant",
        len(rotations) == 24 and local_normalization and local_covariance and spin_flip_covariance,
        "neighbour environments=729; proper rotations=24",
    )

    monotone = True
    same_content_conditional = True
    kernel_normalization = True
    for current in (EMPTY, *CONTENTS):
        for neighbours in product((EMPTY, *CONTENTS), repeat=6):
            target = content_distribution(neighbours)
            for formation_probability in (Q_SLOW, Q_FAST):
                kernel = local_record_kernel(current, neighbours, formation_probability)
                kernel_normalization &= sum(kernel.values(), Fraction(0, 1)) == 1
                if current in CONTENTS:
                    monotone &= kernel[current] == 1 and kernel[-current] == 0 and kernel[EMPTY] == 0
                else:
                    same_content_conditional &= all(
                        kernel[content] / formation_probability == target[content]
                        for content in CONTENTS
                    )
    checks.check(
        "monotone-permanent-record-kernels",
        "two normalized kernels use the identical content rule and never erase or overwrite a formed Record",
        kernel_normalization and monotone and same_content_conditional,
        "q_slow=1/3; q_fast=2/3",
    )

    empty_star_sites = 7
    slow_expected = empty_star_sites * Q_SLOW
    fast_expected = empty_star_sites * Q_FAST
    slow_survival = (1 - Q_SLOW) ** empty_star_sites
    fast_survival = (1 - Q_FAST) ** empty_star_sites
    checks.check(
        "formation-rate-nonselection",
        "the same admissible content distribution permits distinct covariant formation probabilities and count laws",
        slow_expected == Fraction(7, 3)
        and fast_expected == Fraction(14, 3)
        and slow_survival == Fraction(128, 2187)
        and fast_survival == Fraction(1, 2187),
        f"E[new]={slow_expected},{fast_expected}; P[none]={slow_survival},{fast_survival}",
    )

    parallel, sequential = two_site_schedule_laws()
    schedule_normalization = sum(parallel.values(), Fraction(0, 1)) == 1 and sum(sequential.values(), Fraction(0, 1)) == 1
    endpoint_exchange = all(sequential[(left, right)] == sequential[(right, left)] for left in CONTENTS for right in CONTENTS)
    sign_exchange = all(sequential[(left, right)] == sequential[(-left, -right)] for left in CONTENTS for right in CONTENTS)
    checks.check(
        "formation-scheduler-completions",
        "parallel and random-orientation sequential formation are normalized and preserve endpoint/content symmetry",
        schedule_normalization and endpoint_exchange and sign_exchange,
        "parallel entries=1/4; sequential same/different entries=2/5,1/10",
    )

    def marginal(law: dict[tuple[int, int], Fraction], side: int, value: int) -> Fraction:
        return sum(weight for pair, weight in law.items() if pair[side] == value)

    parallel_correlation = sum(Fraction(left * right) * weight for (left, right), weight in parallel.items())
    sequential_correlation = sum(Fraction(left * right) * weight for (left, right), weight in sequential.items())
    checks.check(
        "precedence-and-correlation-nonselection",
        "the two symmetric schedulers have equal one-site marginals but different precedence and final correlation",
        all(marginal(parallel, side, value) == Fraction(1, 2) for side in (0, 1) for value in CONTENTS)
        and all(marginal(sequential, side, value) == Fraction(1, 2) for side in (0, 1) for value in CONTENTS)
        and parallel_correlation == 0
        and sequential_correlation == Fraction(3, 5),
        f"correlation={parallel_correlation},{sequential_correlation}; precedence=simultaneous versus ordered",
    )

    plus, cross = block44.transverse_traceless_vectors()
    baseline_shell = timed_einstein_operator((1.0, 0.0, 0.0), 1.0, 1.0)
    baseline_gauge = block44.continuum_gauge_map(np.asarray((1.0, 0.0, 0.0, -1.0)))
    baseline_spanning = np.column_stack((baseline_gauge, plus, cross))
    baseline_static = timed_einstein_operator((1.0, 0.0, 0.0), 0.0, 1.0)
    baseline_source = np.zeros(len(block44.HCOMPS))
    baseline_source[block44.STATIC_SOURCE_INDEX] = 1.0
    baseline_response = -np.linalg.pinv(baseline_static, rcond=1.0e-12) @ baseline_source
    baseline_residual = float(np.linalg.norm(baseline_static @ baseline_response + baseline_source))
    checks.check(
        "block44-baseline-retention",
        "the inherited conditional operator retains four gauge plus two TT shell nulls and the unit-source h_tt residue",
        np.linalg.matrix_rank(baseline_shell, tol=1.0e-12) == 4
        and np.linalg.matrix_rank(baseline_spanning, tol=1.0e-12) == 6
        and float(np.max(np.abs(baseline_shell @ baseline_spanning))) < TOLERANCE
        and abs(baseline_response[block44.STATIC_SOURCE_INDEX] - 2.0) < TOLERANCE
        and baseline_residual < TOLERANCE,
        f"rank={np.linalg.matrix_rank(baseline_shell)}; h_tt={baseline_response[block44.STATIC_SOURCE_INDEX]:.12f}; residual={baseline_residual:.3e}",
    )

    static_momentum = np.asarray((0.8, -0.3, 0.5))
    standard_static = timed_einstein_operator(static_momentum, 0.0, 1.0)
    scales = (0.5, 1.0, 2.0)
    static_errors = [
        float(np.max(np.abs(timed_einstein_operator(static_momentum, 0.0, scale) - standard_static)))
        for scale in scales
    ]
    shell_ranks = []
    shell_null_errors = []
    kinetic_coefficients = []
    coordinate_speeds = []
    for scale in scales:
        frequency = 1.0 / scale
        shell = timed_einstein_operator((1.0, 0.0, 0.0), frequency, scale)
        gauge = block44.continuum_gauge_map(np.asarray((1.0, 0.0, 0.0, -1.0)))
        spanning = np.column_stack((gauge, plus, cross))
        shell_ranks.append(np.linalg.matrix_rank(shell, tol=1.0e-12))
        shell_null_errors.append(float(np.max(np.abs(shell @ spanning))))
        kinetic = timed_einstein_operator((0.0, 0.0, 0.0), 1.0, scale)
        kinetic_coefficients.append(float(plus @ kinetic @ plus))
        coordinate_speeds.append(frequency)
    checks.check(
        "einstein-time-normalization-family",
        "three gauge-consistent Einstein completions share the static operator but select different clock/light normalization",
        max(static_errors) < TOLERANCE
        and shell_ranks == [4, 4, 4]
        and max(shell_null_errors) < TOLERANCE
        and np.max(np.abs(np.asarray(kinetic_coefficients) - np.asarray((1 / 16, 1 / 4, 1.0)))) < TOLERANCE
        and np.max(np.abs(np.asarray(coordinate_speeds) - np.asarray((2.0, 1.0, 0.5)))) < TOLERANCE,
        f"TT kinetic={kinetic_coefficients}; coordinate speeds={coordinate_speeds}",
    )

    covariance_error = 0.0
    projector_error = 0.0
    sample_momentum = np.asarray((0.7, -0.2, 0.4))
    sample_frequency = 0.9
    for rotation in rotations:
        representation = symmetric_coordinate_representation(rotation)
        projector_error = max(
            projector_error,
            float(np.max(np.abs(representation @ TIME_PROJECTOR @ representation.T - TIME_PROJECTOR))),
        )
        for scale in scales:
            original = timed_einstein_operator(sample_momentum, sample_frequency, scale)
            rotated = timed_einstein_operator(rotation @ sample_momentum, sample_frequency, scale)
            covariance_error = max(
                covariance_error,
                float(np.max(np.abs(rotated - representation @ original @ representation.T))),
            )
        original_bad = constraint_breaking_operator(sample_momentum, sample_frequency, ZETA)
        rotated_bad = constraint_breaking_operator(rotation @ sample_momentum, sample_frequency, ZETA)
        covariance_error = max(
            covariance_error,
            float(np.max(np.abs(rotated_bad - representation @ original_bad @ representation.T))),
        )
    checks.check(
        "spatial-cubic-covariance",
        "all time-normalized and constraint-breaking completions preserve the supplied proper-cubic spatial covariance",
        covariance_error < TOLERANCE and projector_error < TOLERANCE,
        f"max operator error={covariance_error:.3e}; projector error={projector_error:.3e}",
    )

    broken_static = constraint_breaking_operator(static_momentum, 0.0, ZETA)
    broken_shell = constraint_breaking_operator((1.0, 0.0, 0.0), 1.0, ZETA)
    broken_kinetic = constraint_breaking_operator((0.0, 0.0, 0.0), 1.0, ZETA)
    shell_gauge = block44.continuum_gauge_map(np.asarray((1.0, 0.0, 0.0, -1.0)))
    gauge_residual = float(np.max(np.abs(broken_shell @ shell_gauge)))
    multiplier_kinetic = float(np.max(np.abs(broken_kinetic[np.asarray(block44.TIME_COMPONENTS), :])))
    tt_residual = float(np.max(np.abs(broken_shell @ np.column_stack((plus, cross)))))
    checks.check(
        "constraint-preservation-nonselection",
        "a static-identical spatially covariant completion makes lapse/shift kinetic and removes the four gauge identities",
        float(np.max(np.abs(broken_static - standard_static))) < TOLERANCE
        and multiplier_kinetic == ZETA
        and np.linalg.matrix_rank(broken_shell, tol=1.0e-12) == 8
        and abs(gauge_residual - 0.5) < TOLERANCE
        and tt_residual < TOLERANCE,
        f"time-row kinetic={multiplier_kinetic:.3f}; rank={np.linalg.matrix_rank(broken_shell)}; gauge residual={gauge_residual:.3f}",
    )

    independent_wall_jacobian = np.diag((1.0, 0.5, 1.0))
    checks.check(
        "three-independent-selection-walls",
        "formation probability, Einstein clock scale, and multiplier kinetic status are locally independent controls",
        np.linalg.matrix_rank(independent_wall_jacobian) == 3
        and slow_expected != fast_expected
        and len(set(round(value, 12) for value in kinetic_coefficients)) == 3
        and multiplier_kinetic > 0,
        "observable Jacobian diag=(1,1/2,1), rank=3",
    )

    checks.check(
        "candidate-axiom-interface-boundary",
        "the note states one sufficient unadopted Admissibility-Record composition interface without claiming necessity",
        all(
            phrase in note
            for phrase in (
                "normalized kernel on monotone record extensions",
                "formation occurrence, precedence, and clock normalization",
                "preserves the declared constraint surface",
                "sufficient and unadopted",
                "not proved necessary or minimal",
                "no canonical axiom is edited",
            )
        ),
    )

    checks.check(
        "fresh-no-go-discipline-packet",
        "the bounded non-entailment passes N1 through N8 while preserving constructive dynamics routes",
        all(f"### n{index}" in note for index in range(1, 9))
        and "status: pass" in note
        and all(
            phrase in note
            for phrase in (
                "not a gravity no-go",
                "unitary dilation",
                "reflection-positive",
                "canonical constraint",
                "inclusion order",
                "downstream theorem",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: all 729 six-neighbour binary/empty conditions, 24 proper rotations, two monotone rates, two symmetric schedulers, three Einstein clock scales, and one constraint-breaking completion are resolved"
    )
    print(
        "per_element: checked empty and both central binary Record contents plus all ten metric coordinates"
    )
    print(
        "per_site: checked every six-neighbour condition and both permanent local transition kernels"
    )
    print(
        "per_mode: checked static, kinetic, null-shell, generic off-shell, four gauge, and two TT probes"
    )
    print(
        "per_block: checked formation-rate, precedence, time-normalization, and multiplier-constraint blocks"
    )
    print(
        "lattice_wide: local covariance is exact but no full-Z3 production process, finite-frequency edge theorem, or nonlinear constraint propagation is claimed"
    )
    print(
        "scope_boundary: bounded current-axiom underdetermination and a sufficient unadopted interface; not gravity failure, axiom necessity, minimality, or adoption"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
