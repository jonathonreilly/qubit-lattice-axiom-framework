#!/usr/bin/env python3
"""Cycle568: objective-member / protected commit-candidate tournament.

Three independent bounded sources feed the exact Cycle552 MEMBER_STATE plus
law-word boundary and therefore the unchanged Cycle531 conditional-occurrence
binder.  The routes are an orthogonal retained environment, an explicit local
innovation carrier with a conserved token ledger, and a deterministic unary
seed / threshold table.  A downstream reversible packet exercises formation,
close, commit, redundancy, and continuation diagnostics but is deliberately
typed below framework Record.

No algebraic grade, branch norm, reduced diagonal, sampler, or probability is
a prepare/step/member port.  Pointer correlation and packet copying are not
promoted to Record or realized history.
"""

from __future__ import annotations

import ast
from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import inspect
import json
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_born_menu_compiler_occurrence_interface_cycle565_2026_07_21 as c565


c552 = c565.c552
c531 = c552.c531
c505 = c531.c505

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_OBJECTIVE_MEMBER_RECORD_BRIDGE_TOURNAMENT_CYCLE568_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
ACCEPTED_CYCLE565_COMMIT = "0b7c0e7c7173b4df972a769a20f976c5bc8f4aa8"
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Gate = c505.Gate

FROZEN_PATHS = {
    "Cycle565 runner": ROOT / "scripts/physical_born_menu_compiler_occurrence_interface_cycle565_2026_07_21.py",
    "Cycle565 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md",
    "Cycle552 runner": ROOT / "scripts/physical_autonomous_local_member_law_cell_cycle552_2026_07_21.py",
    "Cycle552 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_LOCAL_MEMBER_LAW_CELL_CYCLE552_NOTE_2026-07-21.md",
    "Cycle531 runner": ROOT / "scripts/physical_selected_seam_conditional_record_binder_cycle531_2026_07_21.py",
    "Cycle531 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CONDITIONAL_RECORD_BINDER_CYCLE531_NOTE_2026-07-21.md",
}
FROZEN = {
    "Cycle565 runner": "b4b6e2c4491c5a6b30389764e8ac597ce07e1dac3f31c7cb8fff9297ac04437a",
    "Cycle565 note": "72dd62448eaf685de0a7f1cc4ce9d164363428976eafc8efb93c973b8856f39a",
    "Cycle552 runner": "405cacd821b5453045f8a8920b1ab0fc2dca5ac90fb150e9b4a95f6f218ac8a4",
    "Cycle552 note": "919f95dd43d8bdd5ba65fba071f58a6d054a89b3d7d4b7cc04686c8c28cdbf42",
    "Cycle531 runner": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "Cycle531 note": "ed40564d4e57090cf03e706b54964e5a24cb735f9ca14df8f008fecffc388042",
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


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def declared_runner_sha() -> str | None:
    if not NOTE.exists():
        return None
    import re
    match = re.search(r"Runner SHA-256:\s*([0-9a-f]{64})", NOTE.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def dependency_and_note_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    required = (
        "authority: none", "audit: unset", "accepted cycle 565", "exact cycle-552 member_state",
        "unchanged cycle-531 conditional occurrence", "route a", "route b", "route c",
        "formation", "close", "commit", "permanence", "pointer copying is not record",
        "train l5", "held l6", "all24", "all576", "inverse", "leakage", "deletion",
        "lawful domain", "supplied / derived / open", "n1", "n2", "n3", "n4", "n5",
        "n6", "n7", "n8", "broad no-go", "no axiom pressure", "authority remains none",
        "audit remains unset", "no frequency bridge", "grade does not choose the member",
    )
    body = normalized(NOTE)
    missing = tuple(fragment for fragment in required if fragment not in body)
    self_sha = file_sha(Path(__file__))
    return {
        "accepted_Cycle565_commit": ACCEPTED_CYCLE565_COMMIT,
        "expected": FROZEN,
        "observed": observed,
        "note_missing_contract_phrases": missing,
        "runner_SHA256": self_sha,
        "declared_runner_SHA256": declared_runner_sha(),
        "pass": observed == FROZEN and not missing and declared_runner_sha() == self_sha,
    }


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    result = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return result


# Common physical layout.  The first 276 M2 are byte-for-byte the Cycle552
# interface.  A three-bit Cycle565 program label is locally decoded to seven
# rails by one fixed reversible schedule; label seven has no admitted rail.
_common = [c552.TOTAL_M2]
PROGRAM_BITS = take(_common, 3)
PROGRAM_ONEHOT = take(_common, 7)
PROGRAM_WORK = take(_common, 1)[0]
SIZE_TAG = take(_common, 2)
FORMATION_READY = take(_common, 1)[0]
CLOSE_READY = take(_common, 1)[0]
CAPACITY_READY = take(_common, 1)[0]
FORMATION = take(_common, 1)[0]
CLOSE = take(_common, 1)[0]
COMMIT = take(_common, 1)[0]
ARCHIVE_FIELDS = take(_common, 12)
ARCHIVE_MEMBER = tuple(take(_common, 5) for _ in range(3))
ARCHIVE_LAW = tuple(take(_common, 5) for _ in range(3))
ARCHIVE_PROGRAM = take(_common, 7)
COMMON_END = _common[0]

_a = [COMMON_END]
A_SYSTEM = take(_a, 5)
A_LAW_SOURCE = take(_a, 5)
A_ENV_MEMBER = take(_a, 5)
A_ENV_RECEIPT = take(_a, 5)
A_ENV_REDUNDANCY = tuple(take(_a, 5) for _ in range(2))
A_WIDTH = _a[0]

_b = [COMMON_END]
B_INNOVATION = take(_b, 5)
B_LAW_IN = take(_b, 5)
B_READY = take(_b, 5)
B_CORRELATION_SINK = take(_b, 5)
B_WIDTH = _b[0]

_c = [COMMON_END]
C_SEED = take(_c, 12)
C_LAW_SOURCE = take(_c, 5)
C_HIDDEN_LABEL = take(_c, 5)
C_WIDTH = _c[0]

WIDTHS = {"A": A_WIDTH, "B": B_WIDTH, "C": C_WIDTH}
ROUTE_LABELS = {"A": A_ENV_MEMBER, "B": B_CORRELATION_SINK, "C": C_HIDDEN_LABEL}


@dataclass(frozen=True)
class ProtectedCommitCandidate:
    route: str
    program: int
    size: int
    source_index: int
    selected_member: int
    law_shift: int
    occurrence: int
    formation: int
    close: int
    commit: int
    archive_syndrome: Word
    framework_Record: None = None
    realized_history: None = None
    Born_probability: None = None
    physical_time: None = None


def one_hot(label: int, width: int) -> Word:
    if label not in range(width):
        raise ValueError("one-hot label leaves its declared carrier")
    return tuple(int(index == label) for index in range(width))


def singleton(bits: Word, width: int, name: str) -> int:
    if len(bits) != width or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError(f"{name} leaves its binary carrier")
    if sum(bits) != 1:
        raise ValueError(f"{name} is not one-hot")
    return bits.index(1)


def program_bits(program: int) -> Word:
    if program not in range(7):
        raise ValueError("program leaves accepted Cycle565 labels")
    return tuple((program >> bit) & 1 for bit in range(3))


def program_of(bits: Word) -> int:
    return sum(bits[site] << lane for lane, site in enumerate(PROGRAM_BITS))


def size_word(size: int) -> Word:
    if size not in (5, 6):
        raise ValueError("size must be train L5 or held L6")
    return (int(size == 5), int(size == 6))


def threshold_member(program: int, seed: int) -> int:
    """Fixed unary comparator table; its thresholds are supplied law data."""
    if program not in range(7) or seed not in range(12):
        raise ValueError("threshold input leaves the finite table")
    if program in (0, 1):
        return min(seed // 4, 2)
    if program in (2, 3, 4):
        return int(seed >= 6)
    if program == 5:
        return min(seed // 4, 2)
    # Program 6 refines the middle program-5 bin into labels 1 and 2.
    return 0 if seed < 4 else 1 if seed < 6 else 2 if seed < 8 else 3


def semantic_route_member(route: str, program: int, source_index: int) -> int:
    if route not in WIDTHS:
        raise ValueError("unknown route")
    selected = threshold_member(program, source_index) if route == "C" else source_index
    c565.validate_interface_member(program, selected)
    return selected


def mk_gate(kind: str, sites: tuple[int, ...], label: str, width: int) -> Gate:
    return c505.gate(kind, sites, label, width)


def decode_schedule(width: int) -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for program in range(7):
        target = program_bits(program)
        for lane, bit in enumerate(target):
            if bit == 0:
                gates.append(mk_gate("X", (PROGRAM_BITS[lane],), f"decode:{program}:open:{lane}", width))
        gates.extend((
            mk_gate("TOFFOLI", (PROGRAM_BITS[0], PROGRAM_BITS[1], PROGRAM_WORK), f"decode:{program}:pair", width),
            mk_gate("TOFFOLI", (PROGRAM_WORK, PROGRAM_BITS[2], PROGRAM_ONEHOT[program]), f"decode:{program}:rail", width),
            mk_gate("TOFFOLI", (PROGRAM_BITS[0], PROGRAM_BITS[1], PROGRAM_WORK), f"decode:{program}:unpair", width),
        ))
        for lane, bit in reversed(tuple(enumerate(target))):
            if bit == 0:
                gates.append(mk_gate("X", (PROGRAM_BITS[lane],), f"decode:{program}:close:{lane}", width))
    return tuple(gates)


def swap_schedule(left: int, right: int, prefix: str, width: int) -> tuple[Gate, ...]:
    return (
        mk_gate("CNOT", (left, right), f"{prefix}:a", width),
        mk_gate("CNOT", (right, left), f"{prefix}:b", width),
        mk_gate("CNOT", (left, right), f"{prefix}:c", width),
    )


def controlled_swap(control: int, left: int, right: int, prefix: str, width: int) -> tuple[Gate, ...]:
    return (
        mk_gate("CNOT", (right, left), f"{prefix}:pre", width),
        mk_gate("TOFFOLI", (control, left, right), f"{prefix}:move", width),
        mk_gate("CNOT", (right, left), f"{prefix}:post", width),
    )


def route_generation_schedule(route: str) -> tuple[Gate, ...]:
    width = WIDTHS[route]
    gates: list[Gate] = []
    if route == "A":
        for label in range(5):
            for target, name in (
                (c552.MEMBER_STATE[label], "member-state"),
                (A_ENV_MEMBER[label], "environment-member"),
                (A_ENV_RECEIPT[label], "environment-receipt"),
                (A_ENV_REDUNDANCY[0][label], "environment-copy-0"),
                (A_ENV_REDUNDANCY[1][label], "environment-copy-1"),
            ):
                gates.append(mk_gate("CNOT", (A_SYSTEM[label], target), f"A:{name}:{label}", width))
        for law in range(5):
            gates.append(mk_gate("CNOT", (A_LAW_SOURCE[law], c552.LAW_WORD[law]), f"A:law:{law}", width))
    elif route == "B":
        for label in range(5):
            gates.extend(swap_schedule(B_INNOVATION[label], c552.MEMBER_STATE[label], f"B:innovation-transfer:{label}", width))
        for law in range(5):
            gates.extend(swap_schedule(B_LAW_IN[law], c552.LAW_WORD[law], f"B:law-transfer:{law}", width))
        for label in range(5):
            gates.extend(controlled_swap(
                c552.MEMBER_STATE[label], B_READY[label], B_CORRELATION_SINK[label],
                f"B:correlation-sink:{label}", width,
            ))
    elif route == "C":
        for program, seed in product(range(7), range(12)):
            selected = threshold_member(program, seed)
            controls = (PROGRAM_ONEHOT[program], C_SEED[seed])
            gates.extend((
                mk_gate("TOFFOLI", (*controls, c552.MEMBER_STATE[selected]), f"C:threshold-member:{program}:{seed}", width),
                mk_gate("TOFFOLI", (*controls, C_HIDDEN_LABEL[selected]), f"C:threshold-retained:{program}:{seed}", width),
            ))
        for law in range(5):
            gates.append(mk_gate("CNOT", (C_LAW_SOURCE[law], c552.LAW_WORD[law]), f"C:law:{law}", width))
    else:
        raise ValueError("unknown route")
    return tuple(gates)


def candidate_schedule(route: str) -> tuple[Gate, ...]:
    width = WIDTHS[route]
    label_sites = ROUTE_LABELS[route]
    occurrence = c552.SNAPSHOT[0][1]
    gates: list[Gate] = [
        mk_gate("TOFFOLI", (occurrence, FORMATION_READY, FORMATION), "candidate:formation", width),
        mk_gate("TOFFOLI", (FORMATION, CLOSE_READY, CLOSE), "candidate:close", width),
        mk_gate("TOFFOLI", (CLOSE, CAPACITY_READY, COMMIT), "candidate:commit", width),
    ]
    for field, source in enumerate(c552.SNAPSHOT[0][:12]):
        gates.append(mk_gate("TOFFOLI", (COMMIT, source, ARCHIVE_FIELDS[field]), f"candidate:field:{field}", width))
    for copy in range(3):
        for label in range(5):
            gates.append(mk_gate("TOFFOLI", (COMMIT, label_sites[label], ARCHIVE_MEMBER[copy][label]), f"candidate:member:{copy}:{label}", width))
            gates.append(mk_gate("TOFFOLI", (COMMIT, c552.LAW_WORD[label], ARCHIVE_LAW[copy][label]), f"candidate:law:{copy}:{label}", width))
    for program in range(7):
        gates.append(mk_gate("TOFFOLI", (COMMIT, PROGRAM_ONEHOT[program], ARCHIVE_PROGRAM[program]), f"candidate:program:{program}", width))
    return tuple(gates)


DECODE = {route: decode_schedule(WIDTHS[route]) for route in WIDTHS}
GENERATION = {route: route_generation_schedule(route) for route in WIDTHS}
CANDIDATE = {route: candidate_schedule(route) for route in WIDTHS}


def apply_outer(bits: Word, schedule: tuple[Gate, ...], *, reverse: bool = False,
                delete_label: str | None = None) -> Word:
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("outer word leaves binary domain")
    if delete_label is not None:
        matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("outer deletion must name one gate")
        schedule = tuple(item for index, item in enumerate(schedule) if index != matches[0])
    word = list(bits)
    for item in (tuple(reversed(schedule)) if reverse else schedule):
        c505.apply_gate(word, item)
    return tuple(word)


def route_prepare(route: str, program: int, source_index: int, law: int, size: int,
                  binding: int, *, edge: int = 1, plus: int = 1, minus: int = 0,
                  K_position: int = 0) -> Word:
    width = WIDTHS.get(route)
    if width is None:
        raise ValueError("unknown route")
    selected = semantic_route_member(route, program, source_index)
    if binding not in range(5) or law not in range(5):
        raise ValueError("binding or law leaves five-label domain")
    base = c531.prepare(
        edge=edge, plus=plus, minus=minus, K_position=K_position,
        binding_label=binding, member_label=None, receipt_label=None,
    )
    bits = list(base) + [0] * (width - c531.TOTAL_M2)
    for site, bit in zip(PROGRAM_BITS, program_bits(program)):
        bits[site] = bit
    for site, bit in zip(SIZE_TAG, size_word(size)):
        bits[site] = bit
    bits[FORMATION_READY] = bits[CLOSE_READY] = bits[CAPACITY_READY] = 1
    bits[c552.OUTPUT_HEAD[0]] = 1
    if route == "A":
        bits[A_SYSTEM[source_index]] = 1
        bits[A_LAW_SOURCE[law]] = 1
    elif route == "B":
        bits[B_INNOVATION[source_index]] = 1
        bits[B_LAW_IN[law]] = 1
        for site in B_READY:
            bits[site] = 1
    else:
        bits[C_SEED[source_index]] = 1
        bits[C_LAW_SOURCE[law]] = 1
    output = tuple(bits)
    validate_initial(output, route)
    assert selected in range(c565.interface_outcome_count(program))
    return output


def validate_initial(bits: Word, route: str) -> None:
    if route not in WIDTHS or len(bits) != WIDTHS[route]:
        raise ValueError("route word has wrong bounded width")
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("route word leaves binary M2 domain")
    program = program_of(bits)
    if program not in range(7):
        raise ValueError("program 7 is outside Cycle565 eligibility")
    singleton(tuple(bits[site] for site in SIZE_TAG), 2, "size tag")
    if any(bits[site] for site in (*PROGRAM_ONEHOT, PROGRAM_WORK)):
        raise ValueError("program decoder target/work is dirty")
    if tuple(bits[site] for site in (FORMATION_READY, CLOSE_READY, CAPACITY_READY)) != (1, 1, 1):
        raise ValueError("formation/close/capacity readiness is not supplied")
    dirty_common = (
        FORMATION, CLOSE, COMMIT, *ARCHIVE_FIELDS,
        *(site for bank in ARCHIVE_MEMBER for site in bank),
        *(site for bank in ARCHIVE_LAW for site in bank), *ARCHIVE_PROGRAM,
    )
    if any(bits[site] for site in dirty_common):
        raise ValueError("commit-candidate target is not blank")
    if any(bits[site] for site in (*c552.LAW_WORD, *c552.MEMBER_STATE, *c552.SNAPSHOT[0])):
        raise ValueError("Cycle552 law/member/snapshot boundary is not blank")
    if tuple(bits[site] for site in c552.OUTPUT_HEAD) != one_hot(0, 5):
        raise ValueError("Cycle552 output head is not at the declared blank slot")
    if route == "A":
        selected = singleton(tuple(bits[site] for site in A_SYSTEM), 5, "A system label")
        singleton(tuple(bits[site] for site in A_LAW_SOURCE), 5, "A law source")
        if any(bits[site] for site in (*A_ENV_MEMBER, *A_ENV_RECEIPT, *(s for bank in A_ENV_REDUNDANCY for s in bank))):
            raise ValueError("A outgoing environment is dirty")
    elif route == "B":
        selected = singleton(tuple(bits[site] for site in B_INNOVATION), 5, "B innovation")
        singleton(tuple(bits[site] for site in B_LAW_IN), 5, "B law token")
        if tuple(bits[site] for site in B_READY) != (1, 1, 1, 1, 1) or any(bits[site] for site in B_CORRELATION_SINK):
            raise ValueError("B ready/correlation resource boundary is malformed")
    else:
        seed = singleton(tuple(bits[site] for site in C_SEED), 12, "C unary seed")
        singleton(tuple(bits[site] for site in C_LAW_SOURCE), 5, "C law source")
        if any(bits[site] for site in C_HIDDEN_LABEL):
            raise ValueError("C hidden-label target is dirty")
        selected = threshold_member(program, seed)
    c565.validate_interface_member(program, selected)


def generated_word(bits: Word, route: str) -> Word:
    decoded = apply_outer(bits, DECODE[route])
    program = program_of(decoded)
    if tuple(decoded[site] for site in PROGRAM_ONEHOT) != one_hot(program, 7) or decoded[PROGRAM_WORK]:
        raise ValueError("program decoder failed its local constraint")
    generated = apply_outer(decoded, GENERATION[route])
    c552.validate_law_code(tuple(generated[:c552.TOTAL_M2]))
    return generated


def physical_route_step(bits: Word, route: str, *, outer_delete: str | None = None,
                        inner_delete: str | None = None) -> Word:
    validate_initial(bits, route)
    decoded = apply_outer(bits, DECODE[route], delete_label=outer_delete if outer_delete and outer_delete.startswith("decode:") else None)
    generated = apply_outer(decoded, GENERATION[route], delete_label=outer_delete if outer_delete and outer_delete.startswith(f"{route}:") else None)
    base = tuple(generated[:c552.TOTAL_M2])
    if inner_delete is None:
        c552.validate_law_code(base)
        advanced = c552.physical_step(base)
    else:
        advanced = c552.apply_schedule(base, delete_label=inner_delete)
    word = tuple(advanced) + tuple(generated[c552.TOTAL_M2:])
    candidate_delete = outer_delete if outer_delete and outer_delete.startswith("candidate:") else None
    return apply_outer(word, CANDIDATE[route], delete_label=candidate_delete)


def reverse_route_step(bits: Word, route: str) -> Word:
    if len(bits) != WIDTHS[route]:
        raise ValueError("route inverse width mismatch")
    word = apply_outer(bits, CANDIDATE[route], reverse=True)
    base = c552.apply_schedule(tuple(word[:c552.TOTAL_M2]), reverse=True)
    word = tuple(base) + tuple(word[c552.TOTAL_M2:])
    word = apply_outer(word, GENERATION[route], reverse=True)
    word = apply_outer(word, DECODE[route], reverse=True)
    return word


def direct_expected(bits: Word, route: str) -> Word:
    """Independent semantic G_coarse followed by the explicit basis encoder E."""
    validate_initial(bits, route)
    program = program_of(bits)
    size = 5 if bits[SIZE_TAG[0]] else 6
    law = (
        singleton(tuple(bits[site] for site in A_LAW_SOURCE), 5, "A law") if route == "A"
        else singleton(tuple(bits[site] for site in B_LAW_IN), 5, "B law") if route == "B"
        else singleton(tuple(bits[site] for site in C_LAW_SOURCE), 5, "C law")
    )
    source_index = (
        singleton(tuple(bits[site] for site in A_SYSTEM), 5, "A source") if route == "A"
        else singleton(tuple(bits[site] for site in B_INNOVATION), 5, "B source") if route == "B"
        else singleton(tuple(bits[site] for site in C_SEED), 12, "C source")
    )
    selected = semantic_route_member(route, program, source_index)
    expected = list(bits)
    for site, bit in zip(PROGRAM_ONEHOT, one_hot(program, 7)):
        expected[site] = bit
    if route == "A":
        for sites in (c552.MEMBER_STATE, A_ENV_MEMBER, A_ENV_RECEIPT, *A_ENV_REDUNDANCY):
            for site, bit in zip(sites, one_hot(selected, 5)):
                expected[site] = bit
        for site, bit in zip(c552.LAW_WORD, one_hot(law, 5)):
            expected[site] = bit
    elif route == "B":
        for site in (*B_INNOVATION, *B_LAW_IN):
            expected[site] = 0
        for site, bit in zip(c552.MEMBER_STATE, one_hot(selected, 5)):
            expected[site] = bit
        for site, bit in zip(c552.LAW_WORD, one_hot(law, 5)):
            expected[site] = bit
        expected[B_READY[selected]] = 0
        expected[B_CORRELATION_SINK[selected]] = 1
    else:
        for sites in (c552.MEMBER_STATE, C_HIDDEN_LABEL):
            for site, bit in zip(sites, one_hot(selected, 5)):
                expected[site] = bit
        for site, bit in zip(c552.LAW_WORD, one_hot(law, 5)):
            expected[site] = bit

    binding = c505.c_view(tuple(expected[c531.C505_OFFSET:c531.C505_OFFSET + c531.C505_WIDTH])).eligibility.index(1)
    edge = expected[c531.C526_EDGE]
    plus, minus = (expected[site] for site in c531.C526_CURRENT)
    Kword = tuple(expected[site] for site in c531.C526_K)
    K_position = Kword.index(1)
    exact531 = c531.logical_apply(c531.prepare(
        edge=edge, plus=plus, minus=minus, K_position=K_position,
        binding_label=binding, member_label=selected, receipt_label=selected,
    ))
    fields = tuple(exact531[site] for site in c552.C531_OUTPUT_FIELDS)
    for site in c552.MEMBER_STATE:
        expected[site] = 0
    for site, bit in zip(c552.MEMBER_STATE, one_hot((selected + law) % 5, 5)):
        expected[site] = bit
    for site in c552.OUTPUT_HEAD:
        expected[site] = 0
    expected[c552.OUTPUT_HEAD[1]] = 1
    for site, bit in zip(c552.SNAPSHOT[0][:12], fields):
        expected[site] = bit
    for site, bit in zip(c552.SNAPSHOT[0][12:], one_hot(law, 5)):
        expected[site] = bit

    occurrence = fields[1]
    formation = occurrence & expected[FORMATION_READY]
    close = formation & expected[CLOSE_READY]
    commit = close & expected[CAPACITY_READY]
    expected[FORMATION], expected[CLOSE], expected[COMMIT] = formation, close, commit
    for site, bit in zip(ARCHIVE_FIELDS, tuple(commit & bit for bit in fields)):
        expected[site] = bit
    for bank in ARCHIVE_MEMBER:
        for site, bit in zip(bank, tuple(commit & bit for bit in one_hot(selected, 5))):
            expected[site] = bit
    for bank in ARCHIVE_LAW:
        for site, bit in zip(bank, tuple(commit & bit for bit in one_hot(law, 5))):
            expected[site] = bit
    for site, bit in zip(ARCHIVE_PROGRAM, tuple(commit & bit for bit in one_hot(program, 7))):
        expected[site] = bit
    assert size in (5, 6)
    return tuple(expected)


def archive_syndrome(bits: Word) -> Word:
    return tuple(
        (bits[ARCHIVE_MEMBER[0][label]] ^ bits[ARCHIVE_MEMBER[1][label]])
        | (bits[ARCHIVE_MEMBER[1][label]] ^ bits[ARCHIVE_MEMBER[2][label]])
        for label in range(5)
    ) + tuple(
        (bits[ARCHIVE_LAW[0][label]] ^ bits[ARCHIVE_LAW[1][label]])
        | (bits[ARCHIVE_LAW[1][label]] ^ bits[ARCHIVE_LAW[2][label]])
        for label in range(5)
    )


def candidate_view(bits: Word, route: str, source_index: int) -> ProtectedCommitCandidate:
    program = singleton(tuple(bits[site] for site in PROGRAM_ONEHOT), 7, "decoded program")
    selected = singleton(tuple(bits[site] for site in ROUTE_LABELS[route]), 5, "retained member")
    law = singleton(tuple(bits[site] for site in c552.LAW_WORD), 5, "retained law")
    size = 5 if bits[SIZE_TAG[0]] else 6
    return ProtectedCommitCandidate(
        route=route, program=program, size=size, source_index=source_index,
        selected_member=selected, law_shift=law,
        occurrence=bits[c552.SNAPSHOT[0][1]], formation=bits[FORMATION],
        close=bits[CLOSE], commit=bits[COMMIT],
        archive_syndrome=archive_syndrome(bits),
    )


def constructive_square_controls() -> dict[str, object]:
    rows = {}
    global_failures = 0
    for route in WIDTHS:
        cases = eg_failures = inverse_failures = interface_failures = archive_failures = 0
        mismatch_failures = held_failures = 0
        route_rows = []
        for size, program in product((5, 6), range(7)):
            sources = range(12) if route == "C" else range(c565.interface_outcome_count(program))
            for source_index in sources:
                selected = semantic_route_member(route, program, source_index)
                law = (program + source_index + size) % 5
                plus, minus = ((1, 0) if (program + source_index) % 2 == 0 else (0, 1))
                source = route_prepare(
                    route, program, source_index, law, size, selected,
                    plus=plus, minus=minus, K_position=(program + 3 * source_index + size) % 16,
                )
                output = physical_route_step(source, route)
                expected = direct_expected(source, route)
                eg_failures += int(output != expected)
                inverse_failures += int(reverse_route_step(output, route) != source)
                snapshot, law_snapshot = c552.snapshot_view(tuple(output[:c552.TOTAL_M2]), 0)
                exact531 = c531.logical_apply(c531.prepare(
                    edge=1, plus=plus, minus=minus,
                    K_position=(program + 3 * source_index + size) % 16,
                    binding_label=selected, member_label=selected, receipt_label=selected,
                ))
                interface_failures += int(snapshot != tuple(exact531[site] for site in c552.C531_OUTPUT_FIELDS))
                interface_failures += int(law_snapshot != one_hot(law, 5))
                view = candidate_view(output, route, source_index)
                archive_failures += int(
                    (view.occurrence, view.formation, view.close, view.commit) != (1, 1, 1, 1)
                    or any(view.archive_syndrome)
                    or view.framework_Record is not None
                )
                cases += 1
            # One mismatching binder row per program/size is required.
            source_index = 0
            selected = semantic_route_member(route, program, source_index)
            mismatch = route_prepare(
                route, program, source_index, program % 5, size, (selected + 1) % 5,
                K_position=(program + size) % 16,
            )
            mismatch_output = physical_route_step(mismatch, route)
            mismatch_failures += int(
                mismatch_output[c552.SNAPSHOT[0][0]] != 1
                or any(mismatch_output[site] for site in (c552.SNAPSHOT[0][1], c552.SNAPSHOT[0][2], FORMATION, CLOSE, COMMIT))
                or any(mismatch_output[site] for site in (*ARCHIVE_FIELDS, *(s for b in ARCHIVE_MEMBER for s in b)))
            )
        # Same physical schedules at train L5 and held L6; only the explicit
        # scalar size tag differs.
        held_failures += int(WIDTHS[route] != len(route_prepare(route, 0, 0, 0, 5, 0)))
        held_failures += int(WIDTHS[route] != len(route_prepare(route, 1, 0, 0, 6, 0)))
        route_rows.append({
            "cases": cases, "EG_failures": eg_failures, "inverse_failures": inverse_failures,
            "interface_failures": interface_failures, "archive_failures": archive_failures,
            "mismatch_failures": mismatch_failures, "held_failures": held_failures,
        })
        rows[route] = route_rows[0]
        global_failures += sum(route_rows[0][key] for key in route_rows[0] if key != "cases")
    check(
        "all three physical sources satisfy the exact E G square, unchanged Cycle552/531 composition, inverse, and protected commit-candidate diagnostics",
        global_failures == 0,
        rows,
    )
    return {"routes": rows, "failures": global_failures, "pass": global_failures == 0}


def route_a_controls() -> dict[str, object]:
    codewords = np.eye(5, dtype=int)
    environment_Gram = codewords @ codewords.T
    source = route_prepare("A", 1, 2, 3, 6, 2, K_position=11)
    output = physical_route_step(source, "A")
    environment_words = tuple(
        tuple(output[site] for site in bank)
        for bank in (A_ENV_MEMBER, A_ENV_RECEIPT, *A_ENV_REDUNDANCY)
    )
    # A continuation may alter the live system carrier while all outgoing
    # environment and archive M2 remain outside its gate support.
    continuation = list(output)
    for left, right in ((3, 4), (2, 3), (1, 2), (0, 1)):
        continuation = list(apply_outer(tuple(continuation), swap_schedule(A_SYSTEM[left], A_SYSTEM[right], f"A:continuation:{left}:{right}", A_WIDTH)))
    stable_sites = (*A_ENV_MEMBER, *A_ENV_RECEIPT, *(s for b in A_ENV_REDUNDANCY for s in b),
                    *ARCHIVE_FIELDS, *(s for b in ARCHIVE_MEMBER for s in b), *(s for b in ARCHIVE_LAW for s in b))
    stable = all(continuation[site] == output[site] for site in stable_sites)
    deleted = apply_outer(apply_outer(source, DECODE["A"]), GENERATION["A"], delete_label="A:environment-receipt:2")
    deletion_visible = tuple(deleted[site] for site in A_ENV_RECEIPT) != one_hot(2, 5)
    result = {
        "outgoing_environment_words": environment_words,
        "orthogonal_environment_Gram_residual": float(np.max(abs(environment_Gram - np.eye(5)))),
        "coherent_input_terminal_type": "correlated superposition retaining all five sectors; no one objective member inferred",
        "live_carrier_continuation_environment_and_archive_stable": stable,
        "retention_sink_banks": 4,
        "deleted_receipt_visible": deletion_visible,
        "actuality_owner": "not supplied for a coherent input; basis-sector label is supplied preparation",
        "framework_Record": None,
    }
    check(
        "Route A makes four orthogonal retained environment carriers and an exact typed basis-sector interface without claiming decoherence selects one member",
        result["orthogonal_environment_Gram_residual"] == 0.0
        and len(set(environment_words)) == 1 and environment_words[0] == one_hot(2, 5)
        and stable and deletion_visible and result["framework_Record"] is None,
        result,
    )
    return result


def route_b_controls() -> dict[str, object]:
    rows = []
    failures = 0
    for program in range(7):
        for selected in range(c565.interface_outcome_count(program)):
            source = route_prepare("B", program, selected, (program + 2) % 5, 5, selected, K_position=program)
            initial_tokens = sum(source[site] for site in (*B_INNOVATION, *B_LAW_IN, *B_READY, *B_CORRELATION_SINK, *c552.MEMBER_STATE, *c552.LAW_WORD))
            generated = generated_word(source, "B")
            generated_tokens = sum(generated[site] for site in (*B_INNOVATION, *B_LAW_IN, *B_READY, *B_CORRELATION_SINK, *c552.MEMBER_STATE, *c552.LAW_WORD))
            output = physical_route_step(source, "B")
            final_tokens = sum(output[site] for site in (*B_INNOVATION, *B_LAW_IN, *B_READY, *B_CORRELATION_SINK, *c552.MEMBER_STATE, *c552.LAW_WORD))
            sink = tuple(output[site] for site in B_CORRELATION_SINK)
            archived = tuple(output[site] for site in ARCHIVE_MEMBER[0])
            failures += int(initial_tokens != generated_tokens or generated_tokens != final_tokens or final_tokens != 7)
            failures += int(sink != one_hot(selected, 5) or archived != sink)
            rows.append((program, selected, initial_tokens, final_tokens))
    source = route_prepare("B", 6, 3, 4, 6, 3, K_position=15)
    decoded = apply_outer(source, DECODE["B"])
    damaged = apply_outer(decoded, GENERATION["B"], delete_label="B:correlation-sink:3:move")
    deletion_residual = sum(left != right for left, right in zip(damaged, generated_word(source, "B")))
    result = {
        "rows": len(rows), "ledger_failures": failures,
        "conserved_token_total": 7,
        "ledger": "innovation 1 + law 1 + five ready tokens -> MEMBER_STATE 1 + law word 1 + four ready + one retained correlation sink",
        "sink_equals_pre-update_member_failures": failures,
        "correlation_gate_deletion_bit_residual": deletion_residual,
        "actuality_owner": "supplied one-hot objective innovation-carrier ontology and incoming token",
        "distribution_or_frequency_law": None,
        "resource_is_energy": False,
        "framework_Record": None,
    }
    check(
        "Route B transfers one supplied objective innovation token into the exact member port with a conserved seven-token resource/correlation ledger",
        failures == 0 and deletion_residual > 0 and result["distribution_or_frequency_law"] is None
        and not result["resource_is_energy"] and result["framework_Record"] is None,
        result,
    )
    return result


def route_c_controls() -> dict[str, object]:
    table = tuple(tuple(threshold_member(program, seed) for seed in range(12)) for program in range(7))
    digest = sha256(json.dumps(table).encode()).hexdigest()
    source = route_prepare("C", 6, 7, 2, 6, threshold_member(6, 7), K_position=9)
    output = physical_route_step(source, "C")
    seed_retained = tuple(output[site] for site in C_SEED) == one_hot(7, 12)
    hidden = tuple(output[site] for site in C_HIDDEN_LABEL)
    refinement_failures = 0
    coarse = {0: 0, 1: 1, 2: 1, 3: 2}
    for seed in range(12):
        refinement_failures += int(coarse[threshold_member(6, seed)] != threshold_member(5, seed))
    context_table_failures = int(table[0] != table[1])
    decomposition_table_failures = sum(int(table[index] != table[2]) for index in (3, 4))
    decoded = apply_outer(source, DECODE["C"])
    delete_label = f"C:threshold-member:6:7"
    damaged = apply_outer(decoded, GENERATION["C"], delete_label=delete_label)
    deletion_visible = tuple(damaged[site] for site in c552.MEMBER_STATE) != one_hot(threshold_member(6, 7), 5)
    result = {
        "threshold_table": table,
        "threshold_table_SHA256": digest,
        "unary_seed_M2": 12,
        "seed_retained": seed_retained,
        "hidden_label": hidden,
        "program5_to_program6_refinement_failures": refinement_failures,
        "program0_1_context_table_failures": context_table_failures,
        "program2_3_4_decomposition_table_failures": decomposition_table_failures,
        "threshold_gate_deletion_visible": deletion_visible,
        "supplied_seed_structure": "one of twelve unary seed rails, a seven-program threshold ROM, one law source, and their ontic interpretation",
        "frequency_bridge_claimed": False,
        "framework_Record": None,
    }
    check(
        "Route C compiles a fixed deterministic threshold ROM, retains the unary seed, and preserves the Cycle565 5-to-6 refinement quotient",
        seed_retained and hidden == one_hot(2, 5) and refinement_failures == 0
        and context_table_failures == 0 and decomposition_table_failures == 0
        and deletion_visible and not result["frequency_bridge_claimed"] and result["framework_Record"] is None,
        result,
    )
    return result


def stage_permanence_controls() -> dict[str, object]:
    source = route_prepare("B", 5, 2, 1, 6, 2, K_position=13)
    full = physical_route_step(source, "B")
    rows = {}
    for label in ("candidate:formation", "candidate:close", "candidate:commit", "candidate:member:1:2"):
        damaged = physical_route_step(source, "B", outer_delete=label)
        rows[label] = {
            "formation": damaged[FORMATION], "close": damaged[CLOSE], "commit": damaged[COMMIT],
            "archive_syndrome": archive_syndrome(damaged),
            "basis_residual": float(np.sqrt(sum(left != right for left, right in zip(full, damaged)))),
        }
    continued_base = c552.physical_step(tuple(full[:c552.TOTAL_M2]))
    continued = tuple(continued_base) + tuple(full[c552.TOTAL_M2:])
    protected_sites = (
        *ARCHIVE_FIELDS, *(s for b in ARCHIVE_MEMBER for s in b),
        *(s for b in ARCHIVE_LAW for s in b), *ARCHIVE_PROGRAM,
    )
    continuation_stable = all(continued[site] == full[site] for site in protected_sites)
    faulted = list(full)
    faulted[ARCHIVE_MEMBER[1][2]] ^= 1
    fault_syndrome = archive_syndrome(tuple(faulted))
    result = {
        "deletions": rows,
        "second_Cycle552_recurrence_leaves_candidate_packet_unchanged": continuation_stable,
        "single_archive_fault_syndrome": fault_syndrome,
        "formation_close_commit_are_reversible_diagnostics": True,
        "permanence_scope": "unchanged under the declared disjoint continuation plus triplicate fault detection; not irreversible or unbounded permanence",
        "packet_is_framework_Record": False,
        "pointer_copying_is_Record": False,
    }
    check(
        "formation, close, commit, protected payload, deletion, continuation, and fault diagnostics are executable without promoting the packet to Record",
        rows["candidate:formation"]["commit"] == 0
        and rows["candidate:close"]["formation"] == 1 and rows["candidate:close"]["commit"] == 0
        and rows["candidate:commit"]["close"] == 1 and rows["candidate:commit"]["commit"] == 0
        and any(rows["candidate:member:1:2"]["archive_syndrome"])
        and all(row["basis_residual"] > 0 for row in rows.values())
        and continuation_stable and any(fault_syndrome)
        and not result["packet_is_framework_Record"] and not result["pointer_copying_is_Record"],
        result,
    )
    return result


def algebraic_and_port_firewall_controls() -> dict[str, object]:
    supplied_grade_a = (0.51, 0.31, 0.18, 0.0, 0.0)
    supplied_grade_b = (0.07, 0.13, 0.29, 0.23, 0.28)
    source = route_prepare("C", 0, 9, 4, 5, threshold_member(0, 9), K_position=6)
    output_a = physical_route_step(source, "C")
    output_b = physical_route_step(source, "C")
    forbidden = ("grade", "weight", "norm", "diagonal", "probability", "sampler")
    functions = (route_prepare, physical_route_step, semantic_route_member, c552.prepare, c552.physical_step, c531.logical_apply)
    hits = {}
    for function in functions:
        tree = ast.parse(inspect.getsource(function))
        args = tuple(
            argument.arg.lower()
            for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            for argument in (*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs)
        )
        hits[function.__name__] = {token: sum(name == token for name in args) for token in forbidden}
    result = {
        "supplied_algebraic_grades_differ": supplied_grade_a != supplied_grade_b,
        "same_physical_output": output_a == output_b,
        "selected_member": candidate_view(output_a, "C", 9).selected_member,
        "prepare_step_member_port_forbidden_name_hits": hits,
        "algebraic_grade_selects_member": False,
    }
    check(
        "independently supplied algebraic grades do not enter any prepare/step/member port and do not select the member",
        result["supplied_algebraic_grades_differ"] and result["same_physical_output"]
        and all(value == 0 for row in hits.values() for value in row.values())
        and not result["algebraic_grade_selects_member"],
        result,
    )
    return result


def domain_and_leakage_controls() -> dict[str, object]:
    refusals = []

    def refused(name: str, thunk) -> None:
        try:
            thunk()
        except (ValueError, IndexError):
            refusals.append(name)

    refused("program7", lambda: route_prepare("A", 7, 0, 0, 5, 0))
    refused("out-of-menu member", lambda: route_prepare("A", 2, 2, 0, 5, 0))
    refused("bad size", lambda: route_prepare("A", 0, 0, 0, 7, 0))
    refused("bad law", lambda: route_prepare("A", 0, 0, 5, 5, 0))
    refused("bad binding", lambda: route_prepare("A", 0, 0, 0, 5, 5))
    for route, sites, name in (
        ("A", A_SYSTEM, "A zero-hot"), ("B", B_INNOVATION, "B zero-hot"),
        ("C", C_SEED, "C zero-hot"),
    ):
        source = list(route_prepare(route, 0, 0, 0, 5, 0))
        for site in sites:
            source[site] = 0
        refused(name, lambda source=tuple(source), route=route: validate_initial(source, route))
    for route, sites, name in (
        ("A", A_SYSTEM, "A multi-hot"), ("B", B_INNOVATION, "B multi-hot"),
        ("C", C_SEED, "C multi-hot"),
    ):
        source = list(route_prepare(route, 0, 0, 0, 5, 0))
        source[sites[1]] = 1
        refused(name, lambda source=tuple(source), route=route: validate_initial(source, route))
    dirty_archive = list(route_prepare("A", 0, 0, 0, 5, 0))
    dirty_archive[ARCHIVE_FIELDS[0]] = 1
    refused("dirty archive", lambda: validate_initial(tuple(dirty_archive), "A"))
    dirty_sink = list(route_prepare("B", 0, 0, 0, 5, 0))
    dirty_sink[B_CORRELATION_SINK[0]] = 1
    refused("dirty B sink", lambda: validate_initial(tuple(dirty_sink), "B"))
    dirty_program = list(route_prepare("C", 0, 0, 0, 5, 0))
    dirty_program[PROGRAM_ONEHOT[0]] = 1
    refused("dirty program decoder", lambda: validate_initial(tuple(dirty_program), "C"))
    nonbinary = list(route_prepare("C", 0, 0, 0, 5, 0))
    nonbinary[C_SEED[0]] = 2
    refused("nonbinary seed", lambda: validate_initial(tuple(nonbinary), "C"))

    leakage_failures = 0
    for route, program, source_index in (("A", 1, 2), ("B", 4, 1), ("C", 6, 10)):
        selected = semantic_route_member(route, program, source_index)
        source = route_prepare(route, program, source_index, 3, 6, selected, K_position=14)
        output = physical_route_step(source, route)
        restored = reverse_route_step(output, route)
        leakage_failures += int(restored != source)
        leakage_failures += int(any(output[site] for site in (c531.WORK_BINDING, c531.WORK_PROVENANCE, c531.WORK_TRIGGER, PROGRAM_WORK)))
    result = {
        "malformed_refusals": tuple(refusals), "refusal_count": len(refusals),
        "terminal_work_or_inverse_leakage_failures": leakage_failures,
        "off_code_coercions": 0,
    }
    check(
        "all source, program, seed, sink, archive, and binary domains reject malformed words and lawful inverses have zero terminal leakage",
        len(refusals) == 15 and leakage_failures == 0 and result["off_code_coercions"] == 0,
        result,
    )
    return result


def frame_outer(bits: Word, route: str, axis: int, frame: np.ndarray) -> tuple[Word, int]:
    base, new_axis = c552.frame_word(tuple(bits[:c552.TOTAL_M2]), axis, frame)
    output = list(bits)
    output[:c552.TOTAL_M2] = base
    plus_field = c552.C531_OUTPUT_FIELDS.index(c531.PAYLOAD_CURRENT[0])
    minus_field = c552.C531_OUTPUT_FIELDS.index(c531.PAYLOAD_CURRENT[1])
    pair = (bits[ARCHIVE_FIELDS[plus_field]], bits[ARCHIVE_FIELDS[minus_field]])
    _axis, mapped = c552.frame_current(axis, pair, frame)
    output[ARCHIVE_FIELDS[plus_field]], output[ARCHIVE_FIELDS[minus_field]] = mapped
    return tuple(output), new_axis


def covariance_controls() -> dict[str, object]:
    frames = c531.c526.c235.proper_cubic_frames()
    failures = tests = 0
    for route, size, program, frame in product(WIDTHS, (5, 6), range(7), frames):
        source_index = (program + size) % (12 if route == "C" else c565.interface_outcome_count(program))
        selected = semantic_route_member(route, program, source_index)
        source = route_prepare(route, program, source_index, (program + 1) % 5, size, selected, K_position=(program + size) % 16)
        output = physical_route_step(source, route)
        framed_source, framed_axis = frame_outer(source, route, 0, frame)
        framed_output = physical_route_step(framed_source, route)
        expected, expected_axis = frame_outer(output, route, 0, frame)
        failures += int(framed_output != expected or framed_axis != expected_axis)
        tests += 1
    group_failures = group_tests = 0
    for first, second, axis, rails in product(frames, frames, range(3), ((0, 0), (1, 0), (0, 1), (1, 1))):
        middle_axis, middle = c552.frame_current(axis, rails, second)
        final_axis, final = c552.frame_current(middle_axis, middle, first)
        direct_axis, direct = c552.frame_current(axis, rails, first @ second)
        group_failures += int((final_axis, final) != (direct_axis, direct))
        group_tests += 1
    mapped_line_failures = 0
    for frame, width in product(frames, WIDTHS.values()):
        points = [frame @ np.asarray((site, 0, 0), dtype=int) for site in range(width)]
        mapped_line_failures += sum(int(np.abs(right - left).sum() != 1) for left, right in zip(points, points[1:]))
    result = {
        "proper_cubic_frames": len(frames), "train_held_route_program_frame_tests": tests,
        "covariance_failures": failures, "ordered_frame_products": len(frames) ** 2,
        "frame_role_tests": group_tests, "frame_group_failures": group_failures,
        "mapped_line_edge_failures": mapped_line_failures,
        "member_law_program_seed_stage_archive_action": "scalar",
        "source_snapshot_archive_current_action": "oriented endpoint rails",
    }
    check(
        "all three routes commute with all24 proper-cubic frames and the current/archive role obeys all576 frame products",
        len(frames) == 24 and failures == 0 and group_failures == 0 and mapped_line_failures == 0,
        result,
    )
    return result


def literal_expansion_sites(item: Gate) -> tuple[tuple[str, tuple[int, ...]], ...]:
    if item.kind in ("X", "CNOT"):
        return ((item.kind, item.sites),)
    first, second, target = item.sites
    return (
        ("H", (target,)), ("CNOT", (second, target)), ("Tdg", (target,)),
        ("CNOT", (first, target)), ("T", (target,)), ("CNOT", (second, target)),
        ("Tdg", (target,)), ("CNOT", (first, target)), ("T", (second,)),
        ("T", (target,)), ("H", (target,)), ("CNOT", (first, second)),
        ("T", (first,)), ("Tdg", (second,)), ("CNOT", (first, second)),
    )


def locality_and_resource_controls() -> dict[str, object]:
    rows = {}
    toffoli = c552.c523.bare_toffoli_controls()
    for route, width in WIDTHS.items():
        logical = DECODE[route] + GENERATION[route] + CANDIDATE[route]
        literal = tuple((kind, sites, item.label) for item in logical for kind, sites in literal_expansion_sites(item))
        routing_swaps = nn_calls = route_failures = restoration_failures = 0
        digest = sha256()
        for kind, sites, label in literal:
            digest.update(f"{kind}:{sites}:{label}".encode())
            if len(sites) == 1:
                nn_calls += 1
                continue
            first, second = sites
            route_path = c552.line_route(first, second)
            routing_swaps += 2 * len(route_path)
            nn_calls += 1 + 6 * len(route_path)
            route_failures += sum(int(abs(left - right) != 1) for left, right in route_path)
            labels = list(range(width))
            for left, right in route_path:
                labels[left], labels[right] = labels[right], labels[left]
            final_sites = (second - 1, second) if first < second else (second + 1, second)
            restoration_failures += int(tuple(labels[site] for site in final_sites) != (first, second))
            for left, right in reversed(route_path):
                labels[left], labels[right] = labels[right], labels[left]
            restoration_failures += int(labels != list(range(width)))
        rows[route] = {
            "total_M2": width, "new_M2_beyond_Cycle552": width - c552.TOTAL_M2,
            "Cycle565_plus_route_product_envelope_M2": c565.MENU_COMPILER_M2 + width,
            "logical_gates_outside_Cycle552": len(logical),
            "logical_gate_kinds": dict(Counter(item.kind for item in logical)),
            "literal_one_two_M2_gates_outside_Cycle552": len(literal),
            "maximum_literal_support_M2": max(len(sites) for _, sites, _ in literal),
            "forward_reverse_adjacent_SWAPS": routing_swaps,
            "literal_NN_calls": nn_calls, "route_failures": route_failures,
            "operand_or_restoration_failures": restoration_failures,
            "outer_schedule_SHA256": digest.hexdigest(),
        }
    combined = sha256(json.dumps(rows, sort_keys=True).encode()).hexdigest()
    result = {
        "routes": rows, "Cycle552_M2": c552.TOTAL_M2, "Cycle565_menu_compiler_M2": c565.MENU_COMPILER_M2,
        "Cycle523_Toffoli": toffoli, "maximum_physical_support_M2": 2,
        "combined_resource_trace_SHA256": combined,
        "constant_overhead_per_declared_cell": True,
        "unbounded_volume_or_renewal_claimed": False,
    }
    check(
        "every new logical route compiles through the exact Cycle523 identity to one/two-M2 primitives with bounded constant overhead",
        toffoli["pass"] and all(
            row["maximum_literal_support_M2"] == 2 and row["route_failures"] == 0
            and row["operand_or_restoration_failures"] == 0
            for row in rows.values()
        ) and not result["unbounded_volume_or_renewal_claimed"],
        result,
    )
    return result


def no_go_controls() -> dict[str, object]:
    n1 = (
        ("orthogonal retained environment", "system/environment correlation / orthogonal outgoing carriers / one stable typed basis-sector interface", "ATTEMPTED — POSITIVE CONDITIONAL; coherent input retains every sector"),
        ("objective local innovation", "one incoming carrier / conserved transfer and correlation sink / exact member and receipt", "ATTEMPTED — POSITIVE CONDITIONAL on objective-carrier ontology and genesis"),
        ("deterministic hidden threshold", "unary seed plus threshold ROM / reversible comparison / exact member", "ATTEMPTED — POSITIVE CONDITIONAL on seed, table, and ontology"),
        ("periodic hidden carrier", "retained phase / deterministic orbit / actual overlay", "RULED IN BY PRIOR Cycle508 as conditional non-Born comparator"),
        ("objective stochastic field", "local innovation process / law-selected jump / calibrated objective member", "OPEN"),
        ("renewable first passage", "incoming bath carriers / unique retained hit and exhaust / stationary renewal", "OPEN"),
        ("unique extension history", "admissible global continuation / unique member / permanent Record", "OPEN"),
    )
    walls = (
        "autonomous source/seed/bath genesis and renewal",
        "objective actuality law or ontology selection",
        "grade-to-member dynamical coupling",
        "framework Record admission and unbounded permanence",
        "calibrated realized-corpus frequency theorem",
        "translation-invariant noisy volume deployment",
    )
    n2 = tuple((left, right, "no", "no", True) for left, right in combinations(walls, 2))
    n3 = (
        "seven-program label and local binary-to-onehot adapter",
        "L5/L6 tag, one-hot source/law/seed words, and blank Cycle552 boundary",
        "A basis-sector preparation and environment blank capacity",
        "B objective-carrier ontology, incoming token, five ready resources, and law token",
        "C twelve-state unary seed, threshold ROM, hidden-carrier ontology, and law source",
        "formation/close/fresh-capacity readiness and blank protected packet",
        "finite noiseless gates, line chart, tolerance, and proper-cubic frame convention",
    )
    n4 = (
        ("Cycle565", "finite menu compiler stops at supplied member", "new routes emit exact member/law boundary", True),
        ("Cycle552", "recurrence after supplied genesis", "same exact member-state/law input and snapshot", True),
        ("Cycle531", "conditional occurrence after member/receipt", "same exact twelve-field binder output", True),
        ("Cycle508", "hidden carrier positive conditional; stochastic bath open", "B/C conditional actuality and remaining genesis/selection", True),
        ("Cycle433", "protected candidate packet is not admitted Record", "same candidate-versus-Record ceiling", True),
    )
    n5 = (
        ("per source sector", "tested exhaustively on A/B lawful labels and C all 12 seeds", "positive exact"),
        ("per finite program/context", "all seven Cycle565 programs", "positive exact"),
        ("per bounded cell", "A 374, B 364, C 366 M2", "positive exact"),
        ("held size/frame orbit", "L5/L6 and all24/all576", "positive exact"),
        ("coherent actuality / lattice / corpus", "not tested as objective selection", "no negative claim"),
    )
    n6 = (
        "derive a renewable physical innovation source rather than supply B's incoming token",
        "select and test an objective stochastic law without placing algebraic grade on the member port",
        "replace C's supplied unary seed/ROM with a locally generated invariant process",
        "bind the commit candidate to an approved framework formation/admission/protection law",
        "run a preregistered blinded realized corpus only after objective members and Record status exist",
    )
    n7 = (
        "A hostile constructive reviewer should couple the finite menu to a translation-invariant renewable bath whose local first-hit token is the objective innovation owner, whose spent correlations are retained, and whose stationary law is derived independently of the menu grade.  If the resulting exact Cycle552 member stream enters an approved formation/close/commit/protection law and a preregistered held corpus matches a separately derived algebraic functional under context/refinement controls, then the remaining member, Record, and calibration contracts can close without an axiom edit."
    )
    n8 = (
        "Cycles384/565 retired bounded menu registration without universal eligibility",
        "Cycles508/531 retired hidden-carrier and conditional occurrence pieces after supplied actuality",
        "Cycle552 retired autonomous recurrence after supplied genesis",
        "Cycle433 retired a protected candidate packet while preserving the Record-admission boundary",
        "Cycle568 adds concrete environment, innovation, and seed owners but leaves their genesis/law status explicit",
    )
    result = {
        "N1_normalized_routes": n1, "N2_pairwise_walls": n2, "N3_hidden_condition_scan": n3,
        "N4_residual_matching": n4, "N5_rhetoric_resolution": n5,
        "N6_partial_closure_paths": n6, "N7_hostile_steelman": n7, "N8_cross_cycle_echo": n8,
        "supplied": (
            "accepted Cycle565 program/menu code and exact Cycle552/531 interfaces",
            "finite source carriers, law words, seed/table, blank environments and packet capacity",
            "B objective innovation ontology; C hidden seed ontology; A basis-sector preparation",
            "formation/close/capacity readiness, static gates, frame chart, and tolerances",
        ),
        "derived": (
            "three bounded fixed source schedules and exact E G squares",
            "unchanged Cycle552 member/receipt emission and Cycle531 conditional occurrence",
            "A orthogonal four-bank retention, B seven-token conservation, C refinement-compatible threshold ROM",
            "conditional formation/close/commit packet, continuation stability, triplicate fault detection",
            "inverse/leakage/deletion/domain/all24/all576 and literal support-two compiler",
        ),
        "open": (
            "autonomous objective source/seed/bath genesis and renewal",
            "law or evidence selecting B/C ontology and any grade-to-member coupling",
            "approved framework Record admission, irreversible/unbounded permanence, and realized history",
            "Born calibration, independence, blinded realized corpus, and frequency theorem",
            "unbounded noisy cubic tiling, physical time, source/stress/gravity coupling",
        ),
        "broad_no_go": "FAIL / DO NOT SHIP", "minimum_content": False,
        "shared_obstruction": False, "axiom_pressure": False,
        "authority": AUTHORITY, "audit": AUDIT,
        "six_wall_ledger": {
            "C_ref": "member provenance now has three explicit finite physical owners; source ontology/genesis remains supplied",
            "C_num": "exact finite source and packet algebra; no grade-to-member, sampler, calibration, or frequency theorem",
            "C_wrap": "formation/close/commit candidate and one-step continuation diagnostic; no framework Record, realized history, or time",
            "C_int": "unchanged; menu/member plumbing does not identify energy, rate, or interacting dynamics",
            "C_local": "bounded A/B/C compilers, literal support two, all24/all576; volume tiling, renewal, and noise open",
            "C_source": "B has a counted innovation resource but it is not energy/stress/gravity source content",
        },
    }
    check(
        "full N1-N8 keeps three route gains separate from source genesis, Record admission, and calibration and rejects broad no-go/minimum/axiom pressure",
        len(n1) >= 5 and len(n2) == 15 and len(n3) >= 7 and len(n4) >= 5 and len(n5) >= 5
        and len(n6) >= 5 and bool(n7) and len(n8) >= 5
        and result["broad_no_go"].startswith("FAIL") and not result["minimum_content"]
        and not result["shared_obstruction"] and not result["axiom_pressure"]
        and result["authority"] == "none" and result["audit"] == "unset",
        result,
    )
    return result


def main() -> int:
    started = time.monotonic()
    signal.alarm(int(WALL_CAP_SECONDS))
    print("Cycle568 objective-member / protected commit-candidate bridge tournament")
    print("authority none audit unset; pointer copying is not Record; no frequency bridge")

    dependency = dependency_and_note_controls()
    check("accepted Cycle565 and exact Cycle552/531 artifacts plus the Cycle568 note contract are frozen", dependency["pass"], dependency)
    square = constructive_square_controls()
    route_a_controls()
    route_b_controls()
    route_c_controls()
    stage_permanence_controls()
    algebraic_and_port_firewall_controls()
    domain_and_leakage_controls()
    covariance_controls()
    resources = locality_and_resource_controls()
    no_go = no_go_controls()

    elapsed = time.monotonic() - started
    peak = rss_bytes()
    check(
        "runtime/resource cap and final authority/audit/claim firewall hold",
        elapsed < WALL_CAP_SECONDS and peak < RSS_CAP_BYTES and square["pass"]
        and no_go["authority"] == "none" and no_go["audit"] == "unset"
        and not no_go["axiom_pressure"] and resources["maximum_physical_support_M2"] == 2,
        {
            "elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
            "peak_rss_bytes": peak, "rss_cap_bytes": RSS_CAP_BYTES,
            "runner_SHA256": file_sha(Path(__file__)),
            "combined_resource_trace_SHA256": resources["combined_resource_trace_SHA256"],
            "six_wall_ledger": no_go["six_wall_ledger"],
        },
    )
    signal.alarm(0)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
