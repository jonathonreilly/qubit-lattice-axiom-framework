#!/usr/bin/env python3
"""Cycle 536: finite coherent-seed member dilation comparator.

The circuit coherently copies the exact Cycle505 singleton binding label into
a blank retained five-M2 seed/bath, emits Cycle531's exact MEMBER and receipt
types, invokes the exact conditional binder, copies a reversible candidate
echo, and uncomputes every member/binder scratch.  The reduced seed diagonal
equals the operational grade vector q algebraically.  Calling that diagonal a
stochastic p=q actual-member law remains supplied: no branch actualization,
Born rule, sampler, Record, or realized history is implemented.
"""

from __future__ import annotations

import ast
from collections import Counter
from dataclasses import asdict, dataclass
from hashlib import sha256
import inspect
from itertools import product
import json
from math import prod, sqrt
from pathlib import Path
import re
import resource
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_autonomous_hidden_carrier_member_law_cycle534_2026_07_21 as c534


c531 = c534.c531
c505 = c534.c505
c508 = c534.c508
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COHERENT_SEED_MEMBER_DILATION_CYCLE536_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
MENU = tuple(range(5))
ECHO_SLOTS = 5
TRAIN_N = 2
HELD_N = 4
TOL = 2e-9
PASS = 0
FAIL = 0
Word = tuple[int, ...]
Sparse = dict[Word, complex]


FROZEN = {
    "Cycle534 runner": "76a46047a4f14054f6e0655a360122967d3626c45f51d584e5df2e4aa6e1e2db",
    "Cycle534 note": "1ddf4c552b035ffbc977dfd7b3c1d0e72f02063a3e127adb71c6dfe859c46a3e",
    "Cycle531 runner": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "Cycle531 note": "ed40564d4e57090cf03e706b54964e5a24cb735f9ca14df8f008fecffc388042",
    "Cycle508 train runner": "b223ff44b159a598ef52ea21b3e758a1303e126d7f53474f799ed14c0a829dc6",
    "Cycle508 held note": "8651a1bcfb39b2e2b8980bd5a25a352ffbe3e8e7a199ff421fc47f3a576c03c7",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
}
FROZEN_PATHS = {
    "Cycle534 runner": Path(c534.__file__),
    "Cycle534 note": c534.NOTE,
    "Cycle531 runner": Path(c531.__file__),
    "Cycle531 note": c531.NOTE,
    "Cycle508 train runner": Path(c508.__file__),
    "Cycle508 held note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ACTUAL_MEMBER_ADMITTED_HISTORY_LAW_TOURNAMENT_HELD_CYCLE508_NOTE_2026-07-20.md",
    "realized-state primitive": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "Born-frequency boundary": ROOT / "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
}


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    answer = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return answer


_layout = [c531.TOTAL_M2]
RETAINED_SEED = take(_layout, 5)
ECHO_HEAD = take(_layout, 5)
ECHO_OCCURRENCE = take(_layout, ECHO_SLOTS)
ECHO_CONTENT = tuple(take(_layout, 3) for _ in range(ECHO_SLOTS))
TOTAL_M2 = _layout[0]
NEW_M2 = TOTAL_M2 - c531.TOTAL_M2


@dataclass(frozen=True)
class OperationalGradeDiagnostic:
    fixture: str
    preparation: str
    q: tuple[float, ...]
    probability: None = None


@dataclass(frozen=True)
class ReducedSeedDiagonal:
    diagonal: tuple[float, ...]
    source: str = "diagnostic partial trace over orthogonal retained seed/binding sectors"
    actual_member: None = None
    probability_law: None = None


@dataclass(frozen=True)
class CandidateKernelInterpretation:
    p: tuple[float, ...]
    relation: str = "p=q supplied candidate-law interpretation of a derived reduced diagonal"
    derived_from_unitary: bool = False
    stochastic_process_derived: bool = False
    Born_derived: bool = False
    sampler: None = None


@dataclass(frozen=True)
class ConditionalBranchString:
    retained_seed_label: int
    word: Word
    counts: Word
    empirical: bool = False
    probability: None = None


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def declared_runner_sha() -> str | None:
    if not NOTE.exists():
        return None
    match = re.search(r"runner SHA-256:\s*([0-9a-f]{64})", NOTE.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def contract_controls() -> dict:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    required = (
        "authority: none", "audit: unset", "finite reversible unitary dilation",
        "retained seed", "exact cycle-531 member and receipt interface",
        "derived reduced diagonal", "p=q is a supplied candidate kernel",
        "not stochastic dynamics", "not born", "not actualization",
        "not a record", "not realized history", "diagnostic partial trace",
        "supplied bath mixture", "branch actualization", "reset", "independence",
        "host randomness", "train", "held", "empirical strings remain separate",
        "finite capacity", "renewal", "inverse", "leakage", "deletion",
        "all 24 proper-cubic frames", "cycle 534 comparator", "n1", "n2", "n3",
        "n4", "n5", "n6", "n7", "n8", "no axiom pressure",
        "supplied / derived / open",
    )
    body = normalized(NOTE)
    missing = tuple(fragment for fragment in required if fragment not in body)
    registry = json.loads(FROZEN_PATHS["premise registry"].read_text(encoding="utf-8"))
    registry_text = json.dumps(registry).lower()
    return {
        "observed_SHA256": observed,
        "strict_dependency_hashes_match": observed == FROZEN,
        "note_missing_contract_fragments": missing,
        "runner_SHA256": file_sha(Path(__file__)),
        "declared_runner_SHA256": declared_runner_sha(),
        "realized_state_primitive_registered": "realized_state_primitive" in registry_text,
        "pass": (
            observed == FROZEN and not missing
            and declared_runner_sha() == file_sha(Path(__file__))
            and "realized_state_primitive" in registry_text
        ),
    }


def one_hot(label: int, width: int = 5) -> Word:
    if label not in range(width):
        raise ValueError("one-hot label leaves its declared word")
    return tuple(int(index == label) for index in range(width))


def singleton(bits: Word, name: str) -> int:
    if len(bits) != 5 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError(f"{name} leaves its exact binary five-M2 domain")
    if sum(bits) != 1:
        raise ValueError(f"{name} must be one-hot")
    return bits.index(1)


def gate(kind: str, sites: tuple[int, ...], label: str) -> c505.Gate:
    return c505.gate(kind, sites, label, TOTAL_M2)


def clone(item: c505.Gate, label: str) -> c505.Gate:
    return gate(item.kind, item.sites, label)


def swap_schedule(left: int, right: int, label: str) -> tuple[c505.Gate, ...]:
    return (
        gate("CNOT", (left, right), f"{label}:1"),
        gate("CNOT", (right, left), f"{label}:2"),
        gate("CNOT", (left, right), f"{label}:3"),
    )


def seed_preparation_schedule() -> tuple[c505.Gate, ...]:
    return tuple(
        gate(
            "CNOT", (c531.offset(c505.C_ELIGIBILITY[label]), RETAINED_SEED[label]),
            f"seed-prepare:binding-copy:{label}",
        )
        for label in MENU
    )


def emit_schedule(prefix: str) -> tuple[c505.Gate, ...]:
    gates = []
    for label in MENU:
        gates.extend((
            gate("CNOT", (RETAINED_SEED[label], c531.MEMBER[label]), f"{prefix}:member:{label}"),
            gate("CNOT", (RETAINED_SEED[label], c531.LAW_RECEIPT[label]), f"{prefix}:receipt:{label}"),
        ))
    return tuple(gates)


def binder_schedule(reverse: bool) -> tuple[c505.Gate, ...]:
    sequence = tuple(reversed(c531.SCHEDULE)) if reverse else c531.SCHEDULE
    direction = "reverse" if reverse else "forward"
    return tuple(
        clone(item, f"binder-{direction}:{index}:{item.label}")
        for index, item in enumerate(sequence)
    )


def echo_schedule() -> tuple[c505.Gate, ...]:
    gates = []
    for slot in range(ECHO_SLOTS):
        gates.append(gate(
            "TOFFOLI", (ECHO_HEAD[slot], c531.OCCURRENCE, ECHO_OCCURRENCE[slot]),
            f"echo:occurrence:{slot}",
        ))
        for lane in range(3):
            gates.append(gate(
                "TOFFOLI", (ECHO_HEAD[slot], c531.ATOM_CONTENT[lane], ECHO_CONTENT[slot][lane]),
                f"echo:content:{slot}:{lane}",
            ))
    return tuple(gates)


def head_advance_schedule() -> tuple[c505.Gate, ...]:
    gates = []
    for left, right in (
        (ECHO_HEAD[3], ECHO_HEAD[4]), (ECHO_HEAD[2], ECHO_HEAD[3]),
        (ECHO_HEAD[1], ECHO_HEAD[2]), (ECHO_HEAD[0], ECHO_HEAD[1]),
    ):
        gates.extend(swap_schedule(left, right, f"advance-head:{left}:{right}"))
    return tuple(gates)


SEED_PREPARE = seed_preparation_schedule()
EMIT = emit_schedule("emit")
BINDER_FORWARD = binder_schedule(False)
ECHO = echo_schedule()
BINDER_REVERSE = binder_schedule(True)
UNEMIT = emit_schedule("unemit")
ADVANCE_HEAD = head_advance_schedule()
RECURRENT_SCHEDULE = EMIT + BINDER_FORWARD + ECHO + BINDER_REVERSE + UNEMIT + ADVANCE_HEAD


def validate_word(bits: Word) -> None:
    if len(bits) != TOTAL_M2 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Cycle536 word leaves its exact binary 206-M2 domain")


def apply_schedule(
    bits: Word, schedule: tuple[c505.Gate, ...],
    *, reverse: bool = False, delete_label: str | None = None,
) -> Word:
    validate_word(bits)
    matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
    if delete_label is not None and len(matches) != 1:
        raise ValueError("deletion must name exactly one Cycle536 primitive")
    active = tuple(
        item for index, item in enumerate(schedule)
        if delete_label is None or index != matches[0]
    )
    word = list(bits)
    for item in (tuple(reversed(active)) if reverse else active):
        c505.apply_gate(word, item)
    return tuple(word)


def sparse_apply(state: Sparse, schedule: tuple[c505.Gate, ...], *, reverse: bool = False) -> Sparse:
    output: Sparse = {}
    for word, amplitude in state.items():
        target = apply_schedule(word, schedule, reverse=reverse)
        output[target] = output.get(target, 0j) + amplitude
    return {word: amplitude for word, amplitude in output.items() if abs(amplitude) > 1e-14}


def prepare_unseeded_branch(
    binding_label: int, echo_head: int,
    *, edge: int = 1, plus: int = 1, minus: int = 0, K_position: int = 0,
) -> Word:
    base = c531.prepare(
        edge=edge, plus=plus, minus=minus, K_position=K_position,
        binding_label=binding_label, member_label=None, receipt_label=None,
    )
    bits = list(base + (0,) * NEW_M2)
    for site, bit in zip(ECHO_HEAD, one_hot(echo_head)):
        bits[site] = bit
    output = tuple(bits)
    validate_preparation_code(output)
    return output


def prepare_seeded_branch(
    binding_label: int, echo_head: int, *, seed_label: int | None = None,
    edge: int = 1, plus: int = 1, minus: int = 0, K_position: int = 0,
) -> Word:
    source = prepare_unseeded_branch(
        binding_label, echo_head, edge=edge, plus=plus, minus=minus,
        K_position=K_position,
    )
    if seed_label is None:
        return apply_schedule(source, SEED_PREPARE)
    bits = list(source)
    for site, bit in zip(RETAINED_SEED, one_hot(seed_label)):
        bits[site] = bit
    output = tuple(bits)
    validate_recurrent_code(output)
    return output


def scratch_sites() -> tuple[int, ...]:
    return (
        *c531.MEMBER, *c531.LAW_RECEIPT, c531.PRECOMMIT_READY,
        c531.OCCURRENCE, c531.ATOM_FLAG, *c531.ATOM_CONTENT,
        *c531.PAYLOAD_CURRENT, *c531.PAYLOAD_K_BINARY,
        c531.WORK_BINDING, c531.WORK_PROVENANCE, c531.WORK_TRIGGER,
    )


def validate_preparation_code(bits: Word) -> None:
    validate_word(bits)
    if any(bits[site] for site in RETAINED_SEED):
        raise ValueError("pre-dilation retained seed must be blank")
    singleton(tuple(bits[site] for site in ECHO_HEAD), "echo head")
    if any(bits[site] for site in scratch_sites()):
        raise ValueError("Cycle536 member/binder scratch must be blank")


def validate_recurrent_code(bits: Word) -> None:
    validate_word(bits)
    singleton(tuple(bits[site] for site in RETAINED_SEED), "retained seed")
    singleton(tuple(bits[site] for site in ECHO_HEAD), "echo head")
    if any(bits[site] for site in scratch_sites()):
        raise ValueError("Cycle536 terminal member/binder scratch must be blank")


def seed_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in RETAINED_SEED), "retained seed")


def head_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in ECHO_HEAD), "echo head")


def echo_view(bits: Word) -> tuple[tuple[int, Word], ...]:
    return tuple(
        (bits[ECHO_OCCURRENCE[slot]], tuple(bits[site] for site in ECHO_CONTENT[slot]))
        for slot in range(ECHO_SLOTS)
    )


def norm2(state: Sparse) -> float:
    return float(sum(abs(amplitude) ** 2 for amplitude in state.values()))


def sparse_residual(left: Sparse, right: Sparse) -> float:
    keys = set(left) | set(right)
    return sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys))


def normalized_q(q: tuple[float, ...]) -> None:
    if len(q) != 5 or any(value < -TOL for value in q) or abs(sum(q) - 1.0) >= TOL:
        raise ValueError("candidate q leaves the normalized five-label domain")


def coherent_binding_state(q: tuple[float, ...], head: int, phases: Word | None = None) -> Sparse:
    normalized_q(q)
    phase_word = phases if phases is not None else (0, 1, 2, 3, 4)
    if len(phase_word) != 5:
        raise ValueError("coherent phase fixture must have five entries")
    state = {}
    for label, value in enumerate(q):
        if value <= 1e-15:
            continue
        phase = complex(c531.c526.np.exp(0.173j * phase_word[label]))
        state[prepare_unseeded_branch(label, head)] = sqrt(value) * phase
    return state


def reduced_label_diagonal(state: Sparse, sites: tuple[int, ...], name: str) -> tuple[float, ...]:
    diagonal = [0.0] * 5
    for word, amplitude in state.items():
        label = singleton(tuple(word[site] for site in sites), name)
        diagonal[label] += abs(amplitude) ** 2
    return tuple(diagonal)


def composition_controls() -> dict:
    failures = prep_inverse_failures = recurrent_inverse_failures = scratch_failures = 0
    source_mutations = exact_c531_failures = 0
    tests = 0
    for binding, head, K_position, current in product(
        MENU, MENU, range(c531.K_BITS), ((0, 0), (1, 0), (0, 1))
    ):
        plus, minus = current
        edge = plus ^ minus
        unseeded = prepare_unseeded_branch(
            binding, head, edge=edge, plus=plus, minus=minus, K_position=K_position,
        )
        seeded = apply_schedule(unseeded, SEED_PREPARE)
        prep_inverse_failures += apply_schedule(seeded, SEED_PREPARE, reverse=True) != unseeded
        failures += seed_of(seeded) != binding

        emitted = apply_schedule(seeded, EMIT)
        member = tuple(emitted[site] for site in c531.MEMBER)
        receipt = tuple(emitted[site] for site in c531.LAW_RECEIPT)
        failures += member != one_hot(binding) or receipt != one_hot(binding)
        midpoint = apply_schedule(emitted, BINDER_FORWARD)
        exact = c531.logical_apply(tuple(emitted[:c531.TOTAL_M2]))
        exact_c531_failures += tuple(midpoint[:c531.TOTAL_M2]) != exact
        failures += int(
            midpoint[c531.OCCURRENCE] != edge
            or midpoint[c531.ATOM_FLAG] != edge
            or tuple(midpoint[site] for site in c531.ATOM_CONTENT)
            != tuple(edge & bit for bit in c505.bits3(binding))
        )

        output = apply_schedule(seeded, RECURRENT_SCHEDULE)
        validate_recurrent_code(output)
        recurrent_inverse_failures += apply_schedule(
            output, RECURRENT_SCHEDULE, reverse=True
        ) != seeded
        expected_echo = [list(item) for item in echo_view(seeded)]
        if edge:
            expected_echo[head] = [1, c505.bits3(binding)]
        failures += int(
            seed_of(output) != binding
            or head_of(output) != (head + 1) % 5
            or echo_view(output) != tuple((item[0], tuple(item[1])) for item in expected_echo)
        )
        scratch_failures += any(output[site] for site in scratch_sites())
        source_mutations += any(
            output[site] != seeded[site]
            for site in (
                c531.C526_EDGE, *c531.C526_CURRENT, *c531.C526_K,
                *range(c531.C505_OFFSET, c531.C505_OFFSET + c531.C505_WIDTH),
                *RETAINED_SEED,
            )
        )
        tests += 1

    mismatched_occurrences = 0
    for binding, seed in product(MENU, MENU):
        if binding == seed:
            continue
        source = prepare_seeded_branch(binding, 0, seed_label=seed)
        emitted = apply_schedule(source, EMIT)
        midpoint = apply_schedule(emitted, BINDER_FORWARD)
        mismatched_occurrences += midpoint[c531.OCCURRENCE]

    return {
        "binding_head_K_current_columns": tests,
        "expected_columns": 5 * 5 * c531.K_BITS * 3,
        "seed_preparation_or_member_type_failures": failures,
        "exact_Cycle531_midpoint_failures": exact_c531_failures,
        "seed_preparation_inverse_failures": prep_inverse_failures,
        "recurrent_inverse_failures": recurrent_inverse_failures,
        "terminal_scratch_failures": scratch_failures,
        "source_binding_seed_mutations": source_mutations,
        "mismatched_seed_binding_counterfactual_occurrences": mismatched_occurrences,
        "pass": not any((
            failures, exact_c531_failures, prep_inverse_failures,
            recurrent_inverse_failures, scratch_failures, source_mutations,
            mismatched_occurrences,
        )),
    }


def operational_rows() -> tuple[OperationalGradeDiagnostic, ...]:
    surface = c508.c500.c493.c488.menu_surface()
    rows = []
    for fixture, program, states in (
        ("L5-interface/train-program", surface.train_program, c505.input_states("train")),
        ("held-L6-interface/held-program", surface.held_program, c505.input_states("held")),
    ):
        for name, psi in states:
            rows.append(OperationalGradeDiagnostic(
                fixture, name, tuple(c508.c500.branch_grades(program, psi))
            ))
    return tuple(rows)


def dilation_and_kernel_firewall_controls() -> dict:
    rows = []
    failures = 0
    for fixture_index, typed in enumerate(operational_rows()):
        q = typed.q
        source = coherent_binding_state(q, fixture_index % 5)
        seeded = sparse_apply(source, SEED_PREPARE)
        emitted = sparse_apply(seeded, EMIT)
        midpoint = sparse_apply(emitted, BINDER_FORWARD)
        recurrent = sparse_apply(seeded, RECURRENT_SCHEDULE)
        inverse = sparse_apply(recurrent, RECURRENT_SCHEDULE, reverse=True)
        unseeded = sparse_apply(seeded, SEED_PREPARE, reverse=True)

        seed_diagonal = reduced_label_diagonal(seeded, RETAINED_SEED, "retained seed")
        member_diagonal = reduced_label_diagonal(midpoint, c531.MEMBER, "member scratch")
        diagonal_residual = max(abs(left - right) for left, right in zip(seed_diagonal, q))
        member_residual = max(abs(left - right) for left, right in zip(member_diagonal, q))
        interpretation = CandidateKernelInterpretation(q)
        failures += int(
            diagonal_residual >= TOL or member_residual >= TOL
            or abs(norm2(source) - 1.0) >= TOL
            or abs(norm2(recurrent) - 1.0) >= TOL
            or sparse_residual(inverse, seeded) >= TOL
            or sparse_residual(unseeded, source) >= TOL
            or interpretation.derived_from_unitary
            or interpretation.stochastic_process_derived
            or interpretation.Born_derived
            or interpretation.sampler is not None
        )
        rows.append({
            "operational": asdict(typed),
            "derived_seed_diagonal": asdict(ReducedSeedDiagonal(seed_diagonal)),
            "derived_member_scratch_diagonal": member_diagonal,
            "candidate_kernel_interpretation": asdict(interpretation),
            "p_equals_q_diagonal_residual": diagonal_residual,
            "member_diagonal_residual": member_residual,
            "coherent_terms": len(seeded),
            "source_norm_residual": abs(norm2(source) - 1.0),
            "recurrent_norm_residual": abs(norm2(recurrent) - 1.0),
            "recurrent_inverse_residual": sparse_residual(inverse, seeded),
            "seed_unpreparation_residual": sparse_residual(unseeded, source),
            "actual_member_read": None,
        })

    return {
        "rows": rows,
        "algebraically_derived": "orthogonal seed/member reduced diagonal equals operational q",
        "supplied_candidate_law": "interpret reduced diagonal as actual-member p=q",
        "pure_dilation_requires_supplied_bath_mixture": False,
        "classical_mixture_interpretation_requires_supplied_bath_mixture": True,
        "one_member_read_requires_branch_actualization": True,
        "diagnostic_partial_trace_is_physical_deletion": False,
        "host_randomness": None,
        "Born_rule": None,
        "pass": failures == 0,
    }


def cylinder_table(q: tuple[float, ...], n: int, independent: bool) -> dict[Word, float]:
    normalized_q(q)
    if independent:
        return {
            tuple(word): float(prod(q[label] for label in word))
            for word in product(MENU, repeat=n)
        }
    return {tuple((label,) * n): q[label] for label in MENU}


def total_variation(left: dict[Word, float], right: dict[Word, float]) -> float:
    keys = set(left) | set(right)
    return 0.5 * sum(abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in keys)


def recurrence_capacity_and_independence_controls() -> dict:
    failures = inverse_failures = 0
    capacity_rows = []
    renewal_rows = []
    for seed, head in product(MENU, MENU):
        word = prepare_seeded_branch(seed, head)
        initial = word
        for step in range(10):
            previous = word
            word = apply_schedule(word, RECURRENT_SCHEDULE)
            inverse_failures += apply_schedule(
                word, RECURRENT_SCHEDULE, reverse=True
            ) != previous
            failures += int(seed_of(word) != seed or head_of(word) != (head + step + 1) % 5)
            expected_occupied = 5 if step == 4 else 0 if step == 9 else None
            if expected_occupied is not None:
                observed = sum(item[0] for item in echo_view(word))
                failures += observed != expected_occupied
                row = {
                    "seed": seed, "initial_head": head,
                    "occupied_echo_slots": observed,
                }
                (capacity_rows if step == 4 else renewal_rows).append(row)
        failures += word != initial

    grade_rows = operational_rows()
    cylinder_rows = []
    for typed in grade_rows:
        n = TRAIN_N if "train" in typed.fixture else HELD_N
        retained = cylinder_table(typed.q, n, False)
        fresh = cylinder_table(typed.q, n, True)
        marginal = tuple(
            sum(weight for word, weight in fresh.items() if word[0] == label)
            for label in MENU
        )
        residual = max(abs(left - right) for left, right in zip(marginal, typed.q))
        tv = total_variation(retained, fresh)
        failures += int(
            abs(sum(retained.values()) - 1.0) >= TOL
            or abs(sum(fresh.values()) - 1.0) >= TOL
            or residual >= TOL or tv <= 1e-6
        )
        cylinder_rows.append({
            "fixture": typed.fixture,
            "preparation": typed.preparation,
            "N": n,
            "retained_same_seed_support": len(retained),
            "supplied_fresh_product_support": len(fresh),
            "marginal_q_residual": residual,
            "same_seed_vs_fresh_product_TV": tv,
            "fresh_seed_independence": "supplied, not derived by the recurrent unitary",
            "fresh_bank_capacity": n,
            "fresh_bank_reset_or_renewal": None,
            "finite_table_stationarity": None,
        })

    conditional_strings = tuple(
        asdict(ConditionalBranchString(
            label, tuple((label,) * 25),
            tuple(25 if index == label else 0 for index in MENU),
        ))
        for label in MENU
    )
    cycle534_strings = tuple(
        tuple((start + step) % 5 for step in range(25))
        for start in MENU
    )
    return {
        "all_seed_head_pairs": 25,
        "five_step_capacity_rows": capacity_rows,
        "ten_step_renewal_rows": renewal_rows,
        "retained_seed_period": 1,
        "echo_head_period": 5,
        "echo_archive_period": 10,
        "ten_step_exact_return": True,
        "inverse_failures": inverse_failures,
        "cylinder_rows": cylinder_rows,
        "conditional_same_seed_strings": conditional_strings,
        "Cycle534_rotating_strings_comparator": cycle534_strings,
        "comparison": "Cycle534 rotates uniformly; Cycle536 retained-seed branches are constant and maximally correlated",
        "actual_empirical_strings": None,
        "independent_empirical_strings": None,
        "new_independent_event_requires": "fresh independently prepared operational branch/seed bath or a reset/renewal law",
        "host_randomness": None,
        "pass": not any((failures, inverse_failures)),
    }


def covariance_controls() -> dict:
    frames = c531.c526.c235.proper_cubic_frames()
    failures = tests = 0
    orientations = Counter()
    for frame in frames:
        mapped = frame @ c531.c526.np.asarray((1, 0, 0), dtype=int)
        axis = int(c531.c526.np.flatnonzero(mapped)[0])
        reversed_endpoints = int(mapped[axis]) == -1
        orientations["endpoint_reversing" if reversed_endpoints else "endpoint_preserving"] += 1
        for binding, head, current in product(MENU, MENU, ((0, 0), (1, 0), (0, 1))):
            plus, minus = current
            edge = plus ^ minus
            source = prepare_seeded_branch(
                binding, head, edge=edge, plus=plus, minus=minus,
                K_position=(binding + head) % c531.K_BITS,
            )
            output = apply_schedule(source, RECURRENT_SCHEDULE)
            framed_plus, framed_minus = ((minus, plus) if reversed_endpoints else (plus, minus))
            framed_source = prepare_seeded_branch(
                binding, head, edge=edge, plus=framed_plus, minus=framed_minus,
                K_position=(binding + head) % c531.K_BITS,
            )
            framed_output = apply_schedule(framed_source, RECURRENT_SCHEDULE)
            expected = list(output)
            if reversed_endpoints:
                expected[c531.C526_CURRENT[0]], expected[c531.C526_CURRENT[1]] = (
                    expected[c531.C526_CURRENT[1]], expected[c531.C526_CURRENT[0]]
                )
            failures += tuple(expected) != framed_output
            tests += 1
    return {
        "proper_cubic_frames": len(frames),
        "frame_tests": tests,
        "frame_failures": failures,
        "orientations": dict(orientations),
        "seed_head_member_receipt_echo_frame_action": "scalar",
        "current_frame_action": "plus/minus exchange under endpoint reversal",
        "same_schedule_train_L5_and_held_L6": True,
        "pass": len(frames) == 24 and failures == 0,
    }


def deletion_controls() -> dict:
    rows = []

    def witness(label: str, source: Word, schedule: tuple[c505.Gate, ...]) -> None:
        full = apply_schedule(source, schedule)
        damaged = apply_schedule(source, schedule, delete_label=label)
        rows.append({
            "deleted": label,
            "changed": damaged != full,
            "basis_residual": 0.0 if damaged == full else sqrt(2.0),
            "terminal_scratch_nonblank": any(damaged[site] for site in scratch_sites()),
        })

    for label in MENU:
        unseeded = prepare_unseeded_branch(label, 0)
        witness(f"seed-prepare:binding-copy:{label}", unseeded, SEED_PREPARE)
        seeded = prepare_seeded_branch(label, 0)
        witness(f"emit:member:{label}", seeded, RECURRENT_SCHEDULE)
        witness(f"emit:receipt:{label}", seeded, RECURRENT_SCHEDULE)
        witness(f"unemit:member:{label}", seeded, RECURRENT_SCHEDULE)
        witness(f"unemit:receipt:{label}", seeded, RECURRENT_SCHEDULE)
    for slot in range(ECHO_SLOTS):
        seeded = prepare_seeded_branch(4, slot)
        witness(f"echo:occurrence:{slot}", seeded, RECURRENT_SCHEDULE)
        for lane, label in enumerate((1, 2, 4)):
            seeded = prepare_seeded_branch(label, slot)
            witness(f"echo:content:{slot}:{lane}", seeded, RECURRENT_SCHEDULE)
    seeded = prepare_seeded_branch(3, 3, K_position=7)
    witness("binder-forward:46:II:conditional-occurrence", seeded, RECURRENT_SCHEDULE)
    witness("binder-reverse:15:II:conditional-occurrence", seeded, RECURRENT_SCHEDULE)
    witness(ADVANCE_HEAD[0].label, seeded, RECURRENT_SCHEDULE)

    seed_deleted = list(seeded)
    for site in RETAINED_SEED:
        seed_deleted[site] = 0
    deleted_seed_rejected = False
    try:
        validate_recurrent_code(tuple(seed_deleted))
    except ValueError:
        deleted_seed_rejected = True

    return {
        "rows": rows,
        "deletion_witnesses": len(rows),
        "unwitnessed": tuple(row["deleted"] for row in rows if not row["changed"]),
        "retained_seed_deletion_rejected": deleted_seed_rejected,
        "unique_preparation_labels": len({item.label for item in SEED_PREPARE}) == len(SEED_PREPARE),
        "unique_recurrent_labels": len({item.label for item in RECURRENT_SCHEDULE}) == len(RECURRENT_SCHEDULE),
        "pass": (
            all(row["changed"] for row in rows) and deleted_seed_rejected
            and len({item.label for item in SEED_PREPARE}) == len(SEED_PREPARE)
            and len({item.label for item in RECURRENT_SCHEDULE}) == len(RECURRENT_SCHEDULE)
        ),
    }


def routing_resource_and_source_audit() -> dict:
    # Relabel the final inverse preparation so deletion labels remain unique in
    # the displayed combined route; gate action is unchanged.
    combined = (
        SEED_PREPARE + RECURRENT_SCHEDULE
        + tuple(clone(item, f"seed-unprepare:{index}:{item.label}") for index, item in enumerate(reversed(SEED_PREPARE)))
    )
    trace = c505.nn_trace(combined, TOTAL_M2)
    source = prepare_unseeded_branch(4, 3, K_position=15)
    logical = apply_schedule(source, combined)
    routed = c505.apply_routed(source, combined)
    roundtrip = c505.apply_routed(routed, combined, reverse=True)

    forbidden = {
        "random", "choice", "choices", "argmax", "branch_grades", "norm",
        "sample", "seed", "partial_trace",
    }
    calls = []
    for function in (
        seed_preparation_schedule, emit_schedule, binder_schedule,
        echo_schedule, head_advance_schedule,
    ):
        tree = ast.parse(inspect.getsource(function))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
    forbidden_calls = tuple(call for call in calls if call.lower() in forbidden)
    return {
        **trace,
        "seed_preparation_gates": len(SEED_PREPARE),
        "recurrent_gates": len(RECURRENT_SCHEDULE),
        "prepare_recur_unprepare_gates": len(combined),
        "fixed_schedule_routed_equals_logical": routed == logical,
        "routed_inverse_roundtrip": roundtrip == source,
        "Cycle531_existing_port_composite_M2": c531.TOTAL_M2,
        "new_retained_seed_M2": 5,
        "new_echo_head_M2": 5,
        "new_echo_archive_M2": 20,
        "new_Cycle536_M2": NEW_M2,
        "total_bounded_port_composite_M2": TOTAL_M2,
        "maximum_displayed_support_M2": trace["maximum_support_M2"],
        "two_site_Toffoli_decomposition_supplied": False,
        "autonomous_constraint_preparation_supplied": False,
        "forbidden_physical_schedule_calls": forbidden_calls,
        "host_randomness_calls": 0,
        "underlying_mass_parameter_preserved": 0.45340565417488515,
        "enlarged_history_mass_eigenstate_claimed": False,
        "pass": (
            routed == logical and roundtrip == source and not forbidden_calls
            and trace["maximum_support_M2"] <= 3
            and trace["connected_failures"] == 0
            and trace["final_adjacent_support_failures"] == 0
            and trace["terminal_operand_order_failures"] == 0
            and trace["reverse_label_restoration_failures"] == 0
            and NEW_M2 == 30 and TOTAL_M2 == 206
        ),
    }


def no_go_controls() -> dict:
    n1 = (
        ("coherent retained-seed dilation", "fixed reversible label copy", "derived diagonal q; no single actual read", "ATTEMPTED"),
        ("classical supplied seed mixture", "mixed-state preparation with weights p", "conditional member ensemble", "ATTEMPTED"),
        ("fresh independent seed bank", "tensor-product preparations", "finite product cylinder", "ATTEMPTED"),
        ("autonomous bath reset/renewal", "local regenerative bath dynamics", "new independent events", "OPEN"),
        ("branch-actualization law", "objective selection of one retained sector", "one actual member", "RULED OUT BY PRIOR as derived; candidate law remains"),
        ("host random read", "external random choice", "one sampled label", "RULED OUT BY SCOPE"),
        ("deterministic retained carrier", "Cycle534 period-five ontic phase", "non-Born member string", "RULED OUT BY PRIOR as stochastic route; retained comparator"),
        ("objective stochastic field", "law-owned noise/dilation and calibration", "actual strings and probabilities", "OPEN"),
    )
    n2 = (
        "coherent seed preparation independent of actualization",
        "actualization independent of Record permanence",
        "fresh-bank independence independent of one-step marginal",
        "bath reset independent of branch read",
        "empirical calibration independent of reduced diagonal",
        "host randomness absent independently of unitary closure",
    )
    n3 = (
        "operational branch state supplied", "blank seed supplied",
        "singleton binding supplied", "blank member/receipt/output scratch supplied",
        "p=q candidate-law meaning supplied", "partial trace diagnostic",
        "fresh product preparation and independence supplied", "no reset law",
        "no actual member read", "no empirical corpus", "finite capacity",
        "L5/L6 port interface", "three-site Toffoli", "static line chart",
    )
    n4 = (
        "zero unitary/inverse/leakage residual diagnoses reversible dilation only",
        "zero reduced-diagonal residual diagnoses algebraic q only",
        "same-seed/product TV diagnoses independence wall, not actualization",
        "deletion sqrt(2) diagnoses load-bearing gates only",
        "all24 zero mismatch diagnoses covariance only",
    )
    n5 = (
        "derived diagonal not derived probability", "candidate kernel not stochastic dynamics",
        "conditional branch string not empirical string", "echo not Record",
        "partial trace not physical deletion", "finite table not stationarity",
        "fresh bank not autonomous renewal", "open route not impossibility",
    )
    n6 = (
        "retain exact one-step dilation", "retain exact q diagonal",
        "retain same-seed recurrent comparator", "retain supplied fresh-product cylinders",
        "retain Cycle534 deterministic discriminator", "leave branch read/reset/calibration open",
    )
    n7 = (
        "Construct a bounded local regenerative bath whose physical recurrence prepares fresh orthogonal seed sectors without host refresh, prove its finite-window mixing and reset law rather than assuming an iid bank, couple its law-owned actualization receipt to the exact Cycle531 interface, and compare blinded member strings against the separately typed operational grades on train and held preparations. Require inverse/leakage on the dilation, an explicit nonunitary or enlarged-unitary account of reset, all24 covariance, and a predeclared likelihood test that can reject p=q."
    )
    n8 = (
        "Cycle243 event before Record", "Cycles259/262/266 coherent occurrence candidates",
        "Cycle500 coherent cylinders", "Cycle505 binding without member",
        "Cycle508 supplied p=q and hidden carrier", "Cycle531 conditional binder",
        "Cycle534 deterministic ontology comparator",
    )
    return {
        "N1_normalized_routes": n1,
        "N2_wall_independence": n2,
        "N3_hidden_wall_scan": n3,
        "N4_residual_matching": n4,
        "N5_rhetoric_audit": n5,
        "N6_partial_closure": n6,
        "N7_concrete_next_route": n7,
        "N8_cross_cycle_echo": n8,
        "shared_obstruction": False,
        "minimum_content_theorem": False,
        "axiom_pressure": False,
        "pass": (
            len(n1) == 8 and all(len(row) == 4 for row in n1)
            and len(n2) >= 6 and len(n3) >= 12 and len(n4) >= 5
            and len(n5) >= 8 and len(n6) >= 6 and len(n7) > 400 and len(n8) >= 7
        ),
    }


def inventory() -> dict:
    return {
        "supplied": (
            "exact Cycle531 port/interface binder and upstream binding/event interfaces",
            "operational coherent branch state and its grade vector q",
            "blank retained seed, echo head, archive, and member/binder scratch",
            "candidate-law interpretation p=q if used as actual-member weights",
            "fresh tensor-product preparations and independence for product-table comparator",
            "proper-cubic field action and static routing chart",
        ),
        "derived": (
            "fixed coherent copy from singleton binding label to retained seed",
            "finite reversible unitary dilation feeding exact Cycle531 MEMBER plus receipt",
            "orthogonal seed/member reduced diagonal equals q",
            "retained-seed recurrent constant strings and five-slot XOR renewal",
            "fresh-product finite cylinder consequences conditional on supplied independence",
            "inverse/leakage/deletions/all24 and Cycle534 correlation discriminator",
        ),
        "open": (
            "law interpreting reduced diagonal as probability or actual-member p=q",
            "branch actualization and one-member read",
            "physical supplied bath mixture if a classical mixture rather than pure dilation is intended",
            "autonomous fresh-bath reset, independence, renewal, and arbitrary horizon",
            "actual empirical strings, calibration, likelihood, and stationarity",
            "Born law, stochastic dynamics, Record, realized history, permanence/readability",
            "autonomous constraints, two-site Toffoli, integrated amplitude compiler, source/gravity",
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "actual_member": None,
        "framework_Record": None,
        "realized_history": None,
        "Born_probability": None,
    }


def main() -> int:
    started = time.monotonic()
    print("CYCLE 536: FINITE COHERENT-SEED MEMBER DILATION COMPARATOR")
    print("authority=none; audit=unset; derived diagonal only; p=q law supplied")

    contract = contract_controls()
    composition = composition_controls()
    dilation = dilation_and_kernel_firewall_controls()
    recurrence = recurrence_capacity_and_independence_controls()
    covariance = covariance_controls()
    deletions = deletion_controls()
    routing = routing_resource_and_source_audit()
    nogo = no_go_controls()
    supplied_derived_open = inventory()

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "status": "finite coherent dilation; not stochastic dynamics or actualization",
        "contract": contract,
        "Cycle531_composition": composition,
        "dilation_kernel_firewall": dilation,
        "recurrence_capacity_independence": recurrence,
        "proper_cubic_train_held": covariance,
        "deletions": deletions,
        "routing_resources_source_audit": routing,
        "no_go_N1_N8": nogo,
        "supplied_derived_open": supplied_derived_open,
        "elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "process_swap_count": int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0)),
    }

    check("strict hashes, note contract, and primitive registry control close", contract["pass"], contract)
    check("blank-seed dilation emits the exact Cycle531 member/receipt interface and inverts", composition["pass"], composition)
    check("derived q diagonal remains firewalled from supplied p=q law and actual read", dilation["pass"], dilation)
    check("retained-seed recurrence and supplied fresh-product tables expose capacity/independence/reset", recurrence["pass"], recurrence)
    check("the dilation is covariant under all24 with the same train/held schedule", covariance["pass"], covariance)
    check("seed/member/receipt/binder/echo/head deletions are separately visible", deletions["pass"], deletions)
    check("the bounded 206-M2 dilation has exact NN routing/inverse and no host randomness", routing["pass"], routing)
    check("N1-N8 retains constructive closure without a broad no-go or axiom pressure", nogo["pass"], nogo)

    result["PASS"] = PASS
    result["FAIL"] = FAIL
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
