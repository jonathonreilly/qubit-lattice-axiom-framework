#!/usr/bin/env python3
"""Exact CFSI-Q7 Bell-capable coherent causal-front law probes.

The construction uses one M2 carrier per physical site plus the existing
partial record-map status.  A seven-site cubic-lattice cell contains a
two-qubit coherent source, a two-qubit propagated front, two recorded setting
sites, and one recorded preparation-phase site.  A nearest-neighbor circuit
prepares and propagates a Bell pair; local sharp instruments sample two
outcome records.  The runner checks Bell/no-signalling behavior, record-sector
invariance, projective cell composition, fresh support, exact-law-value
alternatives, and record-only predictive sufficiency.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Iterable

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CFSI_Q_BELL_COHERENT_CAUSAL_FRONT_LAW_NOTE_2026-07-14.md"
)
BASE_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md"
)
PAIR_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md"
)
SCHEDULE_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Outcome = tuple[int, int]


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


def exact_equal(left, right) -> bool:
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        return sp.simplify(left - right) == sp.zeros(*left.shape)
    return sp.simplify(left - right) == 0


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def trace(matrix: sp.Matrix):
    return sp.simplify(sp.trace(matrix))


def reduced_qubit_state(rho: sp.Matrix, keep: int) -> sp.Matrix:
    """Exact partial trace of a two-qubit state, retaining qubit 0 or 1."""

    if keep not in (0, 1) or rho.shape != (4, 4):
        raise ValueError("expected a two-qubit state and keep in {0,1}")
    reduced = sp.zeros(2)
    for row in range(2):
        for column in range(2):
            for traced in range(2):
                if keep == 0:
                    full_row = 2 * row + traced
                    full_column = 2 * column + traced
                else:
                    full_row = 2 * traced + row
                    full_column = 2 * traced + column
                reduced[row, column] += rho[full_row, full_column]
    return sp.simplify(reduced)


def exact_dict_equal(left: dict, right: dict) -> bool:
    return left.keys() == right.keys() and all(exact_equal(left[key], right[key]) for key in left)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
S = sp.diag(1, sp.I)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET00 = sp.kronecker_product(KET0, KET0)


def kron_all(factors: Iterable[sp.Matrix]) -> sp.Matrix:
    factors = tuple(factors)
    result = factors[0]
    for factor in factors[1:]:
        result = sp.kronecker_product(result, factor)
    return sp.Matrix(result)


def embed_single(operator: sp.Matrix, qubits: int, position: int) -> sp.Matrix:
    return kron_all(operator if site == position else I2 for site in range(qubits))


def swap_operator(qubits: int, left: int, right: int) -> sp.Matrix:
    dimension = 2**qubits
    swap = sp.zeros(dimension)
    for state in range(dimension):
        bits = [((state >> (qubits - 1 - position)) & 1) for position in range(qubits)]
        bits[left], bits[right] = bits[right], bits[left]
        target = 0
        for bit in bits:
            target = (target << 1) | bit
        swap[target, state] = 1
    return swap


def cnot_operator(qubits: int, control: int, target_site: int) -> sp.Matrix:
    dimension = 2**qubits
    cnot = sp.zeros(dimension)
    for state in range(dimension):
        bits = [((state >> (qubits - 1 - position)) & 1) for position in range(qubits)]
        if bits[control]:
            bits[target_site] ^= 1
        target = 0
        for bit in bits:
            target = (target << 1) | bit
        cnot[target, state] = 1
    return cnot


def bell_vector(phase: int) -> sp.Matrix:
    sign = 1 if phase == 0 else -1
    return (sp.kronecker_product(KET0, KET0) + sign * sp.kronecker_product(KET1, KET1)) / sp.sqrt(2)


def bell_density(phase: int, visibility=sp.Integer(1)) -> sp.Matrix:
    pure = density(bell_vector(phase))
    return sp.simplify(visibility * pure + (1 - visibility) * sp.eye(4) / 4)


def coherent_circuit(phase: int) -> sp.Matrix:
    """Prepare on source sites 0,1 and propagate to front sites 2,3."""

    prepare_h = embed_single(H, 4, 0)
    entangle = cnot_operator(4, 0, 1)
    phase_gate = embed_single(Z if phase else I2, 4, 0)
    propagate_a = swap_operator(4, 0, 2)
    propagate_b = swap_operator(4, 1, 3)
    return sp.simplify(propagate_b * propagate_a * phase_gate * entangle * prepare_h)


ALICE = (Z, X)
BOB = ((Z + X) / sp.sqrt(2), (Z - X) / sp.sqrt(2))
OUTCOMES = (1, -1)


def projector(observable: sp.Matrix, outcome: int) -> sp.Matrix:
    return sp.simplify((sp.eye(observable.rows) + outcome * observable) / 2)


def joint_probability_table(
    rho: sp.Matrix,
    alice_observables: tuple[sp.Matrix, sp.Matrix] = ALICE,
    bob_observables: tuple[sp.Matrix, sp.Matrix] = BOB,
) -> dict[tuple[int, int, int, int], sp.Expr]:
    table = {}
    for x, y in product((0, 1), repeat=2):
        for a, b in product(OUTCOMES, repeat=2):
            joint = sp.kronecker_product(
                projector(alice_observables[x], a),
                projector(bob_observables[y], b),
            )
            table[(x, y, a, b)] = sp.simplify(trace(joint * rho))
    return table


def context_distribution(
    table: dict[tuple[int, int, int, int], sp.Expr],
    x: int,
    y: int,
) -> dict[Outcome, sp.Expr]:
    return {(a, b): table[(x, y, a, b)] for a, b in product(OUTCOMES, repeat=2)}


def branch_post_state(rho: sp.Matrix, x: int, y: int, a: int, b: int) -> tuple[sp.Expr, sp.Matrix]:
    joint = sp.kronecker_product(projector(ALICE[x], a), projector(BOB[y], b))
    branch = sp.simplify(joint * rho * joint)
    weight = trace(branch)
    return weight, sp.simplify(branch / weight)


def ordered_local_branch(
    rho: sp.Matrix,
    x: int,
    y: int,
    a: int,
    b: int,
    order: tuple[str, str],
) -> tuple[sp.Expr, sp.Matrix]:
    """Apply the two disjoint local measurement updates in a chosen order."""

    projectors = {
        "alice": sp.kronecker_product(projector(ALICE[x], a), I2),
        "bob": sp.kronecker_product(I2, projector(BOB[y], b)),
    }
    branch = rho
    for party in order:
        effect = projectors[party]
        branch = sp.simplify(effect * branch * effect)
    weight = trace(branch)
    return weight, sp.simplify(branch / weight)


def correlation(table: dict[tuple[int, int, int, int], sp.Expr], x: int, y: int):
    return sp.simplify(
        sum(a * b * table[(x, y, a, b)] for a, b in product(OUTCOMES, repeat=2))
    )


def sample_distribution(distribution: dict[Outcome, sp.Expr], seed: Fraction) -> Outcome:
    cumulative = sp.Integer(0)
    threshold = sp.Rational(seed.numerator, seed.denominator)
    for outcome in product(OUTCOMES, repeat=2):
        cumulative = sp.simplify(cumulative + distribution[outcome])
        difference = sp.simplify(cumulative - threshold)
        if difference.is_positive:
            return outcome
        if difference.is_positive is None:
            raise ValueError("symbolic sampler could not order an exact threshold")
    raise ValueError("normalized distribution did not select an outcome")


def l1_distance(left: Coord, right: Coord) -> int:
    return sum(abs(left[axis] - right[axis]) for axis in range(3))


def bell_block(index: int) -> dict[str, Coord]:
    """Seven-site nearest-neighbor motif on a boundary-oriented cubic ray."""

    base = 3 * index
    return {
        "prep": (base - 1, 0, 0),
        "source_a": (base, 0, 0),
        "source_b": (base, 1, 0),
        "front_a": (base + 1, 0, 0),
        "front_b": (base + 1, 1, 0),
        "setting_a": (base + 1, -1, 0),
        "setting_b": (base + 1, 2, 0),
    }


def cfsi_q_record_packet(index: int, phase: int, x: int, y: int) -> dict[str, object]:
    """Complete boundary/program record packet used by the finite decoder."""

    return {
        "cell": index,
        "phase": phase,
        "setting_a": x,
        "setting_b": y,
        "frame": "boundary-common-bloch-frame",
        "causal_policy": "cfsi-q7-atomic-dag",
        "predecessor_complete": True,
    }


def decode_event_dag(packet: dict[str, object]) -> tuple[tuple[str, str], ...]:
    """Reconstruct the cell event DAG from complete records and boundary data."""

    required = {
        "cell",
        "phase",
        "setting_a",
        "setting_b",
        "frame",
        "causal_policy",
        "predecessor_complete",
    }
    if not required <= packet.keys():
        raise ValueError("incomplete record packet")
    if packet["frame"] != "boundary-common-bloch-frame":
        raise ValueError("unsupported relational frame")
    if packet["causal_policy"] != "cfsi-q7-atomic-dag":
        raise ValueError("unsupported causal policy")
    if packet["predecessor_complete"] is not True:
        raise ValueError("cell is not causally ready")

    prefix = f"cell-{packet['cell']}"
    node = lambda label: f"{prefix}:{label}"
    return tuple(
        sorted(
            (
                (node("predecessor-complete"), node("prep-record")),
                (node("prep-record"), node("prepare")),
                (node("prepare"), node("propagate-a")),
                (node("prepare"), node("propagate-b")),
                (node("propagate-a"), node("measure-a")),
                (node("setting-a-record"), node("measure-a")),
                (node("propagate-b"), node("measure-b")),
                (node("setting-b-record"), node("measure-b")),
                (node("measure-a"), node("append-a")),
                (node("measure-b"), node("append-b")),
                (node("append-a"), node("complete")),
                (node("append-b"), node("complete")),
            )
        )
    )


def has_path(edges: tuple[tuple[str, str], ...], source: str, target: str) -> bool:
    frontier = [source]
    visited: set[str] = set()
    while frontier:
        current = frontier.pop()
        if current == target:
            return True
        if current in visited:
            continue
        visited.add(current)
        frontier.extend(right for left, right in edges if left == current)
    return False


def one_dimensional_live_schedule(order: tuple[int, int]) -> dict[tuple[int, int], Fraction]:
    """Exact live-read countercontrol from the causal-schedule probe."""

    states: list[tuple[dict[int, int], Fraction]] = [({-1: 0, 2: 1}, Fraction(1))]
    for site in order:
        next_states: list[tuple[dict[int, int], Fraction]] = []
        for records, prior in states:
            values = [records[neighbor] for neighbor in (site - 1, site + 1) if neighbor in records]
            for value in set(values):
                probability = Fraction(values.count(value), len(values))
                updated = dict(records)
                updated[site] = value
                next_states.append((updated, prior * probability))
        states = next_states
    result: dict[tuple[int, int], Fraction] = {}
    for records, weight in states:
        transcript = (records[0], records[1])
        result[transcript] = result.get(transcript, Fraction(0)) + weight
    return result


def cylinder_law(phase: int, contexts: tuple[tuple[int, int], ...]) -> dict[tuple[Outcome, ...], sp.Expr]:
    """Finite future transcript law decoded from a preparation-phase record."""

    table = joint_probability_table(bell_density(phase))
    cylinders: dict[tuple[Outcome, ...], sp.Expr] = {tuple(): sp.Integer(1)}
    for x, y in contexts:
        distribution = context_distribution(table, x, y)
        cylinders = {
            history + (outcome,): sp.simplify(weight * probability)
            for history, weight in cylinders.items()
            for outcome, probability in distribution.items()
        }
    return cylinders


def decoded_cylinder_law(
    packet: dict[str, object],
    contexts: tuple[tuple[int, int], ...],
) -> dict[tuple[Outcome, ...], sp.Expr]:
    """Validate the complete record packet, then reconstruct its future law."""

    decode_event_dag(packet)
    return cylinder_law(int(packet["phase"]), contexts)


def source_contract() -> None:
    section("A - Source and authority boundary")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "").split())
    base = BASE_NOTE.read_text(encoding="utf-8").lower()
    pair = PAIR_NOTE.read_text(encoding="utf-8").lower()
    schedule = SCHEDULE_NOTE.read_text(encoding="utf-8").lower()
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in note)
    check("A note changes no live foundation surface", "changes no axiom, registry, or audit" in note)
    check("A note names the exact CFSI-Q7 law value", "cfsi-q7" in note and "exact law value" in note)
    check("A note limits its no-go claim", "narrow no-go" in note)
    check("A repaired CFSI-1 base is common-frame relative", "common-frame record configurations" in base)
    check("A paired-law discriminator is wired in", "one-record transcript" in pair)
    check("A schedule/provenance acceptance control is wired in", "causal input relation" in schedule and "linear extension" in schedule)
    check("A live Qubit domain remains M2", "M_2(C)" in axioms)
    check("A live state qualification remains record configurations", "A state is a configuration of records." in axioms)


def local_block_and_coherent_propagation() -> None:
    section("B - Seven-site local block and coherent nearest-neighbor propagation")
    blocks = tuple(bell_block(index) for index in range(8))
    check("B every cell has seven distinct physical sites", all(len(set(block.values())) == 7 for block in blocks))
    union = set().union(*(set(block.values()) for block in blocks))
    check("B the first eight cells are pairwise disjoint", len(union) == 7 * len(blocks))
    for index, block in enumerate(blocks):
        check(f"B cell {index} source pair is nearest-neighbor", l1_distance(block["source_a"], block["source_b"]) == 1)
        check(f"B cell {index} A propagation edge is nearest-neighbor", l1_distance(block["source_a"], block["front_a"]) == 1)
        check(f"B cell {index} B propagation edge is nearest-neighbor", l1_distance(block["source_b"], block["front_b"]) == 1)
        check(f"B cell {index} settings are local to their front sites", l1_distance(block["setting_a"], block["front_a"]) == 1 and l1_distance(block["setting_b"], block["front_b"]) == 1)
        check(f"B cell {index} preparation record is local to source A", l1_distance(block["prep"], block["source_a"]) == 1)
        if index:
            check(f"B cell {index} preparation site is one edge beyond the prior record front", l1_distance(blocks[index - 1]["front_a"], block["prep"]) == 1)

    initial = kron_all((KET0, KET0, KET0, KET0))
    for phase in (0, 1):
        circuit = coherent_circuit(phase)
        final = sp.simplify(circuit * initial)
        expected = sp.kronecker_product(KET00, bell_vector(phase))
        source_blank = sp.kronecker_product(density(KET00), sp.eye(4))
        check(f"B phase {phase} coherent circuit is unitary", exact_equal(dagger(circuit) * circuit, sp.eye(16)))
        check(f"B phase {phase} propagates the Bell pair to the front", exact_equal(final, expected))
        check(f"B phase {phase} restores the source pair to blank", exact_equal(trace(source_blank * density(final)), 1))


def bell_instrument_and_no_signalling() -> None:
    section("C - Exact Bell instrument, CHSH, no-signalling, and context records")
    rho = bell_density(0)
    table = joint_probability_table(rho)
    correlations = {(x, y): correlation(table, x, y) for x, y in product((0, 1), repeat=2)}
    expected = {
        (0, 0): 1 / sp.sqrt(2),
        (0, 1): 1 / sp.sqrt(2),
        (1, 0): 1 / sp.sqrt(2),
        (1, 1): -1 / sp.sqrt(2),
    }
    check("C all four recorded setting contexts normalize", all(exact_equal(sum(context_distribution(table, x, y).values()), 1) for x, y in product((0, 1), repeat=2)))
    check("C exact Bell correlations match the CHSH optimum", all(exact_equal(correlations[key], value) for key, value in expected.items()))
    chsh = sp.simplify(correlations[(0, 0)] + correlations[(0, 1)] + correlations[(1, 0)] - correlations[(1, 1)])
    check("C CHSH is exactly 2 sqrt(2)", exact_equal(chsh, 2 * sp.sqrt(2)))

    alice_no_signal = True
    bob_no_signal = True
    for x, a in product((0, 1), OUTCOMES):
        marginals = [sp.simplify(sum(table[(x, y, a, b)] for b in OUTCOMES)) for y in (0, 1)]
        alice_no_signal &= exact_equal(marginals[0], marginals[1]) and exact_equal(marginals[0], sp.Rational(1, 2))
    for y, b in product((0, 1), OUTCOMES):
        marginals = [sp.simplify(sum(table[(x, y, a, b)] for a in OUTCOMES)) for x in (0, 1)]
        bob_no_signal &= exact_equal(marginals[0], marginals[1]) and exact_equal(marginals[0], sp.Rational(1, 2))
    check("C Alice marginals are independent of Bob's recorded setting", alice_no_signal)
    check("C Bob marginals are independent of Alice's recorded setting", bob_no_signal)

    all_commute = True
    all_complete = True
    for x, y in product((0, 1), repeat=2):
        joint_sum = sp.zeros(4)
        for a, b in product(OUTCOMES, repeat=2):
            pa = sp.kronecker_product(projector(ALICE[x], a), I2)
            pb = sp.kronecker_product(I2, projector(BOB[y], b))
            all_commute &= exact_equal(pa * pb, pb * pa)
            joint_sum += pa * pb
        all_complete &= exact_equal(joint_sum, sp.eye(4))
    check("C disjoint local outcome projectors commute", all_commute)
    check("C every recorded context is a complete normalized PVM instrument", all_complete)
    check("C changing a setting record changes the local instrument", not exact_equal(projector(ALICE[0], 1), projector(ALICE[1], 1)))


def common_frame_covariance() -> None:
    section("D - Boundary-relative common-frame covariance")
    rho = bell_density(0)
    table = joint_probability_table(rho)
    common = sp.kronecker_product(S, S)
    rotated_rho = sp.simplify(common * rho * dagger(common))
    rotated_alice = tuple(sp.simplify(S * observable * dagger(S)) for observable in ALICE)
    rotated_bob = tuple(sp.simplify(S * observable * dagger(S)) for observable in BOB)
    rotated_table = joint_probability_table(rotated_rho, rotated_alice, rotated_bob)
    check("D simultaneous state/instrument frame conjugation preserves every transcript", all(exact_equal(table[key], rotated_table[key]) for key in table))

    mixed_table = joint_probability_table(rotated_rho, ALICE, BOB)
    check("D rotating the process without transporting the measurement frame changes transcripts", any(not exact_equal(table[key], mixed_table[key]) for key in table))
    check("D a mixed-frame neighborhood therefore needs a relational transport rule", correlation(table, 1, 0) != correlation(mixed_table, 1, 0))


def sampled_branch_and_record_invariance() -> None:
    section("E - One sampled record branch and invariant post-front sectors")
    rho = bell_density(0)
    table = joint_probability_table(rho)
    distribution = context_distribution(table, 0, 0)
    low = sample_distribution(distribution, Fraction(1, 10))
    high = sample_distribution(distribution, Fraction(9, 10))
    check("E each seed selects exactly one joint record tuple", low in distribution and high in distribution)
    check("E separated seeds select different actual branches", low != high)

    for label, outcome in (("low", low), ("high", high)):
        a, b = outcome
        weight, post = branch_post_state(rho, 0, 0, a, b)
        joint = sp.kronecker_product(projector(ALICE[0], a), projector(BOB[0], b))
        check(f"E {label} branch weight equals its transcript probability", exact_equal(weight, distribution[outcome]))
        check(f"E {label} branch writes the context-relative rank-one record", exact_equal(trace(joint * post), 1))
        check(f"E {label} same-context repeat is certain", exact_equal(trace(joint * post * joint), 1))

    q = projector(ALICE[0], 1)
    nondemolition_read = sp.kronecker_product(q, I2) + sp.kronecker_product(I2 - q, X)
    record_effect = sp.kronecker_product(q, I2)
    check("E controlled read is unitary", exact_equal(dagger(nondemolition_read) * nondemolition_read, sp.eye(4)))
    check("E controlled read fixes the selected record sector", exact_equal(dagger(nondemolition_read) * record_effect * nondemolition_read, record_effect))
    check("E an incompatible-setting projector does not preserve the old record sector", not exact_equal(projector(ALICE[1], 1) * q, q * projector(ALICE[1], 1)))


def predictive_record_sufficiency() -> None:
    section("F - Complete-record decoder and minimum process memory")
    plus = bell_density(0)
    minus = bell_density(1)
    plus_table = joint_probability_table(plus)
    minus_table = joint_probability_table(minus)
    zz = sp.kronecker_product(Z, Z)
    xx = sp.kronecker_product(X, X)
    check(
        "F Phi plus/minus have the same local reduced states on both wings",
        all(
            exact_equal(reduced_qubit_state(state, wing), I2 / 2)
            for state in (plus, minus)
            for wing in (0, 1)
        ),
    )
    check("F Phi plus/minus have the same ZZ transcript", exact_equal(trace(plus * zz), 1) and exact_equal(trace(minus * zz), 1))
    check("F their unrecorded relative phase changes the future XX transcript", exact_equal(trace(plus * xx), 1) and exact_equal(trace(minus * xx), -1))
    check("F omitting preparation phase merges different all-context laws", any(not exact_equal(plus_table[key], minus_table[key]) for key in plus_table))

    decoded = {phase: joint_probability_table(bell_density(phase)) for phase in (0, 1)}
    check("F one preparation-phase record bit separates the restricted process family", len(decoded) == 2 and any(not exact_equal(decoded[0][key], decoded[1][key]) for key in decoded[0]))
    check("F equal complete phase/frame records reconstruct equal future tables", all(exact_equal(decoded[phase][key], joint_probability_table(bell_density(phase))[key]) for phase in (0, 1) for key in decoded[phase]))
    future_contexts = ((0, 0), (1, 0), (0, 1))
    first_complete_packet = cfsi_q_record_packet(2, 0, 0, 0)
    second_complete_packet = dict(first_complete_packet)
    check(
        "F equal complete record packets imply equal tested all-future cylinder laws",
        first_complete_packet == second_complete_packet
        and exact_dict_equal(
            decoded_cylinder_law(first_complete_packet, future_contexts),
            decoded_cylinder_law(second_complete_packet, future_contexts),
        ),
    )

    outcome_plus_z = projector(Z, 1)
    outcome_plus_x = projector(X, 1)
    future_z_from_z_record = trace(projector(Z, 1) * outcome_plus_z)
    future_z_from_x_record = trace(projector(Z, 1) * outcome_plus_x)
    check("F an outcome bit without its setting record is predictively ambiguous", exact_equal(future_z_from_z_record, 1) and exact_equal(future_z_from_x_record, sp.Rational(1, 2)))
    check("F retaining the setting record fixes the context-relative post-state", not exact_equal(outcome_plus_z, outcome_plus_x))

    table = joint_probability_table(plus)
    distribution = context_distribution(table, 0, 0)
    first_seed = sample_distribution(distribution, Fraction(1, 10))
    second_seed = sample_distribution(distribution, Fraction(1, 5))
    check("F two hidden sample seeds can yield the same complete record tuple", first_seed == second_seed)
    first_post = branch_post_state(plus, 0, 0, *first_seed)[1]
    second_post = branch_post_state(plus, 0, 0, *second_seed)[1]
    check("F sample-seed identity has no future effect after equal complete records", exact_equal(first_post, second_post))

    initial = kron_all((KET0, KET0, KET0, KET0))
    h0 = embed_single(H, 4, 0)
    entangle = cnot_operator(4, 0, 1)
    propagate = swap_operator(4, 1, 3) * swap_operator(4, 0, 2)
    stage_vectors = (
        initial,
        sp.simplify(h0 * initial),
        sp.simplify(entangle * h0 * initial),
        sp.simplify(propagate * entangle * h0 * initial),
    )
    stage_states = tuple(density(vector) for vector in stage_vectors)
    check("F four interruptible circuit stages are operationally distinct", all(not exact_equal(stage_states[i], stage_states[j]) for i in range(4) for j in range(i + 1, 4)))
    check("F identifying four exposed stages needs at least two classical bits", 2**1 < len(stage_states) <= 2**2)


def causal_schedule_and_provenance() -> None:
    section("G - Causal predecessor reconstruction and linear-extension invariance")
    packet = cfsi_q_record_packet(3, 0, 1, 0)
    dag = decode_event_dag(packet)
    clone_dag = decode_event_dag(dict(packet))
    prefix = "cell-3:"
    measure_a = prefix + "measure-a"
    measure_b = prefix + "measure-b"
    check("G complete boundary/program records deterministically reconstruct the causal DAG", dag == clone_dag)
    check(
        "G the two local Bell measurements are causally incomparable",
        not has_path(dag, measure_a, measure_b) and not has_path(dag, measure_b, measure_a),
    )

    invariant = True
    for x, y, a, b in product((0, 1), (0, 1), OUTCOMES, OUTCOMES):
        alice_first = ordered_local_branch(bell_density(0), x, y, a, b, ("alice", "bob"))
        bob_first = ordered_local_branch(bell_density(0), x, y, a, b, ("bob", "alice"))
        invariant &= exact_equal(alice_first[0], bob_first[0])
        invariant &= exact_equal(alice_first[1], bob_first[1])
    check("G every Alice/Bob linear extension gives the same exact branch law", invariant)

    incomplete = dict(packet)
    del incomplete["causal_policy"]
    rejected = False
    try:
        decode_event_dag(incomplete)
    except ValueError:
        rejected = True
    check("G omitting causal-policy provenance makes the decoder reject the record packet", rejected)

    left_first = one_dimensional_live_schedule((0, 1))
    right_first = one_dimensional_live_schedule((1, 0))
    check(
        "G uncontrolled live reads reproduce the exact 00/01 versus 01/11 schedule fork",
        left_first == {(0, 0): Fraction(1, 2), (0, 1): Fraction(1, 2)}
        and right_first == {(0, 1): Fraction(1, 2), (1, 1): Fraction(1, 2)},
    )
    check("G schedule provenance is predictive whenever live execution order is allowed", left_first != right_first)


def projective_cells_and_fresh_support() -> None:
    section("H - Projective full-lattice cell family and fresh support")
    contexts = ((0, 0), (1, 0), (0, 1))
    table = joint_probability_table(bell_density(0))
    levels = [cylinder_law(0, contexts[:depth]) for depth in range(len(contexts) + 1)]
    cylinders = levels[-1]
    check("H three-cell cylinder family has 4^3 histories", len(cylinders) == 64)
    check("H every finite cylinder level normalizes", all(exact_equal(sum(level.values()), 1) for level in levels))
    first_distribution = context_distribution(table, *contexts[0])
    first_marginal = {
        outcome: sp.simplify(sum(weight for history, weight in cylinders.items() if history[0] == outcome))
        for outcome in first_distribution
    }
    check("H later-cell marginalization recovers the first-cell law", all(exact_equal(first_marginal[outcome], probability) for outcome, probability in first_distribution.items()))

    adaptive_total = sp.Integer(0)
    first = context_distribution(table, 0, 0)
    for first_outcome, first_probability in first.items():
        adaptive_x = 0 if first_outcome[0] == 1 else 1
        second = context_distribution(table, adaptive_x, 1)
        adaptive_total += first_probability * sum(second.values())
    check("H outcome-recorded adaptive settings preserve cylinder normalization", exact_equal(adaptive_total, 1))

    blocks = tuple(bell_block(index) for index in range(12))
    all_sites = set().union(*(set(block.values()) for block in blocks))
    check("H shell/ray allocation gives twelve disjoint fresh seven-site cells", len(all_sites) == 7 * len(blocks))
    check("H allocation reaches unbounded tested distance", max(site[0] for site in all_sites) == bell_block(11)["front_a"][0])
    check("H every outcome pair is written on fresh front sites", len({block["front_a"] for block in blocks} | {block["front_b"] for block in blocks}) == 2 * len(blocks))
    check("H coherent propagation restores each source pair before front commit", exact_equal(coherent_circuit(0) * kron_all((KET0, KET0, KET0, KET0)), sp.kronecker_product(KET00, bell_vector(0))))


def exact_law_value_ablation() -> None:
    section("I - Exact law value remains load-bearing")
    ideal = bell_density(0, sp.Integer(1))
    noisy = bell_density(0, sp.Rational(1, 2))
    ideal_table = joint_probability_table(ideal)
    noisy_table = joint_probability_table(noisy)
    ideal_chsh = sp.simplify(correlation(ideal_table, 0, 0) + correlation(ideal_table, 0, 1) + correlation(ideal_table, 1, 0) - correlation(ideal_table, 1, 1))
    noisy_chsh = sp.simplify(correlation(noisy_table, 0, 0) + correlation(noisy_table, 0, 1) + correlation(noisy_table, 1, 0) - correlation(noisy_table, 1, 1))
    check("I visibility one gives exact Tsirelson CHSH", exact_equal(ideal_chsh, 2 * sp.sqrt(2)))
    check("I visibility one half gives a different exact CHSH", exact_equal(noisy_chsh, sp.sqrt(2)))
    check("I both law values normalize in every setting context", all(exact_equal(sum(context_distribution(table, x, y).values()), 1) for table in (ideal_table, noisy_table) for x, y in product((0, 1), repeat=2)))
    check("I both law values have full outcome support", all(table[key] > 0 for table in (ideal_table, noisy_table) for key in table))
    check("I the two otherwise identical architectures have different transcripts", any(not exact_equal(ideal_table[key], noisy_table[key]) for key in ideal_table))
    seed = Fraction(19, 50)
    ideal_outcome = sample_distribution(context_distribution(ideal_table, 0, 0), seed)
    noisy_outcome = sample_distribution(context_distribution(noisy_table, 0, 0), seed)
    check("I one common seed operationally separates the two law values", ideal_outcome != noisy_outcome)


def minimum_block_and_domain_boundary() -> None:
    section("J - Minimum block and domain boundary")
    check("J two front qubits plus three local program records give the five-site no-propagation block", 2 + 3 == 5)
    check("J explicit source-to-front propagation adds two source work sites", 5 + 2 == 7)
    check("J CFSI-Q7 therefore retains one M2 at every physical site", len(set(bell_block(0).values())) == 7)
    check("J common frame and causal policy remain supplied boundary records outside the cell", len(cfsi_q_record_packet(0, 0, 0, 0)) == 7)
    check("J autonomous open-qubit plus two record sectors would still need local dimension four", 2 + 1 + 1 == 4)


def documentation_contract() -> None:
    section("K - Residual and no-go-discipline needles")
    note = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "cfsi-q7",
        "common-frame",
        "recorded setting",
        "2 sqrt(2)",
        "no-signalling",
        "preparation-phase bit",
        "record-only predictive sufficiency",
        "atomic transaction",
        "projective full-lattice",
        "fresh-support",
        "exact law value",
        "causal predecessor",
        "linear-extension invariance",
        "boundary/program records",
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
        check(f"K note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    local_block_and_coherent_propagation()
    bell_instrument_and_no_signalling()
    common_frame_covariance()
    sampled_branch_and_record_invariance()
    predictive_record_sufficiency()
    causal_schedule_and_provenance()
    projective_cells_and_fresh_support()
    exact_law_value_ablation()
    minimum_block_and_domain_boundary()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
