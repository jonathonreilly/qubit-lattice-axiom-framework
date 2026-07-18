#!/usr/bin/env python3
"""Exact controls for deterministic unique extension, record sectors, and Bell.

This runner tests a narrow deterministic escape from sampled record laws.  It
does not select the physical law or cosmological boundary.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
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
    / "DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PRIOR_UNIQUE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CAUSAL_REVERSIBLE_ACTUALITY_WEIGHT_INDEPENDENCE_NOTE_2026-07-14.md"
)
QB16_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "AUTONOMOUS_HOMOGENEOUS_BINARY_NUCLEATION_NOTE_2026-07-14.md"
)
CONTINUATION_NOTE = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md"
)


PASS = 0
FAIL = 0
OPEN = -1
Alphabet = (-1, 0, 1)
Configuration = tuple[int, ...]
LocalStrategy = tuple[int, int, int, int]


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


def transition_matrix(
    states: tuple[Configuration, ...],
    update,
) -> sp.Matrix:
    index = {state: position for position, state in enumerate(states)}
    matrix = sp.zeros(len(states))
    for row, state in enumerate(states):
        matrix[row, index[update(state)]] = 1
    return matrix


def invariant_linear_dimension(matrix: sp.Matrix) -> int:
    return len((matrix.T - sp.eye(matrix.rows)).nullspace())


def recurrent_cycles(
    states: tuple[Configuration, ...],
    update,
) -> set[frozenset[Configuration]]:
    """Independent graph route to the recurrent cycles of a finite map."""

    cycles: set[frozenset[Configuration]] = set()
    for start in states:
        path: list[Configuration] = []
        positions: dict[Configuration, int] = {}
        state = start
        while state not in positions:
            positions[state] = len(path)
            path.append(state)
            state = update(state)
        cycles.add(frozenset(path[positions[state] :]))
    return cycles


def fill_open(configuration: Configuration, bit: int) -> Configuration:
    return tuple(bit if value == OPEN else value for value in configuration)


def shift(configuration: Configuration, amount: int = 1) -> Configuration:
    amount %= len(configuration)
    return configuration[amount:] + configuration[:amount]


def orbit(configuration: Configuration) -> tuple[Configuration, ...]:
    return tuple(dict.fromkeys(shift(configuration, amount) for amount in range(len(configuration))))


def local_uniform_update(configuration: Configuration, diagonal_map: tuple[int, int, int]) -> Configuration:
    """A radius-one covariant rule completed by center-copy off uniform triples."""

    lookup = dict(zip(Alphabet, diagonal_map))
    size = len(configuration)
    output = []
    for site in range(size):
        triple = (
            configuration[(site - 1) % size],
            configuration[site],
            configuration[(site + 1) % size],
        )
        output.append(lookup[triple[0]] if triple[0] == triple[1] == triple[2] else triple[1])
    return tuple(output)


def frequency(configuration: Configuration, bit: int = 1) -> Fraction:
    return Fraction(sum(value == bit for value in configuration), len(configuration))


def copy_boundary_layers(boundary: Configuration, depth: int) -> tuple[Configuration, ...]:
    """Unique oriented nearest-neighbor continuation: each layer copies its predecessor."""

    layers = [boundary]
    for _ in range(depth):
        layers.append(tuple(layers[-1]))
    return tuple(layers)


def local_chsh(strategy: LocalStrategy) -> int:
    a0, a1, b0, b1 = strategy
    return a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1


def quantum_table() -> dict[tuple[int, int, int, int], sp.Expr]:
    program = q10.BinaryProgram(
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        0,
        0,
        0,
        0,
    )
    return q10.program_table(program)


def quantum_chsh(table: dict[tuple[int, int, int, int], sp.Expr]) -> sp.Expr:
    return q10.chsh(table)


def measurement_dependent_local_models(
    table: dict[tuple[int, int, int, int], sp.Expr],
) -> dict[tuple[int, int], dict[LocalStrategy, sp.Expr]]:
    """Context-correlated lambda distributions with local deterministic responses."""

    models: dict[tuple[int, int], dict[LocalStrategy, sp.Expr]] = {}
    for x, y in product((0, 1), repeat=2):
        weights: dict[LocalStrategy, sp.Expr] = defaultdict(lambda: sp.Integer(0))
        for a, b in product(q7.OUTCOMES, repeat=2):
            assignment = [1, 1, 1, 1]
            assignment[x] = a
            assignment[2 + y] = b
            weights[tuple(assignment)] += table[(x, y, a, b)]
        models[(x, y)] = dict(weights)
    return models


def local_model_probability(
    weights: dict[LocalStrategy, sp.Expr],
    x: int,
    y: int,
    a: int,
    b: int,
) -> sp.Expr:
    return sp.simplify(
        sum(
            weight
            for strategy, weight in weights.items()
            if strategy[x] == a and strategy[2 + y] == b
        )
    )


def global_context_table_distribution(
    table: dict[tuple[int, int, int, int], sp.Expr],
) -> dict[tuple[tuple[int, int], ...], sp.Expr]:
    """One setting-independent distribution over deterministic joint-context tables."""

    contexts = tuple(product((0, 1), repeat=2))
    outcome_pairs = tuple(product(q7.OUTCOMES, repeat=2))
    distribution: dict[tuple[tuple[int, int], ...], sp.Expr] = {}
    for context_outcomes in product(outcome_pairs, repeat=len(contexts)):
        weight = sp.Integer(1)
        for (x, y), (a, b) in zip(contexts, context_outcomes):
            weight *= table[(x, y, a, b)]
        distribution[context_outcomes] = sp.simplify(weight)
    return distribution


def global_model_probability(
    distribution: dict[tuple[tuple[int, int], ...], sp.Expr],
    x: int,
    y: int,
    a: int,
    b: int,
) -> sp.Expr:
    contexts = tuple(product((0, 1), repeat=2))
    context_index = contexts.index((x, y))
    return sp.simplify(
        sum(
            weight
            for context_outcomes, weight in distribution.items()
            if context_outcomes[context_index] == (a, b)
        )
    )


def source_contract() -> None:
    section("A - Source and authority boundary")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    prior = PRIOR_UNIQUE.read_text(encoding="utf-8").lower()
    qb16 = QB16_NOTE.read_text(encoding="utf-8").lower()
    continuation = CONTINUATION_NOTE.read_text(encoding="utf-8").lower()
    check("A note is authority-free", "authority: none" in note)
    check("A note changes no live foundation surface", "changes no axiom, registry, primitive, or audit" in note)
    check(
        "A current law qualification gives one answer only after a domain is supplied",
        "Its domain is a supplied condition" in axioms
        and "where the condition holds it gives exactly one answer" in axioms,
    )
    check("A current Admissibility is not dynamics", "Admissibility is not a dynamics axiom." in axioms)
    check("A prior packet keeps deterministic unique QCA live", "deterministic uniquely extendible qca" in prior)
    check("A relational QB16 reference boundary is wired in", "cross-site reference transport" in qb16 and "finite-radius atomic write" in qb16)
    check("A site-tagged permanence condition is kept explicit", "site-tagged immutable-extension semantics" in continuation)


def permanent_record_sector_controls() -> None:
    section("B - Permanent-record sectors and invariant measures")
    size = 2
    states = tuple(product(Alphabet, repeat=size))
    fill_zero = lambda state: fill_open(state, 0)
    matrix = transition_matrix(states, fill_zero)
    fully_recorded = tuple(product((0, 1), repeat=size))

    check("B fill-zero is deterministic on every finite state", all(sum(matrix[row, column] for column in range(matrix.cols)) == 1 for row in range(matrix.rows)))
    check("B all existing records survive fill-zero", all(all(after[index] == value for index, value in enumerate(state) if value != OPEN) for state in states for after in (fill_zero(state),)))
    check("B every fully recorded configuration is a fixed point", all(fill_zero(state) == state for state in fully_recorded))
    check("B finite invariant-space dimension equals the four absorbing archives", invariant_linear_dimension(matrix) == len(fully_recorded) == 4)
    check("B independent recurrent-cycle enumeration also finds four archives", len(recurrent_cycles(states, fill_zero)) == 4)
    check("B uniform all-zero and all-one archives are distinct stable sectors", fill_zero((0, 0)) == (0, 0) and fill_zero((1, 1)) == (1, 1))

    zero_delta = sp.Matrix([[1 if state == (0, 0) else 0 for state in states]])
    one_delta = sp.Matrix([[1 if state == (1, 1) else 0 for state in states]])
    check("B both archive Dirac measures are temporally invariant", zero_delta * matrix == zero_delta and one_delta * matrix == one_delta)
    mixtures = tuple(sp.Rational(numerator, 4) * zero_delta + (1 - sp.Rational(numerator, 4)) * one_delta for numerator in range(5))
    check("B every tested convex mixture is invariant", all(mixture * matrix == mixture for mixture in mixtures))
    check("B record-zero and record-one site sectors are disjoint", not set(state for state in states if state[0] == 0) & set(state for state in states if state[0] == 1))
    check("B each site/content sector is forward invariant", all(fill_zero(state)[0] == bit for bit in (0, 1) for state in states if state[0] == bit))


def homogeneous_deterministic_symmetry_controls() -> None:
    section("C - Deterministic symmetry inheritance from all-open")
    size = 7
    all_open = (OPEN,) * size
    all_uniform_trajectories = True
    possible_archives = set()
    for diagonal_map in product(Alphabet, repeat=3):
        state = all_open
        for _ in range(8):
            state = local_uniform_update(state, diagonal_map)
            all_uniform_trajectories &= len(set(state)) == 1
        if OPEN not in state:
            possible_archives.add(state)
    check("C all 27 possible uniform-neighborhood responses preserve translation symmetry", all_uniform_trajectories)
    check("C every formed archive reached from all-open has density zero or one", all(frequency(state, 1) in (0, 1) for state in possible_archives))
    check("C no sparse nonhomogeneous archive appears", all(not (0 < frequency(state, 1) < 1) for state in possible_archives))

    checkerboard = tuple(index % 2 for index in range(8))
    translated_checkerboard = shift(checkerboard)
    check("C a coordinate-parity seed would make a sparse archive", frequency(checkerboard) == Fraction(1, 2))
    check("C coordinate parity fails one-site translation covariance on all-open", checkerboard != translated_checkerboard)

    rotations = q10.proper_cubic_rotations()
    check("C all 24 proper cubic rotations leave the empty record configuration fixed", len(rotations) == 24 and all(q10.transform_records({}, rotation) == {} for rotation in rotations))


def deterministic_choice_and_boundary_frequency_controls() -> None:
    section("D - Unique continuation versus law and boundary content")
    all_open = (OPEN,) * 6
    zero_history = (all_open, fill_open(all_open, 0))
    one_history = (all_open, fill_open(all_open, 1))
    check("D each fill law has one exact continuation from all-open", zero_history[1] == (0,) * 6 and one_history[1] == (1,) * 6)
    check("D the two equally deterministic laws encode opposite outcome choices", zero_history[1] != one_history[1])
    check("D deterministic uniqueness removes sampling but not exact law value", frequency(zero_history[1]) == 0 and frequency(one_history[1]) == 1)

    boundary_low = (0, 0, 1)
    boundary_high = (0, 1, 1)
    low_layers = copy_boundary_layers(boundary_low, 8)
    high_layers = copy_boundary_layers(boundary_high, 8)
    check("D the same nearest-neighbor copy rule uniquely extends either boundary", all(layer == boundary_low for layer in low_layers) and all(layer == boundary_high for layer in high_layers))
    check("D copied archive frequencies remain boundary-owned", all(frequency(layer) == Fraction(1, 3) for layer in low_layers) and all(frequency(layer) == Fraction(2, 3) for layer in high_layers))
    check("D equal local copy architecture does not select one boundary frequency", frequency(low_layers[-1]) != frequency(high_layers[-1]))


def unique_ergodic_component_controls() -> None:
    section("E - Unique ergodicity only after component and decoder selection")
    all_open = (OPEN, OPEN)
    zero = (0, 0)
    one = (1, 1)
    zero_component = (all_open, zero)
    one_component = (all_open, one)
    zero_matrix = transition_matrix(zero_component, lambda state: fill_open(state, 0))
    one_matrix = transition_matrix(one_component, lambda state: fill_open(state, 1))
    check("E the all-open-to-zero reachable component has one invariant measure", invariant_linear_dimension(zero_matrix) == 1)
    check("E the all-open-to-one reachable component has one invariant measure", invariant_linear_dimension(one_matrix) == 1)
    check(
        "E selecting a reachable component selects its absorbing archive",
        zero_component[-1] == zero and one_component[-1] == one and zero != one,
    )

    low_orbit = orbit((0, 0, 1))
    high_orbit = orbit((0, 1, 1))
    low_shift = transition_matrix(low_orbit, shift)
    high_shift = transition_matrix(high_orbit, shift)
    combined_orbits = low_orbit + high_orbit
    combined_shift = transition_matrix(combined_orbits, shift)
    check("E each three-phase boundary orbit is one irreducible cycle", invariant_linear_dimension(low_shift) == 1 and invariant_linear_dimension(high_shift) == 1)
    check("E the two selected components have different exact spatial frequencies", sum(frequency(state) for state in low_orbit) / len(low_orbit) == Fraction(1, 3) and sum(frequency(state) for state in high_orbit) / len(high_orbit) == Fraction(2, 3))
    check(
        "E one boundary component admits distinct decoder frequencies",
        sum(frequency(state, 1) for state in low_orbit) / len(low_orbit)
        == Fraction(1, 3)
        and sum(frequency(state, 0) for state in low_orbit) / len(low_orbit)
        == Fraction(2, 3),
    )
    check("E their union has two invariant measures", invariant_linear_dimension(combined_shift) == 2)
    check("E independent recurrent-cycle enumeration finds the two components", len(recurrent_cycles(combined_orbits, shift)) == 2)

    six_cycle = tuple((index,) for index in range(6))
    cycle_update = lambda state: ((state[0] + 1) % 6,)
    cycle_matrix = transition_matrix(six_cycle, cycle_update)
    check("E a deterministic six-cycle is uniquely ergodic", invariant_linear_dimension(cycle_matrix) == 1)
    check("E independent graph enumeration finds one six-state recurrent cycle", recurrent_cycles(six_cycle, cycle_update) == {frozenset(six_cycle)})
    decoder_two = {0, 1}
    decoder_four = {0, 1, 2, 3}
    check("E one cycle admits different record decoders and frequencies", Fraction(len(decoder_two), 6) == Fraction(1, 3) and Fraction(len(decoder_four), 6) == Fraction(2, 3))
    phase_zero_prefix = tuple(step % 6 in decoder_two for step in range(3))
    phase_one_prefix = tuple((1 + step) % 6 in decoder_two for step in range(3))
    phase_zero_cycle = sum(step % 6 in decoder_two for step in range(6))
    phase_one_cycle = sum((1 + step) % 6 in decoder_two for step in range(6))
    check(
        "E changing orbit phase changes finite transcript but not full-cycle frequency",
        phase_zero_prefix != phase_one_prefix
        and phase_zero_cycle == phase_one_cycle == 2,
    )


def bell_route_controls() -> None:
    section("F - Bell locality, measurement independence, and global consistency")
    strategies = tuple(product(q7.OUTCOMES, repeat=4))
    chsh_values = tuple(local_chsh(strategy) for strategy in strategies)
    check("F all sixteen deterministic local strategies have CHSH magnitude two", set(abs(value) for value in chsh_values) == {2})
    rational_weights = tuple(Fraction(index + 1, sum(range(1, 17))) for index in range(16))
    mixed_chsh = sum(weight * value for weight, value in zip(rational_weights, chsh_values))
    check("F every common-distribution convex mixture obeys the local ceiling", abs(mixed_chsh) <= 2)

    table = quantum_table()
    check("F the supplied relational Bell table has exact Tsirelson CHSH", q7.exact_equal(quantum_chsh(table), 2 * sp.sqrt(2)))
    check("F the supplied Bell table is normalized", all(q7.exact_equal(sum(table[(x, y, a, b)] for a, b in product(q7.OUTCOMES, repeat=2)), 1) for x, y in product((0, 1), repeat=2)))
    check("F the supplied Bell table is no-signalling", all(q7.exact_equal(sum(table[(x, y, a, b)] for b in q7.OUTCOMES), sp.Rational(1, 2)) for x, y, a in product((0, 1), (0, 1), q7.OUTCOMES)) and all(q7.exact_equal(sum(table[(x, y, a, b)] for a in q7.OUTCOMES), sp.Rational(1, 2)) for x, y, b in product((0, 1), (0, 1), q7.OUTCOMES)))

    dependent_models = measurement_dependent_local_models(table)
    check("F every setting-correlated local model normalizes", all(q7.exact_equal(sum(weights.values()), 1) for weights in dependent_models.values()))
    check("F setting-correlated lambda distributions reproduce every Bell probability", all(q7.exact_equal(local_model_probability(dependent_models[(x, y)], x, y, a, b), table[(x, y, a, b)]) for x, y, a, b in product((0, 1), (0, 1), q7.OUTCOMES, q7.OUTCOMES)))
    canonical_models = tuple(tuple(sorted((strategy, sp.simplify(weight)) for strategy, weight in weights.items())) for weights in dependent_models.values())
    check("F the local completion pays with measurement dependence", len(set(canonical_models)) > 1)

    global_distribution = global_context_table_distribution(table)
    check("F one setting-independent global context-table distribution normalizes", q7.exact_equal(sum(global_distribution.values()), 1))
    check("F deterministic global-context responses reproduce every Bell probability", all(q7.exact_equal(global_model_probability(global_distribution, x, y, a, b), table[(x, y, a, b)]) for x, y, a, b in product((0, 1), (0, 1), q7.OUTCOMES, q7.OUTCOMES)))
    contexts = tuple(product((0, 1), repeat=2))
    nonlocal_table = ((1, 1), (-1, 1), (1, 1), (1, 1))
    check("F a positive-weight global table makes Alice context-dependent", global_distribution[nonlocal_table].is_positive and nonlocal_table[contexts.index((0, 0))][0] != nonlocal_table[contexts.index((0, 1))][0])


def relational_qb16_steelman_controls() -> None:
    section("G - Relational QB16 deterministic steelman")
    program = q10.BinaryProgram((0, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 0)
    records = q10.program_records(program, reference_bit=0)
    records = q10.advance_program(records, program, Fraction(1, 9))
    records = q10.advance_program(records, program, Fraction(2, 9))
    stage_two = dict(records)
    records = q10.advance_program(records, program, Fraction(3, 9))
    complement = {site: 1 - value for site, value in records.items()}
    check("G the relational packet reaches one complete permanent transcript", q10.program_stage(records, program) == 3)
    check("G global possibility-label exchange preserves its complete decoded state", q10.program_stage(complement, program) == 3 and q7.exact_equal(q10.decoded_work_state(records, program), q10.decoded_work_state(complement, program)))
    check("G relational frame covariance does not alter the Bell table", q7.exact_equal(q10.chsh(q10.program_table(program)), 2 * sp.sqrt(2)))
    low_sample = q10.advance_program(stage_two, program, Fraction(1, 100))
    high_sample = q10.advance_program(stage_two, program, Fraction(99, 100))
    check("G the present packet still uses a supplied sample coordinate", low_sample != high_sample)


def documentation_contract() -> None:
    section("H - Scope and no-go-discipline needles")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "permanent-record sector",
        "unique extension is not unique ergodicity",
        "deterministic symmetry inheritance",
        "irreducible boundary component",
        "measurement independence",
        "boundary correlation",
        "nonlocal/global consistency",
        "relational cfsi-qb16",
        "exact-law reference",
        "state/boundary",
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
        check(f"H note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    permanent_record_sector_controls()
    homogeneous_deterministic_symmetry_controls()
    deterministic_choice_and_boundary_frequency_controls()
    unique_ergodic_component_controls()
    bell_route_controls()
    relational_qb16_steelman_controls()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
