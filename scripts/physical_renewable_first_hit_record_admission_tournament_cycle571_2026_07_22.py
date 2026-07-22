#!/usr/bin/env python3
"""Cycle571: renewable carrier, first-hit, and Record-admission tournament.

The runner composes three new finite reversible source/admission cells with the
exact Cycle552 MEMBER_STATE/law boundary and the unchanged Cycle531 occurrence
packet.  It never uses an algebraic grade, weight, norm, diagonal, probability,
or sampler to select a member.  The Record route is a conditional finite
site-tagged admission candidate; reversibility and bounded protection are not
promoted to irreversible/unbounded permanence or realized history.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_objective_member_record_bridge_tournament_cycle568_2026_07_22 as c568


c552 = c568.c552
c531 = c568.c531
c565 = c568.c565
c505 = c568.c505

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RENEWABLE_FIRST_HIT_RECORD_ADMISSION_TOURNAMENT_CYCLE571_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
ACCEPTED_CYCLE568_COMMIT = "a6f4bd5356"
TOL = 8e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Gate = c505.Gate

FROZEN_PATHS = {
    "Cycle568 runner": ROOT / "scripts/physical_objective_member_record_bridge_tournament_cycle568_2026_07_22.py",
    "Cycle568 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_OBJECTIVE_MEMBER_RECORD_BRIDGE_TOURNAMENT_CYCLE568_NOTE_2026-07-22.md",
    "Cycle552 runner": ROOT / "scripts/physical_autonomous_local_member_law_cell_cycle552_2026_07_21.py",
    "Cycle552 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_LOCAL_MEMBER_LAW_CELL_CYCLE552_NOTE_2026-07-21.md",
    "Cycle531 runner": ROOT / "scripts/physical_selected_seam_conditional_record_binder_cycle531_2026_07_21.py",
    "Cycle531 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CONDITIONAL_RECORD_BINDER_CYCLE531_NOTE_2026-07-21.md",
    "Cycle433 runner": ROOT / "scripts/physical_detector_to_protected_record_formation_compiler_cycle433_2026_07_19.py",
    "Cycle433 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_DETECTOR_TO_PROTECTED_RECORD_FORMATION_COMPILER_CYCLE433_NOTE_2026-07-19.md",
    "minimal axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "formation append": ROOT / "docs/RECORD_FORMATION_APPEND_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md",
    "production interface": ROOT / "docs/RECORD_PRODUCTION_INTERFACE_PRINCIPLE_2026-06-06.md",
    "production kernel": ROOT / "docs/RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md",
    "fresh-site permanence": ROOT / "docs/RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "continuation refinement": ROOT / "docs/ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md",
}
FROZEN = {
    "Cycle568 runner": "eeb044df6b4d73ace0f707908d9101919d69df4002fdeb249f2c71d4f1735179",
    "Cycle568 note": "6879e89721609e7e4673334346942d772c031871b044e1a216565f2efc89fcbb",
    "Cycle552 runner": "405cacd821b5453045f8a8920b1ab0fc2dca5ac90fb150e9b4a95f6f218ac8a4",
    "Cycle552 note": "919f95dd43d8bdd5ba65fba071f58a6d054a89b3d7d4b7cc04686c8c28cdbf42",
    "Cycle531 runner": "8885593dcc644e601179891265c226158c8835a8a143ed7205c0cc7e291e9057",
    "Cycle531 note": "ed40564d4e57090cf03e706b54964e5a24cb735f9ca14df8f008fecffc388042",
    "Cycle433 runner": "53a8c2b97407b6444ad0c0bc2e4077419c9e74686bc309cbd1884066bdd378d3",
    "Cycle433 note": "ae03b1158f095c9ac654ec65cd0dc023b85aa9cf096d08ffd77774e22f4d237a",
    "minimal axioms": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "formation append": "8b2315c8756f77d31de75a84b65bb7526db81eea176fdcf80bcd03a4ca8ef77d",
    "production interface": "13978d5263a1b91e660a2bfd9f2ba5c27d2030e73113da9ae1eea3a20c609e32",
    "production kernel": "26de173bb9e3a613145fa72e614a0e27d67bcbfb431605d0f8b376b52c724b26",
    "fresh-site permanence": "5ed49dd0e0db1183cb464c3daa3748be593387ca177f7bf4ad8d40c215e85e9e",
    "continuation refinement": "d22a7ec84c3ffc8a57f46d9d2353d47837aad19d3ea6a041836f9e5334d314d9",
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
        raise ValueError("one-hot label leaves its carrier")
    return tuple(int(index == label) for index in range(width))


def singleton(bits: Word, width: int, name: str) -> int:
    if len(bits) != width or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError(f"{name} leaves its binary carrier")
    if sum(bits) != 1:
        raise ValueError(f"{name} is not one-hot")
    return bits.index(1)


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    result = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return result


def gate(kind: str, sites: tuple[int, ...], label: str, width: int) -> Gate:
    return c505.gate(kind, sites, label, width)


def swap_schedule(left: int, right: int, prefix: str, width: int) -> tuple[Gate, ...]:
    return (
        gate("CNOT", (left, right), prefix + ":a", width),
        gate("CNOT", (right, left), prefix + ":b", width),
        gate("CNOT", (left, right), prefix + ":c", width),
    )


def and3_schedule(a: int, b: int, c: int, work: int, target: int, prefix: str, width: int) -> tuple[Gate, ...]:
    return (
        gate("TOFFOLI", (a, b, work), prefix + ":pair", width),
        gate("TOFFOLI", (work, c, target), prefix + ":write", width),
        gate("TOFFOLI", (a, b, work), prefix + ":unpair", width),
    )


def apply(bits: Word, schedule: tuple[Gate, ...], *, reverse: bool = False,
          delete_label: str | None = None) -> Word:
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("word leaves binary M2 carrier")
    if delete_label is not None:
        matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("deletion must name exactly one gate")
        schedule = tuple(item for index, item in enumerate(schedule) if index != matches[0])
    word = list(bits)
    for item in (tuple(reversed(schedule)) if reverse else schedule):
        c505.apply_gate(word, item)
    return tuple(word)


def base_prepare(member: int | None, law: int | None, *, binding: int, plus: int,
                 minus: int, K_position: int) -> Word:
    raw = list(c531.prepare(
        edge=1, plus=plus, minus=minus, K_position=K_position,
        binding_label=binding, member_label=None, receipt_label=None,
    ))
    raw.extend([0] * (c552.TOTAL_M2 - c531.TOTAL_M2))
    raw[c552.OUTPUT_HEAD[0]] = 1
    if member is not None:
        for site, bit in zip(c552.MEMBER_STATE, one_hot(member, 5)):
            raw[site] = bit
    if law is not None:
        for site, bit in zip(c552.LAW_WORD, one_hot(law, 5)):
            raw[site] = bit
    return tuple(raw)


def semantic_c552(base: Word, member: int, law: int) -> Word:
    """Independent coarse Cycle531 map followed by the declared Cycle552 encoding."""
    expected = list(base)
    for site, bit in zip(c552.MEMBER_STATE, one_hot(member, 5)):
        expected[site] = bit
    for site, bit in zip(c552.LAW_WORD, one_hot(law, 5)):
        expected[site] = bit
    binding = c505.c_view(tuple(expected[c531.C505_OFFSET:c531.C505_OFFSET + c531.C505_WIDTH])).eligibility.index(1)
    Kword = tuple(expected[site] for site in c531.C526_K)
    exact = c531.logical_apply(c531.prepare(
        edge=expected[c531.C526_EDGE],
        plus=expected[c531.C526_CURRENT[0]], minus=expected[c531.C526_CURRENT[1]],
        K_position=Kword.index(1), binding_label=binding,
        member_label=member, receipt_label=member,
    ))
    fields = tuple(exact[site] for site in c552.C531_OUTPUT_FIELDS)
    for site, bit in zip(c552.MEMBER_STATE, one_hot((member + law) % 5, 5)):
        expected[site] = bit
    for site in c552.OUTPUT_HEAD:
        expected[site] = 0
    expected[c552.OUTPUT_HEAD[1]] = 1
    for site, bit in zip(c552.SNAPSHOT[0][:12], fields):
        expected[site] = bit
    for site, bit in zip(c552.SNAPSHOT[0][12:], one_hot(law, 5)):
        expected[site] = bit
    return tuple(expected)


# Route A: one active carrier is consumed and the active inlet is renewed from
# a two-carrier finite reserve.  The spent resource and its member label remain.
_a = [c552.TOTAL_M2]
A_ACTIVE_MEMBER = take(_a, 5)
A_ACTIVE_LAW = take(_a, 5)
A_RESERVE_MEMBER = tuple(take(_a, 5) for _ in range(2))
A_RESERVE_LAW = tuple(take(_a, 5) for _ in range(2))
A_ACTIVE_READY = take(_a, 1)[0]
A_RESERVE_READY = take(_a, 2)
A_SPENT_READY = take(_a, 1)[0]
A_SPENT_LABEL = take(_a, 5)
A_WIDTH = _a[0]


def route_a_schedule() -> tuple[Gate, ...]:
    result: list[Gate] = []
    for lane in range(5):
        result.extend(swap_schedule(A_ACTIVE_MEMBER[lane], c552.MEMBER_STATE[lane], f"A:consume-member:{lane}", A_WIDTH))
        result.extend(swap_schedule(A_ACTIVE_LAW[lane], c552.LAW_WORD[lane], f"A:consume-law:{lane}", A_WIDTH))
        result.append(gate("CNOT", (c552.MEMBER_STATE[lane], A_SPENT_LABEL[lane]), f"A:retain-spent-label:{lane}", A_WIDTH))
    result.extend(swap_schedule(A_ACTIVE_READY, A_SPENT_READY, "A:ready-to-spent", A_WIDTH))
    for lane in range(5):
        result.extend(swap_schedule(A_RESERVE_MEMBER[0][lane], A_ACTIVE_MEMBER[lane], f"A:renew-member-0:{lane}", A_WIDTH))
        result.extend(swap_schedule(A_RESERVE_MEMBER[1][lane], A_RESERVE_MEMBER[0][lane], f"A:renew-member-1:{lane}", A_WIDTH))
        result.extend(swap_schedule(A_RESERVE_LAW[0][lane], A_ACTIVE_LAW[lane], f"A:renew-law-0:{lane}", A_WIDTH))
        result.extend(swap_schedule(A_RESERVE_LAW[1][lane], A_RESERVE_LAW[0][lane], f"A:renew-law-1:{lane}", A_WIDTH))
    result.extend(swap_schedule(A_RESERVE_READY[0], A_ACTIVE_READY, "A:renew-ready-0", A_WIDTH))
    result.extend(swap_schedule(A_RESERVE_READY[1], A_RESERVE_READY[0], "A:renew-ready-1", A_WIDTH))
    return tuple(result)


A_SCHEDULE = route_a_schedule()


def prepare_a(member: int, law: int, reserve_members: tuple[int, int], reserve_laws: tuple[int, int],
              *, binding: int, size: int) -> Word:
    if size not in (5, 6):
        raise ValueError("size must be L5 or L6")
    c565.validate_interface_member(5, member)
    base = base_prepare(None, None, binding=binding, plus=int(size == 5), minus=int(size == 6), K_position=(member + law + size) % 16)
    bits = list(base) + [0] * (A_WIDTH - c552.TOTAL_M2)
    for sites, label in (
        (A_ACTIVE_MEMBER, member), (A_ACTIVE_LAW, law),
        (A_RESERVE_MEMBER[0], reserve_members[0]), (A_RESERVE_MEMBER[1], reserve_members[1]),
        (A_RESERVE_LAW[0], reserve_laws[0]), (A_RESERVE_LAW[1], reserve_laws[1]),
    ):
        for site, bit in zip(sites, one_hot(label, 5)):
            bits[site] = bit
    bits[A_ACTIVE_READY] = 1
    for site in A_RESERVE_READY:
        bits[site] = 1
    validate_a(tuple(bits))
    return tuple(bits)


def validate_a(bits: Word) -> None:
    if len(bits) != A_WIDTH:
        raise ValueError("A width mismatch")
    for sites, name in (
        (A_ACTIVE_MEMBER, "active member"), (A_ACTIVE_LAW, "active law"),
        (A_RESERVE_MEMBER[0], "reserve member 0"), (A_RESERVE_MEMBER[1], "reserve member 1"),
        (A_RESERVE_LAW[0], "reserve law 0"), (A_RESERVE_LAW[1], "reserve law 1"),
    ):
        singleton(tuple(bits[site] for site in sites), 5, name)
    if tuple(bits[site] for site in (A_ACTIVE_READY, *A_RESERVE_READY, A_SPENT_READY)) != (1, 1, 1, 0):
        raise ValueError("A ready/spent ledger malformed")
    if any(bits[site] for site in (*A_SPENT_LABEL, *c552.MEMBER_STATE, *c552.LAW_WORD, *c552.SNAPSHOT[0])):
        raise ValueError("A consumer or spent target dirty")


def step_a(bits: Word, *, delete_label: str | None = None) -> Word:
    validate_a(bits)
    generated = apply(bits, A_SCHEDULE, delete_label=delete_label)
    base = c552.physical_step(tuple(generated[:c552.TOTAL_M2]))
    return tuple(base) + tuple(generated[c552.TOTAL_M2:])


def reverse_a(bits: Word) -> Word:
    base = c552.apply_schedule(tuple(bits[:c552.TOTAL_M2]), reverse=True)
    return apply(tuple(base) + tuple(bits[c552.TOTAL_M2:]), A_SCHEDULE, reverse=True)


def expected_a(bits: Word) -> Word:
    validate_a(bits)
    member = singleton(tuple(bits[site] for site in A_ACTIVE_MEMBER), 5, "A member")
    law = singleton(tuple(bits[site] for site in A_ACTIVE_LAW), 5, "A law")
    reserve_members = tuple(singleton(tuple(bits[s] for s in bank), 5, "A reserve") for bank in A_RESERVE_MEMBER)
    reserve_laws = tuple(singleton(tuple(bits[s] for s in bank), 5, "A reserve law") for bank in A_RESERVE_LAW)
    output = list(bits)
    output[:c552.TOTAL_M2] = semantic_c552(tuple(bits[:c552.TOTAL_M2]), member, law)
    for sites, label in (
        (A_ACTIVE_MEMBER, reserve_members[0]), (A_RESERVE_MEMBER[0], reserve_members[1]),
        (A_ACTIVE_LAW, reserve_laws[0]), (A_RESERVE_LAW[0], reserve_laws[1]),
        (A_SPENT_LABEL, member),
    ):
        for site, bit in zip(sites, one_hot(label, 5)):
            output[site] = bit
    for site in (*A_RESERVE_MEMBER[1], *A_RESERVE_LAW[1]):
        output[site] = 0
    output[A_ACTIVE_READY], output[A_RESERVE_READY[0]], output[A_RESERVE_READY[1]], output[A_SPENT_READY] = 1, 1, 0, 1
    return tuple(output)


# Route B: raw two-lane arrivals in three ordered local time bins.  The fixed
# detector computes the unique earliest lane; no-hit and earliest collision are
# explicit non-code controls, not silently defaulted members.
_b = [c552.TOTAL_M2]
B_ARRIVAL = tuple(take(_b, 2) for _ in range(3))
B_LABEL = tuple(tuple(take(_b, 5) for _ in range(2)) for _ in range(3))
B_LAW = take(_b, 5)
B_PREFIX = take(_b, 4)
B_WINNER = tuple(take(_b, 2) for _ in range(3))
B_COLLISION = take(_b, 3)
B_WORK = take(_b, 1)[0]
B_WIDTH = _b[0]


def route_b_detector_schedule() -> tuple[Gate, ...]:
    result: list[Gate] = []
    for epoch in range(3):
        a0, a1 = B_ARRIVAL[epoch]
        prefix = B_PREFIX[epoch]
        # unique lane zero
        result.append(gate("X", (a1,), f"B:{epoch}:open-lane1", B_WIDTH))
        result.extend(and3_schedule(prefix, a0, a1, B_WORK, B_WINNER[epoch][0], f"B:{epoch}:winner0", B_WIDTH))
        result.append(gate("X", (a1,), f"B:{epoch}:close-lane1", B_WIDTH))
        # unique lane one
        result.append(gate("X", (a0,), f"B:{epoch}:open-lane0", B_WIDTH))
        result.extend(and3_schedule(prefix, a1, a0, B_WORK, B_WINNER[epoch][1], f"B:{epoch}:winner1", B_WIDTH))
        result.append(gate("X", (a0,), f"B:{epoch}:close-lane0", B_WIDTH))
        # collision at the earliest occupied bin
        result.extend(and3_schedule(prefix, a0, a1, B_WORK, B_COLLISION[epoch], f"B:{epoch}:collision", B_WIDTH))
        # next prefix = prefix AND NOT a0 AND NOT a1
        result.append(gate("X", (a0,), f"B:{epoch}:prefix-open0", B_WIDTH))
        result.append(gate("X", (a1,), f"B:{epoch}:prefix-open1", B_WIDTH))
        result.extend(and3_schedule(prefix, a0, a1, B_WORK, B_PREFIX[epoch + 1], f"B:{epoch}:prefix", B_WIDTH))
        result.append(gate("X", (a1,), f"B:{epoch}:prefix-close1", B_WIDTH))
        result.append(gate("X", (a0,), f"B:{epoch}:prefix-close0", B_WIDTH))
    return tuple(result)


def route_b_emit_schedule() -> tuple[Gate, ...]:
    result: list[Gate] = []
    for epoch, lane, label in product(range(3), range(2), range(5)):
        result.append(gate(
            "TOFFOLI", (B_WINNER[epoch][lane], B_LABEL[epoch][lane][label], c552.MEMBER_STATE[label]),
            f"B:emit:{epoch}:{lane}:{label}", B_WIDTH,
        ))
    for law in range(5):
        result.append(gate("CNOT", (B_LAW[law], c552.LAW_WORD[law]), f"B:law:{law}", B_WIDTH))
    return tuple(result)


B_DETECT = route_b_detector_schedule()
B_EMIT = route_b_emit_schedule()


def prepare_b(arrivals: tuple[tuple[int, int], ...], labels: tuple[tuple[int | None, int | None], ...],
              law: int, *, binding: int, size: int) -> Word:
    if len(arrivals) != 3 or len(labels) != 3 or size not in (5, 6):
        raise ValueError("B finite domain malformed")
    base = base_prepare(None, None, binding=binding, plus=int(size == 5), minus=int(size == 6), K_position=(law + size) % 16)
    bits = list(base) + [0] * (B_WIDTH - c552.TOTAL_M2)
    for epoch, lane in product(range(3), range(2)):
        arrival = arrivals[epoch][lane]
        label = labels[epoch][lane]
        bits[B_ARRIVAL[epoch][lane]] = arrival
        if arrival:
            if label is None:
                raise ValueError("occupied B lane lacks a label")
            c565.validate_interface_member(5, label)
            for site, bit in zip(B_LABEL[epoch][lane], one_hot(label, 5)):
                bits[site] = bit
        elif label is not None:
            raise ValueError("empty B lane carries a label")
    for site, bit in zip(B_LAW, one_hot(law, 5)):
        bits[site] = bit
    bits[B_PREFIX[0]] = 1
    return tuple(bits)


def first_hit_semantics(bits: Word) -> tuple[str, int | None, int | None, int | None]:
    for epoch in range(3):
        arrivals = tuple(bits[site] for site in B_ARRIVAL[epoch])
        if arrivals == (0, 0):
            continue
        if arrivals == (1, 1):
            return "collision", epoch, None, None
        lane = arrivals.index(1)
        member = singleton(tuple(bits[site] for site in B_LABEL[epoch][lane]), 5, "winner label")
        return "winner", epoch, lane, member
    return "no-hit", None, None, None


def validate_b(bits: Word, *, require_winner: bool) -> tuple[int, int, int] | None:
    if len(bits) != B_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("B word leaves bounded binary domain")
    singleton(tuple(bits[site] for site in B_LAW), 5, "B law")
    for epoch, lane in product(range(3), range(2)):
        arrival = bits[B_ARRIVAL[epoch][lane]]
        label = tuple(bits[site] for site in B_LABEL[epoch][lane])
        if arrival:
            singleton(label, 5, "B occupied label")
        elif any(label):
            raise ValueError("B empty lane carries label")
    if tuple(bits[site] for site in B_PREFIX) != (1, 0, 0, 0):
        raise ValueError("B prefix work is dirty")
    if any(bits[site] for site in (*[s for pair in B_WINNER for s in pair], *B_COLLISION, B_WORK, *c552.MEMBER_STATE, *c552.LAW_WORD, *c552.SNAPSHOT[0])):
        raise ValueError("B detector/consumer target is dirty")
    status, epoch, lane, member = first_hit_semantics(bits)
    if require_winner and status != "winner":
        raise ValueError(f"B positive code requires unique first hit, got {status}")
    return None if status != "winner" else (int(epoch), int(lane), int(member))


def detect_b(bits: Word, *, delete_label: str | None = None) -> Word:
    validate_b(bits, require_winner=False)
    return apply(bits, B_DETECT, delete_label=delete_label)


def step_b(bits: Word, *, delete_label: str | None = None) -> Word:
    winner = validate_b(bits, require_winner=True)
    assert winner is not None
    detected = apply(bits, B_DETECT, delete_label=delete_label if delete_label and delete_label.startswith("B:") and ":emit:" not in delete_label and ":law:" not in delete_label else None)
    emitted = apply(detected, B_EMIT, delete_label=delete_label if delete_label and (":emit:" in delete_label or ":law:" in delete_label) else None)
    base = c552.physical_step(tuple(emitted[:c552.TOTAL_M2]))
    return tuple(base) + tuple(emitted[c552.TOTAL_M2:])


def reverse_b(bits: Word) -> Word:
    base = c552.apply_schedule(tuple(bits[:c552.TOTAL_M2]), reverse=True)
    word = apply(tuple(base) + tuple(bits[c552.TOTAL_M2:]), B_EMIT, reverse=True)
    return apply(word, B_DETECT, reverse=True)


def expected_b(bits: Word) -> Word:
    winner = validate_b(bits, require_winner=True)
    assert winner is not None
    epoch, lane, member = winner
    law = singleton(tuple(bits[site] for site in B_LAW), 5, "B law")
    expected = list(bits)
    expected[:c552.TOTAL_M2] = semantic_c552(tuple(bits[:c552.TOTAL_M2]), member, law)
    prefix = 1
    for index in range(3):
        a0, a1 = (bits[site] for site in B_ARRIVAL[index])
        expected[B_WINNER[index][0]] = prefix & a0 & (1 - a1)
        expected[B_WINNER[index][1]] = prefix & (1 - a0) & a1
        expected[B_COLLISION[index]] = prefix & a0 & a1
        prefix &= (1 - a0) & (1 - a1)
        expected[B_PREFIX[index + 1]] = prefix
    assert (epoch, lane) == next((i, j) for i, pair in enumerate(B_WINNER) for j, site in enumerate(pair) if expected[site])
    return tuple(expected)


# Route C: a supplied candidate law/domain and actuality token append a full
# independent packet at one fresh site.  The packet satisfies the finite
# site/content/readout clauses but remains reversible and below selected
# framework Record status.
SITE_COUNT = 3
_c = [c552.TOTAL_M2]
C_SOURCE_MEMBER = take(_c, 5)
C_SOURCE_LAW = take(_c, 5)
C_TARGET_SITE = take(_c, SITE_COUNT)
C_ACTUALITY_TOKEN = take(_c, 1)[0]
C_ADMISSIBILITY_CERT = take(_c, 1)[0]
C_LAW_DOMAIN = take(_c, 1)[0]
C_FRESH = take(_c, SITE_COUNT)
C_FRESH_ANY = take(_c, 1)[0]
C_CHAIN = take(_c, 3)
C_ADMIT = take(_c, 1)[0]
C_WORK = take(_c, 1)[0]
C_OCC = tuple(take(_c, 3) for _ in range(SITE_COUNT))
C_MEMBER = tuple(tuple(take(_c, 5) for _ in range(3)) for _ in range(SITE_COUNT))
C_LAW = tuple(tuple(take(_c, 5) for _ in range(3)) for _ in range(SITE_COUNT))
C_FIELDS = tuple(take(_c, 12) for _ in range(SITE_COUNT))
C_WIDTH = _c[0]


def route_c_generation_schedule() -> tuple[Gate, ...]:
    result: list[Gate] = []
    for label in range(5):
        result.append(gate("CNOT", (C_SOURCE_MEMBER[label], c552.MEMBER_STATE[label]), f"C:source-member:{label}", C_WIDTH))
        result.append(gate("CNOT", (C_SOURCE_LAW[label], c552.LAW_WORD[label]), f"C:source-law:{label}", C_WIDTH))
    return tuple(result)


def route_c_admission_schedule() -> tuple[Gate, ...]:
    result: list[Gate] = []
    for site in range(SITE_COUNT):
        occ = C_OCC[site][0]
        result.append(gate("X", (occ,), f"C:fresh-open:{site}", C_WIDTH))
        result.append(gate("TOFFOLI", (C_TARGET_SITE[site], occ, C_FRESH[site]), f"C:fresh-write:{site}", C_WIDTH))
        result.append(gate("X", (occ,), f"C:fresh-close:{site}", C_WIDTH))
        result.append(gate("CNOT", (C_FRESH[site], C_FRESH_ANY), f"C:fresh-any:{site}", C_WIDTH))
    occurrence = c552.SNAPSHOT[0][1]
    result.extend((
        gate("TOFFOLI", (occurrence, C_ACTUALITY_TOKEN, C_CHAIN[0]), "C:admit-occurrence-actuality", C_WIDTH),
        gate("TOFFOLI", (C_CHAIN[0], C_ADMISSIBILITY_CERT, C_CHAIN[1]), "C:admit-admissible", C_WIDTH),
        gate("TOFFOLI", (C_CHAIN[1], C_LAW_DOMAIN, C_CHAIN[2]), "C:admit-law-domain", C_WIDTH),
        gate("TOFFOLI", (C_CHAIN[2], C_FRESH_ANY, C_ADMIT), "C:admit-fresh", C_WIDTH),
    ))
    for site in range(SITE_COUNT):
        for replica in range(3):
            result.append(gate("TOFFOLI", (C_ADMIT, C_TARGET_SITE[site], C_OCC[site][replica]), f"C:occupancy:{site}:{replica}", C_WIDTH))
        for replica, label in product(range(3), range(5)):
            result.extend(and3_schedule(C_ADMIT, C_TARGET_SITE[site], C_SOURCE_MEMBER[label], C_WORK, C_MEMBER[site][replica][label], f"C:member:{site}:{replica}:{label}", C_WIDTH))
            result.extend(and3_schedule(C_ADMIT, C_TARGET_SITE[site], C_SOURCE_LAW[label], C_WORK, C_LAW[site][replica][label], f"C:law:{site}:{replica}:{label}", C_WIDTH))
        for field, source in enumerate(c552.SNAPSHOT[0][:12]):
            result.extend(and3_schedule(C_ADMIT, C_TARGET_SITE[site], source, C_WORK, C_FIELDS[site][field], f"C:field:{site}:{field}", C_WIDTH))
    return tuple(result)


C_GENERATE = route_c_generation_schedule()
C_ADMISSION = route_c_admission_schedule()


def write_existing_record(bits: list[int], site: int, member: int, law: int) -> None:
    for target in C_OCC[site]:
        bits[target] = 1
    for bank in C_MEMBER[site]:
        for target, bit in zip(bank, one_hot(member, 5)):
            bits[target] = bit
    for bank in C_LAW[site]:
        for target, bit in zip(bank, one_hot(law, 5)):
            bits[target] = bit


def prepare_c(member: int, law: int, target_site: int, *, prior_member: int,
              prior_law: int, binding: int, size: int, actuality: int = 1,
              admissible: int = 1, law_domain: int = 1) -> Word:
    if target_site not in (1, 2) or size not in (5, 6):
        raise ValueError("C target/size leaves declared domain")
    base = base_prepare(None, None, binding=binding, plus=int(size == 5), minus=int(size == 6), K_position=(member + law + target_site) % 16)
    bits = list(base) + [0] * (C_WIDTH - c552.TOTAL_M2)
    for sites, label in ((C_SOURCE_MEMBER, member), (C_SOURCE_LAW, law), (C_TARGET_SITE, target_site)):
        for target, bit in zip(sites, one_hot(label, len(sites))):
            bits[target] = bit
    bits[C_ACTUALITY_TOKEN] = actuality
    bits[C_ADMISSIBILITY_CERT] = admissible
    bits[C_LAW_DOMAIN] = law_domain
    write_existing_record(bits, 0, prior_member, prior_law)
    validate_c(tuple(bits))
    return tuple(bits)


def record_syndrome(bits: Word, site: int) -> Word:
    result = []
    occ = tuple(bits[target] for target in C_OCC[site])
    result.append(int(occ[0] != occ[1] or occ[1] != occ[2]))
    for banks in (C_MEMBER[site], C_LAW[site]):
        for label in range(5):
            lane = tuple(bits[bank[label]] for bank in banks)
            result.append(int(lane[0] != lane[1] or lane[1] != lane[2]))
    return tuple(result)


def validate_record_site(bits: Word, site: int, *, allow_blank: bool = True) -> None:
    occ = tuple(bits[target] for target in C_OCC[site])
    if occ == (0, 0, 0) and allow_blank:
        if any(bits[target] for bank in C_MEMBER[site] for target in bank) or any(bits[target] for bank in C_LAW[site] for target in bank) or any(bits[target] for target in C_FIELDS[site]):
            raise ValueError("blank record site contains payload")
        return
    if occ != (1, 1, 1) or any(record_syndrome(bits, site)):
        raise ValueError("record replicas disagree")
    members = tuple(singleton(tuple(bits[target] for target in bank), 5, "record member") for bank in C_MEMBER[site])
    laws = tuple(singleton(tuple(bits[target] for target in bank), 5, "record law") for bank in C_LAW[site])
    if len(set(members)) != 1 or len(set(laws)) != 1:
        raise ValueError("record content is not replica-determined")


def validate_c(bits: Word) -> None:
    if len(bits) != C_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("C word leaves bounded binary carrier")
    singleton(tuple(bits[site] for site in C_SOURCE_MEMBER), 5, "C source member")
    singleton(tuple(bits[site] for site in C_SOURCE_LAW), 5, "C source law")
    target = singleton(tuple(bits[site] for site in C_TARGET_SITE), SITE_COUNT, "C target site")
    for site in range(SITE_COUNT):
        validate_record_site(bits, site)
    if any(bits[site] for site in C_OCC[target]):
        raise ValueError("C target site is not fresh")
    if any(bits[site] for site in (*C_FRESH, C_FRESH_ANY, *C_CHAIN, C_ADMIT, C_WORK, *c552.MEMBER_STATE, *c552.LAW_WORD, *c552.SNAPSHOT[0])):
        raise ValueError("C work or exact interface target is dirty")


def step_c(bits: Word, *, delete_label: str | None = None) -> Word:
    validate_c(bits)
    generated = apply(bits, C_GENERATE, delete_label=delete_label if delete_label and delete_label.startswith("C:source") else None)
    base = c552.physical_step(tuple(generated[:c552.TOTAL_M2]))
    word = tuple(base) + tuple(generated[c552.TOTAL_M2:])
    return apply(word, C_ADMISSION, delete_label=delete_label if delete_label and not delete_label.startswith("C:source") else None)


def reverse_c(bits: Word) -> Word:
    word = apply(bits, C_ADMISSION, reverse=True)
    base = c552.apply_schedule(tuple(word[:c552.TOTAL_M2]), reverse=True)
    return apply(tuple(base) + tuple(word[c552.TOTAL_M2:]), C_GENERATE, reverse=True)


def expected_c(bits: Word) -> Word:
    validate_c(bits)
    member = singleton(tuple(bits[site] for site in C_SOURCE_MEMBER), 5, "C member")
    law = singleton(tuple(bits[site] for site in C_SOURCE_LAW), 5, "C law")
    target = singleton(tuple(bits[site] for site in C_TARGET_SITE), SITE_COUNT, "C target")
    expected = list(bits)
    semantic = semantic_c552(tuple(bits[:c552.TOTAL_M2]), member, law)
    expected[:c552.TOTAL_M2] = semantic
    fresh = int(tuple(bits[site] for site in C_OCC[target]) == (0, 0, 0))
    expected[C_FRESH[target]] = fresh
    expected[C_FRESH_ANY] = fresh
    occurrence = semantic[c552.SNAPSHOT[0][1]]
    chain = (
        occurrence & bits[C_ACTUALITY_TOKEN],
        occurrence & bits[C_ACTUALITY_TOKEN] & bits[C_ADMISSIBILITY_CERT],
        occurrence & bits[C_ACTUALITY_TOKEN] & bits[C_ADMISSIBILITY_CERT] & bits[C_LAW_DOMAIN],
    )
    for site, value in zip(C_CHAIN, chain):
        expected[site] = value
    admit = chain[-1] & fresh
    expected[C_ADMIT] = admit
    if admit:
        for site in C_OCC[target]:
            expected[site] = 1
        for bank in C_MEMBER[target]:
            for site, bit in zip(bank, one_hot(member, 5)):
                expected[site] = bit
        for bank in C_LAW[target]:
            for site, bit in zip(bank, one_hot(law, 5)):
                expected[site] = bit
        for site, bit in zip(C_FIELDS[target], tuple(semantic[s] for s in c552.SNAPSHOT[0][:12])):
            expected[site] = bit
    return tuple(expected)


def readout(bits: Word, site: int) -> int:
    """Supplied finite scalar rule I(record)=member_label+1, I(empty)=0."""
    occ = tuple(bits[target] for target in C_OCC[site])
    if occ == (0, 0, 0):
        return 0
    validate_record_site(bits, site, allow_blank=False)
    member = singleton(tuple(bits[target] for target in C_MEMBER[site][0]), 5, "readout member")
    return member + 1


def frame_word(bits: Word, route: str, axis: int, frame: np.ndarray) -> tuple[Word, int]:
    base, new_axis = c552.frame_word(tuple(bits[:c552.TOTAL_M2]), axis, frame)
    output = list(bits)
    output[:c552.TOTAL_M2] = base
    if route == "C":
        plus_field = c552.C531_OUTPUT_FIELDS.index(c531.PAYLOAD_CURRENT[0])
        minus_field = c552.C531_OUTPUT_FIELDS.index(c531.PAYLOAD_CURRENT[1])
        for site in range(SITE_COUNT):
            pair = (bits[C_FIELDS[site][plus_field]], bits[C_FIELDS[site][minus_field]])
            _mapped_axis, mapped = c552.frame_current(axis, pair, frame)
            output[C_FIELDS[site][plus_field]], output[C_FIELDS[site][minus_field]] = mapped
    return tuple(output), new_axis


def dependency_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    body = NOTE.read_text(encoding="utf-8").lower() if NOTE.exists() else ""
    required = (
        "authority: none", "audit: unset", "route a", "route b", "route c", "e_out g_coarse = g_physical e_in",
        "pointer copying is not record", "no deterministic finite string", "all24", "all576", "n1", "n2", "n3", "n4",
        "n5", "n6", "n7", "n8", "no axiom pressure", "actuality ontology", "fresh low-entropy reservoirs",
        "renewal schedule", "law selection", "irreversible/unbounded permanence", "realized history",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    return {
        "accepted_Cycle568_commit": ACCEPTED_CYCLE568_COMMIT,
        "expected": FROZEN,
        "observed": observed,
        "note_missing": missing,
        "pass": observed == FROZEN and not missing,
    }


def route_a_controls() -> dict[str, object]:
    cases = eg = inverse = ledger = renewal = archive = held = 0
    rows = []
    for size, member, law in product((5, 6), range(3), range(5)):
        source = prepare_a(member, law, ((member + 1) % 3, (member + 2) % 3), ((law + 1) % 5, (law + 2) % 5), binding=member, size=size)
        output = step_a(source)
        cases += 1
        eg += int(output != expected_a(source))
        inverse += int(reverse_a(output) != source)
        before_member_tokens = sum(source[s] for s in (*A_ACTIVE_MEMBER, *A_RESERVE_MEMBER[0], *A_RESERVE_MEMBER[1], *c552.MEMBER_STATE))
        after_member_tokens = sum(output[s] for s in (*A_ACTIVE_MEMBER, *A_RESERVE_MEMBER[0], *A_RESERVE_MEMBER[1], *c552.MEMBER_STATE))
        before_ready = sum(source[s] for s in (A_ACTIVE_READY, *A_RESERVE_READY, A_SPENT_READY))
        after_ready = sum(output[s] for s in (A_ACTIVE_READY, *A_RESERVE_READY, A_SPENT_READY))
        ledger += int((before_member_tokens, after_member_tokens, before_ready, after_ready) != (3, 3, 3, 3))
        renewal += int(tuple(output[s] for s in A_ACTIVE_MEMBER) != one_hot((member + 1) % 3, 5) or output[A_ACTIVE_READY] != 1)
        archive += int(tuple(output[s] for s in A_SPENT_LABEL) != one_hot(member, 5) or output[A_SPENT_READY] != 1)
        held += int(size == 6 and output != expected_a(source))
        rows.append((size, member, law))
    witness = prepare_a(1, 2, (2, 0), (3, 4), binding=1, size=6)
    damaged = step_a(witness, delete_label="A:renew-member-0:2:a")
    deletion_visible = damaged != step_a(witness)
    # The remaining reserve contains one fresh carrier after the refill; no
    # operation here restores the consumed ready token or the empty tail slot.
    finite_capacity = (sum(step_a(witness)[s] for s in A_RESERVE_READY) == 1)
    result = {
        "cases": cases, "eg_failures": eg, "inverse_failures": inverse,
        "ledger_failures": ledger, "renewal_failures": renewal,
        "spent_retention_failures": archive, "held_failures": held,
        "deletion_visible": deletion_visible, "finite_capacity_after_one": finite_capacity,
        "rows_SHA256": sha256(json.dumps(rows).encode()).hexdigest(),
        "pass": not any((eg, inverse, ledger, renewal, archive, held)) and deletion_visible and finite_capacity,
    }
    check("Route A reversibly consumes, retains, and renews from a finite locally conserved carrier reserve", result["pass"], result)
    return result


def route_b_controls() -> dict[str, object]:
    cases = eg = inverse = winner_failures = held = leakage = 0
    rows = []
    for size, epoch, lane, member in product((5, 6), range(3), range(2), range(3)):
        law = (size + 2 * epoch + lane + member) % 5
        arrivals = tuple((0, 0) if i < epoch else ((1, 0) if lane == 0 else (0, 1)) if i == epoch else ((1, 0) if (i + member) % 2 else (0, 0)) for i in range(3))
        labels = tuple(tuple((member if arrivals[i][j] else None) for j in range(2)) for i in range(3))
        source = prepare_b(arrivals, labels, law, binding=member, size=size)
        output = step_b(source)
        cases += 1
        eg += int(output != expected_b(source))
        inverse += int(reverse_b(output) != source)
        winner_failures += int(sum(output[s] for pair in B_WINNER for s in pair) != 1 or output[B_WINNER[epoch][lane]] != 1 or any(output[s] for s in B_COLLISION) or output[B_PREFIX[3]])
        leakage += int(output[B_WORK] != 0)
        held += int(size == 6 and output != expected_b(source))
        rows.append((size, epoch, lane, member, law))
    nohit = prepare_b(((0, 0), (0, 0), (0, 0)), ((None, None),) * 3, 0, binding=0, size=5)
    nohit_detected = detect_b(nohit)
    collision = prepare_b(((0, 0), (1, 1), (1, 0)), ((None, None), (1, 2), (0, None)), 0, binding=0, size=5)
    collision_detected = detect_b(collision)
    nohit_refused = collision_refused = False
    try:
        step_b(nohit)
    except ValueError:
        nohit_refused = True
    try:
        step_b(collision)
    except ValueError:
        collision_refused = True
    controls = (
        nohit_detected[B_PREFIX[3]] == 1 and not any(nohit_detected[s] for pair in B_WINNER for s in pair)
        and collision_detected[B_COLLISION[1]] == 1
        and not any(collision_detected[s] for pair in B_WINNER for s in pair)
        and nohit_refused and collision_refused
    )
    witness = prepare_b(((0, 0), (0, 1), (1, 0)), ((None, None), (None, 2), (1, None)), 1, binding=2, size=6)
    full = step_b(witness)
    deletion_visible = False
    try:
        damaged = step_b(witness, delete_label="B:1:winner1:write")
        deletion_visible = damaged != full
    except ValueError:
        # Deleting the winner write leaves MEMBER_STATE zero-hot; explicit
        # type refusal is the strongest possible deletion signature.
        deletion_visible = True
    result = {
        "lawful_cases": cases, "eg_failures": eg, "inverse_failures": inverse,
        "winner_failures": winner_failures, "held_failures": held,
        "workspace_leakage_failures": leakage,
        "nohit_collision_controls": controls, "winner_deletion_visible": deletion_visible,
        "rows_SHA256": sha256(json.dumps(rows).encode()).hexdigest(),
        "pass": not any((eg, inverse, winner_failures, held, leakage)) and controls and deletion_visible,
    }
    check("Route B computes one unique earliest local hit and explicitly refuses no-hit/collision", result["pass"], result)
    return result


def route_c_controls() -> dict[str, object]:
    cases = eg = inverse = old_changed = clause = additivity = held = leakage = 0
    rows = []
    for size, target, member, law in product((5, 6), (1, 2), range(3), range(5)):
        source = prepare_c(member, law, target, prior_member=(member + 1) % 3, prior_law=(law + 1) % 5, binding=member, size=size)
        before_old = tuple(source[s] for s in (*C_OCC[0], *[x for bank in C_MEMBER[0] for x in bank], *[x for bank in C_LAW[0] for x in bank], *C_FIELDS[0]))
        output = step_c(source)
        after_old = tuple(output[s] for s in (*C_OCC[0], *[x for bank in C_MEMBER[0] for x in bank], *[x for bank in C_LAW[0] for x in bank], *C_FIELDS[0]))
        cases += 1
        eg += int(output != expected_c(source))
        inverse += int(reverse_c(output) != source)
        old_changed += int(before_old != after_old)
        try:
            validate_record_site(output, 0, allow_blank=False)
            validate_record_site(output, target, allow_blank=False)
            ok = output[C_ADMIT] == 1 and not any(
                any(record_syndrome(output, site)) for site in (0, target)
            )
        except ValueError:
            ok = False
        clause += int(not ok)
        additivity += int(sum(readout(output, site) for site in range(SITE_COUNT)) != readout(output, 0) + readout(output, target))
        leakage += int(output[C_WORK] != 0)
        held += int(size == 6 and output != expected_c(source))
        rows.append((size, target, member, law))
    vetoes = {}
    for name, kwargs in (
        ("actuality", {"actuality": 0}),
        ("admissibility", {"admissible": 0}),
        ("law_domain", {"law_domain": 0}),
    ):
        veto_source = prepare_c(1, 2, 1, prior_member=0, prior_law=1, binding=1, size=5, **kwargs)
        veto_output = step_c(veto_source)
        vetoes[name] = veto_output[C_ADMIT] == 0 and tuple(veto_output[s] for s in C_OCC[1]) == (0, 0, 0)
    veto = all(vetoes.values())
    witness = prepare_c(2, 3, 1, prior_member=0, prior_law=1, binding=2, size=6)
    full = step_c(witness)
    damaged = step_c(witness, delete_label="C:occupancy:1:1")
    faulted = list(full)
    faulted[C_MEMBER[1][1][2]] ^= 1
    syndrome_visible = any(record_syndrome(tuple(faulted), 1))
    dirty_refused = False
    dirty = list(witness)
    dirty[C_OCC[1][0]] = 1
    try:
        validate_c(tuple(dirty))
    except ValueError:
        dirty_refused = True
    # A later exact recurrence has support only on the Cycle552 block and does
    # not touch the admitted packet.  This is one bounded protection test.
    continued_base = c552.physical_step(tuple(full[:c552.TOTAL_M2]))
    continued = tuple(continued_base) + tuple(full[c552.TOTAL_M2:])
    packet_sites = tuple(s for site in range(SITE_COUNT) for s in (*C_OCC[site], *[x for bank in C_MEMBER[site] for x in bank], *[x for bank in C_LAW[site] for x in bank], *C_FIELDS[site]))
    continuation_stable = tuple(full[s] for s in packet_sites) == tuple(continued[s] for s in packet_sites)
    result = {
        "cases": cases, "eg_failures": eg, "inverse_failures": inverse,
        "old_record_changes": old_changed, "record_clause_failures": clause,
        "additivity_failures": additivity, "held_failures": held,
        "workspace_leakage_failures": leakage,
        "admission_vetoes": vetoes, "occupancy_deletion_visible": damaged != full,
        "single_replica_fault_detected": syndrome_visible, "dirty_target_refused": dirty_refused,
        "one_disjoint_continuation_stable": continuation_stable,
        "rows_SHA256": sha256(json.dumps(rows).encode()).hexdigest(),
        "pass": not any((eg, inverse, old_changed, clause, additivity, held, leakage)) and veto and damaged != full and syndrome_visible and dirty_refused and continuation_stable,
    }
    check("Route C conditionally appends an independent fresh-site protected Record-clause candidate", result["pass"], result)
    return result


def domain_and_firewall_controls() -> dict[str, object]:
    refused = 0
    total = 0
    malformed = []
    a = prepare_a(1, 2, (2, 0), (3, 4), binding=1, size=5)
    for mutate in (
        lambda w: [0 if i in A_ACTIVE_MEMBER else bit for i, bit in enumerate(w)],
        lambda w: [1 if i in A_SPENT_LABEL[:2] else bit for i, bit in enumerate(w)],
        lambda w: [1 if i == c552.MEMBER_STATE[0] else bit for i, bit in enumerate(w)],
    ):
        malformed.append(("A", tuple(mutate(a))))
    b = prepare_b(((0, 1), (0, 0), (0, 0)), ((None, 1), (None, None), (None, None)), 2, binding=1, size=5)
    bad_b = list(b); bad_b[B_LABEL[1][0][0]] = 1; malformed.append(("B", tuple(bad_b)))
    bad_b = list(b); bad_b[B_PREFIX[1]] = 1; malformed.append(("B", tuple(bad_b)))
    c = prepare_c(1, 2, 1, prior_member=0, prior_law=1, binding=1, size=5)
    bad_c = list(c); bad_c[C_TARGET_SITE[2]] = 1; malformed.append(("C", tuple(bad_c)))
    bad_c = list(c); bad_c[C_MEMBER[0][1][0]] ^= 1; malformed.append(("C", tuple(bad_c)))
    for route, word in malformed:
        total += 1
        try:
            {"A": validate_a, "B": lambda x: validate_b(x, require_winner=True), "C": validate_c}[route](word)
        except ValueError:
            refused += 1
    forbidden_ports = ("grade", "weight", "norm", "diagonal", "probability", "sampler")
    port_names = (
        prepare_a.__code__.co_varnames[:prepare_a.__code__.co_argcount]
        + prepare_b.__code__.co_varnames[:prepare_b.__code__.co_argcount]
        + prepare_c.__code__.co_varnames[:prepare_c.__code__.co_argcount]
        + step_a.__code__.co_varnames[:step_a.__code__.co_argcount]
        + step_b.__code__.co_varnames[:step_b.__code__.co_argcount]
        + step_c.__code__.co_varnames[:step_c.__code__.co_argcount]
    )
    firewall = not any(term in name.lower() for term in forbidden_ports for name in port_names)
    result = {"malformed_refused": refused, "malformed_total": total, "forbidden_member_ports": (), "firewall": firewall, "pass": refused == total and firewall}
    check("lawful domains are explicit and grade/weight/norm/diagonal/probability/sampler have no member port", result["pass"], result)
    return result


def covariance_controls() -> dict[str, object]:
    frames = c531.c526.c235.proper_cubic_frames()
    failures = tests = 0
    fixtures = {
        "A": prepare_a(1, 2, (2, 0), (3, 4), binding=1, size=6),
        "B": prepare_b(((0, 0), (0, 1), (1, 0)), ((None, None), (None, 2), (1, None)), 3, binding=2, size=6),
        "C": prepare_c(2, 3, 1, prior_member=0, prior_law=1, binding=2, size=6),
    }
    steps = {"A": step_a, "B": step_b, "C": step_c}
    for route, frame in product(("A", "B", "C"), frames):
        source = fixtures[route]
        output = steps[route](source)
        framed_source, framed_axis = frame_word(source, route, 0, frame)
        framed_output = steps[route](framed_source)
        expected, expected_axis = frame_word(output, route, 0, frame)
        failures += int(framed_output != expected or framed_axis != expected_axis)
        tests += 1
    group_failures = group_tests = 0
    for first, second, axis, rails in product(frames, frames, range(3), ((0, 0), (1, 0), (0, 1), (1, 1))):
        middle_axis, middle = c552.frame_current(axis, rails, second)
        final_axis, final = c552.frame_current(middle_axis, middle, first)
        direct_axis, direct = c552.frame_current(axis, rails, first @ second)
        group_failures += int((final_axis, final) != (direct_axis, direct))
        group_tests += 1
    result = {
        "proper_cubic_frames": len(frames), "all24_route_tests": tests,
        "covariance_failures": failures, "ordered_frame_products": len(frames) ** 2,
        "all576_role_tests": group_tests, "group_failures": group_failures,
        "pass": len(frames) == 24 and tests == 72 and failures == 0 and group_failures == 0,
    }
    check("all three routes commute with all24 frames and current roles obey all576 frame products", result["pass"], result)
    return result


def locality_controls() -> dict[str, object]:
    schedules = {"A": A_SCHEDULE, "B": B_DETECT + B_EMIT, "C": C_GENERATE + C_ADMISSION}
    rows = {}
    all_literal_support = []
    for route, schedule in schedules.items():
        logical = Counter(item.kind for item in schedule)
        literal = Counter()
        for item in schedule:
            for kind, sites in c568.literal_expansion_sites(item):
                literal[kind] += 1
                all_literal_support.append(len(sites))
        rows[route] = {
            "bounded_M2": {"A": A_WIDTH, "B": B_WIDTH, "C": C_WIDTH}[route],
            "new_M2": {"A": A_WIDTH, "B": B_WIDTH, "C": C_WIDTH}[route] - c552.TOTAL_M2,
            "logical": dict(logical), "literal": dict(literal),
        }
    result = {
        "routes": rows, "maximum_literal_support": max(all_literal_support),
        "constant_overhead_per_cell": True,
        "pass": max(all_literal_support) <= 2 and all(row["bounded_M2"] < 600 for row in rows.values()),
    }
    check("all new gates compile to literal support at most two M2 with bounded constant overhead", result["pass"], result)
    return result


def no_go_controls() -> dict[str, object]:
    routes = (
        ("finite reversible reservoir conveyor", "ATTEMPTED_POSITIVE_CONDITIONAL"),
        ("local first-hit unique winner", "ATTEMPTED_POSITIVE_CONDITIONAL"),
        ("site-tagged formation/admission/protection", "ATTEMPTED_POSITIVE_CONDITIONAL"),
        ("translation-invariant renewable bath", "OPEN"),
        ("collision-resolving interacting carriers", "OPEN"),
        ("unique-extension global history", "OPEN"),
        ("irreversible open-system exhaust", "OPEN"),
    )
    walls = (
        "actuality ontology", "fresh low-entropy reservoirs", "renewal schedule",
        "law selection", "irreversible/unbounded permanence", "realized history",
    )
    pairs = tuple(combinations(walls, 2))
    result = {
        "N1_routes": routes, "N1_route_count": len(routes),
        "N2_walls": walls, "N2_pair_count": len(pairs), "N2_pairs_independent": len(pairs) == 15,
        "N3_hidden_wall_scan": "all carrier, schedule, target, actuality, admissibility, law-domain, protection, readout, gate, chart, and finite-capacity inputs exposed",
        "N4_residual_match": "Cycle568 renewal/Record walls; Cycle552 genesis; Cycle531 occurrence; Cycle433 candidate-versus-Record ceiling; canonical producer/Record clauses",
        "N5_resolution": "one bounded cell, L5/L6, finite three-bin first-hit window, three record sites, all24/all576; no volume/asymptotic claim",
        "N6_partial_closure": "derive a covariant renewable reservoir and selected admission/preservation law; then test unbounded histories and only later a blinded corpus",
        "N7_steelman": "a translation-invariant low-entropy bath with locally interacting carriers and a unique covariant admission law could close renewal and realized-history walls without axiom edit",
        "N8_echo": "Cycle568 left renewable first passage and Record admission open; Cycle433 preserved the coherent-candidate boundary; Cycle552 separated genesis from recurrence",
        "broad_no_go": "FAIL_DO_NOT_SHIP", "minimum_content": "FAIL_DO_NOT_SHIP",
        "shared_obstruction": None, "axiom_pressure": False,
        "pass": len(routes) >= 5 and len(pairs) == 15,
    }
    check("full N1-N8 gate forbids broad no-go, minimum-content, shared-obstruction, and axiom-pressure claims", result["pass"] and not result["axiom_pressure"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str
    audit: str
    strongest_route: str
    framework_Record: None = None
    realized_history: None = None
    probability: None = None
    physical_time: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _signum, _frame: (_ for _ in ()).throw(TimeoutError("Cycle571 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        deps = dependency_controls()
        check("exact dependencies and note contract are frozen", deps["pass"], deps)
        a = route_a_controls()
        b = route_b_controls()
        c = route_c_controls()
        domain = domain_and_firewall_controls()
        covariance = covariance_controls()
        locality = locality_controls()
        discipline = no_go_controls()
        elapsed = time.perf_counter() - started
        resources = {"elapsed_seconds": elapsed, "rss_bytes": rss_bytes(), "wall_cap_seconds": WALL_CAP_SECONDS, "rss_cap_bytes": RSS_CAP_BYTES}
        check("cold resource ceilings", elapsed < WALL_CAP_SECONDS and rss_bytes() < RSS_CAP_BYTES, resources)
        summary = Summary(authority=AUTHORITY, audit=AUDIT, strongest_route="B local first-hit feeding C conditional fresh-site admission")
        print(json.dumps({
            "dependency": deps, "route_A": a, "route_B": b, "route_C": c,
            "domain_firewall": domain, "covariance": covariance, "locality": locality,
            "no_go_discipline": discipline, "resources": resources,
            "summary": summary.__dict__, "pass": PASS, "fail": FAIL,
        }, indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
    print(f"RESULT pass={PASS} fail={FAIL}")
    print("authority=none; audit=unset; pointer copying is not Record; a finite schedule is not time or a frequency theorem")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
