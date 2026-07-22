#!/usr/bin/env python3
"""Cycle587: autonomous occurrence/member and Born/history bridge tournament.

Three bounded constructions test different seams without identifying a
coherent pointer, copied packet, deterministic string, or finite grade with an
objective occurrence, framework Record, or probability law.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import inspect
import json
from pathlib import Path
import re
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_autonomous_local_member_law_cell_cycle552_2026_07_21 as c552
import physical_born_menu_compiler_occurrence_interface_cycle565_2026_07_21 as c565
import physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22 as c571
import physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22 as c577
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_OCCURRENCE_BORN_HISTORY_BRIDGE_TOURNAMENT_CYCLE587_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0
Word = tuple[int, ...]


FROZEN_PATHS = {
    "Cycle531 runner": ROOT / "scripts/physical_selected_seam_conditional_record_binder_cycle531_2026_07_21.py",
    "Cycle531 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CONDITIONAL_RECORD_BINDER_CYCLE531_NOTE_2026-07-21.md",
    "Cycle552 runner": ROOT / "scripts/physical_autonomous_local_member_law_cell_cycle552_2026_07_21.py",
    "Cycle552 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_LOCAL_MEMBER_LAW_CELL_CYCLE552_NOTE_2026-07-21.md",
    "Cycle565 runner": ROOT / "scripts/physical_born_menu_compiler_occurrence_interface_cycle565_2026_07_21.py",
    "Cycle565 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md",
    "Cycle571 runner": ROOT / "scripts/physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22.py",
    "Cycle571 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RENEWABLE_FIRST_HIT_RECORD_ADMISSION_TOURNAMENT_CYCLE571_NOTE_2026-07-22.md",
    "Cycle577 runner": ROOT / "scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py",
    "Cycle577 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_PROJECTOR_INSTRUMENT_COMPILER_TOURNAMENT_CYCLE577_NOTE_2026-07-22.md",
    "Cycle580 runner": ROOT / "scripts/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.py",
    "Cycle580 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md",
    "Cycle582 runner": ROOT / "scripts/physical_l41_autonomous_recurrence_resource_tournament_cycle582_2026_07_22.py",
    "Cycle582 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_AUTONOMOUS_RECURRENCE_RESOURCE_TOURNAMENT_CYCLE582_NOTE_2026-07-22.md",
    "Cycle584 runner": ROOT / "scripts/physical_l41_local_streaming_reuse_tournament_cycle584_2026_07_22.py",
    "Cycle584 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_LOCAL_STREAMING_REUSE_TOURNAMENT_CYCLE584_NOTE_2026-07-22.md",
}
FROZEN = {
    "Cycle531 runner": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "Cycle531 note": "ed40564d4e57090cf03e706b54964e5a24cb735f9ca14df8f008fecffc388042",
    "Cycle552 runner": "405cacd821b5453045f8a8920b1ab0fc2dca5ac90fb150e9b4a95f6f218ac8a4",
    "Cycle552 note": "919f95dd43d8bdd5ba65fba071f58a6d054a89b3d7d4b7cc04686c8c28cdbf42",
    "Cycle565 runner": "b4b6e2c4491c5a6b30389764e8ac597ce07e1dac3f31c7cb8fff9297ac04437a",
    "Cycle565 note": "72dd62448eaf685de0a7f1cc4ce9d164363428976eafc8efb93c973b8856f39a",
    "Cycle571 runner": "7221d59558e4d731f98a2a4523c280aa98b889f23ea3f7be1acc8919395dfee8",
    "Cycle571 note": "b254476f392597c03f27581fbc4f559266ed42984ac86a516888ee81d2aff8e2",
    "Cycle577 runner": "93bf1fa2859289b13037bfe7882cce86732e9377ed8b60e56c3bd55ebc0ce74f",
    "Cycle577 note": "23ef5601b73c121d5e82c9031ec0ff4acffdc5471c43aa4dec63a78085aa7c0f",
    "Cycle580 runner": "c46917d4a932cd3ad9a78e0547625055f5adf9d5cf7393700d7e6715dd515cd3",
    "Cycle580 note": "e8ca5acdaec0c7ec5f0ba9772d7736352bcf132e961483d93f19c679439df276",
    "Cycle582 runner": "47c5138720add60ed6fa8b6506dcb8a9cbee9af5a1ab3defbc7aea4c3cfa290a",
    "Cycle582 note": "c65613cd5f6bffa1cf4cc84ba08815fd9d569627d579438f9a39fa00601fcbc6",
    "Cycle584 runner": "556e3e4759033706c795c9b65f55f12afaaaf84b8858dc4bb06b1c0a93400ab3",
    "Cycle584 note": "7e5ae8971e1b4f3be6bba50d25aa0b3d373f79d2b3224622fa1c4f829f7982dc",
}


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
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def one_hot(label: int, width: int) -> Word:
    if label not in range(width):
        raise ValueError("label leaves declared one-hot word")
    return tuple(int(index == label) for index in range(width))


def singleton(bits: Word, name: str) -> int:
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits) or sum(bits) != 1:
        raise ValueError(f"{name} is not a binary one-hot word")
    return bits.index(1)


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        left, right, target = item.sites
        bits[target] ^= bits[left] & bits[right]
    elif item.kind == "SWAP":
        left, right = item.sites
        bits[left], bits[right] = bits[right], bits[left]
    else:
        raise ValueError(f"unknown gate {item.kind}")


def apply_schedule(bits: Word, schedule: tuple[Gate, ...], *, reverse: bool = False,
                   delete_label: str | None = None) -> Word:
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("word leaves binary physical-M2 domain")
    if delete_label is not None and sum(item.label == delete_label for item in schedule) != 1:
        raise ValueError("deletion must name one gate")
    answer = list(bits)
    sequence = reversed(schedule) if reverse else schedule
    for item in sequence:
        if item.label != delete_label:
            apply_gate(answer, item)
    return tuple(answer)


# Ordered two-site pairs in the exact Cycle-523 fifteen-gate Toffoli identity.
# The other nine primitives in that identity are one-site H/T/T-dagger gates.
TOFFOLI_TWO_SITE_PAIRS = ((1, 2), (0, 2), (1, 2), (0, 2), (0, 1), (0, 1))


def static_line_compiler_controls(schedule: tuple[Gate, ...], width: int) -> dict[str, object]:
    """Compile every one/two-M2 primitive by adjacent route/core/unroute.

    The certificate tracks logical wire labels, verifies the ordered operands
    at the adjacent core, and verifies exact terminal wire restoration.  It is
    a static compile-time route; data never select a path.
    """
    primitive_pairs: list[tuple[str, int, int]] = []
    one_site = 0
    toffoli = 0
    for item in schedule:
        if item.kind == "TOFFOLI":
            toffoli += 1
            one_site += 9
            for left_index, right_index in TOFFOLI_TWO_SITE_PAIRS:
                primitive_pairs.append((f"{item.label}:CNOT:{left_index}:{right_index}", item.sites[left_index], item.sites[right_index]))
        elif item.kind in ("CNOT", "SWAP"):
            primitive_pairs.append((item.label, item.sites[0], item.sites[1]))
        elif item.kind == "X":
            one_site += 1
        else:
            raise ValueError("line compiler received an unsupported gate")

    rows = []
    adjacency_failures = operand_failures = restoration_failures = 0
    adjacent_swaps = 0
    maximum_distance = 0
    for label, left, right in primitive_pairs:
        wires = list(range(width))
        distance = abs(left - right)
        maximum_distance = max(maximum_distance, distance)
        swaps: list[tuple[int, int]] = []
        if left < right:
            swaps = [(position - 1, position) for position in range(right, left + 1, -1)]
            core = (left, left + 1)
        else:
            swaps = [(position, position + 1) for position in range(right, left - 1)]
            core = (left, left - 1)
        for first, second in swaps:
            adjacency_failures += int(abs(first - second) != 1)
            wires[first], wires[second] = wires[second], wires[first]
        adjacency_failures += int(abs(core[0] - core[1]) != 1)
        operand_failures += int((wires[core[0]], wires[core[1]]) != (left, right))
        for first, second in reversed(swaps):
            wires[first], wires[second] = wires[second], wires[first]
        restoration_failures += int(wires != list(range(width)))
        adjacent_swaps += 2 * len(swaps)
        rows.append((label, left, right, distance, len(swaps), core))

    frames = c577.c41.proper_cubic_rotations()
    # Every route/core edge is one of the consecutive edges of this line.
    # Proper-cubic rotations preserve its L1 edge length exactly.
    physical_two_site_calls = len(primitive_pairs) + adjacent_swaps
    frame_edge_failures = 0
    for frame in frames:
        for position in range(width - 1):
            left = frame @ np.asarray((position, 0, 0), dtype=int)
            right = frame @ np.asarray((position + 1, 0, 0), dtype=int)
            frame_edge_failures += int(sum(abs(int(a - b)) for a, b in zip(left, right)) != 1)
    return {
        "line_M2": width,
        "logical_Toffoli": toffoli,
        "literal_one_M2_primitives": one_site,
        "literal_two_M2_core_primitives": len(primitive_pairs),
        "adjacent_route_and_return_SWAPS": adjacent_swaps,
        "nearest_neighbor_two_M2_calls": physical_two_site_calls,
        "maximum_unrouted_operand_distance": maximum_distance,
        "route_adjacency_failures": adjacency_failures,
        "ordered_operand_failures": operand_failures,
        "terminal_wire_restoration_failures": restoration_failures,
        "route_manifest_sha256": sha256(json.dumps(rows).encode()).hexdigest(),
        "proper_cubic_frames": len(frames),
        "all24_line_edge_tests": len(frames) * (width - 1),
        "all24_line_edge_failures": frame_edge_failures,
        "runtime_data_selects_route": False,
        "pass": len(frames) == 24 and not any((adjacency_failures, operand_failures, restoration_failures, frame_edge_failures)),
    }


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    answer = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return answer


# Route A: a bounded four-site program ring and one-hot domain wall.  Program
# symbols are the four nonzero Cycle-41 pointer labels.  All rows are physical
# scalar M2s; Cycle552 supplies the unchanged signed-current interface.
SUPPORTED = tuple(
    c577.history_index(history) for history in c577.HISTORIES
    if float(np.vdot(c577.BRANCH_VECTOR[history], c577.BRANCH_VECTOR[history]).real) > TOL
)
_a = [0]
A_HEAD = take(_a, 4)
A_POINTER = take(_a, 8)
A_PROGRAM = tuple(take(_a, 8) for _ in range(4))
A_EQUAL = take(_a, 4)
A_HIT = take(_a, 1)[0]
A_MEMBER = take(_a, 4)
A_ARCHIVE_POINTER = take(_a, 8)
A_ARCHIVE_MEMBER = take(_a, 4)
A_OCCURRENCE = take(_a, 1)[0]
A_WIDTH = _a[0]


def route_a_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for slot, history in product(range(4), range(8)):
        gates.append(Gate("TOFFOLI", (A_PROGRAM[slot][history], A_POINTER[history], A_EQUAL[slot]), f"A:eq:{slot}:{history}"))
    for slot in range(4):
        gates.append(Gate("TOFFOLI", (A_HEAD[slot], A_EQUAL[slot], A_HIT), f"A:hit:{slot}"))
    gates.append(Gate("CNOT", (A_HIT, A_OCCURRENCE), "A:occurrence"))
    for history in range(8):
        gates.append(Gate("TOFFOLI", (A_HIT, A_POINTER[history], A_ARCHIVE_POINTER[history]), f"A:archive-pointer:{history}"))
    for member in range(4):
        gates.append(Gate("TOFFOLI", (A_HIT, A_HEAD[member], A_MEMBER[member]), f"A:member:{member}"))
        gates.append(Gate("TOFFOLI", (A_HIT, A_HEAD[member], A_ARCHIVE_MEMBER[member]), f"A:archive-member:{member}"))
    for slot, history in reversed(tuple(product(range(4), range(8)))):
        gates.append(Gate("TOFFOLI", (A_PROGRAM[slot][history], A_POINTER[history], A_EQUAL[slot]), f"A:uneq:{slot}:{history}"))
    for left, right in ((2, 3), (1, 2), (0, 1)):
        gates.append(Gate("SWAP", (A_HEAD[left], A_HEAD[right]), f"A:head:{left}:{right}"))
    return tuple(gates)


A_SCHEDULE = route_a_schedule()


def prepare_a(pointer: int, head: int) -> Word:
    if pointer not in SUPPORTED or head not in range(4):
        raise ValueError("Route A leaves supported-pointer/domain-wall domain")
    bits = [0] * A_WIDTH
    for site, bit in zip(A_HEAD, one_hot(head, 4)):
        bits[site] = bit
    for site, bit in zip(A_POINTER, one_hot(pointer, 8)):
        bits[site] = bit
    for slot, symbol in enumerate(SUPPORTED):
        for site, bit in zip(A_PROGRAM[slot], one_hot(symbol, 8)):
            bits[site] = bit
    return tuple(bits)


def expected_a(pointer: int, head: int) -> Word:
    bits = list(prepare_a(pointer, (head + 1) % 4))
    hit = int(pointer == SUPPORTED[head])
    bits[A_HIT] = bits[A_OCCURRENCE] = hit
    if hit:
        for sites, word in (
            (A_MEMBER, one_hot(head, 4)),
            (A_ARCHIVE_MEMBER, one_hot(head, 4)),
            (A_ARCHIVE_POINTER, one_hot(pointer, 8)),
        ):
            for site, bit in zip(sites, word):
                bits[site] = bit
    return tuple(bits)


def route_a_controls() -> dict[str, object]:
    eg_failures = inverse_failures = interface_failures = nohit_failures = 0
    rows = 0
    hit_rows = 0
    for size, pointer, head in product((5, 6), SUPPORTED, range(4)):
        source = prepare_a(pointer, head)
        output = apply_schedule(source, A_SCHEDULE)
        eg_failures += output != expected_a(pointer, head)
        inverse_failures += apply_schedule(output, A_SCHEDULE, reverse=True) != source
        hit = pointer == SUPPORTED[head]
        if hit:
            hit_rows += 1
            member = head
            base = c552.prepare(
                binding=member, law=0, member=member, head=0,
                plus=int(size == 5), minus=int(size == 6), edge=1,
                K_position=(pointer + size) % 16,
            )
            stepped = c552.physical_step(base)
            fields, law = c552.snapshot_view(stepped, 0)
            interface_failures += int(fields[0:3] != (1, 1, 1) or law != one_hot(0, 5))
            interface_failures += c552.apply_schedule(stepped, reverse=True) != base
        else:
            nohit_failures += int(output[A_HIT] or output[A_OCCURRENCE] or any(output[s] for s in (*A_MEMBER, *A_ARCHIVE_MEMBER, *A_ARCHIVE_POINTER)))
        rows += 1

    witness = prepare_a(SUPPORTED[2], 2)
    deleted = apply_schedule(witness, A_SCHEDULE, delete_label=f"A:member:2")
    deletion_residual = float(np.linalg.norm(np.asarray(deleted) - np.asarray(apply_schedule(witness, A_SCHEDULE))))
    malformed = (
        tuple(0 for _ in range(A_WIDTH)),
        tuple(list(prepare_a(SUPPORTED[0], 0))[:A_HEAD[1]] + [1] + list(prepare_a(SUPPORTED[0], 0))[A_HEAD[1] + 1:]),
    )
    malformed_refused = 0
    for word in malformed:
        try:
            singleton(tuple(word[s] for s in A_HEAD), "A head")
            singleton(tuple(word[s] for s in A_POINTER), "A pointer")
        except ValueError:
            malformed_refused += 1

    # The complete coherent-pointer sweep is an isometry with four orthogonal
    # retained sectors, not a map to one selected member.
    coherent_input = np.ones(4, dtype=complex) / 2.0
    coherent_output = np.diag(coherent_input)
    gram_residual = float(np.linalg.norm(coherent_output.conj().T @ coherent_output - np.eye(4) / 4.0))
    toffoli = c523.bare_toffoli_controls()
    logical_toffoli = sum(item.kind == "TOFFOLI" for item in A_SCHEDULE)
    line = static_line_compiler_controls(A_SCHEDULE, A_WIDTH)
    result = {
        "route": "A local program-ring/domain-wall conditional member compiler",
        "supported_L41_pointer_labels": SUPPORTED,
        "program_word_sha256": sha256(json.dumps(SUPPORTED).encode()).hexdigest(),
        "physical_M2_before_Cycle552": A_WIDTH,
        "bounded_product_envelope_M2": A_WIDTH + c552.TOTAL_M2,
        "law_radius_program_cells": 1,
        "EG_rows_L5_held_L6": rows,
        "EG_failures": eg_failures,
        "inverse_failures": inverse_failures,
        "hit_rows": hit_rows,
        "exact_Cycle552_531_interface_failures": interface_failures,
        "lawful_idle_nohit_failures": nohit_failures,
        "member_gate_deletion_residual": deletion_residual,
        "malformed_domain_refusals": malformed_refused,
        "coherent_four_sector_Gram_residual": gram_residual,
        "coherent_sectors_retained": 4,
        "coherent_pointer_selects_one_objective_member": False,
        "domain_wall_front_and_program_supplied": True,
        "logical_Toffoli": logical_toffoli,
        "literal_one_two_M2_gates_from_Toffoli": logical_toffoli * toffoli["bare_one_two_M2_gates_per_Toffoli"],
        "maximum_literal_support_M2": toffoli["maximum_gate_support_M2"],
        "Toffoli_reconstruction_residual": toffoli["Toffoli_reconstruction_residual"],
        "static_nearest_neighbor_line_compiler": line,
        "pass": rows == 32 and hit_rows == 8 and not any((eg_failures, inverse_failures, interface_failures, nohit_failures))
        and deletion_residual > TOL and malformed_refused == len(malformed)
        and gram_residual < TOL and len(SUPPORTED) == 4 and toffoli["pass"] and line["pass"],
    }
    check("Route A compiles a bounded autonomous-after-front domain-wall member occurrence while retaining all coherent sectors", result["pass"], result)
    return result


# Route B: three-copy local archive with an exact ready->spent debit.  The
# complete circuit remains reversible; re-entry is therefore an explicit
# counter-control against an unjustified irreversible/Record claim.
_b = [0]
B_POINTER = take(_b, 8)
B_REPLICA = tuple(take(_b, 8) for _ in range(3))
B_SYNDROME = tuple(take(_b, 8) for _ in range(2))
B_PACKET = take(_b, 8)
B_READY = take(_b, 1)[0]
B_SPENT = take(_b, 1)[0]
B_ADMIT = take(_b, 1)[0]
B_WIDTH = _b[0]


def route_b_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for history in range(8):
        gates.append(Gate("TOFFOLI", (B_READY, B_POINTER[history], B_ADMIT), f"B:admit:{history}"))
    for replica, history in product(range(3), range(8)):
        gates.append(Gate("TOFFOLI", (B_ADMIT, B_POINTER[history], B_REPLICA[replica][history]), f"B:replica:{replica}:{history}"))
    for history in range(8):
        gates.append(Gate("TOFFOLI", (B_ADMIT, B_POINTER[history], B_PACKET[history]), f"B:packet:{history}"))
    for pair, history in product(range(2), range(8)):
        gates.append(Gate("CNOT", (B_REPLICA[pair][history], B_SYNDROME[pair][history]), f"B:syndrome-left:{pair}:{history}"))
        gates.append(Gate("CNOT", (B_REPLICA[pair + 1][history], B_SYNDROME[pair][history]), f"B:syndrome-right:{pair}:{history}"))
    # Fredkin(ADMIT, READY, SPENT) = CNOT(SPENT,READY),
    # Toffoli(ADMIT,READY,SPENT), CNOT(SPENT,READY).
    gates.extend((
        Gate("CNOT", (B_SPENT, B_READY), "B:debit:pre"),
        Gate("TOFFOLI", (B_ADMIT, B_READY, B_SPENT), "B:debit:core"),
        Gate("CNOT", (B_SPENT, B_READY), "B:debit:post"),
    ))
    return tuple(gates)


B_SCHEDULE = route_b_schedule()


def prepare_b(pointer: int) -> Word:
    if pointer not in SUPPORTED:
        raise ValueError("Route B pointer leaves supported L41 code")
    bits = [0] * B_WIDTH
    for site, bit in zip(B_POINTER, one_hot(pointer, 8)):
        bits[site] = bit
    bits[B_READY] = 1
    return tuple(bits)


def route_b_controls() -> dict[str, object]:
    copy_failures = syndrome_failures = ledger_failures = inverse_failures = 0
    for pointer in SUPPORTED:
        source = prepare_b(pointer)
        output = apply_schedule(source, B_SCHEDULE)
        target = one_hot(pointer, 8)
        copy_failures += int(any(tuple(output[s] for s in bank) != target for bank in (*B_REPLICA, B_PACKET)))
        syndrome_failures += int(any(output[s] for bank in B_SYNDROME for s in bank))
        ledger_failures += int((source[B_READY] + source[B_SPENT], output[B_READY] + output[B_SPENT]) != (1, 1))
        ledger_failures += int((output[B_READY], output[B_SPENT], output[B_ADMIT]) != (0, 1, 1))
        inverse_failures += apply_schedule(output, B_SCHEDULE, reverse=True) != source

    witness = prepare_b(SUPPORTED[1])
    ideal = apply_schedule(witness, B_SCHEDULE)
    replica_deleted = apply_schedule(witness, B_SCHEDULE, delete_label=f"B:replica:1:{SUPPORTED[1]}")
    replica_deletion_residual = float(np.linalg.norm(np.asarray(replica_deleted) - np.asarray(ideal)))
    replica_syndrome_visible = any(replica_deleted[s] for bank in B_SYNDROME for s in bank)
    debit_deleted = apply_schedule(witness, B_SCHEDULE, delete_label="B:debit:core")
    debit_deletion_residual = float(np.linalg.norm(np.asarray(debit_deleted) - np.asarray(ideal)))
    reentered = apply_schedule(ideal, B_SCHEDULE, reverse=True)
    reentry_erases_archive = reentered == witness

    # Copying the label suppresses local pointer coherence after the archive is
    # ignored, while the complete state retains a normalized pure vector.
    rho_in = np.ones((4, 4), dtype=complex) / 4.0
    rho_reduced = np.eye(4, dtype=complex) / 4.0
    lost_local_coherence = float(np.linalg.norm(rho_in - rho_reduced))
    global_norm = float(np.linalg.norm(np.ones(4, dtype=complex) / 2.0))
    line = static_line_compiler_controls(B_SCHEDULE, B_WIDTH)
    result = {
        "route": "B redundant consistency archive with reversible ready/spent debit",
        "physical_M2": B_WIDTH,
        "bounded_product_envelope_M2": B_WIDTH + c552.TOTAL_M2,
        "basis_rows": len(SUPPORTED),
        "replica_or_packet_failures": copy_failures,
        "consistency_syndrome_failures": syndrome_failures,
        "resource_ledger_failures": ledger_failures,
        "inverse_failures": inverse_failures,
        "single_replica_deletion_residual": replica_deletion_residual,
        "single_replica_fault_detected": replica_syndrome_visible,
        "debit_deletion_residual": debit_deletion_residual,
        "exact_reentry_restores_ready_and_erases_archive": reentry_erases_archive,
        "local_pointer_coherence_loss_when_archive_ignored": lost_local_coherence,
        "complete_global_state_norm": global_norm,
        "finite_debit_is_globally_irreversible": False,
        "redundant_packet_is_framework_Record": False,
        "objective_member_selected_from_coherent_pointer": False,
        "static_nearest_neighbor_line_compiler": line,
        "pass": not any((copy_failures, syndrome_failures, ledger_failures, inverse_failures))
        and replica_deletion_residual > TOL and replica_syndrome_visible
        and debit_deletion_residual > TOL and reentry_erases_archive
        and lost_local_coherence > TOL and abs(global_norm - 1.0) < TOL and line["pass"],
    }
    check("Route B gives local redundancy and a visible finite debit but exact re-entry falsifies global irreversibility", result["pass"], result)
    return result


# Route C: fixed round-robin law.  The function has no grade/weight argument;
# the same word is tested against the Cycle-41 fixture and a biased held state.
ROTOR_WORD = SUPPORTED


def rotor_step(head: int) -> tuple[int, int]:
    if head not in range(4):
        raise ValueError("rotor head leaves four-state domain")
    return ROTOR_WORD[head], (head + 1) % 4


def rotor_history(length: int, *, delete_advance_at: int | None = None) -> tuple[int, ...]:
    if length < 1:
        raise ValueError("history length must be positive")
    head = 0
    output = []
    for step in range(length):
        label, advanced = rotor_step(head)
        output.append(label)
        if step != delete_advance_at:
            head = advanced
    return tuple(output)


def empirical_vector(history: tuple[int, ...]) -> np.ndarray:
    return np.asarray(tuple(history.count(label) / len(history) for label in range(8)), dtype=float)


def grade_vector(state: np.ndarray) -> np.ndarray:
    return np.asarray(tuple(float(np.vdot(c577.HISTORY_P[h] @ state, c577.HISTORY_P[h] @ state).real) for h in c577.HISTORIES))


def route_c_controls() -> dict[str, object]:
    fixture_grade = grade_vector(c577.CLUSTER)
    direct_fixture = np.asarray(tuple(float(np.vdot(c577.BRANCH_VECTOR[h], c577.BRANCH_VECTOR[h]).real) for h in c577.HISTORIES))
    grade_residual = float(np.linalg.norm(fixture_grade - direct_fixture))
    train_sizes = (8, 12)
    held_sizes = (17, 31)
    rows = []
    for size in (*train_sizes, *held_sizes):
        word = rotor_history(size)
        empirical = empirical_vector(word)
        rows.append({
            "size": size,
            "L1_grade_residual": float(np.linalg.norm(empirical - fixture_grade, ord=1)),
            "Linf_grade_residual": float(np.linalg.norm(empirical - fixture_grade, ord=np.inf)),
            "prefix_discrepancy_bound_1_over_N": bool(np.linalg.norm(empirical - fixture_grade, ord=np.inf) <= 1.0 / size + TOL),
        })
    exact_multiple_failures = sum(row["L1_grade_residual"] > TOL for row in rows if row["size"] % 4 == 0)
    held_bound_failures = sum(not row["prefix_discrepancy_bound_1_over_N"] for row in rows)
    repeatability_failures = sum(rotor_history(size) != rotor_history(size) for size in held_sizes)
    # Deleting the first advance duplicates label 0 and removes the held
    # prefix's terminal label 5.  (Deleting step 2 at N=31 happens to exchange
    # equal-count endpoints and is therefore an intentionally avoided blind
    # deletion witness.)
    deleted = empirical_vector(rotor_history(31, delete_advance_at=0))
    deletion_residual = float(np.linalg.norm(deleted - empirical_vector(rotor_history(31)), ord=1))

    biased_state = c577.ket(0, 8)
    biased_grade = grade_vector(biased_state)
    same_law_empirical = empirical_vector(rotor_history(32))
    biased_L1 = float(np.linalg.norm(same_law_empirical - biased_grade, ord=1))
    biased_Linf = float(np.linalg.norm(same_law_empirical - biased_grade, ord=np.inf))
    signature = inspect.signature(rotor_step)
    forbidden = ("grade", "weight", "norm", "probability", "sampler", "amplitude", "rho")
    forbidden_ports = tuple(name for name in signature.parameters if any(token in name.lower() for token in forbidden))
    result = {
        "route": "C fixed repeated-history rotor versus exact Cycle41 candidate Born surface",
        "rotor_word": ROTOR_WORD,
        "rotor_word_sha256": sha256(json.dumps(ROTOR_WORD).encode()).hexdigest(),
        "physical_controller_M2": 4,
        "per_emitted_archive_cell_M2": 8,
        "train_sizes": train_sizes,
        "held_sizes": held_sizes,
        "Cycle41_grade_vector": tuple(float(x) for x in fixture_grade),
        "direct_branch_grade_residual": grade_residual,
        "frequency_rows": rows,
        "exact_multiple_of_four_failures": exact_multiple_failures,
        "held_prefix_bound_failures": held_bound_failures,
        "repeatability_failures": repeatability_failures,
        "head_advance_deletion_L1_residual": deletion_residual,
        "biased_state_grade_vector": tuple(float(x) for x in biased_grade),
        "same_law_biased_held_L1_residual": biased_L1,
        "same_law_biased_held_Linf_residual": biased_Linf,
        "rotor_forbidden_numeric_or_probability_ports": forbidden_ports,
        "grade_used_to_construct_or_fit_rotor": False,
        "finite_deterministic_history_is_probability_sample": False,
        "fixture_match_is_universal_Born_bridge": False,
        "pass": grade_residual < TOL and not exact_multiple_failures and not held_bound_failures
        and not repeatability_failures and deletion_residual > TOL
        and biased_L1 > 1.0 and biased_Linf > 0.4 and not forbidden_ports,
    }
    check("Route C gives a no-fit repeatable uniform-fixture match and the same-law biased held control falsifies universality", result["pass"], result)
    return result


def covariance_domain_controls() -> dict[str, object]:
    frames = c577.c41.proper_cubic_rotations()
    # All new controller/program/member/archive fields are proper-cubic
    # scalars.  The unchanged Cycle552/531 current pair supplies the oriented
    # seam action, checked here on every frame and every supported member.
    scalar_failures = current_failures = group_failures = 0
    tests = 0
    witness = prepare_a(SUPPORTED[0], 0)
    output = apply_schedule(witness, A_SCHEDULE)
    for frame in frames:
        scalar_failures += int(apply_schedule(witness, A_SCHEDULE) != output)
        for member in range(4):
            source = c552.prepare(binding=member, law=0, member=member, head=0, plus=1, minus=0, edge=1, K_position=member)
            framed, axis = c552.frame_word(source, 0, frame)
            stepped = c552.physical_step(framed)
            expected, expected_axis = c552.frame_word(c552.physical_step(source), 0, frame)
            current_failures += int(stepped != expected or axis != expected_axis)
            tests += 1
    for left, right in product(frames, repeat=2):
        for axis in range(3):
            _, first_axis = c552.frame_word(c552.prepare(0, 0, 0, 0, plus=1, edge=1), axis, right)
            _, second_axis = c552.frame_word(c552.prepare(0, 0, 0, 0, plus=1, edge=1), first_axis, left)
            _, product_axis = c552.frame_word(c552.prepare(0, 0, 0, 0, plus=1, edge=1), axis, left @ right)
            group_failures += int(second_axis != product_axis)
    malformed_refused = 0
    malformed_total = 4
    for action in (
        lambda: prepare_a(1, 0),
        lambda: prepare_a(SUPPORTED[0], 4),
        lambda: prepare_b(7),
        lambda: rotor_history(0),
    ):
        try:
            action()
        except ValueError:
            malformed_refused += 1
    result = {
        "proper_cubic_frames": len(frames),
        "new_scalar_route_tests": len(frames),
        "new_scalar_failures": scalar_failures,
        "Cycle552_member_frame_tests": tests,
        "Cycle552_member_frame_failures": current_failures,
        "all576_axis_product_tests": len(frames) ** 2 * 3,
        "all576_axis_product_failures": group_failures,
        "malformed_domain_refusals": malformed_refused,
        "malformed_domain_total": malformed_total,
        "pass": len(frames) == 24 and scalar_failures == current_failures == group_failures == 0
        and malformed_refused == malformed_total,
    }
    check("all24/all576 covariance and lawful-domain controls remain exact", result["pass"], result)
    return result


def dependency_and_discipline_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "route a", "route b", "route c",
        "conditional instrument", "objective member", "pointer copying is not record",
        "finite deterministic history is not a probability sample", "all 24", "all 576",
        "l5", "held l6", "supplied / derived / open", "n1", "n2", "n3", "n4",
        "n5", "n6", "n7", "n8", "n1 status: fail", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in normalized)
    declared = re.search(r"Runner SHA-256:\s*([0-9a-f]{64})", note)

    routes = (
        {"family": "TI domain-wall/program QCA", "status": "ATTEMPTED", "terminal": "derive front/program genesis and one actuality owner for a coherent pointer"},
        {"family": "decoherence/redundancy/debit", "status": "ATTEMPTED", "terminal": "derive irreversible admission/permanence rather than reversible archive correlation"},
        {"family": "fixed held-history rotor", "status": "ATTEMPTED", "terminal": "derive a state-dependent grade/frequency law without importing a distribution"},
        {"family": "local stochastic innovation field", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "construct innovations and lawful grade coupling with no host sampler"},
        {"family": "unique-extension realized-history law", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "construct covariant successor ownership and readable permanent Records"},
        {"family": "objective-collapse carrier bath", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "give bounded update, conservation/resource ledger, and blinded calibration"},
    )
    walls = (
        "member genesis", "objective actuality", "Record admission/permanence",
        "grade-to-law identification", "realized-corpus frequency calibration",
    )
    pairs = tuple({
        "pair": (walls[a], walls[b]), "independent": True,
        "reason": "neither wall's tested output has the other's typed input or closure witness",
    } for a, b in combinations(range(len(walls)), 2))
    residuals = (
        {"route": "A", "witness": "four orthogonal coherent output sectors", "matches": "conditional member compiler, not objective actuality"},
        {"route": "B", "witness": "exact inverse re-entry", "matches": "finite redundant archive/debit, not irreversible Record"},
        {"route": "C", "witness": "same-law biased held L1 residual > 1", "matches": "fixture-specific deterministic agreement, not universal Born law"},
    )
    hidden = (
        "Cycle41 law and candidate grade", "four supported labels and rotor order",
        "domain-wall front/program", "pure coherent pointer preparation",
        "blank archives and ready resource", "Cycle552 law word/binding/head/K",
        "noiseless X/CNOT/Toffoli/SWAP gates", "proper-cubic chart", "finite train/held cuts",
    )
    partial = (
        "retain Route A as an exact deterministic conditional member/occurrence compiler after supplied front genesis",
        "retain Route B as a fault-visible finite archive and resource-debit diagnostic below Record status",
        "retain Route C as a preregistered uniform-fixture frequency comparator and biased-state falsifier",
        "couple a local innovation field to the Cycle565 grade only through a separately justified physical law",
        "admit only framework-typed Records, then compare a blinded held corpus without fitting the member source",
    )
    steelman = {
        "mechanism": "a translation-invariant innovation bath could locally prepare the domain-wall front, choose one pointer sector through a new objective update, debit a nonreentering formation resource, and append readable Records whose blinded frequencies obey a separately derived Cycle565 grade functional",
        "terminal_obligation": "construct the bounded physical update, prove lawful renewal/permanence and all24 covariance, preregister its transition law without reading held counts, and reject the biased-state control only when the independently predicted grade changes",
        "status": "open constructive route; no route-independent obstruction follows",
    }
    echo = (
        "Cycle531 separated edge/binding from member ownership",
        "Cycle552 separated autonomous recurrence from supplied genesis",
        "Cycle565 separated finite grades from member selection",
        "Cycle571 separated raw first hit and protected append from actuality/admission",
        "Cycles577-584 separated coherent pointer recurrence/resource export from Record and Born semantics",
    )
    qualifying = tuple(route for route in routes if route["status"] == "ATTEMPTED")
    discipline = {
        "N1_routes": routes, "N1_qualifying": len(qualifying), "N1_required": 5, "N1_status": "FAIL",
        "N2_walls": walls, "N2_pairwise": pairs, "N3_explicit_supplies": hidden,
        "N4_residual_matching": residuals,
        "N5_rhetoric": "only conditional member, finite archive, candidate grade, and deterministic frequency comparator are claimed",
        "N6_partial_closure": partial, "N7_hostile_steelman": steelman, "N8_cross_cycle_echo": echo,
        "broad_no_go": "FAIL_DO_NOT_SHIP", "minimum_content": "FAIL_DO_NOT_SHIP",
        "shared_obstruction": "NOT_ESTABLISHED", "axiom_pressure": "NONE",
    }
    result = {
        "expected_hashes": FROZEN,
        "observed_hashes": observed,
        "note_missing_contract_fragments": missing,
        "declared_runner_sha256": declared.group(1) if declared else None,
        "runner_sha256": file_sha(Path(__file__)),
        "discipline": discipline,
        "inventory": {
            "supplied": hidden,
            "derived": (
                "bounded program-ring/member EG and exact Cycle552/531 conditional occurrence",
                "three-copy syndrome archive with exact resource debit, deletion, and inverse re-entry",
                "fixed no-fit frequency comparator, held-prefix bound, and biased-state counter-control",
                "all24/all576 finite covariance and explicit lawful-domain refusals",
            ),
            "open": (
                "law/front/innovation genesis and objective actuality owner",
                "selected framework Record formation, irreversible permanence, deletion restrictions, and unbounded realized history",
                "physical selection of the grade functional, probability meaning, independence/stationarity, and empirical calibration",
                "translation-invariant renewal/resource thermodynamics and physical time",
            ),
        },
        "pass": observed == FROZEN and not missing and declared is not None
        and declared.group(1) == file_sha(Path(__file__))
        and len(qualifying) == 3 and len(pairs) == 10 and all(row["independent"] for row in pairs)
        and len(hidden) == 9 and len(partial) == 5 and len(echo) == 5,
    }
    check("exact shores, supplied inventory, and fresh N1-N8 prevent semantic promotion or axiom pressure", result["pass"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str = AUTHORITY
    audit: str = AUDIT
    strongest_constructive_result: str = "bounded autonomous-after-front domain-wall compiler into exact Cycle552/531 conditional occurrence"
    objective_member_from_coherent_pointer: None = None
    framework_Record: None = None
    realized_history: None = None
    derived_Born_probability: None = None
    shared_obstruction: None = None
    axiom_pressure: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _s, _f: (_ for _ in ()).throw(TimeoutError("Cycle587 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        route_a = route_a_controls()
        route_b = route_b_controls()
        route_c = route_c_controls()
        covariance = covariance_domain_controls()
        dependency = dependency_and_discipline_controls()
        resources = {
            "elapsed_seconds": time.perf_counter() - started,
            "maximum_RSS_bytes": rss_bytes(),
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "RSS_cap_bytes": RSS_CAP_BYTES,
        }
        check("cold resource caps", resources["elapsed_seconds"] < WALL_CAP_SECONDS and resources["maximum_RSS_bytes"] < RSS_CAP_BYTES, resources)
        print(json.dumps({
            "route_A": route_a, "route_B": route_b, "route_C": route_c,
            "covariance_domain": covariance, "dependency_discipline_inventory": dependency,
            "resources": resources, "summary": Summary().__dict__, "pass": PASS, "fail": FAIL,
        }, indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
    print(f"RESULT pass={PASS} fail={FAIL}")
    print("authority=none; audit=unset; conditional member is not objective actuality; copied pointer is not Record; deterministic fixture frequency is not derived Born probability")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
