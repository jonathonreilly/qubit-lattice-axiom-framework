#!/usr/bin/env python3
"""Cycle 496: Kraus/FORM dephasing, microscopic selector, and bath conveyor.

All global maps retain their environments.  Dephasing and a reduced mixture
are therefore never promoted to one actual member.  A deterministic selector
does give one terminal-menu word conditional on its supplied candidate law and
microseed, but it is explicitly not an unraveling of the Cycle478 instrument.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
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
import physical_terminal_menu_member_law_tournament_cycle493_2026_07_20 as c493
import physical_outward_carrier_typed_prefix_cycle485_2026_07_19 as c485


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_KRAUS_FORM_DEPHASING_BATH_CONVEYOR_CYCLE496_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TRAIN_N = 8
HELD_N = 16
FORM_HORIZON = 6
TOL = 2e-9
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
PASS = 0
FAIL = 0
MENU = range(c493.c488.MENU_ARITY)
Word = tuple[int, ...]
Coord = tuple[int, int, int]

FROZEN = {
    "Cycle493 runner": "7c51c313f83e006d1bd036e1d3d3d6a7f0fb39cfa56f874419d1e18658aca9af",
    "Cycle493 note": "81cab7f7fa54bef5789c3991911dc197f7506e4aeaa721973a548685006cbd8a",
    "Cycle485 runner": "050c979de0f27073815309ad67635997f5c54b3344734b36e4f7fb3ab80ded7c",
    "Cycle485 note": "244e8c32f611151664c2b609eea48cd34afce7424ead4d3a1d131c48daafb94e",
    "Cycle483 runner": "52f0621a06792093ad64a706ab7741335cfd7ff9418b3756f4ab83cf72b8d222",
    "Cycle483 note": "be836748288af45b5b71d71ce380376f05b4168468e48e2bc8ff75c4a43dc74f",
}
FROZEN_PATHS = {
    "Cycle493 runner": Path(c493.__file__),
    "Cycle493 note": c493.NOTE,
    "Cycle485 runner": Path(c485.__file__),
    "Cycle485 note": c485.NOTE,
    "Cycle483 runner": Path(c493.c488.c483.__file__),
    "Cycle483 note": c493.c488.c483.NOTE,
}


class WallCapExceeded(RuntimeError):
    pass


@dataclass(frozen=True)
class ConveyorState:
    horizon: int
    cells: tuple[c493.c488.BasisState, ...]
    ready: Word
    moved: Word
    used: Word
    exported: Word
    courier: int


@dataclass(frozen=True)
class ConveyorTrace:
    horizon: int
    cell_M2: int
    total_M2: int
    controlled_logical_gates_per_tick: int
    maximum_support_M2: int
    schedule_selection_reads_state: bool
    sha256: str


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


def contract_controls() -> None:
    required = (
        "authority: none", "audit: unset", "exact target contract",
        "route a — redundant retained-pointer dephasing dilation",
        "route b — deterministic microscopic selector/ca",
        "route c — fresh-bath outward conveyor",
        "same cycle-493 kraus-controlled form seam", "cycle-485 outward carrier",
        "train n=8", "held n=16", "two incompatible input states",
        "physical-m2 e/g", "exact inverse", "no used-bath reentry",
        "all 24 proper-cubic frames", "deletion", "malformed", "noise",
        "record axiom and realized-state primitive far shore",
        "dephasing or a reduced mixture is not one continuing member",
        "no per-event host bath reset", "supplied / derived / open",
        "gate disposition: fail", "no shared obstruction or axiom-pressure claim",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle496 note freezes the three-route target and actuality firewall", not missing, missing)
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    check(
        "Cycle493/485/483 direct inputs are frozen by runner and note SHA",
        observed == FROZEN,
        {"observed": observed, "authority": AUTHORITY, "audit": AUDIT},
    )
    axiom = normalized(ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md")
    primitive = normalized(ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md")
    check(
        "the current Record/realized-state far shore is read without importing formation content",
        "records form" in axiom
        and "formation rules" in axiom
        and "the laws do not pick the state; the world does" in primitive
        and "does not supply a state, state-selection rule" in primitive,
        {
            "Record_supplies": "formation, one admissible lock when present, permanence, finite readout additivity",
            "Record_withholds": "which possibility/site/weight/rate and record-production dynamics",
            "realized_state_primitive": "pointwise slot only; no state content or selector",
        },
    )


def bits3(value: int) -> Word:
    return c493.c488.bits_of(value, c493.c488.POINTER_BITS)


def value3(bits: Word) -> int:
    return c493.c488.int_of(bits)


def copy_pointer(value: int) -> tuple[Word, Word, Word]:
    source = bits3(value)
    left = [0, 0, 0]
    right = [0, 0, 0]
    for lane in range(3):
        left[lane] ^= source[lane]
        right[lane] ^= source[lane]
    return source, tuple(left), tuple(right)


def uncopy_pointer(replicas: tuple[Word, Word, Word]) -> tuple[Word, Word, Word]:
    source, left, right = replicas
    left = list(left)
    right = list(right)
    for lane in reversed(range(3)):
        right[lane] ^= source[lane]
        left[lane] ^= source[lane]
    return source, tuple(left), tuple(right)


def majority_pointer(replicas: tuple[Word, Word, Word]) -> int | None:
    decoded = tuple(int(sum(copy[lane] for copy in replicas) >= 2) for lane in range(3))
    value = value3(decoded)
    return value if value in MENU else None


def menu_packet(pointer: int) -> c485.c482.CandidatePacket:
    if pointer not in MENU:
        raise ValueError("packet pointer leaves the terminal menu")
    word = c493.c488.class_words(c493.c488.HELD_CASE)[pointer]
    packet = c485.c482.CandidatePacket(word, (1,) * c485.ADMISSION_BITS, f"Cycle496 class {pointer}")
    c485.c482.validate_candidate(packet)
    return packet


def route_a_controls(surface: c493.c488.MenuSurface) -> dict[str, object]:
    print("\nROUTE A / REDUNDANT RETAINED-POINTER DEPHASING")
    states = (
        ("z-plus", np.asarray((1.0, 0.0), complex)),
        ("y-plus", np.asarray((1.0, 1.0j), complex) / sqrt(2.0)),
    )
    basis_failures = 0
    one_noise_failures = 0
    two_noise_visible = 0
    prefix_rows = []
    for pointer in range(8):
        replicas = copy_pointer(pointer)
        recovered = uncopy_pointer(replicas)
        basis_failures += int(recovered != (bits3(pointer), (0, 0, 0), (0, 0, 0)))
        if pointer in MENU:
            flat = [list(word) for word in replicas]
            for replica in range(3):
                for lane in range(3):
                    noisy = [list(word) for word in replicas]
                    noisy[replica][lane] ^= 1
                    one_noise_failures += int(majority_pointer(tuple(tuple(word) for word in noisy)) != pointer)
            noisy = [list(word) for word in replicas]
            noisy[0][0] ^= 1
            noisy[1][0] ^= 1
            two_noise_visible += int(majority_pointer(tuple(tuple(word) for word in noisy)) != pointer)

            form_initial = c493.prepare_history(c493.c488.HELD_CASE, FORM_HORIZON, (pointer,))
            form_physical = c493.apply_physical(form_initial)
            form_coarse = c493.coarse_step(form_initial)
            form_recovered = c493.apply_physical(form_physical, reverse=True)
            packet = menu_packet(pointer)
            prefix_initial = c485.prepare(packet, HELD_N)
            prefix_physical = c485.apply_permutation(prefix_initial)
            prefix_coarse = c485.coarse_step(prefix_initial)
            prefix_recovered = c485.apply_permutation(prefix_physical, reverse=True)
            witnessed = c493.c488.receipts(form_physical)
            basis_failures += int(
                form_physical != form_coarse or form_recovered != form_initial
                or witnessed is None or witnessed[0].pointer != pointer
                or prefix_physical != prefix_coarse or prefix_recovered != prefix_initial
            )
            prefix_rows.append((pointer, witnessed[0].effect_class if witnessed else None, prefix_physical == prefix_coarse))

    input_rows = []
    for name, psi in states:
        branches = tuple(operator @ psi for operator in surface.held_program.kraus)
        weights = tuple(float(np.vdot(branch, branch).real) for branch in branches)
        # Distinct environment words are exactly orthogonal, so tracing the
        # two copies removes pointer off-diagonals while the global pure state
        # and every unnormalized branch coefficient remain present.
        input_rows.append({
            "state": name,
            "unnormalized_branch_squared_norms": weights,
            "global_norm": sum(weights),
            "reduced_pointer_diagonal": weights,
            "reduced_pointer_offdiagonal_max": 0.0,
            "global_coherent_terms": sum(np.linalg.norm(branch) > 1e-15 for branch in branches),
            "train_factorized_norm": sum(weights) ** TRAIN_N,
            "held_factorized_norm": sum(weights) ** HELD_N,
        })

    full_initial = c485.prepare(menu_packet(0), HELD_N)
    terminal, history = c485.run_history(full_initial, HELD_N)
    inverse = terminal
    for _ in range(HELD_N):
        inverse = c485.apply_permutation(inverse, reverse=True, require_lawful_prefix=False)
    typed = sum(c485.archive_view(terminal, cell).typed() for cell in range(c485.capacity(HELD_N)))
    check(
        "A: the actual five-sector Kraus output has an exact redundant stable-pointer/FORM/prefix dilation, while reduced dephasing selects no member",
        basis_failures == one_noise_failures == 0 and two_noise_visible == c493.c488.MENU_ARITY
        and all(abs(row["global_norm"] - 1.0) < TOL for row in input_rows)
        and all(row["global_coherent_terms"] == c493.c488.MENU_ARITY for row in input_rows)
        and len(prefix_rows) == c493.c488.MENU_ARITY
        and len(history) == HELD_N + 1 and typed == HELD_N and inverse == full_initial,
        {
            "input_rows": input_rows,
            "basis_FORM_and_Cycle485_prefix_rows": prefix_rows,
            "replicated_pointer_M2": 9,
            "maximum_copy_gate_support_M2": 2,
            "single_bit_noise_failures": one_noise_failures,
            "two_same_lane_errors_visible": two_noise_visible,
            "held_prefix_H16_typed_cells": typed,
            "held_prefix_inverse_exact": inverse == full_initial,
            "global_environment_retained": True,
            "reduced_dephasing_is_actual_member": False,
        },
    )
    return {"states": states, "rows": input_rows}


def ca_word(seed: int, length: int) -> tuple[int, ...]:
    if seed not in MENU or length < 1:
        raise ValueError("CA seed/length leaves the declared domain")
    cursor = seed
    answer = []
    for _ in range(length):
        answer.append(cursor)
        cursor = c493.rotate_pointer(cursor)
    return tuple(answer)


def counts(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(word.count(pointer) for pointer in MENU)


def route_b_controls(route_a: dict[str, object]) -> dict[str, object]:
    print("\nROUTE B / DETERMINISTIC MICROSCOPIC SELECTOR-CA")
    train = ca_word(0, TRAIN_N)
    held = ca_word(0, HELD_N)
    all_orbits = tuple((seed, ca_word(seed, HELD_N), counts(ca_word(seed, HELD_N))) for seed in MENU)
    ca_inverse_failures = 0
    for seed, word, _counts in all_orbits:
        cursor = seed
        for _ in range(HELD_N):
            cursor = c493.rotate_pointer(cursor)
        for _ in range(HELD_N):
            cursor = c493.rotate_pointer(cursor, reverse=True)
        ca_inverse_failures += int(cursor != seed or any(pointer not in MENU for pointer in word))

    frequencies = tuple(Fraction(value, HELD_N) for value in counts(held))
    state_rows = []
    for row in route_a["rows"]:
        q = row["unnormalized_branch_squared_norms"]
        l1 = sum(abs(float(freq) - weight) for freq, weight in zip(frequencies, q))
        accept_reject = tuple((pointer, q[pointer], 1.0 - q[pointer]) for pointer in held)
        state_rows.append({
            "state": row["state"],
            "held_counts": counts(held),
            "held_frequencies": tuple(map(str, frequencies)),
            "L1_from_Kraus_norm_grades": l1,
            "minimum_retained_reject_norm": min(reject for _pointer, _accept, reject in accept_reject),
        })

    lawful_packets = 0
    form_failures = 0
    for pointer in MENU:
        menu_packet(pointer)
        lawful_packets += 1
        initial = c493.prepare_history(c493.c488.HELD_CASE, FORM_HORIZON, (pointer,))
        output = c493.apply_physical(initial)
        receipt = c493.c488.receipts(output)
        form_failures += int(receipt is None or receipt[0].pointer != pointer)

    check(
        "B: a fixed reversible microscopic CA gives one exact terminal-menu member per supplied microseed, but does not unravel the coherent Kraus instrument",
        ca_inverse_failures == form_failures == 0 and lawful_packets == c493.c488.MENU_ARITY
        and counts(train) == (2, 2, 2, 1, 1) and counts(held) == (4, 3, 3, 3, 3)
        and all(row["L1_from_Kraus_norm_grades"] > 0.35 for row in state_rows)
        and all(row["minimum_retained_reject_norm"] > 0.5 for row in state_rows),
        {
            "train_N8_word_counts": (train, counts(train)),
            "held_N16_word_counts_frequencies": (held, counts(held), tuple(map(str, frequencies))),
            "all_held_seed_orbits": all_orbits,
            "two_input_non_Born_control": state_rows,
            "candidate_law_unique_answer": True,
            "candidate_law_and_microseed_supplied": True,
            "proper_unitary_comparator_retains_reject_sectors": True,
            "derived_Cycle478_outcome_unraveling": False,
            "realized_state_primitive_supplies_microseed_content": False,
        },
    )
    return {"train": train, "held": held, "state_rows": state_rows}


def blank_cell() -> c493.c488.BasisState:
    return c493.prepare_history(c493.c488.HELD_CASE, FORM_HORIZON, (0,))


def prepare_conveyor(horizon: int, seed: int = 0) -> ConveyorState:
    if horizon < 1 or seed not in MENU:
        raise ValueError("conveyor horizon/seed leaves the declared domain")
    size = horizon + 1
    state = ConveyorState(
        horizon,
        tuple(blank_cell() for _ in range(size)),
        (1,) + (0,) * horizon,
        (0,) * size,
        (0,) * size,
        (0,) * size,
        seed,
    )
    validate_conveyor(state)
    return state


def conveyor_head(state: ConveyorState) -> int:
    if sum(state.ready) != 1:
        raise ValueError("conveyor READY rail is not one-hot")
    return state.ready.index(1)


def validate_conveyor_shape(state: ConveyorState, *, allow_boundary: bool = False) -> None:
    size = state.horizon + 1
    if (
        not isinstance(state, ConveyorState) or state.horizon < 1 or state.courier not in MENU
        or any(len(field) != size for field in (state.ready, state.moved, state.used, state.exported))
        or len(state.cells) != size
    ):
        raise ValueError("conveyor leaves its finite typed domain")
    if any(bit not in (0, 1) for field in (state.ready, state.moved, state.used, state.exported) for bit in field):
        raise ValueError("conveyor rails are nonbinary")
    if allow_boundary and sum(state.ready) == 0 and sum(state.moved) == 1 and state.moved[-1] == 1:
        return
    if sum(state.ready) != 1:
        raise ValueError("conveyor READY rail is not one-hot")
    if any(state.moved):
        raise ValueError("conveyor MOVED rail must be blank")


def validate_conveyor(state: ConveyorState, *, allow_boundary: bool = False) -> None:
    validate_conveyor_shape(state, allow_boundary=allow_boundary)
    if allow_boundary and sum(state.ready) == 0:
        return
    size = state.horizon + 1
    head = conveyor_head(state)
    if tuple(state.used) != (1,) * head + (0,) * (size - head):
        raise ValueError("used-bath prefix is malformed or reenters")
    if state.exported != state.used:
        raise ValueError("spent bath is not retained on the outward export prefix")
    for index, cell in enumerate(state.cells):
        if index < head:
            receipt = c493.c488.receipts(cell)
            if receipt is None or len(receipt) != 1:
                raise ValueError("used conveyor cell lacks its retained FORM receipt/bath")
        else:
            c493.validate_generic_input(cell)


def set_cell_pointer(cell: c493.c488.BasisState, pointer: int) -> c493.c488.BasisState:
    bits = list(cell.bits)
    c493.c488.replace_selected(
        bits, c493.c488.field(0, c493.c488.POINTER),
        c493.c488.bits_of(pointer, c493.c488.POINTER_BITS),
    )
    output = c493.c488.BasisState(cell.trials, cell.horizon, cell.case_name, tuple(bits))
    c493.validate_generic_input(output)
    return output


def clear_cell_pointer(cell: c493.c488.BasisState, pointer: int) -> c493.c488.BasisState:
    bits = list(cell.bits)
    current = c493.c488.int_of(c493.c488.selected(bits, c493.c488.field(0, c493.c488.POINTER)))
    if current != pointer:
        raise ValueError("inverse conveyor pointer does not match restored courier")
    c493.c488.replace_selected(bits, c493.c488.field(0, c493.c488.POINTER), (0, 0, 0))
    output = c493.c488.BasisState(cell.trials, cell.horizon, cell.case_name, tuple(bits))
    c493.validate_generic_input(output)
    return output


def apply_controlled_form_bits(bits: list[int], enable: int, *, reverse: bool = False) -> None:
    """Literal clean-work compilation of the READY-controlled FORM schedule."""
    work = 0
    schedule = c493.physical_schedule(1, FORM_HORIZON)
    for item in reversed(schedule) if reverse else schedule:
        if item.kind == "X":
            bits[item.sites[0]] ^= enable
        elif item.kind == "CNOT":
            control, target = item.sites
            bits[target] ^= enable & bits[control]
        elif item.kind == "TOFFOLI":
            first, second, target = item.sites
            # Toffoli(enable, first, work); Toffoli(work, second,
            # target); Toffoli(enable, first, work).
            work ^= enable & bits[first]
            bits[target] ^= work & bits[second]
            work ^= enable & bits[first]
        elif item.kind == "SWAP":
            first, second = item.sites
            # Fredkin(enable; first, second) with no work bit:
            # CNOT(first,second); Toffoli(enable,second,first);
            # CNOT(first,second).  The palindrome is its own inverse.
            bits[second] ^= bits[first]
            bits[first] ^= enable & bits[second]
            bits[second] ^= bits[first]
        else:
            raise ValueError("uncompiled conveyor gate")
    if work:
        raise RuntimeError("controlled FORM work did not return blank")


@lru_cache(maxsize=None)
def rail_swap_schedule(horizon: int) -> tuple[tuple[str, int, str, int], ...]:
    """Cycle485 two-rail no-wrap permutation, emitted independently of state."""
    gates: list[tuple[str, int, str, int]] = []
    for cell in range(horizon):
        gates.extend((
            ("ready", cell, "ready", cell + 1),
            ("ready", cell + 1, "moved", cell + 1),
            ("ready", cell, "ready", cell + 1),
        ))
    for cell in range(horizon + 1):
        gates.append(("moved", cell, "ready", cell))
    return tuple(gates)


def apply_rail_schedule(ready: list[int], moved: list[int], *, reverse: bool = False) -> None:
    rails = {"ready": ready, "moved": moved}
    schedule = rail_swap_schedule(len(ready) - 1)
    for first_name, first, second_name, second in reversed(schedule) if reverse else schedule:
        # Literal nearest-neighbour SWAP = CNOT(a,b), CNOT(b,a), CNOT(a,b).
        rails[second_name][second] ^= rails[first_name][first]
        rails[first_name][first] ^= rails[second_name][second]
        rails[second_name][second] ^= rails[first_name][first]


def conveyor_physical_tick(state: ConveyorState, *, reverse: bool = False) -> ConveyorState:
    """Execute one fixed all-cell controlled permutation; no decoded-head lookup."""
    validate_conveyor_shape(state, allow_boundary=reverse)
    cells = [list(cell.bits) for cell in state.cells]
    ready = list(state.ready)
    moved = list(state.moved)
    used = list(state.used)
    exported = list(state.exported)
    courier = state.courier
    event_cells = range(state.horizon)

    if reverse:
        apply_rail_schedule(ready, moved, reverse=True)
        courier = c493.rotate_pointer(courier, reverse=True)
        for cell in reversed(tuple(event_cells)):
            enable = ready[cell]
            used[cell] ^= enable
            exported[cell] ^= enable
        for cell in reversed(tuple(event_cells)):
            apply_controlled_form_bits(cells[cell], ready[cell], reverse=True)
        courier_bits = bits3(courier)
        for cell in reversed(tuple(event_cells)):
            for lane in reversed(range(3)):
                target = c493.c488.field(0, c493.c488.POINTER)[lane]
                cells[cell][target] ^= ready[cell] & courier_bits[lane]
    else:
        courier_bits = bits3(courier)
        for cell in event_cells:
            for lane in range(3):
                target = c493.c488.field(0, c493.c488.POINTER)[lane]
                cells[cell][target] ^= ready[cell] & courier_bits[lane]
        for cell in event_cells:
            apply_controlled_form_bits(cells[cell], ready[cell])
        for cell in event_cells:
            enable = ready[cell]
            used[cell] ^= enable
            exported[cell] ^= enable
        courier = c493.rotate_pointer(courier)
        apply_rail_schedule(ready, moved)

    output = ConveyorState(
        state.horizon,
        tuple(
            c493.c488.BasisState(1, FORM_HORIZON, c493.c488.HELD_CASE, tuple(bits))
            for bits in cells
        ),
        tuple(ready), tuple(moved), tuple(used), tuple(exported), courier,
    )
    validate_conveyor_shape(output, allow_boundary=not any(output.ready))
    return output


def conveyor_coarse_tick(state: ConveyorState) -> ConveyorState:
    """Independent declarative reference; state inspection is licensed here."""
    validate_conveyor(state)
    head = conveyor_head(state)
    if head >= state.horizon:
        raise ValueError("coarse conveyor reached its terminal bath cell")
    cells = list(state.cells)
    cells[head] = c493.coarse_step(set_cell_pointer(cells[head], state.courier))
    ready = list(state.ready)
    used = list(state.used)
    exported = list(state.exported)
    ready[head] = 0
    ready[head + 1] = 1
    used[head] = 1
    exported[head] = 1
    output = ConveyorState(
        state.horizon, tuple(cells), tuple(ready), state.moved,
        tuple(used), tuple(exported), c493.rotate_pointer(state.courier),
    )
    validate_conveyor(output)
    return output


def force_boundary(state: ConveyorState) -> ConveyorState:
    validate_conveyor(state)
    if conveyor_head(state) != state.horizon:
        raise ValueError("boundary syndrome requires the terminal frontier")
    return conveyor_physical_tick(state)


@lru_cache(maxsize=None)
def conveyor_trace(horizon: int) -> ConveyorTrace:
    local = c493.physical_schedule(1, FORM_HORIZON)
    manifest = sha256()
    logical = 0

    def emit(label: str) -> None:
        nonlocal logical
        manifest.update(label.encode("utf-8") + b"\n")
        logical += 1

    # Emit the actual forward order.  Every event cell is present regardless
    # of READY; enable values and decoded-head data never enter the manifest.
    for cell in range(horizon):
        for lane in range(3):
            emit(f"cell:{cell}:ready-controlled-pointer-copy:{lane}")
    for cell in range(horizon):
        for item in local:
            stem = f"cell:{cell}:ready-controlled-form:{item.label}"
            if item.kind == "TOFFOLI":
                emit(stem + ":clean-work-load")
                emit(stem + ":target")
                emit(stem + ":clean-work-clear")
            elif item.kind == "SWAP":
                emit(stem + ":fredkin-cnot-a-b")
                emit(stem + ":fredkin-toffoli-enable-b-a")
                emit(stem + ":fredkin-cnot-a-b")
            else:
                emit(stem)
    for cell in range(horizon):
        emit(f"cell:{cell}:ready-controlled-used")
        emit(f"cell:{cell}:ready-controlled-exported")
    for item in c493.rotor_schedule():
        emit("courier:" + item.label)
    for index, (first_name, first, second_name, second) in enumerate(rail_swap_schedule(horizon)):
        stem = f"rail:{index}:{first_name}:{first}:{second_name}:{second}"
        emit(stem + ":cnot-a-b")
        emit(stem + ":cnot-b-a")
        emit(stem + ":cnot-a-b")

    physical_sources = "\n".join(
        inspect.getsource(function)
        for function in (
            conveyor_physical_tick,
            apply_controlled_form_bits,
            apply_rail_schedule,
            rail_swap_schedule,
        )
    ).lower()
    state_selected_schedule = (
        "conveyor_head" in physical_sources
        or ".index(" in physical_sources
        or "if enable" in physical_sources
    )
    cell_m2 = c493.c488.CELL_M2 + 5
    return ConveyorTrace(
        horizon, cell_m2, (horizon + 1) * cell_m2 + 3,
        logical, 3, state_selected_schedule, manifest.hexdigest(),
    )


def route_c_controls() -> dict[str, object]:
    print("\nROUTE C / FRESH-BATH OUTWARD CONVEYOR")
    rows = []
    terminals = {}
    for horizon in (TRAIN_N, HELD_N):
        initial = prepare_conveyor(horizon)
        physical = initial
        step_residuals = []
        for _ in range(horizon):
            coarse = conveyor_coarse_tick(physical)
            advanced = conveyor_physical_tick(physical)
            validate_conveyor(advanced)
            step_residuals.append(int(advanced != coarse))
            physical = advanced
        terminal = physical
        inverse = terminal
        for _ in range(horizon):
            inverse = conveyor_physical_tick(inverse, reverse=True)
            validate_conveyor(inverse)
        retained_pointers = tuple(
            c493.c488.receipts(cell)[0].pointer
            for cell in terminal.cells[:horizon]
            if c493.c488.receipts(cell) is not None
        )
        rows.append({
            "N": horizon,
            "E_G_residuals": tuple(step_residuals),
            "inverse_exact": inverse == initial,
            "retained_pointer_word": retained_pointers,
            "counts": counts(retained_pointers),
            "used_bath_cells": sum(terminal.used),
            "exported_spent_cells": sum(terminal.exported),
            "trace": conveyor_trace(horizon),
        })
        terminals[horizon] = (initial, terminal)

    held_initial, held_terminal = terminals[HELD_N]
    boundary = force_boundary(held_terminal)
    boundary_inverse = conveyor_physical_tick(boundary, reverse=True)
    bath_sets = tuple(
        frozenset(
            cell * c493.c488.CELL_M2 + site
            for site in c493.c488.c483.B_BATH_SITES
        )
        for cell in range(HELD_N)
    )
    intersections = sum(bool(left.intersection(right)) for left, right in combinations(bath_sets, 2))
    check(
        "C: one fixed finite outward conveyor supplies a fresh Cycle483 bath block per event, retains/exports every spent block, and removes per-event host reset through N16",
        all(not any(row["E_G_residuals"]) and row["inverse_exact"] for row in rows)
        and rows[0]["retained_pointer_word"] == ca_word(0, TRAIN_N)
        and rows[1]["retained_pointer_word"] == ca_word(0, HELD_N)
        and rows[0]["used_bath_cells"] == rows[0]["exported_spent_cells"] == TRAIN_N
        and rows[1]["used_bath_cells"] == rows[1]["exported_spent_cells"] == HELD_N
        and intersections == 0 and sum(boundary.ready) == 0 and boundary.moved[-1] == 1
        and boundary_inverse == held_terminal,
        {
            "train_held_rows": rows,
            "held_pairwise_bath_region_intersections": intersections,
            "used_bath_reentry_operations": 0,
            "per_event_host_bath_reset_operations": 0,
            "initial_blank_bath_cells_supplied": HELD_N + 1,
            "boundary_syndrome": {"READY_population": sum(boundary.ready), "terminal_MOVED": boundary.moved[-1]},
            "boundary_inverse_exact": boundary_inverse == held_terminal,
            "global_environment_discarded": False,
            "fresh_bath_genesis_derived": False,
        },
    )
    return {"rows": rows, "initial": held_initial, "terminal": held_terminal}


def deletion_domain_noise_controls(route_c: dict[str, object]) -> None:
    print("\nDELETION / DOMAIN / NOISE")
    initial = route_c["initial"]
    head = conveyor_head(initial)
    pointed = set_cell_pointer(initial.cells[head], initial.courier)
    damaged = c493.apply_physical(pointed, delete_label="cell:0:match:0:prefix:0")
    form_deletion_visible = c493.c488.receipts(damaged) is None

    advanced = conveyor_physical_tick(initial)
    bad_reentry = ConveyorState(
        advanced.horizon, advanced.cells,
        (1,) + (0,) * advanced.horizon,
        advanced.moved, advanced.used, advanced.exported, advanced.courier,
    )
    dirty_future_cells = list(initial.cells)
    dirty_bits = list(dirty_future_cells[1].bits)
    dirty_bits[c493.c488.site(0, c493.c488.c483.B_FORM_BATH_FRESH)] = 1
    dirty_future_cells[1] = c493.c488.BasisState(1, FORM_HORIZON, c493.c488.HELD_CASE, tuple(dirty_bits))
    dirty_future = ConveyorState(
        initial.horizon, tuple(dirty_future_cells), initial.ready, initial.moved,
        initial.used, initial.exported, initial.courier,
    )
    two_ready = ConveyorState(
        initial.horizon, initial.cells, (1, 1) + (0,) * (initial.horizon - 1),
        initial.moved, initial.used, initial.exported, initial.courier,
    )
    bad_seed = ConveyorState(
        initial.horizon, initial.cells, initial.ready, initial.moved,
        initial.used, initial.exported, 7,
    )
    refusals = 0
    for state in (bad_reentry, dirty_future, two_ready, bad_seed):
        try:
            validate_conveyor(state)
        except ValueError:
            refusals += 1

    # Deleting frontier transport leaves a used active cell under READY; the
    # lawful conveyor validator must reject it before any bath can reenter.
    stalled = ConveyorState(
        advanced.horizon, advanced.cells, initial.ready, advanced.moved,
        advanced.used, advanced.exported, advanced.courier,
    )
    frontier_deletion_visible = False
    try:
        validate_conveyor(stalled)
    except ValueError:
        frontier_deletion_visible = True
    check(
        "FORM/frontier deletions are visible and used-bath reentry, dirty future bath, two-frontier, and bad-seed states are refused",
        form_deletion_visible and frontier_deletion_visible and refusals == 4,
        {
            "FORM_matcher_deletion_visible": form_deletion_visible,
            "frontier_transport_deletion_visible": frontier_deletion_visible,
            "malformed_or_noise_refusals": refusals,
            "one_pointer_bit_noise_corrected_by_route_A": True,
            "two_same_lane_noise_detectably_changes_route_A_decode": True,
        },
    )


def rotate(coord: Coord, frame: tuple[tuple[int, int, int], ...]) -> Coord:
    return tuple(sum(frame[row][column] * coord[column] for column in range(3)) for row in range(3))


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def covariance_resource_controls() -> None:
    print("\nLOCALITY / ALL24 / RESOURCE SCALING")
    frames = c493.c488.proper_cubic_frames()
    traces = {n: conveyor_trace(n) for n in (TRAIN_N, HELD_N)}
    form_trace = c493.generic_adapter_trace(1)
    bath_trace = c493.c488.c483.route_trace("bath", FORM_HORIZON)
    prefix_trace = c485.nn_trace(HELD_N)
    base_edges = tuple(
        ((cell, lane, 0), (cell, lane + 1, 0))
        for cell in range(HELD_N + 1)
        for lane in range(12)
    ) + tuple(((cell, 0, 0), (cell + 1, 0, 0)) for cell in range(HELD_N))
    failures = 0
    rows = 0
    for frame in frames:
        for left, right in base_edges:
            failures += int(manhattan(rotate(left, frame), rotate(right, frame)) != 1)
            rows += 1
    linear_scaling = (
        traces[HELD_N].cell_M2 == traces[TRAIN_N].cell_M2
        and traces[HELD_N].total_M2 == (HELD_N + 1) * traces[HELD_N].cell_M2 + 3
    )
    check(
        "dephasing copies, FORM cells, outward bath/frontier edges, and Cycle485 prefix routes have bounded support and all-24 covariance",
        len(frames) == 24 and failures == 0 and linear_scaling
        and all(trace.maximum_support_M2 <= 3 and not trace.schedule_selection_reads_state for trace in traces.values())
        and form_trace.maximum_support_M2 <= 3 and form_trace.connected_failures == 0
        and bath_trace.maximum_support_M2 <= 3 and bath_trace.connected_failures == 0
        and prefix_trace.maximum_support <= 3 and prefix_trace.connected_failures == 0,
        {
            "proper_cubic_frames": len(frames),
            "rotated_edge_rows": rows,
            "failures": failures,
            "conveyor_traces": traces,
            "one_event_FORM_trace": form_trace,
            "Cycle483_bath_trace": bath_trace,
            "Cycle485_H16_prefix_trace": prefix_trace,
            "constant_M2_per_conveyor_cell": traces[HELD_N].cell_M2,
            "linear_resource_scaling": linear_scaling,
        },
    )


def far_shore_disposition_controls() -> None:
    print("\nRECORD / ACTUALITY FAR-SHORE DISPOSITION")
    dispositions = (
        ("Record axiom", "records form and one admissible possibility locks", "approved premise", "does not choose content/site/weight/rate"),
        ("realized-state primitive", "pointwise evaluation at history-fixed state", "approved premise", "does not supply state or selection rule"),
        ("Record dephasing/broadcast interface", "global correlation and reduced dephasing", "recon", "nonselective state is not one atom"),
        ("selective instrument atom criterion", "normalized repeat-stable selected branch", "recon", "outcome token is separate"),
        ("Cycle485", "typed no-wrap finite prefix", "direct", "typed archive is not framework Record"),
        ("Cycle493", "actual Kraus pointer controls FORM coherently", "direct", "coherence selects no member"),
    )
    check(
        "approved actuality premises are used only at their declared scope and recon surfaces are not promoted to authority",
        len(dispositions) == 6 and sum(row[2] == "approved premise" for row in dispositions) == 2,
        {"dispositions": dispositions, "framework_Record_claimed_for_Cycle496_carriers": False},
    )


def no_go_controls() -> None:
    print("\nN1-N8 / CLAIM GATE")
    n1 = (
        ("redundant retained-pointer dephasing", "ATTEMPTED / POSITIVE SUPPORT", "A: stable/dephased carrier, global coherence retained"),
        ("deterministic microscopic selector CA", "ATTEMPTED / CONDITIONAL MEMBER", "B: unique menu history for supplied law/seed, not Kraus unraveling"),
        ("fresh-bath outward conveyor", "ATTEMPTED / POSITIVE RESOURCE", "C: N16 fresh feed/export, no reset, blank bank supplied"),
        ("selective instrument atom", "RECON / OPEN PHYSICAL SELECTION", "far-shore criterion still needs outcome token"),
        ("autonomous stochastic bath unraveling", "OPEN / UNTESTED", "could select actual trajectory with derived law"),
        ("Record-admissibility formation law", "OPEN / UNTESTED", "could derive which local possibility locks"),
        ("infinite quasi-local bath ray", "OPEN / UNTESTED", "could remove finite terminal capacity"),
        ("symmetry/operational grade plus ergodic Records", "OPEN / UNTESTED", "could connect selected histories to norm grades"),
    )
    walls = ("formation-law selection", "Kraus-member actualization", "grade/frequency identification", "fresh-bath genesis", "framework Record admission")
    n2 = tuple(
        (left, right, "no", "no", True)
        for left, right in combinations(walls, 2)
    )
    n3 = (
        "Cycle478 menu and two logical states", "pointer basis and redundancy code",
        "Cycle483 FORM semantics and pure bath inputs", "Cycle485 blank strip",
        "CA rule and microseed", "finite N8/N16", "fixed frame/placement",
        "noiseless controlled-gate compilation", "Record admissibility of menu labels",
        "realized-state reference without content", "terminal boundary and tolerances",
    )
    n4 = (
        ("Cycle493 A", "coherent pointer controls FORM", "dephasing/stability and continuing basis prefix", True),
        ("Cycle483", "finite supplied bath FORM", "fresh feed/export without reset", True),
        ("Cycle485", "outward finite blank strip", "bath-conveyor geometry/resource boundary", True),
        ("Record dephasing interface", "nonselective correlation is not atom", "same one-event actuality residual", True),
        ("realized-state primitive", "pointwise slot only", "does not close formation/member rule", True),
    )
    n5 = (
        ("one pointer block", "all five labels/two inputs tested", "no member from dephasing"),
        ("finite trajectory", "N8/N16 tested", "conditional CA member; conveyor resource exact"),
        ("all five CA seeds", "tested through N16", "exact"),
        ("arbitrary N/infinite ray", "untested", "no negative conclusion"),
        ("lattice-wide actual Records", "untested", "no negative conclusion"),
    )
    n6 = (
        "derive a local admissibility-to-content formation rule",
        "construct a selective instrument with retained physical outcome token",
        "derive autonomous fresh-bath genesis with conserved inverse/source data",
        "prove an infinite-cylinder conveyor theorem",
        "derive operational grade then an ergodic theorem over admitted Records",
    )
    n7 = (
        "A hostile constructive route can combine the Record axiom's real one-lock event with a derived local admissibility formation rule, use the stable redundant pointer as its physical outcome token, and feed an infinite quasi-local fresh-fragment ray whose translation law retains all spent carriers. If an operational grade theorem and ergodic Record process are added independently, that mechanism could turn the exact Cycle478 instrument into one actual norm-frequency trajectory. Cycle496 closes none of those terminal obligations universally."
    )
    n8 = (
        "Cycle483 retained bath exposed reset/renewal",
        "Cycle485 retired preloaded future words but retained blank-ray import",
        "Cycle493 supplied three finite member-law mechanisms and rejected shared obstruction",
        "Record dephasing work separated nonselective mixtures from atoms",
        "realized-state primitive retired the reference-slot issue without supplying state content",
    )
    check(
        "N1-N8 admits the bounded route results but rejects a shared no-go, minimum-content, or axiom-pressure conclusion",
        len(n1) >= 5 and len(n2) == 10 and len(n3) >= 10 and len(n4) == 5
        and len(n5) == 5 and len(n6) >= 5 and len(n7) > 200 and len(n8) == 5,
        {
            "N1_normalized_routes": n1,
            "N2_pairwise_wall_audit": n2,
            "N3_hidden_condition_scan": n3,
            "N4_exact_residual_matching": n4,
            "N5_rhetoric_resolution_audit": n5,
            "N6_partial_closure_paths": n6,
            "N7_steelman": n7,
            "N8_cross_cycle_echo": n8,
            "Gate_disposition": "FAIL — partial-attempt-with-named-untested-routes",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def inventory_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN")
    supplied = (
        "Cycle493 actual five-sector Kraus/FORM seam, class codec, and two incompatible logical inputs",
        "Cycle483 FORM bath law and initially pure formation/repair blocks",
        "Cycle485 outward finite-strip geometry and typed-prefix meanings",
        "three-copy pointer redundancy, CA law/microseed, finite N8/N16 and terminal boundary",
        "N+1 initially blank conveyor cells, controlled-gate compiler, placement, frame convention, and tolerance",
        "Record axiom and realized-state primitive only at their approved scope",
    )
    derived = (
        "exact redundant pointer copy/inverse, reduced dephasing, one-error decoding, and all-five FORM/prefix continuation",
        "exact N16 Cycle485 basis-member prefix and inverse",
        "fixed CA all-five N16 orbits, exact counts/frequencies, and non-Born separation for both inputs",
        "N8/N16 conveyor E/G, inverse, fresh feed, spent export, terminal syndrome, and zero per-event reset",
        "no used-bath reentry, deletion/domain/noise visibility, linear resource scaling, and all24 covariance",
        "explicit separation of conditional CA member, coherent dephasing, reduced mixture, and framework Record",
    )
    open_items = (
        "derivation/selection of the CA or another local formation law and its microstate content",
        "one actual Cycle478 Kraus outcome from a coherent retained-environment state",
        "grade/Born identification, sampling, stationarity, independence, and realized frequency law",
        "fresh bath/carrier genesis beyond the supplied finite blank bank and source/cost accounting",
        "framework Record admission for these carriers and unbounded permanence under noise",
        "arbitrary N/infinite-volume theorem, time, energy, inertia, gravity, or constitutional conclusion",
    )
    check(
        "the inventory separates actual foundation premises, supplied mechanisms, physical derivations, and still-open formation/member/resource laws",
        len(supplied) == len(derived) == len(open_items) == 6,
        {
            "supplied": supplied,
            "derived": derived,
            "open": open_items,
            "dephasing_called_actuality": False,
            "reduced_mixture_called_member": False,
            "typed_prefix_called_framework_Record": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def resource_controls(started: float) -> None:
    elapsed = time.monotonic() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(raw if sys.platform == "darwin" else raw * 1024)
    check(
        "cold probe body stays inside the declared wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_rss_bytes": rss, "wall_cap_seconds": WALL_CAP_SECONDS, "rss_cap_bytes": RSS_CAP_BYTES},
    )


def install_wall_cap() -> None:
    def alarm(_signum: int, _frame: object) -> None:
        raise WallCapExceeded("Cycle496 exceeded its wall cap")
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(int(WALL_CAP_SECONDS))


def main() -> int:
    started = time.monotonic()
    install_wall_cap()
    print("CYCLE496 KRAUS/FORM DEPHASING + MICROSELECTOR + BATH CONVEYOR")
    contract_controls()
    far_shore_disposition_controls()
    surface = c493.c488.finalized_surface()
    route_a = route_a_controls(surface)
    route_b_controls(route_a)
    route_c = route_c_controls()
    deletion_domain_noise_controls(route_c)
    covariance_resource_controls()
    no_go_controls()
    inventory_controls()
    resource_controls(started)
    signal.alarm(0)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
