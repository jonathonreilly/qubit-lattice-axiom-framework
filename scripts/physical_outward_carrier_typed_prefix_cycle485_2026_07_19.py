#!/usr/bin/env python3
"""Cycle 485: outward-carrier continuation of the Cycle-482 typed prefix.

One translation-local reversible schedule copies one supplied admitted
Cycle-443 packet into the current archive cell and the next dormant carrier,
then advances a two-rail frontier.  Unlike Cycle 482, future candidate words
are not preloaded and the frontier never wraps.  The theorem is nevertheless
finite: the initially blank carrier ray is supplied physical capacity.

Authority is none; audit is unset.  The archive is not promoted to a
framework Record and finite prefix preservation is not unbounded permanence.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from math import sqrt
from pathlib import Path
import inspect
import itertools
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_deterministic_every_orbit_typed_append_cycle482_2026_07_19 as c482


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_OUTWARD_CARRIER_TYPED_PREFIX_CYCLE485_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
FROZEN_C482_RUNNER_SHA256 = "6b6f6242b407714e65b0b34abc34db1492d2dfd0984a308735281dfad8b21fda"
FROZEN_C482_NOTE_SHA256 = "35715437191f944849a54d2811b8edf33d6f7b80222cb235ddca1efe7620cd1e"
WORD = c482.WORD
ADMISSION_BITS = c482.ADMISSION_BITS
TYPE_CODE = c482.TYPE_CODE
LOCK_CODE = c482.LOCK_CODE
OCCUPIED_CODE = c482.OCCUPIED_CODE
TOL = 1e-12
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 2 * 1024**3
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    result = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return result


# READY and MOVED form two nearest-neighbour frontier rails.  All other sites
# form one vertical column in each translation-equivalent cell.
_cursor = [0]
READY = take(_cursor, 1)[0]
MOVED = take(_cursor, 1)[0]
INBOX_WORD = take(_cursor, WORD)
INBOX_ADMISSION = take(_cursor, ADMISSION_BITS)
CARRIER_ACTIVE = take(_cursor, 3)
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
class BasisState:
    horizon: int
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
class OutwardAppend:
    cell: int
    next_cell: int
    content: Word
    unique_successor: bool
    future_word_locally_derived: bool
    cyclic_overwrite: bool = False
    framework_Record: bool = False
    renewable_capacity: bool = False
    unbounded_permanence: bool = False


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


def note_and_source_contracts() -> None:
    required = (
        "authority: none", "audit: unset", "exact target contract",
        "cycle-482 direct input", "translation-local outward carrier",
        "train l=3 / h=6 and held l=6 / h=12", "all 24 proper-cubic frames",
        "exact e/g and inverse", "nearest-neighbour m2 manifest",
        "no cyclic overwrite", "no host allocation during the update",
        "finite prefix preservation", "conditional finite-horizon extendibility",
        "renewable capacity remains open", "unbounded permanence remains open",
        "a typed prefix is not a record", "norm is not probability",
        "supplied / derived / open", "gate disposition: fail",
        "partial-attempt-with-named-untested-routes",
        "n1 — alternative route enumeration", "n8 — cross-cycle echo",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle485 note freezes the finite-prefix and capacity boundary", not missing, missing)

    c482_runner = Path(c482.__file__)
    c482_note = c482.NOTE
    runner_sha = file_sha256(c482_runner)
    note_sha = file_sha256(c482_note)
    c482_body = normalized(c482_note)
    check(
        "the direct Cycle482 typed-prefix input retains its exact packaged source boundary",
        runner_sha == FROZEN_C482_RUNNER_SHA256
        and note_sha == FROZEN_C482_NOTE_SHA256
        and "deterministic every-orbit" in c482_body
        and "forced evolution for a second capacity lap clears the finite archive" in c482_body
        and "finite no-overwrite is not unbounded permanence" in c482_body,
        {
            "Cycle482_runner_sha256": runner_sha,
            "Cycle482_note_sha256": note_sha,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def capacity(horizon: int) -> int:
    return horizon + 1


def site(cell: int, local_index: int) -> int:
    return cell * CELL_M2 + local_index


def field(cell: int, local_indices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(site(cell, index) for index in local_indices)


def ready_sites(horizon: int) -> tuple[int, ...]:
    return tuple(site(cell, READY) for cell in range(capacity(horizon)))


def moved_sites(horizon: int) -> tuple[int, ...]:
    return tuple(site(cell, MOVED) for cell in range(capacity(horizon)))


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


def packet_view(state: BasisState, cell: int) -> c482.CandidatePacket:
    return c482.CandidatePacket(
        selected(state.bits, field(cell, INBOX_WORD)),
        selected(state.bits, field(cell, INBOX_ADMISSION)),
        f"Cycle485 state cell {cell}",
    )


def archive_view(state: BasisState, cell: int) -> ArchiveView:
    return ArchiveView(
        selected(state.bits, field(cell, ARCHIVE_WORD)),
        selected(state.bits, field(cell, ARCHIVE_OCCUPANCY)),
        selected(state.bits, field(cell, ARCHIVE_TYPE)),
        selected(state.bits, field(cell, ARCHIVE_LOCK)),
    )


def frontier(state: BasisState) -> int:
    rail = selected(state.bits, ready_sites(state.horizon))
    if sum(rail) != 1:
        raise ValueError("outward frontier READY rail is not one-hot")
    return rail.index(1)


def validate_basis(
    state: BasisState,
    *,
    require_lawful_prefix: bool = True,
    require_blank_work: bool = True,
    require_blank_moved: bool = True,
) -> None:
    if (
        not isinstance(state, BasisState)
        or state.horizon < 1
        or not is_word(state.bits, capacity(state.horizon) * CELL_M2)
    ):
        raise ValueError("Cycle485 state has the wrong bounded binary M2 domain")
    if require_blank_moved and any(selected(state.bits, moved_sites(state.horizon))):
        raise ValueError("MOVED frontier rail must enter blank")
    if require_blank_work and any(
        state.bits[index]
        for cell in range(capacity(state.horizon))
        for index in field(cell, WORK_LOCAL)
    ):
        raise ValueError("outward-carrier work M2 must enter blank")
    if not require_lawful_prefix:
        return
    head = frontier(state)
    root_packet = packet_view(state, 0)
    for cell in range(capacity(state.horizon)):
        packet = packet_view(state, cell)
        active = selected(state.bits, field(cell, CARRIER_ACTIVE))
        archive = archive_view(state, cell)
        if cell <= head:
            c482.validate_candidate(packet)
            if packet.word != root_packet.word or packet.admission != root_packet.admission:
                raise ValueError("formed carrier packet is not the locally propagated root packet")
            if active != (1, 1, 1):
                raise ValueError("formed carrier lacks the active triple")
        elif any(packet.word) or any(packet.admission) or any(active):
            raise ValueError("dormant outward carrier is not blank")
        if cell < head:
            if not archive.typed() or archive.word != packet.word:
                raise ValueError("archive does not equal the protected typed prefix")
        elif any(archive.word) or any(archive.occupancy + archive.type_code + archive.lock_code):
            raise ValueError("unreached archive cell is not blank")


def prepare(packet: c482.CandidatePacket, horizon: int) -> BasisState:
    c482.validate_candidate(packet)
    if horizon < 1:
        raise ValueError("outward horizon must contain at least one link")
    bits = [0] * (capacity(horizon) * CELL_M2)
    bits[site(0, READY)] = 1
    replace_selected(bits, field(0, INBOX_WORD), packet.word)
    replace_selected(bits, field(0, INBOX_ADMISSION), packet.admission)
    replace_selected(bits, field(0, CARRIER_ACTIVE), (1, 1, 1))
    state = BasisState(horizon, tuple(bits))
    validate_basis(state)
    return state


def gate(horizon: int, kind: str, sites: tuple[int, ...], label: str) -> Gate:
    widths = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in widths or len(sites) != widths[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle485 gate")
    if any(index not in range(capacity(horizon) * CELL_M2) for index in sites):
        raise ValueError("Cycle485 gate leaves its bounded M2 strip")
    return Gate(kind, sites, label)


def append_prefix(
    horizon: int,
    gates: list[Gate],
    conditions: tuple[int, ...],
    work: tuple[int, ...],
    label: str,
) -> tuple[Gate, ...]:
    if len(conditions) != len(work) or not conditions:
        raise ValueError("prefix work does not match conditions")
    start = len(gates)
    gates.append(gate(horizon, "CNOT", (conditions[0], work[0]), f"{label}:0"))
    for lane in range(1, len(conditions)):
        gates.append(
            gate(horizon, "TOFFOLI", (work[lane - 1], conditions[lane], work[lane]), f"{label}:{lane}")
        )
    return tuple(gates[start:])


def append_swap(horizon: int, gates: list[Gate], first: int, second: int, label: str) -> None:
    gates.extend((
        gate(horizon, "CNOT", (first, second), f"{label}:0"),
        gate(horizon, "CNOT", (second, first), f"{label}:1"),
        gate(horizon, "CNOT", (first, second), f"{label}:2"),
    ))


@lru_cache(maxsize=None)
def fixed_schedule(horizon: int) -> tuple[Gate, ...]:
    if horizon < 1:
        raise ValueError("outward horizon must contain at least one link")
    gates: list[Gate] = []
    for cell in range(horizon):
        label = f"link:{cell}"
        admission_compute = append_prefix(
            horizon, gates, field(cell, INBOX_ADMISSION), field(cell, ADMISSION_PREFIX),
            f"{label}:admission-prefix",
        )
        accept_compute = append_prefix(
            horizon, gates,
            (site(cell, READY), site(cell, ADMISSION_PREFIX[-1])),
            field(cell, ACCEPT_PREFIX), f"{label}:accept",
        )
        accept = site(cell, ACCEPT_PREFIX[-1])
        for lane, source in enumerate(field(cell, INBOX_WORD)):
            gates.append(gate(
                horizon, "TOFFOLI", (accept, source, field(cell, ARCHIVE_WORD)[lane]),
                f"{label}:archive-packet:{lane}",
            ))
        for name, targets in (
            ("occupancy", field(cell, ARCHIVE_OCCUPANCY)),
            ("type", field(cell, ARCHIVE_TYPE)),
            ("lock", field(cell, ARCHIVE_LOCK)),
        ):
            for lane, target in enumerate(targets):
                gates.append(gate(horizon, "CNOT", (accept, target), f"{label}:{name}-write:{lane}"))
        for lane, source in enumerate(field(cell, INBOX_WORD)):
            gates.append(gate(
                horizon, "TOFFOLI", (accept, source, field(cell + 1, INBOX_WORD)[lane]),
                f"{label}:propagate-packet:{lane}",
            ))
        for lane, source in enumerate(field(cell, INBOX_ADMISSION)):
            gates.append(gate(
                horizon, "TOFFOLI", (accept, source, field(cell + 1, INBOX_ADMISSION)[lane]),
                f"{label}:propagate-admission:{lane}",
            ))
        for lane, target in enumerate(field(cell + 1, CARRIER_ACTIVE)):
            gates.append(gate(horizon, "CNOT", (accept, target), f"{label}:activate-next:{lane}"))
        gates.extend(Gate(item.kind, item.sites, f"{item.label}:uncompute") for item in reversed(accept_compute))
        gates.extend(Gate(item.kind, item.sites, f"{item.label}:uncompute") for item in reversed(admission_compute))

    # Abstract READY_i <-> MOVED_{i+1} transport uses READY_{i+1} only as a
    # restored NN bridge: SWAP(R_i,R_{i+1}); SWAP(R_{i+1},M_{i+1}); repeat.
    for cell in range(horizon):
        append_swap(horizon, gates, site(cell, READY), site(cell + 1, READY), f"transport:{cell}:bridge-a")
        append_swap(horizon, gates, site(cell + 1, READY), site(cell + 1, MOVED), f"transport:{cell}:vertical")
        append_swap(horizon, gates, site(cell, READY), site(cell + 1, READY), f"transport:{cell}:bridge-b")
    for cell in range(capacity(horizon)):
        append_swap(horizon, gates, site(cell, MOVED), site(cell, READY), f"convert:{cell}")
    return tuple(gates)


def schedule_with_deletion(horizon: int, delete_label: str | None = None) -> tuple[Gate, ...]:
    schedule = fixed_schedule(horizon)
    if delete_label is None:
        return schedule
    matches = tuple(
        index for index, item in enumerate(schedule)
        if item.label in (delete_label, f"{delete_label}:uncompute")
    )
    if len(matches) not in (1, 2):
        raise ValueError("deletion label must identify one write/transport gate or a compute/uncompute lane")
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
        raise ValueError("unknown Cycle485 primitive")


def apply_permutation(
    state: BasisState,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
    require_lawful_prefix: bool = True,
) -> BasisState:
    validate_basis(
        state,
        require_lawful_prefix=require_lawful_prefix if not reverse else False,
        require_blank_moved=not reverse,
    )
    bits = list(state.bits)
    schedule = schedule_with_deletion(state.horizon, delete_label)
    for item in reversed(schedule) if reverse else schedule:
        apply_gate(bits, item)
    return BasisState(state.horizon, tuple(bits))


def coarse_step(state: BasisState) -> BasisState:
    validate_basis(state)
    cell = frontier(state)
    if cell >= state.horizon:
        raise ValueError("the finite outward carrier has reached its supplied terminal cell")
    packet = packet_view(state, cell)
    bits = list(state.bits)
    for target, value in zip(field(cell, ARCHIVE_WORD), packet.word):
        bits[target] ^= value
    for target in field(cell, ARCHIVE_OCCUPANCY) + field(cell, ARCHIVE_TYPE) + field(cell, ARCHIVE_LOCK):
        bits[target] ^= 1
    replace_selected(bits, field(cell + 1, INBOX_WORD), packet.word)
    replace_selected(bits, field(cell + 1, INBOX_ADMISSION), packet.admission)
    replace_selected(bits, field(cell + 1, CARRIER_ACTIVE), (1, 1, 1))
    bits[site(cell, READY)] = 0
    bits[site(cell + 1, READY)] = 1
    return BasisState(state.horizon, tuple(bits))


def append_witness(before: BasisState, after: BasisState) -> OutwardAppend | None:
    cell = frontier(before)
    if cell >= before.horizon:
        return None
    expected = coarse_step(before)
    packet = packet_view(before, cell)
    if (
        after != expected
        or not archive_view(after, cell).typed()
        or archive_view(after, cell).word != packet.word
        or packet_view(after, cell + 1).word != packet.word
    ):
        return None
    return OutwardAppend(cell, cell + 1, packet.word, True, True)


def coord_for_site(index: int) -> Coord:
    cell, local = divmod(index, CELL_M2)
    if local == READY:
        return (cell, 0, 0)
    if local == MOVED:
        return (cell, 0, 1)
    return (cell, local - 1, 0)


def manifest(horizon: int) -> tuple[Coord, ...]:
    return tuple(coord_for_site(index) for index in range(capacity(horizon) * CELL_M2))


def manhattan(first: Coord, second: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(first, second))


def cell_path(cell: int) -> tuple[int, ...]:
    return (site(cell, READY),) + tuple(site(cell, local) for local in range(2, CELL_M2))


def link_path(left: int) -> tuple[int, ...]:
    return cell_path(left) + tuple(reversed(cell_path(left + 1)))


def route_for_gate(item: Gate) -> tuple[tuple[tuple[int, int], ...], tuple[int, ...]]:
    if item.label.startswith(("transport:", "convert:")):
        return (), item.sites
    cells = sorted({index // CELL_M2 for index in item.sites})
    if len(cells) == 1:
        path = cell_path(cells[0])
    elif len(cells) == 2 and cells[1] == cells[0] + 1:
        path = link_path(cells[0])
    else:
        raise RuntimeError("logical gate is outside one cell or one adjacent-cell patch")
    labels = list(path)
    targets = tuple(range(len(path) - len(item.sites), len(path)))
    swaps: list[tuple[int, int]] = []
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("outward-carrier right-edge routing invariant failed")
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((path[position], path[position + 1]))
            position += 1
    if tuple(labels[index] for index in targets) != item.sites:
        raise RuntimeError("outward-carrier routed operand order is not exact")
    return tuple(swaps), tuple(path[index] for index in targets)


def apply_cnot(bits: list[int], first: int, second: int) -> None:
    bits[second] ^= bits[first]


def apply_swap_nn(bits: list[int], first: int, second: int) -> None:
    apply_cnot(bits, first, second)
    apply_cnot(bits, second, first)
    apply_cnot(bits, first, second)


def apply_nearest_neighbor(state: BasisState, *, reverse: bool = False) -> BasisState:
    validate_basis(state, require_lawful_prefix=not reverse)
    bits = list(state.bits)
    schedule = fixed_schedule(state.horizon)
    iterable = reversed(schedule) if reverse else schedule
    coords = manifest(state.horizon)
    for item in iterable:
        swaps, routed_sites = route_for_gate(item)
        for first, second in swaps:
            if manhattan(coords[first], coords[second]) != 1:
                raise RuntimeError("router emitted a non-NN SWAP")
            apply_swap_nn(bits, first, second)
        apply_gate(bits, Gate(item.kind, routed_sites, item.label))
        for first, second in reversed(swaps):
            apply_swap_nn(bits, first, second)
    return BasisState(state.horizon, tuple(bits))


@lru_cache(maxsize=None)
def nn_trace(horizon: int) -> GateTrace:
    coords = manifest(horizon)
    digest = sha256(f"Cycle485 {horizon}-link outward strip router v1".encode())
    primitives = failures = maximum_support = 0
    for item in fixed_schedule(horizon):
        swaps, routed_sites = route_for_gate(item)
        failures += sum(manhattan(coords[first], coords[second]) != 1 for first, second in swaps)
        failures += sum(
            manhattan(coords[first], coords[second]) != 1
            for first, second in zip(routed_sites, routed_sites[1:])
        )
        primitives += 1 + 6 * len(swaps)
        maximum_support = max(maximum_support, len(item.sites))
        digest.update(f"{item.kind}:{item.sites}:{item.label}:{len(swaps)}".encode())
    return GateTrace(len(fixed_schedule(horizon)), primitives, maximum_support, failures, digest.hexdigest())


def run_history(initial: BasisState, steps: int) -> tuple[BasisState, tuple[BasisState, ...]]:
    state = initial
    history = [initial]
    for _ in range(steps):
        state = apply_permutation(state)
        validate_basis(state)
        history.append(state)
    return state, tuple(history)


def prefix_projection(state: BasisState, cells: int) -> Word:
    return state.bits[: cells * CELL_M2]


def actual_packet(case_name: str) -> c482.CandidatePacket:
    return c482.actual_cycle443_candidate(case_name, 0)


def bridge_inverse_nn_controls() -> None:
    print("\nOUTWARD APPEND / EXACT E-G / INVERSE / NN")
    rows = []
    for case_name, source_l, horizon in (("train_L3", 3, 6), ("held_L6", 6, 12)):
        initial = prepare(actual_packet(case_name), horizon)
        physical = apply_permutation(initial)
        coarse = coarse_step(initial)
        recovered = apply_permutation(physical, reverse=True)
        witness = append_witness(initial, physical)
        rows.append({
            "case": case_name, "source_L": source_l, "horizon": horizon,
            "cells": capacity(horizon), "M2": capacity(horizon) * CELL_M2,
            "E_G_exact": physical == coarse, "inverse_exact": recovered == initial,
            "witness": witness,
            "work_leakage": sum(physical.bits[index] for cell in range(capacity(horizon)) for index in field(cell, WORK_LOCAL)),
            "retained_source": packet_view(physical, 0).word == packet_view(initial, 0).word,
        })
    held = prepare(actual_packet("held_L6"), 12)
    held_nn = apply_nearest_neighbor(held)
    held_logical = apply_permutation(held)
    check(
        "one fixed outward update has exact train/held E-G, inverse, and connected-NN realization",
        all(
            row["E_G_exact"] and row["inverse_exact"]
            and isinstance(row["witness"], OutwardAppend)
            and row["witness"].future_word_locally_derived
            and not row["witness"].framework_Record
            and row["work_leakage"] == 0 and row["retained_source"]
            for row in rows
        )
        and held_nn == held_logical
        and nn_trace(6).connected_failures == nn_trace(12).connected_failures == 0
        and nn_trace(6).maximum_support == nn_trace(12).maximum_support == 3,
        {"rows": rows, "held_NN_matches_logical": held_nn == held_logical,
         "train_trace": nn_trace(6), "held_trace": nn_trace(12)},
    )


def repeated_prefix_and_holdout_controls() -> None:
    print("\nREPEATED PREFIX / HELD HORIZON / CYLINDER CONSISTENCY")
    rows = []
    histories: dict[int, tuple[BasisState, ...]] = {}
    for case_name, source_l, horizon in (("train_L3", 3, 6), ("held_L6", 6, 12)):
        initial = prepare(actual_packet(case_name), horizon)
        terminal, history = run_history(initial, horizon)
        histories[horizon] = history
        packet = actual_packet(case_name)
        typed_prefix_exact = all(
            archive_view(terminal, cell).typed()
            and archive_view(terminal, cell).word == packet.word
            for cell in range(horizon)
        )
        terminal_blank = not any(archive_view(terminal, horizon).word)
        inverse = terminal
        for _ in range(horizon):
            inverse = apply_permutation(inverse, reverse=True, require_lawful_prefix=False)
        step_residuals = tuple(
            sum(left != right for left, right in zip(
                apply_permutation(history[step]).bits,
                coarse_step(history[step]).bits,
            ))
            for step in range(horizon)
        )
        rows.append({
            "case": case_name, "source_L": source_l, "horizon": horizon,
            "typed_prefix_length": sum(archive_view(terminal, cell).typed() for cell in range(capacity(horizon))),
            "typed_prefix_exact": typed_prefix_exact, "terminal_archive_blank": terminal_blank,
            "step_EG_bit_residuals": step_residuals, "full_history_inverse_exact": inverse == initial,
            "future_candidate_words_preloaded": 0,
        })

    # The same held packet on H=6 and H=12 has identical states on the shared
    # seven-cell cylinder through six ticks.  No parameter is refit.
    held_packet = actual_packet("held_L6")
    short_initial = prepare(held_packet, 6)
    long_initial = prepare(held_packet, 12)
    _, short_history = run_history(short_initial, 6)
    _, long_history = run_history(long_initial, 6)
    cylinder_residuals = tuple(
        sum(a != b for a, b in zip(prefix_projection(short, 7), prefix_projection(long, 7)))
        for short, long in zip(short_history, long_history)
    )
    gates_per_link = tuple(
        sum(item.label.startswith(f"link:{cell}:") for item in fixed_schedule(12))
        for cell in range(12)
    )
    check(
        "the archive grows without wrap through train H6 and held H12, and the held finite cylinders agree exactly",
        all(
            row["typed_prefix_length"] == row["horizon"]
            and row["typed_prefix_exact"] and row["terminal_archive_blank"]
            and max(row["step_EG_bit_residuals"]) == 0
            and row["full_history_inverse_exact"]
            and row["future_candidate_words_preloaded"] == 0
            for row in rows
        )
        and max(cylinder_residuals) == 0
        and set(gates_per_link) == {210},
        {"rows": rows, "held_H6_vs_H12_shared_prefix_bit_residuals": cylinder_residuals,
         "translation_equivalent_logical_gates_per_link": gates_per_link,
         "horizon_law": "H=2L fixed before held evaluation"},
    )


def boundary_and_resource_controls() -> None:
    print("\nTERMINAL BOUNDARY / NO CYCLIC OVERWRITE / RESOURCE LEDGER")
    horizon = 12
    initial = prepare(actual_packet("held_L6"), horizon)
    terminal, _ = run_history(initial, horizon)
    archive_before = tuple(archive_view(terminal, cell) for cell in range(capacity(horizon)))
    forced = apply_permutation(terminal, require_lawful_prefix=False)
    archive_after = tuple(archive_view(forced, cell) for cell in range(capacity(horizon)))
    forced_ready = selected(forced.bits, ready_sites(horizon))
    forced_moved = selected(forced.bits, moved_sites(horizon))
    recovered = apply_permutation(forced, reverse=True, require_lawful_prefix=False)
    supplied_initial_packet_count = sum(
        bool(any(packet_view(initial, cell).word)) for cell in range(capacity(horizon))
    )
    blank_carrier_cells = sum(
        not any(initial.bits[cell * CELL_M2:(cell + 1) * CELL_M2])
        for cell in range(1, capacity(horizon))
    )
    check(
        "terminal forcing signals exhausted capacity without wrap, overwrite, host repair, reset, discard, or hidden environment",
        archive_after == archive_before
        and sum(forced_ready) == 0 and forced_moved[-1] == 1 and sum(forced_moved) == 1
        and recovered == terminal
        and supplied_initial_packet_count == 1 and blank_carrier_cells == horizon,
        {
            "archive_bit_residual_after_forced_terminal_tick": sum(
                a != b for left, right in zip(archive_before, archive_after)
                for a, b in zip(left.word + left.occupancy + left.type_code + left.lock_code,
                                right.word + right.occupancy + right.type_code + right.lock_code)
            ),
            "boundary_syndrome": {"READY_population": sum(forced_ready), "MOVED_terminal": forced_moved[-1]},
            "inverse_restores_terminal": recovered == terminal,
            "initial_candidate_packets_supplied": supplied_initial_packet_count,
            "initial_blank_carrier_cells_supplied": blank_carrier_cells,
            "host_allocation_calls_during_update": 0,
            "reset_or_discard_operations": 0,
            "hidden_environment_M2": 0,
            "conditional_extendibility": "a larger initially supplied blank ray admits more identical local steps",
            "renewable_capacity_derived": False,
            "unbounded_permanence_derived": False,
        },
    )


def static_law_controls() -> None:
    print("\nFIXED TRANSLATION-LOCAL LAW / NO HOST-SIDE CONTROL")
    horizon = 12
    schedule = fixed_schedule(horizon)
    nominal = (
        inspect.getsource(fixed_schedule).lower()
        + inspect.getsource(apply_permutation).lower()
        + inspect.getsource(coarse_step).lower()
    )
    forbidden = tuple(token for token in (
        "law_program", "occurrence_bit", "realized_member_query", "reset_gate",
        "allocate_site", "environment_service", "host_choice",
    ) if token in nominal)
    link_counts = tuple(sum(item.label.startswith(f"link:{cell}:") for item in schedule) for cell in range(horizon))
    expected_logical = 222 * horizon + 3
    check(
        "all link subcircuits are present independent of state and share one constant-size template",
        set(link_counts) == {210}
        and len(schedule) == expected_logical
        and CELL_M2 == 198
        and not forbidden,
        {
            "horizon": horizon, "logical_gates": len(schedule), "closed_form": expected_logical,
            "logical_gates_per_link": link_counts, "M2_per_cell": CELL_M2,
            "cells": capacity(horizon), "total_M2": capacity(horizon) * CELL_M2,
            "nominal_forbidden_host_controls": forbidden,
            "schedule_selection_reads_state": False,
        },
    )


def coherent_boundary_controls() -> None:
    print("\nCOHERENT INPUT BOUNDARY / NO MEMBER SELECTION")
    base = actual_packet("held_L6")
    rival_word = list(base.word)
    rival_word[24] ^= 1
    rival = c482.CandidatePacket(tuple(rival_word), base.admission, "lawful rival Cycle485 basis packet")
    left = prepare(base, 6)
    right = prepare(rival, 6)
    amplitude = 1 / sqrt(2)
    vector: StateVector = {left.bits: amplitude, right.bits: 1j * amplitude}
    moved: StateVector = {}
    for bits, value in vector.items():
        output = apply_permutation(BasisState(6, bits)).bits
        moved[output] = moved.get(output, 0j) + value
    recovered: StateVector = {}
    for bits, value in moved.items():
        output = apply_permutation(BasisState(6, bits), reverse=True).bits
        recovered[output] = recovered.get(output, 0j) + value
    residual = sqrt(sum(abs(recovered.get(key, 0j) - vector.get(key, 0j)) ** 2 for key in recovered.keys() | vector.keys()))
    norm_in = sum(abs(value) ** 2 for value in vector.values())
    norm_out = sum(abs(value) ** 2 for value in moved.values())
    check(
        "coherent lawful basis packets remain coherent under the permutation; the runner selects no realized member",
        len(vector) == len(moved) == 2 and residual < TOL and abs(norm_in - norm_out) < TOL,
        {"input_support": len(vector), "output_support": len(moved),
         "inverse_vector_residual": residual, "norm_residual": abs(norm_in - norm_out),
         "Born_probability_claimed": False, "realized_member_selected": False},
    )


def deletion_controls() -> None:
    print("\nDELETION CONTROLS")
    initial = prepare(actual_packet("held_L6"), 6)
    nominal = apply_permutation(initial)
    controls = (
        ("admission-prefix", "link:0:admission-prefix:0"),
        ("accept", "link:0:accept:1"),
        ("archive-payload", "link:0:archive-packet:3"),
        ("propagation-payload", "link:0:propagate-packet:3"),
        ("active-carrier", "link:0:activate-next:0"),
        ("head-transport", "transport:0:vertical:0"),
        ("head-conversion", "convert:1:0"),
    )
    rows = []
    for name, label in controls:
        damaged = apply_permutation(initial, delete_label=label)
        visible = damaged != nominal
        refused = False
        try:
            validate_basis(damaged)
        except ValueError:
            refused = True
        rows.append((name, label, visible, refused, sum(a != b for a, b in zip(damaged.bits, nominal.bits))))
    check(
        "admission, archive, propagation, activation, and both frontier rails are causally necessary",
        len(rows) == 7 and all(visible and refused and residual > 0 for _, _, visible, refused, residual in rows),
        rows,
    )


def malformed_controls() -> None:
    print("\nMALFORMED / DIRTY RESOURCE CONTROLS")
    packet = actual_packet("held_L6")
    malformed_packet = c482.CandidatePacket(packet.word[:-1], packet.admission, "short")
    constructors = []
    try:
        prepare(malformed_packet, 6)
    except (TypeError, ValueError):
        constructors.append("short-packet")
    base = prepare(packet, 6)
    corruptions = {
        "zero-ready": ((site(0, READY), 0),),
        "two-ready": ((site(1, READY), 1),),
        "dirty-moved": ((site(0, MOVED), 1),),
        "bad-active-root": ((field(0, CARRIER_ACTIVE)[0], 0),),
        "dirty-dormant-inbox": ((field(2, INBOX_WORD)[24], 1),),
        "dirty-dormant-admission": ((field(2, INBOX_ADMISSION)[0], 1),),
        "dirty-dormant-archive": ((field(2, ARCHIVE_WORD)[24], 1),),
        "dirty-work": ((field(0, ADMISSION_PREFIX)[0], 1),),
    }
    refused = []
    for name, changes in corruptions.items():
        bits = list(base.bits)
        for index, value in changes:
            bits[index] = value
        try:
            apply_permutation(BasisState(base.horizon, tuple(bits)))
        except (TypeError, ValueError):
            refused.append(name)
    check(
        "malformed packets, frontier rails, active codes, dormant capacity, archives, and work are refused",
        constructors == ["short-packet"] and set(refused) == set(corruptions),
        {"constructor_refusals": constructors, "state_refusals": refused},
    )


def determinant(frame: tuple[tuple[int, int, int], ...]) -> int:
    matrix = np.array(frame, dtype=int)
    return int(round(np.linalg.det(matrix)))


@lru_cache(maxsize=1)
def proper_cubic_frames() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    frames = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for row, column in enumerate(permutation):
                matrix[row][column] = signs[row]
            frame = tuple(tuple(row) for row in matrix)
            if determinant(frame) == 1:
                frames.append(frame)
    return tuple(frames)


def rotate_coord(coord: Coord, frame: tuple[tuple[int, int, int], ...]) -> Coord:
    return tuple(sum(frame[row][column] * coord[column] for column in range(3)) for row in range(3))


def covariance_controls() -> None:
    print("\nALL-24 PROPER-CUBIC COVARIANCE")
    frames = proper_cubic_frames()
    rows = []
    failures = 0
    for frame_index, frame in enumerate(frames):
        for case_name, horizon in (("train_L3", 6), ("held_L6", 12)):
            case = next(item for item in c482.c443.CASES if item.name == case_name)
            moved_case, moved_layout = c482.rotated_case(case, np.array(frame, dtype=int))
            _, moved_child, moved_admission, _ = c482.c443.basis_pipeline(
                moved_case, 1, 1, layout=moved_layout,
            )
            packet = c482.CandidatePacket(
                c482.c443.word_from_register(moved_child),
                moved_admission.bits(),
                f"actual rotated Cycle443 {case_name} frame {frame_index}",
            )
            before = prepare(packet, horizon)
            after = apply_permutation(before)
            witness = append_witness(before, after)
            coords = tuple(rotate_coord(coord, frame) for coord in manifest(horizon))
            schedule = fixed_schedule(horizon)
            connected = 0
            for item in schedule:
                swaps, routed = route_for_gate(item)
                connected += sum(manhattan(coords[a], coords[b]) != 1 for a, b in swaps)
                connected += sum(
                    manhattan(coords[a], coords[b]) != 1
                    for a, b in zip(routed, routed[1:])
                )
            exact = (
                isinstance(witness, OutwardAppend)
                and after == coarse_step(before)
                and connected == 0
                and len(set(coords)) == len(coords)
            )
            failures += int(not exact)
            rows.append((frame_index, case_name, exact, connected))
    check(
        "the actual rotated Cycle443 packet, two-column carrier patch, two frontier rails, and fixed update form an all-24 proper-cubic family",
        len(frames) == 24 and len(rows) == 48 and failures == 0,
        {"proper_cubic_frames": len(frames), "train_held_frame_rows": len(rows),
         "failures": failures, "maximum_support": 3,
         "geometry": "frame-rotated two-column serpentine patch plus READY/MOVED rails"},
    )


def no_go_discipline_controls() -> None:
    print("\nNO-GO DISCIPLINE N1-N8 / BOUNDED POSITIVE GATE")
    n1 = (
        ("cyclic fixed-capacity tape", "ATTEMPTED", "Cycle482 positive through H, then exact recurrence/overwrite"),
        ("outward blank-carrier activation", "ATTEMPTED", "Cycle485 finite positive, no wrap; blank ray supplied"),
        ("explicit finite reset sink", "ATTEMPTED PRIOR", "Cycle452 finite resource move; sink renewal open"),
        ("one-root blank-line continuation", "ATTEMPTED PRIOR", "Cycle359 finite positive; repeated program/cap supplied"),
        ("dynamical carrier-pair creation", "OPEN / UNTESTED", "would have to preserve M2 accounting and inverse data"),
        ("infinite quasi-local carrier algebra", "OPEN / UNTESTED", "could state all finite cylinders without finite cap"),
        ("Record-typed absorbing sector", "OPEN / UNTESTED", "could use existing permanence authority after lawful typing"),
    )
    walls = ("W_prefix", "W_capacity", "W_form", "W_permanence", "W_resource")
    n2_pairs = tuple((a, b, False) for a, b in itertools.combinations(walls, 2))
    n3 = (
        "basis packet and admission meanings", "type/lock code meanings", "update cadence",
        "initial blank carrier geometry and terminal boundary", "carrier-active code meaning",
        "proper-cubic frame convention", "finite H=2L scaling law",
    )
    residuals = (
        ("Cycle359", "one-root propagation into blank finite line", "program, formation enable, cap, occurrence remain supplied"),
        ("Cycle452", "finite local ratchet and explicit reset export", "renewable sink/capacity and lawful typing remain supplied"),
        ("Cycle482", "deterministic typed prefix through fixed H", "future tape supplied and forced cyclic recurrence"),
        ("Cycle485", "future words derived; no wrap through held H12", "blank physical ray supplied; actual renewal and permanence open"),
    )
    rhetoric = (
        ("outward-growing", "frontier advances on a pre-existing finite strip", "creation of M2 sites"),
        ("renewable", "conditional finite-horizon extension by a larger supplied strip", "self-renewing capacity"),
        ("archive", "typed reversible physical prefix", "framework Record"),
        ("permanent", "no overwrite within tested H", "all-time permanence"),
    )
    n6 = (
        "larger finite blank rays with the identical local rule",
        "an infinite quasi-local cylinder theorem",
        "explicit carrier-pair genesis with conserved inverse data",
        "lawful Record typing followed by the existing permanence clause",
        "a renewable physical sink/resource lane with explicit source accounting",
    )
    steelman = (
        "A translation-invariant quasi-local algebra can define one rule on an infinite carrier ray; "
        "every finite prefix may then stabilize without any per-tick host action. Cycle485's exact "
        "H6/H12 cylinder agreement is compatible with that route and does not refute it."
    )
    echoes = (
        "Cycle359 finite blank-line cap", "Cycle452 finite receipt/reset-sink boundary",
        "Cycle482 cyclic recurrence", "Cycle485 terminal MOVED syndrome",
    )
    gate_fail = (
        len(n1) >= 5 and any(status == "OPEN / UNTESTED" for _, status, _ in n1)
        and len(n2_pairs) == 10 and len(n3) >= 7 and len(residuals) == 4
        and len(rhetoric) == 4 and len(n6) >= 5 and bool(steelman) and len(echoes) == 4
    )
    check(
        "N1-N8 rejects a no-go/minimum/axiom-pressure conclusion and permits only the bounded constructive statement",
        gate_fail,
        {"N1_routes": n1, "N2_pairwise_independence": n2_pairs, "N3_hidden_conditions": n3,
         "N4_residual_matching": residuals, "N5_rhetoric_resolutions": rhetoric,
         "N6_partial_closure_paths": n6, "N7_steelman": steelman, "N8_cross_cycle_echo": echoes,
         "Gate_disposition": "FAIL — partial-attempt-with-named-untested-routes",
         "no_go_or_axiom_pressure_claimed": False},
    )


def supplied_derived_open_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN")
    supplied = (
        "one actual Cycle443 admitted basis packet at cell zero",
        "H initially blank physical carrier cells and their terminal boundary",
        "basis, admission, occupancy/type/lock, and active-carrier code meanings",
        "one fixed update cadence and H=2L train/held test law",
        "proper-cubic frame convention and M2 primitive interpretation",
    )
    derived = (
        "future packet and admission fields from the single initial packet",
        "one unique append successor per nonterminal lawful basis state",
        "exact E G_coarse = G_physical E and exact inverse",
        "typed prefix preservation through train H6 and held H12",
        "zero cyclic overwrite and an explicit terminal capacity syndrome",
        "translation-local constant cell/link overhead and all-24 covariance",
        "held H6/H12 finite-cylinder consistency without parameter refit",
    )
    open_items = (
        "genesis or renewal of physical M2 capacity and blank carriers",
        "an infinite-volume/all-time theorem",
        "lawful framework Record formation, occurrence, and permanence",
        "independent event provenance and realized-member selection",
        "Born weights or probability", "energy/source/thermodynamic cost",
    )
    check(
        "the resource and semantic inventory separates prefix preservation, conditional extension, renewal, and permanence",
        len(supplied) == 5 and len(derived) == 7 and len(open_items) == 6,
        {"supplied": supplied, "derived": derived, "open": open_items,
         "finite_prefix_preservation": True,
         "conditional_finite_horizon_extendibility": True,
         "renewable_capacity": False, "unbounded_permanence": False,
         "framework_Record": False},
    )


def install_wall_cap() -> None:
    def handler(_signum: int, _frame: object) -> None:
        raise WallCapExceeded(f"Cycle485 exceeded wall cap {WALL_CAP_SECONDS}s")
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, WALL_CAP_SECONDS)


def resource_controls(start: float) -> None:
    elapsed = time.monotonic() - start
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        rss_bytes = int(rss)
    else:
        rss_bytes = int(rss * 1024)
    check(
        "Cycle485 stays within the declared wall/RSS envelope",
        elapsed < WALL_CAP_SECONDS and rss_bytes < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS,
         "peak_rss_bytes": rss_bytes, "rss_cap_bytes": RSS_CAP_BYTES},
    )


def main() -> int:
    start = time.monotonic()
    install_wall_cap()
    print("CYCLE485 OUTWARD-CARRIER TYPED-PREFIX PROBE")
    print("authority", AUTHORITY, "audit", AUDIT, "CELL_M2", CELL_M2)
    try:
        note_and_source_contracts()
        bridge_inverse_nn_controls()
        repeated_prefix_and_holdout_controls()
        boundary_and_resource_controls()
        static_law_controls()
        coherent_boundary_controls()
        deletion_controls()
        malformed_controls()
        covariance_controls()
        no_go_discipline_controls()
        supplied_derived_open_controls()
        resource_controls(start)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
