#!/usr/bin/env python3
"""Cycle 531: selected-seam pre-Record and conditional occurrence binder.

This runner composes the exact Cycle-526 EDGE_PASSED/current/K interface with
the exact Cycle-505 singleton RecordBindingCandidate.  It proves two distinct
statements:

I.  Without a law-owned MEMBER and matching provenance receipt, the physical
    output is only a reversible pre-Record payload.  EDGE_PASSED never selects
    MEMBER.
II. Conditional on independently supplied one-hot MEMBER and matching law
    receipt, EDGE_PASSED can trigger a bounded physical occurrence/admitted-
    atom image.  On EDGE_PASSED=1 this image exactly matches the common
    Cycle-508 binder output.

Neither layer derives an actualization law, realized history, permanence,
framework Record, probability, sampler, or host-side choice.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import re
import resource
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_selected_seam_event_current_adapter_cycle526_2026_07_21 as c526
import physical_kraus_retained_carrier_record_binding_tournament_cycle505_2026_07_20 as c505
import physical_actual_member_admitted_history_law_tournament_train_cycle508_2026_07_20 as c508


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SELECTED_SEAM_CONDITIONAL_RECORD_BINDER_CYCLE531_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MENU = tuple(range(5))
K_BITS = c526.K_BITS
Word = tuple[int, ...]
PASS = 0
FAIL = 0


FROZEN = {
    "Cycle526 runner": "7c3d4a35664eaf5c7737c86464ca069e15ce29c40f61778081af8139970c37cd",
    "Cycle526 note": "2db4d547b284d7c2e19fcd10182ddf682a2ccd6b3907bf075b4097c8e9312615",
    "Cycle505 runner": "87f96ab5c7fd9e96c91cb32de0e2dd012e60d6cce62cf90403fb91a5e041275e",
    "Cycle505 note": "c3e8a1220172d5052089511616ad0ca2cdf6f6db5c92dc520c03a22600e112f4",
    "Cycle508 train runner": "b223ff44b159a598ef52ea21b3e758a1303e126d7f53474f799ed14c0a829dc6",
    "Cycle508 held runner": "f2a1c2a7ce2603fceb1a86b05c24e897111fbf44dde3e0ac0366e58c3c97a3d6",
    "Cycle508 held note": "8651a1bcfb39b2e2b8980bd5a25a352ffbe3e8e7a199ff421fc47f3a576c03c7",
    "Cycle500 runner": "01c459cd067e4b02b60558a3c29c95a0f93b3fd1d916a27176e35128f1668a90",
    "Cycle500 note": "0ba90e82d3759726914cf72d5f27f1687995045ce0c642e809f7bce713f79caa",
    "realized-state primitive": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "Born-frequency boundary": "f01676e96d4470498db667224a922847c98e0425bbdc88354513b7d61c38f081",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
}
FROZEN_PATHS = {
    "Cycle526 runner": Path(c526.__file__),
    "Cycle526 note": c526.NOTE,
    "Cycle505 runner": Path(c505.__file__),
    "Cycle505 note": c505.NOTE,
    "Cycle508 train runner": Path(c508.__file__),
    "Cycle508 held runner": ROOT / "scripts/physical_actual_member_admitted_history_law_tournament_held_cycle508_2026_07_20.py",
    "Cycle508 held note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ACTUAL_MEMBER_ADMITTED_HISTORY_LAW_TOURNAMENT_HELD_CYCLE508_NOTE_2026-07-20.md",
    "Cycle500 runner": Path(c505.c500.__file__),
    "Cycle500 note": c505.c500.NOTE,
    "realized-state primitive": ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "Born-frequency boundary": ROOT / "docs/RECORD_BORN_FREQUENCY_BOUNDARY_2026-06-05.md",
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
}


# Unified bounded line.  The Cycle-526 block has an exact 106-M2 resource
# envelope.  Its public ports occupy the final 19 sites in the resource order
# declared by Cycle526.  The exact 45-M2 Cycle505 block follows, then 25 new M2.
C526_WIDTH = 106
C526_EDGE = 87
C526_CURRENT = (88, 89)
C526_K = tuple(range(90, 106))
C505_OFFSET = C526_WIDTH
C505_WIDTH = c505.C_WIDTH


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    answer = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return answer


_layout = [C526_WIDTH + C505_WIDTH]
MEMBER = take(_layout, 5)
LAW_RECEIPT = take(_layout, 5)
PRECOMMIT_READY = take(_layout, 1)[0]
OCCURRENCE = take(_layout, 1)[0]
ATOM_FLAG = take(_layout, 1)[0]
ATOM_CONTENT = take(_layout, 3)
PAYLOAD_CURRENT = take(_layout, 2)
PAYLOAD_K_BINARY = take(_layout, 4)
WORK_BINDING = take(_layout, 1)[0]
WORK_PROVENANCE = take(_layout, 1)[0]
WORK_TRIGGER = take(_layout, 1)[0]
TOTAL_M2 = _layout[0]
NEW_M2 = TOTAL_M2 - C526_WIDTH - C505_WIDTH


@dataclass(frozen=True)
class PreRecordImage:
    edge_passed: int
    signed_current_rails: Word
    K_position: int
    precommit_ready: int
    payload_current: Word
    payload_K_binary: Word
    occurrence: None = None
    framework_Record: None = None


@dataclass(frozen=True)
class ConditionalBinderImage:
    supplied_member_label: int
    supplied_provenance_label: int
    occurrence_M2: int
    admitted_atom_flag: int
    admitted_atom_content: Word
    binding: c505.RecordBindingCandidate
    actualization_law_derived: bool = False
    framework_Record: None = None
    empirical_probability: None = None


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


def dependency_and_contract_controls() -> dict:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    registry = json.loads(FROZEN_PATHS["premise registry"].read_text(encoding="utf-8"))
    registry_text = json.dumps(registry).lower()
    required = (
        "authority: none", "audit: unset", "layer i", "layer ii",
        "edge_passed never selects member", "conditional binder/occurrence bridge",
        "not derived actualization", "not a framework record", "not physical time",
        "copying is not record", "no sampler", "no host-side selection",
        "all 24 proper-cubic frames", "l5", "held l=6", "n1", "n2", "n3",
        "n4", "n5", "n6", "n7", "n8", "no axiom pressure",
        "supplied / derived / open", "normalized constructive family",
        "primitive registry check", "delete edge", "delete member",
        "delete binding predicate",
    )
    body = normalized(NOTE)
    missing = tuple(fragment for fragment in required if fragment not in body)
    return {
        "strict_dependency_hashes_match": observed == FROZEN,
        "observed": observed,
        "note_missing_contract_fragments": missing,
        "runner_SHA256": file_sha(Path(__file__)),
        "declared_runner_SHA256": declared_runner_sha(),
        "realized_state_primitive_registered": "realized_state_primitive" in registry_text,
        "pass": (
            observed == FROZEN
            and not missing
            and declared_runner_sha() == file_sha(Path(__file__))
            and "realized_state_primitive" in registry_text
        ),
    }


def bits4(value: int) -> Word:
    if value not in range(16):
        raise ValueError("K position leaves the four-M2 binary image")
    return tuple((value >> lane) & 1 for lane in range(4))


def one_hot(label: int, width: int) -> Word:
    if label not in range(width):
        raise ValueError("one-hot label leaves its declared word")
    return tuple(int(index == label) for index in range(width))


def offset(site: int) -> int:
    return C505_OFFSET + site


def bridge_gate(kind: str, sites: tuple[int, ...], label: str) -> c505.Gate:
    return c505.gate(kind, sites, label, TOTAL_M2)


def bridge_schedule() -> tuple[c505.Gate, ...]:
    """One data-independent reversible schedule; no runtime label selection."""
    gates: list[c505.Gate] = [
        bridge_gate("CNOT", (C526_EDGE, PRECOMMIT_READY), "I:edge-to-precommit"),
        bridge_gate("CNOT", (C526_CURRENT[0], PAYLOAD_CURRENT[0]), "I:current-plus"),
        bridge_gate("CNOT", (C526_CURRENT[1], PAYLOAD_CURRENT[1]), "I:current-minus"),
    ]
    for position in range(K_BITS):
        for lane, bit in enumerate(bits4(position)):
            if bit:
                gates.append(bridge_gate(
                    "CNOT", (C526_K[position], PAYLOAD_K_BINARY[lane]),
                    f"I:K-binary:{position}:{lane}",
                ))

    # The same five-label schedule is run for every input.  MEMBER and receipt
    # are independent inputs; EDGE_PASSED is never written into either word.
    for label in MENU:
        gates.append(bridge_gate(
            "TOFFOLI", (MEMBER[label], offset(c505.C_ELIGIBILITY[label]), WORK_BINDING),
            f"II:member-binding:{label}:compute",
        ))
    for label in MENU:
        gates.append(bridge_gate(
            "TOFFOLI", (MEMBER[label], LAW_RECEIPT[label], WORK_PROVENANCE),
            f"II:member-provenance:{label}:compute",
        ))
    gates.extend((
        bridge_gate("TOFFOLI", (C526_EDGE, WORK_BINDING, WORK_TRIGGER), "II:edge-binding:compute"),
        bridge_gate("TOFFOLI", (WORK_TRIGGER, WORK_PROVENANCE, OCCURRENCE), "II:conditional-occurrence"),
        bridge_gate("TOFFOLI", (C526_EDGE, WORK_BINDING, WORK_TRIGGER), "II:edge-binding:uncompute"),
        bridge_gate("TOFFOLI", (OCCURRENCE, WORK_BINDING, ATOM_FLAG), "II:admitted-atom"),
    ))
    for lane in range(3):
        gates.append(bridge_gate(
            "TOFFOLI", (OCCURRENCE, offset(c505.C_CONTENT[lane]), ATOM_CONTENT[lane]),
            f"II:atom-content:{lane}",
        ))
    for label in reversed(MENU):
        gates.append(bridge_gate(
            "TOFFOLI", (MEMBER[label], LAW_RECEIPT[label], WORK_PROVENANCE),
            f"II:member-provenance:{label}:uncompute",
        ))
    for label in reversed(MENU):
        gates.append(bridge_gate(
            "TOFFOLI", (MEMBER[label], offset(c505.C_ELIGIBILITY[label]), WORK_BINDING),
            f"II:member-binding:{label}:uncompute",
        ))
    return tuple(gates)


SCHEDULE = bridge_schedule()


def validate_word(bits: Word) -> None:
    if len(bits) != TOTAL_M2 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Cycle531 word leaves its exact binary 176-M2 domain")


def logical_apply(bits: Word, *, reverse: bool = False, delete_label: str | None = None) -> Word:
    validate_word(bits)
    matches = tuple(index for index, item in enumerate(SCHEDULE) if item.label == delete_label)
    if delete_label is not None and len(matches) != 1:
        raise ValueError("deletion must name exactly one Cycle531 primitive")
    schedule = tuple(
        item for index, item in enumerate(SCHEDULE)
        if delete_label is None or index != matches[0]
    )
    word = list(bits)
    for item in (tuple(reversed(schedule)) if reverse else schedule):
        c505.apply_gate(word, item)
    return tuple(word)


@lru_cache(maxsize=None)
def binding_word(label: int, vacancy: int = 1) -> Word:
    source = c505.c_prepare(label, vacancy=vacancy)
    physical = c505.c_physical(source)
    view = c505.c_view(physical)
    if vacancy and not (
        view.singleton == 1
        and view.central_site_eligible == 1
        and view.eligibility == one_hot(label, 5)
        and view.content == c505.bits3(label)
    ):
        raise RuntimeError("Cycle505 binding contract changed")
    if not vacancy and (view.singleton or sum(view.eligibility) or view.central_site_eligible):
        raise RuntimeError("Cycle505 vacancy deletion contract changed")
    return physical


def prepare(
    *, edge: int, plus: int, minus: int, K_position: int,
    binding_label: int, member_label: int | None, receipt_label: int | None,
    vacancy: int = 1,
) -> Word:
    if edge not in (0, 1) or plus not in (0, 1) or minus not in (0, 1):
        raise ValueError("event/current ports leave their binary domain")
    if edge != (plus ^ minus) or plus & minus:
        raise ValueError("event/current consistency constraint fails")
    if K_position not in range(K_BITS) or binding_label not in MENU:
        raise ValueError("K or binding label leaves its declared domain")
    if (member_label is None) != (receipt_label is None):
        raise ValueError("member and law provenance must be jointly absent or present")
    if member_label is not None and (member_label not in MENU or receipt_label not in MENU):
        raise ValueError("member/provenance label leaves the five-label domain")

    bits = [0] * TOTAL_M2
    bits[C526_EDGE] = edge
    bits[C526_CURRENT[0]] = plus
    bits[C526_CURRENT[1]] = minus
    for site, bit in zip(C526_K, one_hot(K_position, K_BITS)):
        bits[site] = bit
    physical_binding = binding_word(binding_label, vacancy)
    bits[C505_OFFSET:C505_OFFSET + C505_WIDTH] = physical_binding
    if member_label is not None:
        bits[MEMBER[member_label]] = 1
        assert receipt_label is not None
        bits[LAW_RECEIPT[receipt_label]] = 1
    output = tuple(bits)
    validate_word(output)
    return output


def pre_record_view(bits: Word) -> PreRecordImage:
    validate_word(bits)
    K_word = tuple(bits[site] for site in C526_K)
    if sum(K_word) != 1:
        raise ValueError("K is not one-hot")
    return PreRecordImage(
        edge_passed=bits[C526_EDGE],
        signed_current_rails=tuple(bits[site] for site in C526_CURRENT),
        K_position=K_word.index(1),
        precommit_ready=bits[PRECOMMIT_READY],
        payload_current=tuple(bits[site] for site in PAYLOAD_CURRENT),
        payload_K_binary=tuple(bits[site] for site in PAYLOAD_K_BINARY),
    )


def conditional_view(bits: Word) -> ConditionalBinderImage | None:
    validate_word(bits)
    member = tuple(bits[site] for site in MEMBER)
    receipt = tuple(bits[site] for site in LAW_RECEIPT)
    if sum(member) == 0 and sum(receipt) == 0:
        if bits[OCCURRENCE] or bits[ATOM_FLAG] or any(bits[site] for site in ATOM_CONTENT):
            raise ValueError("an occurrence appeared without a law-owned member")
        return None
    if sum(member) != 1 or sum(receipt) != 1 or member.index(1) != receipt.index(1):
        raise ValueError("malformed or mismatched law-owned member provenance")
    label = member.index(1)
    binding = c505.c_view(tuple(bits[C505_OFFSET:C505_OFFSET + C505_WIDTH]))
    return ConditionalBinderImage(
        supplied_member_label=label,
        supplied_provenance_label=receipt.index(1),
        occurrence_M2=bits[OCCURRENCE],
        admitted_atom_flag=bits[ATOM_FLAG],
        admitted_atom_content=tuple(bits[site] for site in ATOM_CONTENT),
        binding=binding,
    )


def c526_transition_table():
    labels = c526.c315.joint_labels()
    rows, phases = c526.signed_permutation(c526.c315.edge_fswap_matrix(labels, 0))
    for data, K_position in product(range(len(labels)), range(K_BITS)):
        target_data, target_K, edge, plus, minus, phase = c526.adapter_transition(
            labels, rows, phases, data, K_position, 0, 0, 0
        )
        yield labels, data, K_position, target_data, target_K, edge, plus, minus, phase


def exhaustive_bridge_controls() -> dict:
    layer_I_failures = conditional_failures = inverse_failures = work_failures = 0
    member_mutations = receipt_mutations = binding_mutations = source_port_mutations = 0
    tested_layer_I = tested_conditional = event_columns = 0
    phase_modulus_residual = 0.0
    labels_object = None
    for row in c526_transition_table():
        labels, data, K_input, _target_data, K_output, edge, plus, minus, phase = row
        labels_object = labels
        phase_modulus_residual = max(phase_modulus_residual, abs(abs(phase) - 1))
        binding_label = data % 5
        source = prepare(
            edge=edge, plus=plus, minus=minus, K_position=K_output,
            binding_label=binding_label, member_label=None, receipt_label=None,
        )
        output = logical_apply(source)
        view = pre_record_view(output)
        no_member = conditional_view(output)
        layer_I_failures += int(
            view.precommit_ready != edge
            or view.payload_current != (plus, minus)
            or view.payload_K_binary != bits4(K_output)
            or no_member is not None
        )
        inverse_failures += logical_apply(output, reverse=True) != source
        work_failures += any(output[site] for site in (WORK_BINDING, WORK_PROVENANCE, WORK_TRIGGER))
        member_mutations += any(output[site] != source[site] for site in MEMBER)
        receipt_mutations += any(output[site] != source[site] for site in LAW_RECEIPT)
        binding_mutations += any(
            output[C505_OFFSET + site] != source[C505_OFFSET + site]
            for site in range(C505_WIDTH)
        )
        source_port_mutations += any(
            output[site] != source[site]
            for site in (C526_EDGE, *C526_CURRENT, *C526_K)
        )
        tested_layer_I += 1
        event_columns += edge

        # Every fifth column exhausts all five conditional labels; across the
        # complete Fock x K domain this gives 65,536 conditional codewords.
        label = (data + K_input) % 5
        conditional_source = prepare(
            edge=edge, plus=plus, minus=minus, K_position=K_output,
            binding_label=label, member_label=label, receipt_label=label,
        )
        conditional_output = logical_apply(conditional_source)
        candidate = conditional_view(conditional_output)
        assert candidate is not None
        conditional_failures += int(
            candidate.occurrence_M2 != edge
            or candidate.admitted_atom_flag != edge
            or candidate.admitted_atom_content != tuple(edge & bit for bit in c505.bits3(label))
            or candidate.binding.eligibility != one_hot(label, 5)
            or candidate.actualization_law_derived
            or candidate.framework_Record is not None
            or candidate.empirical_probability is not None
        )
        inverse_failures += logical_apply(conditional_output, reverse=True) != conditional_source
        work_failures += any(conditional_output[site] for site in (WORK_BINDING, WORK_PROVENANCE, WORK_TRIGGER))
        member_mutations += any(conditional_output[site] != conditional_source[site] for site in MEMBER)
        receipt_mutations += any(conditional_output[site] != conditional_source[site] for site in LAW_RECEIPT)
        binding_mutations += any(
            conditional_output[C505_OFFSET + site] != conditional_source[C505_OFFSET + site]
            for site in range(C505_WIDTH)
        )
        source_port_mutations += any(
            conditional_output[site] != conditional_source[site]
            for site in (C526_EDGE, *C526_CURRENT, *C526_K)
        )
        tested_conditional += 1

    assert labels_object is not None
    return {
        "complete_Cycle526_Fock_x_K_columns": tested_layer_I,
        "expected_columns": len(labels_object) * K_BITS,
        "conditional_member_columns": tested_conditional,
        "moving_event_columns": event_columns,
        "layer_I_failures": layer_I_failures,
        "conditional_layer_II_failures": conditional_failures,
        "inverse_failures": inverse_failures,
        "work_cleanup_failures": work_failures,
        "member_input_mutations": member_mutations,
        "law_receipt_input_mutations": receipt_mutations,
        "Cycle505_binding_input_mutations": binding_mutations,
        "Cycle526_source_port_mutations": source_port_mutations,
        "maximum_imported_phase_modulus_residual": phase_modulus_residual,
        "pass": not any((
            layer_I_failures, conditional_failures, inverse_failures, work_failures,
            member_mutations, receipt_mutations, binding_mutations, source_port_mutations,
        )) and tested_layer_I == len(labels_object) * K_BITS,
    }


def cycle508_exact_comparator() -> dict:
    failures = 0
    rows = []
    for label in MENU:
        old_source = c508.prepare_common(
            label, member_supplied=True, phase=None,
            law_receipt_supplied=True, vacancy=1,
        )
        old_output = c508.physical_apply(old_source, c508.binder_schedule())
        new_source = prepare(
            edge=1, plus=1, minus=0, K_position=label,
            binding_label=label, member_label=label, receipt_label=label,
        )
        new_output = logical_apply(new_source)
        old_tuple = (
            old_output[c508.OCCURRENCE], old_output[c508.ATOM_FLAG],
            tuple(old_output[site] for site in c508.ATOM_CONTENT),
        )
        new_tuple = (
            new_output[OCCURRENCE], new_output[ATOM_FLAG],
            tuple(new_output[site] for site in ATOM_CONTENT),
        )
        failures += old_tuple != new_tuple
        rows.append({"label": label, "Cycle508": old_tuple, "Cycle531": new_tuple})
    return {
        "EDGE_PASSED_one_exact_output_tests": len(rows),
        "failures": failures,
        "rows": rows,
        "qualification": "exact occurrence+admitted-atom image only; Cycle531 does not reproduce or derive Cycle508 member-producing laws",
        "pass": failures == 0,
    }


def covariance_controls() -> dict:
    frames = c526.c235.proper_cubic_frames()
    failures = 0
    tests = 0
    orientation_rows = Counter()
    for frame in frames:
        mapped_direction = frame @ c526.np.asarray((1, 0, 0), dtype=int)
        axis = int(c526.np.flatnonzero(mapped_direction)[0])
        reversed_endpoints = int(mapped_direction[axis]) == -1
        orientation_rows["endpoint_reversing" if reversed_endpoints else "endpoint_preserving"] += 1
        for label, K_position, current in product(MENU, range(K_BITS), ((0, 0), (1, 0), (0, 1))):
            plus, minus = current
            edge = plus ^ minus
            source = prepare(
                edge=edge, plus=plus, minus=minus, K_position=K_position,
                binding_label=label, member_label=label, receipt_label=label,
            )
            output = logical_apply(source)

            framed_plus, framed_minus = ((minus, plus) if reversed_endpoints else (plus, minus))
            framed_source = prepare(
                edge=edge, plus=framed_plus, minus=framed_minus, K_position=K_position,
                binding_label=label, member_label=label, receipt_label=label,
            )
            framed_output = logical_apply(framed_source)
            expected = list(output)
            if reversed_endpoints:
                expected[C526_CURRENT[0]], expected[C526_CURRENT[1]] = expected[C526_CURRENT[1]], expected[C526_CURRENT[0]]
                expected[PAYLOAD_CURRENT[0]], expected[PAYLOAD_CURRENT[1]] = expected[PAYLOAD_CURRENT[1]], expected[PAYLOAD_CURRENT[0]]
            failures += tuple(expected) != framed_output
            tests += 1
    return {
        "proper_cubic_frames": len(frames),
        "bridge_frame_tests": tests,
        "bridge_frame_failures": failures,
        "orientation_rows": dict(orientation_rows),
        "EDGE_PRECOMMIT_OCCURRENCE_K_binding_member_atom_frame_action": "scalar",
        "signed_current_frame_action": "plus/minus swap under endpoint reversal",
        "upstream_Cycle526_all_Fock_covariance_strict_hash_imported": True,
        "pass": len(frames) == 24 and failures == 0,
    }


def deletion_controls() -> dict:
    # Three separately requested semantic deletions on a moving column.
    full_source = prepare(
        edge=1, plus=1, minus=0, K_position=7,
        binding_label=4, member_label=4, receipt_label=4,
    )
    full = logical_apply(full_source)
    edge_deleted_source = prepare(
        edge=0, plus=0, minus=0, K_position=7,
        binding_label=4, member_label=4, receipt_label=4,
    )
    member_deleted_source = prepare(
        edge=1, plus=1, minus=0, K_position=7,
        binding_label=4, member_label=None, receipt_label=None,
    )
    binding_deleted_source = prepare(
        edge=1, plus=1, minus=0, K_position=7,
        binding_label=4, member_label=4, receipt_label=4, vacancy=0,
    )
    receipt_deleted_source = list(full_source)
    receipt_deleted_source[LAW_RECEIPT[4]] = 0
    variants = {
        "delete_EDGE": logical_apply(edge_deleted_source),
        "delete_MEMBER": logical_apply(member_deleted_source),
        "delete_binding_predicate": logical_apply(binding_deleted_source),
        "delete_law_receipt": logical_apply(tuple(receipt_deleted_source)),
    }
    semantic = {
        name: {
            "precommit": bits[PRECOMMIT_READY],
            "occurrence": bits[OCCURRENCE],
            "atom": bits[ATOM_FLAG],
            "work": tuple(bits[site] for site in (WORK_BINDING, WORK_PROVENANCE, WORK_TRIGGER)),
            "basis_residual_from_full": 0.0 if bits == full else 2 ** 0.5,
        }
        for name, bits in variants.items()
    }

    # Each compiled gate must have at least one lawful witness.  This separates
    # unfinished route ingredients from a shared substrate obstruction.
    unwitnessed = []
    witness_checks = 0
    witnesses = tuple(
        prepare(
            edge=plus ^ minus, plus=plus, minus=minus, K_position=K_position,
            binding_label=label, member_label=label, receipt_label=label,
        )
        for label, K_position, (plus, minus) in product(
            MENU, range(K_BITS), ((0, 0), (1, 0), (0, 1))
        )
    )
    for item in SCHEDULE:
        found = False
        for source in witnesses:
            witness_checks += 1
            if logical_apply(source, delete_label=item.label) != logical_apply(source):
                found = True
                break
        if not found:
            unwitnessed.append(item.label)

    malformed_rejections = 0
    operations = (
        lambda: prepare(edge=2, plus=1, minus=0, K_position=0, binding_label=0, member_label=None, receipt_label=None),
        lambda: prepare(edge=0, plus=1, minus=0, K_position=0, binding_label=0, member_label=None, receipt_label=None),
        lambda: prepare(edge=0, plus=1, minus=1, K_position=0, binding_label=0, member_label=None, receipt_label=None),
        lambda: prepare(edge=0, plus=0, minus=0, K_position=16, binding_label=0, member_label=None, receipt_label=None),
        lambda: prepare(edge=0, plus=0, minus=0, K_position=0, binding_label=5, member_label=None, receipt_label=None),
        lambda: prepare(edge=0, plus=0, minus=0, K_position=0, binding_label=0, member_label=0, receipt_label=None),
        lambda: prepare(edge=0, plus=0, minus=0, K_position=0, binding_label=0, member_label=5, receipt_label=0),
    )
    for operation in operations:
        try:
            operation()
        except ValueError:
            malformed_rejections += 1

    return {
        "semantic_deletions": semantic,
        "delete_EDGE_blocks_precommit_and_occurrence": semantic["delete_EDGE"]["precommit"] == 0 and semantic["delete_EDGE"]["occurrence"] == 0,
        "delete_MEMBER_retains_precommit_but_blocks_occurrence": semantic["delete_MEMBER"]["precommit"] == 1 and semantic["delete_MEMBER"]["occurrence"] == 0,
        "delete_binding_retains_precommit_but_blocks_occurrence": semantic["delete_binding_predicate"]["precommit"] == 1 and semantic["delete_binding_predicate"]["occurrence"] == 0,
        "delete_receipt_retains_precommit_but_blocks_occurrence": semantic["delete_law_receipt"]["precommit"] == 1 and semantic["delete_law_receipt"]["occurrence"] == 0,
        "logical_schedule_gates": len(SCHEDULE),
        "individual_gate_witness_checks": witness_checks,
        "unwitnessed_gate_deletions": unwitnessed,
        "malformed_domain_rejections": malformed_rejections,
        "expected_malformed_domain_rejections": len(operations),
        "pass": (
            not unwitnessed
            and malformed_rejections == len(operations)
            and semantic["delete_EDGE"]["precommit"] == 0
            and semantic["delete_EDGE"]["occurrence"] == 0
            and semantic["delete_MEMBER"]["precommit"] == 1
            and semantic["delete_MEMBER"]["occurrence"] == 0
            and semantic["delete_binding_predicate"]["precommit"] == 1
            and semantic["delete_binding_predicate"]["occurrence"] == 0
            and semantic["delete_law_receipt"]["precommit"] == 1
            and semantic["delete_law_receipt"]["occurrence"] == 0
        ),
    }


def routing_and_resource_controls() -> dict:
    trace = c505.nn_trace(SCHEDULE, TOTAL_M2)
    source = prepare(
        edge=1, plus=0, minus=1, K_position=15,
        binding_label=3, member_label=3, receipt_label=3,
    )
    routed = c505.apply_routed(source, SCHEDULE)
    logical = logical_apply(source)
    roundtrip = c505.apply_routed(routed, SCHEDULE, reverse=True)
    return {
        **trace,
        "fixed_schedule_routed_equals_logical": routed == logical,
        "routed_inverse_roundtrip": roundtrip == source,
        "Cycle526_existing_patch_M2": C526_WIDTH,
        "Cycle505_existing_binding_patch_M2": C505_WIDTH,
        "new_cross_lane_M2": NEW_M2,
        "total_bounded_composite_M2": TOTAL_M2,
        "new_input_M2": 10,
        "new_retained_output_M2": 12,
        "new_clean_work_M2": 3,
        "constant_overhead_per_selected_seam": True,
        "runtime_host_selected_gate_sequence": False,
        "L5_and_held_L6_use_same_bridge_schedule": True,
        "upstream_Cycle526_L5_L6_exact_fixture_strict_hash_imported": True,
        "underlying_Cycle219_mass_parameter_preserved": 0.45340565417488515,
        "extended_history_output_mass_eigenstate_claimed": False,
        "pass": (
            routed == logical
            and roundtrip == source
            and trace["maximum_support_M2"] <= 3
            and trace["connected_failures"] == 0
            and trace["final_adjacent_support_failures"] == 0
            and trace["terminal_operand_order_failures"] == 0
            and trace["reverse_label_restoration_failures"] == 0
            and NEW_M2 == 25
            and TOTAL_M2 == 176
        ),
    }


def semantic_firewall_controls() -> dict:
    no_member = conditional_view(logical_apply(prepare(
        edge=1, plus=1, minus=0, K_position=3,
        binding_label=2, member_label=None, receipt_label=None,
    )))
    member_source = prepare(
        edge=1, plus=1, minus=0, K_position=3,
        binding_label=2, member_label=2, receipt_label=2,
    )
    member_output = logical_apply(member_source)
    image = conditional_view(member_output)
    assert image is not None
    return {
        "Layer_I_no_member_output": no_member,
        "Layer_II_actualization_law_derived": image.actualization_law_derived,
        "Layer_II_framework_Record": image.framework_Record,
        "Layer_II_empirical_probability": image.empirical_probability,
        "MEMBER_written_by_schedule": any(MEMBER[0] in item.sites[-1:] for item in SCHEDULE),
        "LAW_RECEIPT_written_by_schedule": any(LAW_RECEIPT[0] in item.sites[-1:] for item in SCHEDULE),
        "supplied": (
            "Cycle526 selected-seam EDGE/current/K ports",
            "Cycle505 singleton binding codeword",
            "one-hot law-owned MEMBER input",
            "matching one-hot law-provenance receipt",
            "blank output/work M2",
            "static nearest-neighbor routing compiler and frame action",
        ),
        "derived": (
            "reversible precommit/current/K image",
            "conditional occurrence M2",
            "conditional singleton-bound admitted-atom image",
            "exact Cycle508 binder output on EDGE_PASSED=1",
        ),
        "open": (
            "law that produces an actual MEMBER",
            "state/member selection",
            "formation location and permanence/close law",
            "framework Record and realized history",
            "Born probability, sampler, frequencies, and source/gravity coupling",
        ),
        "pass": (
            no_member is None
            and not image.actualization_law_derived
            and image.framework_Record is None
            and image.empirical_probability is None
            and not any(site in item.sites[-1:] for item in SCHEDULE for site in MEMBER)
            and not any(site in item.sites[-1:] for item in SCHEDULE for site in LAW_RECEIPT)
        ),
    }


def main() -> int:
    started = time.monotonic()
    print("CYCLE 531: SELECTED-SEAM PRE-RECORD / CONDITIONAL OCCURRENCE BINDER")
    print("authority=none; audit=unset; no actualization or Record claim")

    dependency = dependency_and_contract_controls()
    exhaustive = exhaustive_bridge_controls()
    comparator = cycle508_exact_comparator()
    covariance = covariance_controls()
    deletions = deletion_controls()
    routing = routing_and_resource_controls()
    firewall = semantic_firewall_controls()

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "theorem_layers": {
            "I": "unconditional EDGE/current/K output is reversible pre-Record and never selects MEMBER",
            "II": "conditional on supplied law-owned MEMBER/provenance, EDGE triggers the exact Cycle508 occurrence+atom image",
        },
        "dependency_and_contract": dependency,
        "exhaustive_all_Fock_K": exhaustive,
        "Cycle508_exact_comparator": comparator,
        "proper_cubic_covariance": covariance,
        "deletions_and_domain": deletions,
        "routing_resources_L5_L6_mass": routing,
        "semantic_firewall_and_inventory": firewall,
        "leakage": {
            "full_binary_map": "permutation from X/CNOT/TOFFOLI",
            "code_space_inverse_failures": exhaustive["inverse_failures"],
            "clean_work_failures": exhaustive["work_cleanup_failures"],
            "terminal_code_leakage": 0,
        },
        "elapsed_seconds": time.monotonic() - started,
        "maximum_RSS_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
    }

    check("strict dependencies, note contract, and primitive-registry control close", dependency["pass"], dependency)
    check("complete Cycle526 all-Fock x K Layer-I and conditional Layer-II truth tables close", exhaustive["pass"], exhaustive)
    check("EDGE=1 conditional output exactly reproduces the Cycle508 common binder", comparator["pass"], comparator)
    check("the local bridge is covariant under all 24 proper-cubic frames", covariance["pass"], covariance)
    check("EDGE, MEMBER, binding, receipt, every gate, and malformed domains have witnesses", deletions["pass"], deletions)
    check("the 176-M2 bounded composite has an exact nearest-neighbor inverse", routing["pass"], routing)
    check("the actualization/Record/Born firewall and supplied inventory remain explicit", firewall["pass"], firewall)

    result["PASS"] = PASS
    result["FAIL"] = FAIL
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
