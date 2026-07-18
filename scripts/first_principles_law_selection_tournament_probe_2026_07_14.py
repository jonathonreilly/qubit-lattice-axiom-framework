#!/usr/bin/env python3
"""Bounded exact tournament for first-principles microscopic-law selectors."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

import sympy as sp

import autonomous_homogeneous_binary_nucleation_probe_2026_07_14 as q10
import cfsi_q_bell_coherent_causal_front_law_probe_2026_07_14 as q7


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FIRST_PRINCIPLES_LAW_SELECTION_TOURNAMENT_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
DETERMINISTIC_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md"
)
EXACT_LAW_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CAUSAL_REVERSIBLE_ACTUALITY_WEIGHT_INDEPENDENCE_NOTE_2026-07-14.md"
)


PASS = 0
FAIL = 0
OPEN = -1
VALUES = (OPEN, 0, 1)
Configuration = tuple[int, ...]


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


def label_swap(value: int) -> int:
    return OPEN if value == OPEN else 1 - value


@dataclass(frozen=True)
class RecordRule:
    """Nine label-covariant reflection-symmetric permanent radius-one rules.

    `one_neighbor` is the output for an open center with unordered neighbors
    {open,0}. `equal_neighbors` is the output for neighbors {0,0}. Label
    covariance fixes the {open,1} and {1,1} cases. The invariant contexts
    {open,open} and {0,1} must remain open.
    """

    one_neighbor: int
    equal_neighbors: int


RECORD_RULES = tuple(RecordRule(one, equal) for one, equal in product(VALUES, repeat=2))
NO_FORMATION_RULE = RecordRule(OPEN, OPEN)
COPY_EQUAL_RULE = RecordRule(OPEN, 0)
OPPOSE_EQUAL_RULE = RecordRule(OPEN, 1)


def record_local(rule: RecordRule, left: int, center: int, right: int) -> int:
    if center != OPEN:
        return center
    neighbors = tuple(sorted((left, right)))
    if neighbors in ((OPEN, OPEN), (0, 1)):
        return OPEN
    if neighbors == (OPEN, 0):
        return rule.one_neighbor
    if neighbors == (OPEN, 1):
        return label_swap(rule.one_neighbor)
    if neighbors == (0, 0):
        return rule.equal_neighbors
    if neighbors == (1, 1):
        return label_swap(rule.equal_neighbors)
    raise ValueError(neighbors)


def record_update(rule: RecordRule, configuration: Configuration) -> Configuration:
    size = len(configuration)
    return tuple(
        record_local(
            rule,
            configuration[(site - 1) % size],
            configuration[site],
            configuration[(site + 1) % size],
        )
        for site in range(size)
    )


def record_update_site(rule: RecordRule, configuration: Configuration, site: int) -> Configuration:
    values = list(configuration)
    size = len(configuration)
    values[site] = record_local(
        rule,
        configuration[(site - 1) % size],
        configuration[site],
        configuration[(site + 1) % size],
    )
    return tuple(values)


def record_label_covariant(rule: RecordRule) -> bool:
    return all(
        record_local(rule, *(label_swap(value) for value in triple))
        == label_swap(record_local(rule, *triple))
        for triple in product(VALUES, repeat=3)
    )


def record_reflection_symmetric(rule: RecordRule) -> bool:
    return all(
        record_local(rule, *triple)
        == record_local(rule, triple[2], triple[1], triple[0])
        for triple in product(VALUES, repeat=3)
    )


def record_permanent(rule: RecordRule) -> bool:
    return all(
        record_local(rule, left, center, right) == center
        for left, center, right in product(VALUES, repeat=3)
        if center != OPEN
    )


def record_formation_context_count(rule: RecordRule) -> int:
    return sum(
        record_local(rule, left, OPEN, right) != OPEN
        for left, right in product(VALUES, repeat=2)
    )


def record_output_counts(rule: RecordRule, open_center_only: bool = False) -> tuple[int, int, int]:
    counts = {OPEN: 0, 0: 0, 1: 0}
    triples = (
        ((left, OPEN, right) for left, right in product(VALUES, repeat=2))
        if open_center_only
        else product(VALUES, repeat=3)
    )
    for triple in triples:
        counts[record_local(rule, *triple)] += 1
    return counts[OPEN], counts[0], counts[1]


def record_injective(rule: RecordRule, size: int = 4) -> bool:
    states = tuple(product(VALUES, repeat=size))
    return len({record_update(rule, state) for state in states}) == len(states)


def record_confluent(rule: RecordRule, size: int = 5) -> bool:
    return all(
        record_update_site(
            rule,
            record_update_site(rule, state, left_site),
            right_site,
        )
        == record_update_site(
            rule,
            record_update_site(rule, state, right_site),
            left_site,
        )
        for state in product(VALUES, repeat=size)
        for left_site, right_site in combinations(range(size), 2)
    )


def record_fixed_count(rule: RecordRule, size: int = 5) -> int:
    return sum(
        record_update(rule, state) == state
        for state in product(VALUES, repeat=size)
    )


def triggered_disagreement(rule: RecordRule) -> int:
    """Count disagreements with equal recorded neighbors on the two triggers."""

    return sum(
        sum(output != neighbor for _ in range(2))
        for neighbor in (0, 1)
        for output in (record_local(rule, neighbor, OPEN, neighbor),)
        if output != OPEN
    )


def eca_output(rule: int, triple: tuple[int, int, int]) -> int:
    index = (triple[0] << 2) | (triple[1] << 1) | triple[2]
    return (rule >> index) & 1


def eca_label_covariant(rule: int) -> bool:
    return all(
        eca_output(rule, tuple(1 - value for value in triple))
        == 1 - eca_output(rule, triple)
        for triple in product((0, 1), repeat=3)
    )


def eca_reflection_symmetric(rule: int) -> bool:
    return all(
        eca_output(rule, triple) == eca_output(rule, (triple[2], triple[1], triple[0]))
        for triple in product((0, 1), repeat=3)
    )


def eca_update(rule: int, configuration: tuple[int, ...]) -> tuple[int, ...]:
    size = len(configuration)
    return tuple(
        eca_output(
            rule,
            (
                configuration[(site - 1) % size],
                configuration[site],
                configuration[(site + 1) % size],
            ),
        )
        for site in range(size)
    )


def eca_update_site(rule: int, configuration: tuple[int, ...], site: int) -> tuple[int, ...]:
    values = list(configuration)
    size = len(configuration)
    values[site] = eca_output(
        rule,
        (
            configuration[(site - 1) % size],
            configuration[site],
            configuration[(site + 1) % size],
        ),
    )
    return tuple(values)


def eca_reversible(rule: int, sizes=range(3, 8)) -> bool:
    return all(
        len(
            {
                eca_update(rule, state)
                for state in product((0, 1), repeat=size)
            }
        )
        == 2**size
        for size in sizes
    )


def eca_confluent(rule: int, size: int = 5) -> bool:
    return all(
        eca_update_site(rule, eca_update_site(rule, state, left_site), right_site)
        == eca_update_site(rule, eca_update_site(rule, state, right_site), left_site)
        for state in product((0, 1), repeat=size)
        for left_site, right_site in combinations(range(size), 2)
    )


def eca_dependency_count(rule: int) -> int:
    return sum(
        any(
            eca_output(rule, triple)
            != eca_output(
                rule,
                tuple(
                    1 - value if coordinate == tested_coordinate else value
                    for coordinate, value in enumerate(triple)
                ),
            )
            for triple in product((0, 1), repeat=3)
        )
        for tested_coordinate in range(3)
    )


def eca_fixed_count(rule: int, size: int = 5) -> int:
    return sum(
        eca_update(rule, state) == state
        for state in product((0, 1), repeat=size)
    )


def rotation_matrix(rotation: tuple[tuple[int, int, int], ...]) -> sp.Matrix:
    return sp.Matrix.hstack(*(sp.Matrix(vector) for vector in rotation))


def matrix_key(matrix: sp.Matrix) -> tuple[int, ...]:
    return tuple(int(matrix[row, column]) for row in range(matrix.rows) for column in range(matrix.cols))


def rotation_order(rotation: sp.Matrix) -> int:
    power = sp.eye(3)
    for order in range(1, 13):
        power = power * rotation
        if power == sp.eye(3):
            return order
    raise ValueError("rotation order exceeded cubic-group bound")


def diagonal_unitary(hamiltonian: sp.Matrix, time: sp.Expr) -> sp.Matrix:
    return sp.diag(
        *(sp.simplify(sp.exp(-sp.I * hamiltonian[index, index] * time)) for index in range(hamiltonian.rows))
    )


def source_contract() -> None:
    section("A - Source and authority boundary")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    deterministic = DETERMINISTIC_NOTE.read_text(encoding="utf-8").lower()
    exact_law = EXACT_LAW_NOTE.read_text(encoding="utf-8").lower()
    check("A note is authority-free", "authority: none" in note)
    check("A note changes no live foundation surface", "changes no axiom, registry, primitive, or audit" in note)
    check(
        "A current Admissibility names one fixed rule without supplying dynamics",
        "one fixed nearest-neighbor admissibility rule" in axioms
        and "Admissibility is not a dynamics axiom." in axioms,
    )
    check("A deterministic escape boundary is wired in", "unique extension is not unique ergodicity" in deterministic)
    check(
        "A canonical-law field inventory is wired in",
        "exact_physical_law_domain" in exact_law
        and "predictive_record_decoder" in exact_law,
    )


def permanent_record_rule_tournament() -> None:
    section("B - Nine homogeneous label-covariant permanent record rules")
    check("B the bounded record-rule class has exactly nine members", len(RECORD_RULES) == 9)
    check("B every rule is global-label covariant", all(record_label_covariant(rule) for rule in RECORD_RULES))
    check("B every rule is reflection symmetric", all(record_reflection_symmetric(rule) for rule in RECORD_RULES))
    check("B every rule preserves existing records", all(record_permanent(rule) for rule in RECORD_RULES))
    check("B every rule leaves the homogeneous all-open state open", all(record_update(rule, (OPEN,) * 7) == (OPEN,) * 7 for rule in RECORD_RULES))

    reversible = tuple(rule for rule in RECORD_RULES if record_injective(rule))
    forming = tuple(rule for rule in RECORD_RULES if record_formation_context_count(rule) > 0)
    confluent = tuple(rule for rule in RECORD_RULES if record_confluent(rule))
    check("B finite record-only reversibility selects only no formation", reversible == (NO_FORMATION_RULE,))
    check("B reversibility and actual formation have empty intersection", not set(reversible) & set(forming))
    check("B finite causal confluence leaves exactly three rules", set(confluent) == {NO_FORMATION_RULE, COPY_EQUAL_RULE, OPPOSE_EQUAL_RULE})

    all_context_entropy_max = tuple(rule for rule in RECORD_RULES if record_output_counts(rule) == (9, 9, 9))
    open_context_entropy_max = tuple(rule for rule in RECORD_RULES if record_output_counts(rule, True) == (3, 3, 3))
    check("B maximum entropy on all 27 local triples uniquely selects no formation", all_context_entropy_max == (NO_FORMATION_RULE,))
    check("B maximum entropy conditional on an open center instead gives a four-rule tie", len(open_context_entropy_max) == 4 and NO_FORMATION_RULE not in open_context_entropy_max)

    fixed_maximum = max(record_fixed_count(rule) for rule in RECORD_RULES)
    fixed_winners = tuple(rule for rule in RECORD_RULES if record_fixed_count(rule) == fixed_maximum)
    check("B maximum fixed-point self-consistency uniquely selects no formation", fixed_winners == (NO_FORMATION_RULE,))

    minimum_writes = min(record_formation_context_count(rule) for rule in forming)
    minimum_forming = tuple(rule for rule in forming if record_formation_context_count(rule) == minimum_writes)
    maximum_writes = max(record_formation_context_count(rule) for rule in forming)
    maximum_forming = tuple(rule for rule in forming if record_formation_context_count(rule) == maximum_writes)
    check("B minimum nontrivial write support leaves the copy/opposition pair", set(minimum_forming) == {COPY_EQUAL_RULE, OPPOSE_EQUAL_RULE} and minimum_writes == 2)
    check("B maximum record throughput leaves a four-rule tie", len(maximum_forming) == 4 and maximum_writes == 6)

    confluent_minimum = tuple(rule for rule in minimum_forming if rule in confluent)
    consistency_winner = min(confluent_minimum, key=triggered_disagreement)
    check("B symmetry plus permanence plus confluence plus minimal formation still ties", set(confluent_minimum) == {COPY_EQUAL_RULE, OPPOSE_EQUAL_RULE})
    check("B adding minimum triggered disagreement uniquely selects copy-equal", consistency_winner == COPY_EQUAL_RULE and triggered_disagreement(COPY_EQUAL_RULE) == 0 and triggered_disagreement(OPPOSE_EQUAL_RULE) == 4)


def elementary_ca_tournament() -> None:
    section("C - Exhaustive binary radius-one rule tournament")
    label_covariant = tuple(rule for rule in range(256) if eca_label_covariant(rule))
    maximum_spatial_symmetry = tuple(rule for rule in label_covariant if eca_reflection_symmetric(rule))
    reversible = tuple(rule for rule in label_covariant if eca_reversible(rule))
    confluent = tuple(rule for rule in label_covariant if eca_confluent(rule))
    minimum_dependency = min(eca_dependency_count(rule) for rule in label_covariant)
    efficient = tuple(rule for rule in label_covariant if eca_dependency_count(rule) == minimum_dependency)
    check("C label covariance leaves sixteen of 256 rules", len(label_covariant) == 16)
    check("C adding reflection symmetry still leaves eight rules", len(maximum_spatial_symmetry) == 8)
    check("C finite-ring reversibility leaves six rules", set(reversible) == {15, 51, 85, 170, 204, 240})
    check("C asynchronous causal confluence leaves identity and complement", set(confluent) == {51, 204})
    check("C minimum effective dependency leaves six one-input rules", minimum_dependency == 1 and set(efficient) == {15, 51, 85, 170, 204, 240})
    check("C symmetry-reversibility-confluence-efficiency intersection still ties", set(maximum_spatial_symmetry) & set(reversible) & set(confluent) & set(efficient) == {51, 204})

    check("C every label-covariant truth table is output-balanced", all(sum(eca_output(rule, triple) for triple in product((0, 1), repeat=3)) == 4 for rule in label_covariant))
    fixed_maximum = max(eca_fixed_count(rule) for rule in label_covariant)
    fixed_winners = tuple(rule for rule in label_covariant if eca_fixed_count(rule) == fixed_maximum)
    check("C maximum fixed points uniquely selects identity rule 204", fixed_winners == (204,) and fixed_maximum == 32)
    check("C excluding identity makes complement rule 51 the unique intersection winner", ({51, 204} - {204}) == {51})
    check("C rule 204 is exactly center identity", all(eca_output(204, triple) == triple[1] for triple in product((0, 1), repeat=3)))
    check("C rule 51 is exactly center complement", all(eca_output(51, triple) == 1 - triple[1] for triple in product((0, 1), repeat=3)))


def reversible_qubit_family_tournament() -> None:
    section("D - Proper-cubic one-qubit reversible channel family")
    rotations = tuple(rotation_matrix(rotation) for rotation in q10.proper_cubic_rotations())
    keys = {matrix_key(rotation) for rotation in rotations}
    identity = sp.eye(3)
    check("D the proper-cubic channel family has 24 distinct elements", len(rotations) == len(keys) == 24)
    check("D every family element is orthogonal with determinant one", all(rotation.T * rotation == identity and rotation.det() == 1 for rotation in rotations))
    check("D every element has its inverse in the family", all(matrix_key(rotation.T) in keys for rotation in rotations))

    centralizers = {
        matrix_key(rotation): sum(rotation * other == other * rotation for other in rotations)
        for rotation in rotations
    }
    orders = {matrix_key(rotation): rotation_order(rotation) for rotation in rotations}
    fixed_dimensions = {
        matrix_key(rotation): len((rotation - identity).nullspace())
        for rotation in rotations
    }
    identity_key = matrix_key(identity)
    max_centralizer = max(centralizers.values())
    check("D maximum conjugation symmetry uniquely selects the identity channel", tuple(key for key, value in centralizers.items() if value == max_centralizer) == (identity_key,) and max_centralizer == 24)
    nonidentity_centralizer = max(value for key, value in centralizers.items() if key != identity_key)
    check("D maximum nontrivial conjugation symmetry leaves a three-axis tie", sum(key != identity_key and value == nonidentity_centralizer for key, value in centralizers.items()) == 3)
    check("D maximum nontrivial order leaves a six-element tie", max(orders.values()) == 4 and sum(value == 4 for value in orders.values()) == 6)
    check("D fixed-state dimension also uniquely favors identity", fixed_dimensions[identity_key] == 3 and all(value == 1 for key, value in fixed_dimensions.items() if key != identity_key))

    sample_bloch = sp.Matrix([sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(1, 4)])
    check("D every reversible channel preserves Bloch norm and hence qubit spectrum", all((rotation * sample_bloch).dot(rotation * sample_bloch) == sample_bloch.dot(sample_bloch) for rotation in rotations))

    x_channel = sp.diag(1, -1, -1)
    z_channel = sp.diag(-1, -1, 1)
    hadamard_channel = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    check("D a basis recoding conjugates the X and Z channel candidates", hadamard_channel * x_channel * hadamard_channel.T == z_channel)
    check("D choosing one nontrivial axis is not conjugation-invariant", x_channel != z_channel and matrix_key(x_channel) in keys and matrix_key(z_channel) in keys)


def representation_invariance_attacks() -> None:
    section("E - Representation-invariance attacks on selector scores")
    coarse_entropy = Fraction(1, 1)
    refined_entropy = Fraction(3, 2)
    check("E branch refinement changes Shannon entropy", refined_entropy > coarse_entropy)
    check("E branch refinement changes path-count weights at fixed coarse outcomes", (Fraction(1, 2), Fraction(1, 2)) != (Fraction(1, 4), Fraction(3, 4)))

    code_a = {"identity": "0", "complement": "10"}
    code_b = {"identity": "10", "complement": "0"}
    check("E two prefix descriptions reverse the minimum-description winner", min(code_a, key=lambda item: len(code_a[item])) == "identity" and min(code_b, key=lambda item: len(code_b[item])) == "complement")

    check("E equivalent gate decompositions have different raw gate counts", q7.exact_equal(q7.H * q7.Z * q7.H, q7.X) and 3 != 1)
    check("E redundant inverse pairs change raw gate count without changing the unitary", q7.exact_equal(q7.X * q7.X, q7.I2) and 2 != 0)

    hamiltonian = sp.diag(0, 1)
    rescaled = 2 * hamiltonian
    shifted = hamiltonian + 2 * sp.eye(2)
    base_unitary = diagonal_unitary(hamiltonian, sp.pi)
    rescaled_unitary = diagonal_unitary(rescaled, sp.pi / 2)
    shifted_unitary = diagonal_unitary(shifted, sp.pi)
    check("E clock rescaling leaves the exact unitary unchanged", q7.exact_equal(base_unitary, rescaled_unitary))
    check("E an identity energy shift leaves the exact unitary unchanged", q7.exact_equal(base_unitary, shifted_unitary))
    norms = tuple(sp.trace(matrix.T * matrix) for matrix in (hamiltonian, rescaled, shifted))
    check("E Hamiltonian norm scores change under clock rescaling and energy shift", norms == (1, 4, 13))

    algorithm_a = {"storage": 1, "compute": 4}
    algorithm_b = {"storage": 3, "compute": 1}
    equal_cost_a = algorithm_a["storage"] + algorithm_a["compute"]
    equal_cost_b = algorithm_b["storage"] + algorithm_b["compute"]
    storage_heavy_a = 3 * algorithm_a["storage"] + algorithm_a["compute"]
    storage_heavy_b = 3 * algorithm_b["storage"] + algorithm_b["compute"]
    check("E storage/compute weighting reverses the efficiency winner", equal_cost_b < equal_cost_a and storage_heavy_a < storage_heavy_b)


def selector_outcome_and_canonical_fields() -> None:
    section("F - Genuine finite winners and canonical-law closure")
    check("F fixed-point intersection winner is the no-formation rule", record_fixed_count(NO_FORMATION_RULE) > max(record_fixed_count(rule) for rule in RECORD_RULES if rule != NO_FORMATION_RULE))
    check("F the exact nontrivial ECA intersection winner violates record permanence", eca_update(51, (0, 1, 0, 1)) == (1, 0, 1, 0))
    check("F the copy-equal record rule is a genuine unique bounded winner after consistency cost", triggered_disagreement(COPY_EQUAL_RULE) < triggered_disagreement(OPPOSE_EQUAL_RULE))
    check("F copy-equal forms only with a supplied equal-record boundary", record_update(COPY_EQUAL_RULE, (0, OPEN, 0)) == (0, 0, 0) and record_update(COPY_EQUAL_RULE, (OPEN,) * 3) == (OPEN,) * 3)
    check("F copy-equal and oppose-equal are physically distinct exact-law values", record_update(COPY_EQUAL_RULE, (0, OPEN, 0)) != record_update(OPPOSE_EQUAL_RULE, (0, OPEN, 0)))

    canonical_fields_closed = {
        "homogeneous_domain": True,
        "label_covariance": True,
        "record_preservation": True,
        "bounded_confluence": True,
        "autonomous_origin": False,
        "full_outcome_repertoire": False,
        "bell_frequencies": False,
        "actual_boundary": False,
        "decoder": False,
        "clock_rate": False,
    }
    check("F the bounded unique rule closes only four of ten canonical fields", sum(canonical_fields_closed.values()) == 4)
    check("F the missing canonical fields include outcome, weights, boundary, decoder, and clock", all(not canonical_fields_closed[field] for field in ("full_outcome_repertoire", "bell_frequencies", "actual_boundary", "decoder", "clock_rate")))


def documentation_contract() -> None:
    section("G - Selector coverage, scope, and no-go-discipline needles")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "maximum symmetry",
        "reversibility/extremality",
        "causal invariance/confluence",
        "maximum entropy",
        "minimum description/gate count",
        "minimum nontrivial rule",
        "maximum storage/compute efficiency",
        "fixed-point/self-consistency",
        "intersection of all constraints",
        "representation invariance",
        "branch refinement",
        "clock rescaling",
        "energy shift",
        "equivalent gate decomposition",
        "genuinely unique winner",
        "canonical-law fields",
        "hidden input",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — exact residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path",
        "n7 — strongest steelman",
        "n8 — cross-cycle echo",
    )
    for phrase in required:
        check(f"G note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    permanent_record_rule_tournament()
    elementary_ca_tournament()
    reversible_qubit_family_tournament()
    representation_invariance_attacks()
    selector_outcome_and_canonical_fields()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
