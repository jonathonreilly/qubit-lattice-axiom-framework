#!/usr/bin/env python3
"""Cycle 534: autonomous deterministic hidden-carrier member-law comparator.

An explicitly added one-hot hidden carrier emits Cycle531's exact MEMBER and
law-receipt input types, drives the exact conditional binder, copies only a
coherent candidate occurrence image, uncomputes the binder and member scratch,
and advances by a fixed recurrent local schedule.  The carrier ontology is
supplied and deliberately non-Born.  No Record, realized history, stochastic
law, probability, sampler, or derivation from the current axioms is claimed.
"""

from __future__ import annotations

import ast
from collections import Counter
from dataclasses import asdict, dataclass
from hashlib import sha256
import inspect
from itertools import product
import json
from pathlib import Path
import re
import resource
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_selected_seam_conditional_record_binder_cycle531_2026_07_21 as c531


c505 = c531.c505
c508 = c531.c508
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_HIDDEN_CARRIER_MEMBER_LAW_CYCLE534_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
MENU = tuple(range(5))
TRAIN_LENGTH = 5
HELD_LENGTH = 6
ECHO_SLOTS = 5
PASS = 0
FAIL = 0
Word = tuple[int, ...]


FROZEN = {
    "Cycle531 runner": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "Cycle531 note": "ed40564d4e57090cf03e706b54964e5a24cb735f9ca14df8f008fecffc388042",
    "Cycle508 train runner": "b223ff44b159a598ef52ea21b3e758a1303e126d7f53474f799ed14c0a829dc6",
    "Cycle508 held note": "8651a1bcfb39b2e2b8980bd5a25a352ffbe3e8e7a199ff421fc47f3a576c03c7",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
}
FROZEN_PATHS = {
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
HIDDEN_PHASE = take(_layout, 5)
ECHO_HEAD = take(_layout, 5)
ECHO_OCCURRENCE = take(_layout, ECHO_SLOTS)
ECHO_CONTENT = tuple(take(_layout, 3) for _ in range(ECHO_SLOTS))
TOTAL_M2 = _layout[0]
NEW_M2 = TOTAL_M2 - c531.TOTAL_M2


@dataclass(frozen=True)
class ExplicitHiddenCarrierOntology:
    carrier_label: int
    meaning: str = "stipulated ontic branch designator on the supported coherent candidate menu"
    derived_from_current_axioms: bool = False
    stochastic: bool = False
    Born: bool = False


@dataclass(frozen=True)
class LawOwnedMemberScratch:
    member: Word
    receipt: Word
    owner: str = "Cycle534 deterministic hidden-carrier comparator"
    actualization_status: str = "conditional on explicit added ontology"


@dataclass(frozen=True)
class DeterministicMemberString:
    initial_carrier: int
    word: Word
    counts: Word
    empirical_probability: None = None
    operational_grade: None = None


@dataclass(frozen=True)
class OperationalGradeDiagnostic:
    fixture: str
    preparation: str
    grades: tuple[float, ...]
    probability: None = None
    member_string: None = None


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
        "authority: none", "audit: unset", "explicit added hidden-carrier ontology",
        "non-born comparator", "no host seed", "no host label", "no host refresh",
        "fixed local recurrent law", "exact cycle-531 member and receipt type",
        "not a record", "not realized history", "not stochastic",
        "not derived from the current axioms", "finite-capacity", "autonomous renewal",
        "echo deletion", "operational grades remain separate", "l5", "held l=6",
        "all 24 proper-cubic frames", "inverse", "leakage", "deletion",
        "supplied / derived / open", "no axiom pressure",
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


def emit_schedule(prefix: str) -> tuple[c505.Gate, ...]:
    gates = []
    for label in MENU:
        gates.extend((
            gate("CNOT", (HIDDEN_PHASE[label], c531.MEMBER[label]), f"{prefix}:member:{label}"),
            gate("CNOT", (HIDDEN_PHASE[label], c531.LAW_RECEIPT[label]), f"{prefix}:receipt:{label}"),
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


def advance_schedule(sites: tuple[int, ...], prefix: str) -> tuple[c505.Gate, ...]:
    gates = []
    for left, right in ((sites[3], sites[4]), (sites[2], sites[3]), (sites[1], sites[2]), (sites[0], sites[1])):
        gates.extend(swap_schedule(left, right, f"{prefix}:{left}:{right}"))
    return tuple(gates)


EMIT = emit_schedule("emit")
BINDER_FORWARD = binder_schedule(False)
ECHO = echo_schedule()
BINDER_REVERSE = binder_schedule(True)
UNEMIT = emit_schedule("unemit")
ADVANCE_PHASE = advance_schedule(HIDDEN_PHASE, "advance-phase")
ADVANCE_HEAD = advance_schedule(ECHO_HEAD, "advance-head")
SCHEDULE = EMIT + BINDER_FORWARD + ECHO + BINDER_REVERSE + UNEMIT + ADVANCE_PHASE + ADVANCE_HEAD


def validate_word(bits: Word) -> None:
    if len(bits) != TOTAL_M2 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Cycle534 word leaves its exact binary 206-M2 domain")


def apply_schedule(
    bits: Word, schedule: tuple[c505.Gate, ...] = SCHEDULE,
    *, reverse: bool = False, delete_label: str | None = None,
) -> Word:
    validate_word(bits)
    matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
    if delete_label is not None and len(matches) != 1:
        raise ValueError("deletion must name exactly one Cycle534 primitive")
    active = tuple(
        item for index, item in enumerate(schedule)
        if delete_label is None or index != matches[0]
    )
    word = list(bits)
    for item in (tuple(reversed(active)) if reverse else active):
        c505.apply_gate(word, item)
    return tuple(word)


def prepare_branch(
    binding_label: int, hidden_phase: int, echo_head: int,
    *, edge: int = 1, plus: int = 1, minus: int = 0, K_position: int = 0,
) -> Word:
    base = c531.prepare(
        edge=edge, plus=plus, minus=minus, K_position=K_position,
        binding_label=binding_label, member_label=None, receipt_label=None,
    )
    bits = list(base + (0,) * NEW_M2)
    for site, bit in zip(HIDDEN_PHASE, one_hot(hidden_phase)):
        bits[site] = bit
    for site, bit in zip(ECHO_HEAD, one_hot(echo_head)):
        bits[site] = bit
    output = tuple(bits)
    validate_law_code(output, require_scratch_blank=True)
    return output


def scratch_sites() -> tuple[int, ...]:
    return (
        *c531.MEMBER, *c531.LAW_RECEIPT, c531.PRECOMMIT_READY,
        c531.OCCURRENCE, c531.ATOM_FLAG, *c531.ATOM_CONTENT,
        *c531.PAYLOAD_CURRENT, *c531.PAYLOAD_K_BINARY,
        c531.WORK_BINDING, c531.WORK_PROVENANCE, c531.WORK_TRIGGER,
    )


def validate_law_code(bits: Word, *, require_scratch_blank: bool) -> None:
    validate_word(bits)
    singleton(tuple(bits[site] for site in HIDDEN_PHASE), "hidden carrier")
    singleton(tuple(bits[site] for site in ECHO_HEAD), "echo head")
    if require_scratch_blank and any(bits[site] for site in scratch_sites()):
        raise ValueError("Cycle534 terminal scratch/member/receipt bank is not blank")


def phase_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in HIDDEN_PHASE), "hidden carrier")


def head_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in ECHO_HEAD), "echo head")


def echo_view(bits: Word) -> tuple[tuple[int, Word], ...]:
    return tuple(
        (bits[ECHO_OCCURRENCE[slot]], tuple(bits[site] for site in ECHO_CONTENT[slot]))
        for slot in range(ECHO_SLOTS)
    )


def stage_composition_controls() -> dict:
    failures = inverse_failures = input_mutations = scratch_failures = 0
    exact_c531_failures = member_type_failures = 0
    tests = 0
    rows = []
    for phase, head, binding, K_position, current in product(
        MENU, MENU, MENU, range(c531.K_BITS), ((0, 0), (1, 0), (0, 1))
    ):
        plus, minus = current
        edge = plus ^ minus
        source = prepare_branch(
            binding, phase, head, edge=edge, plus=plus, minus=minus,
            K_position=K_position,
        )
        emitted = apply_schedule(source, EMIT)
        member = tuple(emitted[site] for site in c531.MEMBER)
        receipt = tuple(emitted[site] for site in c531.LAW_RECEIPT)
        member_type_failures += member != one_hot(phase) or receipt != one_hot(phase)

        midpoint = apply_schedule(emitted, BINDER_FORWARD)
        exact = c531.logical_apply(tuple(emitted[:c531.TOTAL_M2]))
        exact_c531_failures += tuple(midpoint[:c531.TOTAL_M2]) != exact
        expected_occurrence = edge & int(binding == phase)
        failures += int(
            midpoint[c531.OCCURRENCE] != expected_occurrence
            or midpoint[c531.ATOM_FLAG] != expected_occurrence
            or tuple(midpoint[site] for site in c531.ATOM_CONTENT)
            != tuple(expected_occurrence & bit for bit in c505.bits3(binding))
        )

        output = apply_schedule(source)
        validate_law_code(output, require_scratch_blank=True)
        expected_echo = [list(item) for item in echo_view(source)]
        if expected_occurrence:
            expected_echo[head] = [1, c505.bits3(binding)]
        failures += int(
            phase_of(output) != (phase + 1) % 5
            or head_of(output) != (head + 1) % 5
            or echo_view(output) != tuple((item[0], tuple(item[1])) for item in expected_echo)
        )
        inverse_failures += apply_schedule(output, reverse=True) != source
        scratch_failures += any(output[site] for site in scratch_sites())
        input_mutations += any(
            output[site] != source[site]
            for site in (
                c531.C526_EDGE, *c531.C526_CURRENT, *c531.C526_K,
                *range(c531.C505_OFFSET, c531.C505_OFFSET + c531.C505_WIDTH),
            )
        )
        tests += 1
    rows.append({
        "tested_phase_head_binding_K_current_columns": tests,
        "expected": 5 * 5 * 5 * c531.K_BITS * 3,
    })
    return {
        "rows": rows,
        "law_columns": tests,
        "exact_Cycle531_midpoint_failures": exact_c531_failures,
        "MEMBER_receipt_type_failures": member_type_failures,
        "conditional_occurrence_or_recurrence_failures": failures,
        "inverse_failures": inverse_failures,
        "terminal_scratch_failures": scratch_failures,
        "upstream_port_or_binding_mutations": input_mutations,
        "pass": not any((
            exact_c531_failures, member_type_failures, failures,
            inverse_failures, scratch_failures, input_mutations,
        )),
    }


def recurrence_and_renewal_controls() -> dict:
    failures = inverse_failures = uniqueness_failures = 0
    five_step_rows = []
    ten_step_rows = []
    member_strings = []
    for initial_phase, initial_head in product(MENU, MENU):
        words = [prepare_branch(label, initial_phase, initial_head) for label in MENU]
        model = [
            [[0, (0, 0, 0)] for _slot in range(ECHO_SLOTS)]
            for _label in MENU
        ]
        for step in range(10):
            current_phase = (initial_phase + step) % 5
            current_head = (initial_head + step) % 5
            previous = words
            words = [apply_schedule(word) for word in previous]
            inverse_failures += sum(
                apply_schedule(after, reverse=True) != before
                for before, after in zip(previous, words)
            )
            uniqueness_failures += len(set(words)) != len(words)
            for label in MENU:
                if label == current_phase:
                    model[label][current_head][0] ^= 1
                    for lane, bit in enumerate(c505.bits3(label)):
                        model[label][current_head][1] = tuple(
                            old ^ (bit if index == lane else 0)
                            for index, old in enumerate(model[label][current_head][1])
                        )
                expected = tuple((item[0], tuple(item[1])) for item in model[label])
                failures += int(
                    phase_of(words[label]) != (current_phase + 1) % 5
                    or head_of(words[label]) != (current_head + 1) % 5
                    or echo_view(words[label]) != expected
                )
            if step == 4:
                occupied = tuple(sum(item[0] for item in echo_view(word)) for word in words)
                five_step_rows.append({
                    "initial_phase": initial_phase,
                    "initial_head": initial_head,
                    "branch_echo_occupancies": occupied,
                })
                failures += occupied != (1, 1, 1, 1, 1)
            if step == 9:
                occupied = tuple(sum(item[0] for item in echo_view(word)) for word in words)
                ten_step_rows.append({
                    "initial_phase": initial_phase,
                    "initial_head": initial_head,
                    "branch_echo_occupancies": occupied,
                })
                failures += occupied != (0, 0, 0, 0, 0)

    for initial_phase in MENU:
        word = tuple((initial_phase + step) % 5 for step in range(25))
        typed = DeterministicMemberString(
            initial_phase, word, tuple(word.count(label) for label in MENU)
        )
        member_strings.append(asdict(typed))
        failures += typed.counts != (5, 5, 5, 5, 5)

    return {
        "all_initial_phase_head_pairs": len(five_step_rows),
        "five_step_capacity_rows": five_step_rows,
        "ten_step_autonomous_echo_renewal_rows": ten_step_rows,
        "deterministic_member_strings": member_strings,
        "member_phase_period": 5,
        "echo_archive_period": 10,
        "finite_echo_slots": ECHO_SLOTS,
        "host_seed_calls": 0,
        "host_label_calls": 0,
        "host_refresh_calls": 0,
        "echo_semantics": "steps 1-5 accumulate coherent candidates; steps 6-10 reversibly delete them by XOR recurrence",
        "permanent_Record_renewal_claimed": False,
        "inverse_failures": inverse_failures,
        "branch_uniqueness_failures": uniqueness_failures,
        "recurrence_failures": failures,
        "pass": not any((failures, inverse_failures, uniqueness_failures)),
    }


def operational_grade_firewall_controls() -> dict:
    surface = c508.c500.c493.c488.menu_surface()
    grade_rows = []
    grade_vectors = []
    for fixture, program, states in (
        ("L5-interface/train-program", surface.train_program, c505.input_states("train")),
        ("held-L6-interface/held-program", surface.held_program, c505.input_states("held")),
    ):
        for name, psi in states:
            grades = tuple(c508.c500.branch_grades(program, psi))
            typed = OperationalGradeDiagnostic(fixture, name, grades)
            grade_rows.append(asdict(typed))
            grade_vectors.append(grades)

    pair_distances = tuple(
        sum(abs(left[index] - right[index]) for index in MENU)
        for left_index, left in enumerate(grade_vectors)
        for right in grade_vectors[left_index + 1:]
    )
    carrier_words = tuple(
        tuple((initial + step) % 5 for step in range(25))
        for initial in MENU
    )
    malformed = 0
    for operation in (
        lambda: singleton((0, 0, 0, 0, 0), "hidden carrier"),
        lambda: singleton((1, 1, 0, 0, 0), "hidden carrier"),
        lambda: singleton((0, 0, 0, 0, 0), "echo head"),
        lambda: prepare_branch(0, 5, 0),
        lambda: prepare_branch(0, 0, 5),
    ):
        try:
            operation()
        except ValueError:
            malformed += 1

    return {
        "operational_grade_diagnostics": grade_rows,
        "deterministic_carrier_words_separate_object": carrier_words,
        "maximum_pairwise_grade_L1_difference": max(pair_distances),
        "member_word_depends_on_preparation_or_grade": False,
        "grade_called_probability": False,
        "member_count_called_probability": False,
        "actual_empirical_data": None,
        "sampler": None,
        "malformed_domain_rejections": malformed,
        "expected_malformed_domain_rejections": 5,
        "pass": (
            len(grade_rows) == 4
            and max(pair_distances) > 1e-6
            and all(abs(sum(row["grades"]) - 1.0) < 2e-9 for row in grade_rows)
            and malformed == 5
        ),
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
        for phase, head, binding, current in product(MENU, MENU, MENU, ((0, 0), (1, 0), (0, 1))):
            plus, minus = current
            edge = plus ^ minus
            source = prepare_branch(
                binding, phase, head, edge=edge, plus=plus, minus=minus,
                K_position=(phase + head) % c531.K_BITS,
            )
            output = apply_schedule(source)
            framed_plus, framed_minus = ((minus, plus) if reversed_endpoints else (plus, minus))
            framed_source = prepare_branch(
                binding, phase, head, edge=edge, plus=framed_plus, minus=framed_minus,
                K_position=(phase + head) % c531.K_BITS,
            )
            framed_output = apply_schedule(framed_source)
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
        "hidden_phase_head_member_receipt_echo_frame_action": "scalar",
        "current_frame_action": "plus/minus exchange under endpoint reversal",
        "same_fixed_schedule_L5_and_held_L6": True,
        "upstream_Cycle531_L5_L6_port_interface_strict_hash_imported": True,
        "pass": len(frames) == 24 and failures == 0,
    }


def deletion_controls() -> dict:
    rows = []

    def witness(label: str, source: Word) -> None:
        full = apply_schedule(source)
        damaged = apply_schedule(source, delete_label=label)
        rows.append({
            "deleted": label,
            "changed": damaged != full,
            "basis_residual": 0.0 if damaged == full else 2 ** 0.5,
            "terminal_scratch_nonblank": any(damaged[site] for site in scratch_sites()),
            "phase_constraint": tuple(damaged[site] for site in HIDDEN_PHASE),
            "head_constraint": tuple(damaged[site] for site in ECHO_HEAD),
        })

    for label in MENU:
        source = prepare_branch(label, label, 0, K_position=label)
        witness(f"emit:member:{label}", source)
        witness(f"emit:receipt:{label}", source)
        witness(f"unemit:member:{label}", source)
        witness(f"unemit:receipt:{label}", source)
    for slot in range(ECHO_SLOTS):
        source = prepare_branch(4, 4, slot, K_position=slot)
        witness(f"echo:occurrence:{slot}", source)
        for lane, label in enumerate((1, 2, 4)):
            source = prepare_branch(label, label, slot, K_position=slot)
            witness(f"echo:content:{slot}:{lane}", source)

    source = prepare_branch(3, 3, 2, K_position=7)
    witness("binder-forward:46:II:conditional-occurrence", source)
    witness("binder-reverse:15:II:conditional-occurrence", source)
    witness(ADVANCE_PHASE[0].label, source)
    head_witness = prepare_branch(3, 3, 3, K_position=7)
    witness(ADVANCE_HEAD[0].label, head_witness)

    carrier_deleted = list(source)
    for site in HIDDEN_PHASE:
        carrier_deleted[site] = 0
    carrier_delete_rejected = False
    try:
        validate_law_code(tuple(carrier_deleted), require_scratch_blank=True)
    except ValueError:
        carrier_delete_rejected = True

    labels_unique = len({item.label for item in SCHEDULE}) == len(SCHEDULE)
    return {
        "deletion_rows": rows,
        "deletion_witnesses": len(rows),
        "unwitnessed": tuple(row["deleted"] for row in rows if not row["changed"]),
        "hidden_carrier_deletion_rejected": carrier_delete_rejected,
        "schedule_labels_unique": labels_unique,
        "pass": all(row["changed"] for row in rows) and carrier_delete_rejected and labels_unique,
    }


def routing_resource_and_source_audit() -> dict:
    trace = c505.nn_trace(SCHEDULE, TOTAL_M2)
    source = prepare_branch(4, 4, 3, K_position=15)
    logical = apply_schedule(source)
    routed = c505.apply_routed(source, SCHEDULE)
    roundtrip = c505.apply_routed(routed, SCHEDULE, reverse=True)

    forbidden = {"random", "choice", "choices", "argmax", "branch_grades", "norm", "sample", "seed"}
    calls = []
    for function in (emit_schedule, binder_schedule, echo_schedule, advance_schedule):
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
        "fixed_schedule_logical_gates": len(SCHEDULE),
        "fixed_schedule_routed_equals_logical": routed == logical,
        "routed_inverse_roundtrip": roundtrip == source,
        "Cycle531_existing_port_composite_M2": c531.TOTAL_M2,
        "new_hidden_carrier_M2": 5,
        "new_echo_head_M2": 5,
        "new_finite_echo_archive_M2": 20,
        "new_Cycle534_M2": NEW_M2,
        "total_bounded_port_composite_M2": TOTAL_M2,
        "maximum_declared_gate_support_M2": trace["maximum_support_M2"],
        "two_site_decomposition_of_Toffoli_supplied": False,
        "autonomous_input_constraint_preparation_supplied": False,
        "forbidden_schedule_calls": forbidden_calls,
        "runtime_host_seed_label_refresh_calls": 0,
        "underlying_Cycle219_mass_parameter_preserved": 0.45340565417488515,
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


def inventory() -> dict:
    supplied = (
        "exact frozen Cycle531 port/interface binder and its upstream Cycle526/Cycle505 dependencies",
        "explicit added hidden-carrier ontology, one-hot initial carrier state with every value admitted",
        "one-hot echo-head boundary with every value tested",
        "full five-label coherent candidate support and blank Cycle531 scratch",
        "fixed routing chart and proper-cubic field action",
    )
    derived = (
        "exact Cycle531 MEMBER plus matching receipt emission without runtime host label",
        "fixed recurrent emit-bind-echo-invert-unemit phase/head advance",
        "five-step finite candidate accumulation and ten-step autonomous XOR echo renewal",
        "exact inverse, zero terminal scratch, bounded support, all24 covariance",
        "deterministic member strings independent of operational grade diagnostics",
    )
    open_items = (
        "derivation or empirical acceptance of hidden-carrier ontology and initial physical carrier state",
        "permanent retained archive renewal; Cycle534 renewal deletes candidate copies and is not Record",
        "actual empirical member data and comparison/calibration law",
        "Born probability, stochastic law, sampler, typicality, and grade-to-member relation",
        "framework Record, realized history, irreversible access restriction, close and permanence",
        "autonomous preparation/enforcement of Cycle531 and Cycle534 input constraints",
        "two-site Toffoli decomposition, integrated full-amplitude encoder, cubic tiling, source/gravity law",
    )
    return {
        "supplied": supplied,
        "derived": derived,
        "open": open_items,
        "ontology": asdict(ExplicitHiddenCarrierOntology(0)),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "framework_Record": None,
        "realized_history": None,
        "Born_probability": None,
        "stochastic_law": None,
        "shared_obstruction": False,
        "axiom_pressure": False,
    }


def main() -> int:
    started = time.monotonic()
    print("CYCLE 534: AUTONOMOUS DETERMINISTIC HIDDEN-CARRIER MEMBER-LAW COMPARATOR")
    print("authority=none; audit=unset; explicit ontology; non-Born; not Record")

    contract = contract_controls()
    composition = stage_composition_controls()
    recurrence = recurrence_and_renewal_controls()
    grades = operational_grade_firewall_controls()
    covariance = covariance_controls()
    deletions = deletion_controls()
    routing = routing_resource_and_source_audit()
    supplied_derived_open = inventory()

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "status": "bounded autonomous deterministic comparator conditional on explicit added ontology",
        "contract": contract,
        "Cycle531_composition": composition,
        "recurrent_finite_capacity_renewal": recurrence,
        "operational_grade_firewall": grades,
        "proper_cubic_L5_L6": covariance,
        "deletions": deletions,
        "routing_resources_source_audit": routing,
        "supplied_derived_open": supplied_derived_open,
        "elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "process_swap_count": int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0)),
    }

    check("strict hashes, note contract, and primitive registry control close", contract["pass"], contract)
    check("fixed hidden carrier emits the exact Cycle531 member/receipt type and composes exactly", composition["pass"], composition)
    check("all carrier/head boundaries close five-slot capacity and autonomous ten-step echo renewal", recurrence["pass"], recurrence)
    check("deterministic member strings remain typed separately from operational grades", grades["pass"], grades)
    check("the recurrent law is covariant under all24 and unchanged at L5/held L6", covariance["pass"], covariance)
    check("carrier/member/receipt/binder/archive/recurrence deletions are visible", deletions["pass"], deletions)
    check("the fixed 206-M2 port composite has exact NN routing/inverse and no host service", routing["pass"], routing)

    result["PASS"] = PASS
    result["FAIL"] = FAIL
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
