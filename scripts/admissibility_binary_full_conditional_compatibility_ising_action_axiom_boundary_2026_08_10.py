#!/usr/bin/env python3
"""Exact finite checks for binary conditional compatibility and action recovery."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Config = tuple[int, ...]
OddsTable = dict[tuple[int, Config], Fraction]
Matrix3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

NEIGHBOR_DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
IDENTITY_MATRIX: Matrix3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def flip(configuration: Config, site: int) -> Config:
    changed = list(configuration)
    changed[site] = 1 - changed[site]
    return tuple(changed)


def zero_at(configuration: Config, site: int) -> Config:
    changed = list(configuration)
    changed[site] = 0
    return tuple(changed)


def probability_from_odds(value: Fraction) -> Fraction:
    return value / (1 + value)


def odds_from_weights(weights: dict[Config, Fraction]) -> OddsTable:
    table: OddsTable = {}
    for configuration in weights:
        for site in range(len(configuration)):
            base = zero_at(configuration, site)
            table[(site, base)] = weights[flip(base, site)] / weights[base]
    return table


def square_residuals(site_count: int, odds: OddsTable) -> tuple[Fraction, ...]:
    residuals: list[Fraction] = []
    for left, right in combinations(range(site_count), 2):
        other_sites = tuple(
            site for site in range(site_count) if site not in (left, right)
        )
        for exterior in product((0, 1), repeat=len(other_sites)):
            base_list = [0] * site_count
            for site, value in zip(other_sites, exterior):
                base_list[site] = value
            base = tuple(base_list)
            left_then_right = odds[(left, base)] * odds[(right, flip(base, left))]
            right_then_left = odds[(right, base)] * odds[(left, flip(base, right))]
            residuals.append(left_then_right - right_then_left)
    return tuple(residuals)


def monotone_path_ratio(
    target: Config, order: tuple[int, ...], odds: OddsTable
) -> Fraction:
    current = tuple(0 for _ in target)
    ratio = Fraction(1)
    for site in order:
        if target[site] != 1:
            raise ValueError("path order may contain only target-one sites")
        ratio *= odds[(site, current)]
        current = flip(current, site)
    if current != target:
        raise ValueError("path order does not reach target")
    return ratio


def recover_weights(site_count: int, odds: OddsTable) -> dict[Config, Fraction]:
    recovered: dict[Config, Fraction] = {}
    for configuration in product((0, 1), repeat=site_count):
        sites = tuple(index for index, value in enumerate(configuration) if value)
        paths = {
            monotone_path_ratio(configuration, order, odds)
            for order in permutations(sites)
        }
        if len(paths) != 1:
            raise ValueError("conditional odds are path-dependent")
        recovered[configuration] = paths.pop()
    return recovered


def normalize(weights: dict[Config, Fraction]) -> dict[Config, Fraction]:
    total = sum(weights.values(), Fraction(0))
    return {configuration: value / total for configuration, value in weights.items()}


def matrix_rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    matrix = [row[:] for row in rows]
    row_count = len(matrix)
    column_count = len(matrix[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if matrix[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / scale for entry in matrix[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def count_logit_constraint_rows() -> list[list[Fraction]]:
    rows: list[list[Fraction]] = []
    for left_count in range(6):
        for right_count in range(left_count + 1, 6):
            row = [Fraction(0) for _ in range(7)]
            row[left_count + 1] += 1
            row[left_count] -= 1
            row[right_count + 1] -= 1
            row[right_count] += 1
            rows.append(row)
    return rows


def dot(left: list[Fraction], right: list[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def determinant(matrix: Matrix3) -> int:
    return (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def matrix_vector(matrix: Matrix3, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def matrix_product(left: Matrix3, right: Matrix3) -> Matrix3:
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def signed_permutation_matrices(determinant_target: int) -> tuple[Matrix3, ...]:
    matrices: set[Matrix3] = set()
    for axes in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            matrix: Matrix3 = tuple(
                tuple(signs[row] if column == axes[row] else 0 for column in range(3))
                for row in range(3)
            )  # type: ignore[assignment]
            if determinant(matrix) == determinant_target:
                matrices.add(matrix)
    return tuple(sorted(matrices))


def neighbor_permutation(matrix: Matrix3) -> tuple[int, ...]:
    return tuple(
        NEIGHBOR_DIRECTIONS.index(matrix_vector(matrix, vector))
        for vector in NEIGHBOR_DIRECTIONS
    )


def rotation_certificate(matrices: tuple[Matrix3, ...]) -> bool:
    matrix_set = set(matrices)
    return (
        len(matrices) == 24
        and IDENTITY_MATRIX in matrix_set
        and all(determinant(matrix) == 1 for matrix in matrices)
        and all(
            set(matrix_vector(matrix, vector) for vector in NEIGHBOR_DIRECTIONS)
            == set(NEIGHBOR_DIRECTIONS)
            for matrix in matrices
        )
        and all(
            matrix_product(left, right) in matrix_set
            for left in matrices
            for right in matrices
        )
    )


def permute_pattern(
    pattern: tuple[int, ...], permutation: tuple[int, ...]
) -> tuple[int, ...]:
    output = [0] * 6
    for source, target in enumerate(permutation):
        output[target] = pattern[source]
    return tuple(output)


def two_site_action_weights(
    field_odds: Fraction,
    coupling_odds: Fraction,
    left_external_count: int,
    right_external_count: int,
) -> dict[Config, Fraction]:
    weights: dict[Config, Fraction] = {}
    for left, right in product((0, 1), repeat=2):
        occupied = left + right
        active_edges = (
            left * right
            + left_external_count * left
            + right_external_count * right
        )
        weights[(left, right)] = (
            field_odds**occupied * coupling_odds**active_edges
        )
    return weights


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
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())

    print(
        "external_scientific_inputs: empty; all finite compatibility and action "
        "calculations are derived with exact rational arithmetic"
    )
    print(
        "analytic_scope: finite nonempty-site strictly positive binary "
        "full-conditionals; "
        "count-only dependence for the cubic classification"
    )

    checks.check(
        "source-current-axiom",
        "the current source retains the nearest-neighbor one-site distribution",
        all(
            phrase in axiom_flat
            for phrase in (
                "There is one fixed nearest-neighbor admissibility rule",
                "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions",
            )
        ),
    )

    site_count = 4
    arbitrary_weights = {
        configuration: Fraction(
            2
            + 3 * configuration[0]
            + 5 * configuration[1]
            + 7 * configuration[2]
            + 11 * configuration[3]
            + 13 * configuration[0] * configuration[1]
            + 17 * configuration[2] * configuration[3]
            + 19 * configuration[0] * configuration[2] * configuration[3]
        )
        for configuration in product((0, 1), repeat=site_count)
    }
    compatible_odds = odds_from_weights(arbitrary_weights)
    checks.check(
        "general-square-necessity",
        "all 24 distinct square contexts close for an independent positive four-site weight",
        len(square_residuals(site_count, compatible_odds)) == 24
        and all(
            residual == 0
            for residual in square_residuals(site_count, compatible_odds)
        ),
    )
    recovered = recover_weights(site_count, compatible_odds)
    recovered_law = normalize(recovered)
    original_law = normalize(arbitrary_weights)
    checks.check(
        "general-path-reconstruction",
        "every monotone path reconstructs the original weights up to one common scale",
        all(
            recovered[configuration]
            == arbitrary_weights[configuration] / arbitrary_weights[(0,) * site_count]
            for configuration in recovered
        ),
    )
    checks.check(
        "general-normalized-uniqueness",
        "normalization recovers the unique positive joint law",
        recovered_law == original_law
        and sum(recovered_law.values(), Fraction(0)) == 1,
    )
    checks.check(
        "general-full-conditionals",
        "the recovered joint law reproduces every supplied one-site conditional",
        all(
            recovered_law[flip(base, site)]
            / (recovered_law[base] + recovered_law[flip(base, site)])
            == probability_from_odds(compatible_odds[(site, base)])
            for base in recovered_law
            for site in range(site_count)
            if base[site] == 0
        ),
    )

    mutated_odds = dict(compatible_odds)
    mutated_key = (0, (0, 0, 0, 0))
    mutated_odds[mutated_key] *= 2
    mutated_residuals = square_residuals(site_count, mutated_odds)
    target = (1, 1, 0, 0)
    mutated_paths = {
        monotone_path_ratio(target, order, mutated_odds)
        for order in permutations((0, 1))
    }
    checks.check(
        "single-odds-mutation",
        "one exact odds mutation creates square curl and path disagreement",
        any(residual != 0 for residual in mutated_residuals)
        and len(mutated_paths) == 2,
    )

    constraint_rows = count_logit_constraint_rows()
    constant_vector = [Fraction(1) for _ in range(7)]
    linear_vector = [Fraction(index) for index in range(7)]
    checks.check(
        "cubic-count-constraint-rank",
        "the exact count system has rank five and nullity two",
        matrix_rank(constraint_rows) == 5
        and 7 - matrix_rank(constraint_rows) == 2,
    )
    checks.check(
        "cubic-count-affine-basis",
        "constant and neighbor-count vectors form an independent null-space basis",
        all(dot(row, constant_vector) == 0 for row in constraint_rows)
        and all(dot(row, linear_vector) == 0 for row in constraint_rows)
        and matrix_rank([constant_vector, linear_vector]) == 2,
    )

    field_odds = Fraction(1, 8)
    coupling_odds = Fraction(2)
    good_odds = tuple(field_odds * coupling_odds**count for count in range(7))
    good_probabilities = tuple(probability_from_odds(value) for value in good_odds)
    checks.check(
        "compatible-cubic-rule",
        "the exact fixture has geometric positive odds and genuine count dependence",
        tuple(
            good_odds[index + 1] / good_odds[index] for index in range(6)
        )
        == (coupling_odds,) * 6
        and all(Fraction(0) < value < Fraction(1) for value in good_probabilities)
        and len(set(good_probabilities)) == 7,
    )
    checks.check(
        "compatible-code-swap-symmetry",
        "the fixture obeys q(6-k)=1-q(k) and A B^3=1",
        all(
            good_probabilities[6 - count] == 1 - good_probabilities[count]
            for count in range(7)
        )
        and field_odds * coupling_odds**3 == 1,
    )

    proper_rotations = signed_permutation_matrices(1)
    improper_mutation = signed_permutation_matrices(-1)
    proper_permutations = tuple(
        neighbor_permutation(matrix) for matrix in proper_rotations
    )
    checks.check(
        "proper-cubic-group",
        "the exact determinant-one matrices form all 24 proper cubic rotations",
        rotation_certificate(proper_rotations)
        and len(set(proper_permutations)) == 24,
    )
    checks.check(
        "proper-orientation-mutation-control",
        "the determinant-minus-one signed-permutation family fails the properness certificate",
        len(improper_mutation) == 24
        and set(proper_rotations).isdisjoint(improper_mutation)
        and not rotation_certificate(improper_mutation),
    )
    checks.check(
        "count-rule-covariance",
        "all 64 neighbor patterns preserve occupied count under all 24 proper rotations",
        all(
            sum(pattern) == sum(permute_pattern(pattern, rotation))
            and good_probabilities[sum(pattern)]
            == good_probabilities[sum(permute_pattern(pattern, rotation))]
            for pattern in product((0, 1), repeat=6)
            for rotation in proper_permutations
        ),
    )

    action_checks: list[bool] = []
    normalized_checks: list[bool] = []
    for left_external_count in range(6):
        for right_external_count in range(6):
            weights = two_site_action_weights(
                field_odds,
                coupling_odds,
                left_external_count,
                right_external_count,
            )
            odds = odds_from_weights(weights)
            action_checks.extend(
                odds[(0, (0, right))]
                == good_odds[left_external_count + right]
                for right in (0, 1)
            )
            action_checks.extend(
                odds[(1, (left, 0))]
                == good_odds[right_external_count + left]
                for left in (0, 1)
            )
            law = normalize(weights)
            normalized_checks.append(
                all(value > 0 for value in law.values())
                and sum(law.values(), Fraction(0)) == 1
            )
    checks.check(
        "finite-action-conditionals",
        "the action recovers all 144 endpoint conditionals across 36 exterior-count pairs",
        len(action_checks) == 144 and all(action_checks),
    )
    checks.check(
        "finite-action-normalization",
        "all 36 two-site boundary-count laws are positive and normalized",
        len(normalized_checks) == 36 and all(normalized_checks),
    )

    checks.check(
        "source-theorem-surface",
        "the note states both exact equivalences and the finite action formula",
        all(
            phrase in note_flat
            for phrase in (
                "claim_scope: \"For strictly positive binary full-conditionals on a finite nonempty set of sites",
                "**Scope:** finite nonempty-site strictly positive binary full-conditionals",
                "Let `V` be a finite nonempty set of binary sites",
                "Let `V` be a finite nonempty set of sites",
                "The certified object is the finite nonempty-site probability theorem",
                "For strictly positive binary full-conditionals on a finite nonempty site set",
                "r_i(x) r_j(x^i) = r_j(x) r_i(x^j)",
                "o_k = A B^k",
                "q(k) = A B^k/(1+A B^k)",
                "pi_Lambda(x|b) = Z_Lambda(b)^(-1)",
                "A B^3 = 1",
            )
        ),
    )
    checks.check(
        "source-governance-surface",
        "the note carries the controlled claim, status, trace, and audit-boundary fields",
        all(
            phrase in note
            for phrase in (
                "claim_type: bounded_theorem",
                "**Type:** bounded_theorem",
                "**Status:** proposed_retained",
                "actual_current_surface_status: candidate-retained-grade",
                "trace_class: frontier_discovery",
                "reachability_to_target: unknown_frontier",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "source-salvage-boundary",
        "the durable source limits itself to the independently verified static theorem",
        "This salvage retains the independently verified static theorem" in note
        and "cross-region projectivity proposal" in note
        and "stochastic update interpretation" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
