#!/usr/bin/env python3
"""Cycle 189: a preterminal quantum context/process construction.

The finite model has two system qubits and a two-bit pointer.  A preparation
record is followed by one of six Peres--Mermin context interventions, then by
pointer and terminal records.  All weights are calculated from explicitly
priced matrices and a supplied trace pairing.

This is an authority-free exact process probe.  It does not derive the
imported quantum law from the framework, amend an axiom, select actuality, or
claim a local nearest-neighbour implementation.
"""

from __future__ import annotations

import hashlib
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PRETERMINAL_CONTEXT_QUANTUM_PROCESS_CYCLE189_NOTE_2026-07-16.md"
)
CYCLE181 = (
    ROOT
    / "scripts/operational_context_process_seam_cycle181_2026_07_16.py"
)
CYCLE181_NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "OPERATIONAL_CONTEXT_PROCESS_SEAM_CYCLE181_NOTE_2026-07-16.md"
)
FROZEN = {
    CYCLE181: "1431fe5cbbb2f45b17d151b7ed48b5432ca22103dc9e4a26211ae40755bdcb47",
    CYCLE181_NOTE: "606662f96ceae06c13ba413145ccbf389285404dea2dcc4fe1912614beec1ccd",
}

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


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tensor(*matrices: sp.Matrix) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for matrix in matrices:
        result = sp.kronecker_product(result, matrix)
    return sp.Matrix(result)


def exact_trace(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(matrix))


def exact_zero(matrix: sp.Matrix) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


def density(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.H)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
I4 = sp.eye(4)
I16 = sp.eye(16)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = sp.Matrix([1, 1]) / sp.sqrt(2)
KET00 = tensor(KET0, KET0)
KET_PLUS_PLUS = tensor(KET_PLUS, KET_PLUS)
POINTER_BLANK = KET00

PAULI_ONE = {
    "I": I2,
    "X": X,
    "Y": Y,
    "Z": Z,
}
OBSERVABLES = {
    "ZI": tensor(Z, I2),
    "IZ": tensor(I2, Z),
    "ZZ": tensor(Z, Z),
    "IX": tensor(I2, X),
    "XI": tensor(X, I2),
    "XX": tensor(X, X),
    "ZX": tensor(Z, X),
    "XZ": tensor(X, Z),
    "YY": tensor(Y, Y),
}


@dataclass(frozen=True)
class Context:
    label: str
    observables: tuple[str, str, str]
    product_sign: int


CONTEXTS = (
    Context("R1", ("ZI", "IZ", "ZZ"), 1),
    Context("R2", ("IX", "XI", "XX"), 1),
    Context("R3", ("ZX", "XZ", "YY"), 1),
    Context("C1", ("ZI", "IX", "ZX"), 1),
    Context("C2", ("IZ", "XI", "XZ"), 1),
    Context("C3", ("ZZ", "XX", "YY"), -1),
)
CONTEXT_BY_LABEL = {context.label: context for context in CONTEXTS}

PREPARATION_UNITARIES = {
    "prep:Z0Z0": I4,
    "prep:X+X+": tensor(H, H),
}
PREPARATION_VECTORS = {
    label: sp.simplify(unitary * KET00)
    for label, unitary in PREPARATION_UNITARIES.items()
}
PREPARATIONS = {
    label: density(vector)
    for label, vector in PREPARATION_VECTORS.items()
}
DIRECT_PREPARATION_VECTORS = {
    "prep:Z0Z0": KET00,
    "prep:X+X+": KET_PLUS_PLUS,
}

PAULI_TESTS = {
    left + right: tensor(PAULI_ONE[left], PAULI_ONE[right])
    for left, right in product(("I", "X", "Y", "Z"), repeat=2)
    if left + right != "II"
}
PAULI_BASIS = {
    left + right: tensor(PAULI_ONE[left], PAULI_ONE[right])
    for left, right in product(("I", "X", "Y", "Z"), repeat=2)
}


def effect(observable: sp.Matrix, outcome: int) -> sp.Matrix:
    return sp.simplify((I4 + outcome * observable) / 2)


@lru_cache(maxsize=None)
def context_projectors(
    label: str,
) -> tuple[tuple[tuple[int, int, int], sp.Matrix], ...]:
    context = CONTEXT_BY_LABEL[label]
    branches = []
    for outcomes in product((-1, 1), repeat=3):
        projector = I4
        for name, outcome in zip(context.observables, outcomes, strict=True):
            projector = sp.simplify(
                projector * effect(OBSERVABLES[name], outcome)
            )
        if not exact_zero(projector):
            branches.append((outcomes, sp.simplify(projector)))
    return tuple(branches)


def pointer_word(outcomes: tuple[int, int, int]) -> tuple[int, int]:
    return int(outcomes[0] == -1), int(outcomes[1] == -1)


def pointer_shift(word: tuple[int, int]) -> sp.Matrix:
    return tensor(
        X if word[0] else I2,
        X if word[1] else I2,
    )


@lru_cache(maxsize=None)
def context_dilation(label: str) -> sp.Matrix:
    unitary = sp.zeros(16)
    for outcomes, projector in context_projectors(label):
        unitary += tensor(projector, pointer_shift(pointer_word(outcomes)))
    return sp.simplify(unitary)


def pointer_kraus(
    unitary: sp.Matrix,
    word: tuple[int, int],
) -> sp.Matrix:
    pointer_index = 2 * word[0] + word[1]
    kraus = sp.zeros(4)
    for system_out in range(4):
        for system_in in range(4):
            kraus[system_out, system_in] = unitary[
                4 * system_out + pointer_index,
                4 * system_in,
            ]
    return sp.simplify(kraus)


def branch_weight(
    preparation: str,
    context: str,
    outcomes: tuple[int, int, int],
) -> sp.Expr:
    projector = dict(context_projectors(context))[outcomes]
    return sp.simplify(exact_trace(projector * PREPARATIONS[preparation]))


def branch_state(
    preparation: str,
    context: str,
    outcomes: tuple[int, int, int],
) -> sp.Matrix:
    projector = dict(context_projectors(context))[outcomes]
    return sp.simplify(
        projector * PREPARATIONS[preparation] * projector
    )


def normalized_branch_state(
    preparation: str,
    context: str,
    outcomes: tuple[int, int, int],
) -> sp.Matrix:
    branch = branch_state(preparation, context, outcomes)
    weight = exact_trace(branch)
    if weight == 0:
        raise ValueError(("zero-branch", preparation, context, outcomes))
    return sp.simplify(branch / weight)


def nonselective_state(preparation: str, context: str) -> sp.Matrix:
    return sp.simplify(
        sum(
            (
                projector
                * PREPARATIONS[preparation]
                * projector
                for _outcomes, projector in context_projectors(context)
            ),
            sp.zeros(4),
        )
    )


def tester_distribution(
    state: sp.Matrix,
    tester: str,
) -> tuple[sp.Expr, sp.Expr]:
    observable = PAULI_TESTS[tester]
    plus = sp.simplify(exact_trace(effect(observable, 1) * state))
    minus = sp.simplify(exact_trace(effect(observable, -1) * state))
    return plus, minus


def joint_process_weight(
    preparation: str,
    context: str,
    context_outcomes: tuple[int, int, int],
    tester: str,
    terminal_outcome: int,
) -> sp.Expr:
    return sp.simplify(
        exact_trace(
            effect(PAULI_TESTS[tester], terminal_outcome)
            * branch_state(preparation, context, context_outcomes)
        )
    )


def context_outcome_distribution(
    preparation: str,
    context: str,
) -> dict[tuple[int, int, int], sp.Expr]:
    return {
        outcomes: branch_weight(preparation, context, outcomes)
        for outcomes, _projector in context_projectors(context)
    }


def interference_matrix(
    preparation: str,
    context: str,
    tester: str,
    terminal_outcome: int,
) -> sp.Matrix:
    rho = PREPARATIONS[preparation]
    final_effect = effect(PAULI_TESTS[tester], terminal_outcome)
    projectors = tuple(
        projector for _outcomes, projector in context_projectors(context)
    )
    return sp.Matrix(
        [
            [
                sp.simplify(
                    exact_trace(
                        final_effect
                        * left
                        * rho
                        * right
                    )
                )
                for right in projectors
            ]
            for left in projectors
        ]
    )


def partial_trace_pointer(joint: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        [
            [
                sp.simplify(
                    sum(
                        joint[4 * left + pointer, 4 * right + pointer]
                        for pointer in range(4)
                    )
                )
                for right in range(4)
            ]
            for left in range(4)
        ]
    )


def dilated_nonselective_state(
    preparation: str,
    context: str,
) -> sp.Matrix:
    joint_input = tensor(
        PREPARATIONS[preparation],
        density(POINTER_BLANK),
    )
    unitary = context_dilation(context)
    return sp.simplify(
        partial_trace_pointer(unitary * joint_input * unitary.H)
    )


@dataclass(frozen=True)
class ProtocolRecord:
    stage: int
    kind: str
    content: object
    parents: tuple[tuple[str, object], ...]


def selective_protocol_records(
    preparation: str,
    context: str,
    context_outcomes: tuple[int, int, int],
    tester: str,
    terminal_outcome: int,
) -> tuple[ProtocolRecord, ...]:
    return (
        ProtocolRecord(0, "blank-boundary", "system:00|pointer:00", ()),
        ProtocolRecord(
            1,
            "preparation",
            preparation,
            (("blank-boundary", "system:00|pointer:00"),),
        ),
        ProtocolRecord(
            2,
            "context-choice",
            context,
            (("preparation", preparation),),
        ),
        ProtocolRecord(
            3,
            "pointer-record",
            (context, context_outcomes),
            (("context-choice", context),),
        ),
        ProtocolRecord(
            4,
            "terminal-tester",
            tester,
            (("pointer-record", (context, context_outcomes)),),
        ),
        ProtocolRecord(
            5,
            "terminal-record",
            (tester, terminal_outcome),
            (
                ("pointer-record", (context, context_outcomes)),
                ("terminal-tester", tester),
            ),
        ),
    )


def pauli_fingerprint(state: sp.Matrix) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(exact_trace(observable * state))
        for observable in PAULI_TESTS.values()
    )


def reconstruct_from_pauli_fingerprint(
    fingerprint: tuple[sp.Expr, ...],
) -> sp.Matrix:
    coefficients = {"II": sp.Integer(1)}
    coefficients.update(dict(zip(PAULI_TESTS, fingerprint, strict=True)))
    return sp.simplify(
        sum(
            (
                coefficients[label] * observable / 4
                for label, observable in PAULI_BASIS.items()
            ),
            sp.zeros(4),
        )
    )


def sequential_selective_state(
    preparation: str,
    context: str,
    outcomes: tuple[int, int, int],
    order: tuple[int, int, int],
) -> sp.Matrix:
    current = PREPARATIONS[preparation]
    context_spec = CONTEXT_BY_LABEL[context]
    for index in order:
        local_effect = effect(
            OBSERVABLES[context_spec.observables[index]],
            outcomes[index],
        )
        current = sp.simplify(local_effect * current * local_effect)
    weight = exact_trace(current)
    if weight == 0:
        raise ValueError(("zero-sequential-branch", preparation, context, outcomes, order))
    return sp.simplify(current / weight)


def sequential_nonselective_state(
    preparation: str,
    context: str,
    order: tuple[int, int, int],
) -> sp.Matrix:
    current = PREPARATIONS[preparation]
    context_spec = CONTEXT_BY_LABEL[context]
    for index in order:
        observable = OBSERVABLES[context_spec.observables[index]]
        current = sp.simplify(
            effect(observable, 1) * current * effect(observable, 1)
            + effect(observable, -1) * current * effect(observable, -1)
        )
    return current


def record_fibre_controls() -> tuple[dict[str, object], tuple[object, ...]]:
    complete: dict[object, set[tuple[sp.Expr, ...]]] = defaultdict(set)
    context_blind: dict[object, set[tuple[sp.Expr, ...]]] = defaultdict(set)
    prep_blind: dict[object, set[tuple[sp.Expr, ...]]] = defaultdict(set)
    instrument_blind: dict[object, set[tuple[sp.Expr, ...]]] = defaultdict(set)
    failures = []
    raw_histories = 0

    # Two exact preparation implementations are deliberately retained as raw
    # micro-history labels: direct vector supply and the priced unitary route.
    for preparation in PREPARATIONS:
        microstates = {
            "direct": density(DIRECT_PREPARATION_VECTORS[preparation]),
            "unitary": PREPARATIONS[preparation],
        }
        for micro_label, microstate in microstates.items():
            if not exact_zero(microstate - PREPARATIONS[preparation]):
                failures.append(("prep-microstate", preparation, micro_label))
            fingerprint = pauli_fingerprint(microstate)
            complete[("identity", preparation)].add(fingerprint)
            prep_blind[("identity",)].add(fingerprint)
            instrument_blind[("current", preparation)].add(fingerprint)
            raw_histories += 1

        for context in CONTEXT_BY_LABEL:
            for order in permutations(range(3)):
                forgotten = sequential_nonselective_state(
                    preparation,
                    context,
                    order,
                )
                fingerprint = pauli_fingerprint(forgotten)
                complete[("forgotten", preparation, context)].add(fingerprint)
                instrument_blind[("current", preparation)].add(fingerprint)
                raw_histories += 1

            for outcomes, _projector in context_projectors(context):
                if branch_weight(preparation, context, outcomes) == 0:
                    continue
                for order in permutations(range(3)):
                    state = sequential_selective_state(
                        preparation,
                        context,
                        outcomes,
                        order,
                    )
                    fingerprint = pauli_fingerprint(state)
                    complete[
                        ("selective", preparation, context, outcomes)
                    ].add(fingerprint)
                    context_blind[
                        ("selective", preparation, outcomes)
                    ].add(fingerprint)
                    raw_histories += 1

    for fibre, fingerprints in complete.items():
        if len(fingerprints) != 1:
            failures.append(("complete-fibre", fibre, len(fingerprints)))
        for fingerprint in fingerprints:
            reconstructed = reconstruct_from_pauli_fingerprint(fingerprint)
            # Match against any one state carrying this exact fingerprint.
            if pauli_fingerprint(reconstructed) != fingerprint:
                failures.append(("tomography", fibre))

    return (
        {
            "raw_histories": raw_histories,
            "complete_fibres": len(complete),
            "complete_max": max(map(len, complete.values())),
            "context_blind_max": max(map(len, context_blind.values())),
            "prep_blind_max": max(map(len, prep_blind.values())),
            "instrument_blind_max": max(map(len, instrument_blind.values())),
        },
        tuple(failures[:10]),
    )


def shared_observable_assignment_census() -> Counter[int]:
    labels = tuple(OBSERVABLES)
    histogram: Counter[int] = Counter()
    for values in product((-1, 1), repeat=len(labels)):
        assignment = dict(zip(labels, values, strict=True))
        satisfied = sum(
            assignment[first]
            * assignment[second]
            * assignment[third]
            == context.product_sign
            for context in CONTEXTS
            for first, second, third in (context.observables,)
        )
        histogram[satisfied] += 1
    return histogram


def repeated_observable_marginals(
    preparation: str,
) -> tuple[dict[tuple[str, str], tuple[sp.Expr, sp.Expr]], tuple[object, ...]]:
    occurrences: dict[str, list[str]] = defaultdict(list)
    for context in CONTEXTS:
        for observable in context.observables:
            occurrences[observable].append(context.label)
    marginals = {}
    failures = []
    for observable, context_labels in occurrences.items():
        if len(context_labels) != 2:
            failures.append(("occurrence-count", observable, context_labels))
            continue
        compared = []
        for context_label in context_labels:
            context = CONTEXT_BY_LABEL[context_label]
            index = context.observables.index(observable)
            distribution = context_outcome_distribution(preparation, context_label)
            compared.append(
                tuple(
                    sp.simplify(
                        sum(
                            weight
                            for outcomes, weight in distribution.items()
                            if outcomes[index] == outcome
                        )
                    )
                    for outcome in (-1, 1)
                )
            )
        marginals[(observable, preparation)] = compared[0]
        if compared[0] != compared[1]:
            failures.append(
                ("marginal-context-dependence", observable, compared)
            )
    return marginals, tuple(failures)


def context_indexed_lookup_control(
    preparation: str,
) -> tuple[bool, object]:
    branch_spaces = [
        tuple(context_outcome_distribution(preparation, context.label).items())
        for context in CONTEXTS
    ]
    total = sp.Integer(0)
    marginals: list[dict[tuple[int, int, int], sp.Expr]] = [
        defaultdict(lambda: sp.Integer(0))
        for _context in CONTEXTS
    ]
    support = 0
    for selected in product(*branch_spaces):
        outcomes = tuple(item[0] for item in selected)
        weight = sp.simplify(sp.prod(item[1] for item in selected))
        total += weight
        if weight != 0:
            support += 1
        for index, local_outcomes in enumerate(outcomes):
            marginals[index][local_outcomes] += weight
    failures = []
    for index, context in enumerate(CONTEXTS):
        wanted = context_outcome_distribution(preparation, context.label)
        observed = {
            outcomes: sp.simplify(weight)
            for outcomes, weight in marginals[index].items()
        }
        if observed != wanted:
            failures.append((context.label, observed, wanted))
    return (
        sp.simplify(total - 1) == 0 and not failures,
        {
            "support": support,
            "total": sp.simplify(total),
            "failures": failures[:3],
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    print("FROZEN SEAM")
    observed_hashes = {path: sha256(path) for path in FROZEN}
    check(
        "Cycle 181 runner and note remain frozen",
        observed_hashes == FROZEN,
        {path.name: digest for path, digest in observed_hashes.items()},
    )

    print("\nIMPORTED ALGEBRA AND PREPARATION INTERFACE")
    check(
        "single-qubit I, X, Y, Z and H have their exact involution/unitary forms",
        I2 == sp.eye(2)
        and X * X == Y * Y == Z * Z == I2
        and H.H * H == I2,
        "",
    )
    check(
        "the two priced preparation unitaries are exact and map the blank correctly",
        all(unitary.H * unitary == I4 for unitary in PREPARATION_UNITARIES.values())
        and all(
            exact_zero(
                PREPARATION_VECTORS[label]
                - DIRECT_PREPARATION_VECTORS[label]
            )
            for label in PREPARATIONS
        )
        and all(exact_trace(rho) == 1 for rho in PREPARATIONS.values()),
        tuple(PREPARATIONS),
    )

    print("\nSIX CONTEXT INSTRUMENTS AND POINTER DILATIONS")
    context_failures = []
    pointer_checks = 0
    for context in CONTEXTS:
        matrices = tuple(OBSERVABLES[name] for name in context.observables)
        if any(matrix.H != matrix or matrix * matrix != I4 for matrix in matrices):
            context_failures.append(("observable", context.label))
        if any(
            not exact_zero(left * right - right * left)
            for left, right in (
                (matrices[0], matrices[1]),
                (matrices[0], matrices[2]),
                (matrices[1], matrices[2]),
            )
        ):
            context_failures.append(("commutation", context.label))
        if not exact_zero(
            matrices[0] * matrices[1] * matrices[2]
            - context.product_sign * I4
        ):
            context_failures.append(("product", context.label))
        branches = context_projectors(context.label)
        if (
            len(branches) != 4
            or any(projector.rank() != 1 for _outcomes, projector in branches)
            or any(exact_trace(projector) != 1 for _outcomes, projector in branches)
            or not exact_zero(
                sum((projector for _outcomes, projector in branches), sp.zeros(4))
                - I4
            )
            or any(
                sp.prod(outcomes) != context.product_sign
                for outcomes, _projector in branches
            )
        ):
            context_failures.append(("projectors", context.label))
        unitary = context_dilation(context.label)
        if (
            unitary.H != unitary
            or unitary * unitary != I16
            or unitary.H * unitary != I16
        ):
            context_failures.append(("dilation", context.label))
        for outcomes, projector in branches:
            pointer_checks += 1
            if not exact_zero(
                pointer_kraus(unitary, pointer_word(outcomes)) - projector
            ):
                context_failures.append(
                    ("pointer-kraus", context.label, outcomes)
                )
    occurrence_counts = Counter(
        observable
        for context in CONTEXTS
        for observable in context.observables
    )
    check(
        "six commuting Peres-Mermin contexts close with exact signed products",
        not context_failures
        and occurrence_counts == Counter({name: 2 for name in OBSERVABLES}),
        {
            "failures": context_failures[:5],
            "occurrences": occurrence_counts,
        },
    )
    check(
        "each context has a unitary two-bit pointer dilation with exact Lüders Kraus blocks",
        not context_failures and pointer_checks == 24,
        {"pointer_blocks": pointer_checks, "failures": context_failures[:5]},
    )

    print("\nNORMALIZED MULTI-TIME PROCESS")
    process_failures = []
    process_tables = 0
    process_entries = 0
    for preparation in PREPARATIONS:
        for context in CONTEXT_BY_LABEL:
            for tester in PAULI_TESTS:
                weights = []
                for outcomes, _projector in context_projectors(context):
                    for terminal_outcome in (-1, 1):
                        weight = joint_process_weight(
                            preparation,
                            context,
                            outcomes,
                            tester,
                            terminal_outcome,
                        )
                        weights.append(weight)
                        process_entries += 1
                        if weight.is_nonnegative is not True:
                            process_failures.append(
                                (
                                    "negative",
                                    preparation,
                                    context,
                                    outcomes,
                                    tester,
                                    terminal_outcome,
                                    weight,
                                )
                            )
                process_tables += 1
                if sp.simplify(sum(weights) - 1) != 0:
                    process_failures.append(
                        ("normalization", preparation, context, tester, sum(weights))
                    )
    check(
        "the explicit preparation-context-pointer-terminal process normalizes exactly",
        not process_failures
        and process_tables == 2 * 6 * 15
        and process_entries == 2 * 6 * 15 * 4 * 2,
        {
            "tables": process_tables,
            "entries": process_entries,
            "failures": process_failures[:5],
        },
    )
    dilation_failures = []
    for preparation in PREPARATIONS:
        for context in CONTEXT_BY_LABEL:
            if not exact_zero(
                dilated_nonselective_state(preparation, context)
                - nonselective_state(preparation, context)
            ):
                dilation_failures.append((preparation, context))
    check(
        "tracing the physical pointer gives the exact nonselective instrument",
        not dilation_failures,
        dilation_failures,
    )

    print("\nPRETERMINAL CONTEXT ANCESTRY")
    record_failures = []
    record_count = 0
    for preparation in PREPARATIONS:
        for context in CONTEXT_BY_LABEL:
            distribution = context_outcome_distribution(preparation, context)
            for outcomes, weight in distribution.items():
                if weight == 0:
                    continue
                for terminal_outcome in (-1, 1):
                    records = selective_protocol_records(
                        preparation,
                        context,
                        outcomes,
                        "XX",
                        terminal_outcome,
                    )
                    record_count += 1
                    stages = {record.kind: record.stage for record in records}
                    if not (
                        stages["preparation"]
                        < stages["context-choice"]
                        < stages["pointer-record"]
                        < stages["terminal-record"]
                    ):
                        record_failures.append(
                            (preparation, context, outcomes, stages)
                        )
    check(
        "context choice and physical pointer records precede every terminal record",
        not record_failures and record_count > 0,
        {"records": record_count, "failures": record_failures[:5]},
    )
    omitted_xx = tester_distribution(PREPARATIONS["prep:X+X+"], "XX")
    r1_xx = tester_distribution(
        nonselective_state("prep:X+X+", "R1"),
        "XX",
    )
    r2_xx = tester_distribution(
        nonselective_state("prep:X+X+", "R2"),
        "XX",
    )
    check(
        "the earlier context intervention changes the later terminal law",
        omitted_xx == (1, 0)
        and r1_xx == (sp.Rational(1, 2), sp.Rational(1, 2))
        and r2_xx == (1, 0),
        {"omitted": omitted_xx, "R1": r1_xx, "R2": r2_xx},
    )

    print("\nIDENTITY CONTAINMENT AND MEASURE-AND-FORGET")
    identity_failures = []
    for preparation in PREPARATIONS:
        for tester in PAULI_TESTS:
            omitted = tester_distribution(PREPARATIONS[preparation], tester)
            identity = tester_distribution(
                I4 * PREPARATIONS[preparation] * I4,
                tester,
            )
            if omitted != identity or sp.simplify(sum(omitted) - 1) != 0:
                identity_failures.append((preparation, tester, omitted, identity))
    check(
        "omitted slot is exactly identity insertion for every preparation and tester",
        not identity_failures,
        identity_failures[:5],
    )
    branch_sum = tuple(
        sp.simplify(
            sum(
                joint_process_weight(
                    "prep:X+X+",
                    "R1",
                    outcomes,
                    "XX",
                    terminal_outcome,
                )
                for outcomes, _projector in context_projectors("R1")
            )
        )
        for terminal_outcome in (1, -1)
    )
    check(
        "summing real R1 pointer outcomes gives measure-and-forget, not omission",
        branch_sum
        == r1_xx
        == (sp.Rational(1, 2), sp.Rational(1, 2))
        and branch_sum != omitted_xx,
        {
            "identity": omitted_xx,
            "measure-and-forget": branch_sum,
        },
    )
    check(
        "a real intervention may also be nondisturbing on the selected preparation",
        r2_xx == omitted_xx,
        {"identity": omitted_xx, "R2": r2_xx},
    )

    print("\nINTERFERENCE CONTROL")
    decoherence = interference_matrix(
        "prep:X+X+",
        "R1",
        "XX",
        1,
    )
    diagonal = sp.simplify(sum(decoherence[index, index] for index in range(4)))
    total = sp.simplify(sum(decoherence))
    off_diagonal = sp.simplify(total - diagonal)
    check(
        "the omitted coherent process has a strongly-positive exact history matrix",
        decoherence.H == decoherence
        and decoherence.eigenvals()
        == {sp.Rational(1, 4): 2, sp.Integer(0): 2}
        and total == 1,
        {"matrix": decoherence, "eigenvalues": decoherence.eigenvals()},
    )
    check(
        "R1 measure-and-forget removes an exact one-half interference contribution",
        diagonal == sp.Rational(1, 2)
        and off_diagonal == sp.Rational(1, 2)
        and r1_xx[0] == diagonal
        and omitted_xx[0] == total,
        {
            "coherent": total,
            "recorded-diagonal": diagonal,
            "interference": off_diagonal,
        },
    )

    print("\nSHARED-ANSWER LATE-LOOKUP CONTROL")
    wrong_parity_failures = []
    for preparation in PREPARATIONS:
        for context in CONTEXTS:
            wrong_weight = sp.Integer(0)
            for outcomes in product((-1, 1), repeat=3):
                if sp.prod(outcomes) == context.product_sign:
                    continue
                projector = I4
                for name, outcome in zip(
                    context.observables,
                    outcomes,
                    strict=True,
                ):
                    projector = sp.simplify(
                        projector * effect(OBSERVABLES[name], outcome)
                    )
                wrong_weight += exact_trace(
                    projector * PREPARATIONS[preparation]
                )
            if sp.simplify(wrong_weight) != 0:
                wrong_parity_failures.append(
                    (preparation, context.label, wrong_weight)
                )
    histogram = shared_observable_assignment_census()
    check(
        "every physical context gives zero weight to the wrong parity sector",
        not wrong_parity_failures,
        wrong_parity_failures,
    )
    check(
        "no context-independent shared-observable answer table satisfies all six sectors",
        histogram == Counter({1: 96, 3: 320, 5: 96})
        and histogram[6] == 0,
        histogram,
    )
    marginal_failures = []
    marginal_accounting = {}
    for preparation in PREPARATIONS:
        marginals, failures = repeated_observable_marginals(preparation)
        marginal_accounting[preparation] = len(marginals)
        marginal_failures.extend(failures)
    check(
        "each repeated observable has the same immediate marginal in both contexts",
        not marginal_failures
        and marginal_accounting
        == {preparation: 9 for preparation in PREPARATIONS},
        {
            "accounting": marginal_accounting,
            "failures": marginal_failures[:5],
        },
    )
    lookup_ok, lookup_detail = context_indexed_lookup_control("prep:X+X+")
    check(
        "dropping shared identity permits a context-indexed precomputed comparator",
        lookup_ok,
        lookup_detail,
    )

    print("\nRECORD-FIBRE SUFFICIENCY")
    fibre_accounting, fibre_failures = record_fibre_controls()
    check(
        "complete preparation/context/instrument/outcome records are Pauli-lumpable",
        not fibre_failures
        and fibre_accounting["complete_max"] == 1,
        (fibre_accounting, fibre_failures),
    )
    check(
        "dropping preparation, context, or instrument identity breaks future sufficiency",
        fibre_accounting["context_blind_max"] > 1
        and fibre_accounting["prep_blind_max"] > 1
        and fibre_accounting["instrument_blind_max"] > 1,
        fibre_accounting,
    )

    print("\nIMPORT AND SCOPE FIREWALL")
    note_text = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    normalized = " ".join(note_text.lower().split())
    required_phrases = (
        "two system qubits and a two-bit pointer",
        "the context intervention occurs before the terminal record",
        "identity containment",
        "measure-and-forget",
        "normalized multi-time law",
        "explicit preparation interface",
        "record-fibre future-equivalence",
        "shared-observable late-lookup model",
        "context-indexed lookup remains live",
        "born trace pairing is imported",
        "the preparation boundary is imported",
        "the context instrument family is imported",
        "the relative y phase and c3 sign are imported",
        "actuality and frequency remain open",
        "no axiom conclusion follows",
        "no-go-discipline status: pass for the narrow claim",
        "## n1",
        "## n2",
        "## n3",
        "## n4",
        "## n5",
        "## n6",
        "## n7",
        "## n8",
    )
    missing = tuple(
        phrase for phrase in required_phrases
        if phrase not in normalized
    )
    check(
        "the Cycle-189 note prices every atom and preserves the no-go scope",
        not missing,
        missing,
    )

    print("\nACCOUNTING")
    print("PREPARATIONS", tuple(PREPARATIONS))
    print("CONTEXTS", tuple(CONTEXT_BY_LABEL))
    print("POINTER_BLOCKS", pointer_checks)
    print("PROCESS_TABLES", process_tables, "ENTRIES", process_entries)
    print(
        "XX_CONTEXT",
        {"omitted": omitted_xx, "R1": r1_xx, "R2": r2_xx},
    )
    print(
        "INTERFERENCE",
        {"total": total, "diagonal": diagonal, "off_diagonal": off_diagonal},
    )
    print("SHARED_ASSIGNMENT_HISTOGRAM", histogram)
    print("CONTEXT_INDEXED_LOOKUP", lookup_detail)
    print("FIBRES", fibre_accounting)
    print("PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE189_PRETERMINAL_QUANTUM_PROCESS_GREEN"
        if FAIL == 0
        else "CYCLE189_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
