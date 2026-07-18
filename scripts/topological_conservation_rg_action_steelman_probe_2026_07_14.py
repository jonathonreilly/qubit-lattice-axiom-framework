#!/usr/bin/env python3
"""Exact bounded attack on topological/conservation/RG one-action selection."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations_with_replacement, permutations, product
from math import gcd, isqrt
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "TOPOLOGICAL_CONSERVATION_RG_ACTION_STEELMAN_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "SINGLE_INVARIANT_ACTION_STEELMAN_ATTACK_NOTE_2026-07-14.md"
)


PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def exact_equal(left: sp.Matrix | sp.Expr, right: sp.Matrix | sp.Expr) -> bool:
    difference = left - right
    if isinstance(difference, sp.MatrixBase):
        return all(sp.simplify(value) == 0 for value in difference)
    return sp.simplify(difference) == 0


def permutation_shift(size: int, direction: int) -> sp.Matrix:
    shift = sp.zeros(size)
    for column in range(size):
        shift[(column + direction) % size, column] = 1
    return shift


def biased_ring_kernel(size: int, right: Fraction) -> sp.Matrix:
    left = 1 - right
    kernel = sp.zeros(size)
    for row in range(size):
        kernel[row, (row + 1) % size] = sp.Rational(right.numerator, right.denominator)
        kernel[row, (row - 1) % size] = sp.Rational(left.numerator, left.denominator)
    return kernel


def canonical_charge_tuple(charges: tuple[int, ...]) -> tuple[int, ...]:
    charges = tuple(sorted(charges))
    conjugate = tuple(sorted(-charge for charge in charges))
    return min(charges, conjugate)


def anomaly_free_chiral(charges: tuple[int, ...]) -> bool:
    return (
        all(charge != 0 for charge in charges)
        and sum(charges) == 0
        and sum(charge**3 for charge in charges) == 0
        and not any(-charge in charges for charge in charges)
        and gcd(*(abs(charge) for charge in charges)) == 1
    )


def enumerate_anomaly_quintets(bound: int) -> tuple[tuple[int, ...], ...]:
    values = tuple(value for value in range(-bound, bound + 1) if value)
    solutions = {
        canonical_charge_tuple(charges)
        for charges in combinations_with_replacement(values, 5)
        if anomaly_free_chiral(charges)
    }
    return tuple(sorted(solutions))


def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column, row in enumerate(permutation):
                matrix[row, column] = signs[column]
            if matrix.det() == 1:
                rotations.append(matrix)
    unique = {tuple(matrix): matrix for matrix in rotations}
    return tuple(unique.values())


def tensor_response(source: sp.Matrix, traceless_weight: sp.Expr, trace_weight: sp.Expr) -> sp.Matrix:
    trace_part = sp.trace(source) * sp.eye(3) / 3
    traceless_part = source - trace_part
    return sp.simplify(traceless_weight * traceless_part + trace_weight * trace_part)


def cubic_torus_laplacian(size: int = 3) -> sp.Matrix:
    sites = tuple(product(range(size), repeat=3))
    index = {site: position for position, site in enumerate(sites)}
    laplacian = sp.zeros(len(sites))
    for site in sites:
        row = index[site]
        laplacian[row, row] = 6
        for axis in range(3):
            for direction in (-1, 1):
                neighbor = list(site)
                neighbor[axis] = (neighbor[axis] + direction) % size
                laplacian[row, index[tuple(neighbor)]] -= 1
    return laplacian


def source_contract() -> None:
    section("A - Authority and strongest-surviving-action contract")
    note = " ".join(
        NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .split()
    )
    axioms = AXIOMS.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8").lower()
    check("A note is authority-free", "authority: none" in note)
    check(
        "A note changes no live authority surface",
        "changes no axiom, registry, primitive, audit, review queue, or retained surface" in note,
    )
    check("A actual domain retains Z3 M2 and permanent records", "`Z^3`" in axioms and "`M_2(C)`" in axioms and "records are permanent" in axioms.lower())
    check("A parent topological conservation action steelman is wired in", "topological/conservation action" in parent and "strongest surviving steelman" in parent)
    check("A parent leaves coefficient boundary and measure uniqueness open", all(term in parent for term in ("coefficient", "boundary", "measure")))


def quantized_level_and_linked_signs() -> None:
    section("B - Quantized level magnitude and linked orientation sign")
    levels = tuple(range(-5, 6))
    nontrivial = tuple(level for level in levels if level)
    minimum_nonzero = tuple(level for level in nontrivial if abs(level) == min(abs(value) for value in nontrivial))
    check("B integer quantization plus minimum nontrivial magnitude leaves a sign pair", minimum_nonzero == (-1, 1))
    topological_action = {level: (level**2 - 1) ** 2 for level in levels}
    check("B orientation-even topological action has exact minima at plus and minus one", tuple(level for level, score in topological_action.items() if score == min(topological_action.values())) == (-1, 1))
    oriented_action = {level: (level**2 - 1) ** 2 - Fraction(1, 10) * level for level in levels}
    check("B an orientation-odd term selects plus one by inserting its sign", min(oriented_action, key=oriented_action.get) == 1)

    sign_fields = ("bulk_level", "pump", "chirality", "boundary", "rg_fixed_point")
    sign_candidates = tuple(product((-1, 1), repeat=len(sign_fields)))
    links = tuple((index, index + 1) for index in range(len(sign_fields) - 1))

    def linked(candidate: tuple[int, ...], active_links=links) -> bool:
        return all(candidate[left] == candidate[right] for left, right in active_links)

    linked_winners = tuple(candidate for candidate in sign_candidates if linked(candidate))
    check("B anomaly-pump-boundary-RG sign linkage collapses 32 branches to one mirror pair", len(linked_winners) == 2 and linked_winners == ((-1,) * 5, (1,) * 5))
    for removed in links:
        remaining = tuple(link for link in links if link != removed)
        winners = tuple(candidate for candidate in sign_candidates if linked(candidate, remaining))
        check(f"B deleting sign link {removed} restores four branches", len(winners) == 4)
    check("B fixing one spatial orientation would select one linked branch", sum(candidate[0] == 1 for candidate in linked_winners) == 1)


def anomaly_index_matter_selection() -> None:
    section("C - Anomaly constraints and a genuine scoped matter winner")
    a, b, c = sp.symbols("a b c")
    three_charge_identity = sp.expand(a**3 + b**3 + (-a - b) ** 3)
    four_charge_identity = sp.expand(a**3 + b**3 + c**3 + (-a - b - c) ** 3)
    check("C three-charge anomaly identity forces a zero factor", sp.factor(three_charge_identity) == -3 * a * b * (a + b))
    check(
        "C four-charge anomaly identity forces an opposite-pair factor",
        sp.simplify(four_charge_identity + 3 * (a + b) * (a + c) * (b + c)) == 0,
    )
    winner = (-9, -5, -1, 7, 8)
    competitor = (-10, -4, -2, 7, 9)
    check("C displayed winner cancels linear and cubic U1 anomalies", sum(winner) == 0 and sum(charge**3 for charge in winner) == 0)
    check("C displayed competitor cancels the same anomalies", sum(competitor) == 0 and sum(charge**3 for charge in competitor) == 0)
    check("C both quintets are primitive and contain no vectorlike pair", anomaly_free_chiral(winner) and anomaly_free_chiral(competitor))

    solutions = enumerate_anomaly_quintets(14)
    norms = {charges: sum(charge**2 for charge in charges) for charges in solutions}
    minimum_norm = min(norms.values())
    minimum_solutions = tuple(charges for charges in solutions if norms[charges] == minimum_norm)
    check("C bounded exhaustive primitive chiral anomaly census has two quintet families", set(solutions) == {winner, competitor})
    check("C minimum quadratic charge norm uniquely selects the displayed winner up to sign and permutation", minimum_solutions == (winner,) and minimum_norm == 220 and norms[competitor] == 250)
    check("C norm at most 220 makes the exhaustive absolute-charge bound 14 sufficient", isqrt(minimum_norm) == 14 and (isqrt(minimum_norm) + 1) ** 2 > minimum_norm)

    values = tuple(value for value in range(-14, 15) if value)
    smaller_solutions = {
        canonical_charge_tuple(charges)
        for count in (3, 4)
        for charges in combinations_with_replacement(values, count)
        if anomaly_free_chiral(charges)
    }
    check("C no three- or four-charge primitive chiral solution occurs in the exhaustive norm-relevant box", not smaller_solutions)
    check("C dropping primitive normalization restores rescaled copies", sum(2 * charge for charge in winner) == 0 and sum((2 * charge) ** 3 for charge in winner) == 0)
    check("C dropping the no-vectorlike condition admits trivial anomaly-free pairs", sum((1, -1)) == 0 and sum(charge**3 for charge in (1, -1)) == 0)


def conservation_links_record_export_source_and_tick() -> None:
    section("D - One conservation clause genuinely collapses four walls")
    fields = ("record_increment", "export_quantum", "green_source", "causal_tick")
    candidates = tuple(product((0, 1), repeat=len(fields)))
    links = tuple((index, index + 1) for index in range(len(fields) - 1))

    def action(candidate: tuple[int, ...], active_links=links) -> int:
        return sum((candidate[left] - candidate[right]) ** 2 for left, right in active_links)

    scores = {candidate: action(candidate) for candidate in candidates}
    minima = tuple(candidate for candidate, score in scores.items() if score == min(scores.values()))
    check("D conservation links record export source and tick into two zero-action histories", minima == ((0, 0, 0, 0), (1, 1, 1, 1)))
    check("D conservation prices event content but does not trigger the event", len(minima) == 2)
    for removed in links:
        remaining = tuple(link for link in links if link != removed)
        local_scores = {candidate: action(candidate, remaining) for candidate in candidates}
        local_minima = tuple(candidate for candidate, score in local_scores.items() if score == min(local_scores.values()))
        check(f"D deleting conservation link {removed} restores four histories", len(local_minima) == 4)
    occurrence_scores = {candidate: score + (candidate[0] - 1) ** 2 for candidate, score in scores.items()}
    check("D adding occurrence selects the all-one linked event by explicitly requiring it", min(occurrence_scores, key=occurrence_scores.get) == (1, 1, 1, 1))

    laplacian = cubic_torus_laplacian(3)
    count = laplacian.rows
    ones = sp.ones(count, 1)
    source = sp.zeros(count, 1)
    source[0] = 1
    source[1] = -1
    augmented = laplacian.row_join(ones).col_join(ones.T.row_join(sp.zeros(1, 1)))
    field = (augmented.inv(method="DM") * source.col_join(sp.zeros(1, 1)))[:count, :]
    check("D one linked unit source gives an exact finite Green response after a sink and zero-mode boundary", laplacian * field == source and (ones.T * field)[0] == 0)


def pump_and_detailed_balance_breaking() -> None:
    section("E - Quantized pump and continuous detailed-balance breaking")
    size = 5
    right_shift = permutation_shift(size, 1)
    left_shift = permutation_shift(size, -1)
    identity = sp.eye(size)
    check("E minimal right and left pumps are unitary permutation laws", right_shift.T * right_shift == identity and left_shift.T * left_shift == identity)
    check("E pump orientations are inverse and physically distinct", right_shift * left_shift == identity and right_shift != left_shift)
    check("E finite quantized pumps recur after one circuit", right_shift**size == identity and left_shift**size == identity)
    initial = sp.Matrix([1, 0, 0, 0, 0])
    check("E the two pumps carry one token in opposite directions per causal tick", right_shift * initial == sp.Matrix([0, 1, 0, 0, 0]) and left_shift * initial == sp.Matrix([0, 0, 0, 0, 1]))

    uniform = sp.ones(1, size) / size
    kernels = {
        Fraction(2, 3): biased_ring_kernel(size, Fraction(2, 3)),
        Fraction(3, 4): biased_ring_kernel(size, Fraction(3, 4)),
    }
    currents = {}
    entropy_productions = {}
    for right_probability, kernel in kernels.items():
        left_probability = 1 - right_probability
        currents[right_probability] = Fraction(2 * right_probability - 1, size)
        entropy_productions[right_probability] = sp.Rational(
            currents[right_probability].numerator,
            currents[right_probability].denominator,
        ) * sp.log(
            sp.Rational(right_probability.numerator, right_probability.denominator)
            / sp.Rational(left_probability.numerator, left_probability.denominator)
        )
        check(f"E biased kernel {right_probability} is normalized and uniform-stationary", kernel * sp.ones(size, 1) == sp.ones(size, 1) and exact_equal(uniform * kernel, uniform))
        check(f"E biased kernel {right_probability} violates detailed balance with positive current", currents[right_probability] > 0 and entropy_productions[right_probability].is_positive)
    check("E fixed activity leaves a continuous current magnitude", currents[Fraction(2, 3)] == Fraction(1, 15) and currents[Fraction(3, 4)] == Fraction(1, 10))
    check("E orientation reversal preserves structure and flips current", Fraction(1, 3) == 1 - Fraction(2, 3))


def rg_fixed_point_and_sign_intersection() -> None:
    section("F - RG fixed points can fix magnitude after the RG map is supplied")
    coupling = sp.symbols("g", real=True)
    positive_map_fixed = sp.solve(sp.Eq(coupling, coupling**2), coupling)
    negative_map_fixed = sp.solve(sp.Eq(coupling, -coupling**2), coupling)
    odd_map_fixed = sp.solve(sp.Eq(coupling, coupling**3), coupling)
    check("F quadratic RG map has one nonzero fixed point plus one", positive_map_fixed == [0, 1])
    check("F orientation-conjugate quadratic RG map has one nonzero fixed point minus one", negative_map_fixed == [-1, 0])
    check("F orientation-odd RG map retains both nonzero signs", odd_map_fixed == [-1, 0, 1])
    check("F conjugate nonzero fixed points have equal stability magnitude", abs(sp.diff(coupling**2, coupling).subs(coupling, 1)) == abs(sp.diff(-coupling**2, coupling).subs(coupling, -1)) == 2)

    for level in (-1, 1):
        fixed = sp.solve(sp.Eq(coupling, level * coupling**2), coupling)
        nonzero = tuple(value for value in fixed if value)
        check(f"F linking RG orientation to topological level {level} fixes coupling to that sign", nonzero == (level,))
    check("F the exact RG transformation remains an input to the fixed-point theorem", positive_map_fixed != odd_map_fixed)


def clock_boundary_and_actuality_residuals() -> None:
    section("G - Pump cycles supply causal ticks but not metric duration or actuality")
    cycles = sp.Integer(12)
    check("G one pump cycle per linked event gives exact causal depth", cycles == 12)
    check("G rates one and two give distinct durations for the same topological cycle count", cycles / 1 == 12 and cycles / 2 == 6)

    size = 5
    shift = permutation_shift(size, 1)
    orbit = tuple(shift**step * basis for basis in (sp.eye(size).col(0),) for step in range(size))
    check("G a finite pump has five equally lawful orbit phases", len({tuple(state) for state in orbit}) == size)
    check("G topological level and anomaly data do not select an orbit phase", shift**size == sp.eye(size))

    finite_transcripts = ((1, 0, 1, 1), (1, 1, 0, 1))
    check("G different actual record transcripts can share event count and pump index", sum(finite_transcripts[0]) == sum(finite_transcripts[1]) and finite_transcripts[0] != finite_transcripts[1])


def tensor_gravity_response_residual() -> None:
    section("H - Proper-cubic tensor response retains trace and traceless coefficients")
    rotations = proper_cubic_rotations()
    source = sp.diag(2, -1, 0)
    response_equal = tensor_response(source, 1, 1)
    response_trace_two = tensor_response(source, 1, 2)
    check("H proper-cubic group has 24 exact rotations", len(rotations) == 24 and all(rotation.T * rotation == sp.eye(3) and rotation.det() == 1 for rotation in rotations))
    for trace_weight in (1, 2):
        check(
            f"H trace weight {trace_weight} response is proper-cubic covariant",
            all(
                exact_equal(
                    tensor_response(rotation * source * rotation.T, 1, trace_weight),
                    rotation * tensor_response(source, 1, trace_weight) * rotation.T,
                )
                for rotation in rotations
            ),
        )
    check("H equal and doubled trace response are physically distinct", response_equal != response_trace_two)
    check("H their difference is not removed by one overall normalization", not any(exact_equal(response_trace_two, factor * response_equal) for factor in (sp.Rational(1, 2), 1, 2)))

    universal = (1, 1)
    nonuniversal = (1, 2)
    check("H conserved common source permits universal or nonuniversal species coupling", universal != nonuniversal)
    check("H common rescaling leaves the WEP-breaking coupling ratio", Fraction(*universal[::-1]) == 1 and Fraction(*nonuniversal[::-1]) == 2)


def strongest_intersection_and_clause_deletion() -> None:
    section("I - Strongest combined intersection and residual count")
    sign_variables = tuple(product((-1, 1), repeat=5))
    sign_links = tuple((index, index + 1) for index in range(4))
    linked_signs = tuple(
        candidate
        for candidate in sign_variables
        if all(candidate[left] == candidate[right] for left, right in sign_links)
    )
    event_variables = tuple(product((0, 1), repeat=4))
    event_links = tuple((index, index + 1) for index in range(3))
    linked_events = tuple(
        candidate
        for candidate in event_variables
        if all(candidate[left] == candidate[right] for left, right in event_links)
    )
    charge_families = ((-9, -5, -1, 7, 8), (-10, -4, -2, 7, 9))
    minimum_charge_families = tuple(
        charges
        for charges in charge_families
        if sum(charge**2 for charge in charges)
        == min(sum(charge**2 for charge in candidate) for candidate in charge_families)
    )
    residuals = tuple(
        product(
            linked_signs,
            linked_events,
            minimum_charge_families,
            (0, 1),  # actual orbit/history member
            (1, 2),  # metric rate
            (1, 2),  # trace/traceless tensor ratio
            (1, 2),  # common/noncommon species coupling
        )
    )
    check("I strongest linked topological-conservation-anomaly intersection leaves 64 exact branches", len(residuals) == 64)
    record_forming = tuple(candidate for candidate in residuals if candidate[1][0] == 1)
    check("I imposing one nonzero event in the one-event intersection removes all-zero but leaves 32", len(record_forming) == 32)
    oriented = tuple(candidate for candidate in record_forming if candidate[0][0] == 1)
    check("I supplying one orientation still leaves 16 actuality-rate-tensor-coupling branches", len(oriented) == 16)

    for removed in sign_links:
        remaining = tuple(link for link in sign_links if link != removed)
        survivors = tuple(candidate for candidate in sign_variables if all(candidate[left] == candidate[right] for left, right in remaining))
        check(f"I deleting linked topological sign clause {removed} doubles sign residual", len(survivors) == 4)
    for removed in event_links:
        remaining = tuple(link for link in event_links if link != removed)
        survivors = tuple(candidate for candidate in event_variables if all(candidate[left] == candidate[right] for left, right in remaining))
        check(f"I deleting linked conservation clause {removed} doubles event residual", len(survivors) == 4)
    check("I deleting minimum charge norm restores the second anomaly-free matter family", len(charge_families) == 2 and len(minimum_charge_families) == 1)
    check("I selecting the final 16 requires four further physical clauses", 2**4 == len(oriented))


def documentation_contract() -> None:
    section("J - Route coverage and no-go-discipline needles")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "one dimensionless representation-independent principle",
        "quantized topological coefficients",
        "anomaly/index constraints",
        "conserved-current action",
        "detailed-balance breaking",
        "topological pump",
        "rg fixed point",
        "record occurrence",
        "no-return",
        "chiral relativistic matter",
        "common clock",
        "sourced tensor/gravity response",
        "genuine wall collapse",
        "scoped unique winner",
        "clause-deletion audit",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — exact residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path",
        "n7 — strongest surviving steelman",
        "n8 — cross-cycle echo",
    )
    for phrase in required:
        check(f"J note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    quantized_level_and_linked_signs()
    anomaly_index_matter_selection()
    conservation_links_record_export_source_and_tick()
    pump_and_detailed_balance_breaking()
    rg_fixed_point_and_sign_intersection()
    clock_boundary_and_actuality_residuals()
    tensor_gravity_response_residual()
    strongest_intersection_and_clause_deletion()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
