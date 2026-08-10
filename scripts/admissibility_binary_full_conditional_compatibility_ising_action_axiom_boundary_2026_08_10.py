#!/usr/bin/env python3
"""Exact finite checks for local conditional compatibility and action recovery.

The source note proves the finite binary square-curl theorem. This runner
checks its constructive fixtures, the seven-point cubic count classification,
the exact compatible and incompatible covariant rules, and source boundaries.
"""

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
LOCAL_MEASURE_PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
GLOBAL_HISTORY_PARENT_PATH = ROOT / "docs" / "work_history" / "repo" / (
    "review_feedback/GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md"
)
SOURCE_ACTION_PARENT_PATH = ROOT / "docs" / (
    "SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/work_history/repo/review_feedback/GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md",
    "docs/SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)


Config = tuple[int, ...]
OddsTable = dict[tuple[int, Config], Fraction]


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


def odds_from_probability(value: Fraction) -> Fraction:
    return value / (1 - value)


def odds_from_weights(weights: dict[Config, Fraction]) -> OddsTable:
    table: OddsTable = {}
    for configuration in weights:
        for site in range(len(configuration)):
            base = zero_at(configuration, site)
            table[(site, base)] = weights[flip(base, site)] / weights[base]
    return table


def square_residuals(site_count: int, odds: OddsTable) -> tuple[Fraction, ...]:
    residuals: list[Fraction] = []
    for configuration in product((0, 1), repeat=site_count):
        for left, right in combinations(range(site_count), 2):
            base_list = list(configuration)
            base_list[left] = 0
            base_list[right] = 0
            base = tuple(base_list)
            left_then_right = odds[(left, base)] * odds[(right, flip(base, left))]
            right_then_left = odds[(right, base)] * odds[(left, flip(base, right))]
            residuals.append(left_then_right - right_then_left)
    return tuple(residuals)


def monotone_path_ratio(target: Config, order: tuple[int, ...], odds: OddsTable) -> Fraction:
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
            raise ValueError("conditional odds are not path independent")
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
            (row for row in range(pivot_row, row_count) if matrix[row][column]),
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


NEIGHBOR_DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def permutation_parity(values: tuple[int, int, int]) -> int:
    inversions = sum(
        values[left] > values[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_neighbor_permutations() -> tuple[tuple[int, ...], ...]:
    rotations: set[tuple[int, ...]] = set()
    for axes in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            determinant = permutation_parity(axes) * signs[0] * signs[1] * signs[2]
            if determinant != 1:
                continue
            images = []
            for vector in NEIGHBOR_DIRECTIONS:
                transformed = tuple(signs[row] * vector[axes[row]] for row in range(3))
                images.append(NEIGHBOR_DIRECTIONS.index(transformed))
            rotations.add(tuple(images))
    return tuple(sorted(rotations))


def permute_pattern(pattern: tuple[int, ...], neighbor_permutation: tuple[int, ...]) -> tuple[int, ...]:
    output = [0] * 6
    for source, target in enumerate(neighbor_permutation):
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
    local_measure_parent = LOCAL_MEASURE_PARENT_PATH.read_text(encoding="utf-8")
    global_history_parent = GLOBAL_HISTORY_PARENT_PATH.read_text(encoding="utf-8")
    source_action_parent = SOURCE_ACTION_PARENT_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    global_history_flat = " ".join(global_history_parent.split())

    print("external_scientific_inputs: none; the finite binary compatibility theorem and cubic count classification are proved in-source from exact conditional odds")
    print("package_local_integrity_reads: current axioms and three explicit local-measure, global-history, and source-action boundaries are source-bound")
    print("analytic_boundary: square-generation of monotone hypercube paths and the all-environment cubic classification are proved generally; exact rational fixtures are executed")
    print("negative_scope: local normalization and covariance alone do not force static full-conditional compatibility; no axiom inconsistency, global-law impossibility, or gravity no-go is claimed")

    checks.check(
        "source-current-axiom",
        "the one-site distribution, nearest-neighbor determination, covariance, and nondynamics clauses are present",
        all(
            phrase in axiom_flat
            for phrase in (
                "There is one fixed nearest-neighbor admissibility rule",
                "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions",
                "Admissibility is not a dynamics axiom.",
                "a record locks exactly one admissible local possibility",
            )
        ),
    )
    clean_local_parent = local_measure_parent.replace(chr(96), "")
    checks.check(
        "source-local-measure-parent",
        "the preceding local measure is typed on one M2 possibility domain",
        "current Admissibility measure mu_eta" in clean_local_parent
        and "measurable subsets of all point possibilities X" in clean_local_parent,
    )
    checks.check(
        "source-global-history-parent",
        "the existing process-law corpus keeps projective consistency explicit",
        "projective consistency" in global_history_flat
        and "complete record protocols" in global_history_flat,
    )
    checks.check(
        "source-action-parent",
        "the gravity source-action identification remains explicitly open",
        "readout-to-action / source-action identification is an OPEN bridge" in source_action_parent
        and "The axioms alone do NOT force" in source_action_parent,
    )

    site_count = 4
    arbitrary_weights = {
        configuration: Fraction(
            1
            + sum((index + 2) * value for index, value in enumerate(configuration))
            + 3 * configuration[0] * configuration[2]
            + 5 * configuration[1] * configuration[3]
        )
        for configuration in product((0, 1), repeat=site_count)
    }
    compatible_odds = odds_from_weights(arbitrary_weights)
    residuals = square_residuals(site_count, compatible_odds)
    checks.check(
        "general-square-necessity",
        "all exact square curls vanish for conditionals derived from an arbitrary positive four-site joint law",
        residuals and all(residual == 0 for residual in residuals),
    )
    recovered = recover_weights(site_count, compatible_odds)
    base_weight = arbitrary_weights[(0, 0, 0, 0)]
    checks.check(
        "general-path-reconstruction",
        "path integration recovers every arbitrary joint weight up to the unique common scale",
        all(
            recovered[configuration]
            == arbitrary_weights[configuration] / base_weight
            for configuration in arbitrary_weights
        ),
    )
    recovered_law = normalize(recovered)
    original_law = normalize(arbitrary_weights)
    checks.check(
        "general-normalized-uniqueness",
        "normalization removes the common scale and reproduces the unique positive joint law",
        recovered_law == original_law and sum(recovered_law.values()) == 1,
    )
    checks.check(
        "general-full-conditionals",
        "every recovered one-site conditional probability equals its supplied odds conversion",
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
    checks.check(
        "single-kernel-mutation",
        "one exact local-odds mutation creates nonzero square curl",
        any(residual != 0 for residual in mutated_residuals),
    )
    target = (1, 1, 0, 0)
    mutated_paths = {
        monotone_path_ratio(target, order, mutated_odds)
        for order in permutations((0, 1))
    }
    checks.check(
        "path-dependence-control",
        "the same mutation makes two orders from 00 to 11 disagree",
        len(mutated_paths) == 2,
    )

    constraint_rows = count_logit_constraint_rows()
    constant_vector = [Fraction(1) for _ in range(7)]
    linear_vector = [Fraction(index) for index in range(7)]
    checks.check(
        "cubic-count-constraint-rank",
        "the exact all-environment first-difference constraints have rank five and nullity two",
        matrix_rank(constraint_rows) == 5 and 7 - matrix_rank(constraint_rows) == 2,
    )
    checks.check(
        "cubic-count-affine-basis",
        "constant and neighbor-count vectors are independent null vectors and therefore span every compatible logit",
        all(dot(row, constant_vector) == 0 for row in constraint_rows)
        and all(dot(row, linear_vector) == 0 for row in constraint_rows)
        and matrix_rank([constant_vector, linear_vector]) == 2,
    )

    good_odds = tuple(Fraction(2**count, 8) for count in range(7))
    good_probabilities = tuple(probability_from_odds(value) for value in good_odds)
    good_ratios = tuple(
        good_odds[index + 1] / good_odds[index] for index in range(6)
    )
    checks.check(
        "compatible-cubic-rule",
        "the exact rule has geometric odds 2^(k-3), affine logit, full support, and genuine neighbor variation",
        good_ratios == (Fraction(2),) * 6
        and all(Fraction(0) < value < Fraction(1) for value in good_probabilities)
        and len(set(good_probabilities)) == 7,
    )
    checks.check(
        "compatible-code-swap-symmetry",
        "the compatible fixture obeys q(6-k)=1-q(k) and q(3)=1/2",
        all(
            good_probabilities[6 - count] == 1 - good_probabilities[count]
            for count in range(7)
        )
        and good_probabilities[3] == Fraction(1, 2),
    )

    bad_probabilities = (
        Fraction(1, 8),
        Fraction(1, 4),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(3, 4),
        Fraction(7, 8),
    )
    bad_odds = tuple(odds_from_probability(value) for value in bad_probabilities)
    bad_ratios = tuple(
        bad_odds[index + 1] / bad_odds[index] for index in range(6)
    )
    checks.check(
        "hostile-local-rule-strength",
        "the hostile rule is normalized, strictly positive, count-varying, monotone, and code-swap symmetric",
        all(Fraction(0) < value < Fraction(1) for value in bad_probabilities)
        and all(
            bad_probabilities[index] < bad_probabilities[index + 1]
            for index in range(6)
        )
        and all(
            bad_probabilities[6 - count] == 1 - bad_probabilities[count]
            for count in range(7)
        ),
    )
    checks.check(
        "hostile-nongeometric-odds",
        "its exact successive odds ratios are not constant",
        bad_odds
        == (
            Fraction(1, 7),
            Fraction(1, 3),
            Fraction(1, 2),
            Fraction(1),
            Fraction(2),
            Fraction(3),
            Fraction(7),
        )
        and len(set(bad_ratios)) > 1,
    )
    bad_left_then_right = bad_odds[0] * bad_odds[2]
    bad_right_then_left = bad_odds[1] * bad_odds[1]
    checks.check(
        "hostile-square-witness",
        "independent exterior counts a=0,b=1 give path products 1/14 and 1/9, so no positive joint law has these as full conditionals",
        bad_left_then_right == Fraction(1, 14)
        and bad_right_then_left == Fraction(1, 9)
        and bad_left_then_right != bad_right_then_left,
    )

    rotations = proper_cubic_neighbor_permutations()
    checks.check(
        "proper-cubic-group",
        "the exact signed-permutation construction produces all 24 proper cubic neighbor permutations",
        len(rotations) == 24 and all(sorted(rotation) == list(range(6)) for rotation in rotations),
    )
    checks.check(
        "count-rule-covariance",
        "every one of 64 neighbor patterns keeps its good and hostile probabilities under all 24 proper cubic rotations",
        all(
            sum(pattern) == sum(permute_pattern(pattern, rotation))
            and good_probabilities[sum(pattern)]
            == good_probabilities[sum(permute_pattern(pattern, rotation))]
            and bad_probabilities[sum(pattern)]
            == bad_probabilities[sum(permute_pattern(pattern, rotation))]
            for pattern in product((0, 1), repeat=6)
            for rotation in rotations
        ),
    )

    good_two_site_weights = two_site_action_weights(
        field_odds=Fraction(1, 8),
        coupling_odds=Fraction(2),
        left_external_count=0,
        right_external_count=1,
    )
    good_two_site_odds = odds_from_weights(good_two_site_weights)
    checks.check(
        "ising-action-conditionals",
        "the exact finite action A^(sum x)B^(active edges) reproduces q(a+y) and q(b+x) on both sites",
        all(
            good_two_site_odds[(0, (0, right))]
            == good_odds[right]
            for right in (0, 1)
        )
        and all(
            good_two_site_odds[(1, (left, 0))]
            == good_odds[1 + left]
            for left in (0, 1)
        ),
    )
    good_left_then_right = good_odds[0] * good_odds[2]
    good_right_then_left = good_odds[1] * good_odds[1]
    checks.check(
        "ising-action-square",
        "the compatible fixture gives the same exact 1/16 ratio along both update orders",
        good_left_then_right
        == good_right_then_left
        == Fraction(1, 16),
    )
    good_two_site_law = normalize(good_two_site_weights)
    checks.check(
        "ising-action-normalization",
        "the derived two-site finite-volume law is positive and normalized",
        all(value > 0 for value in good_two_site_law.values())
        and sum(good_two_site_law.values()) == 1,
    )

    construction_needles = (
        "r_i(x) r_j(x^i)=r_j(x) r_i(x^j)",
        "o_k=A B^k",
        "q(k)=A B^k/(1+A B^k)",
        "pi_Lambda(x|b)=Z_Lambda(b)^(-1)",
        "1/14",
        "1/9",
        "whose one-site full conditional measures are the sitewise",
        "projectively consistent family",
    )
    checks.check(
        "construction-source-surface",
        "the source states the square criterion, cubic classification, action, hostile witness, and candidate compatibility clause",
        all(phrase in note_flat for phrase in construction_needles),
    )
    boundary_needles = (
        "No canonical axiom is edited",
        "the fixed TOE percentages do not move",
        "No axiom inconsistency, global-law impossibility, or gravity no-go is claimed",
        "update-kernel reading",
        "hypothetical wording only",
    )
    checks.check(
        "boundary-source-surface",
        "the source preserves governance, percentage, semantic-alternative, and global-negative limits",
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
                "next_trace_action:",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the compatibility, projective joint-law, and Ising-action wording is absent from the canonical memo",
        all(
            phrase not in axiom
            for phrase in (
                "square-curl",
                "compatible full conditionals",
                "projectively consistent joint law",
                "projectively consistent family",
                "Ising action",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections, source matching, primitive scan, accepted steelman, and broad-negative rejection are visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "| Source location | Exact residual used |" in note
        and "The primitive-registry scan used" in note
        and "This steelman is accepted" in note
        and "FAIL / DO NOT SHIP" in note
        and "No axiom inconsistency, global-law impossibility, or gravity no-go is claimed" in note_flat,
    )

    print("per_element: seven exact conditional probabilities, their odds, six first differences, and both two-path products are checked")
    print("per_site: a binary central M2 code has one normalized full-support conditional law for each neighbor count")
    print("per_mode: general four-site reconstruction, compatible geometric odds, hostile symmetric odds, and a one-entry mutation are separated")
    print("per_block: local conditionals -> square compatibility -> unique finite joint law -> cubic Ising-type action is checked")
    print("lattice_wide: covariance is checked over all 24 proper cubic rotations; infinite-volume existence, dynamics, formation order, realized history, and gravity identification are not executed")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
