#!/usr/bin/env python3
"""Cycle 279: local conditional instrument to candidate Record-close tournament.

Three independent finite routes act on one generic parity-even observable on
three ordinary M2 sites: a coherent pointer/uncompute route, an explicit
environment/dephasing route, and an append-only candidate fact plus causal
close.  The runner tests exactly what each route supplies without renaming a
pointer, reduced channel, close token, or branch weight as a framework Record,
occurrence, clock, rate, energy, source, or Born law.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "LOCAL_INSTRUMENT_TO_RECORD_CLOSE_TOURNAMENT_CYCLE279_NOTE_2026-07-17.md"
)
PASS = 0
FAIL = 0
TOL = 3.0e-11


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-279 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "generic parity-even",
        "coherent pointer correlation/uncompute",
        "measure-and-forget",
        "explicit environment",
        "append-only candidate fact",
        "causal close",
        "identical visible pointer",
        "different fine archives",
        "choi residual",
        "gate deletion",
        "repeatability",
        "erasure/reconnection",
        "branch selection",
        "permanence import",
        "cycle-189-style conditional instrument",
        "cycle-209",
        "all-five-lane bridge consequences",
        "pointer copying is not a record",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no route-independent obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "note preserves route, endpoint, N1-N8, and semantic-firewall contracts",
        not missing,
        missing,
    )


def basis(dimension: int, index: int) -> np.ndarray:
    vector = np.zeros(dimension, dtype=complex)
    vector[index] = 1.0
    return vector


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


@dataclass(frozen=True)
class EvenObservable:
    parity: np.ndarray
    effect_yes: np.ndarray
    effect_no: np.ndarray
    observable: np.ndarray
    fine_vectors: tuple[np.ndarray, ...]
    fine_projectors: tuple[np.ndarray, ...]
    yes_labels: tuple[int, ...]


def generic_even_observable() -> EvenObservable:
    """A non-diagonal binary observable commuting with three-mode parity."""
    dimension = 8
    even_indices = (0, 3, 5, 6)
    odd_indices = (1, 2, 4, 7)
    fourier = np.asarray(
        [[np.exp(2j * np.pi * row * column / 4) / 2 for column in range(4)]
         for row in range(4)],
        dtype=complex,
    )
    hadamard = np.asarray(
        ((1, 1, 1, 1), (1, -1, 1, -1), (1, 1, -1, -1), (1, -1, -1, 1)),
        dtype=complex,
    ) / 2
    even = []
    odd = []
    for column in range(4):
        even.append(sum(fourier[row, column] * basis(dimension, index)
                        for row, index in enumerate(even_indices)))
        odd.append(sum(hadamard[row, column] * basis(dimension, index)
                       for row, index in enumerate(odd_indices)))
    fine_vectors = tuple(even + odd)
    fine_projectors = tuple(projector(vector) for vector in fine_vectors)
    yes_labels = (0, 1, 4, 5)
    effect_yes = sum((fine_projectors[index] for index in yes_labels),
                     np.zeros((dimension, dimension), dtype=complex))
    effect_no = np.eye(dimension, dtype=complex) - effect_yes
    observable = 0.73 * effect_yes - 1.17 * effect_no
    parity = np.diag(
        [1 if int(index).bit_count() % 2 == 0 else -1 for index in range(dimension)]
    ).astype(complex)
    return EvenObservable(
        parity, effect_yes, effect_no, observable, fine_vectors,
        fine_projectors, yes_labels
    )


def xor_shift(dimension: int, mask: int) -> np.ndarray:
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        matrix[source ^ mask, source] = 1.0
    return matrix


def pointer_unitary(model: EvenObservable) -> np.ndarray:
    return np.kron(model.effect_no, np.eye(2)) + np.kron(
        model.effect_yes, xor_shift(2, 1)
    )


def channel(kraus: tuple[np.ndarray, ...], density: np.ndarray) -> np.ndarray:
    return sum(
        (operator @ density @ operator.conj().T for operator in kraus),
        np.zeros_like(density),
    )


def choi(kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    dimension = kraus[0].shape[0]
    result = np.zeros((dimension**2, dimension**2), dtype=complex)
    for operator in kraus:
        vector = operator.reshape(-1, order="F")
        result += np.outer(vector, vector.conj()) / dimension
    return result


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    difference = (left - right + (left - right).conj().T) / 2
    return float(np.sum(np.abs(np.linalg.eigvalsh(difference))) / 2)


def partial_density_pure(
    state: np.ndarray, dimensions: tuple[int, ...], keep: tuple[int, ...]
) -> np.ndarray:
    tensor = state.reshape(dimensions)
    rest = tuple(axis for axis in range(len(dimensions)) if axis not in keep)
    ordered = np.transpose(tensor, keep + rest)
    keep_dimension = int(np.prod([dimensions[axis] for axis in keep]))
    matrix = ordered.reshape(keep_dimension, -1)
    return matrix @ matrix.conj().T


def random_density(dimension: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    matrix = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    density = matrix @ matrix.conj().T
    return density / np.trace(density)


def route_one_conditional_instrument(model: EvenObservable) -> dict[str, float]:
    dimension = model.effect_yes.shape[0]
    unitary = pointer_unitary(model)
    blank = basis(2, 0)
    yes = basis(2, 1)
    isometry = unitary @ np.kron(np.eye(dimension), blank[:, None])
    # Pointer Kraus blocks in system-major ordering.
    reshaped = isometry.reshape(dimension, 2, dimension)
    kraus_no = reshaped[:, 0, :]
    kraus_yes = reshaped[:, 1, :]
    check(
        "route 1 is a unitary coherent pointer correlation",
        np.linalg.norm(unitary.conj().T @ unitary - np.eye(2 * dimension)) < TOL
        and np.linalg.norm(unitary @ unitary - np.eye(2 * dimension)) < TOL,
    )
    check(
        "route 1 instantiates the Cycle-189 conditional-instrument Kraus clauses",
        np.linalg.norm(kraus_no - model.effect_no) < TOL
        and np.linalg.norm(kraus_yes - model.effect_yes) < TOL
        and np.linalg.norm(
            kraus_no.conj().T @ kraus_no
            + kraus_yes.conj().T @ kraus_yes
            - np.eye(dimension)
        )
        < TOL,
    )
    check(
        "route 1 selective branches are exactly repeatable and mutually exclusive",
        np.linalg.norm(kraus_no @ kraus_no - kraus_no) < TOL
        and np.linalg.norm(kraus_yes @ kraus_yes - kraus_yes) < TOL
        and np.linalg.norm(kraus_no @ kraus_yes) < TOL
        and np.linalg.norm(kraus_yes @ kraus_no) < TOL,
    )

    cross_state = (model.fine_vectors[0] + model.fine_vectors[2]) / np.sqrt(2)
    input_joint = np.kron(cross_state, blank)
    written = unitary @ input_joint
    restored = unitary @ written
    check(
        "route 1 erases and reconnects exactly under pointer uncompute",
        np.linalg.norm(restored - input_joint) < TOL,
        np.linalg.norm(restored - input_joint),
    )
    pointer_density = partial_density_pure(written, (dimension, 2), (1,))
    check(
        "route 1 correlates a nontrivial visible pointer without selecting a branch",
        np.linalg.norm(pointer_density - np.eye(2) / 2) < TOL
        and abs(np.vdot(written, written) - 1) < TOL,
        pointer_density,
    )

    same_pointer_twice = unitary @ written
    check(
        "reusing the same pointer twice uncomputes rather than appends a fact",
        np.linalg.norm(same_pointer_twice - input_joint) < TOL,
    )

    # Two fresh pointer factors: both carry the same coarse value, while the
    # system reduced channel equals the one-pointer nonselective channel.
    identity_pointer = np.eye(2)
    write_first = np.kron(model.effect_no, np.eye(4)) + np.kron(
        model.effect_yes, np.kron(xor_shift(2, 1), identity_pointer)
    )
    write_second = np.kron(model.effect_no, np.eye(4)) + np.kron(
        model.effect_yes, np.kron(identity_pointer, xor_shift(2, 1))
    )
    input_two = np.kron(cross_state, basis(4, 0))
    two_written = write_second @ write_first @ input_two
    one_system = partial_density_pure(written, (dimension, 2), (0,))
    two_system = partial_density_pure(two_written, (dimension, 2, 2), (0,))
    check(
        "fresh redundant coherent pointers preserve the same reduced instrument channel",
        np.linalg.norm(one_system - two_system) < TOL,
        np.linalg.norm(one_system - two_system),
    )

    omitted = projector(cross_state)
    forgotten = channel((model.effect_no, model.effect_yes), omitted)
    check(
        "Cycle-189 identity containment distinguishes omission from measure-and-forget",
        np.linalg.norm(omitted - forgotten) > 0.5,
        np.linalg.norm(omitted - forgotten),
    )
    return {
        "omission_forgotten_residual": float(np.linalg.norm(omitted - forgotten)),
        "pointer_purity": float(np.trace(pointer_density @ pointer_density).real),
    }


def fine_archive_unitary(model: EvenObservable) -> np.ndarray:
    identity_pointer = np.eye(2)
    result = np.zeros((8 * 2 * 8, 8 * 2 * 8), dtype=complex)
    for label, fine_projector in enumerate(model.fine_projectors):
        result += np.kron(
            fine_projector, np.kron(identity_pointer, xor_shift(8, label))
        )
    return result


def route_two_environment(model: EvenObservable) -> dict[str, float]:
    dimension = 8
    pointer = pointer_unitary(model)
    # Coarse measure-and-forget dilation: write A, copy A to E, uncompute A.
    lifted_pointer = np.kron(pointer, np.eye(2))
    copy_ae = np.kron(np.eye(dimension), np.asarray(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    ))
    coarse_dilation = lifted_pointer @ copy_ae @ lifted_pointer
    check(
        "route 2 coarse measure-and-forget has an explicit unitary environment dilation",
        np.linalg.norm(coarse_dilation.conj().T @ coarse_dilation - np.eye(32)) < TOL,
    )

    cross_state = (model.fine_vectors[0] + model.fine_vectors[2]) / np.sqrt(2)
    input_coarse = np.kron(cross_state, basis(4, 0))
    coarse_output = coarse_dilation @ input_coarse
    visible_pointer = partial_density_pure(coarse_output, (8, 2, 2), (1,))
    reduced_system = partial_density_pure(coarse_output, (8, 2, 2), (0,))
    expected_coarse = channel(
        (model.effect_no, model.effect_yes), projector(cross_state)
    )
    check(
        "measure-and-forget resets the visible pointer and realizes coarse dephasing",
        np.linalg.norm(visible_pointer - projector(basis(2, 0))) < TOL
        and np.linalg.norm(reduced_system - expected_coarse) < TOL,
        np.linalg.norm(reduced_system - expected_coarse),
    )
    reconnected = coarse_dilation.conj().T @ coarse_output
    check(
        "environment reconnection reverses the complete measure-and-forget dilation",
        np.linalg.norm(reconnected - input_coarse) < TOL,
        np.linalg.norm(reconnected - input_coarse),
    )

    # A second route keeps the same visible coarse pointer but archives the
    # complete eigenvector label in an eight-state environment.
    lifted = np.kron(pointer, np.eye(8))
    fine_unitary = fine_archive_unitary(model)
    fine_dilation = fine_unitary @ lifted
    blank_pointer_environment = np.kron(basis(2, 0), basis(8, 0))
    fine_zero = fine_dilation @ np.kron(model.fine_vectors[0], blank_pointer_environment)
    fine_one = fine_dilation @ np.kron(model.fine_vectors[1], blank_pointer_environment)
    pointer_zero = partial_density_pure(fine_zero, (8, 2, 8), (1,))
    pointer_one = partial_density_pure(fine_one, (8, 2, 8), (1,))
    environment_zero = partial_density_pure(fine_zero, (8, 2, 8), (2,))
    environment_one = partial_density_pure(fine_one, (8, 2, 8), (2,))
    archive_distance = trace_distance(environment_zero, environment_one)
    check(
        "identical visible pointer values coexist with orthogonal fine archives",
        np.linalg.norm(pointer_zero - pointer_one) < TOL
        and np.linalg.norm(pointer_zero - projector(basis(2, 1))) < TOL
        and abs(archive_distance - 1.0) < TOL,
        archive_distance,
    )

    coarse_kraus = (model.effect_no, model.effect_yes)
    fine_kraus = model.fine_projectors
    choi_residual = trace_distance(choi(coarse_kraus), choi(fine_kraus))
    held = random_density(8, 279)
    held_disturbance = trace_distance(
        channel(coarse_kraus, held), channel(fine_kraus, held)
    )
    check(
        "fine archive changes the instrument channel despite the same coarse pointer alphabet",
        choi_residual > 0.3 and held_disturbance > 0.1,
        (choi_residual, held_disturbance),
    )
    check(
        "coarse and fine measure-and-forget channels are repeatable and idempotent",
        np.linalg.norm(
            channel(coarse_kraus, channel(coarse_kraus, held))
            - channel(coarse_kraus, held)
        )
        < TOL
        and np.linalg.norm(
            channel(fine_kraus, channel(fine_kraus, held))
            - channel(fine_kraus, held)
        )
        < TOL,
    )

    within_yes = (model.fine_vectors[0] + model.fine_vectors[1]) / np.sqrt(2)
    fine_superposed = fine_dilation @ np.kron(within_yes, blank_pointer_environment)
    fine_reduced = partial_density_pure(fine_superposed, (8, 2, 8), (0,))
    coarse_conditional = projector(within_yes)
    check(
        "fine archival destroys within-outcome coherence that the coarse Lüders branch retains",
        abs(np.trace(fine_reduced @ fine_reduced).real - 0.5) < TOL
        and abs(np.trace(coarse_conditional @ coarse_conditional).real - 1.0) < TOL,
        (
            np.trace(fine_reduced @ fine_reduced).real,
            np.trace(coarse_conditional @ coarse_conditional).real,
        ),
    )
    fine_restored = fine_dilation.conj().T @ fine_superposed
    check(
        "the fine archive is globally reversible when its environment reconnects",
        np.linalg.norm(
            fine_restored - np.kron(within_yes, blank_pointer_environment)
        )
        < TOL,
    )
    return {
        "choi_trace_distance": choi_residual,
        "held_channel_distance": held_disturbance,
        "archive_distance": archive_distance,
    }


# Candidate append interface ancilla bits.
A, DONE, UNCOMPUTED, FACT_NO, FACT_YES, CLOSE, ARCHIVE_NO, ARCHIVE_YES = range(8)
ANCILLA_DIMENSION = 2**8


def permutation_for_flip(target: int, controls: dict[int, int] | None = None) -> np.ndarray:
    controls = controls or {}
    mapping = np.arange(ANCILLA_DIMENSION)
    for source in range(ANCILLA_DIMENSION):
        if all(((source >> bit) & 1) == value for bit, value in controls.items()):
            mapping[source] = source ^ (1 << target)
    return mapping


def apply_permutation(state: np.ndarray, mapping: np.ndarray) -> np.ndarray:
    matrix = state.reshape(8, ANCILLA_DIMENSION)
    output = np.zeros_like(matrix)
    output[:, mapping] = matrix
    return output.reshape(-1)


def apply_controlled_pointer(
    state: np.ndarray, model: EvenObservable
) -> np.ndarray:
    matrix = state.reshape(8, ANCILLA_DIMENSION)
    pointer_permutation = np.arange(ANCILLA_DIMENSION) ^ (1 << A)
    output = model.effect_no @ matrix + model.effect_yes @ matrix[:, pointer_permutation]
    return output.reshape(-1)


def append_gates(
    model: EvenObservable,
    data_coupling: bool = True,
    done: bool = True,
    fact_no: bool = True,
    fact_yes: bool = True,
    uncompute: bool = True,
    close: bool = True,
):
    gates = []
    if data_coupling:
        gates.append(("pointer", None))
    if done:
        gates.append(("permutation", permutation_for_flip(DONE)))
    if fact_no:
        gates.append(("permutation", permutation_for_flip(
            FACT_NO, {DONE: 1, A: 0}
        )))
    if fact_yes:
        gates.append(("permutation", permutation_for_flip(
            FACT_YES, {DONE: 1, A: 1}
        )))
    if uncompute:
        if data_coupling:
            gates.append(("pointer", None))
        gates.append(("permutation", permutation_for_flip(UNCOMPUTED)))
    if close:
        gates.append(("permutation", permutation_for_flip(
            CLOSE, {UNCOMPUTED: 1, FACT_NO: 1}
        )))
        gates.append(("permutation", permutation_for_flip(
            CLOSE, {UNCOMPUTED: 1, FACT_YES: 1}
        )))
    return tuple(gates)


def apply_gate_sequence(
    state: np.ndarray, gates, model: EvenObservable, inverse: bool = False
) -> np.ndarray:
    sequence = tuple(reversed(gates)) if inverse else gates
    output = state.copy()
    for kind, payload in sequence:
        if kind == "pointer":
            output = apply_controlled_pointer(output, model)
        else:
            output = apply_permutation(output, payload)
    return output


def ancilla_probability(state: np.ndarray, conditions: dict[int, int]) -> float:
    matrix = state.reshape(8, ANCILLA_DIMENSION)
    indices = [
        index
        for index in range(ANCILLA_DIMENSION)
        if all(((index >> bit) & 1) == value for bit, value in conditions.items())
    ]
    return float(np.sum(np.abs(matrix[:, indices]) ** 2))


def append_isometry(model: EvenObservable, gates) -> np.ndarray:
    columns = []
    blank = basis(ANCILLA_DIMENSION, 0)
    for index in range(8):
        columns.append(
            apply_gate_sequence(np.kron(basis(8, index), blank), gates, model)
        )
    return np.column_stack(columns)


def route_three_candidate_close(model: EvenObservable) -> dict[str, float]:
    gates = append_gates(model)
    isometry = append_isometry(model, gates)
    gram_error = np.linalg.norm(isometry.conj().T @ isometry - np.eye(8))
    # Expected ancilla packets on the Q and P branches.
    no_index = sum(1 << bit for bit in (DONE, UNCOMPUTED, FACT_NO, CLOSE))
    yes_index = sum(1 << bit for bit in (DONE, UNCOMPUTED, FACT_YES, CLOSE))
    no_packet = basis(ANCILLA_DIMENSION, no_index)
    yes_packet = basis(ANCILLA_DIMENSION, yes_index)
    expected = np.column_stack(
        [
            np.kron(model.effect_no[:, column], no_packet)
            + np.kron(model.effect_yes[:, column], yes_packet)
            for column in range(8)
        ]
    )
    check(
        "route 3 appends the coarse fact only after pointer uncompute and causal close",
        gram_error < TOL and np.linalg.norm(isometry - expected) < TOL,
        (gram_error, np.linalg.norm(isometry - expected)),
    )

    cross_state = (model.fine_vectors[0] + model.fine_vectors[2]) / np.sqrt(2)
    input_state = np.kron(cross_state, basis(ANCILLA_DIMENSION, 0))
    output = apply_gate_sequence(input_state, gates, model)
    check(
        "candidate close has facts and close on both coherent branches but no selected branch",
        abs(ancilla_probability(output, {CLOSE: 1}) - 1.0) < TOL
        and abs(ancilla_probability(output, {FACT_NO: 1}) - 0.5) < TOL
        and abs(ancilla_probability(output, {FACT_YES: 1}) - 0.5) < TOL
        and abs(np.vdot(output, output) - 1.0) < TOL,
    )
    recovered = apply_gate_sequence(output, gates, model, inverse=True)
    check(
        "unrestricted reconnection erases the candidate fact and close exactly",
        np.linalg.norm(recovered - input_state) < TOL,
        np.linalg.norm(recovered - input_state),
    )

    whole_deleted_gates = append_gates(
        model, data_coupling=False, done=False, uncompute=False
    )
    whole_deleted = apply_gate_sequence(input_state, whole_deleted_gates, model)
    split_deleted_gates = append_gates(model, data_coupling=False)
    split_deleted = apply_gate_sequence(input_state, split_deleted_gates, model)
    check(
        "whole-instrument deletion creates no fact and no close",
        ancilla_probability(whole_deleted, {CLOSE: 1}) < TOL
        and ancilla_probability(whole_deleted, {FACT_NO: 1}) < TOL
        and ancilla_probability(whole_deleted, {FACT_YES: 1}) < TOL,
    )
    split_false_close = ancilla_probability(split_deleted, {CLOSE: 1, FACT_NO: 1})
    check(
        "split data-coupling deletion spoofs the supplied done/fact interface",
        abs(split_false_close - 1.0) < TOL,
        split_false_close,
    )

    no_yes_writer = apply_gate_sequence(
        input_state, append_gates(model, fact_yes=False), model
    )
    no_uncompute = apply_gate_sequence(
        input_state, append_gates(model, uncompute=False), model
    )
    check(
        "fact-writer and uncompute-token deletions block the affected causal close",
        abs(ancilla_probability(no_yes_writer, {CLOSE: 1}) - 0.5) < TOL
        and ancilla_probability(no_uncompute, {CLOSE: 1}) < TOL,
        (
            ancilla_probability(no_yes_writer, {CLOSE: 1}),
            ancilla_probability(no_uncompute, {CLOSE: 1}),
        ),
    )

    # Supplied append-only continuation: facts and close are controls only.
    fact_before = (
        ancilla_probability(output, {FACT_NO: 1}),
        ancilla_probability(output, {FACT_YES: 1}),
        ancilla_probability(output, {CLOSE: 1}),
    )
    append_no = permutation_for_flip(ARCHIVE_NO, {FACT_NO: 1, CLOSE: 1})
    append_yes = permutation_for_flip(ARCHIVE_YES, {FACT_YES: 1, CLOSE: 1})
    continued = apply_permutation(apply_permutation(output, append_no), append_yes)
    fact_after = (
        ancilla_probability(continued, {FACT_NO: 1}),
        ancilla_probability(continued, {FACT_YES: 1}),
        ancilla_probability(continued, {CLOSE: 1}),
    )
    check(
        "the supplied append-only continuation preserves original fact and close marginals",
        np.linalg.norm(np.asarray(fact_before) - np.asarray(fact_after)) < TOL
        and abs(ancilla_probability(continued, {ARCHIVE_NO: 1}) - 0.5) < TOL
        and abs(ancilla_probability(continued, {ARCHIVE_YES: 1}) - 0.5) < TOL,
        (fact_before, fact_after),
    )

    # Each XOR writer is its own inverse: reuse on the same target clears it
    # rather than appending a new immutable fact.
    no_writer = permutation_for_flip(FACT_NO, {DONE: 1, A: 0})
    yes_writer = permutation_for_flip(FACT_YES, {DONE: 1, A: 1})
    check(
        "reusing the same candidate fact interface is not append-only permanence",
        np.array_equal(no_writer[no_writer], np.arange(ANCILLA_DIMENSION))
        and np.array_equal(yes_writer[yes_writer], np.arange(ANCILLA_DIMENSION)),
    )
    return {
        "split_false_close": split_false_close,
        "isometry_error": gram_error,
    }


def domain_and_semantic_controls(model: EvenObservable) -> None:
    dimension = 8
    check(
        "the tested observable is a generic local parity-even three-M2 operator",
        np.linalg.norm(model.effect_yes @ model.effect_yes - model.effect_yes) < TOL
        and round(np.trace(model.effect_yes).real) == 4
        and np.linalg.norm(model.observable @ model.parity - model.parity @ model.observable) < TOL
        and np.linalg.norm(
            model.observable - np.diag(np.diag(model.observable))
        )
        > 0.5,
    )
    held = random_density(dimension, 999)
    yes_weight = float(np.trace(model.effect_yes @ held).real)
    no_weight = float(np.trace(model.effect_no @ held).real)
    check(
        "finite instrument weights are positive and normalized without a frequency claim",
        yes_weight >= 0 and no_weight >= 0 and abs(yes_weight + no_weight - 1) < TOL,
        (yes_weight, no_weight),
    )
    text = normalized(NOTE)
    check(
        "the result remains code-agnostic and preserves the occurrence/time/Record firewall",
        "cycle 251" not in text
        and "cycle 271" not in text
        and "pointer copying is not a record" in text
        and "no occurrence law" in text
        and "no clock law" in text
        and "no born law" in text,
    )


def main() -> int:
    note_contract()
    model = generic_even_observable()
    domain_and_semantic_controls(model)
    route_one = route_one_conditional_instrument(model)
    route_two = route_two_environment(model)
    route_three = route_three_candidate_close(model)
    check(
        "three routes have distinct exact operational dispositions",
        route_one["omission_forgotten_residual"] > 0.5
        and route_two["choi_trace_distance"] > 0.3
        and abs(route_three["split_false_close"] - 1.0) < TOL,
        (route_one, route_two, route_three),
    )
    check(
        "bounded clauses do not imply a route-independent obstruction or axiom pressure",
        "no route-independent obstruction" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
    )
    print("DATA route_one", route_one)
    print("DATA route_two", route_two)
    print("DATA route_three", route_three)
    print("SUMMARY", "PASS", PASS, "FAIL", FAIL)
    if FAIL:
        print("RESULT CYCLE279_LOCAL_INSTRUMENT_TO_RECORD_CLOSE_RED")
        return 1
    print("RESULT CYCLE279_LOCAL_INSTRUMENT_TO_RECORD_CLOSE_GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
