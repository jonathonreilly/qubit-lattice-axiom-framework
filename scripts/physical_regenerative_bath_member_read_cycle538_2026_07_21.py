#!/usr/bin/env python3
"""Cycle 538: deterministic finite-bath member-read comparator.

A 125-state one-hot bath follows a fixed reversible cycle.  A supplied,
preparation-indexed partition of that cycle emits exactly one law-owned MEMBER
and receipt into the exact Cycle531 conditional occurrence interface.  This is
a constructive pointwise deterministic read ontology, not stochastic dynamics:
its finite member word, frequency quantization, correlations, recurrence, and
XOR echo deletion are all explicit.  No host RNG or runtime branch choice is
used by the physical schedule.
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
from math import sqrt
from pathlib import Path
import re
import resource
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_coherent_seed_member_dilation_cycle536_2026_07_21 as c536


c534 = c536.c534
c531 = c536.c531
c505 = c536.c505
c508 = c536.c508
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_REGENERATIVE_BATH_MEMBER_READ_CYCLE538_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
MENU = tuple(range(5))
BATH_PERIOD = 125
ECHO_SLOTS = 5
TOL = 2e-9
PASS = 0
FAIL = 0
Word = tuple[int, ...]
Sparse = dict[Word, complex]


FROZEN = {
    "Cycle536 runner": "911d500b42d6c45644ad6d0a9f50a79572380e7b01592a6bf66a842c3c4fcf2f",
    "Cycle536 note": "e15944633127890fe27cb52193960a28d9860212d5d7aafd70f15eef2e987457",
    "Cycle534 runner": "76a46047a4f14054f6e0655a360122967d3626c45f51d584e5df2e4aa6e1e2db",
    "Cycle534 note": "1ddf4c552b035ffbc977dfd7b3c1d0e72f02063a3e127adb71c6dfe859c46a3e",
    "Cycle531 runner": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "Cycle531 note": "ed40564d4e57090cf03e706b54964e5a24cb735f9ca14df8f008fecffc388042",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
}
FROZEN_PATHS = {
    "Cycle536 runner": Path(c536.__file__),
    "Cycle536 note": c536.NOTE,
    "Cycle534 runner": Path(c534.__file__),
    "Cycle534 note": c534.NOTE,
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
BATH = take(_layout, BATH_PERIOD)
ECHO_HEAD = take(_layout, ECHO_SLOTS)
ECHO_OCCURRENCE = take(_layout, ECHO_SLOTS)
ECHO_CONTENT = tuple(take(_layout, 3) for _ in range(ECHO_SLOTS))
TOTAL_M2 = _layout[0]
NEW_M2 = TOTAL_M2 - c531.TOTAL_M2


@dataclass(frozen=True)
class BathLaw:
    fixture: str
    preparation: str
    q: tuple[float, ...]
    counts: tuple[int, ...]
    p_hat: tuple[float, ...]
    member_table: Word
    stochastic: bool = False
    Born_calibrated: bool = False
    p_equals_q: bool = False
    derived_from_axioms: bool = False


@dataclass(frozen=True)
class PointwiseRead:
    bath_microstate: int
    actual_member: int
    read_rule: str = "supplied deterministic bath partition"
    probability: None = None
    random_draw: None = None
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
        "authority: none", "audit: unset", "125-state", "deterministic bath",
        "exact cycle-531", "pointwise actual member", "supplied read ontology",
        "not stochastic", "not born", "not a record", "not realized history",
        "p=q is not derived", "pure unitary dilation", "reduced diagonal",
        "single realized member", "repeated-trial independence", "permanent record",
        "bath genesis", "reset entropy sink", "host rng", "host branch choice",
        "train", "held", "recurrence", "inverse", "leakage", "deletion",
        "all 24 proper-cubic frames", "empirical strings remain separate",
        "blinded rejection", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8",
        "no axiom pressure", "supplied / derived / open",
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


def normalized_q(q: tuple[float, ...]) -> None:
    if len(q) != 5 or any(value < -TOL for value in q) or abs(sum(q) - 1.0) >= TOL:
        raise ValueError("q leaves the normalized five-label domain")


def largest_remainder(q: tuple[float, ...]) -> tuple[int, ...]:
    normalized_q(q)
    raw = tuple(value * BATH_PERIOD for value in q)
    counts = [int(value) for value in raw]
    missing = BATH_PERIOD - sum(counts)
    order = sorted(MENU, key=lambda label: (-(raw[label] - counts[label]), label))
    for label in order[:missing]:
        counts[label] += 1
    return tuple(counts)


def partition_table(counts: tuple[int, ...]) -> Word:
    if len(counts) != 5 or any(type(value) is not int or value < 0 for value in counts):
        raise ValueError("partition counts leave the exact nonnegative five-label domain")
    if sum(counts) != BATH_PERIOD:
        raise ValueError("partition counts must cover exactly 125 bath states")
    return tuple(label for label, count in enumerate(counts) for _ in range(count))


@cache
def operational_laws() -> tuple[BathLaw, ...]:
    laws = []
    for typed in c536.operational_rows():
        counts = largest_remainder(typed.q)
        laws.append(BathLaw(
            fixture=typed.fixture,
            preparation=typed.preparation,
            q=typed.q,
            counts=counts,
            p_hat=tuple(value / BATH_PERIOD for value in counts),
            member_table=partition_table(counts),
        ))
    return tuple(laws)


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


def emit_schedule(table: Word, prefix: str) -> tuple[c505.Gate, ...]:
    gates = []
    for bath_state, label in enumerate(table):
        gates.extend((
            gate("CNOT", (BATH[bath_state], c531.MEMBER[label]),
                 f"{prefix}:bath:{bath_state}:member:{label}"),
            gate("CNOT", (BATH[bath_state], c531.LAW_RECEIPT[label]),
                 f"{prefix}:bath:{bath_state}:receipt:{label}"),
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


def cyclic_advance(sites: tuple[int, ...], name: str) -> tuple[c505.Gate, ...]:
    gates = []
    for index in reversed(range(len(sites) - 1)):
        gates.extend(swap_schedule(sites[index], sites[index + 1], f"advance-{name}:{index}:{index + 1}"))
    return tuple(gates)


BINDER_FORWARD = binder_schedule(False)
ECHO = echo_schedule()
BINDER_REVERSE = binder_schedule(True)
ADVANCE_BATH = cyclic_advance(BATH, "bath")
ADVANCE_HEAD = cyclic_advance(ECHO_HEAD, "head")


def schedule_for(table: Word) -> tuple[c505.Gate, ...]:
    emit = emit_schedule(table, "emit")
    unemit = emit_schedule(table, "unemit")
    return emit + BINDER_FORWARD + ECHO + BINDER_REVERSE + unemit + ADVANCE_BATH + ADVANCE_HEAD


def validate_word(bits: Word) -> None:
    if len(bits) != TOTAL_M2 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Cycle538 word leaves its exact binary 326-M2 domain")


def apply_schedule(
    bits: Word, schedule: tuple[c505.Gate, ...], *, reverse: bool = False,
    delete_label: str | None = None,
) -> Word:
    validate_word(bits)
    matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
    if delete_label is not None and len(matches) != 1:
        raise ValueError("deletion must name exactly one Cycle538 primitive")
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


def scratch_sites() -> tuple[int, ...]:
    return (
        *c531.MEMBER, *c531.LAW_RECEIPT, c531.PRECOMMIT_READY,
        c531.OCCURRENCE, c531.ATOM_FLAG, *c531.ATOM_CONTENT,
        *c531.PAYLOAD_CURRENT, *c531.PAYLOAD_K_BINARY,
        c531.WORK_BINDING, c531.WORK_PROVENANCE, c531.WORK_TRIGGER,
    )


def prepare(
    binding: int, bath: int, head: int, *, edge: int = 1,
    plus: int = 1, minus: int = 0, K_position: int = 0,
) -> Word:
    base = c531.prepare(
        edge=edge, plus=plus, minus=minus, K_position=K_position,
        binding_label=binding, member_label=None, receipt_label=None,
    )
    bits = list(base + (0,) * NEW_M2)
    for site, bit in zip(BATH, one_hot(bath, BATH_PERIOD)):
        bits[site] = bit
    for site, bit in zip(ECHO_HEAD, one_hot(head, ECHO_SLOTS)):
        bits[site] = bit
    output = tuple(bits)
    validate_code(output)
    return output


def validate_code(bits: Word) -> None:
    validate_word(bits)
    singleton(tuple(bits[site] for site in BATH), BATH_PERIOD, "bath")
    singleton(tuple(bits[site] for site in ECHO_HEAD), ECHO_SLOTS, "echo head")
    if any(bits[site] for site in scratch_sites()):
        raise ValueError("Cycle538 terminal member/binder scratch must be blank")


def bath_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in BATH), BATH_PERIOD, "bath")


def head_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in ECHO_HEAD), ECHO_SLOTS, "echo head")


def echo_view(bits: Word) -> tuple[tuple[int, Word], ...]:
    return tuple(
        (bits[ECHO_OCCURRENCE[slot]], tuple(bits[site] for site in ECHO_CONTENT[slot]))
        for slot in range(ECHO_SLOTS)
    )


def binding_of(bits: Word) -> int:
    return singleton(
        tuple(bits[c531.offset(c505.C_ELIGIBILITY[label])] for label in MENU),
        5, "binding eligibility",
    )


def composition_controls() -> dict:
    failures = inverse_failures = scratch_failures = exact_c531_failures = 0
    tests = mismatch_tests = 0
    laws = operational_laws()
    for law in laws:
        schedule = schedule_for(law.member_table)
        for bath, binding, head, current in product(
            range(BATH_PERIOD), MENU, MENU, ((0, 0), (1, 0), (0, 1))
        ):
            plus, minus = current
            edge = plus ^ minus
            source = prepare(
                binding, bath, head, edge=edge, plus=plus, minus=minus,
                K_position=(bath + binding + head) % c531.K_BITS,
            )
            emit = emit_schedule(law.member_table, "emit")
            emitted = apply_schedule(source, emit)
            member = law.member_table[bath]
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
            output = apply_schedule(source, schedule)
            validate_code(output)
            inverse_failures += apply_schedule(output, schedule, reverse=True) != source
            expected_echo = list(echo_view(source))
            if occurrence:
                expected_echo[head] = (1, c505.bits3(binding))
            failures += int(
                bath_of(output) != (bath + 1) % BATH_PERIOD
                or head_of(output) != (head + 1) % ECHO_SLOTS
                or echo_view(output) != tuple(expected_echo)
            )
            scratch_failures += any(output[site] for site in scratch_sites())
            mismatch_tests += int(member != binding)
            tests += 1
    return {
        "law_fixtures": len(laws),
        "bath_binding_head_current_columns": tests,
        "expected_columns": len(laws) * BATH_PERIOD * 5 * 5 * 3,
        "mismatched_member_binding_columns": mismatch_tests,
        "member_occurrence_failures": failures,
        "exact_Cycle531_midpoint_failures": exact_c531_failures,
        "inverse_failures": inverse_failures,
        "terminal_scratch_failures": scratch_failures,
        "pass": not any((failures, exact_c531_failures, inverse_failures, scratch_failures)),
    }


def ontology_and_frequency_controls() -> dict:
    rows = []
    failures = 0
    for law in operational_laws():
        reads = tuple(PointwiseRead(state, law.member_table[state]) for state in range(BATH_PERIOD))
        observed = tuple(Counter(read.actual_member for read in reads)[label] for label in MENU)
        max_residual = max(abs(left - right) for left, right in zip(law.p_hat, law.q))
        exact_p_equals_q = max_residual < TOL
        failures += int(
            observed != law.counts or len(reads) != BATH_PERIOD
            or any(read.probability is not None or read.random_draw is not None for read in reads)
            or max_residual > 1.0 / BATH_PERIOD + TOL
        )
        rows.append({
            **asdict(law),
            "member_table": sha256(bytes(law.member_table)).hexdigest(),
            "pointwise_reads": len(reads),
            "observed_full_cycle_counts": observed,
            "max_abs_p_hat_minus_q": max_residual,
            "exact_p_hat_equals_q": exact_p_equals_q,
            "relation": "p_hat is a supplied deterministic-cycle allocation approximating q; it is not p=q",
        })
    return {
        "rows": rows,
        "single_realized_member_given_bath_microstate": True,
        "read_ontology_supplied": True,
        "unitary_schedule_produces_pointwise_member_receipt": True,
        "stochastic_transition_law": None,
        "Born_calibration": None,
        "host_RNG": None,
        "host_branch_choice": None,
        "probability_measure_over_bath_genesis": None,
        "pass": failures == 0,
    }


def recurrence_independence_and_record_controls() -> dict:
    return_failures = midpoint_failures = inverse_failures = 0
    rows = []
    for law in operational_laws():
        schedule = schedule_for(law.member_table)
        # Test the five coherent binding sectors at one bath/head origin.  The
        # same reversible schedule is applied to every sector; no branch is
        # chosen by the host.
        initial: Sparse = {
            prepare(label, 0, 0): sqrt(value)
            for label, value in enumerate(law.q) if value > 1e-15
        }
        state = initial
        checkpoint125 = None
        for step in range(250):
            prior = state
            state = sparse_apply(state, schedule)
            inverse_failures += sparse_apply(state, schedule, reverse=True) != prior
            if step == 124:
                checkpoint125 = state
        return_failures += state != initial
        occupied125 = tuple(
            sorted({sum(item[0] for item in echo_view(word)) for word in checkpoint125})
        ) if checkpoint125 is not None else ()
        midpoint_failures += checkpoint125 == initial

        word = law.member_table
        rotations = tuple(word[start:] + word[:start] for start in range(BATH_PERIOD))
        counts_all_starts = {
            tuple(Counter(candidate)[label] for label in MENU) for candidate in rotations
        }
        bigrams = Counter((word[index], word[(index + 1) % BATH_PERIOD]) for index in range(BATH_PERIOD))
        same_label_fraction = sum(value for (left, right), value in bigrams.items() if left == right) / BATH_PERIOD
        iid_same_label = sum(value * value for value in law.p_hat)
        return_failures += int(len(counts_all_starts) != 1)
        rows.append({
            "fixture": law.fixture,
            "preparation": law.preparation,
            "full_cycle_counts_all_125_origins": tuple(counts_all_starts)[0],
            "member_period_divides": BATH_PERIOD,
            "bath_period": BATH_PERIOD,
            "head_period": ECHO_SLOTS,
            "full_bath_head_period": BATH_PERIOD,
            "echo_archive_exact_return_steps": 250,
            "occupied_echo_slots_after_125": occupied125,
            "same_label_bigram_fraction": same_label_fraction,
            "iid_comparator_same_label_probability": iid_same_label,
            "same_label_residual_from_iid_comparator": same_label_fraction - iid_same_label,
            "repeated_trial_independence": False,
            "fresh_product_independence": None,
            "finite_deterministic_stationarity_measure": None,
        })
    return {
        "rows": rows,
        "inverse_failures": inverse_failures,
        "125_step_nonblank_checkpoint_failures": midpoint_failures,
        "250_step_exact_sparse_return_failures": return_failures,
        "bath_genesis_microstate": "supplied singleton; all 125 origins admitted and tested",
        "regeneration": "closed finite recurrence only",
        "reset_entropy_sink": None,
        "entropy_export": None,
        "echo_semantics": "reversible XOR candidate; erased on recurrence",
        "permanent_Record_or_history": None,
        "actual_empirical_strings": None,
        "pass": not any((return_failures, midpoint_failures, inverse_failures)),
    }


def blinded_rejection_controls() -> dict:
    rows = []
    failures = 0
    for law in operational_laws():
        admitted = {law.member_table[start:] + law.member_table[:start] for start in range(BATH_PERIOD)}
        cycle534 = tuple(step % 5 for step in range(BATH_PERIOD))
        constant = tuple((0,) * BATH_PERIOD)
        reversed_table = tuple(reversed(law.member_table))
        probes = {
            "all_compiled_cyclic_origins": all(candidate in admitted for candidate in admitted),
            "Cycle534_uniform_rotation_rejected": cycle534 not in admitted,
            "constant_Cycle536_style_rejected": constant not in admitted,
            "reversed_partition_rejected": reversed_table not in admitted,
        }
        # Some degenerate tables could be reversal invariant.  The operational
        # fixtures are checked rather than assuming this discriminator.
        failures += int(not probes["all_compiled_cyclic_origins"])
        rows.append({
            "fixture": law.fixture,
            "preparation": law.preparation,
            "predeclared_blind_rule": (
                "accept exactly a cyclic rotation of the compiled 125-label table; "
                "otherwise reject this deterministic bath law"
            ),
            "admitted_distinct_rotations": len(admitted),
            "probes": probes,
            "likelihood_or_p_value": None,
            "reason": "no stochastic transition law or genesis measure is supplied",
        })
    return {
        "rows": rows,
        "candidate_is_empirically_falsifiable_by_exact_word_mismatch": True,
        "observed_empirical_corpus": None,
        "blinding_key_or_trial_order": None,
        "calibration_result": None,
        "pass": failures == 0,
    }


def covariance_controls() -> dict:
    frames = c531.c526.c235.proper_cubic_frames()
    failures = tests = 0
    orientations = Counter()
    for law in operational_laws():
        schedule = schedule_for(law.member_table)
        for frame in frames:
            mapped = frame @ c531.c526.np.asarray((1, 0, 0), dtype=int)
            axis = int(c531.c526.np.flatnonzero(mapped)[0])
            reversed_endpoints = int(mapped[axis]) == -1
            orientations["endpoint_reversing" if reversed_endpoints else "endpoint_preserving"] += 1
            for bath, current in product(range(BATH_PERIOD), ((0, 0), (1, 0), (0, 1))):
                plus, minus = current
                edge = plus ^ minus
                binding = law.member_table[bath]
                source = prepare(binding, bath, bath % 5, edge=edge, plus=plus, minus=minus)
                output = apply_schedule(source, schedule)
                framed_plus, framed_minus = ((minus, plus) if reversed_endpoints else (plus, minus))
                framed_source = prepare(
                    binding, bath, bath % 5, edge=edge,
                    plus=framed_plus, minus=framed_minus,
                )
                framed_output = apply_schedule(framed_source, schedule)
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
        "bath_head_member_receipt_echo_partition_frame_action": "scalar",
        "current_frame_action": "plus/minus exchange under endpoint reversal",
        "same_schedule_train_L5_and_held_L6": True,
        "pass": len(frames) == 24 and failures == 0,
    }


def deletion_and_domain_controls() -> dict:
    law = operational_laws()[0]
    schedule = schedule_for(law.member_table)
    rows = []

    def witness(label: str, source: Word) -> None:
        full = apply_schedule(source, schedule)
        damaged = apply_schedule(source, schedule, delete_label=label)
        rows.append({
            "deleted": label,
            "changed": damaged != full,
            "basis_residual": 0.0 if damaged == full else sqrt(2.0),
            "scratch_nonblank": any(damaged[site] for site in scratch_sites()),
        })

    for bath, label in enumerate(law.member_table):
        if bath == 0 or law.member_table[bath - 1] != label:
            source = prepare(label, bath, bath % 5)
            witness(f"emit:bath:{bath}:member:{label}", source)
            witness(f"emit:bath:{bath}:receipt:{label}", source)
            witness(f"unemit:bath:{bath}:member:{label}", source)
            witness(f"unemit:bath:{bath}:receipt:{label}", source)
    source = prepare(law.member_table[0], 0, 0, K_position=7)
    witness("binder-forward:46:II:conditional-occurrence", source)
    witness("binder-reverse:15:II:conditional-occurrence", source)
    witness("echo:occurrence:0", source)
    content = c505.bits3(law.member_table[0])
    for lane, bit in enumerate(content):
        if bit:
            witness(f"echo:content:0:{lane}", source)
    witness(ADVANCE_BATH[-3].label, source)
    witness(ADVANCE_HEAD[-3].label, source)

    invalid = list(source)
    invalid[BATH[0]] = 0
    bath_deletion_rejected = False
    try:
        validate_code(tuple(invalid))
    except ValueError:
        bath_deletion_rejected = True

    bad_counts_rejected = False
    try:
        partition_table((25, 25, 25, 25, 24))
    except ValueError:
        bad_counts_rejected = True

    transfer = list(law.counts)
    donor = next(index for index, value in enumerate(transfer) if value > 0)
    receiver = (donor + 1) % 5
    transfer[donor] -= 1
    transfer[receiver] += 1
    perturbed = partition_table(tuple(transfer))
    partition_transfer_changes_word = perturbed != law.member_table
    return {
        "rows": rows,
        "deletion_witnesses": len(rows),
        "unwitnessed": tuple(row["deleted"] for row in rows if not row["changed"]),
        "bath_input_deletion_rejected": bath_deletion_rejected,
        "malformed_partition_rejected": bad_counts_rejected,
        "one_count_partition_transfer_changes_word": partition_transfer_changes_word,
        "unique_schedule_labels": len({item.label for item in schedule}) == len(schedule),
        "pass": (
            all(row["changed"] for row in rows) and bath_deletion_rejected
            and bad_counts_rejected and partition_transfer_changes_word
            and len({item.label for item in schedule}) == len(schedule)
        ),
    }


def routing_resource_and_source_audit() -> dict:
    law = operational_laws()[0]
    schedule = schedule_for(law.member_table)
    trace = c505.nn_trace(schedule, TOTAL_M2)
    source = prepare(law.member_table[17], 17, 2, K_position=15)
    logical = apply_schedule(source, schedule)
    routed = c505.apply_routed(source, schedule)
    roundtrip = c505.apply_routed(routed, schedule, reverse=True)

    forbidden = {"random", "choice", "choices", "randint", "sample", "argmax", "multinomial"}
    calls = []
    for function in (emit_schedule, binder_schedule, echo_schedule, cyclic_advance, schedule_for):
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
        "recurrent_logical_gates": len(schedule),
        "expected_recurrent_logical_gates": 1028,
        "Cycle531_existing_port_composite_M2": c531.TOTAL_M2,
        "new_bath_M2": BATH_PERIOD,
        "new_echo_head_M2": 5,
        "new_echo_archive_M2": 20,
        "new_Cycle538_M2": NEW_M2,
        "total_bounded_port_composite_M2": TOTAL_M2,
        "maximum_displayed_support_M2": trace["maximum_support_M2"],
        "fixed_schedule_routed_equals_logical": routed == logical,
        "routed_inverse_roundtrip": roundtrip == source,
        "forbidden_physical_schedule_calls": forbidden_calls,
        "host_randomness_calls": 0,
        "runtime_host_branch_choice": None,
        "q_dependent_schedule_compilation": "supplied ahead of recurrence",
        "two_site_Toffoli_decomposition_supplied": False,
        "autonomous_constraint_preparation_supplied": False,
        "underlying_mass_parameter_preserved": 0.45340565417488515,
        "enlarged_bath_history_mass_eigenstate_claimed": False,
        "pass": (
            len(schedule) == 1028 and routed == logical and roundtrip == source
            and not forbidden_calls and trace["maximum_support_M2"] <= 3
            and trace["connected_failures"] == 0
            and trace["final_adjacent_support_failures"] == 0
            and trace["terminal_operand_order_failures"] == 0
            and trace["reverse_label_restoration_failures"] == 0
            and NEW_M2 == 150 and TOTAL_M2 == 326
        ),
    }


def no_go_controls() -> dict:
    n1 = (
        ("deterministic 125-state bath", "fixed local reversible cycle plus supplied partition", "pointwise member and finite periodic word", "ATTEMPTED"),
        ("pure unitary seed dilation", "Cycle536 coherent seed", "derived reduced diagonal q without read", "ATTEMPTED"),
        ("classical bath mixture", "supplied measure over bath genesis", "one-step ensemble p_hat", "ATTEMPTED AS CONDITIONAL"),
        ("fresh product bank", "independently prepared finite bath copies", "finite iid cylinder conditional on independence", "ATTEMPTED AS CONDITIONAL"),
        ("open regenerative bath", "entropy export plus reset dynamics", "renewed trials beyond closed recurrence", "OPEN"),
        ("objective stochastic field", "law-owned transition and read", "actual stochastic strings", "OPEN"),
        ("host RNG/read", "external random branch", "sampled member", "RULED OUT BY SCOPE"),
        ("Cycle534 hidden carrier", "deterministic period-five ontology", "uniform correlated comparator", "ATTEMPTED"),
    )
    n2 = (
        "pointwise read ontology independent of a probability measure",
        "probability measure independent of p=q calibration",
        "one-step frequency independent of repeated-trial independence",
        "finite recurrence independent of entropy-export reset",
        "XOR echo capacity independent of permanent Record",
        "pure reduced diagonal independent of a single realized member",
        "empirical rejection independent of likelihood without a stochastic law",
    )
    n3 = (
        "operational q supplied", "q-to-125-count allocation supplied",
        "contiguous partition convention supplied", "bath microstate genesis supplied",
        "pointwise bath-read ontology supplied", "singleton bath and head constraints supplied",
        "blank member receipt binder and echo scratch supplied", "exact Cycle531 interface imported",
        "no stochastic transition law", "no genesis measure", "no entropy sink",
        "no permanent output medium", "no empirical corpus or blind key",
        "three-site Toffoli and static line chart", "L5/L6 preparation interface",
    )
    n4 = (
        "zero circuit inverse and leakage residual diagnoses reversible recurrence only",
        "full-cycle counts diagnose deterministic allocation only",
        "p_hat-minus-q residual diagnoses 125-state quantization only",
        "bigram residual diagnoses non-iid correlation, not probabilities",
        "all24 mismatch diagnoses covariance only",
        "deletion sqrt(2) diagnoses load-bearing primitives only",
        "exact-word rejection is not a stochastic p-value",
    )
    n5 = (
        "deterministic read not stochastic actualization", "periodic recurrence not physical reset",
        "XOR clear not permanent Record", "finite frequency not Born probability",
        "supplied bath genesis not spontaneous trial", "reduced diagonal not actual member",
        "empirical candidate surface not empirical result", "q-dependent compiler not derived law",
        "counter advance not physical time", "no route-specific wall promoted to constitutional evidence",
    )
    n6 = (
        "retain exact pointwise deterministic read", "retain exact Cycle531 occurrence composition",
        "retain bounded 326-M2 all24 circuit", "retain explicit periodic member strings",
        "retain p_hat quantization and correlation residuals", "retain inverse deletion and recurrence tests",
        "leave stochasticity independence reset permanence and Born open",
    )
    n7 = (
        "Construct an explicit bounded open-system comparator with a local entropy-export register and a law-owned reset map, specify the genesis measure and stochastic transition kernel independently of the Cycle531 read, and predeclare a train/held blinded likelihood test against actual member strings.  Require a finite-window mixing or renewal residual, capacity accounting for every exported bit, all24 covariance, inverse checks on the enlarged dilation, and a permanent readable medium before calling any output Record.  Compare its strings directly with this Cycle538 periodic table, Cycle536 coherent same-seed sectors, and Cycle534 period-five carrier; do not assume p=q or iid preparation."
    )
    n8 = (
        "Cycle243 event-before-Record boundary", "Cycles259/262/266 coherent occurrence candidates",
        "Cycle500 coherent cylinders", "Cycle505 binding without actual member",
        "Cycle508 supplied p=q and hidden-carrier routes", "Cycle531 exact conditional binder",
        "Cycle534 deterministic member ontology", "Cycle536 pure dilation and reduced diagonal",
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
            and len(n2) >= 7 and len(n3) >= 15 and len(n4) >= 7
            and len(n5) >= 10 and len(n6) >= 7 and len(n7) > 500 and len(n8) >= 8
        ),
    }


def inventory() -> dict:
    return {
        "supplied": (
            "exact Cycle531 MEMBER/receipt/conditional occurrence interface and upstream binding",
            "operational preparation and grade vector q",
            "largest-remainder q-to-125-count compiler and contiguous partition convention",
            "deterministic pointwise bath-member read ontology",
            "initial one-hot bath microstate, one-hot head, blank scratch, and admissible code constraints",
            "proper-cubic field action, static line chart, and three-site Toffoli primitive",
        ),
        "derived": (
            "fixed 125-state reversible bath and five-state head recurrence",
            "one unique member and receipt at every admitted bath microstate without host RNG or branch choice",
            "exact Cycle531 occurrence iff edge, binding, member, and receipt agree",
            "full-cycle p_hat counts within one bath quantum 1/125 of q",
            "explicit periodic bigram correlations and 250-step XOR echo return",
            "bounded support, inverse, leakage, deletion, routing, all24, and train/held controls",
        ),
        "open": (
            "derivation of the bath ontology, genesis microstate, q-to-partition law, or p=q",
            "probability measure over bath genesis and stochastic transition law",
            "fresh repeated-trial independence, mixing, entropy export, and irreversible reset",
            "single realized member without the supplied pointwise read ontology",
            "permanent Record, realized history, and readable non-erasing memory",
            "actual empirical member strings, blind key, likelihood, and Born calibration",
            "autonomous constraint preparation, two-site Toffoli compilation, source, gravity, energy, or physical time",
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "physical_time_derived": False,
        "energy_derived": False,
        "source_or_gravity_derived": False,
        "framework_Record": None,
        "realized_history": None,
        "Born_probability": None,
    }


def main() -> int:
    started = time.monotonic()
    print("CYCLE 538: DETERMINISTIC FINITE-BATH MEMBER-READ COMPARATOR")
    print("authority=none; audit=unset; pointwise supplied read; not stochastic/Born/Record")

    contract = contract_controls()
    composition = composition_controls()
    ontology = ontology_and_frequency_controls()
    recurrence = recurrence_independence_and_record_controls()
    rejection = blinded_rejection_controls()
    covariance = covariance_controls()
    deletions = deletion_and_domain_controls()
    routing = routing_resource_and_source_audit()
    nogo = no_go_controls()
    supplied_derived_open = inventory()

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "status": "constructive deterministic read comparator; stochastic/reset/Born/Record walls remain open",
        "contract": contract,
        "Cycle531_composition": composition,
        "read_ontology_frequency": ontology,
        "recurrence_independence_Record": recurrence,
        "blinded_candidate_rejection": rejection,
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
    check("the fixed bath read feeds exact Cycle531 occurrence on train and held fixtures", composition["pass"], composition)
    check("pointwise actual members remain firewalled from stochastic and Born meanings", ontology["pass"], ontology)
    check("closed recurrence exposes correlations, XOR erasure, and missing reset/independence", recurrence["pass"], recurrence)
    check("the deterministic law has a predeclared exact-word rejection surface", rejection["pass"], rejection)
    check("the same schedule is covariant under all 24 proper-cubic frames", covariance["pass"], covariance)
    check("member receipt binder echo advance and lawful-domain deletions are visible", deletions["pass"], deletions)
    check("the bounded 326-M2 schedule has exact NN routing/inverse and no host RNG", routing["pass"], routing)
    check("N1-N8 retains constructive closure without a shared no-go or axiom pressure", nogo["pass"], nogo)

    result["PASS"] = PASS
    result["FAIL"] = FAIL
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
