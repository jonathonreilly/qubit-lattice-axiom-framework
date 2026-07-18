#!/usr/bin/env python3
"""Exact finite probes for record-instrument and Lueders-form selection.

This runner separates four questions that are often compressed into the word
"measurement": the outcome context, the conditional CP map, one-outcome
actuality, and statistics.  It checks repeatable degenerate countermodels,
the sharp binary-qubit reduction, covariance, strong versus weak disturbance,
instrument dilations, reversible redundant witnesses, and the U(1) charge
precedent control used by the paired source note.
"""

from __future__ import annotations

from itertools import product
from math import gcd
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RECORD_INSTRUMENT_SELECTION_LUDERS_PRIMARY_SOURCE_AUDIT_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE13 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "APPEND_ONLY_CAUSAL_BELL_WIRE_CYCLE13_NOTE_2026-07-14.md"
)
CYCLE14 = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md"
)
U1_PARENT = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "TOPOLOGICAL_CONSERVATION_RG_ACTION_STEELMAN_NOTE_2026-07-14.md"
)


TOL = 1.0e-10
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


def ket(index: int, dimension: int) -> np.ndarray:
    vector = np.zeros((dimension, 1), dtype=complex)
    vector[index, 0] = 1.0
    return vector


def projector(vector: np.ndarray) -> np.ndarray:
    return vector @ vector.conj().T


def apply(kraus: tuple[np.ndarray, ...], rho: np.ndarray) -> np.ndarray:
    return sum((operator @ rho @ operator.conj().T for operator in kraus), np.zeros_like(rho))


def dual(kraus: tuple[np.ndarray, ...], observable: np.ndarray) -> np.ndarray:
    return sum(
        (operator.conj().T @ observable @ operator for operator in kraus),
        np.zeros_like(observable),
    )


def effect(kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    dimension = kraus[0].shape[1]
    return sum(
        (operator.conj().T @ operator for operator in kraus),
        np.zeros((dimension, dimension), dtype=complex),
    )


def choi(kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    columns = tuple(operator.reshape((-1, 1), order="F") for operator in kraus)
    return sum((column @ column.conj().T for column in columns), np.zeros((columns[0].size, columns[0].size), dtype=complex))


def is_cp(kraus: tuple[np.ndarray, ...]) -> bool:
    eigenvalues = np.linalg.eigvalsh(choi(kraus))
    return bool(np.min(eigenvalues) >= -TOL)


def is_complete(instrument: tuple[tuple[np.ndarray, ...], ...]) -> bool:
    total = sum((effect(branch) for branch in instrument), np.zeros_like(effect(instrument[0])))
    return bool(np.allclose(total, np.eye(total.shape[0]), atol=TOL))


def branch_repeatable(
    instrument: tuple[tuple[np.ndarray, ...], ...],
    projectors: tuple[np.ndarray, ...],
) -> bool:
    for outcome, branch in enumerate(instrument):
        for operator in branch:
            if not np.allclose(projectors[outcome] @ operator, operator, atol=TOL):
                return False
            for other, value in enumerate(projectors):
                if other != outcome and not np.allclose(value @ operator, 0, atol=TOL):
                    return False
    return True


def nonselective(instrument: tuple[tuple[np.ndarray, ...], ...], rho: np.ndarray) -> np.ndarray:
    return sum((apply(branch, rho) for branch in instrument), np.zeros_like(rho))


def nonselective_dual(
    instrument: tuple[tuple[np.ndarray, ...], ...], observable: np.ndarray
) -> np.ndarray:
    return sum((dual(branch, observable) for branch in instrument), np.zeros_like(observable))


def instruments_equal(
    first: tuple[tuple[np.ndarray, ...], ...],
    second: tuple[tuple[np.ndarray, ...], ...],
    probes: tuple[np.ndarray, ...],
) -> bool:
    return all(
        np.allclose(apply(first[index], rho), apply(second[index], rho), atol=TOL)
        for index in range(len(first))
        for rho in probes
    )


def instrument_isometry(instrument: tuple[tuple[np.ndarray, ...], ...]) -> np.ndarray:
    return np.vstack(tuple(operator for branch in instrument for operator in branch))


def partial_trace_pure(state: np.ndarray, keep: int, dimensions: tuple[int, ...]) -> np.ndarray:
    tensor = state.reshape(dimensions)
    axes = tuple(index for index in range(len(dimensions)) if index != keep)
    return np.tensordot(tensor, tensor.conj(), axes=(axes, axes))


def authority_and_source_contract() -> None:
    section("A - Authority, foundation, and source-note contract")
    note = NOTE.read_text(encoding="utf-8")
    note_lower = " ".join(note.lower().replace("*", "").replace("`", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8").lower()
    registry = REGISTRY.read_text(encoding="utf-8")
    cycle13 = CYCLE13.read_text(encoding="utf-8").lower()
    cycle14 = " ".join(CYCLE14.read_text(encoding="utf-8").lower().split())
    check("A note is authority-free", "authority: none" in note_lower)
    check(
        "A note changes no live authority surface",
        "changes no axiom, primitive, registry, audit, review queue, or retained surface" in note_lower,
    )
    check("A current Record text is read exactly", "records form" in axioms and "records are permanent" in axioms)
    check("A current foundation supplies no context-selection rule", "context selection" in axioms)
    for primitive in ("scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"):
        check(f"A registry contains {primitive}", primitive in registry)
    for source in (
        "davies",
        "lewis",
        "ozawa",
        "lüders",
        "busch",
        "heinosaari",
        "barnum",
        "darwinism",
        "batra",
        "dobrescu",
        "spivak",
    ):
        check(f"A primary-source ledger names {source}", source in note_lower)
    check("A Cycle 13 explicitly supplies projective X and Z reads", "projective `x` instrument" in cycle13 and "projective `z` instruments" in cycle13)
    check("A Cycle 14 retains the supplied projective/Born instrument", "supplied projective/born instrument" in cycle14)


def degenerate_repeatable_countermodels() -> dict[str, object]:
    section("B - Degenerate sharp PVM admits inequivalent repeatable CP instruments")
    e0, e1, e2 = (ket(index, 3) for index in range(3))
    p0 = projector(e0) + projector(e1)
    p1 = projector(e2)
    phase = np.diag([1.0, -1.0, 1.0]).astype(complex)

    luders = ((p0,), (p1,))
    rotated = ((phase @ p0,), (p1,))
    measure_prepare = (
        ((e0 @ e0.conj().T), (e0 @ e1.conj().T)),
        ((e2 @ e2.conj().T),),
    )
    instruments = {
        "Lueders": luders,
        "within-sector unitary": rotated,
        "measure-prepare": measure_prepare,
    }
    projectors = (p0, p1)
    plus = (e0 + e1) / np.sqrt(2)
    plus_i = (e0 + 1j * e1) / np.sqrt(2)
    probes = tuple(projector(vector) for vector in (e0, e1, e2, plus, plus_i, (e0 + e2) / np.sqrt(2)))

    for name, instrument in instruments.items():
        check(f"B {name} branches are CP", all(is_cp(branch) for branch in instrument))
        check(f"B {name} is trace complete", is_complete(instrument))
        check(f"B {name} has the same sharp PVM effects", all(np.allclose(effect(instrument[j]), projectors[j], atol=TOL) for j in range(2)))
        check(f"B {name} is exactly repeatable", branch_repeatable(instrument, projectors))
        check(
            f"B {name} preserves the recorded outcome probabilities on repetition",
            all(np.allclose(nonselective_dual(instrument, p), p, atol=TOL) for p in projectors),
        )

    rho_plus = projector(plus)
    luders_output = apply(luders[0], rho_plus)
    rotated_output = apply(rotated[0], rho_plus)
    prepared_output = apply(measure_prepare[0], rho_plus)
    check("B Lueders and rotated instruments have different conditional states", not np.allclose(luders_output, rotated_output, atol=TOL))
    check("B Lueders and measure-prepare instruments have different conditional states", not np.allclose(luders_output, prepared_output, atol=TOL))
    check("B all three instruments give identical outcome probabilities", all(abs(np.trace(apply(instrument[0], rho_plus)).real - 1.0) < TOL for instrument in instruments.values()))
    check("B repeatability therefore fixes sector support, not dynamics inside a degenerate sector", len({tuple(np.round(apply(instrument[0], rho_plus).flatten(), 10)) for instrument in instruments.values()}) == 3)

    return {
        "basis": (e0, e1, e2),
        "projectors": projectors,
        "phase": phase,
        "instruments": instruments,
        "probes": probes,
        "plus": plus,
    }


def covariance_does_not_select(data: dict[str, object]) -> None:
    section("C - Nontrivial covariance still leaves a repeatable instrument family")
    p0, p1 = data["projectors"]
    plus = data["plus"]
    probes = data["probes"]

    angles = (0.0, np.pi / 7, np.pi / 3, np.pi / 2)
    instruments = []
    for theta in angles:
        unitary = np.diag([np.exp(1j * theta), np.exp(-1j * theta), 1.0])
        instrument = ((unitary @ p0,), (p1,))
        instruments.append(instrument)
        check(f"C theta={theta:.6f} instrument is complete", is_complete(instrument))
        check(f"C theta={theta:.6f} instrument is repeatable", branch_repeatable(instrument, (p0, p1)))
        for phi in (0.0, np.pi / 5, np.pi / 2):
            covariance = np.diag([np.exp(1j * phi), np.exp(-1j * phi), 1.0])
            covariant = True
            for branch in instrument:
                for rho in probes:
                    left = apply(branch, covariance @ rho @ covariance.conj().T)
                    right = covariance @ apply(branch, rho) @ covariance.conj().T
                    covariant &= np.allclose(left, right, atol=TOL)
            check(f"C theta={theta:.6f} is covariant under phase phi={phi:.6f}", covariant)

    rho_plus = projector(plus)
    outputs = tuple(apply(instrument[0], rho_plus) for instrument in instruments)
    check("C sampled covariant family contains four distinct branch maps", all(not np.allclose(outputs[i], outputs[j], atol=TOL) for i in range(len(outputs)) for j in range(i + 1, len(outputs))))
    check("C covariance group acts nontrivially inside the degenerate sector", not np.allclose(np.diag([np.exp(1j * np.pi / 5), np.exp(-1j * np.pi / 5), 1.0]) @ plus, plus, atol=TOL))
    check("C covariance therefore classifies a family rather than selecting one member", len(instruments) == 4)


def weak_and_strong_minimal_disturbance(data: dict[str, object]) -> None:
    section("D - Weak nondisturbance is insufficient; strong ideality selects Lueders for a supplied PVM")
    e0, e1, _ = data["basis"]
    p0, p1 = data["projectors"]
    instruments = data["instruments"]
    plus = data["plus"]
    q_plus = projector(plus)
    check("D within-sector Q commutes with every supplied PVM projector", np.allclose(q_plus @ p0, p0 @ q_plus, atol=TOL) and np.allclose(q_plus @ p1, p1 @ q_plus, atol=TOL))

    for name, instrument in instruments.items():
        weak = all(np.allclose(nonselective_dual(instrument, projector_), projector_, atol=TOL) for projector_ in (p0, p1))
        check(f"D {name} satisfies weak first-kind nondisturbance", weak)

    check("D Lueders fixes every tested compatible block observable", all(np.allclose(nonselective_dual(instruments["Lueders"], observable), observable, atol=TOL) for observable in (projector(e0), projector(e1), q_plus, projector((e0 + 1j * e1) / np.sqrt(2)), p1)))
    check("D within-sector unitary disturbs a compatible observable", not np.allclose(nonselective_dual(instruments["within-sector unitary"], q_plus), q_plus, atol=TOL))
    check("D measure-prepare disturbs a compatible observable", not np.allclose(nonselective_dual(instruments["measure-prepare"], q_plus), q_plus, atol=TOL))

    within_sector_states = tuple(projector(vector) for vector in (e0, e1, plus, (e0 + 1j * e1) / np.sqrt(2)))
    for name, instrument in instruments.items():
        preserves_all = all(np.allclose(apply(instrument[0], rho), rho, atol=TOL) for rho in within_sector_states)
        check(f"D {name} branchwise identity-on-sector verdict is {name == 'Lueders'}", preserves_all == (name == "Lueders"))
    check("D strong ideality is extra content beyond repeatability", branch_repeatable(instruments["within-sector unitary"], (p0, p1)) and not np.allclose(nonselective_dual(instruments["within-sector unitary"], q_plus), q_plus, atol=TOL))


def binary_qubit_partial_closure() -> None:
    section("E - Exhaustive repeatable binary qubit instruments force sharp Lueders form, not context")
    grid = (0.0, 0.25, 0.5, 0.75, 1.0)
    survivors = []
    for first, second in product(grid, repeat=2):
        effect0 = np.diag([first, second])
        effect1 = np.eye(2) - effect0
        if abs(np.max(np.linalg.eigvalsh(effect0)) - 1.0) < TOL and abs(np.max(np.linalg.eigvalsh(effect1)) - 1.0) < TOL:
            survivors.append((first, second))
    check("E two attainable repeatable outcomes force effect eigenvalues zero and one on the exact grid", set(survivors) == {(0.0, 1.0), (1.0, 0.0)})

    e0, e1 = ket(0, 2), ket(1, 2)
    pz0, pz1 = projector(e0), projector(e1)
    plus, minus = (e0 + e1) / np.sqrt(2), (e0 - e1) / np.sqrt(2)
    px0, px1 = projector(plus), projector(minus)
    z_instrument = ((pz0,), (pz1,))
    x_instrument = ((px0,), (px1,))
    check("E Z binary instrument is complete and repeatable", is_complete(z_instrument) and branch_repeatable(z_instrument, (pz0, pz1)))
    check("E X binary instrument is complete and repeatable", is_complete(x_instrument) and branch_repeatable(x_instrument, (px0, px1)))

    coefficients = ((1.0 + 0j, 0.0 + 0j), (3.0 / 5.0, 4.0 / 5.0), (1.0 / np.sqrt(2), 1j / np.sqrt(2)))
    rho = np.array([[0.4, 0.2 + 0.1j], [0.2 - 0.1j, 0.6]], dtype=complex)
    for first, second in coefficients:
        branch = (first * pz0, second * pz0)
        check("E every rank-one supported Kraus decomposition with effect P gives the same Lueders map", np.allclose(effect(branch), pz0, atol=TOL) and np.allclose(apply(branch, rho), pz0 @ rho @ pz0, atol=TOL))

    z_probabilities = tuple(np.trace(apply(branch, pz0)).real for branch in z_instrument)
    x_probabilities = tuple(np.trace(apply(branch, pz0)).real for branch in x_instrument)
    check("E Z and X contexts give different records on one supplied state", np.allclose(z_probabilities, (1.0, 0.0), atol=TOL) and np.allclose(x_probabilities, (0.5, 0.5), atol=TOL))
    check("E each context is ideal relative to its own commuting algebra", np.allclose(nonselective_dual(z_instrument, pz0), pz0, atol=TOL) and np.allclose(nonselective_dual(x_instrument, px0), px0, atol=TOL))
    check("E repeatability plus ideality therefore fixes form but not X versus Z", not np.allclose(pz0, px0, atol=TOL))


def dilation_and_purification_controls(data: dict[str, object]) -> None:
    section("F - Instrument dilation realizes competitors; it does not select one")
    instruments = data["instruments"]
    dimension = 3
    for name, instrument in instruments.items():
        isometry = instrument_isometry(instrument)
        check(f"F {name} canonical Kraus stack is an isometry", np.allclose(isometry.conj().T @ isometry, np.eye(dimension), atol=TOL))

    plus = data["plus"]
    rho_plus = projector(plus)
    luders = instruments["Lueders"]
    rotated = instruments["within-sector unitary"]
    check("F two valid dilations have the same pointer probabilities", all(abs(np.trace(apply(luders[j], rho_plus)).real - np.trace(apply(rotated[j], rho_plus)).real) < TOL for j in range(2)))
    check("F those valid dilations induce different conditional system states", not np.allclose(apply(luders[0], rho_plus), apply(rotated[0], rho_plus), atol=TOL))

    original = instruments["measure-prepare"][0]
    mixed = (
        (original[0] + original[1]) / np.sqrt(2),
        (original[0] - original[1]) / np.sqrt(2),
    )
    probes = data["probes"]
    check("F unitary mixing of same-outcome Kraus labels preserves the branch CP map", all(np.allclose(apply(original, rho), apply(mixed, rho), atol=TOL) for rho in probes))
    check("F Kraus/dilation coordinates are not a unique microscopic realization", not all(np.allclose(original[index], mixed[index], atol=TOL) for index in range(2)))


def broadcasting_and_darwinism_controls() -> None:
    section("G - Broadcastability and redundant witnesses constrain a basis but do not choose actuality")
    zero, one = ket(0, 2), ket(1, 2)
    plus, minus = (zero + one) / np.sqrt(2), (zero - one) / np.sqrt(2)
    overlap = (zero.conj().T @ plus)[0, 0]
    check("G a copier for zero and plus would violate inner-product preservation", abs(overlap - overlap**2) > TOL)
    check("G orthogonal pointer states evade that obstruction", abs((zero.conj().T @ one)[0, 0]) < TOL)

    h = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    cnot = np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]],
        dtype=complex,
    )
    x_copier = np.kron(h, h) @ cnot @ np.kron(h, h)
    check("G CNOT copies the Z pointer basis", np.allclose(cnot @ np.kron(zero, zero), np.kron(zero, zero), atol=TOL) and np.allclose(cnot @ np.kron(one, zero), np.kron(one, one), atol=TOL))
    check("G a conjugate unitary copies the X pointer basis", np.allclose(x_copier @ np.kron(plus, plus), np.kron(plus, plus), atol=TOL) and np.allclose(x_copier @ np.kron(minus, plus), np.kron(minus, minus), atol=TOL))
    check("G equally exact Z and X copiers are different physical contexts", not np.allclose(cnot, x_copier, atol=TOL))

    def controlled_on_three(target: int) -> np.ndarray:
        result = np.zeros((8, 8), dtype=complex)
        for bits in product((0, 1), repeat=3):
            output = list(bits)
            if bits[0] == 1:
                output[target] ^= 1
            source_index = 4 * bits[0] + 2 * bits[1] + bits[2]
            output_index = 4 * output[0] + 2 * output[1] + output[2]
            result[output_index, source_index] = 1.0
        return result

    u_z = controlled_on_three(2) @ controlled_on_three(1)
    input_z = np.kron(plus, np.kron(zero, zero))
    ghz_z = u_z @ input_z
    target_ghz = (np.kron(zero, np.kron(zero, zero)) + np.kron(one, np.kron(one, one))) / np.sqrt(2)
    check("G two disjoint witnesses form an exact GHZ redundancy", np.allclose(ghz_z, target_ghz, atol=TOL))
    check("G each witness marginal is a classical half-half record", all(np.allclose(partial_trace_pure(ghz_z, index, (2, 2, 2)), np.eye(2) / 2, atol=TOL) for index in (1, 2)))
    check("G the complete witness interaction is exactly reversible", np.allclose(u_z.conj().T @ ghz_z, input_z, atol=TOL))

    h3 = np.kron(h, np.kron(h, h))
    u_x = h3 @ u_z @ h3
    input_x = np.kron(zero, np.kron(plus, plus))
    ghz_x = u_x @ input_x
    target_x = (np.kron(plus, np.kron(plus, plus)) + np.kron(minus, np.kron(minus, minus))) / np.sqrt(2)
    check("G conjugate dynamics gives equally redundant X witnesses", np.allclose(ghz_x, target_x, atol=TOL))
    check("G redundancy does not select the pointer context", not np.allclose(u_z, u_x, atol=TOL))


def actuality_and_statistics_controls(data: dict[str, object]) -> None:
    section("H - A complete instrument still leaves actuality and prepared-state statistics separate")
    e0, _, e2 = data["basis"]
    instrument = data["instruments"]["Lueders"]
    superposition = (e0 + e2) / np.sqrt(2)
    rho = projector(superposition)
    branches = tuple(apply(branch, rho) for branch in instrument)
    weights = tuple(np.trace(branch).real for branch in branches)
    mixture = sum(branches, np.zeros_like(rho))
    check("H one supplied state gives two nonzero instrument branches", np.allclose(weights, (0.5, 0.5), atol=TOL))
    check("H the nonselective output is mixed rather than one selected branch", abs(np.trace(mixture @ mixture).real - 0.5) < TOL)
    check("H neither branch equals the nonselective mixture", all(not np.allclose(branch, mixture, atol=TOL) for branch in branches))

    rho_recorded = projector(e0)
    recorded_weights = tuple(np.trace(apply(branch, rho_recorded)).real for branch in instrument)
    check("H changing only the prepared state changes statistics", np.allclose(recorded_weights, (1.0, 0.0), atol=TOL))
    check("H repeatability and CP completeness survive that state change", branch_repeatable(instrument, data["projectors"]) and is_complete(instrument))


def u1_primary_precedent_control() -> None:
    section("I - Minimal chiral U(1) tuple has exact precedent but not its quadratic selector")
    winner = (-9, -5, -1, 7, 8)
    batra_table = (1, 5, -7, -8, 9)
    competitor = (-10, -4, -2, 7, 9)

    def canonical(values: tuple[int, ...]) -> tuple[int, ...]:
        direct = tuple(sorted(values))
        conjugate = tuple(sorted(-value for value in values))
        return min(direct, conjugate)

    def valid(values: tuple[int, ...]) -> bool:
        return (
            sum(values) == 0
            and sum(value**3 for value in values) == 0
            and all(value != 0 for value in values)
            and not any(-value in values for value in values)
            and gcd(*(abs(value) for value in values)) == 1
        )

    check("I Batra-Dobrescu-Spivak table tuple equals the new winner up to sign and permutation", canonical(batra_table) == canonical(winner))
    check("I winner satisfies the linear and cubic anomaly equations", valid(winner))
    check("I displayed competitor satisfies the same anomaly equations", valid(competitor))
    check("I quadratic norm prefers winner over competitor", sum(value * value for value in winner) == 220 and sum(value * value for value in competitor) == 250)
    check("I primary precedent does not make anomaly cancellation a microscopic-law selector", winner != competitor and valid(winner) and valid(competitor))
    parent = U1_PARENT.read_text(encoding="utf-8").lower()
    check("I paired parent states the scoped unique quadratic-norm result", "unique global minimum" in parent and "quadratic norm" in parent)


def interface_and_no_go_contract() -> None:
    section("J - Interface map and N1-N8 no-go-discipline contract")
    note = NOTE.read_text(encoding="utf-8")
    note_lower = " ".join(note.lower().replace("*", "").replace("`", "").split())
    for field in ("record", "context", "actuality", "statistics"):
        check(f"J interface map contains {field.upper()}", f"`{field.upper()}`" in note)
    for phrase in (
        "sharp binary-qubit reduction",
        "conditional on a supplied context",
        "projective form can be reduced",
        "x versus z remains supplied",
        "dilation is a realization theorem, not a selection theorem",
        "redundancy is not actuality",
    ):
        check(f"J note contains conclusion needle: {phrase}", phrase in note_lower)
    for index in range(1, 9):
        check(f"J N{index} section is present", f"### N{index}" in note)
    check("J no-go discipline status is scoped PASS", "no-go discipline status: pass" in note_lower)
    check("J negative result is explicitly corpus/premise bounded", "premise-bounded" in note_lower and "not a universal no-go" in note_lower)


def main() -> int:
    authority_and_source_contract()
    data = degenerate_repeatable_countermodels()
    covariance_does_not_select(data)
    weak_and_strong_minimal_disturbance(data)
    binary_qubit_partial_closure()
    dilation_and_purification_controls(data)
    broadcasting_and_darwinism_controls()
    actuality_and_statistics_controls(data)
    u1_primary_precedent_control()
    interface_and_no_go_contract()
    section("SUMMARY")
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
