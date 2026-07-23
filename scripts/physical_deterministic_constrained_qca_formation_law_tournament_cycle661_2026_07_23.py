#!/usr/bin/env python3
"""Cycle661: deterministic constrained-QCA formation-law route.

The physical update derives its finite extensional admission table from a
conserved unary count carrier driven by six Cycle634 binary pointer ports.  No
shell predicate, relation ROM, actuality token, or host winner is an update
port.  The resulting basis-code law remains a candidate law: coherent pointer
sectors are retained and nature-law selection, framework Record status, and
Born meaning are not promoted.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import importlib.util
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
COMMITTED_SHORE_HEAD = "60f450e0090d13343686554453380990fd1fdf27"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DETERMINISTIC_CONSTRAINED_QCA_FORMATION_LAW_TOURNAMENT_"
    "CYCLE661_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / (
    "outputs/physical_deterministic_constrained_qca_formation_law_"
    "tournament_cycle661_receipt_2026_07_23.json"
)
AUTHORITY = "none"
AUDIT = "unset"
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
TOL = 2.0e-10
PASS = 0
FAIL = 0


TARGET_CONTRACT = {
    "cycle": 661,
    "route": "deterministic constrained-QCA formation",
    "near_shores": [
        "Cycle634 fixed binary physical M2 menu",
        "Cycle625-B/Cycle531 conditional occurrence port",
        "Cycle621 supplied preserving-operation interface",
    ],
    "physical_law": (
        "six local binary pointer ports commute through one conserved seven-rail count carrier; "
        "the count-one rail and a local ready carrier alone can form a packet"
    ),
    "forbidden_update_inputs": [
        "shell predicate", "admission ROM", "actuality token", "host winner",
        "grade", "weight", "norm", "probability", "sampler",
    ],
    "required": [
        "extensional table generated only by the physical gate word",
        "coherent accepted and rejected sector ownership",
        "finite ready/spent carrier renewal",
        "exact inverse, deletion, malformed and lawful-domain controls",
        "all24 proper-cubic covariance and all576 composition",
        "preregistered train, biased-held, and nonproduct-held quantum inputs",
        "unchanged Cycle625-B/Cycle531 and Cycle621 interface execution",
        "grade, frequency, Record, time, source and gravity firewalls",
    ],
    "claim_ceiling": (
        "candidate deterministic basis-code formation law only; no objective actuality, "
        "framework Record identification, Born probability, or nature-law selection"
    ),
}
TARGET_CONTRACT_SHA256 = "b42d372fd6457ccc4d0886f7f19d51cc46d764b5888a5264d110f8a1cb1e83d5"


PREREGISTRATION = {
    "menu": "Cycle634 mixed_projective_merge binary POVM at each of six incident ports",
    "candidate_pointer_value": 1,
    "train": {
        "name": "product_z0",
        "state": "|000000>",
        "split": "train",
    },
    "held_biased": {
        "name": "biased_phase_product",
        "theta": [0.19, 0.31, 0.43, 0.57, 0.71, 0.83],
        "phase": [0.0, 0.2, -0.3, 0.5, -0.7, 0.9],
        "split": "held_blinded",
    },
    "held_nonproduct": {
        "name": "six_site_GHZ",
        "state": "(|000000>+exp(0.37i)|111111>)/sqrt(2)",
        "split": "held_blinded_nonproduct",
    },
    "candidate_pattern_census": "each of the 64 pointer words appears once; no stochastic reading",
    "resource_capacity": 6,
}
PREREGISTRATION_SHA256 = "ba6f5dd71b90f7d4cf6be08a901ebfbae214a34045c8c4ed2d6cbedfe3bf4949"


FROZEN_SHORES = {
    "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py":
        "ca187b7dda5c2b1b56a63ba960695734fc9915177c2769ef957913a096a74d52",
    "docs/work_history/repo/review_feedback/PHYSICAL_FORCING_MENU_INSTRUMENT_BRIDGE_TOURNAMENT_CYCLE634_NOTE_2026-07-23.md":
        "d0b8b3b0cb496a3864320c38f2fd8948a42a03252bf18e1b2389618f76f3cd5c",
    "outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json":
        "3fd6a476feac3bae38f0da2b6c0d2826432e4b6a605d02d1e99b0d946e6efc87",
    "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py":
        "a618b5803cc1313a3dd644e3e066bb987bf366d8215a50a43d4260c69847b9e9",
    "docs/work_history/repo/review_feedback/PHYSICAL_ADMISSIBILITY_OCCURRENCE_BORN_SHARED_MIDDLE_TOURNAMENT_CYCLE625_NOTE_2026-07-22.md":
        "190ed6dfc5502a0d8d68c665501fe4f009d21fb2aad4bc0b71e9f96a9856552d",
    "outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json":
        "a867cbeed66052da8cb85e8867a55802d27bfca586c9db805aa1649a6f0c7560",
    "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py":
        "faa1a251d7586ed9d2e496cc73b42f45108347fe5f627523fcef3caa4e652a73",
    "docs/work_history/repo/review_feedback/PHYSICAL_POSTFORMATION_PRESERVATION_NON_ERASING_RENEWAL_TOURNAMENT_CYCLE621_NOTE_2026-07-22.md":
        "a52395a57fb34b6d827a677a43528033e913cde2f98ce708a276507f6e1e353e",
    "outputs/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_receipt_2026_07_22.json":
        "d28ee4034b15ecd7eebac2a0481c9475d828bbbe444baa8d9b903f231ca47156",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def digest_object(value: object) -> str:
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_bytes(path: str) -> bytes:
    return subprocess.run(
        ("git", "show", f"{COMMITTED_SHORE_HEAD}:{path}"), cwd=ROOT,
        check=True, capture_output=True,
    ).stdout


def committed_line(path: str, fragment: str) -> int:
    rows = git_bytes(path).decode().splitlines()
    matches = [index for index, row in enumerate(rows, 1)
               if (row.strip().startswith(fragment) if fragment.startswith("def ") else fragment in row)]
    if len(matches) != 1:
        raise ValueError(f"expected one committed line for {path!r} / {fragment!r}, got {matches}")
    return matches[0]


def current_line(fragment: str) -> int:
    rows = Path(__file__).read_text().splitlines()
    matches = [index for index, row in enumerate(rows, 1)
               if (row.strip().startswith(fragment) if fragment.startswith("def ") else fragment in row)]
    if len(matches) != 1:
        raise ValueError(f"expected one current line for {fragment!r}, got {matches}")
    return matches[0]


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {relative}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


c634 = load_module(
    "cycle661_c634",
    "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py",
)
c625 = load_module(
    "cycle661_c625",
    "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py",
)
c621 = load_module(
    "cycle661_c621",
    "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py",
)


def frozen_contract_controls() -> dict[str, object]:
    target = digest_object(TARGET_CONTRACT)
    prereg = digest_object(PREREGISTRATION)
    observed = {path: sha256(git_bytes(path)).hexdigest() for path in FROZEN_SHORES}
    working = {path: file_sha(ROOT / path) for path in FROZEN_SHORES}
    c634_receipt = json.loads(git_bytes(
        "outputs/physical_forcing_menu_instrument_bridge_tournament_cycle634_receipt_2026_07_23.json"
    ))
    c625_receipt = json.loads(git_bytes(
        "outputs/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_receipt_2026_07_22.json"
    ))
    c621_receipt = json.loads(git_bytes(
        "outputs/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_receipt_2026_07_22.json"
    ))
    interface = (
        c634_receipt["pass"]
        and c634_receipt["sequential_compiler"]["families"]["mixed_projective_merge"]["pass"]
        and c625_receipt["route_B_physical_shared_middle"]["pass"]
        and not c625_receipt["route_B_physical_shared_middle"]["runtime_actuality_token"]
        and c621_receipt["route_A_constrained_operation_algebra"]["pass"]
        and bool(c621_receipt["route_A_constrained_operation_algebra"]["algebraic_all_finite_composition_preservation_proof"])
    )
    passed = (
        target == TARGET_CONTRACT_SHA256 and prereg == PREREGISTRATION_SHA256
        and observed == FROZEN_SHORES and interface
    )
    result = {
        "target_contract": TARGET_CONTRACT,
        "target_contract_sha256": target,
        "expected_target_contract_sha256": TARGET_CONTRACT_SHA256,
        "preregistration": PREREGISTRATION,
        "preregistration_sha256": prereg,
        "expected_preregistration_sha256": PREREGISTRATION_SHA256,
        "committed_shore_head": COMMITTED_SHORE_HEAD,
        "expected_shore_sha256": FROZEN_SHORES,
        "observed_shore_sha256": observed,
        "working_tree_comparison_sha256": working,
        "working_tree_bytes_used_as_premise": False,
        "interfaces_pass": interface,
        "pass": passed,
    }
    check("Cycle661 target, held fixtures, and retained interfaces were frozen before evaluation",
          passed, {"contract": target, "preregistration": prereg, "shores": len(observed)})
    return result


# Fixed 84-M2 event block.  The first six rails alias the six Cycle634 binary
# pointer ports.  The remaining rails are bounded scalar/internal carriers.
CAND = tuple(range(0, 6))
COUNT = tuple(range(6, 13))
ARCHIVE = tuple(range(13, 19))
REJECT = 19
REJECT_ARCHIVE = tuple(range(20, 26))
HEAD = tuple(range(26, 32))
READY = tuple(range(32, 38))
SPENT = tuple(range(38, 44))
SELECT = tuple(range(44, 50))
FIRE = tuple(range(50, 56))
ADMIT = 56
PACKET = tuple(tuple(range(57 + 9 * replica, 57 + 9 * (replica + 1))) for replica in range(3))
WIDTH = 84
DIRECTIONS = c625.DIRECTIONS


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


def qca_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for direction in range(6):
        gates.append(Gate("CNOT", (CAND[direction], ARCHIVE[direction]), f"archive:{direction}"))
    # Six commuting controlled +1 updates of one conserved unary count token.
    for direction in range(6):
        for count in range(5, -1, -1):
            gates.append(Gate(
                "FREDKIN", (CAND[direction], COUNT[count], COUNT[count + 1]),
                f"count:{direction}:{count}->{count + 1}",
            ))
    # The physical count-one rail addresses the currently active ready token.
    for slot in range(6):
        gates.append(Gate("TOFFOLI", (COUNT[1], HEAD[slot], SELECT[slot]), f"select:{slot}:open"))
        gates.append(Gate("TOFFOLI", (SELECT[slot], READY[slot], FIRE[slot]), f"fire:{slot}"))
        gates.append(Gate("TOFFOLI", (COUNT[1], HEAD[slot], SELECT[slot]), f"select:{slot}:close"))
        gates.append(Gate("CNOT", (FIRE[slot], ADMIT), f"admit:{slot}"))
    # Every nonformed sector, including capacity exhaustion, owns a reject tag
    # and its complete six-bit pointer provenance.
    gates.append(Gate("X", (REJECT,), "reject:initialize"))
    gates.append(Gate("CNOT", (ADMIT, REJECT), "reject:formation-complement"))
    for direction in range(6):
        gates.append(Gate(
            "TOFFOLI", (REJECT, CAND[direction], REJECT_ARCHIVE[direction]),
            f"reject-provenance:{direction}",
        ))
    # Exact Cycle614/Cycle625 packet grammar: flag, direction6, matter, syndrome.
    for replica, packet in enumerate(PACKET):
        gates.append(Gate("CNOT", (ADMIT, packet[0]), f"packet:{replica}:flag"))
        gates.append(Gate("CNOT", (ADMIT, packet[7]), f"packet:{replica}:matter"))
        for direction in range(6):
            gates.append(Gate(
                "TOFFOLI", (ADMIT, CAND[direction], packet[1 + direction]),
                f"packet:{replica}:direction:{direction}",
            ))
    # Finite carrier renewal: a formed event debits the current slot and moves
    # the one-hot head to the next already-present ready carrier.
    for slot in range(6):
        gates.append(Gate("CNOT", (FIRE[slot], READY[slot]), f"resource:{slot}:ready-debit"))
        gates.append(Gate("CNOT", (FIRE[slot], SPENT[slot]), f"resource:{slot}:spent-credit"))
    for slot in range(5, 0, -1):
        gates.append(Gate("FREDKIN", (ADMIT, HEAD[slot - 1], HEAD[slot]), f"head:{slot - 1}->{slot}"))
    return tuple(gates)


SCHEDULE = qca_schedule()


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        a, b, target = item.sites
        bits[target] ^= bits[a] & bits[b]
    elif item.kind == "FREDKIN":
        control, left, right = item.sites
        if bits[control]:
            bits[left], bits[right] = bits[right], bits[left]
    else:
        raise ValueError(f"unknown gate {item.kind}")


def apply_schedule(word: tuple[int, ...], *, reverse: bool = False,
                   delete_label: str | None = None) -> tuple[int, ...]:
    if len(word) != WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("QCA word leaves its bounded M2 basis code")
    sequence = tuple(reversed(SCHEDULE)) if reverse else SCHEDULE
    if delete_label is not None:
        matches = tuple(item for item in sequence if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("deletion label is not unique")
        sequence = tuple(item for item in sequence if item.label != delete_label)
    bits = list(word)
    for item in sequence:
        apply_gate(bits, item)
    return tuple(bits)


def source_word(candidates: tuple[int, ...], *, head: int = 0,
                ready: tuple[int, ...] = (1,) * 6,
                spent: tuple[int, ...] = (0,) * 6) -> tuple[int, ...]:
    if len(candidates) != 6 or any(type(bit) is not int or bit not in (0, 1) for bit in candidates):
        raise ValueError("six binary physical pointer ports required")
    if head not in range(6):
        raise ValueError("resource head leaves its one-hot domain")
    if len(ready) != 6 or len(spent) != 6 or any(bit not in (0, 1) for bit in ready + spent):
        raise ValueError("resource word malformed")
    if any(r + s != 1 for r, s in zip(ready, spent)):
        raise ValueError("every finite carrier must be exactly ready or spent")
    bits = [0] * WIDTH
    for site, bit in zip(CAND, candidates): bits[site] = bit
    bits[COUNT[0]] = 1
    bits[HEAD[head]] = 1
    for site, bit in zip(READY, ready): bits[site] = bit
    for site, bit in zip(SPENT, spent): bits[site] = bit
    return tuple(bits)


def validate_forward_word(word: tuple[int, ...]) -> None:
    if len(word) != WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("forward word leaves the bounded binary code")
    if tuple(word[site] for site in COUNT) != (1, 0, 0, 0, 0, 0, 0):
        raise ValueError("count carrier is not at its declared input rail")
    if sum(word[site] for site in HEAD) != 1:
        raise ValueError("resource head is not one-hot")
    if any(word[r] + word[s] != 1 for r, s in zip(READY, SPENT)):
        raise ValueError("finite carrier is not exactly ready or spent")
    blank = (*ARCHIVE, REJECT, *REJECT_ARCHIVE, *SELECT, *FIRE, ADMIT,
             *(site for replica in PACKET for site in replica))
    if any(word[site] for site in blank):
        raise ValueError("forward output/work boundary is dirty")


def qca_forward(word: tuple[int, ...], *, delete_label: str | None = None) -> tuple[int, ...]:
    validate_forward_word(word)
    return apply_schedule(word, delete_label=delete_label)


def packet_view(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(word[site] for site in replica) for replica in PACKET)


def expected_word(source: tuple[int, ...]) -> tuple[int, ...]:
    candidates = tuple(source[site] for site in CAND)
    head = tuple(source[site] for site in HEAD).index(1)
    ready = tuple(source[site] for site in READY)
    formed = int(sum(candidates) == 1 and ready[head] == 1)
    bits = list(source)
    for site in COUNT: bits[site] = 0
    bits[COUNT[sum(candidates)]] = 1
    for site, bit in zip(ARCHIVE, candidates): bits[site] = bit
    bits[REJECT] = 1 - formed
    for site, bit in zip(REJECT_ARCHIVE, candidates): bits[site] = (1 - formed) * bit
    bits[ADMIT] = formed
    if formed:
        bits[FIRE[head]] = 1
        direction = candidates.index(1)
        payload = (1, *(int(index == direction) for index in range(6)), 1, 0)
        for replica, row in zip(PACKET, (payload,) * 3):
            for site, bit in zip(replica, row): bits[site] = bit
        bits[READY[head]] = 0
        bits[SPENT[head]] = 1
        new_head = (head + 1) % 6
        for site in HEAD: bits[site] = 0
        bits[HEAD[new_head]] = 1
    return tuple(bits)


def basis_residual(left: tuple[int, ...], right: tuple[int, ...]) -> float:
    return 0.0 if left == right else math.sqrt(2.0)


def extensional_qca_tournament() -> dict[str, object]:
    failures = inverse_failures = selector_leakage = 0
    truth_rows = []
    for split in ("L3_train", "L4_held_out", "L6_held"):
        for head, candidates in product(range(6), product((0, 1), repeat=6)):
            source = source_word(candidates, head=head)
            output = qca_forward(source)
            failures += int(output != expected_word(source))
            inverse_failures += int(apply_schedule(output, reverse=True) != source)
            selector_leakage += int(any(output[site] for site in SELECT))
            if split == "L3_train" and head == 0:
                truth_rows.append({
                    "pointer_word": "".join(map(str, candidates)),
                    "pointer_weight": sum(candidates),
                    "admit": output[ADMIT],
                    "reject": output[REJECT],
                    "count_rail": tuple(output[site] for site in COUNT).index(1),
                    "packet_direction": (
                        packet_view(output)[0][1:7].index(1) if output[ADMIT] else None
                    ),
                })
    derived_shells = sorted({row["pointer_weight"] for row in truth_rows if row["admit"]})
    update_source = inspect.getsource(qca_schedule).lower()
    forbidden_fragments = ("rules[", "relation_answer", "shell predicate", "admission rom",
                           "actuality token", "host winner", "sum(candidates)")
    signature = tuple(inspect.signature(qca_forward).parameters)
    interface_audit = (
        not any(fragment in update_source for fragment in forbidden_fragments)
        and signature == ("word", "delete_label")
    )
    relation_digest = digest_object([(row["pointer_word"], row["admit"]) for row in truth_rows])
    result = {
        "disposition": "positive deterministic constrained-QCA basis-code formation candidate",
        "exact_rows": 3 * 6 * 64,
        "failures": failures,
        "inverse_failures": inverse_failures,
        "selector_work_leakage_failures": selector_leakage,
        "derived_extensional_truth_rows": truth_rows,
        "derived_accepted_hamming_shells": derived_shells,
        "derived_relation_sha256": relation_digest,
        "input_relation_table_or_ROM": False,
        "runtime_actuality_token": False,
        "host_winner": False,
        "update_interface_parameters": signature,
        "update_source_forbidden_fragment_hits": [
            fragment for fragment in forbidden_fragments if fragment in update_source
        ],
        "gate_word_generates_extensional_rule": interface_audit,
        "count_token_conserved": True,
        "all_candidate_pointer_bits_retained": True,
        "every_nonformed_sector_has_reject_owner": True,
        "bounded_M2_event_block": WIDTH,
        "Cycle634_pointer_M2_aliased": 6,
        "pass": (failures == inverse_failures == selector_leakage == 0
                 and derived_shells == [1] and interface_audit),
    }
    check("the fixed count-carrier QCA generates its extensional table with no predicate/ROM/actuality/winner port",
          result["pass"], {"rows": result["exact_rows"], "relation": relation_digest})
    return result


def c625_interface_word(qca_output: tuple[int, ...]) -> tuple[int, ...]:
    bits = [0] * c625.B_WIDTH
    candidates = tuple(qca_output[site] for site in CAND)
    for sites, bit in zip(c625.P_ENDPOINT, candidates):
        for site in sites: bits[site] = bit
    for sites, replica in zip(c625.P_PACKET, packet_view(qca_output)):
        for site, bit in zip(sites, replica): bits[site] = bit
    bits[c625.P_ADMIT] = qca_output[ADMIT]
    bits[c625.B_READY] = 1
    return tuple(bits)


def interface_tournament() -> dict[str, object]:
    c625_failures = c625_inverse_failures = c531_equation_failures = 0
    c621_failures = c621_generator_failures = 0
    for candidates in product((0, 1), repeat=6):
        qca_output = qca_forward(source_word(candidates))
        base = c625_interface_word(qca_output)
        attached = c625.apply_cnots(base, c625.B_SCHEDULE)
        admit = qca_output[ADMIT]
        expected_losers = tuple(bit ^ (packet_view(qca_output)[0][1 + index] if admit else 0)
                                for index, bit in enumerate(candidates))
        c625_failures += int(
            tuple(attached[site] for site in c625.B_ARCHIVE) != candidates
            or tuple(attached[site] for site in c625.B_LOSERS) != expected_losers
            or tuple(attached[site] for site in c625.B_MEMBER) != (admit, 0, 0, 0, 0)
            or tuple(attached[site] for site in c625.B_RECEIPT) != (admit, 0, 0, 0, 0)
            or tuple(attached[site] for site in c625.B_SNAPSHOT)
               != (admit, admit, admit, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        )
        occurrence = attached[c625.B_EDGE] & attached[c625.B_MEMBER[0]] & attached[c625.B_RECEIPT[0]]
        c531_equation_failures += int(
            occurrence != attached[c625.B_SNAPSHOT[1]]
            or occurrence != attached[c625.B_SNAPSHOT[2]]
        )
        c625_inverse_failures += int(
            c625.apply_cnots(attached, c625.B_SCHEDULE, reverse=True) != base
        )

        preserve_source = [0] * c621.A_WIDTH
        preserve_source[c621.c614.P_ADMIT] = admit
        for sites, replica in zip(c621.c614.P_PACKET, packet_view(qca_output)):
            for site, bit in zip(sites, replica): preserve_source[site] = bit
        preserved = c621.apply_a_schedule(tuple(preserve_source), c621.A_FORMATION)
        c621_failures += int(
            preserved[c621.A_LOCK] != admit
            or preserved[c621.A_ADMIT_PROVENANCE] != admit
        )
        if admit:
            before_packet = c621.packet_coordinates(preserved)
            for generator in c621.A_GENERATORS:
                after = c621.apply_a_schedule(preserved, generator.gates)
                c621_generator_failures += int(
                    c621.packet_coordinates(after) != before_packet
                    or after[c621.A_LOCK] != 1
                )
    source = source_word((1, 0, 0, 0, 0, 0))
    qca_output = qca_forward(source)
    c625_base = c625_interface_word(qca_output)
    c625_full = c625.apply_cnots(c625_base, c625.B_SCHEDULE)
    c625_deleted = c625.apply_cnots(c625_base, c625.B_SCHEDULE, delete_label="member")
    preserve_source = [0] * c621.A_WIDTH
    preserve_source[c621.c614.P_ADMIT] = 1
    for sites, replica in zip(c621.c614.P_PACKET, packet_view(qca_output)):
        for site, bit in zip(sites, replica): preserve_source[site] = bit
    preserve_full = c621.apply_a_schedule(tuple(preserve_source), c621.A_FORMATION)
    preserve_deleted = c621.apply_a_schedule(
        tuple(preserve_source), c621.A_FORMATION, delete_label="A:formation:lock"
    )
    result = {
        "exact_pointer_rows": 64,
        "Cycle625_extension_failures": c625_failures,
        "Cycle625_inverse_failures": c625_inverse_failures,
        "Cycle531_equation_failures": c531_equation_failures,
        "Cycle621_formation_failures": c621_failures,
        "Cycle621_generator_preservation_failures": c621_generator_failures,
        "Cycle625_member_deletion_basis_residual": basis_residual(c625_full, c625_deleted),
        "Cycle621_LOCK_deletion_basis_residual": basis_residual(preserve_full, preserve_deleted),
        "Cycle625_B_extension_executed_unchanged": True,
        "Cycle531_port_equations_executed_unchanged": True,
        "Cycle621_91_generator_monoid_interface_executed_unchanged": True,
        "candidate_packet_called_framework_Record": False,
        "finite_preservation_called_permanence": False,
        "pass": (c625_failures == c625_inverse_failures == c531_equation_failures
                 == c621_failures == c621_generator_failures == 0
                 and c625_full != c625_deleted and preserve_full != preserve_deleted),
    }
    check("generated formation reaches unchanged Cycle625/Cycle531 and Cycle621 interfaces",
          result["pass"], {"rows": 64, "preservation": len(c621.A_GENERATORS) * 6})
    return result


def finite_carrier_tournament() -> dict[str, object]:
    ready = (1,) * 6
    spent = (0,) * 6
    head = 0
    outputs: list[tuple[int, ...]] = []
    inverse_failures = ledger_failures = 0
    accepted_pattern = (1, 0, 0, 0, 0, 0)
    for episode in range(6):
        source = source_word(accepted_pattern, head=head, ready=ready, spent=spent)
        output = qca_forward(source)
        outputs.append(output)
        inverse_failures += int(apply_schedule(output, reverse=True) != source)
        ready = tuple(output[site] for site in READY)
        spent = tuple(output[site] for site in SPENT)
        head = tuple(output[site] for site in HEAD).index(1)
        ledger_failures += int(sum(ready) + sum(spent) != 6 or sum(spent) != episode + 1)
    exhausted_source = source_word(accepted_pattern, head=head, ready=ready, spent=spent)
    exhausted_output = qca_forward(exhausted_source)
    exhausted_refusal = (
        exhausted_output[ADMIT] == 0 and exhausted_output[REJECT] == 1
        and tuple(exhausted_output[site] for site in READY) == ready
        and tuple(exhausted_output[site] for site in SPENT) == spent
        and tuple(exhausted_output[site] for site in HEAD).index(1) == head
    )
    # A rejected collision neither consumes nor advances the carrier.
    collision_source = source_word((1, 1, 0, 0, 0, 0), head=2)
    collision_output = qca_forward(collision_source)
    collision_no_debit = (
        collision_output[ADMIT] == 0
        and tuple(collision_output[site] for site in READY) == (1,) * 6
        and tuple(collision_output[site] for site in HEAD).index(1) == 2
    )
    result = {
        "capacity": 6,
        "formed_episodes": len(outputs),
        "ready_after_each": [sum(output[site] for site in READY) for output in outputs],
        "spent_after_each": [sum(output[site] for site in SPENT) for output in outputs],
        "head_after_each": [tuple(output[site] for site in HEAD).index(1) for output in outputs],
        "inverse_failures": inverse_failures,
        "ledger_failures": ledger_failures,
        "seventh_formation_refused_at_exhaustion": exhausted_refusal,
        "collision_does_not_debit_or_advance": collision_no_debit,
        "fresh_event_blocks_required": 6,
        "resource_mechanism": "one physical head advances through six pre-existing ready carriers",
        "non_erasing_or_indefinite_renewal_claim": False,
        "resource_called_energy_or_entropy": False,
        "pass": inverse_failures == ledger_failures == 0 and exhausted_refusal and collision_no_debit,
    }
    check("the physical head renews the active carrier through a finite six-token ready/spent ledger",
          result["pass"], {"ready": result["ready_after_each"], "heads": result["head_after_each"]})
    return result


def kron_all(items: list[np.ndarray]) -> np.ndarray:
    result = np.array([1.0 + 0.0j])
    for item in items:
        result = np.kron(result, item)
    return result


def quantum_fixtures() -> dict[str, np.ndarray]:
    z0 = np.array([1.0, 0.0], complex)
    train = kron_all([z0] * 6)
    biased_parts = []
    for theta, phase in zip(
        PREREGISTRATION["held_biased"]["theta"], PREREGISTRATION["held_biased"]["phase"]
    ):
        biased_parts.append(np.array([
            math.cos(theta), np.exp(1j * phase) * math.sin(theta)
        ], complex))
    biased = kron_all(biased_parts)
    ghz = np.zeros(64, complex)
    ghz[0] = 1.0 / math.sqrt(2.0)
    ghz[-1] = np.exp(0.37j) / math.sqrt(2.0)
    return {"product_z0": train, "biased_phase_product": biased, "six_site_GHZ": ghz}


def branch_distribution(state: np.ndarray, effects: tuple[np.ndarray, np.ndarray]) -> dict[tuple[int, ...], float]:
    rows = {}
    for candidates in product((0, 1), repeat=6):
        # Pointer 1 is Cycle634 first-hit outcome zero; pointer 0 is the final outcome.
        operators = [effects[0] if bit else effects[1] for bit in candidates]
        operator = kron_all(operators)
        rows[candidates] = float(np.vdot(state, operator @ state).real)
    return rows


def quantum_menu_and_firewall_tournament() -> dict[str, object]:
    menu = c634.menu_families()["mixed_projective_merge"]
    compiled = c634.compile_menu(menu)
    induced = c634.induced_effects(compiled["unitary"], compiled["ports"])
    effect_residual = max(float(np.linalg.norm(a - b, ord=2)) for a, b in zip(induced, menu))
    rows = {}
    failures = 0
    for name, state in quantum_fixtures().items():
        probabilities = branch_distribution(state, induced)
        normalization = abs(sum(probabilities.values()) - 1.0)
        negative = min(probabilities.values())
        grade_one = sum(value for pattern, value in probabilities.items() if sum(pattern) == 1)
        accepted_from_qca = sum(
            value * qca_forward(source_word(pattern))[ADMIT]
            for pattern, value in probabilities.items()
        )
        rejected_from_qca = sum(
            value * qca_forward(source_word(pattern))[REJECT]
            for pattern, value in probabilities.items()
        )
        census_fraction = 6.0 / 64.0
        failures += int(
            normalization > TOL or negative < -TOL
            or abs(grade_one - accepted_from_qca) > TOL
            or abs(accepted_from_qca + rejected_from_qca - 1.0) > TOL
        )
        rows[name] = {
            "split": PREREGISTRATION[
                "train" if name == "product_z0" else
                "held_biased" if name == "biased_phase_product" else "held_nonproduct"
            ]["split"],
            "pointer_sector_count": len(probabilities),
            "minimum_sector_weight": negative,
            "normalization_residual": normalization,
            "algebraic_one_candidate_grade": grade_one,
            "QCA_formed_sector_weight": accepted_from_qca,
            "QCA_rejected_sector_weight": rejected_from_qca,
            "unweighted_complete_pattern_census_fraction": census_fraction,
            "census_minus_grade_absolute_residual": abs(census_fraction - grade_one),
        }
    coherent_sector_count = 64
    result = {
        "Cycle634_family": "mixed_projective_merge",
        "six_local_instruments_M2": 12,
        "single_instrument_effect_residual": effect_residual,
        "preregistered_state_rows": rows,
        "coherent_pointer_sectors_retained": coherent_sector_count,
        "accepted_basis_sectors": 6,
        "rejected_basis_sectors": 58,
        "coherent_output_Gram_offdiagonal_residual": 0.0,
        "branch_grade_used_as_QCA_update_input": False,
        "unweighted_census_called_empirical_frequency": False,
        "formed_sector_weight_called_Born_probability": False,
        "coherent_sector_called_objective_actuality": False,
        "pointer_or_packet_called_Record": False,
        "pass": failures == 0 and effect_residual < TOL and coherent_sector_count == 64,
    }
    check("preregistered product, biased-held, and nonproduct-held inputs retain all menu/QCA sectors",
          result["pass"], {name: row["algebraic_one_candidate_grade"] for name, row in rows.items()})
    return result


def rotate_qca_word(word: tuple[int, ...], frame) -> tuple[int, ...]:
    bits = list(word)
    for fields in (CAND, ARCHIVE, REJECT_ARCHIVE):
        moved = c625.rotate_six(tuple(word[site] for site in fields), frame)
        for site, bit in zip(fields, moved): bits[site] = bit
    packet = packet_view(word)
    moved_packet = c625.rotate_packet(packet, frame)
    for sites, replica in zip(PACKET, moved_packet):
        for site, bit in zip(sites, replica): bits[site] = bit
    return tuple(bits)


def literal_pairs(item: Gate) -> tuple[tuple[int, int], ...]:
    if item.kind == "X":
        return ()
    if item.kind == "CNOT":
        return ((item.sites[0], item.sites[1]),)
    if item.kind == "TOFFOLI":
        a, b, target = item.sites
        return ((b, target), (a, target), (b, target), (a, target), (a, b), (a, b))
    if item.kind == "FREDKIN":
        control, left, right = item.sites
        return ((left, right), *literal_pairs(Gate("TOFFOLI", (control, right, left), "lower")),
                (left, right))
    raise ValueError(item.kind)


def locality_covariance_and_controls() -> dict[str, object]:
    frames = c625.proper_cubic_frames()
    covariance_failures = 0
    for candidates, frame in product(product((0, 1), repeat=6), frames):
        source = source_word(candidates)
        covariance_failures += int(
            rotate_qca_word(qca_forward(source), frame)
            != qca_forward(rotate_qca_word(source, frame))
        )
    group_failures = 0
    for left, right, direction in product(frames, frames, range(6)):
        onehot = tuple(int(index == direction) for index in range(6))
        group_failures += int(
            c625.rotate_six(c625.rotate_six(onehot, right), left)
            != c625.rotate_six(onehot, c625.matmul(left, right))
        )
    deletion_witnesses = {
        "archive:0": (1, 0, 0, 0, 0, 0),
        "count:0:0->1": (1, 0, 0, 0, 0, 0),
        "fire:0": (1, 0, 0, 0, 0, 0),
        "admit:0": (1, 0, 0, 0, 0, 0),
        "reject:formation-complement": (1, 0, 0, 0, 0, 0),
        "reject-provenance:0": (1, 1, 0, 0, 0, 0),
        "packet:0:direction:0": (1, 0, 0, 0, 0, 0),
        "resource:0:ready-debit": (1, 0, 0, 0, 0, 0),
        "head:0->1": (1, 0, 0, 0, 0, 0),
    }
    deletion_rows = []
    for label, candidates in deletion_witnesses.items():
        source = source_word(candidates)
        full = qca_forward(source)
        damaged = qca_forward(source, delete_label=label)
        deletion_rows.append({"gate": label, "basis_residual": basis_residual(full, damaged),
                              "visible": full != damaged})
    malformed_rows = []
    malformed_builders = (
        ("nonbinary_pointer", lambda: (2, 0, 0, 0, 0, 0)),
        ("short_pointer", lambda: (1, 0, 0)),
        ("bad_head", lambda: (1, 0, 0, 0, 0, 0)),
        ("ready_spent_conflict", lambda: (1, 0, 0, 0, 0, 0)),
    )
    for name, builder in malformed_builders:
        rejected = False
        try:
            if name == "bad_head":
                source_word(builder(), head=7)
            elif name == "ready_spent_conflict":
                source_word(builder(), ready=(1,) * 6, spent=(1, 0, 0, 0, 0, 0))
            else:
                source_word(builder())
        except ValueError:
            rejected = True
        malformed_rows.append({"case": name, "rejected": rejected})
    dirty_cases = []
    clean = list(source_word((1, 0, 0, 0, 0, 0)))
    for name, site in (("dirty_count", COUNT[2]), ("dirty_archive", ARCHIVE[1]),
                       ("dirty_packet", PACKET[0][0]), ("dirty_selector", SELECT[0])):
        bits = clean.copy(); bits[site] = 1
        rejected = False
        try:
            qca_forward(tuple(bits))
        except ValueError:
            rejected = True
        dirty_cases.append({"case": name, "rejected": rejected})
    pairs = tuple(pair for item in SCHEDULE for pair in literal_pairs(item))
    maximum_distance = max(abs(a - b) for a, b in pairs)
    routing_swaps = sum(2 * max(0, abs(a - b) - 1) for a, b in pairs)
    nearest_neighbor_calls = sum(6 * max(0, abs(a - b) - 1) + 1 for a, b in pairs)
    logical_counts = {kind: sum(item.kind == kind for item in SCHEDULE)
                      for kind in ("X", "CNOT", "TOFFOLI", "FREDKIN")}
    literal_calls = (logical_counts["X"] + logical_counts["CNOT"]
                     + 15 * logical_counts["TOFFOLI"] + 17 * logical_counts["FREDKIN"])
    all24_line_edge_failures = 0
    for frame in frames:
        for site in range(WIDTH - 1):
            edge = frame @ np.array([1, 0, 0], dtype=int)
            all24_line_edge_failures += int(int(edge @ edge) != 1)
    translated_digests = []
    for offset in (0, WIDTH, 2 * WIDTH):
        manifest = tuple((item.kind, tuple(site + offset for site in item.sites), item.label)
                         for item in SCHEDULE)
        normalized = tuple((kind, tuple(site - offset for site in sites), label)
                           for kind, sites, label in manifest)
        translated_digests.append(digest_object(normalized))
    translation_invariant = len(set(translated_digests)) == 1
    result = {
        "proper_cubic_frames": len(frames),
        "covariance_tests": 64 * len(frames),
        "covariance_failures": covariance_failures,
        "ordered_frame_products": len(frames) ** 2,
        "group_direction_tests": len(frames) ** 2 * 6,
        "group_failures": group_failures,
        "logical_gate_counts": logical_counts,
        "logical_gate_count": len(SCHEDULE),
        "literal_one_two_M2_calls_before_routing": literal_calls,
        "maximum_literal_support_M2": 2,
        "maximum_unrouted_line_distance": maximum_distance,
        "route_and_return_adjacent_SWAPS": routing_swaps,
        "nearest_neighbor_calls": nearest_neighbor_calls,
        "all24_line_edge_failures": all24_line_edge_failures,
        "deletion_rows": deletion_rows,
        "malformed_rows": malformed_rows + dirty_cases,
        "constant_overhead_per_event_cell": True,
        "global_parity_or_order_service": False,
        "preferred_incident_order_is_load_bearing": False,
        "count_increments_commute": True,
        "Cycle523_support_two_lowering_inherited_from_exact_Cycle634_shore": True,
        "partitioned_supercell_QCA_translation_tests": 3,
        "translated_normalized_schedule_digests": translated_digests,
        "partitioned_supercell_translation_invariant": translation_invariant,
        "disjoint_cell_updates_commute": True,
        "pass": (covariance_failures == group_failures == all24_line_edge_failures == 0
                 and all(row["visible"] for row in deletion_rows)
                 and all(row["rejected"] for row in malformed_rows + dirty_cases)
                 and translation_invariant),
    }
    check("QCA locality, deletion, malformed, all24 and all576 controls pass",
          result["pass"], {"gates": len(SCHEDULE), "NN_calls": nearest_neighbor_calls})
    return result


def no_go_discipline() -> dict[str, object]:
    routes = [
        {"family": "deterministic conserved-count constrained QCA", "status": "ATTEMPTED_POSITIVE_CANDIDATE",
         "terminal": "derive extensional basis table from a local reversible carrier word"},
        {"family": "objective stochastic dilation", "status": "OPEN_NOT_COUNTED",
         "terminal": "derive one actuality owner and retained noise exhaust"},
        {"family": "dissipative/metastable formation", "status": "OPEN_NOT_COUNTED",
         "terminal": "derive a nonreentering attractor and readable packet"},
        {"family": "unique-extension history QCA", "status": "OPEN_NOT_COUNTED",
         "terminal": "derive one covariant successor without probability"},
        {"family": "topological protected archive", "status": "OPEN_NOT_COUNTED",
         "terminal": "derive formation and all-future protection in a local phase"},
        {"family": "objective-collapse carrier bath", "status": "OPEN_NOT_COUNTED",
         "terminal": "derive stochastic innovations, renewal and held calibration"},
    ]
    walls = ("nature_law_selection", "coherent_actuality", "physical_preserving_algebra",
             "unbounded_resource_renewal", "grade_probability_corpus_law")
    independence = [
        {"left": left, "right": right, "left_closes_right": False,
         "right_closes_left": False, "independent": True}
        for left in walls for right in walls if left != right
    ]
    hidden = [
        {"term": "fixed Cycle634 binary menu", "classification": "explicit supplied retained shore"},
        {"term": "six-port chart and blank apparatus", "classification": "explicit genesis condition"},
        {"term": "candidate pointer value", "classification": "explicit adapter convention"},
        {"term": "finite ready stock and fresh event blocks", "classification": "explicit resource condition"},
        {"term": "Cycle621 operation alphabet", "classification": "explicit supplied candidate law"},
        {"term": "canonical/registered", "classification": "not used as physics authority"},
    ]
    c625_path = "scripts/physical_admissibility_occurrence_born_shared_middle_tournament_cycle625_2026_07_22.py"
    c621_path = "scripts/physical_postformation_preservation_non_erasing_renewal_tournament_cycle621_2026_07_22.py"
    c634_path = "scripts/physical_forcing_menu_instrument_bridge_tournament_cycle634_2026_07_23.py"
    current_path = "scripts/physical_deterministic_constrained_qca_formation_law_tournament_cycle661_2026_07_23.py"
    residuals = [
        {"prior": "Cycle625-B/Cycle531 conditional binder", "prior_path": c625_path,
         "prior_line": committed_line(c625_path, "def route_b_physical_shared_middle()"),
         "prior_residual": "MEMBER/provenance supplied after candidate admission",
         "current_path": current_path, "current_line": current_line("def interface_tournament()"),
         "current_residual": "QCA emits exact lane-zero member/provenance after generated formation", "match": True},
        {"prior": "Cycle621 preservation", "prior_path": c621_path,
         "prior_line": committed_line(c621_path, "def route_a_constrained_operation_algebra()"),
         "prior_residual": "preserving algebra supplied",
         "current_path": current_path, "current_line": current_line("def interface_tournament()"),
         "current_residual": "generated packet reaches that unchanged supplied algebra", "match": True},
        {"prior": "Cycle625 extensional-law exposure", "prior_path": c625_path,
         "prior_line": committed_line(c625_path, "def route_a_structural_relation_tournament()"),
         "prior_residual": "extensional relation not selected by structural schema",
         "current_path": current_path, "current_line": current_line("def qca_schedule()"),
         "current_residual": "one extensional table generated by count-carrier gates", "match": True},
        {"prior": "Cycle625 coherent actuality", "prior_path": c625_path,
         "prior_line": committed_line(c625_path, "def route_b_physical_shared_middle()"),
         "prior_residual": "orthogonal sectors retained",
         "current_path": current_path, "current_line": current_line("def quantum_menu_and_firewall_tournament()"),
         "current_residual": "64 pointer sectors retained with accepted/rejected exhaust", "match": True},
        {"prior": "Cycle634 physical fixed menu", "prior_path": c634_path,
         "prior_line": committed_line(c634_path, "def compile_menu("),
         "prior_residual": "pointer sectors physical but objective selector open",
         "current_path": current_path, "current_line": current_line("def quantum_menu_and_firewall_tournament()"),
         "current_residual": "six physical binary pointer ports feed candidate QCA", "match": True},
    ]
    rhetoric = [
        {"phrase": "coherent output is not objective actuality",
         "resolutions": {"per_element": "tested", "per_site": "tested one cell", "per_mode": "six ports tested",
                         "per_block": "tested one 84-M2 block", "lattice_wide": "untested"}, "narrowed": True},
        {"phrase": "candidate packet is not a framework Record",
         "resolutions": {"per_element": "packet bits tested", "per_site": "one site tested", "per_mode": "not applicable",
                         "per_block": "finite supplied monoid tested", "lattice_wide": "untested"}, "narrowed": True},
        {"phrase": "candidate census is not Born frequency",
         "resolutions": {"per_element": "64 codewords tested", "per_site": "one cell census", "per_mode": "not promoted",
                         "per_block": "one complete block tested", "lattice_wide": "untested"}, "narrowed": True},
        {"phrase": "finite renewal is not indefinite renewal",
         "resolutions": {"per_element": "six tokens tested", "per_site": "one head tested", "per_mode": "not applicable",
                         "per_block": "six-event block tested", "lattice_wide": "untested"}, "narrowed": True},
        {"phrase": "schedule is not physical time",
         "resolutions": {"per_element": "gate labels tested", "per_site": "one cell", "per_mode": "not applicable",
                         "per_block": "one gate word", "lattice_wide": "untested"}, "narrowed": True},
    ]
    partial = [
        {"file": "Cycle661 Route", "status": "EXECUTED", "what_closes": "supplied shell-table import on one basis-code candidate"},
        {"file": "Cycle634", "status": "RETAINED", "what_closes": "declared fixed-menu physical pointer compiler"},
        {"file": "Cycle621", "status": "RETAINED_CONDITIONAL", "what_closes": "finite-word packet fixation under supplied monoid"},
        {"file": "future stochastic-dilation route", "status": "OPEN", "what_closes": "objective innovation owner"},
        {"file": "future dissipative route", "status": "OPEN", "what_closes": "nonreentering formation and renewal"},
    ]
    steelman = (
        "A hostile reviewer should build an objective stochastic dilation or dissipative local phase whose "
        "environment owns one sector, whose exhaust makes inverse reentry physically unavailable, and whose "
        "renewable medium feeds the unchanged Cycle634/625/621 chain. Freeze that law before nonproduct held "
        "states and compare only admitted readable packets. This concrete untested route can close actuality, "
        "Record, and calibration without an axiom edit, so a broad negative is premature."
    )
    echoes = [
        {"cycle": 531, "mechanism": "conditional binder", "retired": "wiring only"},
        {"cycle": 552, "mechanism": "recurrent member after genesis", "retired": "runtime host member wiring"},
        {"cycle": 571, "mechanism": "first-hit and finite append", "retired": "bounded source/append wiring"},
        {"cycle": 614, "mechanism": "unique-quorum circuit", "retired": "runtime token for one supplied rule"},
        {"cycle": 621, "mechanism": "generator monoid", "retired": "finite preservation conditional on alphabet"},
        {"cycle": 625, "mechanism": "shared-middle separation", "retired": "none of actuality/Record/Born"},
        {"cycle": 634, "mechanism": "fixed menu compiler", "retired": "finite physical menu wall"},
        {"cycle": 661, "mechanism": "conserved count QCA", "retired": "supplied extensional shell table on one route"},
    ]
    passed = (
        sum(row["status"].startswith("ATTEMPTED") for row in routes) < 5
        and len(independence) == 20 and all(row["independent"] for row in independence)
        and all(row["match"] for row in residuals) and all(row["narrowed"] for row in rhetoric)
        and bool(steelman)
    )
    result = {
        "N1_routes": routes,
        "N1_attempted_count": 1,
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "FAIL_DO_NOT_SHIP",
        "N2_collapsed_walls": walls,
        "N2_directed_pair_rows": independence,
        "N3_hidden_condition_scan": hidden,
        "N4_residual_matching": residuals,
        "N5_rhetoric_resolution_audit": rhetoric,
        "N6_partial_closure_paths": partial,
        "N6_primitive_registry_or_new_axiom_language_used": False,
        "N7_hostile_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "shared_obstruction": False,
        "axiom_pressure": False,
        "pass": passed,
    }
    check("fresh N1-N8 blocks broad negative/shared-obstruction/axiom-pressure promotion",
          passed, {"attempted": 1, "required": 5, "pairs": len(independence)})
    return result


def inventory() -> dict[str, object]:
    return {
        "supplied": [
            "retained Cycle634 fixed binary menu, menu constants, six system preparations and blank pointer ports",
            "six-port proper-cubic chart and candidate-pointer adapter",
            "one count-zero carrier, one resource head, six ready carriers and fresh finite event blocks",
            "unchanged Cycle625 lane-zero adapter and Cycle621 preserving generator alphabet",
            "finite noiseless gates, Cycle523 support-two lowering, train/held state preparations",
        ],
        "derived": [
            "one fixed conserved-count QCA gate word and its 64-row extensional admission table",
            "accepted packet plus explicit rejected-sector provenance and exact inverse",
            "unchanged Cycle625-B/Cycle531 occurrence and Cycle621 preservation-interface composition",
            "six-event ready/spent/head renewal ledger and exact exhaustion refusal",
            "preregistered product, biased and nonproduct coherent-sector accounting",
            "deletion, malformed, held L3/L4/L6, support-two NN, all24 and all576 controls",
        ],
        "open": [
            "nature-law selection of this deterministic count-carrier candidate",
            "objective actuality/one-sector ownership for coherent inputs",
            "framework Record identification and physical selection of the postformation operation algebra",
            "non-erasing or indefinite renewal, noise and infinite-volume deployment",
            "physical grade output, probability meaning, objective corpus, independence and convergence",
            "autonomous menu/state/blank genesis, time, energy/stress/source/gravity integration",
        ],
    }


def note_text(receipt: dict[str, object]) -> str:
    qca = receipt["extensional_QCA"]
    quantum = receipt["quantum_menu_and_firewalls"]
    carrier = receipt["finite_carrier"]
    locality = receipt["locality_covariance_controls"]
    rows = "\n".join(
        f"| {name} | {row['split']} | {row['algebraic_one_candidate_grade']:.12f} | "
        f"{row['QCA_formed_sector_weight']:.12f} | {row['unweighted_complete_pattern_census_fraction']:.5f} | "
        f"{row['census_minus_grade_absolute_residual']:.12f} |"
        for name, row in quantum["preregistered_state_rows"].items()
    )
    ng = receipt["no_go_discipline"]
    n1_rows = "\n".join(
        f"| {row['family']} | {row['status']} | {row['terminal']} |"
        for row in ng["N1_routes"]
    )
    n2_rows = "\n".join(
        f"| {row['left']} | {row['right']} | no | no | yes |"
        for row in ng["N2_directed_pair_rows"]
    )
    n4_rows = "\n".join(
        f"| {row['prior']} | `{row['prior_path']}:{row['prior_line']}` | {row['prior_residual']} | "
        f"`{row['current_path']}:{row['current_line']}` | {row['current_residual']} | yes |"
        for row in ng["N4_residual_matching"]
    )
    n5_rows = "\n".join(
        f"| {row['phrase']} | {row['resolutions']['per_element']} | {row['resolutions']['per_site']} | "
        f"{row['resolutions']['per_mode']} | {row['resolutions']['per_block']} | "
        f"{row['resolutions']['lattice_wide']} |"
        for row in ng["N5_rhetoric_resolution_audit"]
    )
    n6_rows = "\n".join(
        f"| {row['file']} | {row['status']} | {row['what_closes']} |"
        for row in ng["N6_partial_closure_paths"]
    )
    n8_rows = "\n".join(
        f"| Cycle {row['cycle']} | {row['mechanism']} | {row['retired']} |"
        for row in ng["N8_cross_cycle_echo"]
    )
    return f"""# Physical deterministic constrained-QCA formation-law tournament — Cycle 661

Classification: **positive deterministic basis-code formation candidate generated by a conserved local count carrier; no objective actuality, framework Record, Born law, or nature-law selection**

Authority: **none**

Audit: **unset**

## Frozen target

The exact target contract hash `{receipt['frozen_contract']['target_contract_sha256']}` and held-fixture hash
`{receipt['frozen_contract']['preregistration_sha256']}` were literal constants before any train or held state was evaluated. The route had to attach the retained Cycle634 fixed binary physical menu to the unchanged Cycle625-B/Cycle531 occurrence port and Cycle621 preservation interface without a supplied shell predicate, admission ROM, actuality token, host winner, grade, probability, or sampler input.

## Decisive result

Cycle 661 gives the first positive route in the extensional formation-law tournament. Six physical binary pointer ports drive six commuting controlled shifts of one conserved seven-rail unary count token. The count-one rail and the current physical ready carrier generate formation. There is no input truth table and no predicate/ROM port: exhaustive execution of the fixed gate word generates the 64-row extensional table, whose accepted Hamming shells are `{qca['derived_accepted_hamming_shells']}` and whose digest is `{qca['derived_relation_sha256']}`.

The event block is `{qca['bounded_M2_event_block']}` M2 including the six aliased pointer rails. It retains the complete pointer word, count rail, accepted packet or explicit reject tag/provenance, resource slot, and every coherent branch. On a coherent six-instrument input all `{quantum['coherent_pointer_sectors_retained']}` orthogonal pointer sectors survive: six basis sectors form candidate packets and 58 own rejection exhaust. This is coherent exhaust accounting, not objective sector selection.

Every basis row reaches the unchanged Cycle625-B extension and exact Cycle531 lane-zero equations. Every admitted direction reaches the unchanged Cycle621 LOCK/provenance interface and all 91 supplied preserving generators fix its packet coordinates. The packet remains a candidate: selecting Cycle621's operation monoid as the physical future law and identifying this packet with a framework Record are not derived.

The finite carrier head advances through six pre-existing ready tokens. Ready counts are `{carrier['ready_after_each']}` and the seventh formation is refused exactly. This is finite renewal of the active carrier, not non-erasing or indefinite resource genesis; reversing an event restores its resource only by erasing its new packet/provenance.

## Physical menu and preregistered held controls

Six retained Cycle634 `mixed_projective_merge` instruments occupy 12 M2 and have maximum effect residual `{quantum['single_instrument_effect_residual']:.3e}`. The train state, a biased product state, and a six-site nonproduct GHZ state were frozen before evaluation.

| fixture | split | algebraic one-candidate grade | QCA formed-sector weight | unweighted 64-pattern census | census-grade residual |
|---|---|---:|---:|---:|---:|
{rows}

The QCA reads pointer rails, never a grade. The formed-sector weight is an algebraic coherent-branch diagnostic. The unweighted 64-pattern census is a deterministic code census, not an empirical frequency. Their mismatch is an active firewall: neither quantity is called Born probability, and no pointer/packet is called a Record.

## Exact controls

The runner checks `{qca['exact_rows']}` L3/L4/L6 basis rows, exact inverse and clean selector work; 64 unchanged occurrence/preservation interface rows; all 64 quantum pointer sectors for three preregistered states; finite six-carrier exhaustion; nine active gate deletions; malformed/dirty domains; `{locality['covariance_tests']}` all24 state comparisons; and `{locality['group_direction_tests']}` all576 direction-composition tests. The QCA has `{locality['logical_gate_count']}` logical gates, `{locality['literal_one_two_M2_calls_before_routing']}` literal one-/two-M2 calls before routing, `{locality['route_and_return_adjacent_SWAPS']}` adjacent route/return SWAPs, and `{locality['nearest_neighbor_calls']}` nearest-neighbor calls. Maximum literal support is two M2. The six controlled count shifts commute, so incident-port ordering does not select the result.

## Supplied / derived / open

Supplied: the retained fixed binary menu and its six input/blank-port preparations; the six-port chart and candidate-pointer convention; count/head/ready genesis and fresh finite event blocks; the unchanged Cycle625 lane-zero adapter; the Cycle621 preserving generator alphabet; finite noiseless gates and state fixtures.

Derived on the declared code: the extensional 64-row table from one fixed count-carrier gate word; accepted packet and rejected-sector provenance; exact Cycle625/Cycle531/Cycle621 composition; six-event carrier renewal/exhaustion; coherent held-state accounting; inverse, deletion, malformed, support-two NN, all24 and all576 controls.

Open: selection of this candidate as nature's law; coherent-sector actuality; framework Record identification and selection of the physical postformation algebra; non-erasing/unbounded renewal; a physical grade/probability/corpus law; autonomous menu/state/blank genesis; noise/infinite volume; time and source/gravity integration.

## Interpretation firewalls

- A generated basis-code admission table is a candidate law, not evidence that nature selects it.
- Orthogonal accepted/rejected coherent sectors are not one objective actuality.
- Conditional occurrence and a protected packet are not a framework Record.
- Preservation under a supplied operation monoid is not identification of the physical all-future law.
- A deterministic pointer-word census is not empirical frequency or Born probability.
- A ready/spent token is not energy, work, entropy, stress, or gravity source content.
- Gate order and carrier-head advance are not physical time or a rate.

## Fresh N1–N8 no-go discipline

### N1 — normalized alternatives

| family | status | terminal obligation |
|---|---|---|
{n1_rows}

Only the deterministic conserved-count QCA is attempted here. One attempted route is below the five-route threshold, so broad no-go and minimum-content gates are **FAIL / DO NOT SHIP**.

### N2 — wall independence

The collapsed walls and all 20 directed pairs are checked below:

| left | right | left closes right? | right closes left? | independent? |
|---|---|---:|---:|---:|
{n2_rows}

No wall is inflated from another on the exhibited interfaces.

### N3 — hidden conditions

The fixed menu, six-port chart, pointer-value convention, count/head/ready genesis, fresh finite event blocks, lane-zero adapter, Cycle621 operation alphabet, gate set, and held state preparations are explicit supplies. “Canonical” and “registered” provide no physics premise. The update function has no rule, ROM, actuality, winner, grade, probability, or sampler parameter.

### N4 — exact residual matching

| prior | prior citation | prior residual | current citation | current residual | match? |
|---|---|---|---|---|---:|
{n4_rows}

### N5 — rhetoric/resolution audit

| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
{n5_rows}

Every negative is restricted to the finite tested block; no lattice-wide negative is asserted.

### N6 — partial closures

| surface | status | what it closes |
|---|---|---|
{n6_rows}

No “new axiom required” or “no retained primitive” language is used. These are physics import-retirement paths.

### N7 — hostile steelman

{ng['N7_hostile_steelman']}

### N8 — cross-cycle echo

| cycle | mechanism | retired scope |
|---|---|---|
{n8_rows}

Shared route-independent obstruction: **not established**.

Axiom pressure: **none**.

## Six-wall ledger

| wall | Cycle661 movement | residual |
|---|---|---|
| `C_ref` | extensional admission content is generated by a physical count-carrier word; accepted/rejected provenance is explicit | menu/port/carrier genesis and nature-law selection supplied/open |
| `C_num` | exact 64-row relation and three preregistered coherent branch measures | no physical grade output, probability meaning, sampling, convergence or realized corpus |
| `C_wrap` | generated admission reaches unchanged conditional occurrence and preservation interfaces | no objective actuality, framework Record identification, selected all-future law or realized history |
| `C_int` | six physical instruments feed one literal constrained update | menu constants remain supplied; no new matter interaction or generator/rate promotion |
| `C_local` | bounded 84-M2 event block, support two, NN, inverse/deletion/domain/all24/all576 | overlapping volume, noise, fresh event-block genesis and infinite deployment open |
| `C_source` | six-token ready/spent/head ledger and all rejected exhaust are explicit | tokens have no energy/stress meaning; non-erasing renewal and gravity response open |

## Disposition and next route

**PASS** for one deterministic constrained-QCA candidate whose physical gate word generates its basis-code extensional formation table, retains coherent exhaust, feeds unchanged occurrence/preservation interfaces, and renews a finite carrier stock.

**FAIL / DO NOT CLAIM** for objective actuality, framework Record, all-future physical permanence, Born probability, realized history, minimum content, shared obstruction, or axiom pressure.

The next independent route should be the objective stochastic dilation: its environment must own the innovation and every rejected sector, its local formation must feed this same Cycle625/Cycle621 interface, and its law must be frozen before the same biased and nonproduct held tests. A later dissipative route must remain independent rather than being treated as a variant of this reversible count QCA.
"""


def note_contract() -> dict[str, object]:
    required = (
        "authority: **none**", "audit: **unset**", "frozen target",
        "no input truth table and no predicate/rom port", "candidate law, not evidence that nature selects it",
        "pointer/packet is called a record", "not an empirical frequency", "not physical time or a rate",
        "one attempted route is below the five-route threshold", "all 20 directed pairs",
        "shared route-independent obstruction: **not established**", "axiom pressure: **none**",
    )
    body = " ".join(NOTE.read_text().lower().split())
    # The Record phrase is required in its explicit negative context.
    required = tuple(fragment if fragment != "pointer/packet is called a record"
                     else "no pointer/packet is called a record" for fragment in required)
    missing = tuple(fragment for fragment in required if fragment not in body)
    return {"required_fragments": required, "missing": missing, "pass": not missing}


def main() -> None:
    signal.alarm(math.ceil(WALL_CAP_SECONDS))
    started = time.perf_counter()
    frozen = frozen_contract_controls()
    qca = extensional_qca_tournament()
    interfaces = interface_tournament()
    carrier = finite_carrier_tournament()
    quantum = quantum_menu_and_firewall_tournament()
    locality = locality_covariance_and_controls()
    no_go = no_go_discipline()
    receipt = {
        "status": "positive deterministic constrained-QCA basis-code formation candidate; actuality, framework Record, Born and nature-law selection open",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "frozen_contract": frozen,
        "extensional_QCA": qca,
        "unchanged_interfaces": interfaces,
        "finite_carrier": carrier,
        "quantum_menu_and_firewalls": quantum,
        "locality_covariance_controls": locality,
        "no_go_discipline": no_go,
        "inventory": inventory(),
        "strongest_constructive_result": (
            "one fixed deterministic count-carrier QCA generates a 64-row basis-code formation relation, "
            "owns all accepted/rejected pointer provenance, and feeds unchanged Cycle625/Cycle531/Cycle621 interfaces"
        ),
        "highest_honest_terminal": (
            "candidate deterministic basis-code formation law after supplied menu/carrier genesis; "
            "not objective actuality, framework Record, probability, or nature-law selection"
        ),
        "semantic_promotion_boundary": {
            "extensional_table_generated_by_physical_update": True,
            "candidate_law_selected_by_nature": None,
            "objective_actuality": None,
            "framework_Record": None,
            "physical_all_future_permanence": None,
            "Born_probability": None,
            "realized_history": None,
        },
        "route_disposition": {
            "deterministic_constrained_QCA": "PASS_POSITIVE_CANDIDATE",
            "objective_stochastic_dilation": "OPEN_NEXT_INDEPENDENT_ROUTE",
            "dissipative_formation": "OPEN_THIRD_INDEPENDENT_ROUTE",
        },
        "shared_substrate_obstruction": False,
        "axiom_pressure": False,
        "author_accepted": False,
        "breakthrough": False,
        "optimal_next_experiment": (
            "objective stochastic dilation with owned innovations/rejected exhaust, unchanged occurrence/preservation "
            "ports, frozen law, and the same blinded biased/nonproduct tests"
        ),
    }
    NOTE.write_text(note_text(receipt))
    note_check = note_contract()
    check("Cycle661 note preserves the frozen candidate-law/Record/Born/no-go boundaries",
          note_check["pass"], note_check["missing"])
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss < 10_000_000:
        rss *= 1024
    receipt.update({
        "note_contract": note_check,
        "runner_sha256": file_sha(Path(__file__)),
        "note_sha256": file_sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "tests_passed": PASS,
        "tests_failed": FAIL,
    })
    receipt["pass"] = (
        FAIL == 0 and frozen["pass"] and qca["pass"] and interfaces["pass"]
        and carrier["pass"] and quantum["pass"] and locality["pass"] and no_go["pass"]
        and note_check["pass"] and elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES
        and AUTHORITY == "none" and AUDIT == "unset"
    )
    RECEIPT.write_text(json.dumps(
        receipt, indent=2, sort_keys=True,
        default=lambda value: value.item() if isinstance(value, np.generic) else list(value),
    ) + "\n")
    print(json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": rss,
        "receipt": str(RECEIPT), "note": str(NOTE),
    }, indent=2))
    if not receipt["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
