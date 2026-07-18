#!/usr/bin/env python3
"""Cycle 361: faithful local close candidate for Cycle-356 continuation words.

Cycle 356 autonomously computed a 30-M2 successor-word candidate from one
root word, blank future payloads, and a repeated 78-M2 continuation program.
This follow-up adds a post-computation close verifier.  It re-transports the
predecessor fields through the seven physical bond lanes, reapplies the local
phase/future-post program, compares all thirty generated target bits, forms a
reversible thirty-input AND transcript, and latches ``close_candidate`` only
on exact equality.  Successful verification uncomputes all match, AND, and
active-residue workspace.  A deleted underlying continuation gate therefore
cannot leave an unchanged successful close transcript.

All fixed X/CNOT/Toffoli layers are state-only and carry explicit cubic M2
coordinates.  Two-site gates are NN and three-site supports are connected NN
subgraphs; longer in-cell moves use explicit NN SWAP routing.  Close remains
a reversible continuation-word certificate.  It is not a Record, occurrence,
actualization, irreversible formation, interval, rate, time, OS/Z4 axis,
energy, or Born law.  K_form stays open.  Authority is none; audit unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from inspect import signature
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_autonomous_record_payload_continuation_nn_route_cycle356_2026_07_18 as c356


c352 = c356.c352
c342 = c356.c342
c317 = c356.c317
LENGTHS = c356.LENGTHS
CHAIN_SIZES = c356.CHAIN_SIZES
HELD_CHAIN_SIZE = c356.HELD_CHAIN_SIZE
RESIDUES = c356.RESIDUES
MATCH_BITS = c342.RECORD_BITS
AND_BITS = MATCH_BITS - 1
ACTIVE_BITS = RESIDUES
CERTIFICATE_BITS = MATCH_BITS + AND_BITS + ACTIVE_BITS + 1
REUSED_ROUTER_M2 = 35
ADDED_CERTIFICATE_M2 = CERTIFICATE_BITS - REUSED_ROUTER_M2
MACROCELL_M2 = c352.MACROCELL_M2 + ADDED_CERTIFICATE_M2
OVERHEAD_M2 = MACROCELL_M2 - c342.RECORD_BITS
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.2e-10
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


@dataclass(frozen=True)
class CloseCell:
    payload: c356.PayloadCell
    match: tuple[int, ...]
    and_chain: tuple[int, ...]
    active_residue: tuple[int, ...]
    close_candidate: int


@dataclass(frozen=True)
class CloseLayout:
    sites: tuple[c352.Site, ...]
    cells: tuple[c352.Macrocell, ...]
    bonds: tuple[tuple[c352.Macrocell, c352.Macrocell], ...]
    layers: tuple[tuple[c352.Gate, ...], ...]
    logical_operations: int
    payload_cells: tuple[c356.PayloadCell, ...]
    program_word: tuple[int, ...]
    close_cells: tuple[CloseCell, ...]


@dataclass(frozen=True)
class BasisState:
    layout: CloseLayout
    bits: tuple[int, ...]


class CloseCircuitBuilder:
    def __init__(self, sites: tuple[c352.Site, ...], cells: tuple[CloseCell, ...]):
        self.sites = sites
        self.cells = cells
        self.layers: list[tuple[c352.Gate, ...]] = []
        self.logical_operations = 0

    def local(self, kind: str, operands, label: str) -> None:
        first = self.cells[0]
        first_operands = tuple(operands(first))
        template = c352.routed_gate(
            kind,
            first_operands,
            first.payload.base,
            self.sites,
            label,
        )
        relative = tuple(
            first.payload.base.path.index(item) for item in first_operands
        )
        rows = []
        for item in self.cells:
            current_operands = tuple(operands(item))
            if tuple(item.payload.base.path.index(value) for value in current_operands) != relative:
                raise RuntimeError("close routing lost homogeneous relative operands")
            position = {
                source: target
                for source, target in zip(
                    first.payload.base.path,
                    item.payload.base.path,
                )
            }
            rows.append(
                tuple(
                    c352.Gate(
                        primitive.kind,
                        tuple(position[site] for site in primitive.sites),
                        tuple(self.sites[position[site]].coord for site in primitive.sites),
                        primitive.label,
                    )
                    for primitive in template
                )
            )
        for column in range(len(rows[0])):
            self.layers.append(tuple(row[column] for row in rows))
        self.logical_operations += 1

    def cross(self, operands, label: str) -> None:
        layer = tuple(
            c352.gate(
                "TOFFOLI",
                tuple(operands(left, right)),
                self.sites,
                label,
            )
            for left, right in zip(self.cells, self.cells[1:])
        )
        if layer:
            self.layers.append(layer)
        self.logical_operations += 1


def append_certificate_sites(
    base: c356.PayloadLayout,
) -> tuple[
    tuple[c352.Site, ...],
    tuple[c352.Macrocell, ...],
    tuple[c356.PayloadCell, ...],
    tuple[CloseCell, ...],
]:
    sites = list(base.sites)
    rows = []
    for payload in base.payload_cells:
        cell = payload.base
        reusable = tuple(
            offset
            for offset in cell.router_ancilla
            if offset not in set(payload.source_ports)
        )[:REUSED_ROUTER_M2]
        if len(reusable) != REUSED_ROUTER_M2:
            raise RuntimeError("insufficient reusable router M2 for close certificate")
        appended = []
        for extension in range(ADDED_CERTIFICATE_M2):
            coord = (
                cell.origin[0] + c352.CELL_X - 1,
                c352.CELL_Y + extension,
                0,
            )
            appended.append(len(sites))
            sites.append(c352.Site(coord, cell.origin))
        new_cell = replace(
            cell,
            path=cell.path + tuple(appended),
            router_ancilla=tuple(
                offset for offset in cell.router_ancilla if offset not in set(reusable)
            ),
        )
        # Active residue and 29/30 match witnesses reuse blank router M2.
        # Only one match, the AND chain, and close add new physical sites.
        active = reusable[:ACTIVE_BITS]
        match = reusable[ACTIVE_BITS:] + (appended[0],)
        and_chain = tuple(appended[1 : 1 + AND_BITS])
        close = appended[-1]
        if len(match) != MATCH_BITS or len(and_chain) != AND_BITS:
            raise RuntimeError("close-certificate inventory drifted")
        rows.append(
            (
                new_cell,
                c356.PayloadCell(new_cell, payload.program, payload.source_ports),
                match,
                and_chain,
                active,
                close,
            )
        )
    cells = tuple(row[0] for row in rows)
    payload = tuple(row[1] for row in rows)
    close_cells = tuple(
        CloseCell(item, row[2], row[3], row[4], row[5])
        for item, row in zip(payload, rows)
    )
    return tuple(sites), cells, payload, close_cells


def certificate_layers(
    sites: tuple[c352.Site, ...],
    close_cells: tuple[CloseCell, ...],
) -> tuple[tuple[tuple[c352.Gate, ...], ...], int]:
    builder = CloseCircuitBuilder(sites, close_cells)

    for residue in range(RESIDUES):
        builder.local(
            "TOFFOLI",
            lambda item, residue=residue: (
                item.payload.base.front,
                item.payload.base.residue[residue],
                item.active_residue[residue],
            ),
            f"close:active-residue:{residue}",
        )

    pairs = c356.transport_pairs()
    for batch_start in range(0, len(pairs), c356.TRANSPORT_LANES):
        batch = pairs[batch_start : batch_start + c356.TRANSPORT_LANES]
        for lane, _ in enumerate(batch):
            builder.local(
                "CNOT",
                lambda item, lane=lane: (
                    item.payload.base.front,
                    item.payload.base.in_form[lane],
                ),
                f"close:front-lane:{batch_start + lane}",
            )
        for lane, (source_bit, _) in enumerate(batch):
            builder.local(
                "TOFFOLI",
                lambda item, lane=lane, source_bit=source_bit: (
                    item.payload.base.successor_out,
                    item.payload.base.record[source_bit],
                    item.payload.source_ports[lane],
                ),
                f"close:source-snapshot:{batch_start + lane}",
            )
        for lane, _ in enumerate(batch):
            builder.cross(
                lambda left, right, lane=lane: (
                    left.payload.source_ports[lane],
                    right.payload.base.in_form[lane],
                    right.payload.base.in_data[lane],
                ),
                f"close:expected-cross:{batch_start + lane}",
            )

        # Convert the transported base bit into the exact programmed expected
        # bit, compare it with the generated target, and retain one match bit.
        for lane, (_, target_bit) in enumerate(batch):
            if 5 <= target_bit < 8:
                phase_bit = target_bit - 5
                for residue in range(RESIDUES):
                    index = c356.program_index(residue, "phase", phase_bit)
                    builder.local(
                        "TOFFOLI",
                        lambda item, lane=lane, residue=residue, index=index: (
                            item.active_residue[residue],
                            item.payload.program[index],
                            item.payload.base.in_data[lane],
                        ),
                        f"close:expected-delta:bit-{target_bit}:residue-{residue}",
                    )
            elif 18 <= target_bit < 28:
                post_bit = target_bit - 18
                for residue in range(RESIDUES):
                    index = c356.program_index(residue, "post", post_bit)
                    builder.local(
                        "TOFFOLI",
                        lambda item, lane=lane, residue=residue, index=index: (
                            item.active_residue[residue],
                            item.payload.program[index],
                            item.payload.base.in_data[lane],
                        ),
                        f"close:expected-delta:bit-{target_bit}:residue-{residue}",
                    )
            builder.local(
                "TOFFOLI",
                lambda item, lane=lane, target_bit=target_bit: (
                    item.payload.base.front,
                    item.payload.base.record[target_bit],
                    item.payload.base.in_data[lane],
                ),
                f"close:difference:{target_bit}",
            )
            builder.local(
                "X",
                lambda item, lane=lane: (item.payload.base.in_data[lane],),
                f"close:negative-control-open:{target_bit}",
            )
            builder.local(
                "TOFFOLI",
                lambda item, lane=lane, target_bit=target_bit: (
                    item.payload.base.front,
                    item.payload.base.in_data[lane],
                    item.match[target_bit],
                ),
                f"close:match:{target_bit}",
            )
            builder.local(
                "X",
                lambda item, lane=lane: (item.payload.base.in_data[lane],),
                f"close:negative-control-close:{target_bit}",
            )
            builder.local(
                "TOFFOLI",
                lambda item, lane=lane, target_bit=target_bit: (
                    item.payload.base.front,
                    item.payload.base.record[target_bit],
                    item.payload.base.in_data[lane],
                ),
                f"close:uncompute-difference:{target_bit}",
            )
            if 5 <= target_bit < 8:
                phase_bit = target_bit - 5
                for residue in reversed(range(RESIDUES)):
                    index = c356.program_index(residue, "phase", phase_bit)
                    builder.local(
                        "TOFFOLI",
                        lambda item, lane=lane, residue=residue, index=index: (
                            item.active_residue[residue],
                            item.payload.program[index],
                            item.payload.base.in_data[lane],
                        ),
                        f"close:uncompute-expected-delta:bit-{target_bit}:residue-{residue}",
                    )
            elif 18 <= target_bit < 28:
                post_bit = target_bit - 18
                for residue in reversed(range(RESIDUES)):
                    index = c356.program_index(residue, "post", post_bit)
                    builder.local(
                        "TOFFOLI",
                        lambda item, lane=lane, residue=residue, index=index: (
                            item.active_residue[residue],
                            item.payload.program[index],
                            item.payload.base.in_data[lane],
                        ),
                        f"close:uncompute-expected-delta:bit-{target_bit}:residue-{residue}",
                    )

        for lane, _ in reversed(tuple(enumerate(batch))):
            builder.cross(
                lambda left, right, lane=lane: (
                    left.payload.source_ports[lane],
                    right.payload.base.in_form[lane],
                    right.payload.base.in_data[lane],
                ),
                f"close:uncompute-expected-cross:{batch_start + lane}",
            )
        for lane, (source_bit, _) in reversed(tuple(enumerate(batch))):
            builder.local(
                "TOFFOLI",
                lambda item, lane=lane, source_bit=source_bit: (
                    item.payload.base.successor_out,
                    item.payload.base.record[source_bit],
                    item.payload.source_ports[lane],
                ),
                f"close:uncompute-source:{batch_start + lane}",
            )
        for lane, _ in reversed(tuple(enumerate(batch))):
            builder.local(
                "CNOT",
                lambda item, lane=lane: (
                    item.payload.base.front,
                    item.payload.base.in_form[lane],
                ),
                f"close:uncompute-front-lane:{batch_start + lane}",
            )

    for residue in reversed(range(RESIDUES)):
        builder.local(
            "TOFFOLI",
            lambda item, residue=residue: (
                item.payload.base.front,
                item.payload.base.residue[residue],
                item.active_residue[residue],
            ),
            f"close:uncompute-active-residue:{residue}",
        )

    builder.local(
        "TOFFOLI",
        lambda item: (item.match[0], item.match[1], item.and_chain[0]),
        "close:and:0",
    )
    for index in range(1, AND_BITS):
        builder.local(
            "TOFFOLI",
            lambda item, index=index: (
                item.and_chain[index - 1],
                item.match[index + 1],
                item.and_chain[index],
            ),
            f"close:and:{index}",
        )
    builder.local(
        "CNOT",
        lambda item: (item.and_chain[-1], item.close_candidate),
        "close:latch",
    )
    for index in reversed(range(1, AND_BITS)):
        builder.local(
            "TOFFOLI",
            lambda item, index=index: (
                item.and_chain[index - 1],
                item.match[index + 1],
                item.and_chain[index],
            ),
            f"close:uncompute-and:{index}",
        )
    builder.local(
        "TOFFOLI",
        lambda item: (item.match[0], item.match[1], item.and_chain[0]),
        "close:uncompute-and:0",
    )
    for bit in range(MATCH_BITS):
        builder.local(
            "TOFFOLI",
            lambda item, bit=bit: (
                item.payload.base.front,
                item.close_candidate,
                item.match[bit],
            ),
            f"close:clear-match:{bit}",
        )
    return tuple(builder.layers), builder.logical_operations


def build_layout(count: int, program: tuple[int, ...]) -> CloseLayout:
    base = c356.build_layout(count, program)
    sites, cells, payload, close_cells = append_certificate_sites(base)
    extra, logical = certificate_layers(sites, close_cells)
    layout = CloseLayout(
        sites,
        cells,
        tuple(zip(cells, cells[1:])),
        base.layers + extra,
        base.logical_operations + logical,
        payload,
        program,
        close_cells,
    )
    c352.validate_layout(layout)
    return layout


def initial_state(
    layout: CloseLayout,
    fixture,
    *,
    formation_hole: int | None = None,
) -> BasisState:
    payload_state = c356.initial_state(layout, fixture, formation_hole=formation_hole)
    values = list(payload_state.bits)
    # The supplied root already carries its source close witness.  Every
    # unoccupied future close candidate remains exactly blank.
    values[layout.close_cells[0].close_candidate] = 1
    return BasisState(layout, tuple(values))


def certificate_workspace_zero(state: BasisState) -> bool:
    return all(
        not any(
            state.bits[offset]
            for offset in item.match + item.and_chain + item.active_residue
        )
        for item in state.layout.close_cells
    )


def step(state: BasisState) -> BasisState:
    """One fixed state-only rule; no host schedule/index enters."""

    c352.validate_basis(state)
    return c352.apply_layers(state, state.layout.layers)  # type: ignore[return-value]


def inverse_step(state: BasisState) -> BasisState:
    return c352.apply_layers(state, state.layout.layers, reverse=True)  # type: ignore[return-value]


def close_report(state: BasisState, fixture) -> dict[str, object]:
    payload = c356.code_report(state, fixture)
    failures = []
    future_blank = 0
    for index, item in enumerate(state.layout.close_cells):
        cell = item.payload.base
        close = state.bits[item.close_candidate]
        occupied = state.bits[cell.occupied]
        seeded = state.bits[cell.seed]
        if index > 0 and not occupied and close == 0:
            future_blank += 1
        if (occupied or seeded) and close != 1:
            failures.append("live-close-candidate-missing")
        if not occupied and not seeded and close:
            failures.append("unoccupied-close-candidate")
        if any(state.bits[offset] for offset in item.match + item.and_chain + item.active_residue):
            failures.append("visible-close-workspace")
    for left, right in state.layout.bonds:
        if state.bits[left.successor_out]:
            try:
                exact = c356.logical_continue(
                    c356.record_word_at(state, left),
                    state.layout.program_word,
                    c352.residue_at(state, right),
                ) == c356.record_word_at(state, right)
            except ValueError:
                exact = False
                failures.append("close-continuation-decode-invalid")
            if state.bits[
                next(
                    item.close_candidate
                    for item in state.layout.close_cells
                    if item.payload.base is right
                )
            ] != int(exact):
                failures.append("close-not-faithful-to-successor-word")
    return {
        "valid": bool(payload["valid"] and not failures),
        "payload": payload,
        "close_failures": tuple(failures),
        "workspace_zero": certificate_workspace_zero(state),
        "future_blank_close_candidates": future_blank,
        "close_candidate_count": sum(
            state.bits[item.close_candidate] for item in state.layout.close_cells
        ),
        "close_constraint_max_cells": 2,
    }


def run_until_done(state: BasisState, fixture) -> tuple[BasisState, int, tuple[bool, ...]]:
    current = state
    trace = [close_report(current, fixture)["valid"]]
    calls = 0
    while not c352.locally_done(current) and calls < len(state.layout.cells) + 2:
        current = step(current)
        calls += 1
        trace.append(close_report(current, fixture)["valid"])
    return current, calls, tuple(bool(item) for item in trace)


def constructive_controls() -> dict[str, object]:
    fixtures = {length: c342.c338.build_fixture(length) for length in LENGTHS}
    programs = {length: c356.program_word(fixture) for length, fixture in fixtures.items()}
    layouts = {count: build_layout(count, programs[3]) for count in CHAIN_SIZES}
    rows = []
    states = {}
    failures = inverse_failures = leakage = 0
    inverse_models = 0
    for length in LENGTHS:
        fixture = fixtures[length]
        program = programs[length]
        for count in CHAIN_SIZES:
            layout = replace(layouts[count], program_word=program)
            initial = initial_state(layout, fixture)
            initial_report = close_report(initial, fixture)
            final, calls, trace = run_until_done(initial, fixture)
            report = close_report(final, fixture)
            inverse_tested = (length, count) in ((3, 6), (6, 18))
            restored = final
            if inverse_tested:
                for _ in range(calls):
                    restored = inverse_step(restored)
                inverse_models += 1
            programs_before = tuple(
                initial.bits[offset]
                for item in layout.payload_cells
                for offset in item.program
            )
            programs_after = tuple(
                final.bits[offset]
                for item in layout.payload_cells
                for offset in item.program
            )
            failures += int(
                not initial_report["valid"]
                or initial_report["future_blank_close_candidates"] != count - 1
                or not report["valid"]
                or report["close_candidate_count"] != count
                or calls != count - 1
                or not all(trace)
            )
            inverse_failures += int(inverse_tested and restored != initial)
            leakage += sum(left != right for left, right in zip(programs_before, programs_after))
            states[(length, count)] = (fixture, initial, final, calls)
            rows.append(
                {
                    "L": length,
                    "N": count,
                    "held_N": count == HELD_CHAIN_SIZE,
                    "step_calls": calls,
                    "initial_blank_future_close_bits": count - 1,
                    "final_future_close_candidates": count - 1,
                    "workspace_zero": report["workspace_zero"],
                    "exact_inverse_replay": inverse_tested,
                    "macrocell_M2": MACROCELL_M2,
                    "constant_overhead_M2": OVERHEAD_M2,
                    "certificate_M2": CERTIFICATE_BITS,
                    "reused_router_M2": REUSED_ROUTER_M2,
                    "added_certificate_M2": ADDED_CERTIFICATE_M2,
                    "logical_operations_per_step": layout.logical_operations,
                    "fixed_layers_per_step": len(layout.layers),
                    "primitive_gates_per_step": sum(len(layer) for layer in layout.layers),
                }
            )
    fixed_failures = int(
        tuple(signature(step).parameters) != ("state",)
        or len({row["logical_operations_per_step"] for row in rows}) != 1
        or len({row["fixed_layers_per_step"] for row in rows}) != 1
        or inverse_models != 2
    )
    check(
        "one fixed connected-NN verifier latches faithful close candidates at L3/L6 and N6/N12/held-N18",
        failures == inverse_failures == leakage == fixed_failures == 0,
        {
            "rows": rows,
            "constructive_failures": failures,
            "inverse_failures": inverse_failures,
            "exact_inverse_models": inverse_models,
            "algebraic_inverse_scope": "all X/CNOT/Toffoli gates self-inverse; reverse every fixed layer and gate",
            "program_leakage": leakage,
            "fixed_rule_failures": fixed_failures,
        },
    )
    return {"fixtures": fixtures, "programs": programs, "layouts": layouts, "states": states, "rows": rows}


def filtered_layers(layout: CloseLayout, label: str) -> tuple[tuple[c352.Gate, ...], ...]:
    return tuple(
        tuple(item for item in layer if item.label != label)
        for layer in layout.layers
    )


def flipped(state: BasisState, offset: int) -> BasisState:
    values = list(state.bits)
    values[offset] ^= 1
    return replace(state, bits=tuple(values))


def deletion_controls(result: dict[str, object]) -> dict[str, object]:
    fixture, initial, ideal_final, _ = result["states"][(3, 6)]
    ideal_one = step(initial)
    target = initial.layout.close_cells[1]
    labels = (
        ("underlying_phase_transition", "payload:delta:residue-1:phase-0"),
        ("underlying_payload_write", "payload:target-write:19"),
        ("underlying_transport", "payload:transport-cross:5"),
        ("close_match", "close:match:5"),
        ("close_latch", "close:latch"),
    )
    rows = []
    failures = 0
    for kind, label in labels:
        layers = filtered_layers(initial.layout, label)
        attacked = c352.apply_layers(initial, layers)
        restored = c352.apply_layers(attacked, layers, reverse=True)
        close = attacked.bits[target.close_candidate]
        visible = not certificate_workspace_zero(attacked) or not close_report(attacked, fixture)["valid"]
        unchanged_transcript = (
            close == ideal_one.bits[target.close_candidate]
            and certificate_workspace_zero(attacked)
            and close_report(attacked, fixture)["valid"]
        )
        failures += int(
            attacked == ideal_one
            or restored != initial
            or not (close == 0 or visible)
            or unchanged_transcript
        )
        rows.append(
            {
                "class": kind,
                "deleted": label,
                "target_close": close,
                "visible_workspace_or_code_failure": visible,
                "unchanged_success_transcript": unchanged_transcript,
                "inverse": restored == initial,
            }
        )

    program_fault = flipped(initial, initial.layout.payload_cells[1].program[0])
    program_out = step(program_fault)
    program_close = program_out.bits[target.close_candidate]
    program_visible = not close_report(program_out, fixture)["valid"]
    malformed_rejections = 0
    malformed = list(initial.bits)
    malformed[initial.layout.cells[0].formation] = 2
    try:
        step(replace(initial, bits=tuple(malformed)))
    except ValueError:
        malformed_rejections += 1
    dirty_rows = []
    for name, candidate in (
        (
            "certificate_active_residue",
            flipped(initial, initial.layout.close_cells[0].active_residue[0]),
        ),
        (
            "payload_transport_input",
            flipped(initial, initial.layout.cells[0].in_data[0]),
        ),
    ):
        input_invalid = not close_report(candidate, fixture)["valid"]
        acted = step(candidate)
        restored = inverse_step(acted)
        output_invalid = not close_report(acted, fixture)["valid"]
        dirty_rows.append(
            {
                "dirty_class": name,
                "input_invalid": input_invalid,
                "same_layers_act": acted != candidate,
                "exact_inverse": restored == candidate,
                "output_invalid": output_invalid,
            }
        )
    check(
        "sampled K_close deletions cannot preserve a clean successful close transcript; dirty workspace acts and inverts under the same fixed layers while local code rejects it",
        failures == 0
        and program_visible
        and malformed_rejections == 1
        and all(
            row["input_invalid"]
            and row["same_layers_act"]
            and row["exact_inverse"]
            and row["output_invalid"]
            for row in dirty_rows
        ),
        {
            "sampled_deletions": rows,
            "sampled_deletion_failures": failures,
            "program_fault_target_close": program_close,
            "program_fault_visible_code_failure": program_visible,
            "basis_shape_type_rejections": malformed_rejections,
            "dirty_workspace_fixed_rule_rows": dirty_rows,
            "untested_individual_deletions": (
                "all individual NN SWAP routing primitives",
                "all zero-valued program-control gates",
                "the remaining 27 payload-bit representatives",
                "the remaining 29 match-bit representatives",
                "the remaining 28 AND-chain representatives",
            ),
        },
    )
    return {"rows": rows, "failures": failures}


def frame_controls(result: dict[str, object]) -> dict[str, object]:
    layouts: dict[int, CloseLayout] = result["layouts"]  # type: ignore[assignment]
    frames = tuple(c317.c311.c235.proper_cubic_frames())
    frame_failures = 0
    for frame in frames:
        matrix = np.asarray(frame, dtype=int)
        frame_failures += int(
            not np.array_equal(matrix.T @ matrix, np.eye(3, dtype=int))
            or round(np.linalg.det(matrix)) != 1
            or not np.all(np.sum(np.abs(matrix), axis=0) == 1)
            or not np.all(np.sum(np.abs(matrix), axis=1) == 1)
        )
    gate_cases = sum(
        sum(len(layer) for layer in layout.layers)
        for layout in layouts.values()
    ) * len(frames)
    layer_cases = sum(len(layout.layers) for layout in layouts.values()) * len(frames)
    program_cases = program_failures = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        for frame in frames:
            carried, _, failures = c342.mapped_fixture(fixture, frame)
            program_failures += failures
            program = c356.program_word(carried)
            chain = c342.make_cylinder_chain(carried, c356.ENDPOINT, RESIDUES)
            for source_residue, cylinder in enumerate(chain):
                source = c342.form_conditional_record(carried, cylinder)
                expected = c342.form_conditional_record(
                    carried, c342.advance_cylinder(carried, cylinder)
                )
                program_failures += int(
                    c356.logical_continue(
                        c342.record_word(source),
                        program,
                        (source_residue + 1) % RESIDUES,
                    )
                    != c342.record_word(expected)
                )
                program_cases += 1
    check(
        "the close verifier, program carrier, and all NN layers are covariant under all 24 proper-cubic frames",
        len(frames) == 24 and frame_failures == program_failures == 0,
        {
            "proper_cubic_frames": len(frames),
            "gate_frame_cases": gate_cases,
            "layer_frame_cases": layer_cases,
            "program_close_cases": program_cases,
            "signed_permutation_failures": frame_failures,
            "program_mapping_failures": program_failures,
            "maximum_gate_support_M2": 3,
        },
    )
    return {"gate_frame_cases": gate_cases}


def inherited_controls() -> dict[str, object]:
    expected_contact = np.diag((np.exp(1j * c317.c311.COUPLING), 1))
    rows = []
    failures = 0
    for length in LENGTHS:
        fixture = c317.physical_fixture(length)
        projector = fixture.full_encoding @ fixture.full_encoding.conj().T
        row = {
            "L": length,
            "contact_residual": float(np.linalg.norm(fixture.contact - expected_contact)),
            "accepted_code_leakage": float(
                np.linalg.norm((np.eye(projector.shape[0]) - projector) @ fixture.two_ray_encoding)
            ),
            "contact_intertwiner": float(
                np.linalg.norm(
                    fixture.physical_contact @ fixture.two_ray_encoding
                    - fixture.two_ray_encoding @ fixture.contact
                )
            ),
        }
        failures += int(
            max(
                row["contact_residual"],
                row["accepted_code_leakage"],
                row["contact_intertwiner"],
            ) > TOL
        )
        rows.append(row)
    species = c317.c311.c219.common_species(-0.3)
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    one_particle = c317.c311.exterior_matrix(species.coin, 1)
    failures += int(np.linalg.norm(one_particle - species.coin) > TOL or mass_residual > TOL)
    check(
        "the faithful close sidecar preserves the inherited one-particle mass and seam contact fixtures",
        failures == 0,
        {
            "rows": rows,
            "one_particle_residual": float(np.linalg.norm(one_particle - species.coin)),
            "mass_relative_residual": mass_residual,
        },
    )
    return {"rows": rows, "mass_residual": mass_residual}


def inventory_controls(result: dict[str, object]) -> dict[str, object]:
    detail = {
        "result": "bounded positive faithful reversible close candidate for Cycle-356 continuation words",
        "supplied": (
            "one root 30-M2 continuation word and its root close witness",
            "one repeated 78-M2 L-specific continuation program per macrocell",
            "one preloaded formation/commit input per macrocell",
            "finite blank NN macrocell capacity and terminal cap",
            "fixed reversible circuit layering",
        ),
        "future_payload_words_supplied": 0,
        "future_close_candidate_bits_initially_one": 0,
        "future_close_candidate_bits_initially_blank_per_model": tuple(
            row["initial_blank_future_close_bits"] for row in result["rows"]
        ),
        "certificate_M2": CERTIFICATE_BITS,
        "reused_router_M2": REUSED_ROUTER_M2,
        "added_certificate_M2": ADDED_CERTIFICATE_M2,
        "match_bits": MATCH_BITS,
        "AND_workspace_bits": AND_BITS,
        "active_residue_workspace_bits": ACTIVE_BITS,
        "close_candidate_bits": 1,
        "macrocell_M2": MACROCELL_M2,
        "constant_overhead_M2": OVERHEAD_M2,
        "close_candidate_is_Record": False,
        "close_candidate_is_occurrence": False,
        "close_candidate_is_actualization": False,
        "irreversible_formation_generated": False,
        "K_form": None,
        "global_scratch_precheck": False,
        "state_dependent_host_branch": False,
        "dirty_workspace_uses_same_installed_layers": True,
        "dirty_workspace_rejected_by_local_code_report": True,
        "circuit_layers_are_time": False,
        "interval": None,
        "rate": None,
        "OS_or_Z4_axis": None,
        "proper_time": None,
        "no_go": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "deletion_scope": "five exact semantic representatives; untested individual classes named in deletion control",
    }
    check(
        "the faithful-close inventory keeps formation/actuality and all time semantics open with authority none and audit unset",
        detail["future_payload_words_supplied"] == 0
        and detail["future_close_candidate_bits_initially_one"] == 0
        and detail["close_candidate_is_Record"] is False
        and detail["close_candidate_is_occurrence"] is False
        and detail["close_candidate_is_actualization"] is False
        and detail["irreversible_formation_generated"] is False
        and detail["K_form"] is None
        and detail["global_scratch_precheck"] is False
        and detail["state_dependent_host_branch"] is False
        and detail["dirty_workspace_uses_same_installed_layers"] is True
        and detail["dirty_workspace_rejected_by_local_code_report"] is True
        and detail["circuit_layers_are_time"] is False
        and detail["interval"] is detail["rate"] is detail["proper_time"] is None
        and detail["no_go"] is detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("=" * 79)
    print("CYCLE 361: AUTONOMOUS RECORD-PAYLOAD FAITHFUL CLOSE NN ROUTE")
    print("authority=none; audit=unset")
    print("close is reversible continuation certification, not formation or time")
    print("=" * 79)
    result = constructive_controls()
    deletion_controls(result)
    frame_controls(result)
    inherited_controls()
    inventory_controls(result)
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_AUTONOMOUS_RECORD_PAYLOAD_FAITHFUL_CLOSE_NN_ROUTE_OPEN")
        return 1
    print("RESULT PHYSICAL_AUTONOMOUS_RECORD_PAYLOAD_FAITHFUL_CLOSE_NN_ROUTE_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
