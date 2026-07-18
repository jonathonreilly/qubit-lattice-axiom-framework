#!/usr/bin/env python3
"""Cycle 284: finite process/history law from the Cycle-278 contact instrument.

Construct an explicit finite protocol/event domain on a four-dimensional
subspace of the actual 64-dimensional contact cell.  The domain contains
identity, selective/forgotten coarse contact instruments, and selective/
forgotten fine refinements.  It supplies a positive normalized composition
functional, identity containment, a candidate complete-record decoder, and a
tomographically complete record-fibre future-equivalence test.  Record typing
and occurrence are supplied; branch weights do not choose an actual member.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import redundant_archive_permanence_history_cycle283_2026_07_17 as c283


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CONTACT_ARCHIVE_FINITE_PROCESS_HISTORY_CYCLE284_NOTE_2026-07-17.md"
)
PASS = 0
FAIL = 0
TOL = 4.0e-11
TRAINING_DEPTHS = (1, 2, 3)
HELD_DEPTH = 4


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
        check("the Cycle-284 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycle-278 same-code contact instrument",
        "cycle-283 finite archive cylinders",
        "finite protocol/event domain",
        "normalized positive composition functional",
        "identity containment",
        "record decoder candidate",
        "record-fibre future-equivalence",
        "boundary inventory",
        "actuality inventory",
        "held-out protocol depth 4",
        "coarse/fine archive distinction",
        "lawful record typing is supplied",
        "no born-frequency",
        "no actual member is selected",
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
        "note preserves process, decoder, endpoint, N1-N8, and semantic contracts",
        not missing,
        missing,
    )


def basis(index: int) -> np.ndarray:
    vector = np.zeros(4, dtype=complex)
    vector[index] = 1.0
    return vector


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


I4 = np.eye(4, dtype=complex)
R = tuple(projector(basis(index)) for index in range(4))
Q0 = R[0] + R[1]
Q1 = R[2] + R[3]


@dataclass(frozen=True)
class Operation:
    name: str
    branches: tuple[tuple[str | None, tuple[np.ndarray, ...]], ...]


OPERATIONS = (
    Operation("I", ((None, (I4,)),)),
    Operation("Cs", (("0", (Q0,)), ("1", (Q1,)))),
    Operation("Cf", ((None, (Q0, Q1)),)),
    Operation(
        "Fs",
        tuple((format(index, "02b"), (R[index],)) for index in range(4)),
    ),
    Operation("Ff", ((None, R),)),
)
OPERATION_BY_NAME = {operation.name: operation for operation in OPERATIONS}


def paulis() -> dict[str, np.ndarray]:
    matrices = {
        "I": np.eye(2, dtype=complex),
        "X": np.asarray(((0, 1), (1, 0)), dtype=complex),
        "Y": np.asarray(((0, -1j), (1j, 0)), dtype=complex),
        "Z": np.asarray(((1, 0), (0, -1)), dtype=complex),
    }
    return {
        left + right: np.kron(matrices[left], matrices[right])
        for left in matrices
        for right in matrices
        if left + right != "II"
    }


TESTERS = paulis()


def preparations() -> dict[str, np.ndarray]:
    return {
        "cross_plus": projector((basis(0) + basis(2)) / np.sqrt(2)),
        "yes_fine_plus": projector((basis(2) + basis(3)) / np.sqrt(2)),
        "generic_phase": projector(
            (basis(0) + 1j * basis(1) + basis(2) - 1j * basis(3)) / 2
        ),
        "contact_basis": R[2],
    }


PREPARATIONS = preparations()


def apply_kraus(density: np.ndarray, kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    return sum(
        (operator @ density @ operator.conj().T for operator in kraus),
        np.zeros_like(density),
    )


def choi(kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    result = np.zeros((16, 16), dtype=complex)
    for operator in kraus:
        vector = operator.reshape(-1, order="F")
        result += np.outer(vector, vector.conj()) / 4
    return result


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    difference = (left - right + (left - right).conj().T) / 2
    return float(np.sum(np.abs(np.linalg.eigvalsh(difference))) / 2)


@dataclass(frozen=True)
class Leaf:
    preparation: str
    schedule: tuple[str, ...]
    outcomes: tuple[str | None, ...]
    density: np.ndarray

    @property
    def weight(self) -> float:
        return float(np.trace(self.density).real)

    @property
    def packet(self) -> tuple:
        return self.preparation, tuple(zip(self.schedule, self.outcomes))


def enumerate_domain(depth: int) -> tuple[Leaf, ...]:
    if depth < 0:
        raise ValueError("protocol depth must be nonnegative")
    leaves = tuple(
        Leaf(preparation, (), (), density)
        for preparation, density in PREPARATIONS.items()
    )
    for _slot in range(depth):
        next_leaves = []
        for leaf in leaves:
            for operation in OPERATIONS:
                for outcome, kraus in operation.branches:
                    next_leaves.append(
                        Leaf(
                            leaf.preparation,
                            leaf.schedule + (operation.name,),
                            leaf.outcomes + (outcome,),
                            apply_kraus(leaf.density, kraus),
                        )
                    )
        leaves = tuple(next_leaves)
    return leaves


def replay(
    preparation: str,
    schedule: tuple[str, ...],
    outcomes: tuple[str | None, ...],
) -> np.ndarray:
    density = PREPARATIONS[preparation].copy()
    for name, requested in zip(schedule, outcomes):
        operation = OPERATION_BY_NAME[name]
        matches = [kraus for outcome, kraus in operation.branches if outcome == requested]
        if len(matches) != 1:
            raise ValueError((name, requested, len(matches)))
        density = apply_kraus(density, matches[0])
    return density


def normalized_state(density: np.ndarray) -> np.ndarray | None:
    weight = float(np.trace(density).real)
    return None if weight < 1e-14 else density / weight


def fingerprint(density: np.ndarray) -> tuple[float, ...] | None:
    state = normalized_state(density)
    if state is None:
        return None
    return tuple(float(np.trace(tester @ state).real) for tester in TESTERS.values())


@lru_cache(maxsize=None)
def redundant_binary_archive(bit: int, depth: int) -> tuple[int, tuple[int, ...]]:
    """Run one actual Cycle-283 archive and return its canonical bit plus raw word."""
    if bit not in (0, 1):
        raise ValueError("archive bit must be binary")
    spec = c283.layout(depth)
    output = c283.apply_circuit(
        {(bit, 0): 1.0 + 0.0j},
        c283.circuit(depth),
        spec,
    )
    if len(output) != 1:
        raise ValueError((bit, depth, output))
    (contact, ancilla), amplitude = next(iter(output.items()))
    values = tuple((ancilla >> index) & 1 for index in spec.value)
    valids = tuple((ancilla >> index) & 1 for index in spec.valid)
    pointer = (ancilla >> spec.pointer) & 1
    close = (ancilla >> spec.close) & 1
    if not (
        contact == bit
        and abs(amplitude - 1) < TOL
        and pointer == 0
        and close == 1
        and all(valids)
        and values == (bit,) * depth
        and c283.archive_consistent(ancilla, spec)
    ):
        raise ValueError((bit, depth, output))
    raw = (depth, spec.bits, ancilla, *valids, *values)
    return values[0], raw


def archive_event_word(
    outcomes: tuple[str | None, ...], depth: int
) -> tuple[tuple[str | None, ...], tuple[tuple[int, ...] | None, ...]]:
    decoded = []
    raw = []
    for outcome in outcomes:
        if outcome is None:
            decoded.append(None)
            raw.append(None)
            continue
        archived = tuple(redundant_binary_archive(int(bit), depth) for bit in outcome)
        decoded.append("".join(str(value) for value, _word in archived))
        raw.append(tuple(item for _value, word in archived for item in word))
    return tuple(decoded), tuple(raw)


def contact_input_controls() -> None:
    coefficients = c278.walsh_coefficients()
    recovered = tuple(
        sum(
            coefficient * (-1 if (mask & occupation).bit_count() % 2 else 1)
            for mask, coefficient in enumerate(coefficients)
        )
        for occupation in range(64)
    )
    expected = tuple(Fraction(c278.contact_active(index), 1) for index in range(64))
    mapped_occupations = (0b000000, 0b000001, 0b000011, 0b000101)
    restricted = tuple(int(recovered[index]) for index in mapped_occupations)
    check(
        "the finite process restricts the exact Cycle-278 contact effect to a coarse/fine four-state subspace",
        recovered == expected
        and restricted == (0, 0, 1, 1)
        and sum(recovered) == 57,
        {
            "mapped_occupations": mapped_occupations,
            "restricted_Q": restricted,
            "rank_full_Q": sum(recovered),
        },
    )
    cycle283 = c283.history_measure(Fraction(57, 64), 5)
    check(
        "Cycle-283 finite archive cylinders are the repeatable coarse-history input",
        cycle283
        == {
            (0, 0, 0, 0, 0): Fraction(7, 64),
            (1, 1, 1, 1, 1): Fraction(57, 64),
        },
        cycle283,
    )


def operation_cp_and_containment_controls() -> None:
    rows = []
    failures = []
    for operation in OPERATIONS:
        total_effect = np.zeros((4, 4), dtype=complex)
        branch_minimum = 1.0
        for _outcome, kraus in operation.branches:
            branch_choi = choi(kraus)
            branch_minimum = min(
                branch_minimum, float(np.min(np.linalg.eigvalsh(branch_choi)).real)
            )
            for operator in kraus:
                total_effect += operator.conj().T @ operator
        row = {
            "operation": operation.name,
            "branches": len(operation.branches),
            "minimum_Choi_eigenvalue": branch_minimum,
            "normalization_residual": float(np.linalg.norm(total_effect - I4)),
        }
        rows.append(row)
        if branch_minimum < -TOL or row["normalization_residual"] > TOL:
            failures.append(row)
    check(
        "every event-map branch is completely positive and every operation family is trace preserving",
        not failures,
        rows,
    )
    check(
        "fine/coarse forgetting is exact event coarse-graining",
        all(
            np.linalg.norm(
                sum(
                    (
                        apply_kraus(density, kraus)
                        for _outcome, kraus in OPERATION_BY_NAME[selective].branches
                    ),
                    np.zeros_like(density),
                )
                - apply_kraus(
                    density, OPERATION_BY_NAME[forgotten].branches[0][1]
                )
            )
            < TOL
            for density in PREPARATIONS.values()
            for selective, forgotten in (("Cs", "Cf"), ("Fs", "Ff"))
        ),
    )


def domain_composition_and_decoder_controls() -> dict[int, dict[str, object]]:
    summaries = {}
    maximum_decoder_residual = 0.0
    minimum_density_eigenvalue = 1.0
    minimum_terminal_weight = 1.0
    maximum_protocol_error = 0.0
    fibre_failures = 0
    distinct_raw_fibre_cases = 0
    for depth in TRAINING_DEPTHS + (HELD_DEPTH,):
        leaves = enumerate_domain(depth)
        protocol_weights: dict[tuple, float] = {}
        positive = 0
        for leaf in leaves:
            key = (leaf.preparation, leaf.schedule)
            protocol_weights[key] = protocol_weights.get(key, 0.0) + leaf.weight
            replayed = replay(leaf.preparation, leaf.schedule, leaf.outcomes)
            maximum_decoder_residual = max(
                maximum_decoder_residual, float(np.linalg.norm(replayed - leaf.density))
            )
            if leaf.weight < 1e-14:
                continue
            positive += 1
            state = leaf.density / leaf.weight
            minimum_density_eigenvalue = min(
                minimum_density_eigenvalue,
                float(np.min(np.linalg.eigvalsh((state + state.conj().T) / 2)).real),
            )
            # Tomographically complete future repertoire.  Run the actual
            # Cycle-283 redundant archive at depths 1 and 5, canonicalize its
            # raw valid/value words, and require both microhistories to decode
            # to the same complete packet and therefore state.
            base_fingerprint = fingerprint(leaf.density)
            raw_fibre_words = []
            for archive_depth in (1, 5):
                decoded_outcomes, raw_words = archive_event_word(
                    leaf.outcomes, archive_depth
                )
                if decoded_outcomes != leaf.outcomes:
                    fibre_failures += 1
                decoded = replay(leaf.preparation, leaf.schedule, decoded_outcomes)
                if fingerprint(decoded) != base_fingerprint:
                    fibre_failures += 1
                raw_fibre_words.append(raw_words)
            if any(outcome is not None for outcome in leaf.outcomes):
                if raw_fibre_words[0] == raw_fibre_words[1]:
                    fibre_failures += 1
                else:
                    distinct_raw_fibre_cases += 1
            for tester in TESTERS.values():
                effects = ((I4 + tester) / 2, (I4 - tester) / 2)
                terminal = tuple(float(np.trace(effect @ leaf.density).real) for effect in effects)
                minimum_terminal_weight = min(minimum_terminal_weight, *terminal)
                if abs(sum(terminal) - leaf.weight) > TOL:
                    fibre_failures += 1
        maximum_protocol_error = max(
            maximum_protocol_error,
            max(abs(weight - 1) for weight in protocol_weights.values()),
        )
        summaries[depth] = {
            "leaves": len(leaves),
            "expected_leaves": len(PREPARATIONS) * 9**depth,
            "positive_leaves": positive,
            "protocols": len(protocol_weights),
            "expected_protocols": len(PREPARATIONS) * 5**depth,
        }
    check(
        "finite protocol/event domain has a normalized positive composition functional through held-out depth 4",
        all(
            row["leaves"] == row["expected_leaves"]
            and row["protocols"] == row["expected_protocols"]
            for row in summaries.values()
        )
        and maximum_protocol_error < TOL
        and minimum_density_eigenvalue > -TOL
        and minimum_terminal_weight > -TOL,
        {
            "summaries": summaries,
            "maximum_protocol_normalization_error": maximum_protocol_error,
            "minimum_state_eigenvalue": minimum_density_eigenvalue,
            "minimum_terminal_weight": minimum_terminal_weight,
        },
    )
    check(
        "complete candidate Record packets replay exactly and satisfy Pauli-complete record-fibre future-equivalence",
        maximum_decoder_residual < TOL and fibre_failures == 0,
        {
            "maximum_decoder_residual": maximum_decoder_residual,
            "archive_microhistory_depths": (1, 5),
            "fibre_failures": fibre_failures,
            "distinct_raw_fibre_cases": distinct_raw_fibre_cases,
            "future_testers": len(TESTERS),
        },
    )
    return summaries


def identity_containment_controls() -> float:
    leaves = enumerate_domain(3)
    maximum = 0.0
    tests = 0
    for leaf in leaves:
        for position in range(4):
            schedule = leaf.schedule[:position] + ("I",) + leaf.schedule[position:]
            outcomes = leaf.outcomes[:position] + (None,) + leaf.outcomes[position:]
            inserted = replay(leaf.preparation, schedule, outcomes)
            maximum = max(maximum, float(np.linalg.norm(inserted - leaf.density)))
            tests += 1
    check(
        "identity containment holds at every insertion position in the complete training-depth-3 domain",
        maximum < TOL,
        {"tests": tests, "maximum_residual": maximum},
    )
    return maximum


def coarse_fine_and_deletion_controls() -> dict[str, float]:
    yes_fine = PREPARATIONS["yes_fine_plus"]
    coarse = apply_kraus(yes_fine, (Q1,))
    fine_forgotten = apply_kraus(yes_fine, R)
    coarse_state = normalized_state(coarse)
    fine_state = normalized_state(fine_forgotten)
    assert coarse_state is not None and fine_state is not None
    coarse_fine_trace = trace_distance(coarse_state, fine_state)
    coarse_fine_fro = float(np.linalg.norm(coarse_state - fine_state))
    fine_x = TESTERS["IX"]
    future_gap = abs(
        float(np.trace(fine_x @ coarse_state).real)
        - float(np.trace(fine_x @ fine_state).real)
    )
    check(
        "same visible coarse-YES archive can hide distinct coarse and fine post-instrument states",
        abs(coarse_fine_trace - 0.5) < TOL
        and abs(coarse_fine_fro - 1 / np.sqrt(2)) < TOL
        and abs(future_gap - 1) < TOL,
        (coarse_fine_trace, coarse_fine_fro, future_gap),
    )

    # Removing status merges identity with coarse-forgotten and coarse with
    # fine-forgotten.  Removing the fine outcome merges |10> and |11>.
    cross = PREPARATIONS["cross_plus"]
    identity_state = cross
    coarse_forgotten = apply_kraus(cross, (Q0, Q1))
    status_deletion = trace_distance(identity_state, coarse_forgotten)
    fine_outcome_deletion = trace_distance(R[2], R[3])
    prep_deletion = trace_distance(
        PREPARATIONS["cross_plus"], PREPARATIONS["generic_phase"]
    )
    check(
        "decoder clause deletions destroy record-fibre sufficiency with exact future witnesses",
        status_deletion > 0.49
        and coarse_fine_trace > 0.49
        and abs(fine_outcome_deletion - 1) < TOL
        and prep_deletion > 0.5,
        {
            "identity_vs_coarse_forgotten": status_deletion,
            "coarse_vs_fine_forgotten": coarse_fine_trace,
            "fine_outcome_10_vs_11": fine_outcome_deletion,
            "preparation_record_deletion": prep_deletion,
        },
    )

    # Whole omission is identity and decodes correctly.  A split fault that
    # omits the physical coupling but leaves a syntactically valid outcome-0
    # packet makes the decoder predict Q0 conditioning while the data stayed
    # coherent.
    whole_deleted_actual = cross
    whole_deleted_decoded = replay("cross_plus", ("I",), (None,))
    false_packet = replay("cross_plus", ("Cs",), ("0",))
    false_state = normalized_state(false_packet)
    assert false_state is not None
    split_residual = trace_distance(whole_deleted_actual, false_state)
    check(
        "whole deletion is identity-contained but Cycle-279/283 split false-close spoofs the candidate decoder",
        np.linalg.norm(whole_deleted_actual - whole_deleted_decoded) < TOL
        and abs(split_residual - 1 / np.sqrt(2)) < TOL,
        split_residual,
    )
    return {
        "coarse_fine_trace_distance": coarse_fine_trace,
        "coarse_fine_frobenius": coarse_fine_fro,
        "future_IX_gap": future_gap,
        "split_decoder_trace_distance": split_residual,
    }


def actuality_and_boundary_controls() -> dict[str, object]:
    leaves = [
        leaf
        for leaf in enumerate_domain(1)
        if leaf.preparation == "cross_plus" and leaf.schedule == ("Cs",)
    ]
    weights = {
        leaf.outcomes[0]: Fraction(leaf.weight).limit_denominator()
        for leaf in leaves
    }
    annotations = tuple(outcome for outcome, weight in weights.items() if weight > 0)
    check(
        "one normalized process law admits two distinct actual-member annotations without selecting either",
        weights == {"0": Fraction(1, 2), "1": Fraction(1, 2)}
        and annotations == ("0", "1"),
        (weights, annotations),
    )
    text = normalized(NOTE)
    check(
        "boundary, lawful Record typing, actuality, Born, and clock inventories remain explicit",
        "lawful record typing is supplied" in text
        and "boundary inventory" in text
        and "actuality inventory" in text
        and "no born-frequency" in text
        and "no actual member is selected" in text
        and "no clock-rate" in text,
    )
    return {
        "actual_member_candidates": annotations,
        "selection_rule": None,
        "typed_Record_decoder": "supplied candidate",
    }


def lawful_domain_controls() -> None:
    rejected = 0
    for depth in (-1,):
        try:
            enumerate_domain(depth)
        except ValueError:
            rejected += 1
    try:
        replay("cross_plus", ("Fs",), ("bad",))
    except ValueError:
        rejected += 1
    check("lawful protocol domain rejects negative depth and malformed outcomes", rejected == 2, rejected)


def main() -> int:
    note_contract()
    contact_input_controls()
    operation_cp_and_containment_controls()
    summaries = domain_composition_and_decoder_controls()
    containment = identity_containment_controls()
    distinctions = coarse_fine_and_deletion_controls()
    inventory = actuality_and_boundary_controls()
    lawful_domain_controls()
    check(
        "finite process/history success creates no route-independent obstruction or axiom pressure",
        summaries[HELD_DEPTH]["leaves"] == len(PREPARATIONS) * 9**HELD_DEPTH
        and containment < TOL
        and distinctions["coarse_fine_trace_distance"] > 0
        and inventory["selection_rule"] is None
        and "no route-independent obstruction" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
    )
    print("DATA held_summary", summaries[HELD_DEPTH])
    print("DATA distinctions", distinctions)
    print("DATA actuality", inventory)
    print("SUMMARY", "PASS", PASS, "FAIL", FAIL)
    if FAIL:
        print("RESULT CYCLE284_CONTACT_ARCHIVE_FINITE_PROCESS_HISTORY_RED")
        return 1
    print("RESULT CYCLE284_CONTACT_ARCHIVE_FINITE_PROCESS_HISTORY_GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
