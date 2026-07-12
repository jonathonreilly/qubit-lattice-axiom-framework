#!/usr/bin/env python3
"""Exact two-completion certificate for the PMNS minimum-information gate.

The load-bearing claim is deliberately narrow: the current supplied premises
(four axioms and three approved primitives) do not entail the adopted rule

    minimize I_seed subject to eta_{i_*} / eta_obs = 1.

This runner does not try to infer an audit verdict.  It checks the hypotheses
used by the note's model-theoretic proof and constructs explicit conservative
completions of one unchanged explicit base-model witness.  The completions obey the
framework's state-neutral, total, single-valued law qualification but select
different sources, modality weights, favored columns, or closure anchors.

Only the Python standard library is used.  The old numerical optimizer remains
available as the separate conditional diagnostic
``frontier_dm_leptogenesis_pmns_mininfo_source_law.py``.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
import math
from pathlib import Path
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PRIMITIVE_PATHS = (
    ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)
NOTE_PATH = (
    ROOT
    / "docs"
    / "DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_CURRENT_BASELINE_NON_ENTAILMENT_NO_GO_NOTE_2026-07-12.md"
)

PASS_COUNT = 0
FAIL_COUNT = 0
XBAR_NE = 0.5633333333333334
YBAR_NE = 0.30666666666666664


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {name}{suffix}")


def argmin_unique(values: dict[str, float]) -> str:
    ordered = sorted(values.items(), key=lambda item: (item[1], item[0]))
    if len(ordered) < 2 or math.isclose(ordered[0][1], ordered[1][1], abs_tol=1e-14):
        raise ValueError("minimum is not unique")
    return ordered[0][0]


def kl_to_uniform(p: tuple[float, float, float]) -> float:
    if not math.isclose(sum(p), 1.0, abs_tol=1e-14):
        raise ValueError("distribution is not normalized")
    if min(p) <= 0.0:
        raise ValueError("distribution is not strictly positive")
    return sum(value * math.log(3.0 * value) for value in p)


def positive_three_distribution_with_kl(target: float) -> tuple[float, float, float]:
    """Solve KL((1/3+t,1/3-t,1/3)||uniform)=target by bisection.

    On 0 <= t < 1/3 this KL is continuous and strictly increasing.  The two
    targets used below are far inside its range.  Bisection is independent of
    the selector comparison and is used only to construct real simplex points.
    """

    lo = 0.0
    hi = (1.0 / 3.0) - 1e-12
    hi_value = kl_to_uniform((1.0 / 3.0 + hi, 1.0 / 3.0 - hi, 1.0 / 3.0))
    if not (0.0 < target < hi_value):
        raise ValueError("target outside the positive one-parameter KL range")
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        p = (1.0 / 3.0 + mid, 1.0 / 3.0 - mid, 1.0 / 3.0)
        if kl_to_uniform(p) < target:
            lo = mid
        else:
            hi = mid
    t = 0.5 * (lo + hi)
    return (1.0 / 3.0 + t, 1.0 / 3.0 - t, 1.0 / 3.0)


@dataclass(frozen=True)
class BaseModelWitness:
    """Schematic data of one explicit model used by both completions.

    The infinite ``Z^3`` construction and spectral-rule proof live in the
    source note.  These fields make the shared reduct explicit in the finite
    certificate; Parts 1 and 2 verify its local algebra, covariance, record,
    and law conditions rather than pretending to instantiate an infinite
    lattice in memory.
    """

    sites: str
    nearest_neighbor_offsets: tuple[tuple[int, int, int], ...]
    local_algebra: str
    admissibility_rule: str
    state_space: str
    uniform_record: str
    finite_readout: str
    base_law: str


@dataclass(frozen=True)
class SelectorCompletion:
    """A conservative downstream completion over the same base model."""

    base: BaseModelWitness
    name: str
    answer: str

    def answer_for_state(self, _state: str) -> str:
        return self.answer

    def answers(self, states: Iterable[str]) -> tuple[str, ...]:
        return tuple(self.answer_for_state(state) for state in states)


def law_is_total_single_valued_and_state_neutral(
    completion: SelectorCompletion, states: tuple[str, ...]
) -> bool:
    answers = completion.answers(states)
    return (
        completion.answer in {"q_x", "q_y"}
        and len(answers) == len(states)
        and all(answer == completion.answer for answer in answers)
    )


def permutation_sign(perm: tuple[int, int, int]) -> int:
    inversions = sum(
        perm[left] > perm[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[
    tuple[tuple[int, int, int], tuple[int, int, int]], ...
]:
    rotations = []
    for perm in permutations((0, 1, 2)):
        for signs in product((-1, 1), repeat=3):
            determinant = permutation_sign(perm) * signs[0] * signs[1] * signs[2]
            if determinant == 1:
                rotations.append((perm, signs))
    return tuple(rotations)


def rotate_vector(
    vector: tuple[int, int, int],
    rotation: tuple[tuple[int, int, int], tuple[int, int, int]],
) -> tuple[int, int, int]:
    perm, signs = rotation
    return tuple(signs[index] * vector[perm[index]] for index in range(3))


def available_from_neighbor_projectors(n_zero: int, n_one: int) -> tuple[str, ...]:
    """Evaluate the spectral rule on diagonal neighbor examples."""

    if n_zero > n_one:
        return ("P0",)
    if n_one > n_zero:
        return ("P1",)
    return ("all_rank_one_projectors",)


def record_readout(records: frozenset[int]) -> int:
    return len(records)


Matrix2 = tuple[tuple[complex, complex], tuple[complex, complex]]
ZERO2: Matrix2 = ((0j, 0j), (0j, 0j))


def matrix_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_scale(scalar: complex, matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(scalar * matrix[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(2))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_dagger(matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(matrix[column][row].conjugate() for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_close(left: Matrix2, right: Matrix2, tolerance: float = 1e-12) -> bool:
    return all(
        abs(left[row][column] - right[row][column]) < tolerance
        for row in range(2)
        for column in range(2)
    )


def rank_one_projector(vector: tuple[complex, complex]) -> Matrix2:
    norm_squared = sum(abs(entry) ** 2 for entry in vector)
    if norm_squared <= 0.0:
        raise ValueError("zero vector has no rank-one projector")
    normalized = tuple(entry / math.sqrt(norm_squared) for entry in vector)
    return tuple(
        tuple(normalized[row] * normalized[column].conjugate() for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def sum_matrices(matrices: Iterable[Matrix2]) -> Matrix2:
    total = ZERO2
    for matrix in matrices:
        total = matrix_add(total, matrix)
    return total


def top_spectral_projector(matrix: Matrix2) -> Matrix2 | None:
    """Top eigenspace projector; ``None`` denotes full degeneracy."""

    if not matrix_close(matrix, matrix_dagger(matrix)):
        raise ValueError("top_spectral_projector requires a Hermitian matrix")
    a = float(matrix[0][0].real)
    d = float(matrix[1][1].real)
    b = matrix[0][1]
    gap = math.sqrt((a - d) ** 2 + 4.0 * abs(b) ** 2)
    if gap < 1e-12:
        return None
    lambda_minus = 0.5 * (a + d - gap)
    identity: Matrix2 = ((1 + 0j, 0j), (0j, 1 + 0j))
    return matrix_scale(
        1.0 / gap,
        matrix_add(matrix, matrix_scale(-lambda_minus, identity)),
    )


def normalize_three(values: tuple[float, float, float]) -> tuple[float, float, float]:
    total = sum(values)
    if total <= 0.0:
        raise ValueError("normalization requires a positive total")
    return tuple(value / total for value in values)


def scale_three(
    distribution: tuple[float, float, float], total: float
) -> tuple[float, float, float]:
    return tuple(total * value for value in distribution)


def matrix_units() -> dict[tuple[int, int], Matrix2]:
    units: dict[tuple[int, int], Matrix2] = {}
    for unit_row in range(2):
        for unit_column in range(2):
            units[(unit_row, unit_column)] = tuple(
                tuple(
                    1.0 + 0j if (row, column) == (unit_row, unit_column) else 0j
                    for column in range(2)
                )
                for row in range(2)
            )  # type: ignore[assignment]
    return units


def part_one_language_and_scope(base: BaseModelWitness) -> None:
    print("\nPART 1: CURRENT BASELINE LANGUAGE AND SOURCE SCOPE")
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
    primitive_texts = tuple(
        " ".join(path.read_text(encoding="utf-8").split()) for path in PRIMITIVE_PATHS
    )
    note_text = NOTE_PATH.read_text(encoding="utf-8")

    check(
        "The source row declares the narrow no-go claim type",
        "**Type:** no_go" in note_text and "**Claim type:** no_go" in note_text,
    )
    check(
        "The source row names the four-axiom memo as its load-bearing authority",
        "[Minimal Framework Axioms](MINIMAL_AXIOMS_2026-06-29.md)" in note_text,
    )
    absent_symbols = ("I_seed", "eta_obs", "favored column", "PMNS", "Kullback")
    check(
        "The selector-specific symbols are absent from the four-axiom statement",
        all(symbol not in axiom_text for symbol in absent_symbols),
        ", ".join(absent_symbols),
    )
    required_open_content = (
        "Born weights",
        "context selection",
        "source/action",
        "physical-observable identification",
        "measurement basis selection",
    )
    check(
        "The axiom memo explicitly leaves every relevant bridge outside the axioms",
        all(needle in axiom_text for needle in required_open_content),
        ", ".join(required_open_content),
    )
    check(
        "The source firewall preserves future downstream bridge routes",
        "does not rule out a future downstream selector theorem" in note_text,
    )
    check(
        "Approved primitives are included but supply no selector or state-contingent value",
        "no mass ratio, coupling, mixing angle, phase, selector" in primitive_texts[0]
        and "no mass ratio, coupling, mixing angle, phase, selector" in primitive_texts[1]
        and "not a state-selection rule" in primitive_texts[2]
        and "no state, averaging over alternatives, measure, weighting" in primitive_texts[2],
    )

    nearest_neighbors = set(base.nearest_neighbor_offsets)
    rotations = proper_cubic_rotations()
    check(
        "The local lattice checks match Z^3 and its 24 proper cubic rotations",
        base.sites == "Z^3"
        and len(nearest_neighbors) == 6
        and len(rotations) == 24
        and all(
            {rotate_vector(vector, rotation) for vector in nearest_neighbors}
            == nearest_neighbors
            for rotation in rotations
        ),
    )

    units = matrix_units()
    multiplication_table_is_exact = all(
        matrix_multiply(units[(left_row, left_column)], units[(right_row, right_column)])
        == (
            units[(left_row, right_column)]
            if left_column == right_row
            else ZERO2
        )
        for left_row, left_column in units
        for right_row, right_column in units
    )
    identity = matrix_add(units[(0, 0)], units[(1, 1)])
    arbitrary_matrix: Matrix2 = ((1 + 2j, 3 - 1j), (-2j, 4 + 0j))
    reconstructed = ZERO2
    for (row, column), unit in units.items():
        reconstructed = matrix_add(
            reconstructed,
            matrix_scale(arbitrary_matrix[row][column], unit),
        )
    check(
        "Actual matrix units realize the full complex M_2 multiplication and span",
        base.local_algebra == "M_2(C)"
        and len(units) == 4
        and multiplication_table_is_exact
        and all(matrix_multiply(identity, unit) == unit for unit in units.values())
        and reconstructed == arbitrary_matrix,
    )
    p_zero = units[(0, 0)]
    p_one = units[(1, 1)]
    p_plus = rank_one_projector((1 + 0j, 1 + 0j))
    neighbor_sum = sum_matrices((p_zero,) * 4 + (p_plus,) * 2)
    top = top_spectral_projector(neighbor_sum)
    trace_neighbor_sum = float(
        (neighbor_sum[0][0] + neighbor_sum[1][1]).real
    )
    discriminant = math.sqrt(
        float((neighbor_sum[0][0] - neighbor_sum[1][1]).real) ** 2
        + 4.0 * abs(neighbor_sum[0][1]) ** 2
    )
    lambda_plus = 0.5 * (trace_neighbor_sum + discriminant)
    identity_minus_top = (
        None
        if top is None
        else matrix_add(identity, matrix_scale(-1.0, top))
    )
    top_rayleigh = (
        float(
            sum(
                matrix_multiply(neighbor_sum, top)[index][index].real
                for index in range(2)
            )
        )
        if top is not None
        else float("nan")
    )
    complement_rayleigh = (
        float(
            sum(
                matrix_multiply(neighbor_sum, identity_minus_top)[index][index].real
                for index in range(2)
            )
        )
        if identity_minus_top is not None
        else float("nan")
    )
    h = 1.0 / math.sqrt(2.0)
    unitary: Matrix2 = ((h + 0j, h + 0j), (h + 0j, -h + 0j))
    rotated_sum = matrix_multiply(
        matrix_multiply(unitary, neighbor_sum), matrix_dagger(unitary)
    )
    rotated_top = top_spectral_projector(rotated_sum)
    covariant_top = (
        None
        if top is None
        else matrix_multiply(matrix_multiply(unitary, top), matrix_dagger(unitary))
    )
    degenerate_sum = sum_matrices((p_zero,) * 3 + (p_one,) * 3)
    check(
        "Non-diagonal spectral admissibility is unitary-covariant and detects degeneracy",
        base.admissibility_rule == "top spectral projector of unordered neighbor sum"
        and top is not None
        and rotated_top is not None
        and covariant_top is not None
        and matrix_close(top, matrix_dagger(top))
        and matrix_close(matrix_multiply(top, top), top)
        and abs((top[0][0] + top[1][1]).real - 1.0) < 1e-12
        and matrix_close(
            matrix_multiply(neighbor_sum, top), matrix_scale(lambda_plus, top)
        )
        and abs(top_rayleigh - lambda_plus) < 1e-12
        and top_rayleigh > complement_rayleigh
        and matrix_close(rotated_top, covariant_top)
        and matrix_close(
            top_spectral_projector(matrix_scale(6.0, p_zero)), p_zero
        )
        and top_spectral_projector(degenerate_sum) is None,
    )
    record_families = (
        frozenset(),
        frozenset({0}),
        frozenset({1, 2}),
        frozenset({3, 4, 5}),
    )
    finite_additivity = all(
        record_readout(left | right)
        == record_readout(left) + record_readout(right)
        for left in record_families
        for right in record_families
        if left.isdisjoint(right)
    )
    check(
        "The local record/readout probes match the explicit infinite model",
        base.state_space == "all partial admissible rank-one record configurations"
        and base.uniform_record == "P0 at every site"
        and base.finite_readout == "record cardinality"
        and base.base_law == "constant total answer"
        and "P0" in available_from_neighbor_projectors(6, 0)
        and record_readout(frozenset()) == 0
        and finite_additivity,
        "I(R)=number of records, I(empty)=0",
    )


def part_two_objective_use_independence(base: BaseModelWitness) -> None:
    print("\nPART 2: MINIMIZATION PRINCIPLE IS NOT ENTAILED")
    states = ("record_state_0", "record_state_1", "record_state_2")
    fixed_cost = {"q_x": 0.1, "q_y": 0.2}
    q_min = argmin_unique(fixed_cost)
    q_other = "q_y" if q_min == "q_x" else "q_x"

    minimize_completion = SelectorCompletion(base, "minimize", q_min)
    alternative_completion = SelectorCompletion(base, "alternative", q_other)

    check(
        "Both selector laws extend the identical base-model witness",
        minimize_completion.base is alternative_completion.base is base,
    )
    check(
        "The minimizing completion is total, single-valued, and state-neutral",
        law_is_total_single_valued_and_state_neutral(minimize_completion, states),
    )
    check(
        "The alternative completion is total, single-valued, and state-neutral",
        law_is_total_single_valued_and_state_neutral(alternative_completion, states),
    )
    check(
        "The two allowed downstream laws select different sources",
        minimize_completion.answers(states)[0] != alternative_completion.answers(states)[0],
        f"{minimize_completion.answers(states)[0]} vs {alternative_completion.answers(states)[0]}",
    )


def part_three_modality_weight_independence(base: BaseModelWitness) -> None:
    print("\nPART 3: EQUAL MODALITY WEIGHTS ARE NOT ENTAILED")
    uniform = (1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0)
    x_deformed = positive_three_distribution_with_kl(0.1)
    y_deformed = positive_three_distribution_with_kl(0.15)

    x_seed = scale_three(uniform, 3.0 * XBAR_NE)
    y_seed = scale_three(uniform, 3.0 * YBAR_NE)
    x_native_deformed = scale_three(x_deformed, 3.0 * XBAR_NE)
    y_native_deformed = scale_three(y_deformed, 3.0 * YBAR_NE)

    sources = {
        "q_x": {"x": x_native_deformed, "y": y_seed, "phase": 0.0},
        "q_y": {"x": x_seed, "y": y_native_deformed, "phase": 0.0},
    }

    def costs(wx: float, wy: float) -> dict[str, float]:
        return {
            name: wx * kl_to_uniform(normalize_three(source["x"]))
            + wy * kl_to_uniform(normalize_three(source["y"]))
            + (1.0 - math.cos(source["phase"]))
            for name, source in sources.items()
        }

    equal_costs = costs(1.0, 1.0)
    weighted_costs = costs(2.0, 0.5)
    equal_choice = argmin_unique(equal_costs)
    weighted_choice = argmin_unique(weighted_costs)

    check(
        "Constructed deformations lie on the native fixed-total seed surface",
        min(x_native_deformed + y_native_deformed) > 0.0
        and math.isclose(sum(x_native_deformed), 3.0 * XBAR_NE, abs_tol=1e-14)
        and math.isclose(sum(y_native_deformed), 3.0 * YBAR_NE, abs_tol=1e-14),
    )
    check(
        "Independent KL evaluation reproduces the prescribed block costs",
        math.isclose(kl_to_uniform(normalize_three(x_native_deformed)), 0.1, abs_tol=2e-14)
        and math.isclose(kl_to_uniform(normalize_three(y_native_deformed)), 0.15, abs_tol=2e-14),
        "normalization removes the native fixed totals",
    )
    check(
        "Equal and positive-reweighted information laws choose different sources",
        equal_choice == "q_x" and weighted_choice == "q_y",
        f"equal={equal_costs}, weighted={weighted_costs}",
    )

    states = ("record_state_0", "record_state_1")
    equal_completion = SelectorCompletion(base, "equal weights", equal_choice)
    weighted_completion = SelectorCompletion(base, "positive unequal weights", weighted_choice)
    check(
        "Both weighted selectors satisfy the same state-neutral law qualification",
        law_is_total_single_valued_and_state_neutral(equal_completion, states)
        and law_is_total_single_valued_and_state_neutral(weighted_completion, states),
    )


def part_four_closure_and_column_independence(base: BaseModelWitness) -> None:
    print("\nPART 4: OBSERVATIONAL ANCHOR AND FAVORED COLUMN ARE NOT ENTAILED")
    eta_by_source = {"q_x": 1.0, "q_y": 2.0}

    closure_at_one = tuple(name for name, value in eta_by_source.items() if value == 1.0)
    closure_at_two = tuple(name for name, value in eta_by_source.items() if value == 2.0)
    check(
        "Changing only the external comparator changes the exact-closure locus",
        closure_at_one == ("q_x",) and closure_at_two == ("q_y",),
        f"eta_obs=1 -> {closure_at_one}; eta_obs=2 -> {closure_at_two}",
    )

    transport_completion_zero = (2.0, 1.0, 0.5)
    transport_completion_one = (1.0, 2.0, 0.5)
    favored_zero = max(range(3), key=transport_completion_zero.__getitem__)
    favored_one = max(range(3), key=transport_completion_one.__getitem__)
    check(
        "Two transport completions over the same base favor different columns",
        favored_zero == 0 and favored_one == 1,
        f"i_*={favored_zero} vs {favored_one}",
    )

    states = ("record_state_0", "record_state_1")
    closure_completion_one = SelectorCompletion(base, "anchor one", closure_at_one[0])
    closure_completion_two = SelectorCompletion(base, "anchor two", closure_at_two[0])
    check(
        "Both closure-anchor completions remain total and state-neutral",
        law_is_total_single_valued_and_state_neutral(closure_completion_one, states)
        and law_is_total_single_valued_and_state_neutral(closure_completion_two, states),
    )
    check(
        "The closure-anchor completions share the identical base-model witness",
        closure_completion_one.base is closure_completion_two.base is base,
    )


def part_five_logical_conclusion() -> None:
    print("\nPART 5: NARROW LOGICAL CONCLUSION")
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    required_boundaries = (
        "not a no-go against downstream selector physics",
        "does not invalidate the conditional optimizer output",
        "supplies no positive selector authority",
        "independent audit lane",
    )
    check(
        "The no-go is fenced against broader impossibility rhetoric",
        all(boundary in note_text for boundary in required_boundaries),
        ", ".join(required_boundaries),
    )
    check(
        "The theorem conclusion is stated as non-entailment from the current baseline alone",
        "the adopted minimum-information closure law is not entailed by the current supplied premises" in note_flat,
    )


def main() -> int:
    print("DM LEPTOGENESIS PMNS MINIMUM-INFORMATION BASELINE NON-DERIVABILITY")
    print("Exact two-completion certificate; no observational value is a proof input")

    base = BaseModelWitness(
        sites="Z^3",
        nearest_neighbor_offsets=(
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ),
        local_algebra="M_2(C)",
        admissibility_rule="top spectral projector of unordered neighbor sum",
        state_space="all partial admissible rank-one record configurations",
        uniform_record="P0 at every site",
        finite_readout="record cardinality",
        base_law="constant total answer",
    )
    part_one_language_and_scope(base)
    part_two_objective_use_independence(base)
    part_three_modality_weight_independence(base)
    part_four_closure_and_column_independence(base)
    part_five_logical_conclusion()

    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("FINAL_TAG: PMNS_MININFO_CURRENT_BASELINE_NON_ENTAILMENT_NO_GO")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
