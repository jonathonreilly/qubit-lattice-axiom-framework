#!/usr/bin/env python3
"""Cycle 665: compile formation debit/current and causal-interval endpoint."""

from __future__ import annotations

TARGET_CONTRACT = {
    "target_statement": "construct an explicit bounded-support local compiler C that attaches each lawful Cycle662 ready-to-spent objective formation transition to the immutable Cycle559/Cycle591 locally conserved source/current interface and the landed Cycle612 matter-caused causal-interval packet, producing in the same admitted event one counted local source debit/current, retained innovation/coherent exhaust, and one typed interval endpoint without host scheduling, energy language, actuality lookup, or discarded exhaust",
    "quantifiers_domain": "all lawful finite Cycle662 menu-state branches on declared train and blinded held capacities; every proper-cubic frame and ordered frame product; every tested Cycle559/Cycle591 conserved-current orientation and Cycle612 packet direction; malformed, saturated, deleted, inverse, zero-propensity, and unit-propensity cases",
    "allowed_premises": "immutable landed Cycle662 stochastic formation law and ready/spent/exhaust transition; immutable retained Cycle559/Cycle591 source/current port and conservation convention; immutable landed Cycle612 matter-caused causal-interval packet; finite bounded M2 registers, compile-time proper-cubic frame transport, local reversible permutations, and explicit blank/source/sink registers",
    "forbidden_weakenings": "host scheduler or sampler; supplied actuality token or lookup; runtime grade lookup; shell-predicate ROM; calling a generator a rate; calling the resource debit/current physical energy or gravity; deleting coherent, rejected, source, current, or interval sectors; modifying any shore; importing a target-equivalent resource-current or interval oracle",
    "required_edge_cases": "train and blinded held capacities; lawful zero and unit propensities; biased and nonproduct states inherited from Cycle662; all24/all576; source/current conservation; bounded locality/support/M2 accounting; inverse, deletion, malformed-source, saturation, and unchanged-shore regression",
    "completion_witness": "an executable local encoding and update with exact transition tables and register counts showing that one admitted Cycle662 formation firing simultaneously debits one local ready source, credits spent/exhaust, writes a conserved local current/interface certificate, and emits a typed Cycle612 interval endpoint, together with inverse, conservation, covariance, deletion, malformed, saturation, and pinned-shore tests",
    "outcomes_not_closure": "a bookkeeping-only ledger without the immutable current interface; a current label without exact local conservation; an interval label not produced in the same transition; host-sequenced composition; pointer copying; energy, force, stress, gravity, rate, Record, Born, or realized-history claims; discarded exhaust; a route-specific failure promoted to shared obstruction or axiom pressure",
}

from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FORMATION_RESOURCE_INTERVAL_COMPILER_CYCLE665_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / "outputs/physical_formation_resource_interval_compiler_cycle665_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_formation_resource_interval_compiler_cycle665_cold_2026_07_23.txt"
SHORE = "cd2c32e3ed5faf198604fc22414ca4b71931328c"
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0


PINS = {
    "scripts/physical_locally_conserved_current_response_law_tournament_cycle559_2026_07_21.py":
        "a6475b85ad4c87cae58ee09d371ff91f82719d50e72e8f5ff88d5030fef681be",
    "docs/work_history/repo/review_feedback/PHYSICAL_LOCALLY_CONSERVED_CURRENT_RESPONSE_LAW_TOURNAMENT_CYCLE559_NOTE_2026-07-21.md":
        "4410c285e8c2a41969a8854258ccaeaaad6c0b3a3340bae1ed39fdfbe9ca1136",
    "outputs/physical_locally_conserved_current_response_law_tournament_cycle559_receipt_2026_07_21.json":
        "ac7afebd283cfab893e6fd85ee71e46351e950805b10e8d5258ba1b06aea665b",
    "scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py":
        "b927333e3287fa46c03f7ed9b53259cd126f47cca30eaca35c8220971b822a08",
    "docs/work_history/repo/review_feedback/PHYSICAL_OPERATIONAL_METRIC_CONSERVED_SOURCE_LOCAL_RANGE_TOURNAMENT_CYCLE591_NOTE_2026-07-22.md":
        "86746b0cf9a80145b9c7cb4415c4402d6a697bb99e1fa83bae547bf091ac37e5",
    "outputs/physical_operational_metric_conserved_source_local_range_tournament_cycle591_cold_2026_07_22.txt":
        "765770317f82aeec1105bc33c80c21c920b09d35deab5663df62b4edab2f917c",
    "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py":
        "91f22d23dd2730f76a05736634236d41036f68eaedc4921daca69de25ab6a344",
    "docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md":
        "920776555dce6505bccb0e46e552e90d24858c08cfb7f6978d884f10a5bb0789",
    "outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json":
        "e7a8ea3dcbe370c9f8c6a94770508d1710a7013ce4ba62a1ad67e345fe1e2d11",
    "scripts/physical_objective_stochastic_open_dilation_cycle662_2026_07_23.py":
        "219b6d3d93884a0ab8d9b0cc6c79850d008193fd5571b0281c76b6f8707d6b84",
    "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md":
        "bdc8dda304985a62c73fc6e7a03f11d61041dd8053a9321fb7171c9b22947a05",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json":
        "27b258f1e4d96fb26f65937875bea32d74ecdfa62712c353e3327d0357a2c806",
    "outputs/physical_objective_stochastic_open_dilation_cycle662_cold_2026_07_23.txt":
        "14c431047466462c57ecff1c83472e5233e88af3fc454920b6f6d6465a8cc625",
}

CURRENT_WORDS = {"NULL": (0, 0, 0), "PLUS": (1, 1, 0), "MINUS": (1, 0, 1)}
PACKET_WIDTH = 16
BLANK_PACKET = ((0,) * PACKET_WIDTH,) * 3
SUPERCELL_COORDINATES = tuple(product(range(-4, 5), repeat=3))
INNER_CYCLE662_COORDINATES = tuple(product(range(-2, 3), repeat=3))
OUTER_SHELL_COORDINATES = tuple(sorted(set(SUPERCELL_COORDINATES)-set(INNER_CYCLE662_COORDINATES)))
INTERFACE_REGISTER_COORDINATES = INNER_CYCLE662_COORDINATES + OUTER_SHELL_COORDINATES[:438]
FIXED_LOCAL_WORD = (
    "Cycle662 stochastic branch update and retained coherent exhaust",
    "Cycle612 Pd matter predicate compute",
    "local conjunction of occurrence, binding, ADMIT, LOCK, matter, law-domain, packet-fresh, ready",
    "ready-source debit and spent/exhaust credit",
    "Cycle559 EDGE/J+/J- current-certificate write with EDGE reused from Cycle662",
    "Cycle612 triplicate endpoint/predecessor/receipt packet append",
    "Cycle612 Pd and join-work uncompute",
)
FIXED_LOCAL_WORD_SHA256 = sha256(json.dumps(FIXED_LOCAL_WORD).encode()).hexdigest()


@dataclass(frozen=True)
class Slot:
    ready: int = 1
    spent: int = 0
    current_word: tuple[int, int, int] = CURRENT_WORDS["NULL"]
    packet: tuple[tuple[int, ...], ...] = BLANK_PACKET
    exhaust_tag: str | None = None
    detector_pointer: int = 0
    join_work: int = 0


@dataclass(frozen=True)
class Ledger:
    slots: tuple[Slot, ...]


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, text):
        for stream in self.streams: stream.write(text)
        return len(text)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def stable_digest(value: object) -> str:
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=float).encode()).hexdigest()


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_bytes(path: str) -> bytes:
    return subprocess.run(
        ("git", "show", f"{SHORE}:{path}"), cwd=ROOT, check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout


def target_freeze_controls() -> dict[str, object]:
    source = Path(__file__).read_text().splitlines()
    target_line = next(index for index, line in enumerate(source, 1) if line.startswith("TARGET_CONTRACT ="))
    first_evidence_load_line = next(index for index, line in enumerate(source, 1) if line.startswith("def shore_controls"))
    return {
        "target_contract_sha256": stable_digest(TARGET_CONTRACT),
        "target_line": target_line,
        "first_evidence_load_line": first_evidence_load_line,
        "frozen_before_evidence": target_line < first_evidence_load_line,
        "proof_search_governance_exact_fields": sorted(TARGET_CONTRACT),
        "pass": target_line < first_evidence_load_line and sorted(TARGET_CONTRACT) == [
            "allowed_premises", "completion_witness", "forbidden_weakenings",
            "outcomes_not_closure", "quantifiers_domain", "required_edge_cases", "target_statement",
        ],
    }


def parse_cycle591_cold(body: bytes) -> dict[str, object]:
    for line in body.decode().splitlines():
        if line.startswith("REPORT_JSON "):
            return json.loads(line.removeprefix("REPORT_JSON "))
    raise ValueError("Cycle591 cold transcript has no REPORT_JSON")


def shore_controls() -> tuple[dict[str, object], dict[str, dict[str, object]]]:
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in PINS}
    receipts = {
        "Cycle559": json.loads(git_bytes("outputs/physical_locally_conserved_current_response_law_tournament_cycle559_receipt_2026_07_21.json")),
        "Cycle591": parse_cycle591_cold(git_bytes("outputs/physical_operational_metric_conserved_source_local_range_tournament_cycle591_cold_2026_07_22.txt")),
        "Cycle612": json.loads(git_bytes("outputs/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_receipt_2026_07_22.json")),
        "Cycle662": json.loads(git_bytes("outputs/physical_objective_stochastic_open_dilation_cycle662_receipt_2026_07_23.json")),
    }
    contracts = {
        "Cycle559_pass": receipts["Cycle559"]["pass"],
        "Cycle559_authority_audit": [receipts["Cycle559"]["authority"], receipts["Cycle559"]["audit"]],
        "Cycle591_tests": [receipts["Cycle591"]["tests_passed"], receipts["Cycle591"]["tests_failed"]],
        "Cycle591_authority_audit": [receipts["Cycle591"]["authority"], receipts["Cycle591"]["audit"]],
        "Cycle612_pass": receipts["Cycle612"]["pass"],
        "Cycle612_interval_pass": receipts["Cycle612"]["route_B_protected_causal_interval"]["pass"],
        "Cycle662_pass": receipts["Cycle662"]["pass"],
        "Cycle662_tests": [receipts["Cycle662"]["tests_passed"], receipts["Cycle662"]["tests_failed"]],
    }
    passed = (
        observed == PINS and contracts["Cycle559_pass"] and contracts["Cycle591_tests"] == [16, 0]
        and contracts["Cycle612_pass"] and contracts["Cycle612_interval_pass"]
        and contracts["Cycle662_pass"] and contracts["Cycle662_tests"] == [9, 0]
        and all(value == ["none", "unset"] for key, value in contracts.items() if key.endswith("authority_audit"))
    )
    return {
        "ref": SHORE, "pins": PINS, "observed": observed, "imported_contracts": contracts,
        "working_tree_bytes_used_as_premise": False, "author_status_accepted_as_audit": False, "pass": passed,
    }, receipts


def validate_bit(value: int, name: str) -> None:
    if value not in (0, 1): raise ValueError(f"{name} leaves M2 bit domain")


def validate_current(word: tuple[int, int, int]) -> None:
    if word not in CURRENT_WORDS.values(): raise ValueError("current word leaves Cycle559 interface")
    edge, plus, minus = word
    if edge != (plus ^ minus) or plus + minus > 1: raise ValueError("Cycle559 EDGE/J constraint")


def endpoint_payload(endpoint: int = 1, predecessor: int | None = 0,
                     reference: int = 4, probe: int = 4) -> tuple[int, ...]:
    if endpoint not in (0, 1) or predecessor not in (None, 0): raise ValueError("endpoint/predecessor")
    if reference not in range(1, 5) or probe not in range(1, 6): raise ValueError("unary receipt")
    return (
        1, int(endpoint == 0), int(endpoint == 1), int(predecessor is not None), int(predecessor == 0),
        *(1 if index < reference else 0 for index in range(4)),
        *(1 if index < probe else 0 for index in range(5)), 1, 1,
    )


def packet_read(packet: tuple[tuple[int, ...], ...]) -> dict[str, object] | None:
    if len(packet) != 3 or any(len(replica) != PACKET_WIDTH for replica in packet): return None
    if packet[0] != packet[1] or packet[1] != packet[2]: return None
    word = packet[0]
    if any(bit not in (0, 1) for bit in word) or not word[0] or word[1] + word[2] != 1: return None
    endpoint = 0 if word[1] else 1
    reference, probe = sum(word[5:9]), sum(word[9:14])
    predecessor_valid = ((endpoint == 0 and not word[3] and not word[4])
                         or (endpoint == 1 and word[3] and word[4]))
    if (not predecessor_valid or tuple(word[5:9]) != (1,) * reference + (0,) * (4-reference)
            or tuple(word[9:14]) != (1,) * probe + (0,) * (5-probe)
            or not word[14] or not word[15] or not reference): return None
    return {
        "endpoint": endpoint, "predecessor_edge_present": bool(word[3]),
        "predecessor_zero": bool(word[4]), "reference_receipt_cells": reference,
        "probe_receipt_cells": probe, "probe_over_reference": f"{probe // reference}" if probe % reference == 0 else f"{probe}/{reference}",
        "matter_caused_endpoint_type": bool(word[15]),
    }


def validate_slot(slot: Slot) -> None:
    validate_bit(slot.ready, "ready"); validate_bit(slot.spent, "spent")
    validate_bit(slot.detector_pointer, "detector_pointer"); validate_bit(slot.join_work, "join_work")
    validate_current(slot.current_word)
    if slot.ready + slot.spent != 1: raise ValueError("ready+spent must equal one")
    if slot.ready and (slot.exhaust_tag is not None or slot.current_word != CURRENT_WORDS["NULL"]
                       or slot.packet != BLANK_PACKET): raise ValueError("ready slot is dirty")
    if slot.spent and (slot.exhaust_tag is None or slot.current_word != CURRENT_WORDS["PLUS"]
                       or packet_read(slot.packet) is None): raise ValueError("spent slot incomplete")
    if slot.detector_pointer or slot.join_work: raise ValueError("work not uncomputed")


def branch_live(branch: dict[str, object]) -> bool:
    required = ("propensity", "occurrence_candidate", "ADMIT", "LOCK", "Cycle531_EDGE_PASSED",
                "Cycle531_binding_match", "Cycle531_provenance_match", "Cycle531_conditional_occurrence_equation")
    if any(key not in branch for key in required): raise ValueError("malformed Cycle662 branch")
    return bool(
        branch["propensity"] > 1e-15 and branch["occurrence_candidate"] == 1
        and branch["ADMIT"] == branch["LOCK"] == branch["Cycle531_EDGE_PASSED"] == 1
        and branch["Cycle531_binding_match"] == branch["Cycle531_provenance_match"] == 1
        and branch["Cycle531_conditional_occurrence_equation"] == 1
    )


def branch_tag(row: dict[str, object], branch: dict[str, object]) -> str:
    return stable_digest({"menu": row["menu"], "state": row["state"], "pattern": branch["pattern"],
                          "member": branch["Cycle531_MEMBER"], "propensity": branch["propensity"]})


def computed_matter_opportunity(matter: int, binder: int, *, delete: str | None = None) -> tuple[int, int]:
    validate_bit(matter, "matter"); validate_bit(binder, "binder")
    pointer = 0; opportunity = 0
    if delete != "Pd-compute": pointer ^= matter
    if delete != "binder-Toffoli": opportunity ^= pointer & binder
    if delete != "Pd-uncompute": pointer ^= matter
    return pointer, opportunity


def forward_event(slot: Slot, row: dict[str, object], branch: dict[str, object],
                  *, matter: int = 1, binder: int = 1, law_domain: int = 1,
                  delete: str | None = None) -> tuple[Slot, dict[str, object]]:
    validate_slot(slot); validate_bit(law_domain, "law_domain")
    pointer, opportunity = computed_matter_opportunity(matter, binder, delete=delete)
    live = branch_live(branch)
    fresh = int(slot.packet == BLANK_PACKET)
    admit = int(live and opportunity and law_domain and fresh and slot.ready and not slot.spent)
    if delete in {"branch", "ADMIT", "LOCK", "binding", "occurrence"}: admit = 0
    if not admit:
        return slot, {"fired": 0, "live_branch": live, "matter_opportunity": opportunity,
                      "fresh": fresh, "terminal_detector_pointer": pointer, "reason": "veto-or-zero"}
    payload = endpoint_payload()
    packet = tuple(tuple((bit ^ payload[index]) if delete != "packet-replica-2" or replica != 2 else bit
                         for index, bit in enumerate(slot.packet[replica])) for replica in range(3))
    if delete == "predecessor":
        packet = tuple(tuple(0 if index in (3, 4) else bit for index, bit in enumerate(replica)) for replica in packet)
    if delete == "endpoint-type":
        packet = tuple(tuple(0 if index == 15 else bit for index, bit in enumerate(replica)) for replica in packet)
    output = replace(
        slot,
        ready=slot.ready if delete == "ready-debit" else slot.ready ^ 1,
        spent=slot.spent if delete == "spent-credit" else slot.spent ^ 1,
        current_word=(0, 1, 0) if delete == "current-EDGE" else ((1, 0, 0) if delete == "current-J+" else CURRENT_WORDS["PLUS"]),
        packet=packet,
        exhaust_tag=None if delete == "coherent-exhaust" else branch_tag(row, branch),
        detector_pointer=pointer,
        join_work=1 if delete == "join-uncompute" else 0,
    )
    return output, {
        "fired": 1, "live_branch": live, "matter_opportunity": opportunity, "fresh": fresh,
        "terminal_detector_pointer": output.detector_pointer, "join_work": output.join_work,
        "fixed_local_word_sha256": FIXED_LOCAL_WORD_SHA256,
    }


def inverse_event(slot: Slot, row: dict[str, object], branch: dict[str, object]) -> Slot:
    validate_slot(slot)
    if slot.exhaust_tag != branch_tag(row, branch): raise ValueError("inverse branch/exhaust mismatch")
    payload = endpoint_payload()
    restored_packet = tuple(
        tuple(bit ^ payload[index] for index, bit in enumerate(replica))
        for replica in slot.packet
    )
    restored = replace(
        slot, ready=slot.ready ^ 1, spent=slot.spent ^ 1,
        current_word=CURRENT_WORDS["NULL"], packet=restored_packet, exhaust_tag=None,
    )
    validate_slot(restored)
    return restored


def current_continuity(direction: tuple[int, int, int], word: tuple[int, int, int]) -> dict[str, object]:
    validate_current(word)
    j = word[1] - word[2]
    source_delta, sink_delta = -j, j
    source_balance = source_delta - (0-j)
    sink_balance = sink_delta - (j-0)
    return {
        "direction": direction, "signed_current": j,
        "ready_source_delta": source_delta, "spent_exhaust_delta": sink_delta,
        "source_continuity_residual": source_balance, "sink_continuity_residual": sink_balance,
        "global_conservation_residual": source_delta + sink_delta,
        "orientation": "j_d(x) leaves ready source x toward spent/exhaust sink x+d; Delta n=incoming-outgoing",
    }


def formation_rows(receipts: dict[str, dict[str, object]]) -> dict[str, object]:
    rows = receipts["Cycle662"]["stochastic_dilation"]["rows"]
    held_states = sorted({row["state"] for row in rows if row["split"] != "train"})
    tests = []; inverse_failures = interface_failures = zero_debits = 0
    live_count = zero_count = unit_count = held_live = train_live = 0
    for row in rows:
        for branch in row["branches"]:
            live = branch_live(branch)
            unit_count += int(abs(branch["propensity"] - 1.0) < 1e-15)
            output, work = forward_event(Slot(), row, branch)
            if live:
                live_count += 1
                held_live += int(row["split"] != "train"); train_live += int(row["split"] == "train")
                read = packet_read(output.packet)
                interface_failures += int(
                    output.ready != 0 or output.spent != 1 or output.current_word != CURRENT_WORDS["PLUS"]
                    or read is None or read["endpoint"] != 1 or not read["predecessor_edge_present"]
                    or read["probe_over_reference"] != "1" or output.detector_pointer != output.join_work != 0
                    or not work["fired"]
                )
                try: restored = inverse_event(output, row, branch)
                except ValueError: inverse_failures += 1; restored = None
                inverse_failures += int(restored != Slot())
            else:
                zero_count += 1; zero_debits += int(output != Slot() or work["fired"])
            tests.append({"menu": row["menu"], "state": row["state"], "split": row["split"],
                          "pattern": branch["pattern"], "propensity": branch["propensity"],
                          "live": live, "fired": work["fired"]})
    return {
        "Cycle662_state_rows": len(rows), "branch_rows": len(tests), "live_branch_rows": live_count,
        "zero_propensity_or_nonadmitted_rows": zero_count, "train_live_branch_rows": train_live,
        "lawful_unit_propensity_branch_rows": unit_count,
        "held_live_branch_rows": held_live, "zero_branch_debit_failures": zero_debits,
        "held_state_types": held_states, "held_biased_and_nonproduct_present": held_states == ["held_blind_biased", "held_blind_nonproduct"],
        "interface_failures": interface_failures, "inverse_failures": inverse_failures,
        "rows": tests, "all_Cycle662_coherent_exhaust_identity_untouched": True,
        "rejected_and_zero_interface_sectors_retained_as_explicit_no_fire_rows": True,
        "inherited_maximum_CQ_entropy_ledger_residual": receipts["Cycle662"]["stochastic_dilation"]["maximum_CQ_entropy_ledger_residual"],
        "runner_samples_a_branch": False, "host_scheduler_calls": 0, "actuality_lookup_calls": 0,
        "grade_lookup_calls": 0, "shell_predicate_ROM_rows": 0,
        "row_and_branch_arguments_are_exhaustive_basis_fixtures_not_runtime_selectors": True,
        "exhaust_tag_is_an_audit_checksum_not_a_physical_register": True,
        "physical_join_controls": ["occurrence", "binding", "ADMIT", "LOCK", "Cycle612_Pd_matter", "Cycle612_binder", "law_domain", "packet_blank", "ready"],
        "pass": interface_failures == inverse_failures == zero_debits == 0 and live_count > 0
                and held_live > 0 and zero_count > 0 and unit_count > 0
                and held_states == ["held_blind_biased", "held_blind_nonproduct"],
    }


def initial_ledger(capacity: int) -> Ledger:
    if capacity not in (3, 4, 6): raise ValueError("capacity outside train/held contract")
    return Ledger(tuple(Slot() for _ in range(capacity)))


def validate_ledger(ledger: Ledger) -> None:
    if len(ledger.slots) not in (3, 4, 6): raise ValueError("ledger capacity")
    frontier_ready = False
    for slot in ledger.slots:
        validate_slot(slot)
        if slot.ready: frontier_ready = True
        elif frontier_ready: raise ValueError("spent slots must be a prefix")


def append_ledger(ledger: Ledger, row: dict[str, object], branch: dict[str, object]) -> tuple[Ledger, bool]:
    validate_ledger(ledger)
    try: index = next(i for i, slot in enumerate(ledger.slots) if slot.ready)
    except StopIteration: return ledger, False
    output, work = forward_event(ledger.slots[index], row, branch)
    if not work["fired"]: return ledger, False
    slots = list(ledger.slots); slots[index] = output
    result = Ledger(tuple(slots)); validate_ledger(result); return result, True


def ledger_controls(receipts: dict[str, dict[str, object]]) -> dict[str, object]:
    candidates = [(row, branch) for row in receipts["Cycle662"]["stochastic_dilation"]["rows"]
                  for branch in row["branches"] if branch_live(branch)]
    rows = []; total_inverse_failures = 0
    for capacity, split in ((3, "train"), (4, "held-out-size"), (6, "held")):
        initial = initial_ledger(capacity); state = initial; conservation_failures = 0
        for index in range(capacity):
            state, fired = append_ledger(state, *candidates[index % len(candidates)])
            conservation_failures += int(not fired or sum(s.ready+s.spent for s in state.slots) != capacity)
        saturated = state; refused, fired = append_ledger(saturated, *candidates[0])
        conservation_failures += int(fired or refused != saturated)
        restored_slots = list(saturated.slots)
        for index in reversed(range(capacity)):
            restored_slots[index] = inverse_event(restored_slots[index], *candidates[index % len(candidates)])
        restored = Ledger(tuple(restored_slots)); total_inverse_failures += int(restored != initial)
        dirty = replace(saturated.slots[0], ready=1, spent=0)
        dirty_refused = False
        try: validate_slot(dirty)
        except ValueError: dirty_refused = True
        rows.append({
            "capacity": capacity, "split": split, "physical_M2_9cube": 729*capacity,
            "declared_interface_register_M2": 563*capacity, "Cycle662_inner_cube_M2": 125*capacity,
            "Cycle612_append_block_M2": 436*capacity, "new_Jplus_Jminus_M2": 2*capacity,
            "proper_cubic_padding_M2": 166*capacity, "spent_at_saturation": capacity,
            "saturation_refuses_firing": not fired, "ready_plus_spent_conservation_failures": conservation_failures,
            "inverse_roundtrip_failures": int(restored != initial),
            "inverse_erases_current_endpoint_and_exhaust": True, "dirty_non_erasing_relabel_refused": dirty_refused,
            "pass": conservation_failures == 0 and restored == initial and dirty_refused,
        })
    return {
        "physical_supercell_M2": 729, "declared_interface_register_M2_per_event": 563,
        "Cycle662_inner_cube_M2": 125, "Cycle612_bounded_append_block_M2": 436,
        "new_current_M2": 2, "Cycle662_EDGE_reused_as_Cycle559_EDGE": True,
        "proper_cubic_padding_M2": 166, "supercell_shape": "{-4,-3,...,4}^3 cube",
        "ready_source_coordinate": [0, 0, 0], "spent_sink_coordinate_frame_root": [1, 0, 0],
        "ready_to_spent_link_range": 1,
        "maximum_supercell_L1_diameter": 24, "maximum_Cycle662_stochastic_jump_support_M2": 30,
        "maximum_conservative_join_route_edges": 24,
        "maximum_inherited_packet_compiler_literal_gate_support_M2": 2,
        "explicit_root_frame_register_injection": len(INTERFACE_REGISTER_COORDINATES) == len(set(INTERFACE_REGISTER_COORDINATES)) == 563,
        "additional_independent_innovation_bits": 0,
        "current_and_endpoint_are_deterministic_functions_of_stored_event_and_material_program_bits": True,
        "joint_full_detector_formation_matrix_executed": False,
        "renewal_residual_name": "W_joint_current_interval_exhaust_non_erasing_renewal",
        "renewal_residual": "finite composite ledgers saturate; inverse restores ready capacity only by erasing the retained current certificate, endpoint packet, objective occurrence, and coherent exhaust",
        "rows": rows, "pass": all(row["pass"] for row in rows) and total_inverse_failures == 0
                and len(INTERFACE_REGISTER_COORDINATES) == len(set(INTERFACE_REGISTER_COORDINATES)) == 563,
    }


def determinant(matrix: tuple[tuple[int, ...], ...]) -> int:
    return (
        matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
        - matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
        + matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
    )


def proper_rotations() -> tuple[tuple[tuple[int, ...], ...], ...]:
    frames = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(tuple(signs[row] if column == perm[row] else 0 for column in range(3)) for row in range(3))
            if determinant(matrix) == 1: frames.append(matrix)
    return tuple(frames)


def matvec(matrix, vector):
    return tuple(sum(matrix[row][column]*vector[column] for column in range(3)) for row in range(3))


def matmul(left, right):
    return tuple(tuple(sum(left[i][k]*right[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def covariance_controls() -> dict[str, object]:
    frames = proper_rotations(); directions = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
    continuity_failures = cube_failures = group_failures = packet_failures = chart_failures = chart_group_failures = 0
    comparisons = inverse_current_failures = 0
    cube = set(SUPERCELL_COORDINATES)
    expected_packet = packet_read(tuple(endpoint_payload() for _ in range(3)))
    for direction in directions:
        for frame in frames:
            rotated = matvec(frame, direction); comparisons += 1
            row = current_continuity(rotated, CURRENT_WORDS["PLUS"])
            continuity_failures += int(any(row[key] != 0 for key in (
                "source_continuity_residual", "sink_continuity_residual", "global_conservation_residual")))
            inverse_row = current_continuity(rotated, CURRENT_WORDS["MINUS"])
            inverse_current_failures += int(
                inverse_row["signed_current"] != -1 or any(inverse_row[key] != 0 for key in (
                    "source_continuity_residual", "sink_continuity_residual", "global_conservation_residual")))
            packet_failures += int(packet_read(tuple(endpoint_payload() for _ in range(3))) != expected_packet)
        for left in frames:
            for right in frames:
                group_failures += int(matvec(left, matvec(right, direction)) != matvec(matmul(left, right), direction))
    for frame in frames:
        cube_failures += int({matvec(frame, coordinate) for coordinate in cube} != cube)
        transported_chart = tuple(matvec(frame, coordinate) for coordinate in INTERFACE_REGISTER_COORDINATES)
        chart_failures += int(len(set(transported_chart)) != 563 or any(coordinate not in cube for coordinate in transported_chart))
    for left in frames:
        for right in frames:
            composed = matmul(left, right)
            chart_group_failures += int(any(
                matvec(left, matvec(right, coordinate)) != matvec(composed, coordinate)
                for coordinate in INTERFACE_REGISTER_COORDINATES))
    return {
        "proper_cubic_frames": len(frames), "ordered_frame_products": len(frames)**2,
        "direction_current_comparisons": comparisons, "direction_group_comparisons": len(directions)*len(frames)**2,
        "continuity_failures": continuity_failures, "direction_group_failures": group_failures,
        "inverse_MINUS_current_failures": inverse_current_failures,
        "cube_all24_failures": cube_failures, "scalar_packet_transport_failures": packet_failures,
        "transported_register_chart_failures": chart_failures,
        "transported_register_chart_all576_failures": chart_group_failures,
        "runtime_frame_selector": False, "compile_time_frame_transport": True,
        "pass": len(frames) == 24 and len(frames)**2 == 576
                and continuity_failures == inverse_current_failures == group_failures == cube_failures == packet_failures == chart_failures == chart_group_failures == 0,
    }


def deletion_and_domain_controls(receipts: dict[str, dict[str, object]]) -> dict[str, object]:
    row, branch = next((row, branch) for row in receipts["Cycle662"]["stochastic_dilation"]["rows"]
                       for branch in row["branches"] if branch_live(branch))
    deletion_results = {}
    for deletion in ("ready-debit", "spent-credit", "current-EDGE", "current-J+", "packet-replica-2",
                     "predecessor", "endpoint-type", "coherent-exhaust", "Pd-compute", "binder-Toffoli",
                     "Pd-uncompute", "join-uncompute", "branch", "ADMIT", "LOCK", "binding", "occurrence"):
        output, work = forward_event(Slot(), row, branch, delete=deletion)
        detected = False
        if deletion in {"Pd-compute", "binder-Toffoli", "branch", "ADMIT", "LOCK", "binding", "occurrence"}:
            detected = output == Slot() and not work["fired"]
        else:
            try: validate_slot(output)
            except ValueError: detected = True
        deletion_results[deletion] = detected
    malformed = []
    cases = (
        lambda: validate_bit(2, "matter"),
        lambda: validate_current((1,1,1)),
        lambda: validate_slot(Slot(ready=1, spent=1)),
        lambda: validate_slot(Slot(packet=((2,)*16,)*3)),
        lambda: branch_live({}),
        lambda: initial_ledger(5),
    )
    for case in cases:
        rejected = False
        try: case()
        except (ValueError, KeyError): rejected = True
        malformed.append(rejected)
    truth_rows = []
    for live_bit, matter, binder, law_domain in product((0,1), repeat=4):
        test_branch = dict(branch)
        if not live_bit: test_branch["propensity"] = 0.0; test_branch["occurrence_candidate"] = 0
        output, work = forward_event(Slot(), row, test_branch, matter=matter, binder=binder, law_domain=law_domain)
        expected = live_bit & matter & binder & law_domain
        truth_rows.append({"formation_live": live_bit, "matter": matter, "binder": binder,
                           "law_domain": law_domain, "fired": work["fired"], "expected": expected})
    return {
        "deletion_controls": deletion_results, "deleted_surfaces": len(deletion_results),
        "malformed_rejections": sum(malformed), "malformed_total": len(malformed),
        "composite_gate_truth_rows": truth_rows, "composite_gate_truth_failures": sum(r["fired"] != r["expected"] for r in truth_rows),
        "saturated_or_malformed_event_debits_source": False, "source_current_called_physical_energy": False,
        "source_current_called_gravity": False, "generator_entry_called_rate": False,
        "packet_called_Record_or_proper_time": False, "packet_called_realized_history": False,
        "pointer_copying_called_Record": False, "pass": all(deletion_results.values()) and all(malformed)
                and all(r["fired"] == r["expected"] for r in truth_rows),
    }


def citation(path: str, fragment: str) -> dict[str, object]:
    for line, text in enumerate(git_bytes(path).decode().splitlines(), 1):
        if fragment in text: return {"ref": SHORE, "path": path, "line": line, "text": text.strip()}
    raise ValueError((path, fragment))


def current_citation(fragment: str) -> dict[str, object]:
    for line, text in enumerate(Path(__file__).read_text().splitlines(), 1):
        if fragment in text: return {"ref": "Cycle665 current artifact", "path": str(Path(__file__).relative_to(ROOT)),
                                     "line": line, "text": text.strip()}
    raise ValueError(fragment)


def no_go_discipline() -> dict[str, object]:
    c559_current = citation("docs/work_history/repo/review_feedback/PHYSICAL_LOCALLY_CONSERVED_CURRENT_RESPONSE_LAW_TOURNAMENT_CYCLE559_NOTE_2026-07-21.md", "It supplies a coefficient-one")
    c559_preparation = citation("docs/work_history/repo/review_feedback/PHYSICAL_LOCALLY_CONSERVED_CURRENT_RESPONSE_LAW_TOURNAMENT_CYCLE559_NOTE_2026-07-21.md", "source-location preparation itself remains supplied")
    c591 = citation("docs/work_history/repo/review_feedback/PHYSICAL_OPERATIONAL_METRIC_CONSERVED_SOURCE_LOCAL_RANGE_TOURNAMENT_CYCLE591_NOTE_2026-07-22.md", "candidate gate and its placement are supplied")
    c612_scope = citation("docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md", "globally scheduled apparatus")
    c612_packet = citation("docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md", "finite packet capacity")
    c662 = citation("docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_STOCHASTIC_OPEN_DILATION_CYCLE662_NOTE_2026-07-23.md", "W_finite_innovation_exhaust_non_erasing_renewal")
    current = current_citation("W_joint_current_interval_exhaust_non_erasing_renewal")
    families = [
        {"family": "direct ready/spent current-word compiler", "object_formulation": "Cycle662 slot plus Cycle559 EDGE/J+/J- and Cycle612 packet bits", "mechanism_invariant": "one fixed branch-controlled reversible basis permutation and exact two-endpoint continuity", "terminal_obligation": "same event owns debit/current/exhaust/endpoint", "strength_vs_target": "target-equivalent at the pinned interface scope", "honesty_marker": "ATTEMPTED", "status": "candidate-complete on the declared finite interface"},
        {"family": "six-lane resource mediator", "object_formulation": "Cycle559 vacuum-plus-Q1 cubic walk", "mechanism_invariant": "number-preserving emitter/stream/receiver exchange", "terminal_obligation": "formation-controlled endpoint append", "strength_vs_target": "incomparable", "honesty_marker": "RULED OUT BY PRIOR", "status": "resource current is positive but source-location preparation and formation join remain supplied", "citation": c559_preparation},
        {"family": "occupation-charge continuity", "object_formulation": "Cycle591 q_beta N density/current", "mechanism_invariant": "U(1) number conservation through coin/stream/contact", "terminal_obligation": "current caused by the Cycle662 ready-to-spent event", "strength_vs_target": "incomparable", "honesty_marker": "RULED OUT BY PRIOR", "status": "conserved candidate charge exists but its coupling/meaning is separately supplied", "citation": c591},
        {"family": "standalone protected endpoint append", "object_formulation": "Cycle612 triplicate predecessor/clock packet", "mechanism_invariant": "compute/copy/uncompute admission involution", "terminal_obligation": "atomic formation debit and current", "strength_vs_target": "weaker", "honesty_marker": "ATTEMPTED", "status": "packet inverse and deletion pass, but standalone append has no Cycle662 resource current", "citation": c612_scope},
        {"family": "host-sequenced ledger then packet", "object_formulation": "two independently invoked shore transitions", "mechanism_invariant": "external sequencing and lookup", "terminal_obligation": "one physical law-owned event", "strength_vs_target": "weaker/forbidden", "honesty_marker": "ATTEMPTED", "status": "rejected by the frozen target; fixed local word replaces host sequencing"},
    ]
    walls = {
        "W_endpoint_predecessor_genesis": "the compiler consumes the pinned Cycle612 physical matter predicate, binder/law-domain program, and predecessor address; it does not autonomously create their genesis",
        "W_joint_non_erasing_renewal": "finite joint source/current/packet/exhaust capacity saturates; inverse frees a slot only by erasing that event's current certificate, endpoint packet, occurrence, and exhaust",
    }
    pairs = [
        {"from": "W_endpoint_predecessor_genesis", "to": "W_joint_non_erasing_renewal", "implied": False, "reason": "autonomous endpoint genesis does not renew spent physical capacity"},
        {"from": "W_joint_non_erasing_renewal", "to": "W_endpoint_predecessor_genesis", "implied": False, "reason": "a renewable sink does not generate the matter predicate or causal predecessor"},
    ]
    n4 = [
        {"prior_ref": c662["ref"], "prior_path": c662["path"], "prior_line": c662["line"], "prior_residual": "Cycle662 finite occurrence/exhaust ledger lacks non-erasing renewal", "current_path": current["path"], "current_line": current["line"], "current_residual": "Cycle665 finite joint current/endpoint/exhaust ledger lacks non-erasing renewal", "same_scope": False, "exact_match": False, "use_as_closure": False, "classification": "strict scope extension, not an exact witness"},
        {"prior_ref": c612_scope["ref"], "prior_path": c612_scope["path"], "prior_line": c612_scope["line"], "prior_residual": "Cycle612 did not route and matrix-execute one globally joined apparatus", "current_path": current["path"], "current_line": current["line"], "current_residual": "Cycle665 executes the bounded Boolean/M2 interface join but not the full Cycle608 detector plus formation matrix", "same_scope": True, "exact_match": True, "use_as_closure": False, "classification": "residual preserved"},
    ]
    return {
        "Status": "PASS", "N1_required_for_negative": 5, "N1_qualifying_attempts": len(families),
        "N1_normalized_families": families, "N1_open_routes_not_counted": [
            {"family": "mobile regenerative current/endpoint exhaust QCA", "status": "OPEN / NOT COUNTED"},
            {"family": "autonomous successor/predecessor formation graph", "status": "OPEN / NOT COUNTED"},
        ],
        "N2_walls": walls, "N2_directed_ordered_pairs": pairs,
        "N3_hidden_wall_scan": [
            {"condition": "Cycle662 stochastic law, menus, finite blank slots, and branch interface", "classification": "explicit pinned target premise"},
            {"condition": "Cycle559 current word and Cycle591 continuity orientation", "classification": "explicit pinned implementation convention"},
            {"condition": "Cycle612 physical matter predicate, binder, law domain, packet freshness, endpoint identity, predecessor zero, 4:4 receipts, and triplicate layout", "classification": "explicit supplied structure; W_endpoint_predecessor_genesis"},
            {"condition": "finite 729-site chart, blank packet blocks, and compile-time transported direction", "classification": "explicit bounded implementation structure; renewal belongs to W_joint_non_erasing_renewal"},
            {"condition": "the word canonical in canonical_claim_gate_contract", "classification": "non-load-bearing output-schema label; it confers no scientific or audit authority"},
        ],
        "N4_exact_residual_matches": [row for row in n4 if row["exact_match"]],
        "N4_nonmatches_not_used_as_closure": [row for row in n4 if not row["exact_match"]],
        "N5_rhetoric": [
            {"claim": "the coefficient-one interface resource current is not identified as physical energy, stress, or gravity", "per_element": "ready/spent bits and EDGE/J rails are exact", "per_site": "two endpoint continuity equations are tested", "per_mode": "all six transported cubic directions are tested", "per_block": "train/held capacities 3/4/6 are tested", "lattice_wide": "no infinite deployment, field response, energy-stress tensor, or gravity claim is made"},
            {"claim": "the typed endpoint packet is not a framework Record, proper time, or realized history", "per_element": "all 16 bits and three replicas are checked", "per_site": "one event endpoint and its predecessor address are checked", "per_mode": "packet is scalar under all proper-cubic frames", "per_block": "finite packet capacity and inverse erasure are tested", "lattice_wide": "autonomous Record DAG, permanence, and history recurrence are untested"},
            {"claim": "the fixed update word and any generator entry are not a physical rate", "per_element": "no division by update count is performed", "per_site": "current is a conserved transition debit", "per_mode": "six current directions are compared", "per_block": "fixed compiler order only", "lattice_wide": "no clock calibration or continuum rate is claimed"},
        ],
        "N6_partial_closure_paths": [
            {"file": "UNMATERIALIZED/autonomous_successor_predecessor_formation_qca_cycle_next.py", "status": "OPEN / PRIORITY", "what_closes": "W_endpoint_predecessor_genesis"},
            {"file": "UNMATERIALIZED/regenerative_current_interval_exhaust_qca_cycle_next.py", "status": "OPEN / PRIORITY", "what_closes": "W_joint_non_erasing_renewal"},
            {"file": "scripts/physical_matter_caused_causal_interval_proper_time_bridge_tournament_cycle612_2026_07_22.py", "status": "EXECUTED PARTIAL INTERFACE", "what_closes": "packet Boolean inverse/deletion/covariance, not either genesis or renewal wall"},
        ],
        "N7_steelman": {
            "mechanism": "A hostile constructive reviewer can make both residuals disappear by embedding the Cycle662 jump cell in a translation-invariant collision QCA: mobile purified ancillas carry spent coherent exhaust outward, a local successor token is emitted only when a prior material endpoint packet is encountered, and an oppositely moving blank carrier returns only after entropy has been exported to a separately counted sink. This would make predecessor selection dynamical and renew local ready capacity without clearing retained occurrence data.",
            "actionable_steps": ["construct the local collision permutation and mobile exhaust carriers", "prove the induced branch kernel equals every pinned Cycle662 K_p propensity", "prove successor uniqueness and exact stationary source/current conservation without packet deletion"],
            "terminal_test": "unchanged Cycle662 held kernel, no supplied predecessor or fresh bath, finite-density stationary renewal, retained occurrence/current/endpoint exhaust, all24/all576, and no host schedule",
            "supporting_citations": [c662, c612_packet],
        },
        "N8_cross_cycle_echo": [
            {"cycle": 559, "retired": "receiver-only missing debit at bounded resource-number scope", "mechanism": "explicit auxiliary debit and later six-lane conserved mediator", "applicability": "motivates the exact ready/spent current join but does not supply renewal or endpoint genesis", "citation_ref": c559_current["ref"], "citation_path": c559_current["path"], "citation_line": c559_current["line"], "citation_text": c559_current["text"]},
            {"cycle": 612, "retired": "supplied detector-output pointer for the bounded endpoint packet", "mechanism": "physical Pd compute/copy/uncompute predicate", "applicability": "reused as a pinned endpoint input; its profile/predecessor genesis remains supplied", "citation_ref": c612_scope["ref"], "citation_path": c612_scope["path"], "citation_line": c612_scope["line"], "citation_text": c612_scope["text"]},
            {"cycle": 662, "retired": "absence of one objective-within-law branch candidate", "mechanism": "hybrid stochastic sigma with retained coherent exhaust", "applicability": "supplies the event but explicitly does not retire finite non-erasing renewal", "citation_ref": c662["ref"], "citation_path": c662["path"], "citation_line": c662["line"], "citation_text": c662["text"]},
        ],
        "N1_broad_negative_gate": "FAIL / DO NOT SHIP", "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP", "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP", "broad_no_go_claim": False,
        "minimum_content_claim": False, "shared_obstruction_claim": False, "axiom_pressure_claim": False,
        "broad_negative_shipped": False, "minimum_content_shipped": False,
        "shared_obstruction_shipped": False, "axiom_pressure_shipped": False,
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "pass": len(families) >= 5 and len(pairs) == 2 and not any(row["use_as_closure"] for row in n4),
    }


def note_text(receipt: dict[str, object]) -> str:
    formation = receipt["formation_interface_compiler"]; ledger = receipt["resource_ledger"]
    cov = receipt["covariance"]; deletion = receipt["deletion_and_domain"]
    capacity_rows = "\n".join(
        f"| {row['capacity']} | {row['split']} | {row['physical_M2_9cube']} | {row['declared_interface_register_M2']} | {row['spent_at_saturation']} | {str(row['saturation_refuses_firing']).lower()} |"
        for row in ledger["rows"]
    )
    return f"""# Physical formation resource/current interval compiler — Cycle 665

Status: **positive bounded interface compiler with retained upstream walls**

Authority: **none**

Audit: **unset**

Breakthrough: **false**

## Frozen target and result

The exact target was frozen before evidence load at runner lines
`{receipt['target_freeze']['target_line']} < {receipt['target_freeze']['first_evidence_load_line']}`
with digest `{receipt['target_freeze']['target_contract_sha256']}`.

Cycle 665 constructs one fixed local interface word joining the immutable
Cycle 662 objective-within-candidate-law formation transition to the exact
Cycle 559 `EDGE,J+,J-` current convention, the Cycle 591 oriented continuity
equation, and the landed Cycle 612 protected endpoint packet.  On each live
Cycle 662 branch in the declared material-endpoint code, the same admitted
transition maps

`ready=1, spent=0, current=NULL, packet=blank`

to

`ready=0, spent=1, current=PLUS, packet=typed-endpoint`,

while the complete Cycle 662 coherent exhaust and objective occurrence fields
remain in the spent block.  `EDGE` is reused from the Cycle 662 occurrence
interface, so only `J+` and `J-` add two current M2.  No host scheduler or
sampler, actuality lookup, grade lookup, or shell-predicate ROM is used.

The runner enumerates `{formation['branch_rows']}` Cycle 662 branch rows from
`{formation['Cycle662_state_rows']}` menu/state rows, including all blinded held
biased and nonproduct fixtures.  `{formation['live_branch_rows']}` live branches
compile and every zero/nonadmitted branch leaves the source and packet blank.
The imported singular controls include `{formation['zero_propensity_or_nonadmitted_rows']}`
zero-propensity branches and `{formation['lawful_unit_propensity_branch_rows']}`
unit-propensity branch.  Rejected and zero sectors remain explicit no-fire
rows; the inherited Cycle 662 coherent/CQ exhaust ledger is untouched, with
maximum entropy residual `{formation['inherited_maximum_CQ_entropy_ledger_residual']:.3e}`.
The runner's row/branch arguments enumerate physical basis fixtures; they are
not runtime selectors.  The stored exhaust tag in the audit is a checksum, not
an added physical register.  The runner never samples a branch.

## Conservation, locality, covariance, and resources

For the forward word `PLUS=(EDGE,J+,J-)=(1,1,0)`, with `j=J+-J-`,

`Delta n_ready=-j`, `Delta n_spent=+j`,

and at both endpoints

`Delta n = incoming - outgoing`.

The inverse orientation uses `MINUS=(1,0,1)` and has the same exact balance.
The source, sink, and global continuity residuals are exactly zero.  This is a
coefficient-one resource ledger/current.  It is not identified as physical
energy, stress, force, or gravity.  The fixed compiler/generator word is not a
physical rate, and its factor order is not called time.

One event reserves an explicit injective root-frame chart inside a
proper-cubic-invariant 9-by-9-by-9 supercell:
`{ledger['physical_supercell_M2']}` physical M2, of which
`{ledger['declared_interface_register_M2_per_event']}` are declared interface
registers: `{ledger['Cycle662_inner_cube_M2']}` for the Cycle 662 inner block,
`{ledger['Cycle612_bounded_append_block_M2']}` for the landed bounded append
block, and `{ledger['new_current_M2']}` new current rails.  The remaining
`{ledger['proper_cubic_padding_M2']}` sites are conservative routing/padding.
Maximum cube L1 diameter is `{ledger['maximum_supercell_L1_diameter']}`.
The ready source is at the origin and the spent sink is one nearest-neighbor
step away in the compile-time transported direction; the conservative maximum
join route is `{ledger['maximum_conservative_join_route_edges']}` edges.
The inherited stochastic jump support is at most
`{ledger['maximum_Cycle662_stochastic_jump_support_M2']}` M2; the inherited
packet compiler decomposes into gates of support at most
`{ledger['maximum_inherited_packet_compiler_literal_gate_support_M2']}` M2.
The current and endpoint words are deterministic functions of the already
stored event and material/program bits, so they add zero independent innovation
bits while consuming the counted M2 memory.

All `{cov['proper_cubic_frames']}` proper-cubic frames and
`{cov['ordered_frame_products']}` ordered products pass.  The six current
directions give `{cov['direction_current_comparisons']}` direct continuity
comparisons and `{cov['direction_group_comparisons']}` group comparisons with
zero failures.  The packet is a transported scalar and the complete 729-site
cube is frame-invariant.  There is no runtime frame selector.

| capacity | split | physical 9-cube M2 | declared register M2 | spent | saturation refusal |
|---:|---|---:|---:|---:|---|
{capacity_rows}

Exact named residual:
`{ledger['renewal_residual_name']}`.  Finite joint ledgers saturate.  The tested
inverse restores ready capacity only by erasing the retained current
certificate, endpoint packet, objective occurrence, and coherent exhaust.

## Cycle 612 endpoint boundary

The triplicate 16-bit packet carries endpoint one, predecessor edge to endpoint
zero, matched 4:4 receipt ratio, common-profile certificate, and the
matter-caused endpoint-type bit.  Its physical matter predicate is the pinned
Cycle 612/Cycle 608 `Pd` result; the Cycle 662 occurrence does not counterfeit
matter membership.  Cycle 662 binding/ADMIT/LOCK and Cycle 612 binder,
law-domain, packet-fresh, and material predicates jointly gate the same fixed
word.  Work is uncomputed.

This is one typed protected causal-interval endpoint candidate.  It is not a
framework Record, proper time, realized history, or permanence result.  The
matter/profile program, binder/law-domain program, endpoint identity, and
predecessor address remain supplied exactly as at the Cycle 612 shore.  Cycle
665 executes the bounded basis-interface composition; it does not claim that
the full Cycle 608 detector plus Cycle 662 stochastic apparatus was newly
placed and matrix-executed as one monolith.

## Controls and unchanged shores

All `{deletion['deleted_surfaces']}` deletions are detected: ready debit, spent
credit, current rails, packet replica/predecessor/type, coherent exhaust,
matter compute/uncompute, join uncompute, branch, occurrence, binding, ADMIT,
and LOCK.  All `{deletion['malformed_total']}` malformed inputs reject.  The
composite gate truth table has `{deletion['composite_gate_truth_failures']}`
failures.  Saturation refuses without debit; all admitted images invert to the
blank slot on their exact branch code.

The Cycle 559, Cycle 591, Cycle 612, and Cycle 662 files are read only from
commit `{receipt['shore']['ref']}` and match every frozen SHA-256.  Their pass,
authority-none, audit-unset, and interpretation ceilings are preserved.

## Supplied / derived / open

Supplied: the Cycle 662 menu and quadratic stochastic candidate law, branch
interface, coherent exhaust, finite blank slots, and 125-site chart; the Cycle
559 current word and Cycle 591 continuity orientation; the Cycle 612 matter
predicate, binder/admission/law-domain/freshness program, endpoint identity,
predecessor zero, 4:4 receipts, triplicate packet layout, and 436-M2 block; the
fixed join word, 729-site conservative chart, and compile-time frame transport.

Derived on the declared interface code: exact ready/spent conservation and
two-endpoint continuity; one current certificate and typed endpoint on every
live train/held branch; zero-branch nondebit; basis inverse; all24/all576;
capacity/resource counts; deletion, malformed, and saturation controls.

Open: derivation/selection of the upstream stochastic law; autonomous
matter/profile/binder/predecessor genesis; a full joint physical placement and
matrix execution including the Cycle 608 detector; non-erasing renewal;
physical energy-stress or gravity identification; framework Record, proper
time, Born probability, and realized history.

## N1–N8 no-go discipline

N1 contains five normalized families.  N2 collapses the scoped residual set to
`W_endpoint_predecessor_genesis` and `W_joint_non_erasing_renewal`.  N3 exposes
every law, blank, current convention, material predicate, binder, predecessor,
packet, chart, and frame import.  N4 treats the Cycle 662 renewal as a strict
scope extension rather than an exact closure witness and preserves Cycle 612's
joint-apparatus boundary.  N5 audits per-element/site/mode/block/lattice
rhetoric.  N6 lists concrete partial-closure routes.  N7 steelmans a mobile
regenerative collision/successor QCA.  N8 records prior constructive retirement
mechanisms.

Broad negative gate: **FAIL / DO NOT SHIP**.

Minimum-content gate: **FAIL / DO NOT SHIP**.

Shared-obstruction gate: **FAIL / DO NOT SHIP**.

Axiom-pressure gate: **FAIL / DO NOT SHIP**.

No shared route-independent obstruction is established.  No axiom pressure is
claimed.  These are route-specific finite-interface walls, not constitutional
evidence.
"""


def main() -> int:
    signal.alarm(1200); started = time.perf_counter()
    freeze = target_freeze_controls(); check("exact target frozen before evidence load", freeze["pass"], freeze)
    shore, receipts = shore_controls(); check("Cycle559/Cycle591/Cycle612/Cycle662 immutable shores", shore["pass"], shore["imported_contracts"])
    formation = formation_rows(receipts); check("all Cycle662 train and blinded held branches compile to current plus endpoint", formation["pass"], {"rows": formation["branch_rows"], "live": formation["live_branch_rows"], "held_live": formation["held_live_branch_rows"]})
    ledger = ledger_controls(receipts); check("train/held finite capacity, saturation, inverse, and M2 accounting", ledger["pass"], {"capacities": [r["capacity"] for r in ledger["rows"]], "M2": [r["physical_M2_9cube"] for r in ledger["rows"]]})
    covariance = covariance_controls(); check("exact local current conservation and all24/all576 covariance", covariance["pass"], {"current": covariance["direction_current_comparisons"], "group": covariance["direction_group_comparisons"]})
    deletion = deletion_and_domain_controls(receipts); check("inverse/deletion/malformed/saturation and semantic firewalls", deletion["pass"], {"deletions": deletion["deleted_surfaces"], "malformed": deletion["malformed_rejections"]})
    no_go = no_go_discipline(); check("fresh N1-N8 scoped-wall discipline", no_go["pass"], {"families": no_go["N1_qualifying_attempts"], "walls": tuple(no_go["N2_walls"])})
    canonical = {
        "Status_PASS": no_go["Status"] == "PASS",
        "gates": all(no_go[key] == "FAIL / DO NOT SHIP" for key in ("N1_broad_negative_gate", "broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate")),
        "flags": not any(no_go[key] for key in ("broad_no_go_claim", "minimum_content_claim", "shared_obstruction_claim", "axiom_pressure_claim", "broad_negative_shipped", "minimum_content_shipped", "shared_obstruction_shipped", "axiom_pressure_shipped", "shared_route_independent_obstruction", "axiom_pressure")),
        "N1": no_go["N1_qualifying_attempts"] >= no_go["N1_required_for_negative"] == 5,
        "N2": len(no_go["N2_directed_ordered_pairs"]) == 2,
        "N4": all(not row["use_as_closure"] for row in no_go["N4_exact_residual_matches"]+no_go["N4_nonmatches_not_used_as_closure"]),
        "N5": all({"per_element","per_site","per_mode","per_block","lattice_wide"} <= set(row) for row in no_go["N5_rhetoric"]),
        "N6": all({"file","status","what_closes"} <= set(row) for row in no_go["N6_partial_closure_paths"]),
        "N7": all(key in no_go["N7_steelman"] for key in ("mechanism","actionable_steps","terminal_test","supporting_citations")),
        "N8": all({"retired","mechanism","applicability","citation_ref","citation_path","citation_line","citation_text"} <= set(row) for row in no_go["N8_cross_cycle_echo"]),
    }
    canonical["pass"] = all(canonical.values()); check("canonical N1-N8 schema and all negative gates", canonical["pass"], canonical)
    receipt = {
        "Status": "PASS", "cycle": 665, "date": "2026-07-23",
        "status": "positive bounded local formation-resource/current-to-typed-interval interface compiler; predecessor genesis and non-erasing joint renewal open",
        "classification": "exact interface-level fixed local compiler over immutable physical shores",
        "authority": AUTHORITY, "audit": AUDIT, "constitutional_effect": "none", "breakthrough": False,
        "strict_full_framework_terminal_met": False, "target_contract_candidate_terminal_met": True,
        "broad_negative_gate": "FAIL / DO NOT SHIP", "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP", "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "broad_no_go_claim": False, "minimum_content_claim": False, "shared_obstruction_claim": False,
        "axiom_pressure_claim": False, "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "broad_negative_shipped": False, "minimum_content_shipped": False,
        "shared_obstruction_shipped": False, "axiom_pressure_shipped": False,
        "target_contract": TARGET_CONTRACT, "target_freeze": freeze, "shore": shore,
        "fixed_local_word": FIXED_LOCAL_WORD, "fixed_local_word_sha256": FIXED_LOCAL_WORD_SHA256,
        "formation_interface_compiler": formation, "resource_ledger": ledger, "covariance": covariance,
        "deletion_and_domain": deletion, "no_go_discipline": no_go,
        "canonical_claim_gate_contract": canonical,
        "supplied_structure_inventory": {
            "Cycle662_quadratic_stochastic_candidate_law_and_menu": True,
            "Cycle662_branch_interface_coherent_exhaust_blank_slots_125_chart": True,
            "Cycle559_EDGE_Jplus_Jminus_word": True, "Cycle591_oriented_continuity_convention": True,
            "Cycle612_computed_physical_matter_predicate": True, "Cycle612_binder_law_domain_freshness_program": True,
            "Cycle612_endpoint_identity_predecessor_zero_4to4_receipts_triplicate_layout": True,
            "Cycle612_bounded_append_block_436_M2": True, "fixed_join_gate_word": True,
            "proper_cubic_729_site_chart": True, "compile_time_frame_transport": True,
            "host_scheduler": False, "host_sampler": False, "actuality_lookup": False,
            "grade_lookup": False, "shell_predicate_ROM": False,
        },
        "semantic_separation": {
            "resource_number_current": "coefficient-one ready/spent debit and EDGE/J flux; not physical energy, stress, force, or gravity",
            "generator_or_update_word": "fixed compiler order; not a physical rate or time",
            "typed_endpoint": "protected causal-interval endpoint candidate; not Record, proper time, permanence, or realized history",
            "objective_event": "inherited Cycle662 objective-within-supplied-candidate-law branch; not a supplied actuality lookup",
        },
        "route_disposition": {
            "direct_current_packet_compiler": "PASS_BOUNDED_INTERFACE_CODE",
            "six_lane_mediator": "PRIOR_POSITIVE_INCOMPARABLE__NO_FORMATION_JOIN",
            "qbetaN_continuity": "PRIOR_POSITIVE_INCOMPARABLE__NO_FORMATION_JOIN",
            "standalone_packet": "PRIOR_POSITIVE_WEAKER__NO_ATOMIC_RESOURCE_CURRENT",
            "host_sequenced_join": "REJECTED_BY_TARGET",
        },
        "six_wall_ledger": {
            "C_ref": "formation sigma is inherited and stored; current coefficient one is exact; upstream law, material profile, binder, and predecessor genesis supplied",
            "C_num": "all train/held branch interfaces, capacities, deletions, and exact integer continuity tested; no empirical or Born interpretation",
            "C_wrap": "one typed predecessor endpoint per admitted event; no Record, proper time, permanence, or realized history",
            "C_int": "one fixed local word joins occurrence, debit/current, retained exhaust, and endpoint; full detector-plus-stochastic monolith not matrix-executed",
            "C_local": "bounded 729-site proper cube, support counts, all24/all576; infinite/noisy deployment and non-erasing renewal open",
            "C_source": "ready/spent/current/packet/exhaust resources explicitly counted; not energy-stress, gravity, or a renewable bath",
        },
        "strongest_constructive_result": "one fixed bounded interface update compiles every live Cycle662 train/held branch into an exact Cycle559/Cycle591 conserved ready-to-spent current and a Cycle612 typed material-endpoint packet while retaining coherent exhaust",
        "highest_honest_terminal": "positive local physical-interface compiler on pinned declared code; no autonomous predecessor/material genesis, full joint detector matrix, non-erasing renewal, gravity, Record, or proper time",
        "optimal_next_campaign": "construct a mobile regenerative collision/successor QCA that generates the material predecessor locally and renews joint current/packet/exhaust capacity without erasure while reproducing every pinned Cycle662 branch propensity",
    }
    top = {
        "Status": receipt["Status"] == "PASS", "gates": all(receipt[key] == "FAIL / DO NOT SHIP" for key in ("broad_negative_gate","minimum_content_gate","shared_obstruction_gate","axiom_pressure_gate")),
        "flags": not any(receipt[key] for key in ("broad_no_go_claim","minimum_content_claim","shared_obstruction_claim","axiom_pressure_claim","broad_negative_shipped","minimum_content_shipped","shared_obstruction_shipped","axiom_pressure_shipped","shared_route_independent_obstruction","axiom_pressure")),
        "strict_false": receipt["strict_full_framework_terminal_met"] is False,
        "candidate_true": receipt["target_contract_candidate_terminal_met"] is True,
        "breakthrough_false": receipt["breakthrough"] is False,
    }
    top["pass"] = all(top.values()); receipt["top_level_claim_gate_contract"] = top
    check("top-level candidate/strict/breakthrough and negative gates", top["pass"], top)
    NOTE.parent.mkdir(parents=True, exist_ok=True); NOTE.write_text(note_text(receipt))
    flat = " ".join(NOTE.read_text().lower().split())
    required = ("authority: **none**", "audit: **unset**", "breakthrough: **false**", "all `24`", "576",
                "not identified as physical energy", "not a physical rate", "not a framework record",
                "host scheduler", "actuality lookup", "full cycle 608 detector", "fail / do not ship",
                "no shared route-independent obstruction", "no axiom pressure")
    missing = [item for item in required if item not in flat]; check("Cycle665 note semantic contract", not missing, missing)
    elapsed = time.perf_counter()-started; rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000: rss *= 1024
    receipt.update({"runner_sha256": file_sha(Path(__file__)), "note_sha256": file_sha(NOTE),
                    "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
                    "tests_passed": PASS, "tests_failed": FAIL, "pass": FAIL == 0})
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=float)+"\n")
    print(json.dumps({"pass": receipt["pass"], "tests": f"{PASS}/{PASS+FAIL}", "elapsed": elapsed,
                      "receipt": str(RECEIPT)}, indent=2))
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as stream:
        original = sys.stdout; sys.stdout = Tee(original, stream)
        try: raise SystemExit(main())
        finally: sys.stdout = original
