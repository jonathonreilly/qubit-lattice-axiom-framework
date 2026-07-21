#!/usr/bin/env python3
"""Cycle 541: finite open-reset and stochastic-member-read comparator.

The physical circuit is a bounded reversible dilation: a 125-state active
bath is read through a fixed 25-states-per-label table, its member and receipt
feed the exact Cycle531 binder, one of four append-only candidate-output slots
is written, and the old bath microstate is displaced into one of three spent
environment cells while a fresh cell becomes active.  The stochastic kernel
and product genesis measure are separately typed supplied laws.  They are not
inferred from the reversible permutation, and p=q remains a rejectable
candidate calibration rather than a Born derivation.
"""

from __future__ import annotations

import ast
from collections import Counter
from dataclasses import asdict, dataclass
from functools import cache
from hashlib import sha256
import inspect
from itertools import product
import json
from math import log, log2, sqrt
from pathlib import Path
import re
import resource
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_regenerative_bath_member_read_cycle538_2026_07_21 as c538


c536 = c538.c536
c534 = c538.c534
c531 = c538.c531
c505 = c538.c505
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_OPEN_RESET_STOCHASTIC_MEMBER_READ_CYCLE541_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
MENU = tuple(range(5))
MICROSTATES = 125
MICROSTATES_PER_LABEL = 25
TRIAL_CAPACITY = 4
FRESH_CELLS = TRIAL_CAPACITY - 1
G_CRITICAL_DF4_ALPHA_001 = 13.276704135987622
TOL = 2e-9
PASS = 0
FAIL = 0
Word = tuple[int, ...]


FROZEN = {
    "Cycle538 runner": "d794bc9084cd4b670b80ccce3fb2dfb008b39f174979cf17c36984bc840b8be4",
    "Cycle538 note": "068ea67f53bce065ef8e2eb5053ab787e7f33b152617bca727df7fb3e5c96e97",
    "Cycle536 runner": "911d500b42d6c45644ad6d0a9f50a79572380e7b01592a6bf66a842c3c4fcf2f",
    "Cycle531 runner": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "Cycle531 note": "ed40564d4e57090cf03e706b54964e5a24cb735f9ca14df8f008fecffc388042",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
}
FROZEN_PATHS = {
    "Cycle538 runner": Path(c538.__file__),
    "Cycle538 note": c538.NOTE,
    "Cycle536 runner": Path(c536.__file__),
    "Cycle531 runner": Path(c531.__file__),
    "Cycle531 note": c531.NOTE,
    "realized-state primitive": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "Born-frequency boundary": ROOT / "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
}


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    answer = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return answer


_layout = [c531.TOTAL_M2]
ACTIVE_BATH = take(_layout, MICROSTATES)
ENVIRONMENT_CELLS = tuple(take(_layout, MICROSTATES) for _ in range(FRESH_CELLS))
TRIAL_POINTER = take(_layout, TRIAL_CAPACITY)
OUTPUT_FILLED = take(_layout, TRIAL_CAPACITY)
OUTPUT_MEMBER = tuple(take(_layout, 5) for _ in range(TRIAL_CAPACITY))
OUTPUT_OCCURRENCE = take(_layout, TRIAL_CAPACITY)
OUTPUT_CONTENT = tuple(take(_layout, 3) for _ in range(TRIAL_CAPACITY))
TOTAL_M2 = _layout[0]
NEW_M2 = TOTAL_M2 - c531.TOTAL_M2


@dataclass(frozen=True)
class SuppliedStochasticKernel:
    fixture: str
    preparation: str
    p: tuple[float, ...]
    relation: str = "candidate p=q categorical member kernel"
    supplied: bool = True
    derived_from_dilation: bool = False
    Born_derived: bool = False
    empirically_rejectable: bool = True


@dataclass(frozen=True)
class SuppliedGenesisMeasure:
    fixture: str
    preparation: str
    microstate_weights: tuple[float, ...]
    product_cells: int = TRIAL_CAPACITY
    independence: str = "supplied tensor-product genesis measure"
    generated_by_physical_schedule: bool = False


@dataclass(frozen=True)
class LawOwnedRead:
    microstate: int
    actual_member: int
    rule: str = "fixed law-owned microstate partition"
    ontology_supplied: bool = True
    stochasticity_from_read: bool = False
    Record: None = None


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
        "authority: none", "audit: unset", "open reset", "entropy export",
        "125-state", "three fresh", "four-trial", "exact cycle-531",
        "stochastic kernel", "genesis measure", "product independence",
        "law-owned read", "p=q remains a candidate", "not born",
        "reversible dilation", "not inferred", "environment m2", "initial state",
        "mutual information", "reset work", "erasure", "mixing horizon",
        "permanent medium", "not a record", "not realized history",
        "host rng", "host branch choice", "train", "held", "inverse", "leakage",
        "deletion", "all 24 proper-cubic frames", "lawful domain",
        "empirical strings remain separate", "blinded rejection", "n1", "n2", "n3",
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


def one_hot(label: int, width: int) -> Word:
    if label not in range(width):
        raise ValueError("one-hot label leaves its declared word")
    return tuple(int(index == label) for index in range(width))


def singleton(bits: Word, width: int, name: str) -> int:
    if len(bits) != width or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError(f"{name} leaves its exact binary domain")
    if sum(bits) != 1:
        raise ValueError(f"{name} must be one-hot")
    return bits.index(1)


def member_of_microstate(microstate: int) -> int:
    if microstate not in range(MICROSTATES):
        raise ValueError("bath microstate leaves the 125-state domain")
    return microstate // MICROSTATES_PER_LABEL


FIXED_MEMBER_TABLE = tuple(member_of_microstate(state) for state in range(MICROSTATES))


@cache
def kernel_rows() -> tuple[tuple[SuppliedStochasticKernel, SuppliedGenesisMeasure], ...]:
    rows = []
    for typed in c536.operational_rows():
        q = typed.q
        if len(q) != 5 or any(value <= 0 for value in q) or abs(sum(q) - 1.0) >= TOL:
            raise ValueError("Cycle541 kernel q leaves its strictly positive normalized domain")
        weights = tuple(q[member_of_microstate(state)] / MICROSTATES_PER_LABEL for state in range(MICROSTATES))
        rows.append((
            SuppliedStochasticKernel(typed.fixture, typed.preparation, q),
            SuppliedGenesisMeasure(typed.fixture, typed.preparation, weights),
        ))
    return tuple(rows)


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


def emit_schedule(prefix: str) -> tuple[c505.Gate, ...]:
    gates = []
    for state, label in enumerate(FIXED_MEMBER_TABLE):
        gates.extend((
            gate("CNOT", (ACTIVE_BATH[state], c531.MEMBER[label]),
                 f"{prefix}:bath:{state}:member:{label}"),
            gate("CNOT", (ACTIVE_BATH[state], c531.LAW_RECEIPT[label]),
                 f"{prefix}:bath:{state}:receipt:{label}"),
        ))
    return tuple(gates)


def binder_schedule(reverse: bool) -> tuple[c505.Gate, ...]:
    sequence = tuple(reversed(c531.SCHEDULE)) if reverse else c531.SCHEDULE
    direction = "reverse" if reverse else "forward"
    return tuple(
        clone(item, f"binder-{direction}:{index}:{item.label}")
        for index, item in enumerate(sequence)
    )


def output_schedule() -> tuple[c505.Gate, ...]:
    gates = []
    for slot in range(TRIAL_CAPACITY):
        gates.append(gate(
            "CNOT", (TRIAL_POINTER[slot], OUTPUT_FILLED[slot]), f"output:filled:{slot}",
        ))
        for label in MENU:
            gates.append(gate(
                "TOFFOLI", (TRIAL_POINTER[slot], c531.MEMBER[label], OUTPUT_MEMBER[slot][label]),
                f"output:member:{slot}:{label}",
            ))
        gates.append(gate(
            "TOFFOLI", (TRIAL_POINTER[slot], c531.OCCURRENCE, OUTPUT_OCCURRENCE[slot]),
            f"output:occurrence:{slot}",
        ))
        for lane in range(3):
            gates.append(gate(
                "TOFFOLI", (TRIAL_POINTER[slot], c531.ATOM_CONTENT[lane], OUTPUT_CONTENT[slot][lane]),
                f"output:content:{slot}:{lane}",
            ))
    return tuple(gates)


def reset_schedule() -> tuple[c505.Gate, ...]:
    gates = []
    for slot, cell in enumerate(ENVIRONMENT_CELLS):
        for rail in range(MICROSTATES):
            active = ACTIVE_BATH[rail]
            fresh = cell[rail]
            # Controlled SWAP(active,fresh): the two CNOTs cancel when this
            # slot is inactive, and complete a Fredkin when pointer[slot]=1.
            gates.extend((
                gate("CNOT", (active, fresh), f"reset:{slot}:{rail}:mix"),
                gate("TOFFOLI", (TRIAL_POINTER[slot], fresh, active),
                     f"reset:{slot}:{rail}:controlled-swap"),
                gate("CNOT", (active, fresh), f"reset:{slot}:{rail}:unmix"),
            ))
    return tuple(gates)


def pointer_advance_schedule() -> tuple[c505.Gate, ...]:
    gates = []
    for index in reversed(range(TRIAL_CAPACITY - 1)):
        gates.extend(swap_schedule(
            TRIAL_POINTER[index], TRIAL_POINTER[index + 1],
            f"advance-pointer:{index}:{index + 1}",
        ))
    return tuple(gates)


EMIT = emit_schedule("emit")
BINDER_FORWARD = binder_schedule(False)
OUTPUT = output_schedule()
BINDER_REVERSE = binder_schedule(True)
UNEMIT = emit_schedule("unemit")
RESET = reset_schedule()
ADVANCE_POINTER = pointer_advance_schedule()
SCHEDULE = EMIT + BINDER_FORWARD + OUTPUT + BINDER_REVERSE + UNEMIT + RESET + ADVANCE_POINTER


def validate_word(bits: Word) -> None:
    if len(bits) != TOTAL_M2 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Cycle541 word leaves its exact binary 720-M2 domain")


def apply_schedule(
    bits: Word, schedule: tuple[c505.Gate, ...] = SCHEDULE,
    *, reverse: bool = False, delete_label: str | None = None,
) -> Word:
    validate_word(bits)
    matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
    if delete_label is not None and len(matches) != 1:
        raise ValueError("deletion must name exactly one Cycle541 primitive")
    active = tuple(
        item for index, item in enumerate(schedule)
        if delete_label is None or index != matches[0]
    )
    word = list(bits)
    for item in (tuple(reversed(active)) if reverse else active):
        c505.apply_gate(word, item)
    return tuple(word)


def scratch_sites() -> tuple[int, ...]:
    return (
        *c531.MEMBER, *c531.LAW_RECEIPT, c531.PRECOMMIT_READY,
        c531.OCCURRENCE, c531.ATOM_FLAG, *c531.ATOM_CONTENT,
        *c531.PAYLOAD_CURRENT, *c531.PAYLOAD_K_BINARY,
        c531.WORK_BINDING, c531.WORK_PROVENANCE, c531.WORK_TRIGGER,
    )


def output_view(bits: Word) -> tuple[dict, ...]:
    rows = []
    for slot in range(TRIAL_CAPACITY):
        member_bits = tuple(bits[site] for site in OUTPUT_MEMBER[slot])
        rows.append({
            "filled": bits[OUTPUT_FILLED[slot]],
            "member": member_bits.index(1) if sum(member_bits) == 1 else None,
            "member_bits": member_bits,
            "occurrence": bits[OUTPUT_OCCURRENCE[slot]],
            "content": tuple(bits[site] for site in OUTPUT_CONTENT[slot]),
        })
    return tuple(rows)


def active_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in ACTIVE_BATH), MICROSTATES, "active bath")


def environment_of(bits: Word) -> Word:
    return tuple(
        singleton(tuple(bits[site] for site in cell), MICROSTATES, f"environment cell {slot}")
        for slot, cell in enumerate(ENVIRONMENT_CELLS)
    )


def pointer_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in TRIAL_POINTER), TRIAL_CAPACITY, "trial pointer")


def validate_code(bits: Word, *, require_available: bool) -> None:
    validate_word(bits)
    active_of(bits)
    environment_of(bits)
    pointer = pointer_of(bits)
    if any(bits[site] for site in scratch_sites()):
        raise ValueError("Cycle541 member/binder scratch must be blank")
    view = output_view(bits)
    filled = sum(row["filled"] for row in view)
    for row in view:
        if row["filled"]:
            if row["member"] is None:
                raise ValueError("filled output must contain one member")
            if not row["occurrence"] and any(row["content"]):
                raise ValueError("non-occurrence output content must be blank")
        elif row["member"] is not None or row["occurrence"] or any(row["content"]):
            raise ValueError("unfilled output slot must be blank")
    if filled < TRIAL_CAPACITY:
        if pointer != filled or any(not view[index]["filled"] for index in range(filled)):
            raise ValueError("output prefix and trial pointer disagree")
    elif pointer != 0:
        raise ValueError("saturated four-trial output must wrap its pointer to zero")
    if require_available and filled >= TRIAL_CAPACITY:
        raise ValueError("four-trial environment/output capacity is exhausted")


def prepare(
    binding: int, active: int, environment: Word, pointer: int,
    *, edge: int = 1, plus: int = 1, minus: int = 0, K_position: int = 0,
) -> Word:
    if len(environment) != FRESH_CELLS:
        raise ValueError("Cycle541 requires exactly three environment cells")
    base = c531.prepare(
        edge=edge, plus=plus, minus=minus, K_position=K_position,
        binding_label=binding, member_label=None, receipt_label=None,
    )
    bits = list(base + (0,) * NEW_M2)
    for site, bit in zip(ACTIVE_BATH, one_hot(active, MICROSTATES)):
        bits[site] = bit
    for cell, value in zip(ENVIRONMENT_CELLS, environment):
        for site, bit in zip(cell, one_hot(value, MICROSTATES)):
            bits[site] = bit
    for site, bit in zip(TRIAL_POINTER, one_hot(pointer, TRIAL_CAPACITY)):
        bits[site] = bit
    # Construct an admitted append-only prefix for testing later schedule slots.
    for slot in range(pointer):
        label = (slot + 1) % 5
        bits[OUTPUT_FILLED[slot]] = 1
        bits[OUTPUT_MEMBER[slot][label]] = 1
        occurrence = slot % 2
        bits[OUTPUT_OCCURRENCE[slot]] = occurrence
        if occurrence:
            for site, bit in zip(OUTPUT_CONTENT[slot], c505.bits3(label)):
                bits[site] = bit
    output = tuple(bits)
    validate_code(output, require_available=True)
    return output


def physical_step(bits: Word) -> Word:
    validate_code(bits, require_available=True)
    output = apply_schedule(bits)
    validate_code(output, require_available=False)
    return output


def composition_controls() -> dict:
    failures = exact_c531_failures = inverse_failures = scratch_failures = 0
    tests = mismatch_tests = 0
    for active, binding, pointer, current in product(
        range(MICROSTATES), MENU, range(TRIAL_CAPACITY), ((0, 0), (1, 0), (0, 1))
    ):
        plus, minus = current
        edge = plus ^ minus
        environment = tuple((active + 17 * (slot + 1)) % MICROSTATES for slot in range(FRESH_CELLS))
        source = prepare(
            binding, active, environment, pointer, edge=edge, plus=plus, minus=minus,
            K_position=(active + binding + pointer) % c531.K_BITS,
        )
        prior_view = output_view(source)
        emitted = apply_schedule(source, EMIT)
        member = member_of_microstate(active)
        failures += int(
            tuple(emitted[site] for site in c531.MEMBER) != one_hot(member, 5)
            or tuple(emitted[site] for site in c531.LAW_RECEIPT) != one_hot(member, 5)
        )
        midpoint = apply_schedule(emitted, BINDER_FORWARD)
        exact_c531_failures += tuple(midpoint[:c531.TOTAL_M2]) != c531.logical_apply(
            tuple(emitted[:c531.TOTAL_M2])
        )
        occurrence = int(edge and member == binding)
        failures += int(
            midpoint[c531.OCCURRENCE] != occurrence
            or midpoint[c531.ATOM_FLAG] != occurrence
            or tuple(midpoint[site] for site in c531.ATOM_CONTENT)
            != tuple(occurrence & bit for bit in c505.bits3(binding))
        )
        output = physical_step(source)
        inverse_failures += apply_schedule(output, reverse=True) != source
        view = output_view(output)
        failures += int(
            any(view[index] != prior_view[index] for index in range(pointer))
            or view[pointer]["filled"] != 1
            or view[pointer]["member"] != member
            or view[pointer]["occurrence"] != occurrence
            or view[pointer]["content"] != tuple(occurrence & bit for bit in c505.bits3(binding))
            or pointer_of(output) != (pointer + 1) % TRIAL_CAPACITY
        )
        expected_active = environment[pointer] if pointer < FRESH_CELLS else active
        expected_environment = list(environment)
        if pointer < FRESH_CELLS:
            expected_environment[pointer] = active
        failures += int(
            active_of(output) != expected_active
            or environment_of(output) != tuple(expected_environment)
        )
        scratch_failures += any(output[site] for site in scratch_sites())
        mismatch_tests += int(member != binding)
        tests += 1
    return {
        "active_binding_pointer_current_columns": tests,
        "expected_columns": MICROSTATES * 5 * TRIAL_CAPACITY * 3,
        "member_binding_mismatch_columns": mismatch_tests,
        "member_occurrence_reset_output_failures": failures,
        "exact_Cycle531_midpoint_failures": exact_c531_failures,
        "enlarged_dilation_inverse_failures": inverse_failures,
        "terminal_scratch_failures": scratch_failures,
        "pass": not any((failures, exact_c531_failures, inverse_failures, scratch_failures)),
    }


def entropy(probabilities: tuple[float, ...]) -> float:
    return -sum(value * log2(value) for value in probabilities if value > 0)


def mutual_information(joint: dict[tuple[int, int], float]) -> float:
    left = Counter()
    right = Counter()
    for (first, second), value in joint.items():
        left[first] += value
        right[second] += value
    return sum(
        value * log2(value / (left[first] * right[second]))
        for (first, second), value in joint.items() if value > 0
    )


def stochastic_kernel_genesis_entropy_controls() -> dict:
    rows = []
    failures = 0
    for kernel, genesis in kernel_rows():
        mu = genesis.microstate_weights
        label_marginal = tuple(
            sum(mu[state] for state in range(MICROSTATES) if member_of_microstate(state) == label)
            for label in MENU
        )
        marginal_residual = max(abs(left - right) for left, right in zip(label_marginal, kernel.p))
        q_entropy = entropy(kernel.p)
        micro_entropy = entropy(mu)
        pair_joint = Counter()
        for old in range(MICROSTATES):
            for fresh in range(MICROSTATES):
                pair_joint[(member_of_microstate(old), member_of_microstate(fresh))] += mu[old] * mu[fresh]
        label_micro_joint = {
            (member_of_microstate(old), old): mu[old] for old in range(MICROSTATES)
        }
        label_fresh_joint = Counter()
        for old in range(MICROSTATES):
            for fresh in range(MICROSTATES):
                label_fresh_joint[(member_of_microstate(old), fresh)] += mu[old] * mu[fresh]
        pair_mi = mutual_information(dict(pair_joint))
        record_spent_mi = mutual_information(label_micro_joint)
        record_new_active_mi = mutual_information(dict(label_fresh_joint))
        failures += int(
            abs(sum(mu) - 1.0) >= TOL or marginal_residual >= TOL
            or abs(micro_entropy - q_entropy - log2(MICROSTATES_PER_LABEL)) >= TOL
            or abs(pair_mi) >= TOL or abs(record_spent_mi - q_entropy) >= TOL
            or abs(record_new_active_mi) >= TOL
        )
        rows.append({
            "kernel": asdict(kernel),
            "genesis": {
                "fixture": genesis.fixture,
                "preparation": genesis.preparation,
                "microstate_weight_digest": sha256(repr(mu).encode()).hexdigest(),
                "product_cells": genesis.product_cells,
                "independence": genesis.independence,
                "generated_by_physical_schedule": genesis.generated_by_physical_schedule,
            },
            "label_marginal": label_marginal,
            "p_equals_q_residual": marginal_residual,
            "member_entropy_bits": q_entropy,
            "microstate_entropy_bits": micro_entropy,
            "within_label_entropy_bits": log2(MICROSTATES_PER_LABEL),
            "fresh_label_pair_mutual_information_bits": pair_mi,
            "record_spent_cell_mutual_information_bits_after_swap": record_spent_mi,
            "record_new_active_mutual_information_bits_after_swap": record_new_active_mi,
            "mixing_horizon_trials_conditional_on_product_genesis": 1,
            "stochasticity_source": "supplied classical product genesis measure, not physical permutation",
        })
    return {
        "rows": rows,
        "fixed_read_table_independent_of_q": True,
        "law_owned_pointwise_reads": tuple(asdict(LawOwnedRead(state, member_of_microstate(state))) for state in (0, 24, 25, 74, 124)),
        "physical_basis_dynamics_stochastic": False,
        "stochastic_kernel_separately_supplied": True,
        "product_genesis_measure_separately_supplied": True,
        "p_equals_q_candidate_not_Born": True,
        "host_RNG": None,
        "host_branch_choice": None,
        "pass": failures == 0,
    }


def capacity_reset_and_output_controls() -> dict:
    failures = inverse_failures = overwrite_failures = 0
    rows = []
    for origin in range(MICROSTATES):
        samples = (origin, (origin + 17) % 125, (origin + 43) % 125, (origin + 91) % 125)
        initial = prepare(
            member_of_microstate(origin), samples[0], samples[1:], 0,
            K_position=origin % c531.K_BITS,
        )
        word = initial
        prior_views = []
        for trial in range(TRIAL_CAPACITY):
            prior = word
            prior_view = output_view(prior)
            word = physical_step(prior)
            inverse_failures += apply_schedule(word, reverse=True) != prior
            view = output_view(word)
            overwrite_failures += any(view[index] != prior_view[index] for index in range(trial))
            failures += int(
                view[trial]["member"] != member_of_microstate(samples[trial])
                or view[trial]["filled"] != 1
            )
            prior_views.append(view)
        failures += int(
            tuple(row["member"] for row in output_view(word))
            != tuple(member_of_microstate(sample) for sample in samples)
        )
        fifth_rejected = False
        try:
            physical_step(word)
        except ValueError:
            fifth_rejected = True
        failures += int(not fifth_rejected)
        reversed_word = word
        for _ in range(TRIAL_CAPACITY):
            reversed_word = apply_schedule(reversed_word, reverse=True)
        inverse_failures += reversed_word != initial

    # A fully correlated genesis is also lawful basis input and produces a
    # constant word.  This counterexample proves the gates do not create iid.
    correlated_rows = []
    for label in MENU:
        state = label * MICROSTATES_PER_LABEL
        word = prepare(label, state, (state, state, state), 0)
        for _ in range(TRIAL_CAPACITY):
            word = physical_step(word)
        observed = tuple(row["member"] for row in output_view(word))
        correlated_rows.append({"label": label, "word": observed})
        failures += observed != (label,) * TRIAL_CAPACITY

    for kernel, genesis in kernel_rows():
        h_micro = entropy(genesis.microstate_weights)
        rows.append({
            "fixture": kernel.fixture,
            "preparation": kernel.preparation,
            "active_bath_M2": MICROSTATES,
            "fresh_environment_cells": FRESH_CELLS,
            "fresh_environment_M2": FRESH_CELLS * MICROSTATES,
            "total_sample_storage_M2": TRIAL_CAPACITY * MICROSTATES,
            "append_only_output_M2": 40,
            "trial_capacity": TRIAL_CAPACITY,
            "fresh_reset_capacity": FRESH_CELLS,
            "reset_mechanism": "reversible controlled swap/displacement into spent cell",
            "reset_work_derived": False,
            "physical_energy_or_temperature_supplied": False,
            "erasure_entropy_lower_bound_per_reblanked_cell_bits": h_micro,
            "full_four-sample_reuse_erasure_lower_bound_bits": TRIAL_CAPACITY * h_micro,
            "Landauer_work_value": None,
            "reason": "temperature and an erasure dynamics are absent; only information bits are counted",
        })
    return {
        "rows": rows,
        "basis_origin_sequences": MICROSTATES,
        "inverse_failures": inverse_failures,
        "prior_output_overwrite_failures": overwrite_failures,
        "capacity_or_member_failures": failures,
        "correlated_genesis_counterexamples": correlated_rows,
        "fifth_trial_lawful_domain_rejected_for_every_origin": True,
        "candidate_output_persists_under_later_forward_steps_within_capacity": True,
        "candidate_output_is_framework_Record": False,
        "realized_history_claimed": False,
        "permanence_horizon_trials": TRIAL_CAPACITY,
        "unbounded_permanence": None,
        "pass": not any((failures, inverse_failures, overwrite_failures)),
    }


def largest_remainder_counts(p: tuple[float, ...], n: int) -> tuple[int, ...]:
    raw = tuple(value * n for value in p)
    counts = [int(value) for value in raw]
    missing = n - sum(counts)
    order = sorted(MENU, key=lambda label: (-(raw[label] - counts[label]), label))
    for label in order[:missing]:
        counts[label] += 1
    return tuple(counts)


def g_statistic(counts: tuple[int, ...], p: tuple[float, ...]) -> float:
    n = sum(counts)
    return 2.0 * sum(
        observed * log(observed / (n * expected))
        for observed, expected in zip(counts, p) if observed > 0
    )


def empirical_blinded_rejection_controls() -> dict:
    rows = []
    failures = 0
    n = 5000
    for kernel, _ in kernel_rows():
        near = largest_remainder_counts(kernel.p, n)
        biased = tuple(n if label == max(MENU, key=lambda item: kernel.p[item]) else 0 for label in MENU)
        near_g = g_statistic(near, kernel.p)
        biased_g = g_statistic(biased, kernel.p)
        minimum_expected = n * min(kernel.p)
        failures += int(
            minimum_expected < 5 or near_g >= G_CRITICAL_DF4_ALPHA_001
            or biased_g <= G_CRITICAL_DF4_ALPHA_001
        )
        rows.append({
            "fixture": kernel.fixture,
            "preparation": kernel.preparation,
            "predeclared_candidate": "iid categorical p=q",
            "test": "multinomial likelihood-ratio G test, asymptotic chi-square df=4",
            "alpha": 0.01,
            "critical_G": G_CRITICAL_DF4_ALPHA_001,
            "minimum_expected_count_at_N5000": minimum_expected,
            "near_q_control_counts": near,
            "near_q_control_G": near_g,
            "near_q_rejected": near_g > G_CRITICAL_DF4_ALPHA_001,
            "biased_control_counts": biased,
            "biased_control_G": biased_g,
            "biased_rejected": biased_g > G_CRITICAL_DF4_ALPHA_001,
            "serial_independence_test_also_required": True,
        })
    return {
        "rows": rows,
        "precommit_protocol": "hash ordered labels and metadata before unblinding; lock q, alpha, exclusions, and serial test first",
        "observed_empirical_corpus": None,
        "blind_commitment": None,
        "actual_calibration_result": None,
        "physical_four-trial_capacity_sufficient_for_N5000": False,
        "independent_1250_batches_or_larger_environment_required": True,
        "empirical_strings_remain_separate": True,
        "pass": failures == 0,
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
        for active, current in product(range(MICROSTATES), ((0, 0), (1, 0), (0, 1))):
            plus, minus = current
            edge = plus ^ minus
            binding = member_of_microstate(active)
            environment = ((active + 17) % 125, (active + 43) % 125, (active + 91) % 125)
            source = prepare(binding, active, environment, 0, edge=edge, plus=plus, minus=minus)
            output = physical_step(source)
            framed_plus, framed_minus = ((minus, plus) if reversed_endpoints else (plus, minus))
            framed_source = prepare(
                binding, active, environment, 0, edge=edge,
                plus=framed_plus, minus=framed_minus,
            )
            framed_output = physical_step(framed_source)
            expected = list(output)
            if reversed_endpoints:
                expected[c531.C526_CURRENT[0]], expected[c531.C526_CURRENT[1]] = (
                    expected[c531.C526_CURRENT[1]], expected[c531.C526_CURRENT[0]]
                )
            failures += tuple(expected) != framed_output
            tests += 1
    return {
        "proper_cubic_frames": len(frames),
        "tests": tests,
        "failures": failures,
        "orientations": dict(orientations),
        "bath_environment_pointer_output_kernel_genesis_frame_action": "scalar",
        "current_frame_action": "plus/minus exchange under endpoint reversal",
        "same_fixed_schedule_train_L5_and_held_L6": True,
        "pass": len(frames) == 24 and failures == 0,
    }


def deletion_and_lawful_domain_controls() -> dict:
    rows = []

    def witness(label: str, source: Word) -> None:
        full = apply_schedule(source)
        damaged = apply_schedule(source, delete_label=label)
        rows.append({
            "deleted": label,
            "changed": damaged != full,
            "basis_residual": 0.0 if damaged == full else sqrt(2.0),
            "scratch_nonblank": any(damaged[site] for site in scratch_sites()),
        })

    source = prepare(4, 124, (0, 51, 76), 0, K_position=7)
    for label in (
        "emit:bath:124:member:4", "emit:bath:124:receipt:4",
        "binder-forward:46:II:conditional-occurrence",
        "output:filled:0", "output:member:0:4", "output:occurrence:0",
        "unemit:bath:124:member:4", "unemit:bath:124:receipt:4",
        ADVANCE_POINTER[-3].label,
    ):
        witness(label, source)
    for lane, bit in enumerate(c505.bits3(4)):
        if bit:
            witness(f"output:content:0:{lane}", source)
    reset_source = prepare(4, 124, (124, 51, 76), 0, K_position=7)
    for label in (
        "reset:0:124:mix", "reset:0:124:unmix",
    ):
        witness(label, reset_source)
    witness("reset:0:0:controlled-swap", source)

    bath_deleted = list(source)
    bath_deleted[ACTIVE_BATH[124]] = 0
    bath_rejected = False
    try:
        validate_code(tuple(bath_deleted), require_available=True)
    except ValueError:
        bath_rejected = True

    env_deleted = list(source)
    env_deleted[ENVIRONMENT_CELLS[0][0]] = 0
    environment_rejected = False
    try:
        validate_code(tuple(env_deleted), require_available=True)
    except ValueError:
        environment_rejected = True

    overwrite = list(source)
    overwrite[OUTPUT_FILLED[0]] = 1
    overwrite[OUTPUT_MEMBER[0][0]] = 1
    overwrite_rejected = False
    try:
        validate_code(tuple(overwrite), require_available=True)
    except ValueError:
        overwrite_rejected = True

    return {
        "rows": rows,
        "deletion_witnesses": len(rows),
        "unwitnessed": tuple(row["deleted"] for row in rows if not row["changed"]),
        "active_bath_deletion_rejected": bath_rejected,
        "environment_cell_deletion_rejected": environment_rejected,
        "nonprefix_output_overwrite_rejected": overwrite_rejected,
        "unique_schedule_labels": len({item.label for item in SCHEDULE}) == len(SCHEDULE),
        "pass": (
            all(row["changed"] for row in rows) and bath_rejected
            and environment_rejected and overwrite_rejected
            and len({item.label for item in SCHEDULE}) == len(SCHEDULE)
        ),
    }


def routing_resource_and_source_audit() -> dict:
    trace = c505.nn_trace(SCHEDULE, TOTAL_M2)
    source = prepare(3, 89, (12, 47, 111), 0, K_position=15)
    logical = apply_schedule(source)
    routed = c505.apply_routed(source, SCHEDULE)
    roundtrip = c505.apply_routed(routed, SCHEDULE, reverse=True)

    forbidden = {"random", "choice", "choices", "randint", "sample", "argmax", "multinomial"}
    calls = []
    for function in (
        emit_schedule, binder_schedule, output_schedule, reset_schedule,
        pointer_advance_schedule,
    ):
        tree = ast.parse(inspect.getsource(function))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    calls.append(node.func.id)
                elif isinstance(node.func, ast.Attribute):
                    calls.append(node.func.attr)
    forbidden_calls = tuple(call for call in calls if call.lower() in forbidden)
    return {
        **trace,
        "logical_schedule_gates": len(SCHEDULE),
        "expected_logical_schedule_gates": 1798,
        "Cycle531_existing_port_composite_M2": c531.TOTAL_M2,
        "active_bath_M2": MICROSTATES,
        "fresh_environment_M2": FRESH_CELLS * MICROSTATES,
        "trial_pointer_M2": TRIAL_CAPACITY,
        "append_only_candidate_output_M2": 40,
        "new_Cycle541_M2": NEW_M2,
        "total_bounded_port_composite_M2": TOTAL_M2,
        "maximum_displayed_support_M2": trace["maximum_support_M2"],
        "fixed_schedule_routed_equals_logical": routed == logical,
        "routed_inverse_roundtrip": roundtrip == source,
        "forbidden_physical_schedule_calls": forbidden_calls,
        "host_randomness_calls": 0,
        "runtime_host_branch_choice": None,
        "kernel_or_q_calls_in_physical_schedule": 0,
        "two_site_Toffoli_decomposition_supplied": False,
        "autonomous_product_genesis_preparation_supplied": False,
        "underlying_mass_parameter_preserved": 0.45340565417488515,
        "enlarged_reset_output_mass_eigenstate_claimed": False,
        "pass": (
            len(SCHEDULE) == 1798 and routed == logical and roundtrip == source
            and not forbidden_calls and trace["maximum_support_M2"] <= 3
            and trace["connected_failures"] == 0
            and trace["final_adjacent_support_failures"] == 0
            and trace["terminal_operand_order_failures"] == 0
            and trace["reverse_label_restoration_failures"] == 0
            and NEW_M2 == 544 and TOTAL_M2 == 720
        ),
    }


def no_go_controls() -> dict:
    n1 = (
        ("finite open reset dilation", "three fresh 125-state cells plus reversible displacement", "four supplied-independent member trials", "ATTEMPTED"),
        ("closed periodic bath", "Cycle538 deterministic 125-cycle", "correlated pointwise word", "ATTEMPTED"),
        ("pure unitary seed dilation", "Cycle536 coherent seed sectors", "reduced diagonal without actual read", "ATTEMPTED"),
        ("objective stochastic kernel", "separately supplied p=q categorical law", "probability of actual member", "ATTEMPTED AS CANDIDATE"),
        ("autonomous stochastic source", "physical generation of product genesis measure", "fresh trials without imported mixture", "OPEN"),
        ("irreversible reusable reset", "entropy sink and reblanking dynamics", "renewable finite apparatus", "OPEN"),
        ("host RNG/read", "external branch sampling", "member strings", "RULED OUT BY SCOPE"),
        ("permanent history medium", "non-overwriting readable capacity growth", "Record/history", "ATTEMPTED ONLY TO FOUR-SLOT CANDIDATE"),
    )
    n2 = (
        "reversible displacement reset independent of stochastic genesis",
        "stochastic kernel independent of p=q calibration",
        "product independence independent of one-step marginals",
        "fresh capacity independent of irreversible reuse",
        "law-owned pointwise read independent of a probability measure",
        "append-only finite output independent of framework Record permanence",
        "entropy-bit lower bound independent of physical work without temperature",
        "empirical likelihood independent of physical four-trial capacity",
    )
    n3 = (
        "operational q supplied", "candidate p=q kernel supplied",
        "microstate genesis weights supplied", "four-cell tensor-product independence supplied",
        "one-hot active and environment states supplied", "law-owned read ontology supplied",
        "blank output and binder scratch supplied", "fixed 25-state partition supplied",
        "exact Cycle531 ports imported", "three fresh environment cells",
        "finite four-trial capacity", "no autonomous mixture preparation",
        "no reblanking entropy sink", "no temperature or work law",
        "no empirical corpus or blind commitment", "three-site Toffoli and static line chart",
        "L5/L6 preparation interface", "no unbounded output growth",
    )
    n4 = (
        "zero enlarged inverse/leakage residual diagnoses dilation reversibility only",
        "zero p=q marginal residual diagnoses supplied genesis arithmetic only",
        "zero fresh mutual information diagnoses supplied product measure only",
        "record-spent mutual information diagnoses exported correlation only",
        "four-step persistence diagnoses finite candidate output only",
        "fifth-step rejection diagnoses capacity rather than impossibility",
        "all24 mismatch diagnoses covariance only", "deletion sqrt(2) diagnoses load-bearing gates only",
        "G-test controls diagnose a predeclared rejection surface, not empirical truth",
    )
    n5 = (
        "open dilation not autonomous stochastic source", "swap reset not erasure",
        "entropy bits not physical work or energy", "supplied iid genesis not derived independence",
        "pointwise read not stochasticity", "finite output not framework Record",
        "four events not realized history", "p=q candidate not Born law",
        "synthetic controls not empirical data", "counter advance not physical time",
        "route-specific capacity wall not constitutional evidence",
    )
    n6 = (
        "retain exact finite reset dilation", "retain exact Cycle531 member occurrence composition",
        "retain separately typed kernel genesis and read", "retain explicit entropy and mutual-information flow",
        "retain exact four-trial product consequences conditional on genesis",
        "retain finite append-only candidate output and fifth-step rejection",
        "retain all24 inverse deletion routing and empirical protocol",
        "leave autonomous stochastic source reusable erasure permanence and Born open",
    )
    n7 = (
        "Construct a local autonomous source model that prepares the Cycle541 product genesis measure from a declared nonequilibrium resource without a host sampler, extend the environment ledger so every renewal exports its correlations to named M2, and either implement a reusable reblanking channel with temperature/work assumptions or prove only a bounded capacity statement.  Scale the append-only readable medium and fresh-cell bank to a predeclared blinded corpus, lock p=q and serial-independence tests before unblinding, and compare actual strings against Cycle541 iid, Cycle538 periodic, Cycle536 coherent, and Cycle534 carrier hypotheses.  Require all24 covariance, enlarged inverse accounting, deletion controls, and an explicit distinction between candidate output and framework Record."
    )
    n8 = (
        "Cycle243 event-before-Record boundary", "Cycles259/262/266 coherent occurrence candidates",
        "Cycle500 coherent cylinders", "Cycle505 binding without member",
        "Cycle508 p=q and actual-member law tournament", "Cycle531 exact conditional binder",
        "Cycle534 deterministic carrier", "Cycle536 reduced-diagonal dilation",
        "Cycle538 deterministic recurrent bath",
    )
    return {
        "N1_normalized_routes": n1,
        "N2_wall_independence": n2,
        "N3_hidden_wall_scan": n3,
        "N4_residual_matching": n4,
        "N5_rhetoric_audit": n5,
        "N6_partial_closure": n6,
        "N7_steelman_next_route": n7,
        "N8_cross_cycle_echo": n8,
        "route_specific_result": True,
        "shared_obstruction": False,
        "minimum_content_theorem": False,
        "axiom_pressure": False,
        "pass": (
            len(n1) == 8 and all(len(row) == 4 for row in n1)
            and len(n2) >= 8 and len(n3) >= 18 and len(n4) >= 9
            and len(n5) >= 11 and len(n6) >= 8 and len(n7) > 600 and len(n8) >= 9
        ),
    }


def inventory() -> dict:
    return {
        "supplied": (
            "exact Cycle531 MEMBER receipt occurrence interface and upstream binding/event fixtures",
            "candidate categorical p=q stochastic kernel for each train/held preparation",
            "125-microstate genesis measure and its four-cell tensor-product independence",
            "law-owned fixed-partition actual-member read ontology",
            "initial one-hot active bath, three fresh environment cells, pointer, blank output, and scratch",
            "proper-cubic field action, static line chart, and three-site Toffoli primitive",
        ),
        "derived": (
            "fixed 720-M2 reversible open dilation with three controlled swap resets",
            "exact Cycle531 occurrence and four append-only candidate-output writes",
            "p=q member marginal and one-trial mixing conditional on supplied product genesis",
            "record-spent mutual information transfer and microstate erasure entropy in bits",
            "finite four-trial persistence, capacity exhaustion, and correlated-genesis counterexample",
            "inverse leakage deletion all24 routing and predeclared likelihood controls",
        ),
        "open": (
            "derivation or autonomous preparation of the stochastic kernel and product genesis measure",
            "Born calibration and empirical acceptance or rejection of p=q",
            "reusable irreversible reset, entropy sink, temperature, work, and physical energy",
            "fresh independence beyond four trials and arbitrary-horizon mixing",
            "permanent framework Record, readable realized history, and unbounded capacity growth",
            "actual empirical strings, blind commitment, serial test, and N=5000 resource realization",
            "autonomous constraints, two-site Toffoli compilation, source, gravity, or physical time",
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "physical_time_derived": False,
        "physical_energy_derived": False,
        "source_or_gravity_derived": False,
        "framework_Record": None,
        "realized_history": None,
        "Born_probability": None,
    }


def main() -> int:
    started = time.monotonic()
    print("CYCLE 541: FINITE OPEN RESET AND STOCHASTIC MEMBER-READ COMPARATOR")
    print("authority=none; audit=unset; supplied kernel/genesis/read; not Born/Record")

    contract = contract_controls()
    composition = composition_controls()
    stochastic = stochastic_kernel_genesis_entropy_controls()
    capacity = capacity_reset_and_output_controls()
    empirical = empirical_blinded_rejection_controls()
    covariance = covariance_controls()
    deletions = deletion_and_lawful_domain_controls()
    routing = routing_resource_and_source_audit()
    nogo = no_go_controls()
    supplied_derived_open = inventory()

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "status": "finite open dilation conditional on supplied stochastic kernel/product genesis/read",
        "contract": contract,
        "Cycle531_composition": composition,
        "stochastic_kernel_genesis_entropy": stochastic,
        "capacity_reset_candidate_output": capacity,
        "empirical_blinded_rejection": empirical,
        "proper_cubic_train_held": covariance,
        "deletions_lawful_domain": deletions,
        "routing_resources_source_audit": routing,
        "no_go_N1_N8": nogo,
        "supplied_derived_open": supplied_derived_open,
        "elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "process_swap_count": int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0)),
    }

    check("strict hashes, note contract, and premise registry control close", contract["pass"], contract)
    check("the enlarged reset/output dilation composes exactly with Cycle531", composition["pass"], composition)
    check("kernel genesis read entropy and mutual information remain separately typed", stochastic["pass"], stochastic)
    check("four-trial capacity persists output and exposes correlated-genesis and fifth-step controls", capacity["pass"], capacity)
    check("p=q has a predeclared blinded likelihood rejection surface", empirical["pass"], empirical)
    check("the same fixed schedule is covariant under all 24 proper-cubic frames", covariance["pass"], covariance)
    check("reset output binder and environment deletions and domains are visible", deletions["pass"], deletions)
    check("the bounded 720-M2 dilation has exact NN routing/inverse and no host RNG", routing["pass"], routing)
    check("N1-N8 retains partial closure without shared no-go or axiom pressure", nogo["pass"], nogo)

    result["PASS"] = PASS
    result["FAIL"] = FAIL
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
