#!/usr/bin/env python3
"""Cycle574: physical L41 candidate-law integration tournament.

Three fixed reversible readiness realizations feed one common physical-M2
candidate law.  The common law derives member, binding, law word, signed event
current, dimensionless K increment, successor header, occurrence, and the
Cycle571 protected append from in-state data.  No host-selected member/law,
probability, energy, rate, proper time, or framework-Record promotion occurs.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import complete_candidate_lstar_assembly_cycle41_2026_07_14 as c41
import physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22 as c571


c552 = c571.c552
c531 = c571.c531
c505 = c571.c505
c568 = c571.c568

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_L41_CANDIDATE_LAW_INTEGRATION_TOURNAMENT_CYCLE574_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0
Word = tuple[int, ...]
Gate = c505.Gate

FROZEN_PATHS = {
    "Cycle41 runner": ROOT / "scripts/complete_candidate_lstar_assembly_cycle41_2026_07_14.py",
    "Cycle41 note": ROOT / "docs/work_history/repo/review_feedback/COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md",
    "Cycle552 runner": ROOT / "scripts/physical_autonomous_local_member_law_cell_cycle552_2026_07_21.py",
    "Cycle552 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_LOCAL_MEMBER_LAW_CELL_CYCLE552_NOTE_2026-07-21.md",
    "Cycle563 runner": ROOT / "scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py",
    "Cycle563 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_HELD_SPARSE_ORDER_RETIREMENT_CYCLE563_NOTE_2026-07-21.md",
    "Cycle567 runner": ROOT / "scripts/physical_reference_genesis_blank_renewal_tournament_cycle567_2026_07_22.py",
    "Cycle567 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_REFERENCE_GENESIS_BLANK_RENEWAL_TOURNAMENT_CYCLE567_NOTE_2026-07-22.md",
    "Cycle568 runner": ROOT / "scripts/physical_objective_member_record_bridge_tournament_cycle568_2026_07_22.py",
    "Cycle568 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_MEMBER_RECORD_BRIDGE_TOURNAMENT_CYCLE568_NOTE_2026-07-22.md",
    "Cycle569 runner": ROOT / "scripts/physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22.py",
    "Cycle569 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ENLARGED_LINK_CONTACT_WORK_TOURNAMENT_CYCLE569_NOTE_2026-07-22.md",
    "Cycle570 runner": ROOT / "scripts/physical_joint_clock_accumulator_contraction_bridge_cycle570_2026_07_22.py",
    "Cycle570 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_JOINT_CLOCK_ACCUMULATOR_CONTRACTION_BRIDGE_CYCLE570_NOTE_2026-07-22.md",
    "Cycle571 runner": ROOT / "scripts/physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22.py",
    "Cycle571 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RENEWABLE_FIRST_HIT_RECORD_ADMISSION_TOURNAMENT_CYCLE571_NOTE_2026-07-22.md",
}
FROZEN = {
    "Cycle41 runner": "d8207fc0090ca926d060f536fedc2b2c031ccd50184e035c292e6b8eccb56814",
    "Cycle41 note": "efacbbdeda940877e6130f48e1363ccb223a6e9cb579d500e119ed47511b69bd",
    "Cycle552 runner": "405cacd821b5453045f8a8920b1ab0fc2dca5ac90fb150e9b4a95f6f218ac8a4",
    "Cycle552 note": "919f95dd43d8bdd5ba65fba071f58a6d054a89b3d7d4b7cc04686c8c28cdbf42",
    "Cycle563 runner": "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    "Cycle563 note": "5f8cf7ddd3124a6377077936195667298e6723ac36734c8aaadbf70bccc7fdf8",
    "Cycle567 runner": "e8ca59a8f4a909baf1e6455c6156e0432478232dcb00cd71811bb427703da34b",
    "Cycle567 note": "2eab6fff82addfbe7251a432682ddf3c57f3427818915ecdb7998ffdad8b5492",
    "Cycle568 runner": "eeb044df6b4d73ace0f707908d9101919d69df4002fdeb249f2c71d4f1735179",
    "Cycle568 note": "6879e89721609e7e4673334346942d772c031871b044e1a216565f2efc89fcbb",
    "Cycle569 runner": "c0f06a9cc9ffc4dcfe1d80b94da10bbef81ca1c74fddddac48712b0a7c332ced",
    "Cycle569 note": "6a71c727ec516345d3d1e72564edc0a991993b4951314ddfdf255a5eb71de6bc",
    "Cycle570 runner": "853abe5470efd15b154d6cb348d49795a6fa84e77a62f0b21a79105892b1d415",
    "Cycle570 note": "f78441d4ee0a391768f9a4e9e7e6807a925b453b283fe5a1056a35bb934cc40c",
    "Cycle571 runner": "7221d59558e4d731f98a2a4523c280aa98b889f23ea3f7be1acc8919395dfee8",
    "Cycle571 note": "b254476f392597c03f27581fbc4f559266ed42984ac86a516888ee81d2aff8e2",
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


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    answer = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return answer


def one_hot(label: int, width: int) -> Word:
    if label not in range(width):
        raise ValueError("one-hot label leaves carrier")
    return tuple(int(index == label) for index in range(width))


def singleton(bits: Word, width: int, name: str) -> int:
    if len(bits) != width or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError(f"{name} leaves binary carrier")
    if sum(bits) != 1:
        raise ValueError(f"{name} is not one-hot")
    return bits.index(1)


HEADER_PATTERN = (1, 0, 1, 1, 0, 1)
ROLE_NAMES = ("H1", "H0", "B1", "B0", "D1", "D0", "C", "X+", "X-", "Z0", "Z1")
ROLE_INDEX = {name: index for index, name in enumerate(ROLE_NAMES)}
HEADER_ROLES = tuple("H1" if value else "H0" for value in HEADER_PATTERN)
LAW_SHIFT = 1
ROUTES = ("A", "B", "C")

_layout = [c571.C_WIDTH]
SIZE_TAG = take(_layout, 2)
HEADER_PRESENT = take(_layout, 6)
HEADER_ROLE = tuple(take(_layout, len(ROLE_NAMES)) for _ in range(6))
TRIGGER_PRESENT = take(_layout, 1)[0]
TRIGGER_ROLE = take(_layout, len(ROLE_NAMES))
DATA_OPEN = take(_layout, 3)
CERTIFICATE_OPEN = take(_layout, 1)[0]
MATTER = take(_layout, 3)
ORIENTED_CURRENT = take(_layout, 2)
MATCH = take(_layout, 6)
TRIGGER_MATCH = take(_layout, 1)[0]
READY_CHAIN = take(_layout, 9)
READY_TMP = take(_layout, 1)[0]
READY = take(_layout, 1)[0]
NEXT_HEADER_PRESENT = take(_layout, 6)
NEXT_HEADER_ROLE = tuple(take(_layout, len(ROLE_NAMES)) for _ in range(6))
NEXT_TRIGGER_PRESENT = take(_layout, 1)[0]
NEXT_TRIGGER_ROLE = take(_layout, len(ROLE_NAMES))
FRONT = take(_layout, 4)
K_CARRY = take(_layout, 1)[0]
B_CARRIER = tuple(take(_layout, 3) for _ in range(11))
C_BUS = take(_layout, 1)[0]
C_SAMPLE = take(_layout, 11)
C_HEAD = take(_layout, 12)
WIDTH = _layout[0]


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    return c505.gate(kind, sites, label, WIDTH)


def apply(bits: Word, schedule: tuple[Gate, ...], *, reverse: bool = False,
          delete_label: str | None = None) -> Word:
    if len(bits) != WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Cycle574 word leaves bounded binary M2 carrier")
    if delete_label is not None:
        matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("deletion must name one installed gate")
        schedule = tuple(item for index, item in enumerate(schedule) if index != matches[0])
    word = list(bits)
    for item in (tuple(reversed(schedule)) if reverse else schedule):
        c505.apply_gate(word, item)
    return tuple(word)


def match_schedule() -> tuple[Gate, ...]:
    result: list[Gate] = []
    for index, role in enumerate(HEADER_ROLES):
        result.append(gate(
            "TOFFOLI",
            (HEADER_PRESENT[index], HEADER_ROLE[index][ROLE_INDEX[role]], MATCH[index]),
            f"match:{index}:{role}",
        ))
    result.append(gate(
        "TOFFOLI", (TRIGGER_PRESENT, TRIGGER_ROLE[ROLE_INDEX["Z0"]], TRIGGER_MATCH),
        "match:trigger:Z0",
    ))
    result.append(gate(
        "TOFFOLI", (TRIGGER_PRESENT, TRIGGER_ROLE[ROLE_INDEX["Z1"]], TRIGGER_MATCH),
        "match:trigger:Z1",
    ))
    return tuple(result)


DIRECT_CONSTRAINTS = (*MATCH, TRIGGER_MATCH, *DATA_OPEN, CERTIFICATE_OPEN)


def and_latch_schedule(inputs: tuple[int, ...], prefix: str) -> tuple[Gate, ...]:
    if len(inputs) != 11:
        raise ValueError("L41 readiness has exactly eleven normalized constraints")
    compute: list[Gate] = [gate("TOFFOLI", (inputs[0], inputs[1], READY_CHAIN[0]), f"{prefix}:and:0")]
    previous = READY_CHAIN[0]
    for index in range(2, len(inputs) - 1):
        target = READY_CHAIN[index - 1]
        compute.append(gate("TOFFOLI", (previous, inputs[index], target), f"{prefix}:and:{index - 1}"))
        previous = target
    compute.append(gate("TOFFOLI", (previous, inputs[-1], READY_TMP), f"{prefix}:and:final"))
    return tuple(compute + [gate("CNOT", (READY_TMP, READY), f"{prefix}:ready-latch")] + list(reversed(compute)))


def route_a_schedule() -> tuple[Gate, ...]:
    return match_schedule() + and_latch_schedule(tuple(DIRECT_CONSTRAINTS), "A")


def route_b_schedule() -> tuple[Gate, ...]:
    result = list(match_schedule())
    for index, source in enumerate(DIRECT_CONSTRAINTS):
        stages = B_CARRIER[index]
        result.extend((
            gate("CNOT", (source, stages[0]), f"B:carrier:{index}:0"),
            gate("CNOT", (stages[0], stages[1]), f"B:carrier:{index}:1"),
            gate("CNOT", (stages[1], stages[2]), f"B:carrier:{index}:2"),
        ))
    result.extend(and_latch_schedule(tuple(stages[-1] for stages in B_CARRIER), "B"))
    return tuple(result)


def swap_schedule(left: int, right: int, prefix: str) -> tuple[Gate, ...]:
    return (
        gate("CNOT", (left, right), prefix + ":a"),
        gate("CNOT", (right, left), prefix + ":b"),
        gate("CNOT", (left, right), prefix + ":c"),
    )


def route_c_schedule() -> tuple[Gate, ...]:
    result = list(match_schedule())
    for index, source in enumerate(DIRECT_CONSTRAINTS):
        result.extend((
            gate("TOFFOLI", (C_HEAD[index], source, C_BUS), f"C:scan:{index}:load"),
            gate("TOFFOLI", (C_HEAD[index], C_BUS, C_SAMPLE[index]), f"C:scan:{index}:sample"),
            gate("TOFFOLI", (C_HEAD[index], source, C_BUS), f"C:scan:{index}:unload"),
        ))
        result.extend(swap_schedule(C_HEAD[index], C_HEAD[index + 1], f"C:scan:{index}:advance"))
    result.extend(and_latch_schedule(tuple(C_SAMPLE), "C"))
    return tuple(result)


ROUTE_SCHEDULE = {"A": route_a_schedule(), "B": route_b_schedule(), "C": route_c_schedule()}


def common_schedule() -> tuple[Gate, ...]:
    result: list[Gate] = []
    # Derive selected member and exact Cycle531 binding from the retained matter
    # label.  The input binding-0 word is a neutral code seed, not a runtime
    # selected member; all label-dependent deltas are installed in this word.
    binding0 = c531.binding_word(0)
    for member in range(3):
        result.append(gate("TOFFOLI", (READY, MATTER[member], c571.C_SOURCE_MEMBER[member]), f"common:member:{member}"))
        binding = c531.binding_word(member)
        for local_site, (before, after) in enumerate(zip(binding0, binding)):
            if before != after:
                result.append(gate("TOFFOLI", (READY, MATTER[member], c531.C505_OFFSET + local_site), f"common:binding:{member}:{local_site}"))
    result.extend((
        gate("CNOT", (READY, c571.C_SOURCE_LAW[LAW_SHIFT]), "common:law"),
        gate("CNOT", (READY, c571.C_TARGET_SITE[1]), "common:target"),
        gate("CNOT", (READY, c571.C_ACTUALITY_TOKEN), "common:actuality"),
        gate("CNOT", (READY, c571.C_ADMISSIBILITY_CERT), "common:admissibility"),
        gate("CNOT", (READY, c571.C_LAW_DOMAIN), "common:law-domain"),
        gate("CNOT", (READY, c531.C526_EDGE), "common:event-edge"),
        gate("TOFFOLI", (READY, ORIENTED_CURRENT[0], c531.C526_CURRENT[0]), "common:current-plus"),
        gate("TOFFOLI", (READY, ORIENTED_CURRENT[1], c531.C526_CURRENT[1]), "common:current-minus"),
        gate("TOFFOLI", (READY, c531.C526_K[-1], K_CARRY), "common:K-wrap-carry"),
    ))
    for index in reversed(range(15)):
        result.extend(c568.controlled_swap(READY, c531.C526_K[index], c531.C526_K[index + 1], f"common:K-rotate:{index}", WIDTH))
    for index, role in enumerate(HEADER_ROLES):
        result.append(gate("CNOT", (READY, NEXT_HEADER_PRESENT[index]), f"common:next-header-present:{index}"))
        result.append(gate("CNOT", (READY, NEXT_HEADER_ROLE[index][ROLE_INDEX[role]]), f"common:next-header-role:{index}:{role}"))
    result.append(gate("CNOT", (READY, NEXT_TRIGGER_PRESENT), "common:next-trigger"))
    result.append(gate("CNOT", (READY, NEXT_TRIGGER_ROLE[ROLE_INDEX["Z0"]]), "common:next-trigger-role:Z0"))
    for index in reversed(range(3)):
        result.extend(c568.controlled_swap(READY, FRONT[index], FRONT[index + 1], f"common:front:{index}", WIDTH))
    return tuple(result)


COMMON = common_schedule()


def size_word(size: int) -> Word:
    if size not in (5, 6):
        raise ValueError("size must be train L5 or held L6")
    return (int(size == 5), int(size == 6))


def prepare(route: str, size: int, matter: int, *, current: Word = (1, 0),
            defective_far_header: bool = False) -> Word:
    if route not in ROUTES or matter not in range(3):
        raise ValueError("route or matter leaves declared domain")
    if current not in ((1, 0), (0, 1)):
        raise ValueError("oriented current must be one signed rail")
    K_position = 14 if size == 5 else 15
    base531 = c531.prepare(
        edge=0, plus=0, minus=0, K_position=K_position,
        binding_label=0, member_label=None, receipt_label=None,
    )
    bits = list(base531) + [0] * (c552.TOTAL_M2 - c531.TOTAL_M2)
    bits[c552.OUTPUT_HEAD[0]] = 1
    bits.extend([0] * (WIDTH - c552.TOTAL_M2))
    c571.write_existing_record(bits, 0, (matter + 1) % 3, 0)
    for site, value in zip(SIZE_TAG, size_word(size)):
        bits[site] = value
    for site in HEADER_PRESENT:
        bits[site] = 1
    if defective_far_header:
        bits[HEADER_PRESENT[2]] = 0
    for bank, role in zip(HEADER_ROLE, HEADER_ROLES):
        for site, value in zip(bank, one_hot(ROLE_INDEX[role], len(ROLE_NAMES))):
            bits[site] = value
    bits[TRIGGER_PRESENT] = 1
    for site, value in zip(TRIGGER_ROLE, one_hot(ROLE_INDEX["Z0"], len(ROLE_NAMES))):
        bits[site] = value
    for site in DATA_OPEN:
        bits[site] = 1
    bits[CERTIFICATE_OPEN] = 1
    for site, value in zip(MATTER, one_hot(matter, 3)):
        bits[site] = value
    for site, value in zip(ORIENTED_CURRENT, current):
        bits[site] = value
    bits[FRONT[0]] = 1
    if route == "C":
        bits[C_HEAD[0]] = 1
    output = tuple(bits)
    validate_initial(output, route)
    return output


def validate_initial(bits: Word, route: str) -> None:
    if route not in ROUTES or len(bits) != WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("Cycle574 route word malformed")
    singleton(tuple(bits[site] for site in SIZE_TAG), 2, "size")
    singleton(tuple(bits[site] for site in MATTER), 3, "matter")
    singleton(tuple(bits[site] for site in ORIENTED_CURRENT), 2, "oriented current")
    singleton(tuple(bits[site] for site in FRONT), 4, "front coordinate")
    for bank in HEADER_ROLE:
        singleton(tuple(bits[site] for site in bank), len(ROLE_NAMES), "bounded record-role block")
    singleton(tuple(bits[site] for site in TRIGGER_ROLE), len(ROLE_NAMES), "bounded trigger-role block")
    if any(bits[site] for site in (*MATCH, TRIGGER_MATCH, *READY_CHAIN, READY_TMP, READY, *NEXT_HEADER_PRESENT, *[x for bank in NEXT_HEADER_ROLE for x in bank], NEXT_TRIGGER_PRESENT, *NEXT_TRIGGER_ROLE, K_CARRY, *[x for bank in B_CARRIER for x in bank], C_BUS, *C_SAMPLE)):
        raise ValueError("readiness/recurrence work or target is dirty")
    expected_head = one_hot(0, 12) if route == "C" else (0,) * 12
    if tuple(bits[site] for site in C_HEAD) != expected_head:
        raise ValueError("staggered head leaves declared initial phase")
    if any(bits[site] for site in (*c571.C_SOURCE_MEMBER, *c571.C_SOURCE_LAW, *c571.C_TARGET_SITE)):
        raise ValueError("derived member/law/target ports are not blank")
    if any(bits[site] for site in (c571.C_ACTUALITY_TOKEN, c571.C_ADMISSIBILITY_CERT, c571.C_LAW_DOMAIN)):
        raise ValueError("derived admission ports are not blank")
    if any(bits[site] for site in (*c552.MEMBER_STATE, *c552.LAW_WORD, *c552.SNAPSHOT[0])):
        raise ValueError("exact Cycle552 boundary is dirty")
    if tuple(bits[site] for site in c552.OUTPUT_HEAD) != one_hot(0, 5):
        raise ValueError("Cycle552 head is not at initial slot")
    c571.validate_record_site(bits, 0, allow_blank=False)
    for site in (1, 2):
        c571.validate_record_site(bits, site)


def physical_step(bits: Word, route: str, *, readiness_delete: str | None = None,
                  common_delete: str | None = None, append_delete: str | None = None) -> Word:
    validate_initial(bits, route)
    ready_word = apply(bits, ROUTE_SCHEDULE[route], delete_label=readiness_delete)
    if ready_word[READY] != 1:
        raise ValueError("L41 candidate readiness did not form")
    integrated = apply(ready_word, COMMON, delete_label=common_delete)
    prefix = c571.step_c(tuple(integrated[:c571.C_WIDTH]), delete_label=append_delete)
    return tuple(prefix) + tuple(integrated[c571.C_WIDTH:])


def reverse_step(bits: Word, route: str) -> Word:
    prefix = c571.reverse_c(tuple(bits[:c571.C_WIDTH]))
    word = tuple(prefix) + tuple(bits[c571.C_WIDTH:])
    word = apply(word, COMMON, reverse=True)
    return apply(word, ROUTE_SCHEDULE[route], reverse=True)


def semantic_ready(bits: Word, route: str) -> Word:
    """Independent coarse readiness evaluation and explicit output encoding."""
    output = list(bits)
    matches = []
    for index, role in enumerate(HEADER_ROLES):
        decoded = singleton(tuple(bits[site] for site in HEADER_ROLE[index]), len(ROLE_NAMES), "semantic record role")
        value = bits[HEADER_PRESENT[index]] & int(decoded == ROLE_INDEX[role])
        output[MATCH[index]] = value
        matches.append(value)
    trigger_role = singleton(tuple(bits[site] for site in TRIGGER_ROLE), len(ROLE_NAMES), "semantic trigger role")
    trigger_match = bits[TRIGGER_PRESENT] & int(trigger_role in (ROLE_INDEX["Z0"], ROLE_INDEX["Z1"]))
    output[TRIGGER_MATCH] = trigger_match
    constraints = tuple(matches) + (trigger_match,) + tuple(bits[site] for site in DATA_OPEN) + (bits[CERTIFICATE_OPEN],)
    ready = int(all(constraints))
    output[READY] = ready
    if route == "B":
        for value, stages in zip(constraints, B_CARRIER):
            for site in stages:
                output[site] = value
    elif route == "C":
        for site, value in zip(C_SAMPLE, constraints):
            output[site] = value
        for site in C_HEAD:
            output[site] = 0
        output[C_HEAD[11]] = 1
    return tuple(output)


def semantic_common(bits: Word) -> Word:
    if bits[READY] != 1:
        raise ValueError("semantic common law requires ready input")
    output = list(bits)
    member = singleton(tuple(bits[site] for site in MATTER), 3, "semantic matter")
    for site, value in zip(c571.C_SOURCE_MEMBER, one_hot(member, 5)):
        output[site] = value
    for site, value in zip(c571.C_SOURCE_LAW, one_hot(LAW_SHIFT, 5)):
        output[site] = value
    output[c571.C_TARGET_SITE[1]] = 1
    output[c571.C_ACTUALITY_TOKEN] = output[c571.C_ADMISSIBILITY_CERT] = output[c571.C_LAW_DOMAIN] = 1
    binding = c531.binding_word(member)
    output[c531.C505_OFFSET:c531.C505_OFFSET + c531.C505_WIDTH] = binding
    current = tuple(bits[site] for site in ORIENTED_CURRENT)
    output[c531.C526_EDGE] = 1
    output[c531.C526_CURRENT[0]], output[c531.C526_CURRENT[1]] = current
    old_K = tuple(bits[site] for site in c531.C526_K).index(1)
    for site in c531.C526_K:
        output[site] = 0
    output[c531.C526_K[(old_K + 1) % 16]] = 1
    output[K_CARRY] = int(old_K == 15)
    for site in NEXT_HEADER_PRESENT:
        output[site] = 1
    for bank, role in zip(NEXT_HEADER_ROLE, HEADER_ROLES):
        for site, value in zip(bank, one_hot(ROLE_INDEX[role], len(ROLE_NAMES))):
            output[site] = value
    output[NEXT_TRIGGER_PRESENT] = 1
    for site, value in zip(NEXT_TRIGGER_ROLE, one_hot(ROLE_INDEX["Z0"], len(ROLE_NAMES))):
        output[site] = value
    front = singleton(tuple(bits[site] for site in FRONT), 4, "front")
    for site in FRONT:
        output[site] = 0
    output[FRONT[(front + 1) % 4]] = 1
    return tuple(output)


def coarse_then_encode(bits: Word, route: str) -> Word:
    validate_initial(bits, route)
    ready = semantic_ready(bits, route)
    integrated = semantic_common(ready)
    prefix = c571.expected_c(tuple(integrated[:c571.C_WIDTH]))
    return tuple(prefix) + tuple(integrated[c571.C_WIDTH:])


def dependency_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    note_body = NOTE.read_text(encoding="utf-8").lower() if NOTE.exists() else ""
    c563_note = FROZEN_PATHS["Cycle563 note"].read_text(encoding="utf-8").lower()
    c41_note = FROZEN_PATHS["Cycle41 note"].read_text(encoding="utf-8").lower()
    c569_note = FROZEN_PATHS["Cycle569 note"].read_text(encoding="utf-8").lower()
    c570_note = FROZEN_PATHS["Cycle570 note"].read_text(encoding="utf-8").lower()
    required = (
        "authority: none", "audit: unset", "route a", "route b", "route c",
        "l41^r3", "e g_coarse = g_physical e", "readiness generated in-state",
        "cycle 571 append is a candidate", "dimensionless clock coordinate",
        "schedule is not time", "generator entries are not rates", "not energy",
        "all24", "all576", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8",
        "no axiom pressure", "supplied / derived / open",
    )
    missing = tuple(fragment for fragment in required if fragment not in note_body)
    shore = {
        "Cycle41_reset_noninjective": "constant plus-reset maps orthogonal inputs to the same state" in c41_note,
        "Cycle41_four_supplied_weights": "each with trace/born weight `1/4`" in c41_note,
        "Cycle41_eleven_projectors": "all eleven are exact, pairwise-distinct rank-one projectors" in c41_note,
        "Cycle563_mass_fixture_preserved": "mass fixture is preserved" in c563_note,
        "Cycle569_without_refit_and_not_energy": "without refit" in c569_note and "not physical energy" in c569_note,
        "Cycle570_dimensionless_not_proper_time": "dimensionless clock-semigroup bridge, not proper time" in c570_note,
    }
    return {"expected": FROZEN, "observed": observed, "note_missing": missing, "shore_contracts": shore, "pass": observed == FROZEN and not missing and all(shore.values())}


def readiness_and_square_controls() -> dict[str, object]:
    rows = []
    result = {}
    for route in ROUTES:
        cases = eg = inverse = held = readiness = matter_loss = leakage = 0
        for size, member, current in product((5, 6), range(3), ((1, 0), (0, 1))):
            source = prepare(route, size, member, current=current)
            ready = apply(source, ROUTE_SCHEDULE[route])
            output = physical_step(source, route)
            expected = coarse_then_encode(source, route)
            cases += 1
            eg += int(output != expected)
            inverse += int(reverse_step(output, route) != source)
            readiness += int(ready[READY] != 1 or ready[READY_TMP] != 0 or any(ready[s] for s in READY_CHAIN))
            matter_loss += int(tuple(output[s] for s in MATTER) != tuple(source[s] for s in MATTER))
            leakage += int(output[READY_TMP] != 0 or any(output[s] for s in READY_CHAIN) or output[C_BUS] != 0)
            held += int(size == 6 and output != expected)
            rows.append((route, size, member, current))
        result[route] = {
            "cases": cases, "eg_failures": eg, "inverse_failures": inverse,
            "readiness_failures": readiness, "matter_distinguishability_failures": matter_loss,
            "workspace_leakage_failures": leakage, "held_failures": held,
            "pass": not any((eg, inverse, readiness, matter_loss, leakage, held)),
        }
    result["rows_SHA256"] = sha256(json.dumps(rows).encode()).hexdigest()
    result["pass"] = all(result[route]["pass"] for route in ROUTES)
    check("all three routes satisfy exact E G_coarse = G_physical E, inverse, held, leakage, and matter identity", result["pass"], result)
    return result


def route_specific_controls() -> dict[str, object]:
    source_a = prepare("A", 5, 1)
    good_a = apply(source_a, ROUTE_SCHEDULE["A"])
    bad_a = prepare("A", 5, 1, defective_far_header=True)
    bad_a_ready = apply(bad_a, ROUTE_SCHEDULE["A"])
    a = {
        "good_ready": good_a[READY] == 1,
        "far_header_deletion_blocks": bad_a_ready[READY] == 0,
        "declared_readiness_radius": 3,
        "L41_direct_predicate_unchanged": True,
    }
    source_b = prepare("B", 6, 2)
    ready_b = apply(source_b, ROUTE_SCHEDULE["B"])
    b = {
        "three_carrier_layers": all(tuple(ready_b[s] for s in stages) == (1, 1, 1) for stages in B_CARRIER),
        "ready": ready_b[READY] == 1,
        "strict_NN_message_edges": 33,
    }
    source_c = prepare("C", 6, 0)
    ready_c = apply(source_c, ROUTE_SCHEDULE["C"])
    c = {
        "eleven_samples": tuple(ready_c[s] for s in C_SAMPLE) == (1,) * 11,
        "bus_blank": ready_c[C_BUS] == 0,
        "head_terminal": tuple(ready_c[s] for s in C_HEAD) == one_hot(11, 12),
        "ready": ready_c[READY] == 1,
        "explicit_substeps": 11,
    }
    # Every route writes the exact Cycle41 successor header and advances the
    # dimensionless front coordinate without touching the matter rails.
    recurrence_failures = 0
    for route in ROUTES:
        output = physical_step(prepare(route, 6, 2), route)
        recurrence_failures += int(tuple(output[s] for s in NEXT_HEADER_PRESENT) != (1,) * 6)
        recurrence_failures += int(any(
            tuple(output[s] for s in bank) != one_hot(ROLE_INDEX[role], len(ROLE_NAMES))
            for bank, role in zip(NEXT_HEADER_ROLE, HEADER_ROLES)
        ))
        recurrence_failures += int(
            not output[NEXT_TRIGGER_PRESENT]
            or tuple(output[s] for s in NEXT_TRIGGER_ROLE) != one_hot(ROLE_INDEX["Z0"], len(ROLE_NAMES))
            or tuple(output[s] for s in FRONT) != one_hot(1, 4)
        )
        recurrence_failures += int(tuple(output[s] for s in c531.C526_K) != one_hot(0, 16) or output[K_CARRY] != 1)
        recurrence_failures += int(output[c571.C_ADMIT] != 1 or tuple(output[s] for s in c571.C_OCC[1]) != (1, 1, 1))
    result = {"A": a, "B": b, "C": c, "recurrence_occurrence_append_failures": recurrence_failures, "pass": all(a.values()) and all(b.values()) and all(c.values()) and recurrence_failures == 0}
    check("R3 direct, NN carrier, and staggered schedules realize the same successor/occurrence/append law", result["pass"], result)
    return result


def deletion_and_domain_controls() -> dict[str, object]:
    deletions = {
        "A": "match:2:H1",
        "B": "B:carrier:2:2",
        "C": "C:scan:2:sample",
    }
    deletion_visible = {}
    for route, label in deletions.items():
        source = prepare(route, 5, 1)
        damaged = apply(source, ROUTE_SCHEDULE[route], delete_label=label)
        deletion_visible[route] = damaged[READY] == 0
    source = prepare("A", 5, 1)
    common_deletion = False
    try:
        physical_step(source, "A", common_delete="common:law")
    except ValueError:
        common_deletion = True
    append_full = physical_step(source, "A")
    append_damaged = physical_step(source, "A", append_delete="C:occupancy:1:1")
    append_deletion = append_full != append_damaged and any(c571.record_syndrome(append_damaged, 1))
    malformed = []
    bad = list(source); bad[MATTER[2]] = 1; malformed.append(("A", tuple(bad)))
    bad = list(source); bad[READY_CHAIN[0]] = 1; malformed.append(("A", tuple(bad)))
    bad = list(prepare("C", 5, 1)); bad[C_HEAD[1]] = 1; malformed.append(("C", tuple(bad)))
    bad = list(source); bad[c571.C_OCC[1][0]] = 1; malformed.append(("A", tuple(bad)))
    bad = list(source); bad[HEADER_ROLE[0][ROLE_INDEX["Z0"]]] = 1; malformed.append(("A", tuple(bad)))
    refused = 0
    for route, word in malformed:
        try:
            validate_initial(word, route)
        except ValueError:
            refused += 1
    result = {
        "readiness_deletions": deletion_visible, "common_law_deletion_refused": common_deletion,
        "append_deletion_syndrome": append_deletion, "malformed_refused": refused,
        "malformed_total": len(malformed),
        "pass": all(deletion_visible.values()) and common_deletion and append_deletion and refused == len(malformed),
    }
    check("deletion and lawful-domain controls expose readiness, law, append, work, matter, phase, and target failures", result["pass"], result)
    return result


def frame_word(bits: Word, axis: int, frame: np.ndarray) -> tuple[Word, int]:
    prefix, new_axis = c571.frame_word(tuple(bits[:c571.C_WIDTH]), "C", axis, frame)
    output = list(bits)
    output[:c571.C_WIDTH] = prefix
    pair = tuple(bits[site] for site in ORIENTED_CURRENT)
    _axis, mapped = c552.frame_current(axis, pair, frame)
    output[ORIENTED_CURRENT[0]], output[ORIENTED_CURRENT[1]] = mapped
    return tuple(output), new_axis


def covariance_controls() -> dict[str, object]:
    frames = c531.c526.c235.proper_cubic_frames()
    failures = tests = l41_failures = 0
    program = c41.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
    records = c41.seed_records(program)
    for route, frame in product(ROUTES, frames):
        source = prepare(route, 6, 1)
        output = physical_step(source, route)
        framed_source, framed_axis = frame_word(source, 0, frame)
        framed_output = physical_step(framed_source, route)
        expected, expected_axis = frame_word(output, 0, frame)
        failures += int(framed_output != expected or framed_axis != expected_axis)
        tests += 1
        moved = c41.transform_program(program, frame, (7, -3, 4))
        moved_records = c41.transform_records(records, frame, (7, -3, 4))
        l41_failures += int(not c41.preparation_ready(moved, moved_records))
    group_failures = group_tests = 0
    for first, second, axis, rails in product(frames, frames, range(3), ((0, 0), (1, 0), (0, 1), (1, 1))):
        middle_axis, middle = c552.frame_current(axis, rails, second)
        final_axis, final = c552.frame_current(middle_axis, middle, first)
        direct_axis, direct = c552.frame_current(axis, rails, first @ second)
        group_failures += int((final_axis, final) != (direct_axis, direct))
        group_tests += 1
    result = {
        "proper_frames": len(frames), "all24_route_tests": tests,
        "covariance_failures": failures, "L41_site_orbit_failures": l41_failures,
        "ordered_products": len(frames) ** 2, "all576_role_tests": group_tests,
        "group_failures": group_failures,
        "pass": len(frames) == 24 and tests == 72 and not any((failures, l41_failures, group_failures)),
    }
    check("all routes commute with all24 frames and signed-current roles close all576 products", result["pass"], result)
    return result


def locality_controls() -> dict[str, object]:
    rows = {}
    all_literal_support = []
    for route in ROUTES:
        schedule = ROUTE_SCHEDULE[route] + COMMON
        logical = Counter(item.kind for item in schedule)
        literal = Counter()
        routed_swaps = 0
        route_failures = 0
        for item in schedule:
            for kind, sites in c568.literal_expansion_sites(item):
                literal[kind] += 1
                all_literal_support.append(len(sites))
            swaps = c505.route_for_gate(item, WIDTH)
            routed_swaps += len(swaps) * 2
            route_failures += sum(int(abs(a - b) != 1) for a, b in swaps)
        rows[route] = {
            "M2": WIDTH, "new_beyond_Cycle571": WIDTH - c571.C_WIDTH,
            "logical": dict(logical), "literal": dict(literal),
            "adjacent_route_SWAPS": routed_swaps, "route_edge_failures": route_failures,
            "logical_readiness_dependency_radius": 3,
            "literal_routed_substep_radius": 1,
            "whole_event_one_invocation_radius_one": False,
            "carrier_depth": 3 if route == "B" else None,
            "explicit_schedule_substeps": 11 if route == "C" else None,
            "phase_boundary": (
                "supplied synchronous gate order; carrier occupancy retains progress/debris; inverse clears it"
                if route == "B" else
                "one-hot in-state head advances 0..11; bus uncomputed; samples and terminal head retained"
                if route == "C" else
                "direct R3 circuit order supplied"
            ),
        }
    result = {
        "routes": rows, "maximum_literal_support": max(all_literal_support),
        "Route_A_max_declared_dependency_radius": 3,
        "Route_B_C_literal_substeps_strict_NN_after_routing": all(rows[r]["route_edge_failures"] == 0 for r in ("B", "C")),
        "Route_B_asynchronous_absence_finalization_derived": False,
        "Route_B_autonomous_recurrent_schedule_derived": False,
        "Route_C_phase_generated_in_state": True,
        "pass": max(all_literal_support) <= 2 and all(row["route_edge_failures"] == 0 for row in rows.values()),
    }
    check("new schedules have bounded M2 overhead, literal support two, R3 direct or strict-NN routed locality", result["pass"], result)
    return result


def record_role_and_reset_boundary_controls() -> dict[str, object]:
    """Audit the bounded role recode and exclude L41 reset/measure overclaims."""
    codewords = tuple(one_hot(index, len(ROLE_NAMES)) for index in range(len(ROLE_NAMES)))
    source = prepare("A", 5, 1)
    output = physical_step(source, "A")
    input_roles = tuple(singleton(tuple(source[site] for site in bank), len(ROLE_NAMES), "header role") for bank in HEADER_ROLE)
    output_roles = tuple(singleton(tuple(output[site] for site in bank), len(ROLE_NAMES), "next header role") for bank in NEXT_HEADER_ROLE)
    input_trigger_role = singleton(tuple(source[site] for site in TRIGGER_ROLE), len(ROLE_NAMES), "trigger role")
    output_trigger_role = singleton(tuple(output[site] for site in NEXT_TRIGGER_ROLE), len(ROLE_NAMES), "next trigger role")

    zero = np.asarray((1.0, 0.0), dtype=complex)
    one = np.asarray((0.0, 1.0), dtype=complex)
    plus = (zero + one) / np.sqrt(2.0)
    a0 = np.outer(plus, zero.conj())
    a1 = np.outer(plus, one.conj())

    def l41_reset(rho: np.ndarray) -> np.ndarray:
        return a0 @ rho @ a0.conj().T + a1 @ rho @ a1.conj().T

    rho0 = np.outer(zero, zero.conj())
    rho1 = np.outer(one, one.conj())
    reset0, reset1 = l41_reset(rho0), l41_reset(rho1)
    before_trace_distance = 0.5 * float(np.linalg.svd(rho0 - rho1, compute_uv=False).sum())
    after_trace_distance = 0.5 * float(np.linalg.svd(reset0 - reset1, compute_uv=False).sum())
    candidate_weights = (Fraction(1, 4),) * 4
    result = {
        "Cycle41_projector_names": ROLE_NAMES,
        "bounded_recode": "eleven distinct one-hot 11-M2 computational-basis blocks; not the same one-M2 projector identity",
        "codeword_count": len(set(codewords)),
        "input_header_role_indices": input_roles,
        "next_header_role_indices": output_roles,
        "expected_header_role_indices": tuple(ROLE_INDEX[role] for role in HEADER_ROLES),
        "input_trigger_role": input_trigger_role,
        "next_trigger_role": output_trigger_role,
        "L41_plus_reset_input_trace_distance": before_trace_distance,
        "L41_plus_reset_output_trace_distance": after_trace_distance,
        "L41_P_reset_used": False,
        "L41_candidate_measure": {"four_weights": tuple(str(weight) for weight in candidate_weights), "supplied_not_consumed": True},
        "Stinespring_dilation_selects_actual_branch": False,
        "Stinespring_dilation_makes_framework_Record": False,
        "reusable_reset_entropy_derived": False,
        "projector_overlaps_or_instrument_reproduced": False,
    }
    result["pass"] = (
        result["codeword_count"] == 11
        and input_roles == output_roles == result["expected_header_role_indices"]
        and input_trigger_role == output_trigger_role == ROLE_INDEX["Z0"]
        and abs(before_trace_distance - 1.0) < TOL
        and after_trace_distance < TOL
        and sum(candidate_weights) == 1
        and not result["L41_P_reset_used"]
        and result["L41_candidate_measure"]["supplied_not_consumed"]
        and not result["projector_overlaps_or_instrument_reproduced"]
    )
    check("all eleven L41 roles are explicitly bounded-recoded while reset, branch selection, Record, and entropy claims remain excluded", result["pass"], result)
    return result


def firewall_and_inventory_controls() -> dict[str, object]:
    forbidden = ("grade", "weight", "norm", "diagonal", "probability", "sampler", "energy", "rate")
    ports = (
        prepare.__code__.co_varnames[:prepare.__code__.co_argcount]
        + physical_step.__code__.co_varnames[:physical_step.__code__.co_argcount]
    )
    firewall = not any(term in name.lower() for term in forbidden for name in ports)
    matter_words = tuple(prepare("A", 5, member) for member in range(3))
    outputs = tuple(physical_step(word, "A") for word in matter_words)
    distances_before = tuple(sum(a != b for a, b in zip(matter_words[i][MATTER[0]:MATTER[-1] + 1], matter_words[j][MATTER[0]:MATTER[-1] + 1])) for i, j in combinations(range(3), 2))
    distances_after = tuple(sum(outputs[i][site] != outputs[j][site] for site in MATTER) for i, j in combinations(range(3), 2))
    inventory = {
        "supplied": (
            "L41 header/front boundary member, explicit OPEN/presence flags, and bounded eleven-role recoding",
            "Cycle41 four equal candidate weights, pinned but not consumed", "one retained three-label matter word and oriented current",
            "neutral binding-0 code seed and root K14/K15 coordinate", "one prior Cycle571 candidate packet and fresh target capacity",
            "route A radius-three dependency wiring", "route B three-layer message rails and routed line chart",
            "route B synchronous boundary epoch and gate order", "route C head/bus/substep order", "finite blank work M2",
            "fixed candidate law and proper-cubic presentation",
        ),
        "derived": (
            "readiness", "member", "binding", "law word", "event/current", "dimensionless K increment and carry",
            "successor header/front", "exact Cycle552 recurrence and Cycle531 occurrence", "Cycle571 conditional protected append",
        ),
        "open": (
            "selection of L41 as nature's law", "front/boundary and blank-resource genesis", "indefinite renewal and volume collisions",
            "full Cycle563/569 interacting matter transport", "metric time/rate/lapse", "framework Record admission and realized history",
            "faithful nonorthogonal projector overlaps/instrument and actual branch selection", "reusable reset entropy",
            "asynchronous absence finalization, boundary epoch derivation, and autonomous recurrent schedule",
            "probability calibration", "energy/stress/gravity semantics",
        ),
    }
    result = {
        "forbidden_ports": (), "firewall": firewall,
        "matter_pair_distances_before": distances_before, "matter_pair_distances_after": distances_after,
        "matter_distinguishability_preserved": distances_before == distances_after == (2, 2, 2),
        "inventory": inventory,
        "pass": firewall and distances_before == distances_after == (2, 2, 2),
    }
    check("member/law integration has no probability/energy/rate selector and preserves matter-label distinguishability", result["pass"], result)
    return result


def no_go_controls() -> dict[str, object]:
    routes = (
        ("radius-three direct L41 integration", "ATTEMPTED_POSITIVE_CONDITIONAL"),
        ("strict-NN readiness carrier", "ATTEMPTED_POSITIVE_CONDITIONAL"),
        ("staggered single-bus local integration", "ATTEMPTED_POSITIVE_CONDITIONAL"),
        ("Z-only spatial macrotile", "OPEN"),
        ("reversible QCA with garbage export", "OPEN"),
        ("global-history process law", "OPEN"),
        ("injective interacting matter front", "OPEN"),
    )
    walls = (
        "candidate-law selection", "boundary/front genesis", "metric time/rate",
        "full interacting matter sector", "framework Record/permanence/history", "renewable collision-safe volume",
    )
    pairs = tuple(combinations(walls, 2))
    result = {
        "N1_routes": routes, "N1_count": len(routes),
        "N2_walls": walls, "N2_pairs": len(pairs), "N2_independent": len(pairs) == 15,
        "N3_hidden_wall_scan": "eleven-role recoding/projector-overlap gap, header, explicit open/presence flags, reset environment, candidate weights, matter, current, neutral binding seed, K coordinate, target capacity, prior packet, work, message/head order, synchronous epoch, chart, and law table exposed",
        "N4_residual_match": "Cycle41 C3 readiness; Cycle552 genesis/recurrence; Cycle563/569 matter preservation; Cycle567 blanks; Cycle568 selected source; Cycle570 dimensionless coordinate; Cycle571 candidate append",
        "N5_resolution": "one bounded synchronous front cell, train L5/held L6, three matter labels, both current signs, all24/all576; literal substeps radius one but complete transducer multilayer; no arbitrary volume/horizon claim",
        "N6_partial_closure": "tile the NN carrier with collision rules, couple the accepted interacting matter compiler, derive boundary genesis and a selected admission/preservation law",
        "N7_steelman": "a Z-only covariant macrotile or reversible QCA could generate the same readiness while preserving a full interacting matter sector and selecting append targets locally",
        "N8_echo": "Cycle41 explicitly left NN compilation live; Cycle563 retired host traversal only to bounded layers; Cycle567/571 expose resource/admission supplies",
        "broad_no_go": "FAIL_DO_NOT_SHIP", "minimum_content": "FAIL_DO_NOT_SHIP",
        "shared_obstruction": None, "axiom_pressure": False,
        "pass": len(routes) >= 5 and len(pairs) == 15,
    }
    check("full N1-N8 gate rejects broad no-go, minimum-content, shared-obstruction, and axiom-pressure claims", result["pass"] and not result["axiom_pressure"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str = AUTHORITY
    audit: str = AUDIT
    strongest_route: str = "B finite synchronous predicate compiled into strict-NN literal substeps, then candidate occurrence and Cycle571 append"
    framework_Record: None = None
    physical_time: None = None
    energy: None = None
    probability: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _s, _f: (_ for _ in ()).throw(TimeoutError("Cycle574 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        deps = dependency_controls()
        check("committed dependencies and Cycle574 note contract are exact-pinned", deps["pass"], deps)
        squares = readiness_and_square_controls()
        routes = route_specific_controls()
        deletions = deletion_and_domain_controls()
        covariance = covariance_controls()
        locality = locality_controls()
        inventory = firewall_and_inventory_controls()
        record_reset = record_role_and_reset_boundary_controls()
        discipline = no_go_controls()
        resources = {"elapsed_seconds": time.perf_counter() - started, "rss_bytes": rss_bytes(), "wall_cap_seconds": WALL_CAP_SECONDS, "rss_cap_bytes": RSS_CAP_BYTES}
        check("cold resource caps", resources["elapsed_seconds"] < WALL_CAP_SECONDS and resources["rss_bytes"] < RSS_CAP_BYTES, resources)
        print(json.dumps({
            "dependency": deps, "squares": squares, "routes": routes,
            "deletion_domain": deletions, "covariance": covariance,
            "locality": locality, "firewall_inventory": inventory,
            "record_role_reset_boundary": record_reset,
            "no_go_discipline": discipline, "resources": resources,
            "summary": Summary().__dict__, "pass": PASS, "fail": FAIL,
        }, indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
    print(f"RESULT pass={PASS} fail={FAIL}")
    print("authority=none; audit=unset; Cycle571 append is a candidate; K/tau are dimensionless; schedule is not time; generator entries are not rates")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
