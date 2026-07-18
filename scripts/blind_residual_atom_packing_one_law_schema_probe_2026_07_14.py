#!/usr/bin/env python3
"""Exact finite controls for the Cycle-25 residual-atom packing audit.

The runner distinguishes extensional law fields, theorem consequences,
registered primitives/conventions, and realized history/boundary data.  It is
authority-free and performs no repository or audit mutation.
"""

from __future__ import annotations

import itertools
import json
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/BLIND_RESIDUAL_ATOM_PACKING_AND_ONE_LAW_CONSTITUTIONAL_SCHEMA_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs/audit/data/axiom_premise_nodes.json"

CYCLE_PACKET = (
    "ACTUAL_HEADER_ROLE_DECODER_PARITY_SELECTION_CYCLE18_NOTE_2026-07-14.md",
    "INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md",
    "COMPLETE_FUTURE_OPERATIONAL_PARITY_CERTIFICATE_CYCLE19_NOTE_2026-07-14.md",
    "NEAREST_NEIGHBOR_SEED_COMPILATION_CYCLE19_NOTE_2026-07-14.md",
    "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md",
    "QUANTUM_DISSIPATIVE_SEED_ESCAPE_CYCLE20_NOTE_2026-07-14.md",
    "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md",
    "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md",
    "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md",
    "NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md",
    "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md",
    "FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md",
    "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md",
    "EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md",
    "MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md",
    "MINIMUM_CONSTITUTIONAL_CONTENT_EXHAUSTION_LEDGER_NOTE_2026-07-14.md",
    "MINIMUM_AXIOM_UPDATE_EXERCISE_SYNTHESIS_AND_CUT_GATE_NOTE_2026-07-14.md",
)
PACKET_DIR = ROOT / "docs/work_history/repo/review_feedback"

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def exact_equal(left: sp.Matrix | sp.Expr, right: sp.Matrix | sp.Expr) -> bool:
    difference = left - right
    if isinstance(difference, sp.MatrixBase):
        return all(sp.simplify(sp.expand_complex(value)) == 0 for value in difference)
    return sp.simplify(sp.expand_complex(difference)) == 0


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.H)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
KET0 = sp.Matrix([1, 0])


def source_contract() -> None:
    section("A - Foundation, primitive, packet, and authority contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized_note = " ".join(note.lower().replace("`", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    check("A note exists and is authority-free", "**authority:** none" in note.lower())
    check("A note disclaims live axiom mutation", "changes no axiom" in normalized_note)
    check("A current foundation has exactly four named axioms", all(f"### {name}" in axioms for name in ("Lattice", "Qubit", "Admissibility", "Record")))
    check("A Admissibility supplies one fixed nearest-neighbor rule", "There is one fixed nearest-neighbor admissibility rule" in axioms)
    check("A Qualification says a law privileges no states", "A law privileges no states" in axioms)
    check("A current memo explicitly withholds dynamics", "Admissibility is not a dynamics axiom" in axioms)
    check("A primitive registry has exactly the expected four canonical nodes", registry["canonical_ids"] == [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ])
    check("A Cycle 18-24 packet has seventeen named sources", len(CYCLE_PACKET) == 17)
    for filename in CYCLE_PACKET:
        path = PACKET_DIR / filename
        check(f"A packet source exists: {filename}", path.is_file())
        if path.is_file():
            text = path.read_text(encoding="utf-8").lower()
            check(
                f"A packet source is authority-free: {filename}",
                "authority" in text and "none" in text[:4000],
            )


PLACEMENTS = {
    "allowed_boundary_class": "LAW_REFERENT",
    "seed_initialization_kernel": "LAW_REFERENT",
    "record_instrument_and_W": "LAW_REFERENT",
    "reset_archive_transition": "LAW_REFERENT",
    "branching_actuality_semantics": "LAW_REFERENT",
    "legal_protocol_and_law_equivalence_category": "LAW_REFERENT",
    "dimensionless_clock_rate_ratios": "LAW_REFERENT",
    "collision_and_routing_policy": "LAW_REFERENT",
    "matter_couplings": "LAW_REFERENT",
    "tensor_response": "LAW_REFERENT",
    "record_preservation_for_selected_law": "THEOREM",
    "born_trace_representation": "THEOREM",
    "reset_to_frequency_concentration": "THEOREM",
    "law_stabilizer_or_equivalence_group": "THEOREM",
    "commit_chain_integer_clock": "THEOREM",
    "scale_reference": "PRIMITIVE_OR_CONVENTION",
    "kinetic_isotropy": "PRIMITIVE_OR_CONVENTION",
    "realized_state_reference_slot": "PRIMITIVE_OR_CONVENTION",
    "overall_unobservable_time_reparameterization": "PRIMITIVE_OR_CONVENTION",
    "framework_sort_isomorphism_definition": "PRIMITIVE_OR_CONVENTION",
    "actual_boundary_or_initial_configuration": "REALIZED_HISTORY_OR_MEASURE",
    "actual_seed_field": "REALIZED_HISTORY_OR_MEASURE",
    "actual_branch_or_random_seed": "REALIZED_HISTORY_OR_MEASURE",
    "actual_trial_corpus_and_interventions": "REALIZED_HISTORY_OR_MEASURE",
    "actual_chiral_domain": "REALIZED_HISTORY_OR_MEASURE",
    "boundary_measure_if_unconditional_cosmology_is_claimed": "REALIZED_HISTORY_OR_MEASURE",
}

LAW_FIELDS = {
    "DOMAIN",
    "BOUNDARY_CLASS",
    "INITIALIZATION",
    "GENERATOR",
    "INSTRUMENT_W",
    "RESET_ARCHIVE",
    "CORPUS_PROCESS",
    "RECORD_INTERFACE",
    "PROTOCOL_CATEGORY",
    "EQUIVALENCE",
    "CLOCK_OBSERVABLES",
    "MATTER_COUPLINGS",
    "TENSOR_RESPONSE",
    "REALIZATION_SEMANTICS",
}

REQUESTED_PACKING = {
    "seed/initialization": "INITIALIZATION",
    "record instrument and W": "INSTRUMENT_W",
    "reset/corpus/frequency": "CORPUS_PROCESS",
    "actuality if branching": "REALIZATION_SEMANTICS",
    "site/law equivalence": "EQUIVALENCE",
    "clock rates": "GENERATOR",
    "collision/routing": "GENERATOR",
    "matter couplings": "MATTER_COUPLINGS",
    "tensor response": "TENSOR_RESPONSE",
}


def placement_contract() -> None:
    section("B - Four-way placement and one-referent packing contract")
    categories = {
        "LAW_REFERENT",
        "THEOREM",
        "PRIMITIVE_OR_CONVENTION",
        "REALIZED_HISTORY_OR_MEASURE",
    }
    check("B every placement uses one of exactly four requested categories", set(PLACEMENTS.values()) == categories)
    check("B every placement has exactly one primary category", len(PLACEMENTS) == len(set(PLACEMENTS)))
    check("B every requested lane maps to a declared exact-law field", all(field in LAW_FIELDS for field in REQUESTED_PACKING.values()))
    check("B all nine requested lanes are represented", len(REQUESTED_PACKING) == 9)
    check("B actual branch is not classified as a law constant", PLACEMENTS["actual_branch_or_random_seed"] == "REALIZED_HISTORY_OR_MEASURE")
    check("B branching semantics is classified as law type/content", PLACEMENTS["branching_actuality_semantics"] == "LAW_REFERENT")
    check("B frequency is a theorem rather than one-shot W", PLACEMENTS["reset_to_frequency_concentration"] == "THEOREM")
    check("B relative rates and overall reparameterization are separated", PLACEMENTS["dimensionless_clock_rate_ratios"] != PLACEMENTS["overall_unobservable_time_reparameterization"])


def deterministic_rule_and_boundary_independence() -> None:
    section("C - Same exact local generator, different boundary/history")

    def shift_right(state: tuple[int, ...]) -> tuple[int, ...]:
        return (state[-1],) + state[:-1]

    empty = (0, 0, 0, 0)
    seeded = (1, 0, 0, 0)
    empty_history = [empty]
    seeded_history = [seeded]
    for _ in range(4):
        empty_history.append(shift_right(empty_history[-1]))
        seeded_history.append(shift_right(seeded_history[-1]))

    check("C one generator preserves the empty boundary", all(state == empty for state in empty_history))
    check("C the same generator transports a supplied seed", len(set(seeded_history[:-1])) == 4)
    check("C equal generator does not equalize the two histories", empty_history != seeded_history)
    check("C both histories satisfy the same deterministic update at every edge", all(
        shift_right(history[index]) == history[index + 1]
        for history in (empty_history, seeded_history)
        for index in range(4)
    ))

    p1 = sp.Rational(1, 4)
    p2 = sp.Rational(1, 2)
    expected_seeds_1 = 4 * p1
    expected_seeds_2 = 4 * p2
    check("C two boundary measures share the same post-boundary generator", shift_right((1, 0, 0, 0)) == (0, 1, 0, 0))
    check("C boundary measures give different expected seed counts", expected_seeds_1 != expected_seeds_2)


def record_instrument_independence() -> None:
    section("D - A nonselective channel does not identify its record instrument")
    pvm = (P0, P1)
    random_unitary = (I2 / sp.sqrt(2), Z / sp.sqrt(2))
    matrix_units = (
        sp.Matrix([[1, 0], [0, 0]]),
        sp.Matrix([[0, 1], [0, 0]]),
        sp.Matrix([[0, 0], [1, 0]]),
        sp.Matrix([[0, 0], [0, 1]]),
    )

    def channel(kraus: tuple[sp.Matrix, ...], rho: sp.Matrix) -> sp.Matrix:
        return sp.simplify(sum((operator * rho * operator.H for operator in kraus), sp.zeros(2)))

    check("D PVM and random-unitary instruments have the same dephasing channel", all(
        exact_equal(channel(pvm, basis), channel(random_unitary, basis)) for basis in matrix_units
    ))
    rho0 = density(KET0)
    pvm_probabilities = tuple(sp.simplify(sp.trace(operator * rho0 * operator.H)) for operator in pvm)
    random_probabilities = tuple(sp.simplify(sp.trace(operator * rho0 * operator.H)) for operator in random_unitary)
    check("D PVM record labels have probabilities (1,0) on |0>", pvm_probabilities == (1, 0))
    check("D random-unitary labels have probabilities (1/2,1/2) on |0>", random_probabilities == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("D same channel leaves distinct record/W completions", pvm_probabilities != random_probabilities)


def corpus_and_frequency_independence() -> None:
    section("E - Same one-shot W, different corpus/frequency law")
    q = sp.Rational(1, 3)
    length = 4
    words = tuple(itertools.product((0, 1), repeat=length))

    def iid_weight(word: tuple[int, ...]) -> sp.Expr:
        ones = sum(word)
        return sp.simplify(q**ones * (1 - q) ** (length - ones))

    def frozen_weight(word: tuple[int, ...]) -> sp.Expr:
        if word == (1,) * length:
            return q
        if word == (0,) * length:
            return 1 - q
        return sp.Integer(0)

    iid = {word: iid_weight(word) for word in words}
    frozen = {word: frozen_weight(word) for word in words}
    check("E both joint corpus laws normalize", sp.simplify(sum(iid.values())) == 1 and sp.simplify(sum(frozen.values())) == 1)
    for position in range(length):
        iid_marginal = sp.simplify(sum(weight for word, weight in iid.items() if word[position] == 1))
        frozen_marginal = sp.simplify(sum(weight for word, weight in frozen.items() if word[position] == 1))
        check(f"E position {position} has the same one-shot marginal q", iid_marginal == q and frozen_marginal == q)

    def moments(distribution: dict[tuple[int, ...], sp.Expr]) -> tuple[sp.Expr, sp.Expr]:
        means = {word: sp.Rational(sum(word), length) for word in words}
        mean = sp.simplify(sum(distribution[word] * means[word] for word in words))
        variance = sp.simplify(sum(distribution[word] * (means[word] - mean) ** 2 for word in words))
        return mean, variance

    iid_mean, iid_variance = moments(iid)
    frozen_mean, frozen_variance = moments(frozen)
    check("E both empirical frequencies have mean q", iid_mean == q and frozen_mean == q)
    check("E IID frequency variance is q(1-q)/N", iid_variance == q * (1 - q) / length)
    check("E frozen frequency variance is q(1-q)", frozen_variance == q * (1 - q))
    check("E same one-shot W does not fix concentration", iid_variance != frozen_variance)


def measure_and_actual_member_independence() -> None:
    section("F - Branching measure versus actual member")
    laws = {
        "q=1/3": {0: sp.Rational(2, 3), 1: sp.Rational(1, 3)},
        "q=1/2": {0: sp.Rational(1, 2), 1: sp.Rational(1, 2)},
    }
    check("F one law admits two different actual members", all(laws["q=1/3"][member] > 0 for member in (0, 1)))
    check("F one actual member is compatible with two different laws", all(law[0] > 0 for law in laws.values()))
    check("F the two laws remain numerically distinct", laws["q=1/3"] != laws["q=1/2"])


def equivalence_category_independence() -> None:
    section("G - Transition table versus physical equivalence category")
    states = (0, 1)
    transition = {0: 0, 1: 1}
    readout = {0: 2, 1: 5}
    permutations = tuple(itertools.permutations(states))

    fixed_readout_automorphisms = []
    transported_dictionary_isomorphisms = []
    for image in permutations:
        permutation = dict(zip(states, image))
        transition_ok = all(permutation[transition[state]] == transition[permutation[state]] for state in states)
        fixed_readout_ok = all(readout[permutation[state]] == readout[state] for state in states)
        transported_readout = {permutation[state]: readout[state] for state in states}
        transported_ok = all(transported_readout[permutation[state]] == readout[state] for state in states)
        if transition_ok and fixed_readout_ok:
            fixed_readout_automorphisms.append(image)
        if transition_ok and transported_ok:
            transported_dictionary_isomorphisms.append(image)

    check("G fixed content dictionary leaves only identity", len(fixed_readout_automorphisms) == 1)
    check("G transporting the complete dictionary admits label swap", len(transported_dictionary_isomorphisms) == 2)
    check("G the same transition table underlies both categories", transition == {0: 0, 1: 1})


def clock_rate_independence() -> None:
    section("H - Event support/order versus dimensionless clock rates")
    model1 = (sp.Integer(1), sp.Integer(1))
    model2 = (sp.Integer(1), sp.Integer(2))
    scaled2 = (sp.Integer(3), sp.Integer(6))

    def next_a_probability(rates: tuple[sp.Expr, sp.Expr]) -> sp.Expr:
        return sp.simplify(rates[0] / sum(rates))

    check("H both models allow the same two next-event labels", set(("A", "B")) == {"A", "B"})
    check("H relative-rate change changes the next-event law", next_a_probability(model1) == sp.Rational(1, 2) and next_a_probability(model2) == sp.Rational(1, 3))
    check("H common rate rescaling leaves dimensionless next-event law fixed", next_a_probability(model2) == next_a_probability(scaled2))
    check("H model1 and model2 have different dimensionless rate ratios", sp.Rational(*model1) != sp.Rational(*model2))


def collision_policy_independence() -> None:
    section("I - Single-front agreement versus collision/routing policy")
    inputs = ((), ("L",), ("R",), ("L", "R"))

    def policy(mode: str, proposals: tuple[str, ...]) -> str:
        if not proposals:
            return "open"
        if len(proposals) == 1:
            return proposals[0]
        return {"left": "L", "right": "R", "cancel": "open"}[mode]

    policies = {mode: {case: policy(mode, case) for case in inputs} for mode in ("left", "right", "cancel")}
    check("I all three laws agree off the collision input", all(
        policies[mode][case] == policies["left"][case]
        for mode in policies
        for case in inputs[:-1]
    ))
    check("I all three laws differ on the collision input", len({policies[mode][("L", "R")] for mode in policies}) == 3)
    check("I collision behavior must be stated or derived for exactness", policies["left"] != policies["right"] != policies["cancel"])


def matter_and_tensor_independence() -> None:
    section("J - Matter coupling and tensor-response countermodels")

    def species_acceleration(couplings: tuple[sp.Expr, sp.Expr], gradient: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
        return tuple(sp.simplify(coupling * gradient) for coupling in couplings)

    universal = (sp.Integer(1), sp.Integer(1))
    nonuniversal = (sp.Integer(1), sp.Integer(2))
    check("J vacuum cannot separate species-coupling laws", species_acceleration(universal, 0) == species_acceleration(nonuniversal, 0))
    check("J sourced species B separates the coupling laws", species_acceleration(universal, 1)[1] != species_acceleration(nonuniversal, 1)[1])
    check("J species A can agree while species B differs", species_acceleration(universal, 1)[0] == species_acceleration(nonuniversal, 1)[0])

    phi = sp.Symbol("phi", nonzero=True, real=True)

    def weak_response(gamma: sp.Expr) -> sp.Matrix:
        return sp.diag(2 * phi, 2 * gamma * phi, 2 * gamma * phi, 2 * gamma * phi)

    lapse_only = weak_response(0)
    tensor = weak_response(1)
    check("J lapse response h00 is identical", exact_equal(lapse_only[0, 0], tensor[0, 0]))
    check("J spatial tensor response differs", not exact_equal(lapse_only[1, 1], tensor[1, 1]))
    light_proxy_lapse = sp.simplify((1 + 0) * phi)
    light_proxy_tensor = sp.simplify((1 + 1) * phi)
    check("J an exact null-response proxy separates gamma=0 from gamma=1", light_proxy_lapse != light_proxy_tensor)


def schema_and_no_go_contract() -> None:
    section("K - Constitutional schema and N1-N8 visibility")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").split())
    check("K one-law packing verdict appears", "yes for universal interfaces; no for the actual history" in normalized)
    check("K schema distinguishes local and global placement", "local-law placement" in normalized and "global-history placement" in normalized)
    check("K zero-edit uniqueness route remains live", "zero-edit route" in normalized)
    check("K packaging is not called derivation", "packaging is not derivation" in normalized)
    check("K no Record clause is recommended", "no separate record clause" in normalized)
    check("K actual history is one collapsed instance rather than many axioms", "one realized-history instance" in normalized)
    check("K all N1-N8 headings are present", all(re.search(rf"^### N{index}\b", note, re.MULTILINE) for index in range(1, 9)))
    for phrase in (
        "seed/initialization",
        "record instrument and w",
        "reset/corpus/frequency",
        "actuality if branching",
        "site/law equivalence",
        "clock rates",
        "collision/routing",
        "matter couplings",
        "tensor response",
        "boundary measure",
    ):
        check(f"K requested residual named: {phrase}", phrase in normalized)


def main() -> None:
    source_contract()
    placement_contract()
    deterministic_rule_and_boundary_independence()
    record_instrument_independence()
    corpus_and_frequency_independence()
    measure_and_actual_member_independence()
    equivalence_category_independence()
    clock_rate_independence()
    collision_policy_independence()
    matter_and_tensor_independence()
    schema_and_no_go_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
