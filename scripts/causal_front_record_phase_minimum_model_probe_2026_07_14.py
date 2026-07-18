#!/usr/bin/env python3
"""Exact finite model for a causal-front phase carrying record occupancy."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CAUSAL_FRONT_RECORD_PHASE_MINIMUM_MODEL_NOTE_2026-07-14.md"
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


def exact_equal(left, right) -> bool:
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        return sp.simplify(left - right) == sp.zeros(*left.shape)
    return sp.simplify(left - right) == 0


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = (KET0 + KET1) / sp.sqrt(2)


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def trace(matrix: sp.Matrix):
    return sp.simplify(sp.trace(matrix))


def source_contract() -> None:
    section("A - Source and scope contract")
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(text.lower().replace("*", "").replace("`", "").split())
    check("A note is authority-free", "authority: none" in normalized)
    check("A note is an exact finite conditional model", "exact finite conditional model" in normalized)
    check("A clock reading is not promoted to a lock", "not an oscillator reading" in normalized)
    check("A model disclaims outcome selection by phase", "does not choose the outcome" in normalized)


def three_way_readout_boundary() -> None:
    section("B - One M2 cannot autonomously read open/0/1")
    vectors = (KET_PLUS, KET0, KET1)
    gram = sp.Matrix([[sp.simplify((dagger(left) * right)[0]) for right in vectors] for left in vectors])
    check("B three candidate pure states live in rank-two span", gram.rank() == 2)
    check("B record zero and one are orthogonal", exact_equal((dagger(KET0) * KET1)[0], 0))
    check("B open plus overlaps record zero", exact_equal(abs((dagger(KET_PLUS) * KET0)[0]) ** 2, sp.Rational(1, 2)))
    check("B open plus overlaps record one", exact_equal(abs((dagger(KET_PLUS) * KET1)[0]) ** 2, sp.Rational(1, 2)))

    # Three nonzero pairwise-orthogonal support projectors require rank at least
    # three.  Enumerate the possible positive integer ranks in dimension two.
    rank_triples = tuple(
        ranks
        for ranks in product((1, 2), repeat=3)
        if sum(ranks) <= 2
    )
    check("B no three nonzero orthogonal supports fit dimension two", not rank_triples)
    check("B binary locked readout fits the qubit", exact_equal(P0 + P1, I2) and exact_equal(P0 * P1, sp.zeros(2)))


def sampled_joint_commit() -> None:
    section("C - Joint sample, write, and phase transition")
    rho = density(KET_PLUS)
    branches = tuple(sp.simplify(projector * rho * projector) for projector in (P0, P1))
    weights = tuple(trace(branch) for branch in branches)
    check("C sharp write instrument normalizes", exact_equal(sum(weights), 1))
    check("C open plus gives equal branch weights", weights == (sp.Rational(1, 2), sp.Rational(1, 2)))

    def sample(seed: Fraction) -> int:
        return 0 if seed < Fraction(1, 2) else 1

    outcomes = (sample(Fraction(1, 4)), sample(Fraction(3, 4)))
    check("C explicit seeds select exactly one branch each", outcomes == (0, 1))
    for outcome in outcomes:
        post = sp.simplify(branches[outcome] / weights[outcome])
        expected = (P0, P1)[outcome]
        check(f"C sampled outcome {outcome} writes its pointer state", exact_equal(post, expected))

    def commit(state: sp.Matrix, seed: Fraction):
        unnormalized = tuple(sp.simplify(projector * state * projector) for projector in (P0, P1))
        probabilities = tuple(trace(branch) for branch in unnormalized)
        threshold = Fraction(int(probabilities[0].p), int(probabilities[0].q))
        outcome = 0 if seed < threshold else 1
        return {
            "phase": "locked",
            "record": outcome,
            "weight": probabilities[outcome],
            "state": sp.simplify(unnormalized[outcome] / probabilities[outcome]),
        }, probabilities

    general = sp.Matrix([[sp.Rational(2, 5), sp.Rational(1, 5)], [sp.Rational(1, 5), sp.Rational(3, 5)]])
    check("C general test state is positive and normalized", general.is_positive_semidefinite and trace(general) == 1)
    committed_zero, general_weights = commit(general, Fraction(1, 5))
    committed_one, _ = commit(general, Fraction(4, 5))
    check("C general branch weights are trace weights", general_weights == (sp.Rational(2, 5), sp.Rational(3, 5)))
    check("C joint commit returns locked phase and record zero", committed_zero["phase"] == "locked" and committed_zero["record"] == 0 and exact_equal(committed_zero["state"], P0))
    check("C joint commit returns locked phase and record one", committed_one["phase"] == "locked" and committed_one["record"] == 1 and exact_equal(committed_one["state"], P1))
    check("C classical seed is an explicit actuality input", committed_zero["record"] != committed_one["record"])


def reversible_clock_control() -> None:
    section("D - A reversible clock correlation is not a commit")
    # Source controls a blank clock qubit.  This correlates outcome and clock,
    # but the same CNOT reverses it exactly.
    cnot = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    blank_clock = KET0
    initial = sp.kronecker_product(KET_PLUS, blank_clock)
    correlated = sp.simplify(cnot * initial)
    restored = sp.simplify(cnot * correlated)
    check("D controlled clock write is unitary", exact_equal(dagger(cnot) * cnot, sp.eye(4)))
    check("D the complete clock correlation reverses exactly", exact_equal(restored, initial))
    check("D correlated state has two nonzero outcome-clock amplitudes", correlated[0] != 0 and correlated[3] != 0 and correlated[1] == correlated[2] == 0)

    outcome_blind_tick = sp.kronecker_product(I2, X)
    ticked = sp.simplify(outcome_blind_tick * initial)
    source_reduced = sp.zeros(2)
    ticked_rho = density(ticked)
    for a, b, clock in product(range(2), range(2), range(2)):
        source_reduced[a, b] += ticked_rho[2 * a + clock, 2 * b + clock]
    check("D outcome-blind tick leaves source unsettled", exact_equal(source_reduced, density(KET_PLUS)))

    # If the outgoing front itself carries the outcome, it is a second witness.
    # Two controlled copies turn |+00> into GHZ, still a coherent pure state.
    copy_record_and_front = sp.zeros(8)
    for index in range(8):
        source = (index >> 2) & 1
        record = (index >> 1) & 1
        front = index & 1
        target = (source << 2) | ((record ^ source) << 1) | (front ^ source)
        copy_record_and_front[target, index] = 1
    initial_three = sp.kronecker_product(KET_PLUS, KET0, KET0)
    ghz = sp.simplify(copy_record_and_front * initial_three)
    expected_ghz = sp.Matrix([1, 0, 0, 0, 0, 0, 0, 1]) / sp.sqrt(2)
    check("D outcome-conditioned front creates an exact second witness", exact_equal(ghz, expected_ghz))
    check("D second-witness write remains globally unitary", exact_equal(dagger(copy_record_and_front) * copy_record_and_front, sp.eye(8)))
    check("D the second-witness write reverses exactly", exact_equal(copy_record_and_front * ghz, initial_three))
    check("D GHZ witness state is pure, not one selected outcome", exact_equal(trace(density(ghz) * density(ghz)), 1) and ghz[0] != 0 and ghz[7] != 0)


def allowed_operation_phase() -> None:
    section("E - The causal phase changes the allowed operation algebra")
    check("E open phase may allow a flip", exact_equal(X * P0 * X, P1))
    check("E the same flip would change a locked value", not exact_equal(X * P0 * X, P0))
    diagonal_family = (
        I2,
        Z,
        sp.diag(sp.I, 1),
        sp.diag(1, sp.I),
    )
    check("E diagonal locked-phase operations commute with both records", all(exact_equal(unitary * p, p * unitary) for unitary in diagonal_family for p in (P0, P1)))
    check("E every checked locked-phase operation preserves record zero", all(exact_equal(unitary * P0 * dagger(unitary), P0) for unitary in diagonal_family))
    check("E every checked locked-phase operation preserves record one", all(exact_equal(unitary * P1 * dagger(unitary), P1) for unitary in diagonal_family))

    # One nonunitary diagonal-Kraus channel and its square exercise the full
    # channel condition rather than only selected unitaries.
    k0 = sp.diag(1, 1 / sp.sqrt(2))
    k1 = sp.diag(0, 1 / sp.sqrt(2))
    kraus = (k0, k1)
    check("E diagonal Kraus family is trace preserving", exact_equal(sum((dagger(k) * k for k in kraus), sp.zeros(2)), I2))

    def dual(effect):
        return sp.simplify(sum((dagger(k) * effect * k for k in kraus), sp.zeros(2)))

    check("E full locked channel fixes both record projectors", exact_equal(dual(P0), P0) and exact_equal(dual(P1), P1))
    check("E every locked-channel Kraus block commutes with both projectors", all(exact_equal(k * p, p * k) for k in kraus for p in (P0, P1)))

    composed = tuple(left * right for left in kraus for right in kraus)
    check("E locked operation class is closed under checked composition", exact_equal(sum((dagger(k) * k for k in composed), sp.zeros(2)), I2) and all(exact_equal(k * p, p * k) for k in composed for p in (P0, P1)))

    # A nondemolition read interaction U=sum_s P_s tensor U_s.
    read = sp.kronecker_product(P0, I2) + sp.kronecker_product(P1, X)
    q0 = sp.kronecker_product(P0, I2)
    q1 = sp.kronecker_product(P1, I2)
    check("E controlled read interaction is unitary", exact_equal(dagger(read) * read, sp.eye(4)))
    check("E controlled read preserves the record algebra", exact_equal(read * q0, q0 * read) and exact_equal(read * q1, q1 * read))


def descendants(graph, start):
    seen = {start}
    queue = deque((start,))
    while queue:
        state = queue.popleft()
        for target in graph[state]:
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return seen


def continuation_phase_graph() -> None:
    section("F - Stipulated monotone causal-front law has nonreconnecting sectors")
    graph = {
        "open": {"R0", "R1"},
        "R0": {"R0+future"},
        "R1": {"R1+future"},
        "R0+future": {"R0+future"},
        "R1+future": {"R1+future"},
    }
    zero_future = descendants(graph, "R0")
    one_future = descendants(graph, "R1")
    check("F open phase supports both record outcomes", graph["open"] == {"R0", "R1"})
    check("F locked phases never return to open", "open" not in zero_future | one_future)
    check("F conflicting record sectors do not reconnect", not (zero_future & one_future))
    check("F each locked sector has indefinite continuation", "R0+future" in graph["R0+future"] and "R1+future" in graph["R1+future"])
    flipped_graph = {**graph, "R0": {"open", "R0+future"}}
    check("F allowing a phase flip destroys monotonicity", "open" in descendants(flipped_graph, "R0"))


def order_metric_boundary() -> None:
    section("G - Causal phase gives order, not metric duration")
    events = tuple(range(6))
    clocks = {
        "count": tuple(events),
        "linear2": tuple(2 * event for event in events),
        "quadratic": tuple(event**2 for event in events),
    }
    check("G all clocks preserve the same event order", all(all(values[i] < values[i + 1] for i in range(5)) for values in clocks.values()))
    check("G the same order has different elapsed durations", len({values[-1] - values[0] for values in clocks.values()}) == 3)


def conclusion_contract() -> None:
    section("H - Constitutional boundary needles")
    text = NOTE.read_text(encoding="utf-8").lower()
    phrases = (
        "occupancy bit",
        "causal-front",
        "joint commit",
        "clock can be the lock",
        "born",
        "metric time",
        "does not require a third onsite level",
        "exact law reference",
        "phase monotonicity is stipulated",
        "recoverable from the present record/front configuration",
        "state is history-dependent",
        "phi*(p_s)=p_s",
    )
    for phrase in phrases:
        check(f"H note contains boundary: {phrase}", phrase in text)


def main() -> None:
    source_contract()
    three_way_readout_boundary()
    sampled_joint_commit()
    reversible_clock_control()
    allowed_operation_phase()
    continuation_phase_graph()
    order_metric_boundary()
    conclusion_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
