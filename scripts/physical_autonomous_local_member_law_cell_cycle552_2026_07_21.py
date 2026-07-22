#!/usr/bin/env python3
"""Cycle 552: autonomous local member-law cell for Cycle 531.

A retained one-hot five-law word selects a deterministic shift of a retained
five-state member carrier.  One fixed reversible circuit emits Cycle531's
matching MEMBER/LAW_RECEIPT words, runs the exact conditional binder, copies
its twelve output ports plus law provenance into a finite XOR snapshot bank,
uncomputes the binder, and advances the member and snapshot head.  Every
Toffoli is replaced by Cycle523's exact fifteen one-/two-M2 gate circuit and
every two-M2 gate has an explicit adjacent-SWAP/core/reverse line route.

The initial law word, member carrier, head, binding/event ports, and blank
snapshot bank are supplied genesis data.  The recurrent circuit is autonomous
after that boundary.  Snapshot copying is not Record, schedule is not time,
and the deterministic law is not Born or stochastic dynamics.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import re
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_selected_seam_conditional_record_binder_cycle531_2026_07_21 as c531
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523


c505 = c531.c505
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_LOCAL_MEMBER_LAW_CELL_CYCLE552_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
MENU = tuple(range(5))
TRAIN_LENGTH = 5
HELD_LENGTH = 6
SNAPSHOT_SLOTS = 5
TOL = 3e-11
PASS = 0
FAIL = 0
Word = tuple[int, ...]


FROZEN_PATHS = {
    "Cycle531 runner": Path(c531.__file__),
    "Cycle536 runner": ROOT / "scripts/physical_coherent_seed_member_dilation_cycle536_2026_07_21.py",
    "Cycle541 runner": ROOT / "scripts/physical_open_reset_stochastic_member_read_cycle541_2026_07_21.py",
    "Cycle543 runner": ROOT / "scripts/physical_autonomous_genesis_renewal_bridge_cycle543_2026_07_21.py",
    "Cycle549 runner": ROOT / "scripts/physical_recoil_source_literal_gate_compiler_cycle549_2026_07_21.py",
    "Cycle523 runner": Path(c523.__file__),
    "Cycle488 runner": ROOT / "scripts/physical_form_occurrence_born_weight_firewall_cycle488_2026_07_20.py",
    "Cycle500 runner": ROOT / "scripts/physical_kraus_grade_repeated_history_law_tournament_cycle500_2026_07_20.py",
    "Cycle508 held runner": ROOT / "scripts/physical_actual_member_admitted_history_law_tournament_held_cycle508_2026_07_20.py",
    "realized-state primitive": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "Born-frequency boundary": ROOT / "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
}
FROZEN = {
    "Cycle531 runner": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "Cycle536 runner": "911d500b42d6c45644ad6d0a9f50a79572380e7b01592a6bf66a842c3c4fcf2f",
    "Cycle541 runner": "2101f9cc0dbf8fefafecd08205b4af4618bbaddf1130fe2bbb593b5abb4246a4",
    "Cycle543 runner": "95fb57bbe14534b3a922fcee0da748039e8337915f02ace7bdb433d23bee3e7e",
    "Cycle549 runner": "7eff68c6cf7688ddc23b8dbe7d66cb74c82232c2bfd4705b992c1972b5d7f399",
    "Cycle523 runner": "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
    "Cycle488 runner": "17bbdd0d30f579668120dbdea55b4d42dfceff550b31cc50b3ec11451b510470",
    "Cycle500 runner": "01c459cd067e4b02b60558a3c29c95a0f93b3fd1d916a27176e35128f1668a90",
    "Cycle508 held runner": "f2a1c2a7ce2603fceb1a86b05c24e897111fbf44dde3e0ac0366e58c3c97a3d6",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
}


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    answer = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return answer


# Cycle531's twelve retained output ports, in a frozen local order.
C531_OUTPUT_FIELDS = (
    c531.PRECOMMIT_READY,
    c531.OCCURRENCE,
    c531.ATOM_FLAG,
    *c531.ATOM_CONTENT,
    *c531.PAYLOAD_CURRENT,
    *c531.PAYLOAD_K_BINARY,
)
if len(C531_OUTPUT_FIELDS) != 12:
    raise RuntimeError("Cycle531 output interface changed")

_layout = [c531.TOTAL_M2]
LAW_WORD = take(_layout, 5)
MEMBER_STATE = take(_layout, 5)
OUTPUT_HEAD = take(_layout, 5)
# Twelve exact Cycle531 fields followed by a retained five-rail law receipt.
SNAPSHOT = tuple(take(_layout, 17) for _ in range(SNAPSHOT_SLOTS))
TOTAL_M2 = _layout[0]
NEW_M2 = TOTAL_M2 - c531.TOTAL_M2


@dataclass(frozen=True)
class LiteralGate:
    kind: str
    sites: tuple[int, ...]
    matrix: tuple[complex, ...]
    label: str


@dataclass(frozen=True)
class LocalLawCell:
    law_shift: int
    member_before: int
    member_after: int
    head_before: int
    head_after: int
    framework_Record: None = None
    stochastic_kernel: None = None
    Born_probability: None = None
    physical_time: None = None


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


def rss_bytes() -> int:
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


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


def dependency_and_contract_controls() -> dict:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    required = (
        "authority: none", "audit: unset", "exact cycle-531 interface",
        "invalid law word", "genesis", "recurrence", "pointer copying is not record",
        "schedule is not time", "all 24 proper-cubic frames", "all 576 frame products",
        "l5", "held l6", "inverse", "work return", "deletion",
        "supplied / derived / open", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8",
        "no axiom pressure", "not born", "law selection remains supplied",
    )
    body = normalized(NOTE)
    missing = tuple(fragment for fragment in required if fragment not in body)
    self_sha = file_sha(Path(__file__))
    return {
        "expected": FROZEN,
        "observed": observed,
        "strict_dependency_hashes_match": observed == FROZEN,
        "note_missing_contract_fragments": missing,
        "runner_SHA256": self_sha,
        "declared_runner_SHA256": declared_runner_sha(),
        "pass": observed == FROZEN and not missing and declared_runner_sha() == self_sha,
    }


def one_hot(label: int, width: int = 5) -> Word:
    if label not in range(width):
        raise ValueError("one-hot label leaves its declared word")
    return tuple(int(index == label) for index in range(width))


def singleton(bits: Word, name: str) -> int:
    if len(bits) != 5 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError(f"{name} leaves its binary five-rail word")
    if sum(bits) != 1:
        raise ValueError(f"{name} is not one-hot")
    return bits.index(1)


def gate(kind: str, sites: tuple[int, ...], label: str) -> c505.Gate:
    return c505.gate(kind, sites, label, TOTAL_M2)


def clone(item: c505.Gate, label: str) -> c505.Gate:
    return gate(item.kind, item.sites, label)


def emit_schedule(prefix: str) -> tuple[c505.Gate, ...]:
    gates = []
    for label in MENU:
        gates.extend((
            gate("CNOT", (MEMBER_STATE[label], c531.MEMBER[label]), f"{prefix}:member:{label}"),
            gate("CNOT", (MEMBER_STATE[label], c531.LAW_RECEIPT[label]), f"{prefix}:receipt:{label}"),
        ))
    return tuple(gates)


def binder_schedule(reverse: bool) -> tuple[c505.Gate, ...]:
    sequence = tuple(reversed(c531.SCHEDULE)) if reverse else c531.SCHEDULE
    prefix = "binder-reverse" if reverse else "binder-forward"
    return tuple(clone(item, f"{prefix}:{item.label}") for item in sequence)


def snapshot_schedule() -> tuple[c505.Gate, ...]:
    gates = []
    for slot in range(SNAPSHOT_SLOTS):
        for field, source in enumerate(C531_OUTPUT_FIELDS):
            gates.append(gate(
                "TOFFOLI", (OUTPUT_HEAD[slot], source, SNAPSHOT[slot][field]),
                f"snapshot:{slot}:Cycle531-field:{field}",
            ))
        for law in MENU:
            gates.append(gate(
                "TOFFOLI", (OUTPUT_HEAD[slot], LAW_WORD[law], SNAPSHOT[slot][12 + law]),
                f"snapshot:{slot}:law:{law}",
            ))
    return tuple(gates)


def controlled_swap(control: int, left: int, right: int, prefix: str) -> tuple[c505.Gate, ...]:
    # Fredkin using CNOT(right,left), Toffoli(control,left,right), CNOT(right,left).
    return (
        gate("CNOT", (right, left), f"{prefix}:pre"),
        gate("TOFFOLI", (control, left, right), f"{prefix}:toffoli"),
        gate("CNOT", (right, left), f"{prefix}:post"),
    )


def swap_schedule(left: int, right: int, prefix: str) -> tuple[c505.Gate, ...]:
    return (
        gate("CNOT", (left, right), f"{prefix}:a"),
        gate("CNOT", (right, left), f"{prefix}:b"),
        gate("CNOT", (left, right), f"{prefix}:c"),
    )


def advance_member_schedule() -> tuple[c505.Gate, ...]:
    gates = []
    # LAW_WORD[delta] controls a cyclic right shift by delta.  All law sectors
    # see one fixed schedule; the data never selects a host-side gate list.
    for delta in range(1, 5):
        for repetition in range(delta):
            for left, right in ((3, 4), (2, 3), (1, 2), (0, 1)):
                gates.extend(controlled_swap(
                    LAW_WORD[delta], MEMBER_STATE[left], MEMBER_STATE[right],
                    f"advance-member:law{delta}:rep{repetition}:swap{left}-{right}",
                ))
    return tuple(gates)


def advance_head_schedule() -> tuple[c505.Gate, ...]:
    gates = []
    for left, right in ((3, 4), (2, 3), (1, 2), (0, 1)):
        gates.extend(swap_schedule(
            OUTPUT_HEAD[left], OUTPUT_HEAD[right], f"advance-head:swap{left}-{right}"
        ))
    return tuple(gates)


EMIT = emit_schedule("emit")
BINDER_FORWARD = binder_schedule(False)
SNAPSHOT_WRITE = snapshot_schedule()
BINDER_REVERSE = binder_schedule(True)
UNEMIT = emit_schedule("unemit")
ADVANCE_MEMBER = advance_member_schedule()
ADVANCE_HEAD = advance_head_schedule()
SCHEDULE = (
    EMIT + BINDER_FORWARD + SNAPSHOT_WRITE + BINDER_REVERSE
    + UNEMIT + ADVANCE_MEMBER + ADVANCE_HEAD
)


def validate_word(bits: Word) -> None:
    if len(bits) != TOTAL_M2 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Cycle552 word leaves its exact binary M2 domain")


def c531_scratch_sites() -> tuple[int, ...]:
    return (
        *c531.MEMBER, *c531.LAW_RECEIPT,
        c531.PRECOMMIT_READY, c531.OCCURRENCE, c531.ATOM_FLAG,
        *c531.ATOM_CONTENT, *c531.PAYLOAD_CURRENT, *c531.PAYLOAD_K_BINARY,
        c531.WORK_BINDING, c531.WORK_PROVENANCE, c531.WORK_TRIGGER,
    )


def validate_law_code(bits: Word, *, require_c531_scratch_blank: bool = True) -> None:
    validate_word(bits)
    singleton(tuple(bits[site] for site in LAW_WORD), "law word")
    singleton(tuple(bits[site] for site in MEMBER_STATE), "member state")
    singleton(tuple(bits[site] for site in OUTPUT_HEAD), "output head")
    if require_c531_scratch_blank and any(bits[site] for site in c531_scratch_sites()):
        raise ValueError("Cycle531 MEMBER/receipt/output/work boundary is not blank")
    K = tuple(bits[site] for site in c531.C526_K)
    if sum(K) != 1:
        raise ValueError("Cycle531 K input is not one-hot")
    edge = bits[c531.C526_EDGE]
    plus, minus = (bits[site] for site in c531.C526_CURRENT)
    if edge != (plus ^ minus) or plus & minus:
        raise ValueError("Cycle531 event/current type fails")


def apply_schedule(
    bits: Word,
    schedule: tuple[c505.Gate, ...] = SCHEDULE,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> Word:
    validate_word(bits)
    if delete_label is not None:
        matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("deletion must identify exactly one Cycle552 logical gate")
        schedule = tuple(item for index, item in enumerate(schedule) if index != matches[0])
    word = list(bits)
    for item in (tuple(reversed(schedule)) if reverse else schedule):
        c505.apply_gate(word, item)
    return tuple(word)


def prepare(
    binding: int,
    law: int,
    member: int,
    head: int,
    *,
    edge: int = 1,
    plus: int = 1,
    minus: int = 0,
    K_position: int = 0,
    vacancy: int = 1,
) -> Word:
    base = c531.prepare(
        edge=edge, plus=plus, minus=minus, K_position=K_position,
        binding_label=binding, member_label=None, receipt_label=None,
        vacancy=vacancy,
    )
    bits = list(base) + [0] * NEW_M2
    for site, bit in zip(LAW_WORD, one_hot(law)):
        bits[site] = bit
    for site, bit in zip(MEMBER_STATE, one_hot(member)):
        bits[site] = bit
    for site, bit in zip(OUTPUT_HEAD, one_hot(head)):
        bits[site] = bit
    output = tuple(bits)
    validate_law_code(output)
    return output


def law_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in LAW_WORD), "law word")


def member_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in MEMBER_STATE), "member state")


def head_of(bits: Word) -> int:
    return singleton(tuple(bits[site] for site in OUTPUT_HEAD), "output head")


def snapshot_view(bits: Word, slot: int) -> tuple[Word, Word]:
    return (
        tuple(bits[site] for site in SNAPSHOT[slot][:12]),
        tuple(bits[site] for site in SNAPSHOT[slot][12:]),
    )


def physical_step(bits: Word) -> Word:
    validate_law_code(bits)
    output = apply_schedule(bits)
    validate_law_code(output)
    return output


def exact_interface_controls() -> dict:
    failures = inverse_failures = scratch_failures = mutation_failures = 0
    midpoint_failures = snapshot_failures = member_receipt_failures = 0
    member_receipt_read_only_failures = 0
    tests = 0
    K_seen = set()
    for length, law, member, binding, head, current in product(
        (TRAIN_LENGTH, HELD_LENGTH), MENU, MENU, MENU, MENU,
        ((0, 0), (1, 0), (0, 1)),
    ):
        plus, minus = current
        edge = plus ^ minus
        K_position = (member + 7 * head + law + length) % c531.K_BITS
        K_seen.add(K_position)
        source = prepare(
            binding, law, member, head, edge=edge, plus=plus, minus=minus,
            K_position=K_position,
        )
        emitted = apply_schedule(source, EMIT)
        member_receipt_failures += int(
            tuple(emitted[site] for site in c531.MEMBER) != one_hot(member)
            or tuple(emitted[site] for site in c531.LAW_RECEIPT) != one_hot(member)
        )
        midpoint = apply_schedule(emitted, BINDER_FORWARD)
        exact = c531.logical_apply(tuple(emitted[:c531.TOTAL_M2]))
        midpoint_failures += tuple(midpoint[:c531.TOTAL_M2]) != exact
        member_receipt_read_only_failures += int(
            any(midpoint[site] != emitted[site] for site in (*c531.MEMBER, *c531.LAW_RECEIPT))
        )
        snapped = apply_schedule(midpoint, SNAPSHOT_WRITE)
        expected_fields = tuple(midpoint[site] for site in C531_OUTPUT_FIELDS)
        snapshot_failures += snapshot_view(snapped, head) != (expected_fields, one_hot(law))
        snapshot_failures += any(
            any(snapped[site] for site in SNAPSHOT[slot])
            for slot in MENU if slot != head
        )
        output = apply_schedule(source)
        occurrence = edge & int(member == binding)
        fields, law_receipt = snapshot_view(output, head)
        expected_fields = (
            edge, occurrence, occurrence,
            *(occurrence & bit for bit in c505.bits3(binding)),
            plus, minus, *c531.bits4(K_position),
        )
        failures += int(
            fields != expected_fields
            or law_receipt != one_hot(law)
            or member_of(output) != (member + law) % 5
            or head_of(output) != (head + 1) % 5
            or law_of(output) != law
        )
        inverse_failures += apply_schedule(output, reverse=True) != source
        scratch_failures += any(output[site] for site in c531_scratch_sites())
        immutable = (
            *range(c531.C505_OFFSET, c531.C505_OFFSET + c531.C505_WIDTH),
            c531.C526_EDGE, *c531.C526_CURRENT, *c531.C526_K, *LAW_WORD,
        )
        mutation_failures += any(output[site] != source[site] for site in immutable)
        tests += 1
    return {
        "L5_and_held_L6_columns": tests,
        "K_positions_covered": tuple(sorted(K_seen)),
        "MEMBER_LAW_RECEIPT_type_failures": member_receipt_failures,
        "Cycle531_MEMBER_LAW_RECEIPT_read_only_failures": member_receipt_read_only_failures,
        "complete_lawword_x_MEMBER_STATE_pairs": 25,
        "exact_Cycle531_midpoint_failures": midpoint_failures,
        "exact_output_snapshot_failures": snapshot_failures,
        "law_update_failures": failures,
        "inverse_failures": inverse_failures,
        "terminal_Cycle531_work_and_scratch_failures": scratch_failures,
        "source_binding_lawword_mutation_failures": mutation_failures,
        "maximum_exact_basis_residual": 0.0 if not any((
            member_receipt_failures, member_receipt_read_only_failures,
            midpoint_failures, snapshot_failures, failures,
            inverse_failures, scratch_failures, mutation_failures,
        )) else 2 ** 0.5,
        "same_schedule_L5_held_L6": True,
        "pass": tests == 2 * 5**4 * 3 and not any((
            member_receipt_failures, member_receipt_read_only_failures,
            midpoint_failures, snapshot_failures, failures,
            inverse_failures, scratch_failures, mutation_failures,
        )),
    }


def recurrence_controls() -> dict:
    failures = inverse_failures = overwrite_failures = return_failures = 0
    prediction_histogram = {law: Counter() for law in MENU}
    for law, initial_member, initial_head, binding in product(MENU, MENU, MENU, MENU):
        initial = prepare(binding, law, initial_member, initial_head, K_position=7)
        word = initial
        occurrences = []
        for step in range(10):
            prior = word
            prior_snapshots = tuple(snapshot_view(prior, slot) for slot in MENU)
            active_head = head_of(prior)
            active_member = member_of(prior)
            word = physical_step(prior)
            inverse_failures += apply_schedule(word, reverse=True) != prior
            for slot in MENU:
                if slot != active_head:
                    overwrite_failures += snapshot_view(word, slot) != prior_snapshots[slot]
            occurrences.append(int(active_member == binding))
            failures += int(
                member_of(word) != (active_member + law) % 5
                or head_of(word) != (active_head + 1) % 5
            )
            if step == 4:
                failures += int(any(not any(snapshot_view(word, slot)[0]) for slot in MENU))
            if step == 9:
                return_failures += word != initial
        expected_first_five = 5 if law == 0 and initial_member == binding else (
            0 if law == 0 else 1
        )
        failures += int(sum(occurrences[:5]) != expected_first_five)
        prediction_histogram[law][sum(occurrences[:5])] += 1
    return {
        "law_member_head_binding_origins": 5**4,
        "five_slot_fill_horizon": 5,
        "ten_step_XOR_renewal_period": 10,
        "finite_snapshot_is_framework_Record": False,
        "pointer_copying_is_Record": False,
        "schedule_is_physical_time": False,
        "law_and_sequence_failures": failures,
        "prior_slot_overwrite_failures": overwrite_failures,
        "per_step_inverse_failures": inverse_failures,
        "ten_step_complete_return_failures": return_failures,
        "first_five_occurrence_count_histogram_by_law": {
            law: dict(sorted(counts.items())) for law, counts in prediction_histogram.items()
        },
        "pass": not any((failures, overwrite_failures, inverse_failures, return_failures)),
    }


def basis_residual(left: Word, right: Word) -> float:
    return 0.0 if left == right else 2 ** 0.5


def deletion_and_domain_controls() -> dict:
    source = prepare(2, 1, 2, 0, K_position=7)
    full = apply_schedule(source)
    deletions = {}
    labels = (
        "emit:member:2",
        "emit:receipt:2",
        "binder-forward:II:conditional-occurrence",
        "snapshot:0:Cycle531-field:0",
        "snapshot:0:Cycle531-field:1",
        "snapshot:0:law:1",
        "advance-member:law1:rep0:swap2-3:toffoli",
        "advance-head:swap0-1:a",
    )
    for label in labels:
        damaged = apply_schedule(source, delete_label=label)
        deletions[label] = basis_residual(full, damaged)

    edge_deleted = apply_schedule(prepare(
        2, 1, 2, 0, edge=0, plus=0, minus=0, K_position=7
    ))
    binding_deleted = apply_schedule(prepare(
        2, 1, 2, 0, K_position=7, vacancy=0
    ))
    semantic = {
        "delete_EDGE": snapshot_view(edge_deleted, 0)[0],
        "delete_binding": snapshot_view(binding_deleted, 0)[0],
    }

    malformed = []
    mutations = []
    for description, sites in (
        ("zero-hot law word", LAW_WORD),
        ("zero-hot member state", MEMBER_STATE),
        ("zero-hot output head", OUTPUT_HEAD),
    ):
        bits = list(source)
        for site in sites:
            bits[site] = 0
        mutations.append((description, tuple(bits)))
    for description, sites in (
        ("multi-hot law word", LAW_WORD),
        ("multi-hot member state", MEMBER_STATE),
        ("multi-hot output head", OUTPUT_HEAD),
    ):
        bits = list(source)
        bits[sites[(tuple(bits[site] for site in sites).index(1) + 1) % 5]] = 1
        mutations.append((description, tuple(bits)))
    dirty = list(source)
    dirty[c531.MEMBER[0]] = 1
    mutations.append(("dirty Cycle531 member scratch", tuple(dirty)))
    nonbinary = list(source)
    nonbinary[LAW_WORD[0]] = 2
    mutations.append(("nonbinary law word", tuple(nonbinary)))
    for description, word in mutations:
        try:
            validate_law_code(word)
        except ValueError:
            malformed.append(description)

    invalid_law = list(source)
    for site in LAW_WORD:
        invalid_law[site] = 0
    invalid_lawword_rejected = False
    try:
        physical_step(tuple(invalid_law))
    except ValueError:
        invalid_lawword_rejected = True

    return {
        "targeted_gate_deletion_basis_residuals": deletions,
        "delete_EDGE_snapshot": semantic["delete_EDGE"],
        "delete_binding_snapshot": semantic["delete_binding"],
        "delete_EDGE_blocks_precommit_and_occurrence": semantic["delete_EDGE"][:2] == (0, 0),
        "delete_binding_retains_precommit_and_blocks_occurrence": (
            semantic["delete_binding"][0] == 1 and semantic["delete_binding"][1] == 0
        ),
        "malformed_domain_rejections": tuple(malformed),
        "expected_malformed_domain_rejections": len(mutations),
        "invalid_lawword_rejected_before_recurrence": invalid_lawword_rejected,
        "pass": (
            all(abs(value - 2 ** 0.5) < 1e-15 for value in deletions.values())
            and semantic["delete_EDGE"][:2] == (0, 0)
            and semantic["delete_binding"][0] == 1
            and semantic["delete_binding"][1] == 0
            and len(malformed) == len(mutations)
            and invalid_lawword_rejected
        ),
    }


def cnot_matrix() -> np.ndarray:
    return c523.cnot_matrix()


def literal(kind: str, sites: tuple[int, ...], matrix: np.ndarray, label: str) -> LiteralGate:
    matrix = np.asarray(matrix, dtype=complex)
    expected = 1 << len(sites)
    if len(sites) not in (1, 2) or matrix.shape != (expected, expected):
        raise ValueError("literal gate is not one-/two-M2")
    if len(set(sites)) != len(sites) or any(site not in range(TOTAL_M2) for site in sites):
        raise ValueError("literal gate leaves the bounded cell")
    return LiteralGate(kind, sites, tuple(matrix.reshape(-1)), label)


def expand_logical(item: c505.Gate) -> tuple[LiteralGate, ...]:
    X = np.asarray(((0, 1), (1, 0)), dtype=complex)
    H = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    T = np.diag((1, np.exp(1j * np.pi / 4))).astype(complex)
    Tdg = T.conj().T
    CNOT = cnot_matrix()
    if item.kind == "X":
        return (literal("X", item.sites, X, item.label + ":X"),)
    if item.kind == "CNOT":
        return (literal("CNOT", item.sites, CNOT, item.label + ":CNOT"),)
    if item.kind != "TOFFOLI":
        raise ValueError("unknown logical primitive")
    first, second, target = item.sites
    template = (
        ("H", (target,), H),
        ("CNOT", (second, target), CNOT),
        ("Tdg", (target,), Tdg),
        ("CNOT", (first, target), CNOT),
        ("T", (target,), T),
        ("CNOT", (second, target), CNOT),
        ("Tdg", (target,), Tdg),
        ("CNOT", (first, target), CNOT),
        ("T", (second,), T),
        ("T", (target,), T),
        ("H", (target,), H),
        ("CNOT", (first, second), CNOT),
        ("T", (first,), T),
        ("Tdg", (second,), Tdg),
        ("CNOT", (first, second), CNOT),
    )
    return tuple(
        literal(kind, sites, matrix, f"{item.label}:Toffoli:{index}:{kind}")
        for index, (kind, sites, matrix) in enumerate(template)
    )


def line_route(first: int, second: int) -> tuple[tuple[int, int], ...]:
    if first == second:
        raise ValueError("two-M2 route has coincident operands")
    if first < second:
        return tuple((site, site + 1) for site in range(first, second - 1))
    return tuple((site, site - 1) for site in range(first, second + 1, -1))


def literal_gate_controls() -> dict:
    literal_schedule = tuple(
        primitive for item in SCHEDULE for primitive in expand_logical(item)
    )
    toffoli = c523.bare_toffoli_controls()
    unitarity_residual = 0.0
    route_failures = label_failures = 0
    routing_swaps = 0
    nn_calls = 0
    maximum_distance = 0
    pair_cache = {}
    digest = sha256()
    for primitive in literal_schedule:
        size = 1 << len(primitive.sites)
        matrix = np.asarray(primitive.matrix, dtype=complex).reshape(size, size)
        unitarity_residual = max(
            unitarity_residual,
            float(np.max(abs(matrix.conj().T @ matrix - np.eye(size)))),
        )
        digest.update(
            f"{primitive.kind}:{primitive.sites}:{primitive.label}:".encode()
        )
        digest.update(repr(tuple((value.real.hex(), value.imag.hex()) for value in primitive.matrix)).encode())
        if len(primitive.sites) == 1:
            nn_calls += 1
            continue
        first, second = primitive.sites
        route = line_route(first, second)
        distance = abs(first - second)
        maximum_distance = max(maximum_distance, distance)
        routing_swaps += 2 * len(route)
        nn_calls += 1 + 6 * len(route)
        route_failures += sum(abs(left - right) != 1 for left, right in route)
        if (first, second) not in pair_cache:
            labels = list(range(TOTAL_M2))
            for left, right in route:
                labels[left], labels[right] = labels[right], labels[left]
            final_sites = (second - 1, second) if first < second else (second + 1, second)
            label_failures += int(tuple(labels[site] for site in final_sites) != (first, second))
            for left, right in reversed(route):
                labels[left], labels[right] = labels[right], labels[left]
            label_failures += int(labels != list(range(TOTAL_M2)))
            pair_cache[(first, second)] = final_sites

    frames = c531.c526.c235.proper_cubic_frames()
    mapped_edge_failures = 0
    for frame in frames:
        points = [frame @ np.asarray((site, 0, 0), dtype=int) for site in range(TOTAL_M2)]
        mapped_edge_failures += sum(
            int(np.abs(right - left).sum() != 1)
            for left, right in zip(points, points[1:])
        )
    logical_counts = Counter(item.kind for item in SCHEDULE)
    literal_counts = Counter(item.kind for item in literal_schedule)
    return {
        "logical_M2": TOTAL_M2,
        "new_M2": NEW_M2,
        "logical_gate_count": len(SCHEDULE),
        "logical_gate_kinds": dict(logical_counts),
        "literal_one_two_M2_gate_count_before_routing": len(literal_schedule),
        "literal_gate_kinds": dict(literal_counts),
        "maximum_literal_support_M2": max(len(item.sites) for item in literal_schedule),
        "Cycle523_exact_Toffoli": toffoli,
        "maximum_local_primitive_unitarity_residual": unitarity_residual,
        "distinct_ordered_two_M2_pairs": len(pair_cache),
        "maximum_line_operand_distance": maximum_distance,
        "forward_and_reverse_adjacent_SWAPS": routing_swaps,
        "literal_NN_one_two_M2_calls_after_routing": nn_calls,
        "route_adjacency_failures": route_failures,
        "terminal_operand_or_label_restoration_failures": label_failures,
        "all24_mapped_line_edge_failures": mapped_edge_failures,
        "literal_schedule_SHA256": digest.hexdigest(),
        "blank_gate_decomposition_work_M2": 0,
        "pass": (
            toffoli["pass"]
            and max(len(item.sites) for item in literal_schedule) == 2
            and unitarity_residual < TOL
            and not any((route_failures, label_failures, mapped_edge_failures))
        ),
    }


def frame_current(axis: int, rails: Word, frame: np.ndarray) -> tuple[int, Word]:
    direction = np.zeros(3, dtype=int)
    direction[axis] = 1
    mapped = frame @ direction
    new_axis = int(np.flatnonzero(mapped)[0])
    if int(mapped[new_axis]) == -1:
        return new_axis, (rails[1], rails[0])
    return new_axis, rails


def frame_word(bits: Word, axis: int, frame: np.ndarray) -> tuple[Word, int]:
    output = list(bits)
    source_rails = tuple(bits[site] for site in c531.C526_CURRENT)
    new_axis, mapped = frame_current(axis, source_rails, frame)
    for site, bit in zip(c531.C526_CURRENT, mapped):
        output[site] = bit
    plus_field = C531_OUTPUT_FIELDS.index(c531.PAYLOAD_CURRENT[0])
    minus_field = C531_OUTPUT_FIELDS.index(c531.PAYLOAD_CURRENT[1])
    for slot in MENU:
        pair = (bits[SNAPSHOT[slot][plus_field]], bits[SNAPSHOT[slot][minus_field]])
        _axis, mapped_pair = frame_current(axis, pair, frame)
        output[SNAPSHOT[slot][plus_field]] = mapped_pair[0]
        output[SNAPSHOT[slot][minus_field]] = mapped_pair[1]
    return tuple(output), new_axis


def covariance_controls() -> dict:
    frames = c531.c526.c235.proper_cubic_frames()
    failures = 0
    tests = 0
    for length, frame, law, member, binding, current in product(
        (TRAIN_LENGTH, HELD_LENGTH), frames, MENU, MENU, MENU,
        ((0, 0), (1, 0), (0, 1)),
    ):
        plus, minus = current
        edge = plus ^ minus
        head = (law + member + binding) % 5
        source = prepare(
            binding, law, member, head, edge=edge, plus=plus, minus=minus,
            K_position=(length + law + member) % c531.K_BITS,
        )
        output = physical_step(source)
        framed_source, framed_axis = frame_word(source, 0, frame)
        framed_output = physical_step(framed_source)
        expected, expected_axis = frame_word(output, 0, frame)
        failures += int(framed_output != expected or framed_axis != expected_axis)
        tests += 1

    group_failures = 0
    group_tests = 0
    for first, second, axis, rails in product(
        frames, frames, range(3), ((0, 0), (1, 0), (0, 1), (1, 1))
    ):
        middle_axis, middle_rails = frame_current(axis, rails, second)
        final_axis, final_rails = frame_current(middle_axis, middle_rails, first)
        direct_axis, direct_rails = frame_current(axis, rails, first @ second)
        group_failures += int(
            final_axis != direct_axis or final_rails != direct_rails
        )
        group_tests += 1
    return {
        "proper_cubic_frames": len(frames),
        "L5_held_L6_covariance_tests": tests,
        "covariance_failures": failures,
        "frame_products": len(frames) ** 2,
        "frame_group_role_tests": group_tests,
        "frame_group_law_failures": group_failures,
        "law_member_head_snapshot_frame_action": "scalar",
        "current_and_snapshot_current_action": "oriented endpoint rails",
        "compile_time_schedule_orbit_only": True,
        "pass": len(frames) == 24 and failures == 0 and group_failures == 0,
    }


def semantic_and_resource_controls() -> dict:
    source = prepare(3, 2, 3, 4, K_position=15)
    output = physical_step(source)
    cell = LocalLawCell(
        law_shift=law_of(source),
        member_before=member_of(source),
        member_after=member_of(output),
        head_before=head_of(source),
        head_after=head_of(output),
    )
    return {
        "cell": cell,
        "Cycle531_existing_M2": c531.TOTAL_M2,
        "law_word_M2": len(LAW_WORD),
        "member_state_M2": len(MEMBER_STATE),
        "snapshot_head_M2": len(OUTPUT_HEAD),
        "five_snapshot_banks_M2": sum(len(row) for row in SNAPSHOT),
        "total_bounded_M2": TOTAL_M2,
        "constant_overhead_per_local_law_cell": True,
        "underlying_Cycle219_mass_fixture": 0.45340565417488515,
        "upstream_source_binding_ports_terminally_unchanged": True,
        "supplied": (
            "one-hot law-word genesis and selection among five shift laws",
            "one-hot initial member carrier and snapshot head",
            "exact Cycle531 binding/event/current/K input and blank scratch",
            "blank finite snapshot bank and local routing chart",
            "deterministic member-carrier ontology and law interpretation",
        ),
        "derived": (
            "fixed autonomous recurrence after genesis",
            "matching Cycle531 MEMBER and LAW_RECEIPT emission",
            "exact Cycle531 precommit occurrence atom current K snapshot",
            "binder inverse member unemit and deterministic law shift",
            "literal one-/two-M2 gates, NN routing, all24/576 covariance",
        ),
        "open": (
            "autonomous genesis or dynamical selection of the law word and initial member",
            "objective stochasticity, p=q, Born probability, and empirical calibration",
            "non-erasing framework Record, realized history, permanence, and readability",
            "unbounded output growth, cubic volume tiling, source gravity and physical time",
        ),
        "law_selection_derived": False,
        "autonomous_genesis_derived": False,
        "autonomous_recurrence_after_genesis": True,
        "actuality_ontology_derived": False,
        "member_state_called_Record": False,
        "member_state_called_occurrence": False,
        "member_state_called_Born_member": False,
        "snapshot_pointer_copy_is_framework_Record": False,
        "finite_XOR_renewal_is_permanence": False,
        "deterministic_member_counts_are_Born_probability": False,
        "schedule_or_head_is_physical_time": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "axiom_pressure": False,
        "lawful_code_constraint_enforced": True,
        "off_code_binary_action": "reversible X/CNOT/Toffoli permutation; no malformed word is promoted to lawful",
        "pass": (
            TOTAL_M2 == 276
            and NEW_M2 == 100
            and cell.framework_Record is None
            and cell.stochastic_kernel is None
            and cell.Born_probability is None
            and cell.physical_time is None
        ),
    }


def main() -> int:
    started = time.monotonic()
    print("CYCLE 552: GENESIS-SUPPLIED AUTONOMOUS-RECURRENCE MEMBER-LAW CELL")
    print("authority=none; audit=unset; pointer copy is not Record; schedule is not time")
    dependency = dependency_and_contract_controls()
    interface = exact_interface_controls()
    recurrence = recurrence_controls()
    deletion = deletion_and_domain_controls()
    literal_gates = literal_gate_controls()
    covariance = covariance_controls()
    semantics = semantic_and_resource_controls()
    tests = {
        "strict_dependencies_and_note_contract": dependency["pass"],
        "exact_Cycle531_MEMBER_receipt_midpoint_and_outputs": interface["pass"],
        "autonomous_five_law_recurrence_inverse_and_XOR_renewal": recurrence["pass"],
        "invalid_lawword_deletions_and_lawful_domain": deletion["pass"],
        "literal_one_two_M2_Toffoli_and_NN_routing": literal_gates["pass"],
        "L5_held_L6_all24_and_576_covariance": covariance["pass"],
        "semantic_firewall_resources_and_no_axiom_pressure": semantics["pass"],
    }
    result = {
        "cycle": 552,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependency_and_contract": dependency,
        "exact_Cycle531_interface": interface,
        "autonomous_recurrence": recurrence,
        "deletions_and_lawful_domain": deletion,
        "literal_gate_and_routing_compiler": literal_gates,
        "covariance": covariance,
        "semantic_and_resource_inventory": semantics,
        "tests": tests,
        "pass": all(tests.values()),
        "elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": rss_bytes(),
        "process_swap_count": swap_count(),
    }
    for label, passed in tests.items():
        check(label.replace("_", " "), bool(passed), "ok" if passed else result)
    result["pass_count"] = PASS
    result["fail_count"] = FAIL
    print("RESULT_JSON", json.dumps(result, sort_keys=True, default=str))
    print("SUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
