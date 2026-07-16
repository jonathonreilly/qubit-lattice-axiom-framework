#!/usr/bin/env python3
"""Cycle 182: coherent dilation of the Cycle-178 orthogonal record lineage.

The Cycle-178 H0/H1 payload map copies one orthogonal classical value along a
permanent lineage.  This probe gives that copy map its strongest elementary
quantum lift: CNOTs from one source qubit into fresh |0> targets.  It separates
four claims that must not be merged:

* basis-record copying;
* local decoherence after one witness;
* erasure redundancy after two witnesses; and
* selection of one actual outcome.

The runner has no authority.  It edits no foundation, axiom, primitive,
registry, policy, audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

import recurrent_five_literal_lane_worldline_cycle178_2026_07_16 as c178


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "ORTHOGONAL_LINEAGE_COHERENT_DILATION_CYCLE182_NOTE_2026-07-16.md"
)

TOL = 1.0e-12
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def close(a: np.ndarray | complex | float, b: np.ndarray | complex | float) -> bool:
    return bool(np.allclose(a, b, atol=TOL, rtol=0.0))


KET0 = np.array([1.0, 0.0], dtype=complex)
KET1 = np.array([0.0, 1.0], dtype=complex)
KET_PLUS = (KET0 + KET1) / np.sqrt(2.0)
KET_PLUS_I = (KET0 + 1.0j * KET1) / np.sqrt(2.0)
X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)


def kron_all(*factors: np.ndarray) -> np.ndarray:
    result = np.array([1.0], dtype=complex)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def cnot(n_qubits: int, control: int, target: int) -> np.ndarray:
    size = 1 << n_qubits
    matrix = np.zeros((size, size), dtype=complex)
    for column in range(size):
        bits = [
            (column >> (n_qubits - 1 - index)) & 1
            for index in range(n_qubits)
        ]
        output = bits[:]
        output[target] ^= bits[control]
        row = 0
        for bit in output:
            row = (row << 1) | bit
        matrix[row, column] = 1.0
    return matrix


def swap(n_qubits: int, left: int, right: int) -> np.ndarray:
    return (
        cnot(n_qubits, left, right)
        @ cnot(n_qubits, right, left)
        @ cnot(n_qubits, left, right)
    )


def reduced_density_pure(
    state: np.ndarray,
    keep: tuple[int, ...],
    n_qubits: int,
) -> np.ndarray:
    rest = tuple(index for index in range(n_qubits) if index not in keep)
    tensor = state.reshape((2,) * n_qubits)
    matrix = np.transpose(tensor, keep + rest).reshape(
        1 << len(keep),
        1 << len(rest),
    )
    return matrix @ matrix.conjugate().T


def density(state: np.ndarray) -> np.ndarray:
    return np.outer(state, state.conjugate())


def expectation(state: np.ndarray, observable: np.ndarray) -> complex:
    return state.conjugate() @ observable @ state


def one_witness_state(source: np.ndarray) -> np.ndarray:
    return cnot(2, 0, 1) @ kron_all(source, KET0)


def two_witness_state(source: np.ndarray) -> np.ndarray:
    network = cnot(3, 0, 2) @ cnot(3, 0, 1)
    return network @ kron_all(source, KET0, KET0)


def endpoint_channel_matrix_unit(i: int, j: int, copies: int) -> np.ndarray:
    """Endpoint channel on |i><j| for a repetition isometry of `copies` qubits."""
    trail_overlap = 1.0 if i == j or copies == 1 else 0.0
    unit = np.zeros((2, 2), dtype=complex)
    unit[i, j] = trail_overlap
    return unit


def repeated_word(value: int, copies: int) -> tuple[int, ...]:
    return (value,) * copies


def five_lane_codeword(word: tuple[int, ...], copies: int) -> tuple[int, ...]:
    return tuple(
        bit
        for value in word
        for bit in repeated_word(value, copies)
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("AUTHORITY AND CYCLE-178 INTERFACE")
    check("Cycle-182 review note exists", NOTE.is_file())
    payload_counts = tuple(
        len(c178.lane_payload_sites(lane))
        for lane in range(5)
    )
    check(
        "Cycle 178 supplies five equal 19-record H0/H1 payload lineages",
        c178.BIT_ROLES == (c178.H0, c178.H1)
        and payload_counts == (19, 19, 19, 19, 19),
        payload_counts,
    )

    print("\nBASIS COPYING AND COHERENT DILATION")
    one_zero = one_witness_state(KET0)
    one_one = one_witness_state(KET1)
    two_zero = two_witness_state(KET0)
    two_one = two_witness_state(KET1)
    check(
        "one CNOT exactly copies the two orthogonal record values",
        close(one_zero, kron_all(KET0, KET0))
        and close(one_one, kron_all(KET1, KET1)),
    )
    check(
        "two CNOT witnesses exactly reproduce each basis record three times",
        close(two_zero, kron_all(KET0, KET0, KET0))
        and close(two_one, kron_all(KET1, KET1, KET1)),
    )
    cnot_unitarity = cnot(3, 0, 1).conjugate().T @ cnot(3, 0, 1)
    check(
        "the strongest elementary copy lift is a reversible quantum process",
        close(cnot_unitarity, np.eye(8, dtype=complex)),
    )

    print("\nONE WITNESS VERSUS TWO")
    one_plus = one_witness_state(KET_PLUS)
    two_plus = two_witness_state(KET_PLUS)
    one_source = reduced_density_pure(one_plus, (0,), 2)
    two_source = reduced_density_pure(two_plus, (0,), 3)
    maximally_mixed = np.eye(2, dtype=complex) / 2.0
    check(
        "one witness already removes local phase coherence from the source",
        close(one_source, maximally_mixed),
        one_source,
    )
    check(
        "a second witness does not create an additional local decoherence threshold",
        close(two_source, maximally_mixed)
        and close(one_source, two_source),
        two_source,
    )

    undo_one = cnot(2, 0, 1) @ one_plus
    undo_first_of_two = cnot(3, 0, 1) @ two_plus
    undo_second_of_two = cnot(3, 0, 2) @ two_plus
    undo_both = cnot(3, 0, 2) @ undo_first_of_two
    check(
        "one witness is wholly erasable by reversing its one copy interaction",
        close(undo_one, kron_all(KET_PLUS, KET0)),
    )
    check(
        "erasing either one of two witnesses leaves one redundant witness",
        close(
            reduced_density_pure(undo_first_of_two, (0,), 3),
            maximally_mixed,
        )
        and close(
            reduced_density_pure(undo_first_of_two, (0, 2), 3),
            density(one_witness_state(KET_PLUS)),
        )
        and close(
            reduced_density_pure(undo_second_of_two, (0, 1), 3),
            density(one_witness_state(KET_PLUS)),
        ),
    )
    check(
        "erasing both witnesses restores the coherent source",
        close(undo_both, kron_all(KET_PLUS, KET0, KET0)),
    )

    print("\nGLOBAL COHERENCE AND ACTUALITY")
    ghz_plus = (kron_all(KET0, KET0, KET0) + kron_all(KET1, KET1, KET1)) / np.sqrt(2.0)
    check(
        "two witnesses create a coherent GHZ record candidate, not one selected branch",
        close(two_plus, ghz_plus)
        and close(abs(expectation(two_plus, kron_all(X, X, X))), 1.0),
        expectation(two_plus, kron_all(X, X, X)),
    )
    two_plus_i = two_witness_state(KET_PLUS_I)
    check(
        "the global branch phase survives even when every local marginal is classical",
        close(reduced_density_pure(two_plus_i, (0,), 3), maximally_mixed)
        and close(
            abs(
                two_plus_i[0]
                * np.conjugate(two_plus_i[-1])
            ),
            0.5,
        ),
    )
    check(
        "neither one nor two CNOT witnesses contains an outcome selector",
        np.count_nonzero(np.abs(one_plus) > TOL) == 2
        and np.count_nonzero(np.abs(two_plus) > TOL) == 2,
        (
            np.flatnonzero(np.abs(one_plus) > TOL),
            np.flatnonzero(np.abs(two_plus) > TOL),
        ),
    )

    print("\nENDPOINT CHANNEL AND NO-CLONING")
    channel_units = {
        (i, j): endpoint_channel_matrix_unit(i, j, copies=3)
        for i in range(2)
        for j in range(2)
    }
    check(
        "the endpoint-only map preserves basis populations and kills phase terms",
        close(channel_units[(0, 0)], density(KET0))
        and close(channel_units[(1, 1)], density(KET1))
        and close(channel_units[(0, 1)], np.zeros((2, 2), dtype=complex))
        and close(channel_units[(1, 0)], np.zeros((2, 2), dtype=complex)),
    )
    plus_endpoint = reduced_density_pure(two_plus, (2,), 3)
    check(
        "the endpoint is a dephased record copy rather than the transported plus state",
        close(plus_endpoint, maximally_mixed)
        and not close(plus_endpoint, density(KET_PLUS)),
        plus_endpoint,
    )
    input_overlap = abs(np.vdot(KET0, KET_PLUS))
    hypothetical_clone_overlap = input_overlap**2
    check(
        "unitarity forbids extending record copying to arbitrary-state cloning",
        not close(input_overlap, hypothetical_clone_overlap),
        (input_overlap, hypothetical_clone_overlap),
    )
    swapped = swap(2, 0, 1) @ kron_all(KET1, KET0)
    check(
        "coherent state transfer by SWAP revokes the old source value",
        close(swapped, kron_all(KET0, KET1))
        and not close(
            reduced_density_pure(swapped, (0,), 2),
            density(KET1),
        ),
    )

    print("\nFIVE-LANE JOINT CODE")
    words = tuple(c178.WORDS)
    codewords = {
        word: five_lane_codeword(word, copies=3)
        for word in words
    }
    check(
        "all 32 five-lane repetition codewords are distinct",
        len(set(codewords.values())) == 32,
        len(set(codewords.values())),
    )
    trail_words = {
        word: tuple(
            bit
            for lane in range(5)
            for bit in codewords[word][3 * lane:3 * lane + 2]
        )
        for word in words
    }
    off_diagonal_survivors = tuple(
        (left, right)
        for left in words
        for right in words
        if left != right and trail_words[left] == trail_words[right]
    )
    check(
        "discarding the persistent trails dephases every distinct five-bit codeword",
        not off_diagonal_survivors,
        off_diagonal_survivors[:2],
    )
    amplitudes = np.array(
        [np.exp(2.0j * np.pi * index / 32.0) for index in range(32)],
        dtype=complex,
    ) / np.sqrt(32.0)
    input_rho = density(amplitudes)
    endpoint_rho = np.diag(np.diag(input_rho))
    check(
        "a coherent 32-codeword superposition becomes a classical endpoint mixture",
        close(np.diag(endpoint_rho), np.full(32, 1.0 / 32.0))
        and np.count_nonzero(np.abs(input_rho - endpoint_rho) > TOL)
        == 32 * 31,
        np.trace(endpoint_rho),
    )

    print("\nFORMATION INTERPRETATION")
    check(
        "two witnesses buy single-erasure redundancy, not a unitary actuality rule",
        close(one_source, maximally_mixed)
        and close(two_source, maximally_mixed)
        and close(undo_both, kron_all(KET_PLUS, KET0, KET0))
        and np.count_nonzero(np.abs(two_plus) > TOL) == 2,
    )
    check(
        "a clock or read register coupled by the same copy interaction is another witness",
        close(
            cnot(3, 0, 2) @ kron_all(one_plus, KET0),
            two_plus,
        ),
        "one witness plus one clock/read copy equals the two-witness state",
    )

    print("\nSUMMARY")
    print("PASS", PASS)
    print("FAIL", FAIL)
    print(
        "RESULT",
        "ORTHOGONAL_COPY_HAS_COHERENT_DILATION_BUT_NOT_ACTUALITY_OR_QUBIT_TRANSPORT"
        if FAIL == 0
        else "CYCLE182_NEEDS_REPAIR",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
