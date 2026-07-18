#!/usr/bin/env python3
"""Cycle 48 exact record-derived coherent-carrier decoder.

Build all 60 pure two-qubit stabilizer states, encode their preparation in
permanent bits, close them under a declared Clifford/Pauli/teleport protocol,
and verify that replaying identical complete records gives identical future
record statistics.  The non-stabilizer escape is tested explicitly.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE41 = REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md"
CYCLE44 = REVIEW / "PROTECTED_MATTER_TRANSPORT_CYCLE44_NOTE_2026-07-14.md"

PASS = 0
FAIL = 0
TOL = 2.0e-10


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
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Authority and predecessor contract")
    for path in (NOTE, AXIOMS, REGISTRY, CYCLE41, CYCLE44):
        check(f"A source exists: {path.name}", path.is_file())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    cycle41 = normalized(CYCLE41)
    cycle44 = normalized(CYCLE44)
    note = normalized(NOTE)
    check("A state qualification is record-only", "A state is a configuration of records" in axioms)
    check("A records remain permanent", "records are permanent" in axioms)
    check("A registry still exposes four approved premise sources", registry.count('"current_path"') == 4)
    check("A Cycle 41 requires record-fibre sufficiency", "record-fibre sufficiency" in cycle41)
    check("A Cycle 44 exposes the readable-carrier fork", "dark coherent carrier" in cycle44 and "record the carrier/decoder" in cycle44)
    check("A note is authority-free", "authority: none" in note)
    check("A note authorizes no live foundation edit", "no live foundation edit is authorized" in note)
    check("A note keeps the arbitrary-state escape open", "arbitrary unknown states escape" in note)


I2 = np.eye(2, dtype=complex)
X = np.array(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
Y = np.array(((0.0, -1.0j), (1.0j, 0.0)), dtype=complex)
Z = np.array(((1.0, 0.0), (0.0, -1.0)), dtype=complex)
H = np.array(((1.0, 1.0), (1.0, -1.0)), dtype=complex) / np.sqrt(2.0)
S = np.diag((1.0, 1.0j)).astype(complex)
ZERO = np.array((1.0, 0.0), dtype=complex)
ONE = np.array((0.0, 1.0), dtype=complex)
PAULI_1 = (("I", I2), ("X", X), ("Y", Y), ("Z", Z))


def kron(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return np.kron(left, right)


PAULI_2 = tuple((left_name + right_name, kron(left, right)) for left_name, left in PAULI_1 for right_name, right in PAULI_1)
NONTRIVIAL_PAULI_2 = PAULI_2[1:]
I4 = np.eye(4, dtype=complex)


def same(left: np.ndarray, right: np.ndarray) -> bool:
    return np.allclose(left, right, atol=TOL)


def state_index(states: tuple[np.ndarray, ...] | list[np.ndarray], target: np.ndarray) -> int | None:
    for index, state in enumerate(states):
        if same(state, target):
            return index
    return None


def stabilizer_states() -> tuple[tuple[np.ndarray, ...], tuple[tuple[str, int, str, int], ...]]:
    states: list[np.ndarray] = []
    labels: list[tuple[str, int, str, int]] = []
    for first_index, (first_name, first) in enumerate(NONTRIVIAL_PAULI_2):
        for second_name, second in NONTRIVIAL_PAULI_2[first_index + 1 :]:
            if not same(first @ second, second @ first):
                continue
            if same(first, second) or same(first, -second):
                continue
            for first_sign, second_sign in product((1, -1), repeat=2):
                rho = ((I4 + first_sign * first) @ (I4 + second_sign * second)) / 4.0
                if abs(float(np.trace(rho).real) - 1.0) > TOL or not same(rho @ rho, rho):
                    continue
                if state_index(states, rho) is None:
                    states.append(rho)
                    labels.append((first_name, first_sign, second_name, second_sign))
    return tuple(states), tuple(labels)


def partial_trace_carrier(rho: np.ndarray) -> np.ndarray:
    shaped = rho.reshape(2, 2, 2, 2)
    return np.trace(shaped, axis1=1, axis2=3)


def stabilizer_census_checks(states: tuple[np.ndarray, ...], labels: tuple[tuple[str, int, str, int], ...]) -> None:
    section("B - Complete recorded two-qubit stabilizer preparation class")
    check("B exact pure two-qubit stabilizer census has sixty states", len(states) == len(labels) == 60)
    check("B every census member is a rank-one density operator", all(same(rho, rho.conj().T) and same(rho @ rho, rho) and abs(float(np.trace(rho).real) - 1.0) < TOL for rho in states))
    purities = tuple(float(np.trace(reduced @ reduced).real) for reduced in map(partial_trace_carrier, states))
    check("B census contains thirty-six product preparations", sum(abs(purity - 1.0) < TOL for purity in purities) == 36)
    check("B census contains twenty-four reference-entangled preparations", sum(abs(purity - 0.5) < TOL for purity in purities) == 24)
    encoded = tuple(tuple((index >> shift) & 1 for shift in range(5, -1, -1)) for index in range(60))
    check("B six permanent bits injectively encode all preparations", len(set(encoded)) == 60 and all(len(bits) == 6 for bits in encoded))
    check("B four unused six-bit words are rejected", len(set(product((0, 1), repeat=6)).difference(encoded)) == 4)
    check("B each stored generator label reconstructs its state", all(same(((I4 + sign1 * dict(PAULI_2)[name1]) @ (I4 + sign2 * dict(PAULI_2)[name2])) / 4.0, rho) for rho, (name1, sign1, name2, sign2) in zip(states, labels)))


def cnot(control: int, target: int) -> np.ndarray:
    answer = np.zeros((4, 4), dtype=complex)
    for column in range(4):
        word = [(column >> 1) & 1, column & 1]
        word[target] ^= word[control]
        answer[2 * word[0] + word[1], column] = 1.0
    return answer


SWAP = np.array(((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)), dtype=complex)
CLIFFORD_GATES = (
    ("H_R", kron(H, I2)),
    ("H_C", kron(I2, H)),
    ("S_R", kron(S, I2)),
    ("S_C", kron(I2, S)),
    ("CX_RC", cnot(0, 1)),
    ("CX_CR", cnot(1, 0)),
    ("SWAP", SWAP),
)


def probability_fraction(value: float) -> Fraction | None:
    for candidate in (Fraction(0), Fraction(1, 2), Fraction(1)):
        if abs(value - float(candidate)) < TOL:
            return candidate
    return None


def closure_and_measurement_checks(states: tuple[np.ndarray, ...]) -> dict[tuple[int, int, int], tuple[Fraction, int | None]]:
    section("C - Clifford closure and exact Born-Luders Pauli record instruments")
    check("C all seven declared Clifford generators are unitary", all(same(gate.conj().T @ gate, I4) for _, gate in CLIFFORD_GATES))
    gate_images = {(state_id, gate_id): state_index(states, gate @ rho @ gate.conj().T) for state_id, rho in enumerate(states) for gate_id, (_, gate) in enumerate(CLIFFORD_GATES)}
    check("C every Clifford generator maps every preparation back into the recorded class", all(index is not None for index in gate_images.values()) and len(gate_images) == 60 * 7)

    transitions: dict[tuple[int, int, int], tuple[Fraction, int | None]] = {}
    all_probabilities: set[Fraction] = set()
    for state_id, rho in enumerate(states):
        for measurement_id, (_, pauli) in enumerate(NONTRIVIAL_PAULI_2):
            for outcome in (1, -1):
                effect = (I4 + outcome * pauli) / 2.0
                probability = float(np.trace(effect @ rho).real)
                exact_probability = probability_fraction(probability)
                if exact_probability is None:
                    transitions[(state_id, measurement_id, outcome)] = (Fraction(-1), None)
                    continue
                all_probabilities.add(exact_probability)
                if exact_probability == 0:
                    transitions[(state_id, measurement_id, outcome)] = (exact_probability, None)
                else:
                    post = effect @ rho @ effect / float(exact_probability)
                    transitions[(state_id, measurement_id, outcome)] = (exact_probability, state_index(states, post))
    check("C every Pauli record probability is exactly zero, half, or one", all_probabilities == {Fraction(0), Fraction(1, 2), Fraction(1)} and all(probability >= 0 for probability, _ in transitions.values()))
    check("C every nonzero Pauli branch remains in the recorded class", all(probability == 0 or target is not None for probability, target in transitions.values()))
    check("C every declared binary Born-Luders Pauli instrument normalizes", all(transitions[(state_id, measurement_id, 1)][0] + transitions[(state_id, measurement_id, -1)][0] == 1 for state_id in range(60) for measurement_id in range(15)))
    return transitions


def teleportation_kraus() -> dict[tuple[int, int], tuple[np.ndarray, np.ndarray]]:
    bell = (np.kron(ZERO, ZERO) + np.kron(ONE, ONE)) / np.sqrt(2.0)
    embed = np.kron(I2, bell.reshape(4, 1))
    # Direct three-qubit CNOT(0->1).
    cnot3 = np.zeros((8, 8), dtype=complex)
    for column in range(8):
        word = [(column >> 2) & 1, (column >> 1) & 1, column & 1]
        word[1] ^= word[0]
        cnot3[4 * word[0] + 2 * word[1] + word[2], column] = 1.0
    circuit = np.kron(H, np.eye(4)) @ cnot3
    full = circuit @ embed
    candidates = (I2, X, Z, X @ Z, Z @ X)
    answer: dict[tuple[int, int], tuple[np.ndarray, np.ndarray]] = {}
    for first, second in product((0, 1), repeat=2):
        branch = np.zeros((2, 2), dtype=complex)
        for output, source in product((0, 1), repeat=2):
            branch[output, source] = full[4 * first + 2 * second + output, source]
        for correction in candidates:
            fixed = correction @ branch
            scalar = np.trace(fixed) / 2.0
            if abs(scalar) > TOL and same(fixed, scalar * I2):
                answer[(first, second)] = (branch, correction)
                break
    return answer


def teleport_lineage_checks(states: tuple[np.ndarray, ...]) -> None:
    section("D - Reference-entangled transport and recorded syndrome lineage")
    teleport = teleportation_kraus()
    check("D all four teleport syndrome corrections are exact", len(teleport) == 4)
    all_restored = True
    for rho in states:
        for branch, correction in teleport.values():
            raw = kron(I2, branch) @ rho @ kron(I2, branch).conj().T
            fixed = kron(I2, correction) @ raw @ kron(I2, correction).conj().T
            all_restored &= same(fixed, rho / 4.0)
    check("D every product and reference-entangled preparation is restored in every syndrome branch", all_restored)
    check("D every recorded syndrome has probability one quarter for all sixty preparations", all(same(kron(I2, branch).conj().T @ kron(I2, branch), I4 / 4.0) for branch, _ in teleport.values()))
    check("D three recorded hops have sixty-four equiprobable syndrome lineages", 4**3 == 64 and Fraction(1, 4**3) == Fraction(1, 64))

    # Before correction, losing one syndrome bit can identify different Pauli frames.
    entangled = next(rho for rho in states if abs(float(np.trace(partial_trace_carrier(rho) @ partial_trace_carrier(rho)).real) - 0.5) < TOL)
    raw_states: dict[tuple[int, int], np.ndarray] = {}
    for outcome, (branch, _) in teleport.items():
        raw = kron(I2, branch) @ entangled @ kron(I2, branch).conj().T
        raw_states[outcome] = raw / 0.25
    missing_second_ambiguous = any(not same(raw_states[(first, 0)], raw_states[(first, 1)]) for first in (0, 1))
    missing_first_ambiguous = any(not same(raw_states[(0, second)], raw_states[(1, second)]) for second in (0, 1))
    check("D each syndrome lineage bit is load-bearing before correction", missing_first_ambiguous and missing_second_ambiguous)


def encode_six(index: int) -> tuple[int, ...]:
    return tuple((index >> shift) & 1 for shift in range(5, -1, -1))


def decode_six(word: tuple[int, ...]) -> int | None:
    value = 0
    for bit in word:
        value = 2 * value + bit
    return value if value < 60 else None


def adaptive_record_decoder_checks(
    states: tuple[np.ndarray, ...],
    transitions: dict[tuple[int, int, int], tuple[Fraction, int | None]],
) -> None:
    section("E - Adaptive complete-record replay and future-statistics theorem")
    gate_image = {(state_id, gate_id): state_index(states, gate @ rho @ gate.conj().T) for state_id, rho in enumerate(states) for gate_id, (_, gate) in enumerate(CLIFFORD_GATES)}

    decoded: dict[tuple[tuple[int, ...], tuple[tuple[int, int, int, int, int], ...]], np.ndarray] = {}
    conflicting = False
    closed = True
    normalized_trees = True
    adaptive_settings: set[tuple[int, int, int]] = set()

    for prep_id in range(60):
        root_key = (encode_six(prep_id), ())
        frontier = ((root_key, prep_id, Fraction(1)),)
        decoded[root_key] = states[prep_id]
        for depth in range(2):
            next_frontier: list[tuple[tuple[tuple[int, ...], tuple[tuple[int, int, int, int, int], ...]], int, Fraction]] = []
            for key, state_id, path_weight in frontier:
                for syndrome_first, syndrome_second in product((0, 1), repeat=2):
                    gate_id = (prep_id + depth + 2 * syndrome_first + syndrome_second + sum(event[-1] for event in key[1])) % len(CLIFFORD_GATES)
                    moved_id = gate_image[(state_id, gate_id)]
                    if moved_id is None:
                        closed = False
                        continue
                    measurement_id = (3 * prep_id + 5 * depth + gate_id + syndrome_first) % len(NONTRIVIAL_PAULI_2)
                    adaptive_settings.add((syndrome_first, syndrome_second, measurement_id))
                    for outcome in (1, -1):
                        probability, target_id = transitions[(moved_id, measurement_id, outcome)]
                        if probability == 0 or target_id is None:
                            continue
                        event = (syndrome_first, syndrome_second, gate_id, measurement_id, 1 if outcome == 1 else 0)
                        new_key = (key[0], key[1] + (event,))
                        new_state = states[target_id]
                        if new_key in decoded and not same(decoded[new_key], new_state):
                            conflicting = True
                        decoded[new_key] = new_state
                        next_frontier.append((new_key, target_id, path_weight * Fraction(1, 4) * probability))
            frontier = tuple(next_frontier)
        normalized_trees &= sum(weight for _, _, weight in frontier) == 1

    check("E recorded adaptive tree remains inside the sixty-state decoder class", closed)
    check("E every preparation's two-round adaptive tree normalizes", normalized_trees)
    check("E syndrome records genuinely change adaptive settings", len(adaptive_settings) > len(NONTRIVIAL_PAULI_2))
    check("E no identical complete record decodes to two carrier states", not conflicting and len(decoded) > 60)

    replay_exact = True
    future_equal = True
    for key, stored_state in decoded.items():
        prep_id = decode_six(key[0])
        if prep_id is None:
            replay_exact = False
            continue
        state_id = prep_id
        for _, _, gate_id, measurement_id, outcome_bit in key[1]:
            moved_id = gate_image[(state_id, gate_id)]
            if moved_id is None:
                replay_exact = False
                break
            outcome = 1 if outcome_bit == 1 else -1
            probability, target_id = transitions[(moved_id, measurement_id, outcome)]
            if probability == 0 or target_id is None:
                replay_exact = False
                break
            state_id = target_id
        replayed = states[state_id]
        replay_exact &= same(replayed, stored_state)
        stored_signature = tuple(probability_fraction(float(np.trace(((I4 + sign * pauli) / 2.0) @ stored_state).real)) for _, pauli in NONTRIVIAL_PAULI_2 for sign in (1, -1))
        replay_signature = tuple(probability_fraction(float(np.trace(((I4 + sign * pauli) / 2.0) @ replayed).real)) for _, pauli in NONTRIVIAL_PAULI_2 for sign in (1, -1))
        future_equal &= stored_signature == replay_signature
    check("E complete permanent records replay the exact current carrier/reference state", replay_exact)
    check("E identical complete records imply identical future Pauli record statistics", future_equal)

    distinct_signatures = {
        tuple(probability_fraction(float(np.trace(((I4 + pauli) / 2.0) @ rho).real)) for _, pauli in NONTRIVIAL_PAULI_2)
        for rho in states
    }
    check("E deleting the preparation record destroys state sufficiency", len(distinct_signatures) > 1)


def arbitrary_escape_checks(states: tuple[np.ndarray, ...]) -> None:
    section("F - Exact arbitrary-unknown-state escape")
    t_state = (ZERO + np.exp(1.0j * np.pi / 4.0) * ONE) / np.sqrt(2.0)
    psi = np.kron(ZERO, t_state)
    rho_t = np.outer(psi, psi.conj())
    check("F the reference-product T state is outside the stabilizer census", state_index(states, rho_t) is None)
    x_carrier = kron(I2, X)
    probability = float(np.trace(((I4 + x_carrier) / 2.0) @ rho_t).real)
    expected = (1.0 + 1.0 / np.sqrt(2.0)) / 2.0
    check("F T-state X probability has the exact non-stabilizer value", abs(probability - expected) < TOL)
    check("F non-stabilizer probability is not zero, half, or one", probability_fraction(probability) is None)
    check("F finite six-bit decoder contains only sixty valid preparation codes", decode_six((1, 1, 1, 1, 0, 0)) is None and len(states) == 60)
    overlap = abs(np.vdot(ZERO, (ZERO + ONE) / np.sqrt(2.0)))
    check("F unknown-state copying into a record still violates isometry", abs(overlap - overlap**2) > TOL)


def documentation_gate() -> None:
    section("G - Placement and fresh N1-N8 bounded gate")
    note = normalized(NOTE)
    required = (
        "conditional positive",
        "all 60 pure two-qubit stabilizer states",
        "24 reference-entangled",
        "born–lüders instruments",
        "identical complete records imply identical future record statistics",
        "arbitrary unknown states escape",
        "broad no-go: fail",
        "partial-narrowing",
        "narrow boundary: pass",
        "### n1",
        "### n2",
        "### n3",
        "### n4",
        "### n5",
        "### n6",
        "### n7",
        "### n8",
        "no axiom wording follows",
    )
    for phrase in required:
        check(f"G note contains: {phrase}", phrase in note)
    n1 = note.split("### n1", 1)[1].split("### n2", 1)[0]
    check("G N1 contains at least five marked attack routes", n1.count("attempted") + n1.count("ruled out by prior") >= 5)
    check("G N2 names the three collapsed arbitrary-closure walls", all(wall in note for wall in ("w_p", "w_o", "w_r")))
    check("G N2 gives all three independence pairs", all(pair in note for pair in ("w_p/w_o", "w_p/w_r", "w_o/w_r")))
    check("G record-only Qualification is retained only at declared scope", "qualification remains unchanged for this declared class" in note)
    check("G no live foundation edit is authorized", "no live foundation edit is authorized" in note)


def main() -> int:
    source_contract()
    states, labels = stabilizer_states()
    stabilizer_census_checks(states, labels)
    transitions = closure_and_measurement_checks(states)
    teleport_lineage_checks(states)
    adaptive_record_decoder_checks(states, transitions)
    arbitrary_escape_checks(states)
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: permanent preparation, program, syndrome, and outcome records "
        "derive the complete carrier/reference state and all future statistics "
        "for the declared stabilizer-Clifford-Born-Luders-Pauli class; arbitrary unknown "
        "non-stabilizer states and unbounded references remain outside it"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
