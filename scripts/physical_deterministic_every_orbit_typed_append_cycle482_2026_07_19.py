#!/usr/bin/env python3
"""Cycle 482: deterministic-every-orbit typed append from Cycle443 packets.

One fixed, program-free reversible update acts on a declared basis-orbit code:
an admitted Cycle443 packet tape, a one-hot frontier, blank typed archive slots,
and blank work.  Every lawful basis state has one successor.  At each step the
frontier packet is copied into the frontier archive slot, occupancy/type/lock
triples are written, and the frontier advances.  The same update repeats for
the finite capacity horizon.

This is a bounded deterministic typed-append theorem, not an unconditional
framework Record theorem.  Basis-orbit preparation, the type-code meaning,
the update cadence, finite blanks, and capacity are explicit imports.  A
coherent superposition of lawful basis orbits remains coherent, the full map
has an exact inverse, and forced evolution past the capacity horizon overwrites
the finite archive.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
from hashlib import sha256
from math import sqrt
from pathlib import Path
import inspect
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_delayed_dependency_admission_latch_cycle443_2026_07_19 as c443
import physical_record_actualization_law_program_tournament_cycle449_2026_07_19 as c449


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DETERMINISTIC_EVERY_ORBIT_TYPED_APPEND_CYCLE482_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
FROZEN_C443_SHA256 = "febfa320e566db01c50abd482352b6573daf6780a18414bef83a6529e960112b"
FROZEN_C449_SHA256 = "857febfb57c7b82559465ab0623ef15b5c392b87ceb323340e007c228df442ad"
WORD = c443.WORD
ADMISSION_BITS = c443.OUTPUT_BITS
TYPE_CODE = (1, 1, 1)
LOCK_CODE = (1, 1, 1)
OCCUPIED_CODE = (1, 1, 1)
TOL = 1e-12
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 2 * 1024**3
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    result = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return result


# One translation-equivalent cell.  Cell-local registers occupy a vertical
# line, while HEAD sites at local coordinate zero form a horizontal NN rail.
_cursor = [0]
HEAD = take(_cursor, 1)[0]
CANDIDATE = take(_cursor, WORD)
ADMISSION = take(_cursor, ADMISSION_BITS)
ARCHIVE_WORD = take(_cursor, WORD)
ARCHIVE_OCCUPANCY = take(_cursor, 3)
ARCHIVE_TYPE = take(_cursor, 3)
ARCHIVE_LOCK = take(_cursor, 3)
ADMISSION_PREFIX = take(_cursor, ADMISSION_BITS)
ACCEPT_PREFIX = take(_cursor, 2)
WORK_LOCAL = ADMISSION_PREFIX + ACCEPT_PREFIX
ARCHIVE_LOCAL = ARCHIVE_WORD + ARCHIVE_OCCUPANCY + ARCHIVE_TYPE + ARCHIVE_LOCK
CELL_M2 = _cursor[0]


@dataclass(frozen=True)
class CandidatePacket:
    word: Word
    admission: Word
    source: str


@dataclass(frozen=True)
class BasisState:
    capacity: int
    bits: Word


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class GateTrace:
    logical_gates: int
    nearest_neighbor_primitives: int
    maximum_support: int
    connected_failures: int
    sha256: str


@dataclass(frozen=True)
class ArchiveView:
    word: Word
    occupancy: Word
    type_code: Word
    lock_code: Word

    def typed(self) -> bool:
        return (
            self.occupancy == OCCUPIED_CODE
            and self.type_code == TYPE_CODE
            and self.lock_code == LOCK_CODE
        )


@dataclass(frozen=True)
class DeterministicTypedAppend:
    cell: int
    content: Word
    type_code: Word
    lock_code: Word
    unique_successor: bool
    physical_archive_mutation: bool
    framework_Record: bool = False
    boundary: str = "bounded basis-orbit typed append; finite reversible history, not framework permanence"


StateVector = dict[Word, complex]


class WallCapExceeded(RuntimeError):
    pass


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def note_contracts() -> None:
    required = (
        "authority: none", "audit: unset", "exact target contract",
        "actual cycle-443 admitted candidate", "deterministic every-orbit",
        "one fixed bounded local physical update", "no law-program register",
        "no host law choice, occurrence bit, reset, consume, or realized-member query",
        "unique typed append transition", "repeatable protected continuation",
        "train l=3 and held l=6", "all 24 proper-cubic frames",
        "exact e/g and inverse", "nearest-neighbour m2 manifest",
        "finite no-overwrite is not unbounded permanence",
        "a reversible pointer or hidden environment is not a record",
        "norm is not probability", "initial-state / blank / environment imports",
        "gate disposition: fail", "partial-attempt-with-named-untested-routes",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
        "supplied / derived / open",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle482 note freezes the deterministic-orbit target and semantic boundary", not missing, missing)

    c443_body = normalized(c443.NOTE)
    c449_body = normalized(c449.NOTE)
    c443_sha = file_sha256(Path(c443.__file__))
    c449_sha = file_sha256(Path(c449.__file__))
    check(
        "the direct Cycle443 admitted-candidate and Cycle449 reversible-precommit inputs retain their exact source boundaries",
        c443_sha == FROZEN_C443_SHA256
        and c449_sha == FROZEN_C449_SHA256
        and "branch-relative admitted record candidate" in c443_body
        and "exact inverse retains both detectors" in c443_body
        and "physical outputs are reversible precommit packets, not records" in c449_body
        and "every-orbit deterministic history law — untested" in c449_body,
        {
            "Cycle443": {"role": "direct input", "runner_sha256": c443_sha},
            "Cycle449": {"role": "direct input", "runner_sha256": c449_sha},
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def site(cell: int, local_index: int) -> int:
    return cell * CELL_M2 + local_index


def field(cell: int, local_indices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(site(cell, index) for index in local_indices)


def head_sites(capacity: int) -> tuple[int, ...]:
    return tuple(site(cell, HEAD) for cell in range(capacity))


def is_word(value: object, width: int) -> bool:
    return (
        isinstance(value, tuple)
        and len(value) == width
        and all(isinstance(bit, int) and not isinstance(bit, bool) and bit in (0, 1) for bit in value)
    )


def selected(bits: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def replace_selected(bits: list[int], sites: tuple[int, ...], values: Word) -> None:
    if len(sites) != len(values):
        raise ValueError("field width mismatch")
    for index, value in zip(sites, values):
        bits[index] = value


def validate_candidate(packet: CandidatePacket) -> None:
    if not isinstance(packet, CandidatePacket):
        raise TypeError("deterministic tape entry requires CandidatePacket")
    if not is_word(packet.word, WORD) or not is_word(packet.admission, ADMISSION_BITS):
        raise ValueError("candidate packet is outside the protected binary domain")
    if packet.word[:3] != OCCUPIED_CODE or packet.admission != (1,) * ADMISSION_BITS:
        raise ValueError("the deterministic-orbit code admits only Cycle443 admitted packets")


@lru_cache(maxsize=None)
def actual_cycle443_candidate(case_name: str, copy: int) -> CandidatePacket:
    case = next(item for item in c443.CASES if item.name == case_name)
    _, child, admission, _ = c443.basis_pipeline(case, 1, 1)
    return CandidatePacket(
        c443.word_from_register(child), admission.bits(),
        f"actual Cycle443 {case_name} detector-11 basis orbit apparatus copy {copy}",
    )


def archive_view(state: BasisState, cell: int) -> ArchiveView:
    return ArchiveView(
        selected(state.bits, field(cell, ARCHIVE_WORD)),
        selected(state.bits, field(cell, ARCHIVE_OCCUPANCY)),
        selected(state.bits, field(cell, ARCHIVE_TYPE)),
        selected(state.bits, field(cell, ARCHIVE_LOCK)),
    )


def candidate_view(state: BasisState, cell: int) -> CandidatePacket:
    return CandidatePacket(
        selected(state.bits, field(cell, CANDIDATE)),
        selected(state.bits, field(cell, ADMISSION)),
        f"state cell {cell}",
    )


def frontier(state: BasisState) -> int:
    heads = selected(state.bits, head_sites(state.capacity))
    if sum(heads) != 1:
        raise ValueError("frontier rail is not one-hot")
    return heads.index(1)


def validate_basis(
    state: BasisState,
    *,
    require_step_code: bool = True,
    require_blank_work: bool = True,
) -> None:
    if (
        not isinstance(state, BasisState)
        or state.capacity < 2
        or not is_word(state.bits, state.capacity * CELL_M2)
    ):
        raise ValueError("Cycle482 state has the wrong bounded binary M2 domain")
    for cell in range(state.capacity):
        validate_candidate(candidate_view(state, cell))
    head = frontier(state)
    if require_blank_work and any(
        state.bits[index]
        for cell in range(state.capacity)
        for index in field(cell, WORK_LOCAL)
    ):
        raise ValueError("deterministic append work M2 must enter blank")
    typed = []
    for cell in range(state.capacity):
        view = archive_view(state, cell)
        flags = (view.occupancy, view.type_code, view.lock_code)
        if all(item == (0, 0, 0) for item in flags):
            if any(view.word):
                raise ValueError("blank archive flags carry a dirty word")
            typed.append(False)
        elif all(item == (1, 1, 1) for item in flags):
            typed.append(True)
        else:
            raise ValueError("archive occupancy/type/lock triples are malformed")
    if require_step_code:
        expected = tuple(cell < head for cell in range(state.capacity))
        if tuple(typed) != expected:
            raise ValueError("archive prefix and one-hot frontier are outside the lawful pre-horizon code")


def prepare(candidates: tuple[CandidatePacket, ...]) -> BasisState:
    if not isinstance(candidates, tuple) or len(candidates) < 2:
        raise ValueError("the deterministic tape requires a finite capacity of at least two")
    for packet in candidates:
        validate_candidate(packet)
    capacity = len(candidates)
    bits = [0] * (capacity * CELL_M2)
    bits[site(0, HEAD)] = 1
    for cell, packet in enumerate(candidates):
        replace_selected(bits, field(cell, CANDIDATE), packet.word)
        replace_selected(bits, field(cell, ADMISSION), packet.admission)
    state = BasisState(capacity, tuple(bits))
    validate_basis(state)
    return state


def gate(capacity: int, kind: str, sites: tuple[int, ...], label: str) -> Gate:
    widths = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in widths or len(sites) != widths[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle482 gate")
    if any(index not in range(capacity * CELL_M2) for index in sites):
        raise ValueError("Cycle482 gate leaves its bounded M2 strip")
    return Gate(kind, sites, label)


def append_prefix(
    capacity: int,
    gates: list[Gate],
    conditions: tuple[int, ...],
    work: tuple[int, ...],
    label: str,
) -> tuple[Gate, ...]:
    if len(conditions) != len(work) or not conditions:
        raise ValueError("prefix work does not match conditions")
    start = len(gates)
    gates.append(gate(capacity, "CNOT", (conditions[0], work[0]), f"{label}:0"))
    for lane in range(1, len(conditions)):
        gates.append(
            gate(capacity, "TOFFOLI", (work[lane - 1], conditions[lane], work[lane]), f"{label}:{lane}")
        )
    return tuple(gates[start:])


@lru_cache(maxsize=None)
def fixed_schedule(capacity: int) -> tuple[Gate, ...]:
    if capacity < 2:
        raise ValueError("capacity must be at least two")
    gates: list[Gate] = []
    for cell in range(capacity):
        admission_compute = append_prefix(
            capacity, gates, field(cell, ADMISSION), field(cell, ADMISSION_PREFIX),
            f"cell:{cell}:admission-prefix",
        )
        accept_compute = append_prefix(
            capacity, gates,
            (site(cell, HEAD), site(cell, ADMISSION_PREFIX[-1])),
            field(cell, ACCEPT_PREFIX), f"cell:{cell}:accept",
        )
        accept = site(cell, ACCEPT_PREFIX[-1])
        for lane, (source, target) in enumerate(zip(field(cell, CANDIDATE), field(cell, ARCHIVE_WORD))):
            gates.append(gate(capacity, "TOFFOLI", (accept, source, target), f"cell:{cell}:packet-write:{lane}"))
        for name, targets in (
            ("occupancy", field(cell, ARCHIVE_OCCUPANCY)),
            ("type", field(cell, ARCHIVE_TYPE)),
            ("lock", field(cell, ARCHIVE_LOCK)),
        ):
            for lane, target in enumerate(targets):
                gates.append(gate(capacity, "CNOT", (accept, target), f"cell:{cell}:{name}-write:{lane}"))
        gates.extend(
            Gate(item.kind, item.sites, f"{item.label}:uncompute")
            for item in reversed(accept_compute)
        )
        gates.extend(
            Gate(item.kind, item.sites, f"{item.label}:uncompute")
            for item in reversed(admission_compute)
        )

    # One deterministic cyclic permutation of the horizontal one-hot frontier
    # rail.  Each standard SWAP is three adjacent CNOTs.
    heads = head_sites(capacity)
    for right in reversed(range(1, capacity)):
        left = right - 1
        a, b = heads[left], heads[right]
        gates.extend((
            gate(capacity, "CNOT", (a, b), f"head-rotate:{left}:{right}:0"),
            gate(capacity, "CNOT", (b, a), f"head-rotate:{left}:{right}:1"),
            gate(capacity, "CNOT", (a, b), f"head-rotate:{left}:{right}:2"),
        ))
    return tuple(gates)


def schedule_with_deletion(capacity: int, delete_label: str | None = None) -> tuple[Gate, ...]:
    schedule = fixed_schedule(capacity)
    if delete_label is None:
        return schedule
    matches = tuple(
        index for index, item in enumerate(schedule)
        if item.label in (delete_label, f"{delete_label}:uncompute")
    )
    if len(matches) not in (1, 2):
        raise ValueError("deletion label must identify one write gate or one compute/uncompute prefix lane")
    removed = set(matches)
    return tuple(item for index, item in enumerate(schedule) if index not in removed)


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites
        bits[target] ^= bits[first] & bits[second]
    else:
        raise ValueError("unknown Cycle482 primitive")


def apply_permutation(
    state: BasisState,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
    require_step_code: bool = True,
) -> BasisState:
    validate_basis(
        state,
        require_step_code=require_step_code if not reverse else False,
    )
    bits = list(state.bits)
    schedule = schedule_with_deletion(state.capacity, delete_label)
    for item in reversed(schedule) if reverse else schedule:
        apply_gate(bits, item)
    return BasisState(state.capacity, tuple(bits))


def coarse_step(state: BasisState) -> BasisState:
    validate_basis(state)
    cell = frontier(state)
    bits = list(state.bits)
    packet = candidate_view(state, cell)
    for target, value in zip(field(cell, ARCHIVE_WORD), packet.word):
        bits[target] ^= value
    for target in field(cell, ARCHIVE_OCCUPANCY) + field(cell, ARCHIVE_TYPE) + field(cell, ARCHIVE_LOCK):
        bits[target] ^= 1
    heads = list(selected(bits, head_sites(state.capacity)))
    heads = (heads[-1], *heads[:-1])
    replace_selected(bits, head_sites(state.capacity), tuple(heads))
    return BasisState(state.capacity, tuple(bits))


def append_witness(before: BasisState, after: BasisState) -> DeterministicTypedAppend | None:
    cell = frontier(before)
    expected = coarse_step(before)
    view = archive_view(after, cell)
    unchanged = all(
        archive_view(before, other) == archive_view(after, other)
        for other in range(before.capacity) if other != cell
    )
    if after != expected or not view.typed() or view.word != candidate_view(before, cell).word or not unchanged:
        return None
    return DeterministicTypedAppend(cell, view.word, view.type_code, view.lock_code, True, True)


def manifest(capacity: int) -> tuple[Coord, ...]:
    return tuple((cell, local_index, 0) for cell in range(capacity) for local_index in range(CELL_M2))


def route_for_gate(item: Gate) -> tuple[tuple[int, int], ...]:
    cells = {index // CELL_M2 for index in item.sites}
    if len(cells) != 1:
        return ()
    cell = cells.pop()
    labels = list(range(CELL_M2))
    local_sites = tuple(index - cell * CELL_M2 for index in item.sites)
    targets = tuple(range(CELL_M2 - len(local_sites), CELL_M2))
    swaps: list[tuple[int, int]] = []
    for desired, target in zip(reversed(local_sites), reversed(targets)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("cell right-edge routing invariant failed")
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((site(cell, position), site(cell, position + 1)))
            position += 1
    if tuple(labels[index] for index in targets) != local_sites:
        raise RuntimeError("cell routed operand order is not exact")
    return tuple(swaps)


@lru_cache(maxsize=None)
def nn_trace(capacity: int) -> GateTrace:
    digest = sha256(f"Cycle482 {capacity}-cell vertical-strip router v1".encode())
    primitives = failures = maximum_support = 0
    coords = manifest(capacity)
    for item in fixed_schedule(capacity):
        swaps = route_for_gate(item)
        if swaps:
            primitives += 1 + 6 * len(swaps)
            failures += sum(int(sum(abs(a - b) for a, b in zip(coords[left], coords[right])) != 1) for left, right in swaps)
            cell = item.sites[0] // CELL_M2
            targets = tuple(site(cell, CELL_M2 - len(item.sites) + lane) for lane in range(len(item.sites)))
            failures += int(any(
                sum(abs(a - b) for a, b in zip(coords[left], coords[right])) != 1
                for left, right in zip(targets, targets[1:])
            ))
        else:
            primitives += 1
            failures += int(any(
                sum(abs(a - b) for a, b in zip(coords[left], coords[right])) != 1
                for left, right in zip(item.sites, item.sites[1:])
            ))
        maximum_support = max(maximum_support, len(item.sites))
        digest.update(f"{item.kind}:{item.sites}:{item.label}:{len(swaps)}".encode())
    return GateTrace(len(fixed_schedule(capacity)), primitives, maximum_support, failures, digest.hexdigest())


def apply_nearest_neighbor(state: BasisState) -> BasisState:
    validate_basis(state)
    bits = list(state.bits)
    for item in fixed_schedule(state.capacity):
        swaps = route_for_gate(item)
        if not swaps:
            apply_gate(bits, item)
            continue
        for left, right in swaps:
            bits[left], bits[right] = bits[right], bits[left]
        cell = item.sites[0] // CELL_M2
        width = len(item.sites)
        targets = tuple(site(cell, CELL_M2 - width + lane) for lane in range(width))
        apply_gate(bits, Gate(item.kind, targets, item.label))
        for left, right in reversed(swaps):
            bits[left], bits[right] = bits[right], bits[left]
    return BasisState(state.capacity, tuple(bits))


def actual_tape(case_name: str, capacity: int) -> tuple[CandidatePacket, ...]:
    return tuple(actual_cycle443_candidate(case_name, copy) for copy in range(capacity))


def bridge_inverse_nn_controls() -> None:
    print("\nDETERMINISTIC TYPED APPEND / EXACT E-G / INVERSE / NN")
    rows = []
    for case in c443.CASES:
        state = prepare(actual_tape(case.name, case.length))
        physical = apply_permutation(state)
        coarse = coarse_step(state)
        recovered = apply_permutation(physical, reverse=True)
        witness = append_witness(state, physical)
        rows.append({
            "case": case.name, "held": case.held, "capacity": case.length,
            "E_G_exact": physical == coarse,
            "inverse_exact": recovered == state,
            "unique_successors": 1,
            "append_witness": witness,
            "work_leakage": sum(physical.bits[index] for cell in range(case.length) for index in field(cell, WORK_LOCAL)),
            "candidate_tape_retained": all(candidate_view(physical, cell).word == candidate_view(state, cell).word for cell in range(case.length)),
        })
    held = prepare(actual_tape("held_L6", 6))
    held_nn = apply_nearest_neighbor(held)
    held_logical = apply_permutation(held)
    check(
        "one program-free update gives every train/held basis-orbit input one typed append successor with exact E/G, inverse, and NN realization",
        len(rows) == 2
        and all(
            row["E_G_exact"] and row["inverse_exact"] and row["unique_successors"] == 1
            and isinstance(row["append_witness"], DeterministicTypedAppend)
            and row["append_witness"].framework_Record is False
            and row["work_leakage"] == 0 and row["candidate_tape_retained"]
            for row in rows
        )
        and held_nn == held_logical
        and nn_trace(3).connected_failures == nn_trace(6).connected_failures == 0
        and nn_trace(3).maximum_support == nn_trace(6).maximum_support == 3,
        {"rows": rows, "held_NN_matches_logical": held_nn == held_logical,
         "train_trace": nn_trace(3), "held_trace": nn_trace(6)},
    )


def every_candidate_lane_and_fixed_law_controls() -> None:
    print("\nEVERY LAWFUL PACKET LANE / FIXED-LAW STATIC CERTIFICATE")
    base = actual_cycle443_candidate("held_L6", 0)
    variants = [base]
    for lane in range(3, WORD):
        word = list(base.word)
        word[lane] ^= 1
        variants.append(CandidatePacket(tuple(word), base.admission, f"parametric lane {lane} complement"))
    failures = 0
    values_by_lane = {lane: set() for lane in range(WORD)}
    for packet in variants:
        state = prepare((packet, packet, packet))
        moved = apply_permutation(state)
        witness = append_witness(state, moved)
        failures += int(witness is None or witness.content != packet.word)
        for lane, value in enumerate(packet.word):
            values_by_lane[lane].add(value)
    schedule = fixed_schedule(6)
    packet_writes = tuple(item for item in schedule if ":packet-write:" in item.label)
    flag_writes = tuple(item for item in schedule if any(tag in item.label for tag in (":occupancy-write:", ":type-write:", ":lock-write:")))
    nominal_source = inspect.getsource(apply_permutation).lower() + inspect.getsource(fixed_schedule).lower()
    forbidden_controls = tuple(token for token in (
        "law_program", "occurrence_bit", "consume", "reset_gate", "realized_member_query"
    ) if token in nominal_source)
    check(
        "the bitwise schedule is parametric over every protected content lane and contains one fixed law with no hidden selection control",
        failures == 0
        and all(values_by_lane[lane] == {0, 1} for lane in range(3, WORD))
        and all(values_by_lane[lane] == {1} for lane in range(3))
        and len(packet_writes) == 6 * WORD
        and len(flag_writes) == 6 * 9
        and not forbidden_controls,
        {
            "tested_lawful_packet_variants": len(variants),
            "parametric_nonoccupancy_lanes_with_both_values": sum(values_by_lane[lane] == {0, 1} for lane in range(3, WORD)),
            "static_packet_write_gates": len(packet_writes),
            "static_type_occupancy_lock_writes": len(flag_writes),
            "nominal_forbidden_control_tokens": forbidden_controls,
            "law_program_M2": 0, "successor_outdegree_on_declared_basis_code": 1,
        },
    )


def repeated_continuation_and_horizon_controls() -> None:
    print("\nREPEATABLE PROTECTED CONTINUATION / FINITE HORIZON")
    rows = []
    for case in c443.CASES:
        initial = prepare(actual_tape(case.name, case.length))
        state = initial
        step_rows = []
        for step in range(case.length):
            before = state
            state = apply_permutation(state)
            witness = append_witness(before, state)
            previous_preserved = all(
                archive_view(state, earlier).typed()
                and archive_view(state, earlier).word == candidate_view(initial, earlier).word
                for earlier in range(step + 1)
            )
            later_blank = all(not any(archive_view(state, later).word) for later in range(step + 1, case.length))
            inverse_exact = apply_permutation(state, reverse=True) == before
            step_rows.append((step, witness is not None, previous_preserved, later_blank, inverse_exact))
        terminal = state
        all_typed = all(
            archive_view(terminal, cell).typed()
            and archive_view(terminal, cell).word == candidate_view(initial, cell).word
            for cell in range(case.length)
        )
        forced = terminal
        for _ in range(case.length):
            forced = apply_permutation(forced, require_step_code=False)
        rows.append({
            "case": case.name, "capacity_horizon": case.length,
            "step_rows": step_rows, "all_slots_typed_at_horizon": all_typed,
            "forced_second_lap_recurs_to_initial": forced == initial,
            "finite_no_overwrite_through_horizon": all_typed,
            "unbounded_permanence_claimed": False,
        })
    check(
        "the same update repeats through train/held capacity while preserving every prior append, and forced post-horizon recurrence exposes the permanence limit",
        all(
            all(all(item[1:]) for item in row["step_rows"])
            and row["all_slots_typed_at_horizon"]
            and row["forced_second_lap_recurs_to_initial"]
            and row["finite_no_overwrite_through_horizon"]
            and not row["unbounded_permanence_claimed"]
            for row in rows
        ),
        rows,
    )


def semantic_discriminator_controls() -> None:
    print("\nSEMANTIC DISCRIMINATOR: PRECOMMIT MENU VS UNIQUE APPEND ORBIT")
    packets449 = c449.packet_sets("held_L6")["three_agree"]
    precommit_signatures = {
        c449.precommit_view(
            c449.apply_logical(c449.prepare(packets449, program, migration_token=1))
        ).signature()
        for program in c449.PROGRAMS.values()
    }
    initial = prepare(actual_tape("held_L6", 6))
    output = apply_permutation(initial)
    witness = append_witness(initial, output)
    check(
        "Cycle482 replaces Cycle449's three supplied program-relative ready sectors by one physical typed-archive mutation on every declared basis orbit",
        len(precommit_signatures) == 3
        and isinstance(witness, DeterministicTypedAppend)
        and witness.unique_successor and witness.physical_archive_mutation
        and witness.type_code == TYPE_CODE and witness.lock_code == LOCK_CODE
        and witness.framework_Record is False
        and selected(initial.bits, head_sites(6)) == (1, 0, 0, 0, 0, 0)
        and selected(output.bits, head_sites(6)) == (0, 1, 0, 0, 0, 0),
        {
            "Cycle449_distinct_program_relative_precommit_signatures": len(precommit_signatures),
            "Cycle482_law_program_M2": 0,
            "Cycle482_successors_per_lawful_basis_state": 1,
            "Cycle482_witness": witness,
            "difference_from_ready_precommit": "archive content plus occupancy/type/lock mutate on every lawful orbit",
            "framework_Record_claimed": False,
        },
    )


def transform_state(state: StateVector, capacity: int, *, reverse: bool = False) -> StateVector:
    output: StateVector = {}
    for bits, amplitude in state.items():
        moved = apply_permutation(BasisState(capacity, bits), reverse=reverse).bits
        output[moved] = output.get(moved, 0j) + amplitude
    return {bits: amplitude for bits, amplitude in output.items() if abs(amplitude) > 1e-15}


def vector_residual(left: StateVector, right: StateVector) -> float:
    keys = left.keys() | right.keys()
    return sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys))


def coherent_boundary_controls() -> None:
    print("\nCOHERENT-ORBIT BOUNDARY / NO MEMBER SELECTION")
    base = actual_cycle443_candidate("held_L6", 0)
    word = list(base.word)
    word[24] ^= 1
    rival = CandidatePacket(tuple(word), base.admission, "lawful rival basis orbit")
    left = prepare((base, base, base))
    right = prepare((rival, rival, rival))
    amplitude = 1 / sqrt(2)
    initial = {left.bits: amplitude + 0j, right.bits: 1j * amplitude}
    output = transform_state(initial, 3)
    recovered = transform_state(output, 3, reverse=True)
    norm = sum(abs(value) ** 2 for value in output.values())
    check(
        "the deterministic map gives one successor per basis orbit but retains a coherent two-orbit input rather than querying or selecting a realized member",
        len(output) == 2 and abs(norm - 1) < TOL
        and vector_residual(recovered, initial) < TOL
        and all(archive_view(BasisState(3, bits), 0).typed() for bits in output),
        {
            "coherent_output_branches": len(output), "norm": norm,
            "inverse_residual": vector_residual(recovered, initial),
            "selected_realized_member": None, "norm_interpreted_as_probability": False,
        },
    )


def deletion_and_malformed_controls() -> None:
    print("\nLOAD-BEARING DELETIONS / MALFORMED DOMAIN")
    initial = prepare(actual_tape("held_L6", 6))
    base_packet = candidate_view(initial, 0)
    payload_lane = next(lane for lane in range(24, 54) if base_packet.word[lane])
    rows = []
    for name, label, predicate in (
        ("admission-prefix", "cell:0:admission-prefix:5", lambda moved: not archive_view(moved, 0).typed()),
        ("accept-prefix", "cell:0:accept:1", lambda moved: not archive_view(moved, 0).typed()),
        ("packet-copy", f"cell:0:packet-write:{payload_lane}", lambda moved: archive_view(moved, 0).word != base_packet.word),
        ("type-lane", "cell:0:type-write:0", lambda moved: archive_view(moved, 0).type_code != TYPE_CODE),
        ("lock-lane", "cell:0:lock-write:0", lambda moved: archive_view(moved, 0).lock_code != LOCK_CODE),
        ("head-rail", "head-rotate:0:1:0", lambda moved: sum(selected(moved.bits, head_sites(6))) != 1),
    ):
        moved = apply_permutation(initial, delete_label=label)
        rows.append((name, label, predicate(moved), sum(moved.bits[index] for cell in range(6) for index in field(cell, WORK_LOCAL))))

    refusals = []
    short = CandidatePacket((1,) * (WORD - 1), (1,) * ADMISSION_BITS, "short")
    unready = replace(actual_cycle443_candidate("held_L6", 0), admission=(1,) * 11 + (0,))
    bad_occupancy = replace(actual_cycle443_candidate("held_L6", 0), word=(0,) + actual_cycle443_candidate("held_L6", 0).word[1:])
    actions = (
        lambda: prepare((short, short)),
        lambda: prepare((unready, unready)),
        lambda: prepare((bad_occupancy, bad_occupancy)),
    )
    for action in actions:
        try:
            action()
            refusals.append(False)
        except (TypeError, ValueError):
            refusals.append(True)
    zero_head = list(initial.bits)
    zero_head[site(0, HEAD)] = 0
    two_head = list(initial.bits)
    two_head[site(1, HEAD)] = 1
    dirty_work = list(initial.bits)
    dirty_work[site(0, WORK_LOCAL[0])] = 1
    dirty_archive = list(initial.bits)
    dirty_archive[site(0, ARCHIVE_WORD[24])] = 1
    for bits in (zero_head, two_head, dirty_work, dirty_archive):
        try:
            validate_basis(BasisState(6, tuple(bits)))
            refusals.append(False)
        except ValueError:
            refusals.append(True)
    check(
        "admission, accept, packet, type, lock, and head gates are load-bearing, while malformed and dirty domains are refused",
        all(visible and leakage == 0 for _, _, visible, leakage in rows)
        and len(refusals) == 7 and all(refusals),
        {"deletions": rows, "malformed_dirty_refusals": refusals},
    )


def rotated_case(case: c443.PipelineCase, frame: np.ndarray) -> tuple[c443.PipelineCase, c443.c433.Layout]:
    fixture, mapping, failures = c443.c364.c342.mapped_fixture(case.parent.fixture, frame)
    if failures:
        raise RuntimeError("Cycle482 payload-frame mapping failed")
    moved = c443.PipelineCase(
        case.name, case.length, case.held,
        c443.rotated_formation_case(case.parent, frame, fixture, mapping),
        c443.rotated_formation_case(case.child, frame, fixture, mapping),
        c443.rotated_formation_case(case.downstream, frame, fixture, mapping),
    )
    return moved, c443.c433.rotated_layout(c443.c433.LAYOUT, frame)


def proper_cubic_covariance_controls() -> None:
    print("\nALL-24 PROPER-CUBIC COVARIANCE")
    frames = c443.c364.c362.c353.proper_cubic_frames()
    rows = []
    failures = 0
    for frame_index, frame in enumerate(frames):
        for case in c443.CASES:
            coords = tuple(c443.c364.c362.c353.rotated(coord, frame) for coord in manifest(case.length))
            unique = len(set(coords)) == case.length * CELL_M2
            vertical = all(
                sum(abs(a - b) for a, b in zip(coords[site(cell, lane)], coords[site(cell, lane + 1)])) == 1
                for cell in range(case.length) for lane in range(CELL_M2 - 1)
            )
            horizontal = all(
                sum(abs(a - b) for a, b in zip(coords[site(cell, HEAD)], coords[site(cell + 1, HEAD)])) == 1
                for cell in range(case.length - 1)
            )
            moved, layout = rotated_case(case, frame)
            _, child, admission, _ = c443.basis_pipeline(moved, 1, 1, layout=layout)
            packet = CandidatePacket(c443.word_from_register(child), admission.bits(), f"frame {frame_index}")
            initial = prepare(tuple(packet for _ in range(case.length)))
            output = apply_permutation(initial)
            witness = append_witness(initial, output)
            exact = (
                unique and vertical and horizontal
                and witness is not None and witness.content == packet.word
                and nn_trace(case.length).connected_failures == 0
            )
            failures += int(not exact)
            rows.append((frame_index, case.name, case.held, exact))
    check(
        "the actual Cycle443 producer, vertical cell strips, horizontal frontier rail, and fixed append update form an all-24 proper-cubic family",
        len(frames) == 24 and len(rows) == 48 and failures == 0,
        {"proper_cubic_frames": len(frames), "train_held_rows": len(rows),
         "failures": failures, "manifest": "H x 194 M2 cubic strip; vertical cell corridors plus horizontal head rail"},
    )


def resource_supply_boundary_controls(started: float) -> None:
    print("\nRESOURCE / INITIAL-STATE / BLANK / ENVIRONMENT / CLAIM BOUNDARY")
    traces = {capacity: nn_trace(capacity) for capacity in (3, 6)}
    supplied = (
        "one definite basis-orbit tape of admitted Cycle443 packets; Cycle443 does not select this tape from a coherent detector state",
        "one one-hot frontier initialized at cell zero and one external application cadence for the fixed update",
        "H blank 79-M2 archive words plus H blank occupancy/type/lock triples",
        "14 clean reversible prefix M2 per cell",
        "the meanings of the 111 occupied, typed, and locked codes",
        "finite capacity H, bounded strip geometry, and carried all-24 frame family",
        "no environment M2 in the reversible route and no hidden discarded output",
    )
    derived = (
        "one successor per lawful basis state under one fixed program-free gate schedule",
        "frontier packet copied into a literal physical archive bank with occupancy/type/lock triples",
        "one-site frontier advance and H-step protected prefix continuation",
        "exact inverse and explicit forced post-horizon recurrence",
    )
    open_items = (
        "physical selection or derivation of one definite Cycle443 basis-orbit tape from coherent detector output",
        "identification of the local 111 type code with the framework Record type rather than a declared finite code",
        "unbounded or renewable capacity and permanence beyond H",
        "autonomous proposal/payload genesis, fault tolerance, and homogeneous infinite-lattice scheduling",
        "probability, Born weights, frequencies, and a realized empirical corpus",
    )
    elapsed = time.monotonic() - started
    maxrss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    nominal_source = inspect.getsource(apply_permutation).lower() + inspect.getsource(fixed_schedule).lower()
    check(
        "Cycle482 inventories the complete finite M2 compiler and every initial-state, blank, environment, semantic, and permanence import",
        CELL_M2 == 194
        and traces[3].logical_gates == 354 and traces[6].logical_gates == 711
        and all(trace.maximum_support == 3 and trace.connected_failures == 0 for trace in traces.values())
        and all(token not in nominal_source for token in (
            "law_program", "occurrence_bit", "consume", "reset_gate", "realized_member_query"
        ))
        and AUTHORITY == "none" and AUDIT == "unset"
        and elapsed < WALL_CAP_SECONDS and maxrss < RSS_CAP_BYTES,
        {
            "cell_M2": CELL_M2,
            "candidate_plus_admission_M2_per_cell": WORD + ADMISSION_BITS,
            "frontier_M2_per_cell": 1,
            "blank_archive_M2_per_cell": len(ARCHIVE_LOCAL),
            "blank_work_M2_per_cell": len(WORK_LOCAL),
            "train_total_M2": 3 * CELL_M2, "held_total_M2": 6 * CELL_M2,
            "traces": traces, "maximum_primitive_support_M2": 3,
            "environment_M2": 0, "discarded_outputs": 0,
            "permanence_horizon_steps": {"train": 3, "held": 6},
            "elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
            "raw_maxrss_Darwin_bytes": maxrss, "RSS_cap_bytes": RSS_CAP_BYTES,
            "supplied": supplied, "derived": derived, "open": open_items,
            "candidate_pointer_or_environment_called_Record": False,
            "finite_no_overwrite_called_unbounded_permanence": False,
            "authority": AUTHORITY, "audit": AUDIT,
        },
    )


def _wall_alarm(_signum, _frame):
    raise WallCapExceeded(f"Cycle482 exceeded its {WALL_CAP_SECONDS:g}-second wall cap")


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    signal.signal(signal.SIGALRM, _wall_alarm)
    signal.setitimer(signal.ITIMER_REAL, WALL_CAP_SECONDS)
    try:
        note_contracts()
        bridge_inverse_nn_controls()
        every_candidate_lane_and_fixed_law_controls()
        repeated_continuation_and_horizon_controls()
        semantic_discriminator_controls()
        coherent_boundary_controls()
        deletion_and_malformed_controls()
        proper_cubic_covariance_controls()
        resource_supply_boundary_controls(started)
    except WallCapExceeded as error:
        check("the Cycle482 runner remains inside its declared wall cap", False, str(error))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY")
    print({
        "result": "bounded deterministic every-basis-orbit typed append with H-step protected continuation",
        "difference_from_Cycle449": "one program-free typed archive mutation, not one of three ready/precommit sectors",
        "framework_Record_derived": False,
        "basis_orbit_initial_member_supplied": True,
        "unbounded_permanence_derived": False,
        "no_go_gate": "FAIL; partial-attempt-with-named-untested-routes",
        "authority": AUTHORITY, "audit": AUDIT,
    })
    print(f"\nFINAL {PASS} pass / {FAIL} fail")
    return int(bool(FAIL))


if __name__ == "__main__":
    raise SystemExit(main())
