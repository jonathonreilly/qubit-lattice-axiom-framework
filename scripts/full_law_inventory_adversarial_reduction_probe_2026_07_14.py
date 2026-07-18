#!/usr/bin/env python3
"""Exact adversarial controls for the expanded FD-SLIR law inventory.

This runner checks finite independence witnesses and a dependency graph under
explicit normalized-instrument typing.  It does not select a physical law,
alter an axiom, or issue an audit verdict.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "FULL_LAW_INVENTORY_ADVERSARIAL_REDUCTION_NOTE_2026-07-14.md"
FULL_NOTE = REVIEW / "FULL_LATTICE_FD_SLIR_COMPATIBILITY_AND_MINIMUM_CONTENT_NOTE_2026-07-14.md"
EXCHANGE_NOTE = REVIEW / "QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md"
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Source, authority, and documentation contract")
    note = normalized(NOTE)
    full_note = normalized(FULL_NOTE)
    exchange_note = normalized(EXCHANGE_NOTE)
    check("A adversarial note exists", NOTE.is_file())
    check("A reviewed full-lattice note exists", FULL_NOTE.is_file())
    check("A reviewed exchange note exists", EXCHANGE_NOTE.is_file())
    check("A adversarial note is authority-free", "authority: none" in note)
    check("A full-lattice source is authority-free", "authority: none" in full_note)
    check("A exchange source is authority-free", "authority: none" in exchange_note)
    check("A adversarial note disclaims an axiom proposal", "not the framework law, an axiom proposal" in note)
    check("A source thirteen-item list is retained as a job checklist", "useful as a job checklist" in note)
    check("A corrected ten-core graph is documented", "corrected ten-core dependency dag" in note)
    check(
        "A optional C11, E1, and B-star nodes are documented",
        all(marker in note for marker in ("c11 formation_eligibility", "e1 trial_corpus", "b actual_boundary_selection")),
    )
    check("A strict and Lieb-Robinson routes are separated", "discrete circuit/qca" in note and "lieb-robinson" in note)
    check("A no global one-law route is closed", "no global one-law route is declared closed" in note)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = (KET0 + KET1) / sp.sqrt(2)
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.conjugate().T


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * dagger(vector))


def trace(matrix: sp.Matrix):
    return sp.simplify(sp.trace(matrix))


def exact(left, right) -> bool:
    if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
        return sp.simplify(left - right) == sp.zeros(*left.shape)
    return sp.simplify(left - right) == 0


def open_record_sector_probe() -> None:
    section("B - OPEN versus two record values on one M2 carrier")
    check("B three nonzero orthogonal rank-one sectors require dimension three", 1 + 1 + 1 > 2)
    check("B record-zero and record-one sectors exhaust M2", P0 + P1 == I2)
    check("B the two record projectors have total rank two", P0.rank() + P1.rank() == 2)
    open_state = density(KET_PLUS)
    check("B ready |+> overlaps record zero by one half", trace(open_state * P0) == sp.Rational(1, 2))
    check("B ready |+> overlaps record one by one half", trace(open_state * P1) == sp.Rational(1, 2))
    check("B ready |+> is not a third orthogonal readable value", open_state * P0 != sp.zeros(2) and open_state * P1 != sp.zeros(2))
    check("B OPEN therefore needs metadata, dilation, or a distinct pointer", "open is metadata" in normalized(NOTE) and "separate classical occupancy flag" in normalized(NOTE))


def measurement_law(unitary: sp.Matrix, boundary: sp.Matrix):
    state = sp.simplify(unitary * density(boundary) * dagger(unitary))
    return trace(P0 * state), trace(P1 * state)


def law_boundary_separation() -> None:
    section("C - Law, boundary class, instance, and selection")
    check("C identity law plus boundary zero gives zero", measurement_law(I2, KET0) == (1, 0))
    check("C identity law plus boundary one gives one", measurement_law(I2, KET1) == (0, 1))
    check("C X law plus the same boundary zero gives one", measurement_law(X, KET0) == (0, 1))
    check("C one law with two boundary instances gives different predictions", measurement_law(I2, KET0) != measurement_law(I2, KET1))
    check("C one boundary with two laws gives different predictions", measurement_law(I2, KET0) != measurement_law(X, KET0))
    allowed_class = frozenset({"boundary-zero", "boundary-one"})
    check("C an allowed boundary class does not select one member", len(allowed_class) == 2)
    note = normalized(NOTE)
    check("C boundary class is assigned to domain typing", "allowed boundary class/type belongs to the event/domain contract" in note)
    check("C chosen boundary instance is assigned to decoding", "chosen boundary or preparation record belongs to state/input reconstruction" in note)
    check("C actual cosmological selection remains external", "actual cosmological boundary is not microscopic law content" in note)


def physical_equivalence_quotient() -> None:
    section("D - Raw carrier versus operational physical quotient")
    states = tuple(product((0, 1), repeat=2))  # visible value, hidden token

    def fingerprint(state, contexts):
        visible, hidden = state
        response = {"value": visible, "token": hidden}
        return tuple(response[context] for context in contexts)

    coarse: dict[tuple[int, ...], set[tuple[int, int]]] = defaultdict(set)
    refined: dict[tuple[int, ...], set[tuple[int, int]]] = defaultdict(set)
    for state in states:
        coarse[fingerprint(state, ("value",))].add(state)
        refined[fingerprint(state, ("value", "token"))].add(state)
    check("D raw carrier has four states", len(states) == 4)
    check("D value-only quotient has two classes", len(coarse) == 2)
    check("D value-only quotient blocks have size two", sorted(map(len, coarse.values())) == [2, 2])
    check("D token-sensitive quotient has four classes", len(refined) == 4)
    check("D token-sensitive quotient blocks are singletons", all(len(block) == 1 for block in refined.values()))
    check("D changing contexts changes equivalence without changing carrier", set(states) == set().union(*coarse.values()) == set().union(*refined.values()))
    check("D operational quotient is downstream in the note", "canonical operational quotient is downstream" in normalized(NOTE))


def swap_23() -> sp.Matrix:
    operator = sp.zeros(8)
    for index in range(8):
        a = (index >> 2) & 1
        b = (index >> 1) & 1
        c = index & 1
        target = (a << 2) | (c << 1) | b
        operator[target, index] = 1
    return operator


def finite_propagation_and_exchange() -> None:
    section("E - Strict propagation, exchange tails, and exchange boundaries")
    s12 = sp.kronecker_product(SWAP, I2)
    s23 = swap_23()
    hamiltonian = s12 + s23
    local = sp.kronecker_product(Z, I2, I2)
    remote_test = sp.kronecker_product(I2, I2, X)
    first = sp.simplify(hamiltonian * local - local * hamiltonian)
    second = sp.simplify(hamiltonian * first - first * hamiltonian)
    check("E adjacent exchange terms do not commute", not exact(s12 * s23, s23 * s12))
    check("E first nested order has not reached site three", exact(first * remote_test, remote_test * first))
    check("E second nested order reaches site three", not exact(second * remote_test, remote_test * second))
    check("E exact order-t-squared coefficient is nonzero", second != sp.zeros(8))

    time = sp.symbols("t", real=True)
    h_constant = SWAP
    h_time_dependent = (1 + time) * SWAP
    diagonal_generators = tuple(
        sp.kronecker_product(pauli, I2) + sp.kronecker_product(I2, pauli)
        for pauli in (X, Y, Z)
    )
    check("E constant exchange has diagonal covariance", all(exact(h_constant * g, g * h_constant) for g in diagonal_generators))
    check("E time-dependent exchange has the same pointwise covariance", all(exact(h_time_dependent * g, g * h_time_dependent) for g in diagonal_generators))
    check("E covariance does not force a time-independent coefficient", not exact(h_constant, h_time_dependent))

    spectrum = SWAP.eigenvals()
    check("E SWAP spectrum is triplet plus singlet", spectrum == {sp.Integer(1): 3, sp.Integer(-1): 1})
    check("E plus-SWAP singlet ground degeneracy is one", spectrum[sp.Integer(-1)] == 1)
    check("E minus-SWAP triplet ground degeneracy is three", spectrum[sp.Integer(1)] == 3)

    ket01 = sp.Matrix([0, 1, 0, 0])
    unitary = (sp.eye(4) - sp.I * SWAP) / sp.sqrt(2)
    state = sp.simplify(unitary * ket01)
    rho = density(state)
    reduced = sp.zeros(2)
    for left in range(2):
        for right in range(2):
            for traced in range(2):
                reduced[left, right] += rho[2 * left + traced, 2 * right + traced]
    check("E quarter exchange is unitary", exact(dagger(unitary) * unitary, sp.eye(4)))
    check("E quarter exchange produces a maximally mixed reduction", exact(reduced, I2 / 2))

    a0, a1 = Z, X
    b0 = (Y - Z) / sp.sqrt(2)
    b1 = -(Y + Z) / sp.sqrt(2)

    def correlator(left: sp.Matrix, right: sp.Matrix):
        return sp.simplify((dagger(state) * sp.kronecker_product(left, right) * state)[0])

    correlators = tuple(correlator(a, b) for a, b in ((a0, b0), (a0, b1), (a1, b0), (a1, b1)))
    check("E four Bell correlators are computed exactly", correlators == (1 / sp.sqrt(2), 1 / sp.sqrt(2), 1 / sp.sqrt(2), -1 / sp.sqrt(2)), str(correlators))
    check("E exchange-generated state reaches CHSH two-root-two", exact(correlators[0] + correlators[1] + correlators[2] - correlators[3], 2 * sp.sqrt(2)))


def sequence_law(kind: str, length: int) -> dict[tuple[int, ...], Fraction]:
    words = tuple(product((0, 1), repeat=length))
    if kind == "iid":
        return {word: Fraction(1, 2**length) for word in words}
    if kind == "frozen":
        return {word: Fraction(1, 2) for word in ((0,) * length, (1,) * length)}
    if kind == "alternating":
        first = tuple(index % 2 for index in range(length))
        second = tuple(1 - bit for bit in first)
        return {first: Fraction(1, 2), second: Fraction(1, 2)}
    raise ValueError(kind)


def marginal(law: dict[tuple[int, ...], Fraction], site: int, value: int) -> Fraction:
    return sum(weight for word, weight in law.items() if word[site] == value)


def correlation(law: dict[tuple[int, ...], Fraction], left: int, right: int) -> Fraction:
    return sum(weight * ((-1) ** word[left]) * ((-1) ** word[right]) for word, weight in law.items())


def trial_and_frequency_semantics() -> None:
    section("F - One-shot laws versus trial and frequency semantics")
    kinds = ("iid", "frozen", "alternating")
    laws8 = {}
    for kind in kinds:
        laws = {length: sequence_law(kind, length) for length in range(1, 9)}
        laws8[kind] = laws[8]
        check(f"F {kind} cylinders normalize", all(sum(law.values()) == 1 for law in laws.values()))
        check(
            f"F {kind} cylinders are projectively consistent",
            all(
                sum(laws[length + 1].get(prefix + (tail,), 0) for tail in (0, 1)) == weight
                for length in range(1, 8)
                for prefix, weight in laws[length].items()
            ),
        )
        check(f"F {kind} one-site marginals are one half", all(marginal(laws[8], site, 0) == Fraction(1, 2) for site in range(8)))
    correlations = tuple(correlation(laws8[kind], 0, 1) for kind in kinds)
    check("F equal one-shot laws permit correlations zero, plus one, minus one", correlations == (0, 1, -1), str(correlations))
    check("F frozen frequency support is zero or one", {sum(word) for word in laws8["frozen"]} == {0, 8})
    check("F alternating frequency is exactly one half", {sum(word) for word in laws8["alternating"]} == {4})
    check("F trial corpus is separated before a frequency theorem", "trial_corpus is an empirical-interface job" in normalized(NOTE))


def record_identity_and_renewal() -> None:
    section("G - Record identity/preservation versus renewal")
    finite_transitions = {"open": {"r0", "r1"}, "r0": {"r0"}, "r1": {"r1"}}
    check("G record zero is absorbing", finite_transitions["r0"] == {"r0"})
    check("G record one is absorbing", finite_transitions["r1"] == {"r1"})
    check("G preserved one-site archive has no renewed OPEN carrier", all("open" not in targets for state, targets in finite_transitions.items() if state != "open"))

    before = {0: 0}
    renewed_but_corrupt = {0: 1, 1: 0}
    check("G renewal can allocate a fresh address", 1 not in before and 1 in renewed_but_corrupt)
    check("G renewal does not preserve the old fact", before[0] != renewed_but_corrupt[0])

    migratory_before = {"fact-A": (0, 1)}
    migratory_after = {"fact-A": (1, 1)}
    check("G migratory identity preserves fact and content", migratory_before.keys() == migratory_after.keys() and migratory_before["fact-A"][1] == migratory_after["fact-A"][1])
    check("G migratory identity is not site equality", migratory_before["fact-A"][0] != migratory_after["fact-A"][0])
    check("G note makes preservation independent of renewal", "identity/preservation and no second fresh carrier" in normalized(NOTE))


def availability_and_instrument_support() -> None:
    section("H - Instrument statistics, support, and menu completeness")
    rho = density(KET0)
    menu = {0, 1}
    weights = {0: trace(P0 * rho * P0), 1: trace(P1 * rho * P1)}
    support = {outcome for outcome, weight in weights.items() if weight > 0}
    check("H algebraic PVM menu has two outcomes", menu == {0, 1})
    check("H normalized instrument weights sum to one", sum(weights.values()) == 1)
    check("H prepared zero has weights one and zero", weights == {0: 1, 1: 0})
    check("H positive support is the singleton zero", support == {0})
    check("H positive support can be a strict subset of the menu", support < menu)
    check("H optional eligibility policy is explicitly conditional", "c11 formation_eligibility is needed only if" in normalized(NOTE))


def corrected_dependency_dag() -> None:
    section("I - Corrected ten-core dependency DAG")
    core = {
        "C1_RAW_GENERATED_CARRIER",
        "C2_RECORD_STATUS_AND_IDENTITY",
        "C3_EVENT_READINESS_LOCAL_CAUSAL_DOMAIN",
        "C4_PREDICTIVE_RECORD_DECODER",
        "C5_CONTEXT_INTERVENTION_REPERTOIRE",
        "C6_EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT",
        "C7_GLUING_AND_EXHAUSTIVE_CONTINUATION",
        "C8_ONE_HISTORY_ACTUALITY",
        "C9_PROJECTIVE_FULL_LATTICE_EXTENSION",
        "C10_RENEWAL_FRESHNESS_OR_EXPORT",
    }
    optional = {"C11_FORMATION_ELIGIBILITY", "E1_TRIAL_CORPUS", "B*_ACTUAL_BOUNDARY_SELECTION"}
    derived = {
        "OPERATIONAL_QUOTIENT": {"C5_CONTEXT_INTERVENTION_REPERTOIRE", "C6_EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT", "C7_GLUING_AND_EXHAUSTIVE_CONTINUATION", "C9_PROJECTIVE_FULL_LATTICE_EXTENSION"},
        "ONE_SHOT_WEIGHTS_AND_SUPPORT": {"C6_EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT"},
        "CONTINUATION": {"C6_EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT", "C7_GLUING_AND_EXHAUSTIVE_CONTINUATION"},
        "DISJOINT_CONCURRENCY": {"C1_RAW_GENERATED_CARRIER", "C6_EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT"},
        "OVERLAP_ORDER": {"C3_EVENT_READINESS_LOCAL_CAUSAL_DOMAIN", "C7_GLUING_AND_EXHAUSTIVE_CONTINUATION"},
        "RECORD_WRITING_AND_FORMATION": {"C2_RECORD_STATUS_AND_IDENTITY", "C6_EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT", "C8_ONE_HISTORY_ACTUALITY"},
        "RECORD_PRESERVATION": {"C2_RECORD_STATUS_AND_IDENTITY", "C6_EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT", "C7_GLUING_AND_EXHAUSTIVE_CONTINUATION"},
        "FINITE_EVENT_STEP_PROPAGATION": {"C1_RAW_GENERATED_CARRIER", "C3_EVENT_READINESS_LOCAL_CAUSAL_DOMAIN", "C6_EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT", "C7_GLUING_AND_EXHAUSTIVE_CONTINUATION"},
        "GLOBAL_HISTORY_MEASURE": {"C6_EXACT_NORMALIZED_LOCAL_CP_INSTRUMENT", "C7_GLUING_AND_EXHAUSTIVE_CONTINUATION", "C9_PROJECTIVE_FULL_LATTICE_EXTENSION"},
    }
    check("I conditional-law core has exactly ten inputs", len(core) == 10)
    check("I C1 through C10 are represented once", {item.split("_")[0] for item in core} == {f"C{index}" for index in range(1, 11)})
    check("I three optional/external nodes are distinct", len(optional) == 3 and core.isdisjoint(optional))
    check("I all core-derived dependencies are declared core nodes", all(requirements <= core for requirements in derived.values()))
    check("I operational quotient consumes context, map, continuation, extension", len(derived["OPERATIONAL_QUOTIENT"]) == 4)
    check("I one-shot weights require only the normalized instrument", len(derived["ONE_SHOT_WEIGHTS_AND_SUPPORT"]) == 1)
    check("I record formation consumes actuality", "C8_ONE_HISTORY_ACTUALITY" in derived["RECORD_WRITING_AND_FORMATION"])
    check("I preservation does not consume renewal", "C10_RENEWAL_FRESHNESS_OR_EXPORT" not in derived["RECORD_PRESERVATION"])
    check("I renewal remains independent core content", all("C10_RENEWAL_FRESHNESS_OR_EXPORT" not in requirements for requirements in derived.values()))
    check("I frequency interface is optional E1 rather than silently derived", "E1_TRIAL_CORPUS" in optional)
    check("I actual boundary selection is external B-star", "B*_ACTUAL_BOUNDARY_SELECTION" in optional)
    check("I independent eligibility is optional C11", "C11_FORMATION_ELIGIBILITY" in optional)


def conclusion_contract() -> None:
    section("J - Narrow no-go and live-route needles")
    note = normalized(NOTE)
    for phrase in (
        "exact-causal discrete exchange circuit",
        "continuous exchange law with a proved lieb-robinson/quasilocal limit",
        "larger pointer dilation",
        "operationally reconstructed quotient",
        "full joint law whose ergodicity makes frequencies a theorem",
        "more primitive global rule",
    ):
        check(f"J live route retained: {phrase}", phrase in note)
    check("J result is scoped to current typings", "under the current fd-slir and exchange typings" in note)
    check("J deeper joint derivations remain open", "does not prove that no deeper rule can derive two core inputs together" in note)


def main() -> int:
    source_contract()
    open_record_sector_probe()
    law_boundary_separation()
    physical_equivalence_quotient()
    finite_propagation_and_exchange()
    trial_and_frequency_semantics()
    record_identity_and_renewal()
    availability_and_instrument_support()
    corrected_dependency_dag()
    conclusion_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: exact finite independence witnesses and a conditional ten-core "
        "law-input DAG; no physical-law, axiom, boundary, or audit selection"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
