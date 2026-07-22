#!/usr/bin/env python3
"""Cycle592: preregistered innovation/member/Record-frequency tournament.

The candidate transition table, three quantum inputs, entropy word, and held
sizes are literal pre-data constants.  Physical source functions have no
grade/probability/sampler port.  Candidate grades are computed independently
and compared only after the local histories are formed.
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
import physical_autonomous_occurrence_born_history_bridge_tournament_cycle587_2026_07_22 as c587


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PREREGISTERED_INNOVATION_RECORD_FREQUENCY_BRIDGE_TOURNAMENT_CYCLE592_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0
Word = tuple[int, ...]
Gate = c587.Gate


FROZEN_PATHS = {
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
    "Cycle587 runner": ROOT / "scripts/physical_autonomous_occurrence_born_history_bridge_tournament_cycle587_2026_07_22.py",
}
FROZEN = {
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
    "Cycle587 runner": "2879d5a2641b334553769f15cf3a6f152f9f16f8f80b23db723448533c28c494",
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
        raise ValueError("label leaves one-hot domain")
    return tuple(int(index == label) for index in range(width))


def singleton(bits: Word, name: str) -> int:
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits) or sum(bits) != 1:
        raise ValueError(f"{name} is not a binary one-hot word")
    return bits.index(1)


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    answer = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return answer


# ---------------------------------------------------------------------------
# Preregistered data.  These are literal candidate-law inputs, not values fit
# from the generated corpus.  Program 0 is the Cycle41 cluster fixture;
# programs 1 and 2 are held biased inputs.
# ---------------------------------------------------------------------------
PROGRAM_NAMES = ("cluster_uniform_train", "computational_000_held", "left_3to1_bias_held")
HISTORY_TABLE = (
    (0, 3, 5, 6, 0, 3, 5, 6),
    (0, 4, 0, 4, 0, 4, 0, 4),
    (0, 0, 0, 2, 4, 4, 4, 6),
)
MEMBER_TABLE = (
    (0, 1, 2, 3, 0, 1, 2, 3),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (0, 0, 0, 1, 2, 2, 2, 3),
)
INNOVATION_WORD = (
    7, 0, 5, 2, 1, 6, 3, 4,
    2, 5, 0, 7, 4, 1, 6, 3,
    4, 3, 6, 1, 0, 7, 2, 5,
    1, 6, 3, 4, 5, 2, 7, 0,
    5, 2, 7, 0, 3, 4, 1, 6,
    0, 7, 4, 3, 6, 1, 5, 2,
    6, 1, 2, 5, 7, 0, 4, 3,
    3, 4, 1, 6, 2, 5, 0, 7,
)
CORPUS_SIZES = (32, 40, 56)
TRAIN_HELD = ("train", "held", "held")
PREREGISTRATION = {
    "program_names": PROGRAM_NAMES,
    "history_table": HISTORY_TABLE,
    "member_table": MEMBER_TABLE,
    "innovation_word": INNOVATION_WORD,
    "corpus_sizes": CORPUS_SIZES,
    "train_held": TRAIN_HELD,
    "address_candidate_law": "one supplied objective innovation address with candidate mass 1/8 on each of eight labels",
    "deterministic_extension": "u_(n+1)=u_n+3 mod 8 from supplied u_0=0",
}
PREREGISTRATION_SHA256 = sha256(json.dumps(PREREGISTRATION, sort_keys=True).encode()).hexdigest()
EXPECTED_PREREGISTRATION_SHA256 = "e2412661758ab9c7b2d36f0a1f5c9151453253429a0be796f29357bd770894ca"


def input_states() -> tuple[np.ndarray, ...]:
    left_bias = np.asarray((np.sqrt(3.0) / 2.0, 0.5), dtype=complex)
    return (
        c577.CLUSTER.copy(),
        c577.ket(0, 8),
        c577.kron_all(left_bias.reshape(-1, 1), c577.ZERO.reshape(-1, 1), c577.ZERO.reshape(-1, 1)).reshape(-1),
    )


def independent_grade_vector(state: np.ndarray) -> np.ndarray:
    if state.shape != (8,) or abs(float(np.vdot(state, state).real) - 1.0) > TOL:
        raise ValueError("input leaves normalized three-M2 pure-state domain")
    return np.asarray(tuple(
        float(np.vdot(c577.HISTORY_P[history] @ state, c577.HISTORY_P[history] @ state).real)
        for history in c577.HISTORIES
    ))


def table_grade(program: int) -> np.ndarray:
    if program not in range(3):
        raise ValueError("program leaves preregistered table")
    return np.asarray(tuple(HISTORY_TABLE[program].count(history) / 8.0 for history in range(8)))


# ---------------------------------------------------------------------------
# Route A: physical rational-reservoir ROM.  A three-rail input program and an
# eight-rail innovation address read physical one-hot history/member table
# rows.  The selected ready token is debited into a retained spent rail.
# ---------------------------------------------------------------------------
_a = [0]
A_PROGRAM = take(_a, 3)
A_ADDRESS = take(_a, 8)
A_HISTORY_TABLE = tuple(tuple(take(_a, 8) for _ in range(8)) for _ in range(3))
A_MEMBER_TABLE = tuple(tuple(take(_a, 4) for _ in range(8)) for _ in range(3))
A_SELECT = tuple(tuple(take(_a, 1)[0] for _ in range(8)) for _ in range(3))
A_HISTORY = take(_a, 8)
A_MEMBER = take(_a, 4)
A_ARCHIVE_HISTORY = take(_a, 8)
A_ARCHIVE_MEMBER = take(_a, 4)
A_READY = take(_a, 8)
A_SPENT = take(_a, 8)
A_WIDTH = _a[0]


def route_a_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for program, address in product(range(3), range(8)):
        selected = A_SELECT[program][address]
        gates.append(Gate("TOFFOLI", (A_PROGRAM[program], A_ADDRESS[address], selected), f"A:select:{program}:{address}"))
        for history in range(8):
            gates.append(Gate("TOFFOLI", (selected, A_HISTORY_TABLE[program][address][history], A_HISTORY[history]), f"A:history:{program}:{address}:{history}"))
        for member in range(4):
            gates.append(Gate("TOFFOLI", (selected, A_MEMBER_TABLE[program][address][member], A_MEMBER[member]), f"A:member:{program}:{address}:{member}"))
    for source, target in zip(A_HISTORY, A_ARCHIVE_HISTORY):
        gates.append(Gate("CNOT", (source, target), f"A:archive-history:{source}"))
    for source, target in zip(A_MEMBER, A_ARCHIVE_MEMBER):
        gates.append(Gate("CNOT", (source, target), f"A:archive-member:{source}"))
    for address in range(8):
        gates.extend((
            Gate("CNOT", (A_SPENT[address], A_READY[address]), f"A:debit:{address}:pre"),
            Gate("TOFFOLI", (A_ADDRESS[address], A_READY[address], A_SPENT[address]), f"A:debit:{address}:core"),
            Gate("CNOT", (A_SPENT[address], A_READY[address]), f"A:debit:{address}:post"),
        ))
    for program, address in reversed(tuple(product(range(3), range(8)))):
        gates.append(Gate("TOFFOLI", (A_PROGRAM[program], A_ADDRESS[address], A_SELECT[program][address]), f"A:unselect:{program}:{address}"))
    return tuple(gates)


A_SCHEDULE = route_a_schedule()


def prepare_a(program: int, address: int) -> Word:
    if program not in range(3) or address not in range(8):
        raise ValueError("Route A program/address leaves preregistered domain")
    bits = [0] * A_WIDTH
    for site, bit in zip(A_PROGRAM, one_hot(program, 3)):
        bits[site] = bit
    for site, bit in zip(A_ADDRESS, one_hot(address, 8)):
        bits[site] = bit
    for p, a in product(range(3), range(8)):
        for site, bit in zip(A_HISTORY_TABLE[p][a], one_hot(HISTORY_TABLE[p][a], 8)):
            bits[site] = bit
        for site, bit in zip(A_MEMBER_TABLE[p][a], one_hot(MEMBER_TABLE[p][a], 4)):
            bits[site] = bit
    for site in A_READY:
        bits[site] = 1
    return tuple(bits)


def expected_a(program: int, address: int) -> Word:
    bits = list(prepare_a(program, address))
    history, member = HISTORY_TABLE[program][address], MEMBER_TABLE[program][address]
    for sites, label, width in (
        (A_HISTORY, history, 8), (A_ARCHIVE_HISTORY, history, 8),
        (A_MEMBER, member, 4), (A_ARCHIVE_MEMBER, member, 4),
    ):
        for site, bit in zip(sites, one_hot(label, width)):
            bits[site] = bit
    bits[A_READY[address]] = 0
    bits[A_SPENT[address]] = 1
    return tuple(bits)


def physical_innovation_step(source: Word) -> Word:
    """Fixed physical ROM/debit update; intentionally has no grade port."""
    if len(source) != A_WIDTH:
        raise ValueError("Route A word has wrong physical width")
    singleton(tuple(source[s] for s in A_PROGRAM), "A program")
    singleton(tuple(source[s] for s in A_ADDRESS), "A innovation address")
    if any(source[s] for s in (*A_HISTORY, *A_MEMBER, *A_ARCHIVE_HISTORY, *A_ARCHIVE_MEMBER, *[s for row in A_SELECT for s in row], *A_SPENT)):
        raise ValueError("Route A output/work/spent boundary is dirty")
    if any(source[s] != 1 for s in A_READY):
        raise ValueError("Route A rational reservoir is not fresh")
    return c587.apply_schedule(source, A_SCHEDULE)


def route_a_controls() -> dict[str, object]:
    eg_failures = inverse_failures = table_failures = interface_failures = ledger_failures = 0
    rows = 0
    for size, program, address in product((5, 6), range(3), range(8)):
        source = prepare_a(program, address)
        output = physical_innovation_step(source)
        eg_failures += output != expected_a(program, address)
        inverse_failures += c587.apply_schedule(output, A_SCHEDULE, reverse=True) != source
        history = singleton(tuple(output[s] for s in A_HISTORY), "A output history")
        member = singleton(tuple(output[s] for s in A_MEMBER), "A output member")
        table_failures += int((history, member) != (HISTORY_TABLE[program][address], MEMBER_TABLE[program][address]))
        ledger_failures += int(sum(source[s] for s in (*A_READY, *A_SPENT)) != sum(output[s] for s in (*A_READY, *A_SPENT)))
        base = c552.prepare(
            binding=member, law=0, member=member, head=0, edge=1,
            plus=int(size == 5), minus=int(size == 6), K_position=(history + size) % 16,
        )
        stepped = c552.physical_step(base)
        fields, law = c552.snapshot_view(stepped, 0)
        interface_failures += int(fields[:3] != (1, 1, 1) or law != one_hot(0, 5))
        interface_failures += c552.apply_schedule(stepped, reverse=True) != base
        rows += 1

    states = input_states()
    grade_rows = []
    maximum_grade_residual = 0.0
    kernel_stochastic_failures = 0
    for program, state in enumerate(states):
        predicted = independent_grade_vector(state)
        physical = table_grade(program)
        residual = float(np.linalg.norm(predicted - physical, ord=1))
        maximum_grade_residual = max(maximum_grade_residual, residual)
        kernel_stochastic_failures += int(abs(float(physical.sum()) - 1.0) > TOL or float(physical.min()) < -TOL)
        grade_rows.append({"program": program, "name": PROGRAM_NAMES[program], "independent_grade": tuple(float(x) for x in predicted), "table_grade": tuple(float(x) for x in physical), "L1_residual": residual})

    witness = prepare_a(2, 3)
    ideal = physical_innovation_step(witness)
    deleted = c587.apply_schedule(witness, A_SCHEDULE, delete_label="A:member:2:3:1")
    deletion_residual = float(np.linalg.norm(np.asarray(deleted) - np.asarray(ideal)))
    line = c587.static_line_compiler_controls(A_SCHEDULE, A_WIDTH)
    forbidden = ("grade", "weight", "norm", "probability", "sampler", "amplitude", "rho", "state")
    forbidden_ports = tuple(name for name in inspect.signature(physical_innovation_step).parameters if any(token in name.lower() for token in forbidden))
    result = {
        "route": "A physical rational-reservoir grade-table compiler",
        "preregistration_sha256": PREREGISTRATION_SHA256,
        "physical_M2_before_Cycle552": A_WIDTH,
        "bounded_product_envelope_M2": A_WIDTH + c552.TOTAL_M2,
        "L5_held_L6_EG_rows": rows,
        "EG_failures": eg_failures,
        "inverse_failures": inverse_failures,
        "table_history_member_failures": table_failures,
        "exact_Cycle552_531_interface_failures": interface_failures,
        "resource_ledger_failures": ledger_failures,
        "independent_grade_rows": grade_rows,
        "maximum_independent_grade_L1_residual": maximum_grade_residual,
        "candidate_transition_kernel_stochastic_failures": kernel_stochastic_failures,
        "active_member_deletion_residual": deletion_residual,
        "physical_update_forbidden_numeric_or_sampler_ports": forbidden_ports,
        "static_nearest_neighbor_line_compiler": line,
        "coherent_equal_address_input_retains_all_eight_address_output_sectors": True,
        "uniform_objective_address_distribution_derived": False,
        "table_multiplicity_and_candidate_address_law_supplied": True,
        "pass": rows == 48 and not any((eg_failures, inverse_failures, table_failures, interface_failures, ledger_failures))
        and maximum_grade_residual < TOL and kernel_stochastic_failures == 0
        and deletion_residual > TOL and not forbidden_ports and line["pass"],
    }
    check("Route A exactly compiles the preregistered rational grade table into the member/occurrence interface with explicit address-law import", result["pass"], result)
    return result


# ---------------------------------------------------------------------------
# Route B: typed actuality/admissibility/ready inputs write a redundant finite
# append candidate.  Forward re-entry is refused, but the physical inverse is
# retained and exact; this is not irreversible Record formation.
# ---------------------------------------------------------------------------
_b = [0]
B_HISTORY = take(_b, 8)
B_MEMBER = take(_b, 4)
B_ACTUALITY = take(_b, 1)[0]
B_ADMISSIBLE = take(_b, 1)[0]
B_READY = take(_b, 1)[0]
B_SPENT = take(_b, 1)[0]
B_WORK = take(_b, 1)[0]
B_ADMIT = take(_b, 1)[0]
B_LOCK = take(_b, 1)[0]
B_OCCUPANCY = take(_b, 3)
B_HISTORY_REPLICA = tuple(take(_b, 8) for _ in range(3))
B_MEMBER_REPLICA = tuple(take(_b, 4) for _ in range(3))
B_WIDTH = _b[0]


def route_b_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = [
        Gate("TOFFOLI", (B_ACTUALITY, B_ADMISSIBLE, B_WORK), "B:predicate"),
        Gate("TOFFOLI", (B_WORK, B_READY, B_ADMIT), "B:admit"),
    ]
    for target in (*B_OCCUPANCY, B_LOCK):
        gates.append(Gate("CNOT", (B_ADMIT, target), f"B:status:{target}"))
    for replica, history in product(range(3), range(8)):
        gates.append(Gate("TOFFOLI", (B_ADMIT, B_HISTORY[history], B_HISTORY_REPLICA[replica][history]), f"B:history:{replica}:{history}"))
    for replica, member in product(range(3), range(4)):
        gates.append(Gate("TOFFOLI", (B_ADMIT, B_MEMBER[member], B_MEMBER_REPLICA[replica][member]), f"B:member:{replica}:{member}"))
    gates.extend((
        Gate("CNOT", (B_SPENT, B_READY), "B:debit:pre"),
        Gate("TOFFOLI", (B_ADMIT, B_READY, B_SPENT), "B:debit:core"),
        Gate("CNOT", (B_SPENT, B_READY), "B:debit:post"),
        Gate("TOFFOLI", (B_ACTUALITY, B_ADMISSIBLE, B_WORK), "B:unpredicate"),
    ))
    return tuple(gates)


B_SCHEDULE = route_b_schedule()


def prepare_b(history: int, member: int, *, actuality: int = 1, admissible: int = 1) -> Word:
    if history not in range(8) or member not in range(4) or actuality not in (0, 1) or admissible not in (0, 1):
        raise ValueError("Route B input leaves typed domain")
    bits = [0] * B_WIDTH
    for site, bit in zip(B_HISTORY, one_hot(history, 8)):
        bits[site] = bit
    for site, bit in zip(B_MEMBER, one_hot(member, 4)):
        bits[site] = bit
    bits[B_ACTUALITY], bits[B_ADMISSIBLE], bits[B_READY] = actuality, admissible, 1
    return tuple(bits)


def validate_b_fresh(bits: Word) -> None:
    if len(bits) != B_WIDTH:
        raise ValueError("Route B has wrong physical width")
    singleton(tuple(bits[s] for s in B_HISTORY), "B history")
    singleton(tuple(bits[s] for s in B_MEMBER), "B member")
    if bits[B_READY] != 1 or bits[B_SPENT] != 0:
        raise ValueError("Route B has no fresh admission resource")
    targets = (*B_OCCUPANCY, B_LOCK, B_WORK, B_ADMIT, *[s for row in B_HISTORY_REPLICA for s in row], *[s for row in B_MEMBER_REPLICA for s in row])
    if any(bits[s] for s in targets):
        raise ValueError("Route B target is dirty or re-entered")


def candidate_admission_step(source: Word) -> Word:
    """Supplied candidate admission law; no claim of framework Record."""
    validate_b_fresh(source)
    return c587.apply_schedule(source, B_SCHEDULE)


def route_b_controls() -> dict[str, object]:
    packet_failures = inverse_failures = resource_failures = 0
    rows = 0
    for program, address in product(range(3), range(8)):
        history, member = HISTORY_TABLE[program][address], MEMBER_TABLE[program][address]
        source = prepare_b(history, member)
        output = candidate_admission_step(source)
        expected_h, expected_m = one_hot(history, 8), one_hot(member, 4)
        packet_failures += int(tuple(output[s] for s in B_OCCUPANCY) != (1, 1, 1) or (output[B_LOCK], output[B_ADMIT]) != (1, 1))
        packet_failures += int(any(tuple(output[s] for s in bank) != expected_h for bank in B_HISTORY_REPLICA))
        packet_failures += int(any(tuple(output[s] for s in bank) != expected_m for bank in B_MEMBER_REPLICA))
        resource_failures += int((output[B_READY], output[B_SPENT]) != (0, 1))
        inverse_failures += c587.apply_schedule(output, B_SCHEDULE, reverse=True) != source
        rows += 1

    veto_failures = 0
    for kwargs in ({"actuality": 0}, {"admissible": 0}):
        source = prepare_b(0, 0, **kwargs)
        output = candidate_admission_step(source)
        veto_failures += int(any(output[s] for s in (*B_OCCUPANCY, B_LOCK, B_ADMIT, *[s for row in B_HISTORY_REPLICA for s in row], *[s for row in B_MEMBER_REPLICA for s in row])) or (output[B_READY], output[B_SPENT]) != (1, 0))

    witness = prepare_b(4, 2)
    ideal = candidate_admission_step(witness)
    reentry_refused = False
    try:
        candidate_admission_step(ideal)
    except ValueError:
        reentry_refused = True
    inverse_accessible = c587.apply_schedule(ideal, B_SCHEDULE, reverse=True) == witness
    replica_deleted = c587.apply_schedule(witness, B_SCHEDULE, delete_label="B:history:1:4")
    replica_deletion_residual = float(np.linalg.norm(np.asarray(replica_deleted) - np.asarray(ideal)))
    debit_deleted = c587.apply_schedule(witness, B_SCHEDULE, delete_label="B:debit:core")
    debit_deletion_residual = float(np.linalg.norm(np.asarray(debit_deleted) - np.asarray(ideal)))
    lock_deleted = c587.apply_schedule(witness, B_SCHEDULE, delete_label=f"B:status:{B_LOCK}")
    lock_deletion_residual = float(np.linalg.norm(np.asarray(lock_deleted) - np.asarray(ideal)))
    line = c587.static_line_compiler_controls(B_SCHEDULE, B_WIDTH)

    # The innovation corpus is literal and contains eight copies of every
    # address.  Calling it entropy or actual is supplied candidate semantics.
    innovation_counts = tuple(INNOVATION_WORD.count(address) for address in range(8))
    remaining = set(range(8))
    first_exhausted_repeat_index = None
    for index, address in enumerate(INNOVATION_WORD):
        if address not in remaining:
            first_exhausted_repeat_index = index
            break
        remaining.remove(address)
    result = {
        "route": "B typed innovation plus finite protected-append candidate",
        "physical_M2": B_WIDTH,
        "lawful_rows": rows,
        "packet_failures": packet_failures,
        "inverse_failures": inverse_failures,
        "resource_ledger_failures": resource_failures,
        "actuality_or_admissibility_veto_failures": veto_failures,
        "innovation_word_sha256": sha256(json.dumps(INNOVATION_WORD).encode()).hexdigest(),
        "innovation_address_counts": innovation_counts,
        "finite_eight_address_stock_first_exhausted_repeat_index": first_exhausted_repeat_index,
        "forward_reentry_refused_by_fresh_domain": reentry_refused,
        "exact_physical_inverse_remains_accessible": inverse_accessible,
        "single_replica_deletion_residual": replica_deletion_residual,
        "debit_deletion_residual": debit_deletion_residual,
        "lock_deletion_residual": lock_deletion_residual,
        "static_nearest_neighbor_line_compiler": line,
        "finite_ready_resource_renews": False,
        "actuality_token_and_uniform_innovation_law_supplied": True,
        "candidate_packet_is_framework_Record": False,
        "global_irreversibility_or_permanence_derived": False,
        "pass": rows == 24 and not any((packet_failures, inverse_failures, resource_failures, veto_failures))
        and innovation_counts == (8,) * 8 and first_exhausted_repeat_index == 8
        and reentry_refused and inverse_accessible
        and min(replica_deletion_residual, debit_deletion_residual, lock_deletion_residual) > TOL and line["pass"],
    }
    check("Route B gives a supplied typed innovation/admission candidate with visible debit and reentry-versus-inverse separation", result["pass"], result)
    return result


# ---------------------------------------------------------------------------
# Route C: deterministic unique-extension address head.  The same predeclared
# ROM is used for all programs.  Frequencies are conditional consequences of
# table multiplicity and a supplied head genesis, not stochastic probabilities.
# ---------------------------------------------------------------------------
def deterministic_extension_step(program: int, head: int) -> tuple[int, int, int]:
    """Return history, member, next head; no grade/probability input."""
    if program not in range(3) or head not in range(8):
        raise ValueError("deterministic extension leaves preregistered domain")
    return HISTORY_TABLE[program][head], MEMBER_TABLE[program][head], (head + 3) % 8


def deterministic_corpus(program: int, length: int, *, initial_head: int = 0,
                         suppress_advances: bool = False,
                         table: tuple[tuple[int, ...], ...] = HISTORY_TABLE) -> tuple[int, ...]:
    if program not in range(3) or length < 1 or initial_head not in range(8):
        raise ValueError("deterministic corpus leaves declared domain")
    head = initial_head
    output = []
    for _ in range(length):
        output.append(table[program][head])
        if not suppress_advances:
            head = (head + 3) % 8
    return tuple(output)


def innovation_corpus(program: int, length: int) -> tuple[int, ...]:
    if program not in range(3) or length < 1 or length > len(INNOVATION_WORD):
        raise ValueError("innovation corpus leaves preregistered domain")
    return tuple(HISTORY_TABLE[program][address] for address in INNOVATION_WORD[:length])


def empirical_vector(corpus: tuple[int, ...]) -> np.ndarray:
    return np.asarray(tuple(corpus.count(history) / len(corpus) for history in range(8)))


def route_c_controls() -> dict[str, object]:
    forbidden = ("grade", "weight", "norm", "probability", "sampler", "amplitude", "rho", "state")
    forbidden_ports = tuple(name for name in inspect.signature(deterministic_extension_step).parameters if any(token in name.lower() for token in forbidden))
    rows = []
    innovation_failures = deterministic_failures = 0
    for program, size in enumerate(CORPUS_SIZES):
        predicted = independent_grade_vector(input_states()[program])
        innovation_empirical = empirical_vector(innovation_corpus(program, size))
        deterministic_empirical = empirical_vector(deterministic_corpus(program, size))
        innovation_residual = float(np.linalg.norm(innovation_empirical - predicted, ord=1))
        deterministic_residual = float(np.linalg.norm(deterministic_empirical - predicted, ord=1))
        innovation_failures += innovation_residual > TOL
        deterministic_failures += deterministic_residual > TOL
        rows.append({
            "program": program, "name": PROGRAM_NAMES[program], "split": TRAIN_HELD[program], "size": size,
            "predicted_grade": tuple(float(x) for x in predicted),
            "innovation_frequency": tuple(float(x) for x in innovation_empirical),
            "deterministic_frequency": tuple(float(x) for x in deterministic_empirical),
            "innovation_L1_residual": innovation_residual,
            "deterministic_L1_residual": deterministic_residual,
        })

    # Exact one-step physical comparison: the A ROM with address=head equals
    # the deterministic coarse extension before the adjacent head update.
    eg_failures = inverse_failures = 0
    head_schedule = tuple(
        Gate("SWAP", (right - 1, right), f"C:head:+1:{repetition}:{right}")
        for repetition in range(3) for right in range(7, 0, -1)
    )
    for program, head in product(range(3), range(8)):
        source = prepare_a(program, head)
        output = physical_innovation_step(source)
        history = singleton(tuple(output[s] for s in A_HISTORY), "C physical history")
        member = singleton(tuple(output[s] for s in A_MEMBER), "C physical member")
        coarse_h, coarse_m, next_head = deterministic_extension_step(program, head)
        eg_failures += int((history, member) != (coarse_h, coarse_m))
        head_word = one_hot(head, 8)
        advanced = c587.apply_schedule(head_word, head_schedule)
        eg_failures += int(advanced != one_hot(next_head, 8))
        inverse_failures += int(c587.apply_schedule(advanced, head_schedule, reverse=True) != head_word)

    suppressed = empirical_vector(deterministic_corpus(2, CORPUS_SIZES[2], suppress_advances=True))
    ideal = empirical_vector(deterministic_corpus(2, CORPUS_SIZES[2]))
    head_deletion_residual = float(np.linalg.norm(suppressed - ideal, ord=1))
    reversed_table = tuple(tuple(reversed(row)) for row in HISTORY_TABLE)
    original_string = deterministic_corpus(2, CORPUS_SIZES[2])
    permuted_string = deterministic_corpus(2, CORPUS_SIZES[2], table=reversed_table)
    count_preserving_frequency_residual = float(np.linalg.norm(empirical_vector(original_string) - empirical_vector(permuted_string), ord=1))
    ordered_string_separator = sum(left != right for left, right in zip(original_string, permuted_string))
    genesis_frequency_residual = float(np.linalg.norm(
        empirical_vector(deterministic_corpus(2, CORPUS_SIZES[2], initial_head=0))
        - empirical_vector(deterministic_corpus(2, CORPUS_SIZES[2], initial_head=5)), ord=1,
    ))
    genesis_string_separator = sum(
        left != right for left, right in zip(
            deterministic_corpus(2, CORPUS_SIZES[2], initial_head=0),
            deterministic_corpus(2, CORPUS_SIZES[2], initial_head=5),
        )
    )
    head_line = c587.static_line_compiler_controls(head_schedule, 8)
    result = {
        "route": "C preregistered deterministic unique-extension comparator",
        "preregistration_sha256": PREREGISTRATION_SHA256,
        "expected_preregistration_sha256": EXPECTED_PREREGISTRATION_SHA256,
        "train_held_frequency_rows": rows,
        "innovation_frequency_failures": innovation_failures,
        "deterministic_frequency_failures": deterministic_failures,
        "one_step_physical_EG_failures": eg_failures,
        "head_inverse_failures": inverse_failures,
        "head_advance_deletion_L1_residual": head_deletion_residual,
        "count_preserving_table_permutation_frequency_residual": count_preserving_frequency_residual,
        "count_preserving_table_permutation_ordered_string_separator": ordered_string_separator,
        "different_genesis_same_frequency_residual": genesis_frequency_residual,
        "different_genesis_ordered_string_separator": genesis_string_separator,
        "physical_update_forbidden_numeric_or_sampler_ports": forbidden_ports,
        "head_static_nearest_neighbor_line_compiler": head_line,
        "table_and_initial_head_supplied": True,
        "unique_deterministic_string_is_objective_actuality_or_probability_sample": False,
        "frequency_identifies_microscopic_law_or_genesis": False,
        "pass": not innovation_failures and not deterministic_failures and not eg_failures and not inverse_failures
        and head_deletion_residual > TOL and count_preserving_frequency_residual < TOL and ordered_string_separator > 0
        and genesis_frequency_residual < TOL and genesis_string_separator > 0 and not forbidden_ports and head_line["pass"],
    }
    check("Route C gives preregistered train/two-held grade-frequency equality while counter-controls show frequency does not identify law, genesis, or actuality", result["pass"], result)
    return result


def covariance_domain_controls() -> dict[str, object]:
    frames = c577.c41.proper_cubic_rotations()
    frame_failures = group_failures = tests = 0
    for frame in frames:
        for member in range(4):
            source = c552.prepare(member, 0, member, 0, edge=1, plus=1, minus=0, K_position=member)
            framed, axis = c552.frame_word(source, 0, frame)
            found = c552.physical_step(framed)
            expected, expected_axis = c552.frame_word(c552.physical_step(source), 0, frame)
            frame_failures += int(found != expected or axis != expected_axis)
            tests += 1
    for left, right in product(frames, repeat=2):
        for axis in range(3):
            source = c552.prepare(0, 0, 0, 0, edge=1, plus=1, minus=0, K_position=0)
            _, first_axis = c552.frame_word(source, axis, right)
            _, second_axis = c552.frame_word(source, first_axis, left)
            _, product_axis = c552.frame_word(source, axis, left @ right)
            group_failures += int(second_axis != product_axis)

    malformed_refused = 0
    malformed_total = 7
    for action in (
        lambda: prepare_a(3, 0), lambda: prepare_a(0, 8),
        lambda: prepare_b(8, 0), lambda: prepare_b(0, 4),
        lambda: deterministic_corpus(3, 8), lambda: deterministic_corpus(0, 0),
        lambda: innovation_corpus(0, 65),
    ):
        try:
            action()
        except ValueError:
            malformed_refused += 1
    result = {
        "proper_cubic_frames": len(frames),
        "all24_member_frame_tests": tests,
        "all24_member_frame_failures": frame_failures,
        "all576_axis_product_tests": len(frames) ** 2 * 3,
        "all576_axis_product_failures": group_failures,
        "new_ROM_innovation_archive_fields_are_proper_cubic_scalars": True,
        "malformed_domain_refusals": malformed_refused,
        "malformed_domain_total": malformed_total,
        "pass": len(frames) == 24 and frame_failures == group_failures == 0 and malformed_refused == malformed_total,
    }
    check("all24/all576 covariance and lawful-domain controls are exact", result["pass"], result)
    return result


def dependency_discipline_inventory_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "route a", "route b", "route c",
        "preregister", "uniform", "two biased", "host sampler", "objective actuality",
        "pointer copying is not record", "finite candidate packet is not a framework record",
        "all 24", "all 576", "nearest-neighbor", "l5", "held l6",
        "supplied / derived / open", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8",
        "n1 status: fail", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in normalized)
    declared = re.search(r"Runner SHA-256:\s*([0-9a-f]{64})", note)

    routes = (
        {"family": "rational local reservoir ROM", "status": "ATTEMPTED", "terminal": "derive address innovation distribution and table/grade law rather than supply them"},
        {"family": "typed stochastic innovation/admission", "status": "ATTEMPTED", "terminal": "derive objective entropy innovations, admission law, and noninvertible permanence"},
        {"family": "deterministic unique extension", "status": "ATTEMPTED", "terminal": "derive program/head genesis and explain state-dependent table selection without grade import"},
        {"family": "physical collapse noise field", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "construct covariant noise dynamics and conserved resource ledger"},
        {"family": "typicality/ergodic environment", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "derive invariant measure, mixing, actuality, and Record readout"},
        {"family": "algorithmic unique-history selector", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "derive a local rule that changes with quantum grade without encoding its answer table"},
    )
    walls = (
        "member genesis", "objective actuality", "Record admission/permanence",
        "grade-to-transition-law selection", "frequency calibration/independence", "resource renewal",
    )
    pairs = tuple({"pair": (walls[a], walls[b]), "independent": True, "reason": "the tested closure object for either wall has no typed proof of the other"} for a, b in combinations(range(len(walls)), 2))
    hidden = (
        "three input-state preparations and Cycle41 projector dictionary",
        "literal rational history/member ROM and program labels",
        "candidate uniform 1/8 address law and 64-token balanced innovation word",
        "objective interpretation of one innovation/address token",
        "actuality and admissibility tokens plus fresh blank archive capacity",
        "Cycle552 law/binding/head/current/K inputs",
        "noiseless gate alphabet, static line router, and proper-cubic chart",
        "finite corpus cuts and supplied access restriction after append",
    )
    residuals = (
        {"route": "A", "witness": "zero table/independent-grade residual on three inputs", "matches": "conditional rational kernel compilation; distribution/table law still supplied"},
        {"route": "A coherent", "witness": "eight retained address/output sectors", "matches": "unitary correlation, not objective innovation"},
        {"route": "B", "witness": "forward reentry refused but exact inverse accessible", "matches": "supplied lawful domain, not global irreversibility/permanence"},
        {"route": "C", "witness": "same frequencies under different table order and head genesis", "matches": "frequency agreement does not identify law/genesis/actuality"},
    )
    partial = (
        "retain the exact three-input rational table compiler as a candidate transition-law test bench",
        "retain the typed innovation/admission cell as a finite conditional append with explicit inverse/access boundary",
        "retain deterministic unique extension as a no-sampler comparator, not probability ontology",
        "derive a physical innovation distribution from a separately conserved local bath and preregister it before new held inputs",
        "replace supplied admission/access restriction with a framework-selected formation/permanence law before calling packets Records",
    )
    steelman = {
        "mechanism": "a covariant local bath with a derived stationary eight-address marginal could feed the fixed rational ROM, while a separately selected formation law consumes a nonrecoverable thermodynamic resource and admits readable Records; an input-independent preregistration would then predict blinded frequencies for a larger state family",
        "terminal_obligation": "construct the bath and formation update on physical M2, prove renewal/resource balance and permanence/access restrictions, derive rather than insert the grade-to-ROM relation, and pass held states not used to choose the table denominator or rows",
        "status": "concrete open route; route-independent negative and axiom pressure remain premature",
    }
    echo = (
        "Cycle565 compiled finite grades but had no member port",
        "Cycle571 supplied actuality/admission and retained an invertible finite append",
        "Cycles577-584 retained every coherent pointer sector and finite resource exhaust",
        "Cycle587 matched one uniform deterministic fixture but failed a changed state",
        "Cycle592 repairs that state-dependence conditionally by encoding a supplied three-program rational law and does not promote the import",
    )
    qualifying = tuple(route for route in routes if route["status"] == "ATTEMPTED")
    discipline = {
        "N1_routes": routes, "N1_qualifying": len(qualifying), "N1_required": 5, "N1_status": "FAIL",
        "N2_walls": walls, "N2_pairwise": pairs, "N3_explicit_supplies": hidden,
        "N4_residual_matching": residuals,
        "N5_rhetoric": "candidate transition law, supplied innovation, conditional append, and frequency comparator only; no objective/Record/Born promotion",
        "N6_partial_closure": partial, "N7_hostile_steelman": steelman, "N8_cross_cycle_echo": echo,
        "broad_no_go": "FAIL_DO_NOT_SHIP", "minimum_content": "FAIL_DO_NOT_SHIP",
        "shared_obstruction": "NOT_ESTABLISHED", "axiom_pressure": "NONE",
    }
    result = {
        "expected_hashes": FROZEN,
        "observed_hashes": observed,
        "preregistration_sha256": PREREGISTRATION_SHA256,
        "note_missing_contract_fragments": missing,
        "declared_runner_sha256": declared.group(1) if declared else None,
        "runner_sha256": file_sha(Path(__file__)),
        "discipline": discipline,
        "inventory": {
            "supplied": hidden,
            "derived": (
                "three exact rational table/grade equalities and bounded NN physical member/occurrence compiler",
                "typed finite admission/debit packet with deletion, veto, forward-reentry, and inverse controls",
                "train plus two held frequency equality for supplied innovation and deterministic extension corpora",
                "count-preserving law/genesis separators, all24/all576, and malformed-domain refusals",
            ),
            "open": (
                "derivation of quantum state preparation, grade functional, rational table, and address distribution",
                "objective actuality owner and framework-selected Record formation/permanence/readability",
                "innovation renewal, thermodynamic nonreentry, stationarity/independence, larger held family and asymptotic calibration",
                "physical time, matter-compatible integration, energy/stress/source/gravity and continuum volume",
            ),
        },
        "pass": observed == FROZEN and PREREGISTRATION_SHA256 == EXPECTED_PREREGISTRATION_SHA256
        and not missing and declared is not None and declared.group(1) == file_sha(Path(__file__))
        and len(qualifying) == 3 and len(pairs) == 15 and all(row["independent"] for row in pairs)
        and len(hidden) == 8 and len(residuals) == 4 and len(partial) == 5 and len(echo) == 5,
    }
    check("exact shores, preregistration, supplied inventory, and fresh N1-N8 prevent actuality/Record/Born or axiom-pressure promotion", result["pass"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str = AUTHORITY
    audit: str = AUDIT
    strongest_constructive_result: str = "bounded three-input rational candidate-law compiler into exact Cycle552/531 conditional occurrence with preregistered held equality"
    objective_actuality: None = None
    framework_Record: None = None
    derived_Born_probability: None = None
    innovation_distribution_derived: None = None
    shared_obstruction: None = None
    axiom_pressure: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _s, _f: (_ for _ in ()).throw(TimeoutError("Cycle592 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        route_a = route_a_controls()
        route_b = route_b_controls()
        route_c = route_c_controls()
        covariance = covariance_domain_controls()
        dependency = dependency_discipline_inventory_controls()
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
    print("authority=none; audit=unset; supplied rational/stochastic law is not derived Born probability; conditional append is not Record; reversible sectors are not objective actuality")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
