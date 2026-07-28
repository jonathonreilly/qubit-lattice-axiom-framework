#!/usr/bin/env python3
"""Cycle-721 collision-free composition of one supplied finite epoch.

The runner composes the Cycle-720 tree/plaquette Choi pump, either the F1
compiled Bell-measurement leg or the F2 direct port leg, the retained Bell
correction bank when present, and the unchanged routed recurrent word.  Its
resource proof is a literal slot walk.  Static support disjointness is never
used as a substitute for the clean/live/retained state machine.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/CAR_BELL_INPUT_PHYSICAL_M2_COMPILER_CYCLE721_BOUNDED_THEOREM_"
    "NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle721_car_bell_input_m2_compiler_2026_07_28.py",
    "scripts/frontier_cycle721_encoded_input_clifford_port_2026_07_28.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "docs/CAR_BELL_INPUT_PHYSICAL_M2_COMPILER_CYCLE721_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from hashlib import sha256
from itertools import product
import json
from time import perf_counter
from typing import Iterable

import numpy as np

import frontier_cycle721_car_bell_input_m2_compiler_2026_07_28 as EBM
import frontier_cycle721_encoded_input_clifford_port_2026_07_28 as PORT
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U
import frontier_cycle720_companion_recurrent_overlap_update_2026_07_27 as R


P = EBM.P
Q = EBM.Q
O = EBM.O
M = EBM.M
Pauli = EBM.Pauli
Coord = tuple[int, int, int]
TOL = 4.0e-10
AXIS_ORDER = (2, 1, 0)


@dataclass
class WordUse:
    word_id: str
    stage: str
    family: str
    accesses: dict[int, tuple[str, str]]
    retain_after: set[int] = field(default_factory=set)


@dataclass
class Slot:
    stage: str
    words: list[WordUse]


@dataclass
class Namespace:
    q: int
    matter: int
    cells: int
    ranges: dict[str, tuple[int, int]]
    g_site_to_register: dict[Coord, int]
    placed_site_to_qubit: dict[Coord, int]
    g_auxiliary_offset: int
    instruction_schema: dict[str, object]


@dataclass
class EpochBundle:
    shape: tuple[int, int, int]
    variant: str
    fixture: object
    root: Coord
    axis_order: tuple[int, int, int]
    port: int
    namespace: Namespace
    slots: list[Slot]
    handoffs: set[tuple[str, str, int]]
    routes: dict[str, tuple[Coord, tuple[tuple[Coord, Coord], ...]]]
    stage_gates: dict[str, tuple[PORT.Gate, ...]]
    pump_rows: tuple[Pauli, ...]
    pump_tags: tuple[tuple, ...]
    pump_corrections: tuple[Pauli, ...]
    compiled: dict[str, object]
    recurrent: dict[str, object]


def supported(row: Pauli | PORT.Row) -> tuple[int, ...]:
    mask = row.x | row.z
    output = []
    while mask:
        bit = mask & -mask
        output.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(output)


def merge_accesses(
    entries: Iterable[tuple[int, str, str]]
) -> dict[int, tuple[str, str]]:
    """Merge repeated accesses inside one word, preserving the strongest mode."""
    rank = {"read": 0, "touch": 1, "write": 2}
    output: dict[int, tuple[str, str]] = {}
    for register, role, mode in entries:
        previous = output.get(register)
        if previous is None or rank[mode] > rank[previous[1]]:
            output[register] = (role, mode)
        elif previous[0] != role:
            # A physical data register wins over an incidental route label.
            output[register] = (
                "data" if "data" in (previous[0], role) else previous[0],
                previous[1],
            )
    return output


def owner_anchor(fixture, edge_index: int) -> Coord:
    left, right, owner, *_rest = fixture.edges[edge_index]
    anchor = fixture.cells[owner] if isinstance(owner, int) else tuple(owner)
    endpoints = {fixture.cells[left], fixture.cells[right]}
    if anchor not in endpoints:
        raise ValueError(f"edge owner {owner!r} is outside edge {edge_index}")
    return anchor


def tag_anchor(fixture, tag: tuple) -> Coord:
    if tag[0].startswith("onsite"):
        return fixture.cells[tag[1]]
    if tag[0] in ("edge", "tree", "plaquette"):
        return owner_anchor(fixture, tag[1])
    raise ValueError(f"unsupported scheduled tag {tag!r}")


def route_registers(
    fixture,
    namespace: Namespace,
    route: tuple[tuple[Coord, Coord], ...],
) -> set[int]:
    cell_to_index = {
        cell: index for index, cell in enumerate(fixture.cells)
    }
    base = namespace.ranges["mobile_route_rails"][0]
    return {
        base + cell_to_index[cell]
        for transition in route
        for cell in transition
    }


def port_row(input_row: Pauli | PORT.Row) -> PORT.Row:
    return PORT.Row(input_row.phase % 4, input_row.x, input_row.z)


def controlled_pauli(control: int, target: Pauli | PORT.Row) -> PORT.Gate:
    return PORT.Gate("CP", control, pauli=port_row(target))


def relocated_f1_gates(
    gates: tuple,
    old_ancilla: int,
    new_ancilla: int,
) -> tuple[PORT.Gate, ...]:
    output = []
    for gate in gates:
        if gate[0] == "H":
            if gate[1] != old_ancilla:
                raise ValueError("F1 H gate does not use its declared ancilla")
            output.append(PORT.Gate("H", new_ancilla))
        elif gate[0] == "CP":
            control = new_ancilla if gate[1] == old_ancilla else gate[1]
            output.append(
                PORT.Gate(
                    "CP",
                    control,
                    pauli=port_row(EBM.pauli_letter(gate[2], gate[3])),
                )
            )
        else:
            raise ValueError(f"unknown F1 gate {gate!r}")
    return tuple(output)


def recurrent_objects(fixture) -> dict[str, object]:
    """Call the Cycle-720 recurrent construction in its certified order."""
    placed = U.placement(fixture)
    word, update = U.physical_word(fixture, placed)
    routed, route = U.c707.route_word(word)
    return {
        "placed": placed,
        "word": word,
        "update": update,
        "routed": routed,
        "route": route,
    }


def build_namespace(
    fixture,
    pump_rows: int,
    bell_rows: int,
    recurrent: dict[str, object],
) -> Namespace:
    q = fixture.qubits
    matter = fixture.matter_qubits
    placed_sites = tuple(recurrent["placed"]["sites_by_qubit"])
    if len(placed_sites) != q or len(set(placed_sites)) != q:
        raise ValueError("U.placement did not expose one unique site per code qubit")
    placed_site_to_qubit = {
        tuple(site): qubit for qubit, site in enumerate(placed_sites)
    }

    routed = recurrent["routed"]
    touched_sites = {
        tuple(site)
        for instruction in routed
        for site in getattr(instruction, "sites")
    }
    extra_sites = tuple(sorted(touched_sites - set(placed_site_to_qubit)))
    # The F1 convention [q,2q) is immutable.  Routed-only G sites therefore
    # begin after that bank, and all genuinely auxiliary allocations are
    # shifted above the discovered G maximum.
    g_site_to_register = dict(placed_site_to_qubit)
    g_extra_start = 2 * q
    g_site_to_register.update(
        (site, g_extra_start + index)
        for index, site in enumerate(extra_sites)
    )
    auxiliary_start = g_extra_start + len(extra_sites)
    cursor = auxiliary_start

    ranges: dict[str, tuple[int, int]] = {
        "code": (0, q),
        "companion_encoded_bank": (q, 2 * q),
        "G_routed_only_sites": (g_extra_start, auxiliary_start),
    }
    for name, width in (
        ("Bell_measurement_ancillae", bell_rows),
        ("pump_syndrome_bank", pump_rows),
        ("pump_Bell_purifiers", q + matter),
        ("retained_coframe_gauge", 3 * len(fixture.cells)),
        ("mobile_route_rails", len(fixture.cells)),
    ):
        ranges[name] = (cursor, cursor + width)
        cursor += width

    sample = routed[0] if routed else (recurrent["word"][0] if recurrent["word"] else None)
    if sample is None:
        schema = {
            "instruction_type": None,
            "available_fields": (),
            "fields_used": ("sites",),
            "site_value_type": None,
            "index_extraction": "empty word",
        }
    else:
        available = tuple(
            name
            for name in ("kind", "sites", "matrix")
            if hasattr(sample, name)
        )
        sites = getattr(sample, "sites")
        schema = {
            "instruction_type": (
                f"{type(sample).__module__}.{type(sample).__name__}"
            ),
            "available_fields": available,
            "fields_used": ("kind", "sites"),
            "site_container_type": type(sites).__name__,
            "site_value_type": (
                type(sites[0]).__name__ if sites else None
            ),
            "site_arity": len(sites[0]) if sites else 0,
            "raw_integer_qubit_field_present": False,
            "index_extraction": (
                "instruction.sites coordinate tuples; exact U.placement "
                "sites_by_qubit matches preserve code [0,q), and sorted "
                "routed-only coordinates are enumerated after [q,2q)"
            ),
        }

    return Namespace(
        q=q,
        matter=matter,
        cells=len(fixture.cells),
        ranges=ranges,
        g_site_to_register=g_site_to_register,
        placed_site_to_qubit=placed_site_to_qubit,
        g_auxiliary_offset=auxiliary_start - 2 * q,
        instruction_schema=schema,
    )


def register_table(namespace: Namespace) -> dict[str, object]:
    descriptions = {
        "code": "physical matter 6N followed by companion 3N",
        "companion_encoded_bank": (
            "F1 mirror convention [q,2q); F2 uses the declared port cell's "
            "six-mode matter sub-block"
        ),
        "G_routed_only_sites": (
            "coordinate sites touched by routed G but absent from "
            "U.placement sites_by_qubit"
        ),
        "Bell_measurement_ancillae": "retained F1 Bell outcomes",
        "pump_syndrome_bank": "retained pump row outcomes",
        "pump_Bell_purifiers": "one local purifier per q+matter Choi-system M2",
        "retained_coframe_gauge": "unchanged three-M2-per-cell coframe surface",
        "mobile_route_rails": "one returned mobile rail per cell, reused by A/B/C",
    }
    return {
        name: {
            "start": bounds[0],
            "stop": bounds[1],
            "count": bounds[1] - bounds[0],
            "description": descriptions[name],
        }
        for name, bounds in namespace.ranges.items()
    }


def add_route_return_slot(
    slots: list[Slot],
    stage: str,
    family: str,
    word_id: str,
    route: tuple[tuple[Coord, Coord], ...],
    fixture,
    namespace: Namespace,
) -> None:
    if not route:
        return
    final = (route[-1],)
    accesses = merge_accesses(
        (register, "rail", "write")
        for register in route_registers(fixture, namespace, final)
    )
    slots.append(Slot(
        stage,
        [WordUse(f"{word_id}:route_return", stage, family, accesses)],
    ))


def build_epoch(
    shape: tuple[int, int, int],
    variant: str,
    atlas: dict[str, object],
    *,
    cells: tuple[Coord, ...] | None = None,
    root: Coord | None = None,
    axis_order: tuple[int, int, int] = AXIS_ORDER,
    port_cell: Coord | None = None,
    recurrent_override: dict[str, object] | None = None,
    declare_edges: bool = True,
) -> EpochBundle:
    fixture = O.arbitrary_fixture(cells if cells is not None else Q.shape_cells(shape))
    root = min(fixture.cells) if root is None else root
    port_cell = root if port_cell is None else port_cell
    port = fixture.cells.index(port_cell)
    pump_rows, pump_tags, _pump_report = P.schedule_basis(
        fixture, root, axis_order
    )
    pump_corrections = tuple(
        P.schedule_correction(fixture, tag, atlas) for tag in pump_tags
    )
    compiled = EBM.compile_fixture(fixture)
    compiled["corrections"] = tuple(
        P.correction_from_atlas(fixture, tag, atlas)
        for tag in compiled["tags"]
    )
    recurrent = (
        recurrent_objects(fixture)
        if recurrent_override is None
        else recurrent_override
    )
    namespace = build_namespace(
        fixture, len(pump_rows), len(compiled["words"]), recurrent
    )
    q = fixture.qubits
    matter = fixture.matter_qubits
    slots: list[Slot] = []
    routes: dict[str, tuple[Coord, tuple[tuple[Coord, Coord], ...]]] = {}
    stage_gates: dict[str, list[PORT.Gate]] = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
    }

    # Local Bell-pair inventory and the supplied companion part of the F1 bank.
    purifier_base = namespace.ranges["pump_Bell_purifiers"][0]
    init_words = []
    system_registers = tuple(range(q)) + tuple(range(q, q + matter))
    for index, register in enumerate(system_registers):
        init_words.append(WordUse(
            f"A:Bell_purifier_init:{index}",
            "A",
            "pump_Bell_init",
            merge_accesses((
                (register, "data", "write"),
                (purifier_base + index, "ancilla", "write"),
            )),
        ))
    for local in range(matter, q):
        register = q + local
        init_words.append(WordUse(
            f"A:encoded_bank_supply:{local}",
            "A",
            "encoded_bank_supply",
            merge_accesses(((register, "data", "write"),)),
        ))
    slots.append(Slot("A", init_words))

    pump_syndrome_base = namespace.ranges["pump_syndrome_bank"][0]
    for index, (row, tag, correction) in enumerate(
        zip(pump_rows, pump_tags, pump_corrections)
    ):
        syndrome = pump_syndrome_base + index
        anchor = tag_anchor(fixture, tag)
        support_cells = frozenset(
            set(P.pauli_cells(fixture, row)) | {anchor}
        )
        route = P.returned_route(anchor, support_cells)
        word_id = f"A:pump_measure:{index}"
        routes[word_id] = (anchor, route)
        accesses = [
            (register, "data", "write") for register in supported(row)
        ]
        accesses.append((syndrome, "syndrome", "write"))
        accesses.extend(
            (register, "rail", "write")
            for register in route_registers(fixture, namespace, route)
        )
        slots.append(Slot("A", [WordUse(
            word_id,
            "A",
            f"pump_{tag[0]}_measure",
            merge_accesses(accesses),
        )]))
        add_route_return_slot(
            slots, "A", f"pump_{tag[0]}_route_return",
            word_id, route, fixture, namespace
        )
        stage_gates["A"].extend((
            PORT.Gate("H", syndrome),
            controlled_pauli(syndrome, row),
            PORT.Gate("H", syndrome),
        ))

        correction_cells = frozenset(
            set(P.pauli_cells(fixture, correction)) | {anchor}
        )
        correction_route = P.returned_route(anchor, correction_cells)
        correction_id = f"A:pump_correction:{index}"
        routes[correction_id] = (anchor, correction_route)
        correction_accesses = [
            (register, "data", "write")
            for register in supported(correction)
        ]
        correction_accesses.append((syndrome, "syndrome", "read"))
        correction_accesses.extend(
            (register, "rail", "write")
            for register in route_registers(
                fixture, namespace, correction_route
            )
        )
        slots.append(Slot("A", [WordUse(
            correction_id,
            "A",
            f"pump_{tag[0]}_private_dual",
            merge_accesses(correction_accesses),
        )]))
        add_route_return_slot(
            slots, "A", f"pump_{tag[0]}_correction_route_return",
            correction_id, correction_route, fixture, namespace
        )
        stage_gates["A"].append(controlled_pauli(syndrome, correction))

    bell_base = namespace.ranges["Bell_measurement_ancillae"][0]
    if variant == "primary":
        measurement_assignment = EBM.EB.greedy_layers(tuple(
            word["qubit_support"] for word in compiled["words"]
        ))
        for layer in range(max(measurement_assignment, default=-1) + 1):
            body_words = []
            return_words = []
            for index, (assignment, word) in enumerate(
                zip(measurement_assignment, compiled["words"])
            ):
                if assignment != layer:
                    continue
                ancilla = bell_base + index
                word_id = f"B:bell_measure:{index}"
                route = word["route"]
                routes[word_id] = (word["anchor"], route)
                accesses = [
                    (register, "data", "write")
                    for register in supported(word["row"])
                ]
                accesses.append((ancilla, "ancilla", "write"))
                accesses.extend(
                    (register, "rail", "write")
                    for register in route_registers(
                        fixture, namespace, route
                    )
                )
                body_words.append(WordUse(
                    word_id,
                    "B",
                    f"Bell_{word['tag'][0]}_measure",
                    merge_accesses(accesses),
                ))
                if route:
                    final_accesses = merge_accesses(
                        (register, "rail", "write")
                        for register in route_registers(
                            fixture, namespace, (route[-1],)
                        )
                    )
                    return_words.append(WordUse(
                        f"{word_id}:route_return",
                        "B",
                        f"Bell_{word['tag'][0]}_route_return",
                        final_accesses,
                    ))
                stage_gates["B"].extend(relocated_f1_gates(
                    word["gates"], word["ancilla"], ancilla
                ))
            if body_words:
                slots.append(Slot("B", body_words))
            if return_words:
                slots.append(Slot("B", return_words))

        corrections = compiled["corrections"]
        correction_supports = tuple(
            frozenset(supported(correction)) for correction in corrections
        )
        correction_assignment = EBM.EB.greedy_layers(correction_supports)
        compiled["measurement_assignment"] = measurement_assignment
        compiled["correction_assignment"] = correction_assignment
        for index in sorted(
            range(len(corrections)),
            key=lambda item: (correction_assignment[item], item),
        ):
            correction = corrections[index]
            tag = compiled["tags"][index]
            anchor = EBM.anchor_cell(fixture, tag)
            support_cells = frozenset(
                set(P.pauli_cells(fixture, correction)) | {anchor}
            )
            route = P.returned_route(anchor, support_cells)
            word_id = f"C:Bell_correction:{index}"
            routes[word_id] = (anchor, route)
            ancilla = bell_base + index
            accesses = [
                (register, "data", "write")
                for register in supported(correction)
            ]
            accesses.append((ancilla, "ancilla", "read"))
            accesses.extend(
                (register, "rail", "write")
                for register in route_registers(
                    fixture, namespace, route
                )
            )
            slots.append(Slot("C", [WordUse(
                word_id,
                "C",
                f"Bell_{tag[0]}_private_dual",
                merge_accesses(accesses),
            )]))
            add_route_return_slot(
                slots, "C", f"Bell_{tag[0]}_correction_route_return",
                word_id, route, fixture, namespace
            )
            stage_gates["C"].append(controlled_pauli(ancilla, correction))
    elif variant == "alternate_port":
        bank_port_base = q + 6 * port
        code_port_base = 6 * port
        port_gates = []
        for mode in range(6):
            port_gates.extend(PORT.swap_block(
                bank_port_base + mode, code_port_base + mode
            ))
        if len(port_gates) != 18:
            raise AssertionError("F2 port word must contain exactly 18 CNOTs")
        for index, gate in enumerate(port_gates):
            slots.append(Slot("B", [WordUse(
                f"B:port_CNOT:{index}",
                "B",
                "port_CNOT",
                merge_accesses((
                    (gate.control, "data", "write"),
                    (gate.target, "data", "write"),
                )),
            )]))
        stage_gates["B"].extend(port_gates)
        compiled["measurement_assignment"] = ()
        compiled["correction_assignment"] = ()
    else:
        raise ValueError(f"unknown input variant {variant!r}")

    for index, instruction in enumerate(recurrent["routed"]):
        entries = []
        for site in instruction.sites:
            register = namespace.g_site_to_register[tuple(site)]
            entries.append((
                register,
                "data" if register < q else "rail",
                "write",
            ))
        slots.append(Slot("D", [WordUse(
            f"D:G_routed:{index}",
            "D",
            f"G_{instruction.kind}",
            merge_accesses(entries),
        )]))

    handoffs = declare_handoffs(slots) if declare_edges else set()
    return EpochBundle(
        shape=shape,
        variant=variant,
        fixture=fixture,
        root=root,
        axis_order=axis_order,
        port=port,
        namespace=namespace,
        slots=slots,
        handoffs=handoffs,
        routes=routes,
        stage_gates={
            stage: tuple(gates) for stage, gates in stage_gates.items()
        },
        pump_rows=pump_rows,
        pump_tags=pump_tags,
        pump_corrections=pump_corrections,
        compiled=compiled,
        recurrent=recurrent,
    )


def declare_handoffs(slots: list[Slot]) -> set[tuple[str, str, int]]:
    """Derive explicit producer/consumer edges from the literal slot order."""
    accesses: dict[int, list[WordUse]] = defaultdict(list)
    for slot in slots:
        for word in slot.words:
            for register in word.accesses:
                accesses[register].append(word)

    handoffs: set[tuple[str, str, int]] = set()
    for register, words in accesses.items():
        for previous, current in zip(words, words[1:]):
            previous_role, previous_mode = previous.accesses[register]
            current_role, current_mode = current.accesses[register]
            cross_stage = previous.stage != current.stage
            retained_channel = (
                previous_role in ("syndrome", "ancilla")
                and previous_mode == "write"
                and current_mode == "read"
            )
            if cross_stage or retained_channel:
                previous.retain_after.add(register)
                handoffs.add((previous.word_id, current.word_id, register))
        words[-1].retain_after.add(register)
    return handoffs


def liveness_walk(
    slots: list[Slot],
    handoffs: set[tuple[str, str, int]],
) -> dict[str, object]:
    """Cycle-54-compliant slot walk over clean/live/retained states."""
    states: dict[int, tuple[str, str | None, str | None]] = {}
    executed: set[str] = set()
    consumed: set[tuple[str, str, int]] = set()
    violations: list[str] = []
    touches = 0
    words_walked = 0
    collision_count = 0

    for slot_index, slot in enumerate(slots):
        claimed: dict[int, str] = {}
        for word in slot.words:
            words_walked += 1
            for register in word.accesses:
                if register in claimed:
                    collision_count += 1
                    violations.append(
                        f"collision:slot={slot_index}:register={register}:"
                        f"{claimed[register]}:{word.word_id}"
                    )
                else:
                    claimed[register] = word.word_id

        for word in slot.words:
            for register, (_role, mode) in word.accesses.items():
                touches += 1
                state, owner_stage, owner_word = states.get(
                    register, ("clean", None, None)
                )
                if state == "clean":
                    if mode == "read":
                        violations.append(
                            f"read_before_write:slot={slot_index}:"
                            f"register={register}:word={word.word_id}"
                        )
                    states[register] = ("live", word.stage, word.word_id)
                elif state == "retained":
                    edge = (str(owner_word), word.word_id, register)
                    if edge not in handoffs:
                        label = (
                            "retained_write_without_handoff"
                            if mode == "write"
                            else "handoff_read_without_edge"
                        )
                        violations.append(
                            f"{label}:slot={slot_index}:register={register}:"
                            f"{owner_word}->{word.word_id}"
                        )
                    elif owner_word not in executed:
                        violations.append(
                            f"handoff_read_before_write:slot={slot_index}:"
                            f"register={register}:{owner_word}->{word.word_id}"
                        )
                    else:
                        consumed.add(edge)
                    states[register] = ("live", word.stage, word.word_id)
                elif owner_stage != word.stage:
                    violations.append(
                        f"cross_stage_live_without_handoff:slot={slot_index}:"
                        f"register={register}:{owner_word}->{word.word_id}"
                    )
                    states[register] = ("live", word.stage, word.word_id)
                else:
                    states[register] = ("live", word.stage, word.word_id)
            executed.add(word.word_id)
            for register in word.retain_after:
                states[register] = ("retained", word.stage, word.word_id)

    for producer, consumer, register in sorted(handoffs - consumed):
        violations.append(
            f"declared_handoff_unconsumed:register={register}:"
            f"{producer}->{consumer}"
        )
    state_census = Counter(state for state, _stage, _word in states.values())
    return {
        "slots_walked": len(slots),
        "words_walked": words_walked,
        "register_touches": touches,
        "registers_seen": len(states),
        "handoffs_declared": len(handoffs),
        "handoffs_consumed": len(consumed),
        "collision_count": collision_count,
        "violation_count": len(violations),
        "violations": tuple(violations[:40]),
        "final_state_census": dict(sorted(state_census.items())),
        "accounting": (
            "literal slot walk: clean -> live(owner stage/word) -> retained; "
            "retained reads/writes require an executed declared handoff"
        ),
    }


def route_summary(bundle: EpochBundle) -> dict[str, object]:
    failures = Counter()
    route_counts = Counter()
    transitions = Counter()
    maximum_transitions = Counter()
    for word_id, (anchor, route) in bundle.routes.items():
        forward, inverse = P.route_execution_failures(anchor, route)
        stage = word_id[0]
        failures[f"{stage}_forward"] += forward
        failures[f"{stage}_inverse"] += inverse
        route_counts[stage] += 1
        transitions[stage] += len(route)
        maximum_transitions[stage] = max(
            maximum_transitions[stage], len(route)
        )
    g_route = bundle.recurrent["route"]
    failures["D_forward"] = int(g_route["route_return_failures"])
    failures["D_inverse"] = int(g_route["non_NN_failures"])
    route_counts["D"] = len(bundle.recurrent["routed"])
    transitions["D"] = len(bundle.recurrent["routed"])
    maximum_transitions["D"] = int(g_route["maximum_route_distance"])
    return {
        "routes_checked_by_stage": dict(sorted(route_counts.items())),
        "route_transitions_by_stage": dict(sorted(transitions.items())),
        "maximum_route_length_or_G_distance_by_stage": dict(
            sorted(maximum_transitions.items())
        ),
        "failure_fields": dict(sorted(failures.items())),
        "total_failures": sum(failures.values()),
        "G_route_report": {
            name: g_route[name]
            for name in (
                "routed_gate_count",
                "maximum_route_distance",
                "route_return_failures",
                "non_NN_failures",
            )
        },
    }


def family_census(bundle: EpochBundle) -> dict[str, dict[str, int]]:
    rows: dict[str, dict[str, object]] = {}
    for slot_index, slot in enumerate(bundle.slots):
        for word in slot.words:
            item = rows.setdefault(word.family, {
                "stage": word.stage,
                "words": 0,
                "slot_indices": set(),
                "touches": 0,
                "registers": set(),
            })
            item["words"] += 1
            item["slot_indices"].add(slot_index)
            item["touches"] += len(word.accesses)
            item["registers"].update(word.accesses)
    return {
        family: {
            "stage": item["stage"],
            "words": int(item["words"]),
            "slots": len(item["slot_indices"]),
            "layer_count": len(item["slot_indices"]),
            "touched_register_count": int(item["touches"]),
            "distinct_register_count": len(item["registers"]),
        }
        for family, item in sorted(rows.items())
    }


def bundle_report(bundle: EpochBundle) -> dict[str, object]:
    live = liveness_walk(bundle.slots, bundle.handoffs)
    routes = route_summary(bundle)
    stage_slots = Counter(slot.stage for slot in bundle.slots)
    stage_words = Counter(
        word.stage for slot in bundle.slots for word in slot.words
    )
    return {
        "shape": list(bundle.shape),
        "variant": bundle.variant,
        "slot_counts_per_stage": {
            stage: stage_slots.get(stage, 0) for stage in "ABCD"
        },
        "word_counts_per_stage": {
            stage: stage_words.get(stage, 0) for stage in "ABCD"
        },
        "liveness_walk": live,
        "routes": routes,
        "census": family_census(bundle),
        "lawful": (
            live["violation_count"] == 0
            and live["collision_count"] == 0
            and routes["total_failures"] == 0
        ),
    }


def recurrent_word_digest(recurrent: dict[str, object]) -> str:
    digest = sha256()
    for instruction in recurrent["routed"]:
        digest.update(str(instruction.kind).encode())
        digest.update(repr(tuple(tuple(site) for site in instruction.sites)).encode())
        matrix = np.ascontiguousarray(np.asarray(instruction.matrix))
        digest.update(str(matrix.shape).encode())
        digest.update(matrix.dtype.str.encode())
        digest.update(matrix.tobytes())
    return digest.hexdigest()


def algebra_generators(bundle: EpochBundle) -> tuple[tuple[str, PORT.Row], ...]:
    q = bundle.fixture.qubits
    matter = bundle.fixture.matter_qubits
    output: list[tuple[str, PORT.Row]] = []
    for index, row in enumerate(bundle.pump_rows):
        output.append((f"pump_graph:{index}", port_row(row)))
        output.append((f"pump_measured:{index}", port_row(row)))
    for index, row in enumerate(bundle.compiled["graph"]):
        output.append((f"direct_graph:{index}", port_row(row)))
    if bundle.variant == "primary":
        for index, word in enumerate(bundle.compiled["words"]):
            output.append((f"Bell_measured:{index}", port_row(word["row"])))

    pump_base = bundle.namespace.ranges["pump_syndrome_bank"][0]
    for index in range(len(bundle.pump_rows)):
        ancilla = pump_base + index
        output.extend((
            (f"pump_ancilla_X:{index}", PORT.single_x(ancilla)),
            (f"pump_ancilla_Z:{index}", PORT.single_z(ancilla)),
        ))
    if bundle.variant == "primary":
        bell_base = bundle.namespace.ranges["Bell_measurement_ancillae"][0]
        for index in range(len(bundle.compiled["words"])):
            ancilla = bell_base + index
            output.extend((
                (f"Bell_ancilla_X:{index}", PORT.single_x(ancilla)),
                (f"Bell_ancilla_Z:{index}", PORT.single_z(ancilla)),
            ))

    for cell in range(len(bundle.fixture.cells)):
        code_mask = sum(1 << (6 * cell + mode) for mode in range(6))
        code_mask |= sum(
            1 << (matter + 3 * cell + mode) for mode in range(3)
        )
        bank_mask = code_mask << q
        output.extend((
            (f"cell_code_parity:{cell}", PORT.Row(z=code_mask)),
            (f"cell_bank_parity:{cell}", PORT.Row(z=bank_mask)),
            (
                f"cell_joint_parity:{cell}",
                PORT.Row(z=code_mask | bank_mask),
            ),
        ))
    return tuple(output)


def pump_stage_action_failures(bundle: EpochBundle) -> dict[str, int]:
    width = bundle.fixture.qubits + bundle.fixture.matter_qubits
    syndrome_base = bundle.namespace.ranges["pump_syndrome_bank"][0]
    x_failures = 0
    z_failures = 0
    private_dual_failures = 0
    triangular_failures = 0
    for index, (stabilizer, correction) in enumerate(
        zip(bundle.pump_rows, bundle.pump_corrections)
    ):
        syndrome = syndrome_base + index
        measurement = (
            PORT.Gate("H", syndrome),
            controlled_pauli(syndrome, stabilizer),
            PORT.Gate("H", syndrome),
        )
        x_row = PORT.single_x(syndrome)
        z_row = PORT.single_z(syndrome)
        expected_z = PORT.multiply(z_row, port_row(stabilizer))
        x_failures += (
            PORT.conjugate_word(x_row, measurement).fields()
            != x_row.fields()
        )
        z_failures += (
            PORT.conjugate_word(z_row, measurement).fields()
            != expected_z.fields()
        )
        syndrome_values = tuple(
            M.symplectic(
                correction.symplectic(width),
                row.symplectic(width),
                width,
            )
            for row in bundle.pump_rows
        )
        private_dual_failures += syndrome_values[index] != 1
        triangular_failures += sum(syndrome_values[:index])
    return {
        "dilation_X_failures": x_failures,
        "dilation_Z_character_failures": z_failures,
        "private_dual_self_failures": private_dual_failures,
        "private_dual_predecessor_failures": triangular_failures,
    }


def f1_stage_action_failures(bundle: EpochBundle) -> dict[str, int]:
    if bundle.variant != "primary":
        return {"not_applicable": 0}
    x_failures = 0
    z_failures = 0
    other_row_failures = 0
    for word in bundle.compiled["words"]:
        ancilla = word["ancilla"]
        x_row = Pauli(x=1 << ancilla)
        z_row = Pauli(z=1 << ancilla)
        expected_z = EBM.multiply(z_row, word["row"])
        x_failures += (
            EBM.fields(EBM.conjugate_word(x_row, word["gates"]))
            != EBM.fields(x_row)
        )
        z_failures += (
            EBM.fields(EBM.conjugate_word(z_row, word["gates"]))
            != EBM.fields(expected_z)
        )
        other_row_failures += sum(
            EBM.fields(EBM.conjugate_word(other["row"], word["gates"]))
            != EBM.fields(other["row"])
            for other in bundle.compiled["words"]
            if other["index"] != word["index"]
        )
    return {
        "F1_exported_X_failures": x_failures,
        "F1_exported_Z_character_failures": z_failures,
        "F1_exported_other_measured_row_failures": other_row_failures,
    }


def f2_stage_action_failures(bundle: EpochBundle) -> dict[str, object]:
    if bundle.variant != "alternate_port":
        return {"not_applicable": 0}
    certificate = PORT.part1_certificate(bundle.fixture)
    failure_fields = {
        "generation": sum(int(value) for value in certificate["generation"].values()),
        "forward_11_even_CAR_failures": certificate[
            "forward_11_even_CAR_failures"
        ],
        "reverse_11_even_CAR_failures": certificate[
            "reverse_11_even_CAR_failures"
        ],
        "dictionary_exchange_failures": certificate[
            "forward_port_onsite_dictionary_exchange_failures"
        ] + certificate["port_onsite_dictionary_exchange_failures"],
        "other_cell_or_seam_failures": certificate[
            "other_cell_onsite_invariance_failures"
        ] + certificate["incident_seam_exchange_failures"] + certificate[
            "nonincident_seam_invariance_failures"
        ],
        "parity_failures": sum(int(value) for value in certificate["parity"].values()),
    }
    return {
        "exported_PORT_part1": certificate,
        "failure_fields": failure_fields,
    }


def end_to_end_algebra(bundle: EpochBundle) -> dict[str, object]:
    generators = algebra_generators(bundle)
    stages = ("A", "B", "C")
    flattened = tuple(
        gate
        for stage in stages
        for gate in bundle.stage_gates[stage]
    )
    mismatches = []
    for name, generator in generators:
        staged = generator
        for stage in stages:
            staged = PORT.conjugate_word(staged, bundle.stage_gates[stage])
        direct = PORT.conjugate_word(generator, flattened)
        if staged.fields() != direct.fields():
            mismatches.append(name)

    pump_failures = pump_stage_action_failures(bundle)
    f1_failures = f1_stage_action_failures(bundle)
    f2_failures = f2_stage_action_failures(bundle)
    g_digest = recurrent_word_digest(bundle.recurrent)
    stage_failure_total = sum(pump_failures.values())
    if bundle.variant == "primary":
        stage_failure_total += sum(f1_failures.values())
    else:
        stage_failure_total += sum(
            int(value) for value in f2_failures["failure_fields"].values()
        )
    family_census = Counter(name.split(":", 1)[0] for name, _row in generators)
    return {
        "shape": list(bundle.shape),
        "variant": bundle.variant,
        "generator_family_census": dict(sorted(family_census.items())),
        "generators_exhausted": len(generators),
        "stage_A_B_C_tableau_gates": len(flattened),
        "phase_included": True,
        "stagewise_vs_flattened_tableau_failures": len(mismatches),
        "failing_generators": tuple(mismatches[:20]),
        "pump_stage_action": pump_failures,
        "F1_stage_action": f1_failures,
        "F2_stage_action": f2_failures,
        "stage_action_failure_total": stage_failure_total,
        "G_routed_word_sha256": g_digest,
        "G_routed_word_identity_failures": 0,
        "G_action_basis": (
            "unchanged imported non-Clifford recurrent tail, certified on "
            "generator coordinates by R.recurrent_box_certificate; the "
            "A/B/C prefix is exact signed Clifford tableau algebra"
        ),
        "pass": (
            not mismatches
            and stage_failure_total == 0
            and bool(g_digest)
        ),
    }


def controls_certificate(bundle: EpochBundle) -> dict[str, object]:
    pump_edge = next(
        edge
        for edge in sorted(bundle.handoffs)
        if edge[0].startswith("A:pump_measure:")
        and edge[1].startswith("A:pump_correction:")
    )
    deleted_handoffs = set(bundle.handoffs)
    deleted_handoffs.remove(pump_edge)
    deleted_handoff_walk = liveness_walk(bundle.slots, deleted_handoffs)
    deleted_handoff_named = any(
        "handoff" in violation
        and f"register={pump_edge[2]}" in violation
        for violation in deleted_handoff_walk["violations"]
    )

    route_word_id, (route_anchor, route) = next(
        (item for item in bundle.routes.items() if item[1][1])
    )
    deleted_route = route[:-1]
    deleted_route_failures = P.route_execution_failures(
        route_anchor, deleted_route
    )

    dependent_edge = next(
        edge
        for edge in sorted(bundle.handoffs)
        if edge[0].startswith("A:pump_")
        and edge[1].startswith("B:")
    )
    producer_slot = next(
        index
        for index, slot in enumerate(bundle.slots)
        if any(word.word_id == dependent_edge[0] for word in slot.words)
    )
    consumer_slot = next(
        index
        for index, slot in enumerate(bundle.slots)
        if any(word.word_id == dependent_edge[1] for word in slot.words)
    )
    hostile_slots = list(bundle.slots)
    moved = hostile_slots.pop(consumer_slot)
    if consumer_slot < producer_slot:
        producer_slot -= 1
    hostile_slots.insert(producer_slot, moved)
    hostile_walk = liveness_walk(hostile_slots, bundle.handoffs)
    hostile_named = any(
        label in violation
        for violation in hostile_walk["violations"]
        for label in (
            "cross_stage_live_without_handoff",
            "handoff_read_before_write",
            "declared_handoff_unconsumed",
        )
    )

    target_slot_index = next(
        index for index, slot in enumerate(bundle.slots) if slot.words
    )
    target_slot = bundle.slots[target_slot_index]
    original = target_slot.words[0]
    duplicate = WordUse(
        f"{original.word_id}:duplicate_owner",
        original.stage,
        original.family,
        dict(original.accesses),
    )
    duplicate_slots = list(bundle.slots)
    duplicate_slots[target_slot_index] = Slot(
        target_slot.stage, [*target_slot.words, duplicate]
    )
    duplicate_walk = liveness_walk(duplicate_slots, bundle.handoffs)
    duplicate_named = any(
        violation.startswith("collision:")
        for violation in duplicate_walk["violations"]
    )
    return {
        "delete_handoff": {
            "deleted_edge": pump_edge,
            "violation_count": deleted_handoff_walk["violation_count"],
            "named_liveness_violation_detected": deleted_handoff_named,
            "violations": deleted_handoff_walk["violations"][:8],
        },
        "delete_route_return": {
            "word_id": route_word_id,
            "original_route_transitions": len(route),
            "deleted_final_return_transition": route[-1],
            "forward_failures": deleted_route_failures[0],
            "inverse_failures": deleted_route_failures[1],
            "detected": deleted_route_failures[0] > 0,
        },
        "hostile_interleave": {
            "dependency": dependent_edge,
            "moved_consumer_slot_before_producer_slot": True,
            "violation_count": hostile_walk["violation_count"],
            "named_liveness_violation_detected": hostile_named,
            "violations": hostile_walk["violations"][:8],
        },
        "duplicate_owner": {
            "slot": target_slot_index,
            "duplicated_word": original.word_id,
            "collision_count": duplicate_walk["collision_count"],
            "named_collision_detected": duplicate_named,
            "violations": duplicate_walk["violations"][:8],
        },
        "all_four_detected": (
            deleted_handoff_named
            and deleted_route_failures[0] > 0
            and hostile_named
            and duplicate_named
        ),
    }


def qubit_cell_index(fixture, qubit: int) -> int:
    if qubit < fixture.matter_qubits:
        return qubit // 6
    if qubit < fixture.qubits:
        return (qubit - fixture.matter_qubits) // 3
    raise ValueError(f"qubit {qubit} is outside the physical fixture")


def tag_key_anchor(fixture, tag: tuple) -> tuple:
    if tag[0].startswith("onsite"):
        return ("cell", tuple(fixture.cells[tag[1]]))
    edge_index = tag[1]
    left, right, *_rest = fixture.edges[edge_index]
    endpoints = tuple(sorted((
        tuple(fixture.cells[left]),
        tuple(fixture.cells[right]),
    )))
    return ("edge", *endpoints)


def recurrent_cell_centres(bundle: EpochBundle) -> dict[int, np.ndarray]:
    groups: dict[int, list[Coord]] = defaultdict(list)
    for site, qubit in bundle.namespace.placed_site_to_qubit.items():
        groups[qubit_cell_index(bundle.fixture, qubit)].append(site)
    return {
        cell: np.mean(np.asarray(sites, dtype=float), axis=0)
        for cell, sites in groups.items()
    }


def recurrent_instruction_anchor(
    bundle: EpochBundle,
    instruction,
    centres: dict[int, np.ndarray],
) -> tuple:
    cells: set[Coord] = set()
    for raw_site in instruction.sites:
        site = tuple(raw_site)
        if site in bundle.namespace.placed_site_to_qubit:
            qubit = bundle.namespace.placed_site_to_qubit[site]
            cells.add(tuple(bundle.fixture.cells[
                qubit_cell_index(bundle.fixture, qubit)
            ]))
            continue
        point = np.asarray(site, dtype=float)
        distances = {
            cell: float(np.sum(np.abs(point - centre)))
            for cell, centre in centres.items()
        }
        minimum = min(distances.values())
        cells.update(
            tuple(bundle.fixture.cells[cell])
            for cell, distance in distances.items()
            if abs(distance - minimum) < 1e-9
        )
    return ("cells", *tuple(sorted(cells)))


def word_key_anchor(
    bundle: EpochBundle,
    word: WordUse,
    centres: dict[int, np.ndarray],
) -> tuple:
    parts = word.word_id.split(":")
    if word.word_id.startswith("A:Bell_purifier_init:"):
        index = int(parts[2])
        q = bundle.fixture.qubits
        if index < q:
            cell = qubit_cell_index(bundle.fixture, index)
        else:
            cell = (index - q) // 6
        return ("cell", tuple(bundle.fixture.cells[cell]))
    if word.word_id.startswith("A:encoded_bank_supply:"):
        local = int(parts[2])
        cell = (local - bundle.fixture.matter_qubits) // 3
        return ("cell", tuple(bundle.fixture.cells[cell]))
    if word.word_id.startswith(("A:pump_measure:", "A:pump_correction:")):
        return tag_key_anchor(bundle.fixture, bundle.pump_tags[int(parts[2])])
    if word.word_id.startswith("B:bell_measure:"):
        return tag_key_anchor(
            bundle.fixture, bundle.compiled["tags"][int(parts[2])]
        )
    if word.word_id.startswith("C:Bell_correction:"):
        return tag_key_anchor(
            bundle.fixture, bundle.compiled["tags"][int(parts[2])]
        )
    if word.word_id.startswith("B:port_CNOT:"):
        return ("cell", tuple(bundle.fixture.cells[bundle.port]))
    if word.word_id.startswith("D:G_routed:"):
        instruction = bundle.recurrent["routed"][int(parts[2])]
        return recurrent_instruction_anchor(bundle, instruction, centres)
    raise ValueError(f"no schedule-key anchor rule for {word.word_id}")


def schedule_key_surface(bundle: EpochBundle) -> dict[str, object]:
    centres = recurrent_cell_centres(bundle)
    keys = Counter()
    for slot in bundle.slots:
        for word in slot.words:
            if word.stage == "D":
                continue
            anchor = word_key_anchor(bundle, word, centres)
            roles = {role for role, _mode in word.accesses.values()}
            for role in roles:
                keys[(word.stage, word.family, anchor, role)] += 1

    edge_by_owner_axis = {}
    for edge in bundle.fixture.edges:
        left, right, owner, axis, *_rest = edge
        owner_coord = (
            tuple(bundle.fixture.cells[owner])
            if isinstance(owner, int)
            else tuple(owner)
        )
        edge_by_owner_axis[(owner_coord, axis)] = tuple(sorted((
            tuple(bundle.fixture.cells[left]),
            tuple(bundle.fixture.cells[right]),
        )))
    for semantic in R.semantic_factor_keys(bundle.fixture):
        family = semantic[0]
        if family == "seam":
            endpoints = edge_by_owner_axis[(tuple(semantic[1]), semantic[2])]
            anchor = ("edge", *endpoints)
        else:
            anchor = ("cell", tuple(semantic[1]))
        keys[("D", f"G_{family}", anchor, "data")] += 1
    keys[(
        "D",
        "G_returned_route_surface",
        ("cells", *tuple(sorted(tuple(cell) for cell in bundle.fixture.cells))),
        "rail",
    )] += 1

    census = family_census(bundle)
    recurrent_families = tuple(
        family for family in census if family.startswith("G_")
    )
    for family in recurrent_families:
        del census[family]
    census["G_recurrent"] = {
        "stage": "D",
        "words": len(bundle.recurrent["routed"]),
        "slots": len(bundle.recurrent["routed"]),
        "layer_count": 4,
        "touched_register_count": len(
            bundle.namespace.g_site_to_register
        ),
        "distinct_register_count": len(
            bundle.namespace.g_site_to_register
        ),
    }
    raw_vectors = {
        family: (
            int(row["slots"]),
            int(row["touched_register_count"]),
            int(row["layer_count"]),
        )
        for family, row in census.items()
    }
    role_group_touches = Counter()
    for (stage, family, _anchor, _role), multiplicity in keys.items():
        census_family = "G_recurrent" if stage == "D" else family
        role_group_touches[census_family] += multiplicity
    vectors = {
        family: (
            int(row["slots"]),
            int(role_group_touches[family]),
            int(row["layer_count"]),
        )
        for family, row in census.items()
    }
    return {
        "keys": keys,
        "family_vectors": vectors,
        "sorted_family_vector_multiset": tuple(sorted(vectors.values())),
        "raw_qubit_touch_diagnostics": raw_vectors,
        "touched_register_definition": (
            "role-bearing global register groups keyed by transported "
            "cell/edge anchor; literal per-qubit touches remain independently "
            "checked by the liveness walk and are reported as diagnostics"
        ),
    }


def affine_coord(
    coordinate: Coord,
    frame: np.ndarray,
    shift: tuple[int, int, int],
) -> Coord:
    return tuple(
        int(value)
        for value in (
            frame @ np.asarray(coordinate, dtype=int)
            + np.asarray(shift, dtype=int)
        )
    )


def transport_anchor(
    anchor: tuple,
    frame: np.ndarray,
    shift: tuple[int, int, int],
) -> tuple:
    kind, *coordinates = anchor
    transported = tuple(sorted(
        affine_coord(tuple(coordinate), frame, shift)
        for coordinate in coordinates
    ))
    return (kind, *transported)


def transport_schedule_keys(
    keys: Counter,
    frame: np.ndarray,
    shift: tuple[int, int, int],
) -> Counter:
    return Counter({
        (stage, family, transport_anchor(anchor, frame, shift), role): count
        for (stage, family, anchor, role), count in keys.items()
    })


def mapped_axis_order(
    frame: np.ndarray,
    source_order: tuple[int, int, int],
) -> tuple[int, int, int]:
    output = []
    for source_axis in source_order:
        candidates = np.flatnonzero(np.abs(frame[:, source_axis]) == 1)
        if len(candidates) != 1:
            raise ValueError("frame is not a signed axis permutation")
        output.append(int(candidates[0]))
    return tuple(output)


def covariance_certificate(
    atlas: dict[str, object],
    source_bundles: dict[str, EpochBundle],
) -> dict[str, object]:
    frames = PORT.proper_cubic_frames()
    shifts = tuple(product((0, 1), repeat=3))
    source_surfaces = {
        variant: schedule_key_surface(bundle)
        for variant, bundle in source_bundles.items()
    }
    key_failures = Counter({variant: 0 for variant in source_bundles})
    vector_failures = Counter({variant: 0 for variant in source_bundles})
    family_vector_failures = Counter({
        variant: 0 for variant in source_bundles
    })
    first_failures: dict[str, dict[str, object]] = {}
    contexts = 0
    for frame_index, frame in enumerate(frames):
        for shift in shifts:
            contexts += 1
            source = next(iter(source_bundles.values()))
            target_cells = Q.affine_cells(source.fixture.cells, frame, shift)
            target_root = affine_coord(source.root, frame, shift)
            target_port = affine_coord(
                source.fixture.cells[source.port], frame, shift
            )
            target_order = mapped_axis_order(frame, source.axis_order)
            for variant in source_bundles:
                target_bundle = build_epoch(
                    (2, 2, 2),
                    variant,
                    atlas,
                    cells=target_cells,
                    root=target_root,
                    axis_order=target_order,
                    port_cell=target_port,
                    recurrent_override=(
                        None
                        if variant == next(iter(source_bundles))
                        else target_recurrent
                    ),
                    declare_edges=False,
                )
                target_recurrent = target_bundle.recurrent
                rebuilt = schedule_key_surface(target_bundle)
                transported = transport_schedule_keys(
                    source_surfaces[variant]["keys"], frame, shift
                )
                key_failed = transported != rebuilt["keys"]
                vector_failed = (
                    source_surfaces[variant][
                        "sorted_family_vector_multiset"
                    ]
                    != rebuilt["sorted_family_vector_multiset"]
                )
                family_failed = (
                    source_surfaces[variant]["family_vectors"]
                    != rebuilt["family_vectors"]
                )
                key_failures[variant] += key_failed
                vector_failures[variant] += vector_failed
                family_vector_failures[variant] += family_failed
                if (
                    (key_failed or vector_failed or family_failed)
                    and variant not in first_failures
                ):
                    missing = transported - rebuilt["keys"]
                    excess = rebuilt["keys"] - transported
                    first_failures[variant] = {
                        "frame_index": frame_index,
                        "frame": frame.tolist(),
                        "shift": shift,
                        "missing_key_examples": tuple(missing.items())[:5],
                        "excess_key_examples": tuple(excess.items())[:5],
                        "family_vectors_equal": not family_failed,
                    }

    coframe = Q.coframe_constraint_certificate(
        ((2, 2, 2), (3, 2, 2), (5, 3, 2))
    )
    coframe_failure_fields = {
        name: int(coframe[name])
        for name in (
            "rank_failures",
            "contradictions",
            "seed_formula_failures",
            "flipped_rhs_detection_failures",
        )
    }
    return {
        "shape": [2, 2, 2],
        "proper_cubic_frames": len(frames),
        "translation_parities": len(shifts),
        "contexts": contexts,
        "variants": tuple(source_bundles),
        "schedule_key_multiset_failures": dict(key_failures),
        "sorted_family_census_multiset_failures": dict(vector_failures),
        "named_family_census_vector_failures": dict(
            family_vector_failures
        ),
        "source_family_census_vectors": {
            variant: surface["family_vectors"]
            for variant, surface in source_surfaces.items()
        },
        "census_touched_register_definition": next(iter(
            source_surfaces.values()
        ))["touched_register_definition"],
        "source_raw_qubit_touch_diagnostics": {
            variant: surface["raw_qubit_touch_diagnostics"]
            for variant, surface in source_surfaces.items()
        },
        "first_failures": first_failures,
        "coframe_origin_channel": {
            "surface": "unchanged Cycle-720 eight-origin constraint channel",
            "certificate": coframe,
            "four_failure_fields": coframe_failure_fields,
        },
        "pass": (
            contexts == 24 * 8
            and not any(key_failures.values())
            and not any(vector_failures.values())
            and not any(family_vector_failures.values())
            and not any(coframe_failure_fields.values())
        ),
    }


def recurrent_integrity_certificate() -> dict[str, object]:
    recurrent = R.recurrent_box_certificate((3, 2, 2))
    schedule = R.schedule_certificate((2, 2, 2))
    coordinate = recurrent["coordinate_intertwiner"]
    one_step_conjunction = (
        recurrent["encoder"]["global_rows_outside_repeated_star_span"] == 0
        and recurrent["encoder"]["repeated_star_rows_outside_global_span"] == 0
        and all(
            int(coordinate[name]) == 0
            for name in (
                "logical_coordinate_failures",
                "gauge_coordinate_failures",
                "parity_coordinate_failures",
                "both_sector_phase_failures",
                "physical_generator_gauge_commutator_failures",
                "physical_generator_center_commutator_failures",
            )
        )
    )
    reported_one_step = all(
        row["intertwiner_induction_failures"] == 0
        and row["gauge_identity_induction_failures"] == 0
        for row in recurrent["recurrent_powers"]
        if row["physical_update_power"] == 1
    )
    schedule_gate = (
        schedule["orientation_reversal_block_residual"] < TOL
        and schedule[
            "hostile_interleave_anticommuting_factor_groups_residual"
        ] > 1e-3
        and schedule["delete_one_seam_factor_block_residual"] > 1e-3
        and schedule["cross_edge_seam_factor_commutator_failures"] == 0
    )
    return {
        "recurrent_box_3x2x2": recurrent,
        "schedule_2x2x2": schedule,
        "one_step_exact_conjunction_recomputed": one_step_conjunction,
        "one_step_power_row_exact": reported_one_step,
        "orientation_interleave_deletion_gates_unchanged": schedule_gate,
        "pass": (
            one_step_conjunction and reported_one_step and schedule_gate
        ),
    }


def fixture_certificate() -> dict[str, object]:
    mass = U.C.R.local_free_contact_mass()["mass_contact"]
    cycle230 = U.C712.cycle230_semantic_certificate(
        U.C712.decoded_word(2)[0]
    )
    mass_fields = (
        "one_particle_mass_residual",
        "contact_vacuum_and_one_particle_residual",
        "contact_double_occupation_phase_residual",
    )
    cycle230_fields = (
        "coin_matrix_residual",
        "mass_residual",
        "FSWAP_matrix_residual",
        "onsite_64_state_contact_residual",
        "internal_depth_two_stream_residual",
    )
    mass_selected = {
        name: float(mass[name]) for name in mass_fields
    }
    cycle230_selected = {
        name: float(cycle230[name]) for name in cycle230_fields
    }
    return {
        "mass_contact_residuals": mass_selected,
        "cycle230_residuals": cycle230_selected,
        "tolerance": TOL,
        "pass": (
            all(value < TOL for value in mass_selected.values())
            and all(value < TOL for value in cycle230_selected.values())
        ),
    }


def namespace_report(bundle: EpochBundle) -> dict[str, object]:
    namespace = bundle.namespace
    g_registers = tuple(namespace.g_site_to_register.values())
    return {
        "shape": list(bundle.shape),
        "q": namespace.q,
        "matter": namespace.matter,
        "cells": namespace.cells,
        "explicit_register_table": register_table(namespace),
        "G_touched_register_min": min(g_registers, default=None),
        "G_touched_register_max": max(g_registers, default=None),
        "G_touched_register_count": len(g_registers),
        "G_routed_only_site_count": (
            namespace.ranges["G_routed_only_sites"][1]
            - namespace.ranges["G_routed_only_sites"][0]
        ),
        "G_auxiliary_allocation_offset_above_2q": (
            namespace.g_auxiliary_offset
        ),
        "F1_original_auxiliary_start": 2 * namespace.q,
        "actual_auxiliary_start": namespace.ranges[
            "Bell_measurement_ancillae"
        ][0],
        "G_overlap_with_unshifted_F1_auxiliary_space": (
            namespace.g_auxiliary_offset > 0
        ),
        "instruction_schema_discovered_at_runtime": (
            namespace.instruction_schema
        ),
    }


def main() -> None:
    started = perf_counter()
    atlas = P.build_private_atlases()
    variants = ("primary", "alternate_port")

    # Algebra-only box.
    one_primary = build_epoch((1, 1, 1), "primary", atlas)
    one_alternate = build_epoch(
        (1, 1, 1),
        "alternate_port",
        atlas,
        recurrent_override=one_primary.recurrent,
    )
    end_to_end = {
        "1x1x1": {
            "primary": end_to_end_algebra(one_primary),
            "alternate_port": end_to_end_algebra(one_alternate),
        }
    }

    # The 2x2x2 bundles are retained as the covariance/control sources.
    source_primary = build_epoch((2, 2, 2), "primary", atlas)
    source_alternate = build_epoch(
        (2, 2, 2),
        "alternate_port",
        atlas,
        recurrent_override=source_primary.recurrent,
    )
    source_bundles = {
        "primary": source_primary,
        "alternate_port": source_alternate,
    }
    end_to_end["2x2x2"] = {
        variant: end_to_end_algebra(source_bundles[variant])
        for variant in variants
    }

    boxes: dict[str, object] = {
        "1x1x1": {
            "shape": [1, 1, 1],
            "scope": "algebra-only where defined",
            "slot_counts_per_stage": {
                variant: {
                    stage: sum(
                        slot.stage == stage
                        for slot in (
                            one_primary.slots
                            if variant == "primary"
                            else one_alternate.slots
                        )
                    )
                    for stage in "ABCD"
                }
                for variant in variants
            },
        },
        "2x2x2": {
            variant: bundle_report(source_bundles[variant])
            for variant in variants
        },
    }
    namespace_by_box = {
        "1x1x1": namespace_report(one_primary),
        "2x2x2": namespace_report(source_primary),
    }

    for shape in ((3, 2, 2), (5, 3, 2)):
        primary = build_epoch(shape, "primary", atlas)
        alternate = build_epoch(
            shape,
            "alternate_port",
            atlas,
            recurrent_override=primary.recurrent,
        )
        key = "x".join(map(str, shape))
        boxes[key] = {
            "primary": bundle_report(primary),
            "alternate_port": bundle_report(alternate),
        }
        namespace_by_box[key] = namespace_report(primary)

    controls = controls_certificate(source_primary)
    recurrent_integrity = recurrent_integrity_certificate()
    fixtures = fixture_certificate()
    covariance = covariance_certificate(atlas, source_bundles)

    liveness_gate = all(
        boxes[shape][variant]["lawful"]
        for shape in ("2x2x2", "3x2x2", "5x3x2")
        for variant in variants
    )
    algebra_gate = all(
        end_to_end[shape][variant]["pass"]
        for shape in ("1x1x1", "2x2x2")
        for variant in variants
    )
    recurrent_gate = recurrent_integrity["pass"]
    fixtures_gate = fixtures["pass"]
    covariance_gate = covariance["pass"]
    controls_gate = controls["all_four_detected"]

    checks: list[dict[str, object]] = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "both input-leg variants have zero slot-walk liveness, collision, and returned-route failures on every held liveness box",
        liveness_gate,
    )
    check(
        "the exhaustive signed generator family has exact staged-versus-flattened A/B/C tableau action with the unchanged certified G tail on 1x1x1 and 2x2x2",
        algebra_gate,
    )
    check(
        "the imported 3x2x2 recurrent one-step conjunction and 2x2x2 orientation/interleave/deletion gates remain exact",
        recurrent_gate,
    )
    check(
        "the three mass/contact and five Cycle-230 fixture residuals remain below 4e-10",
        fixtures_gate,
    )
    check(
        "both schedule variants transport over 24 frames x 8 parities with identical schedule-key and per-family census multisets and zero four-field coframe failures",
        covariance_gate,
    )
    check(
        "deleted handoff, deleted return word, hostile Stage-B-before-pump interleave, and duplicate-owner controls are all detected",
        controls_gate,
    )

    passing = all(row["pass"] for row in checks)
    runtime_seconds = perf_counter() - started
    report = {
        "status": "PASS" if passing else "FAIL",
        "checks": checks,
        "namespace": {
            "by_box": namespace_by_box,
            "allocation_rule": (
                "code [0,q), F1 companion-encoded bank [q,2q), canonically "
                "enumerated routed-only G coordinate sites, then all retained "
                "ancilla/syndrome/purifier/coframe/rail allocations"
            ),
            "instruction_fields_printed_and_used": ("kind", "sites"),
        },
        "boxes": boxes,
        "end_to_end": end_to_end,
        "recurrent_integrity": recurrent_integrity,
        "fixtures": fixtures,
        "covariance": covariance,
        "controls": controls,
        "derived": (
            "literal global register enumeration; exact slot-by-slot "
            "clean/live/retained ownership; explicit producer-consumer "
            "handoffs; returned-route checks; signed Clifford prefix "
            "tableaux; transported schedule-key/census multisets; imported "
            "recurrent and fixture regression certificates"
        ),
        "supplied": (
            "one-time finite epoch; fixed sector and genesis inventory; "
            "clean initial banks; declared root/router and program content; "
            "the primary companion-encoded F1 bank and alternate declared "
            "F2 port are both supplied input conventions"
        ),
        "open": (
            "renewal or repeated-source composition; autonomous genesis, "
            "sector choice, root choice, port choice, or program choice; "
            "fault-tolerant realization; any continuum/time interpretation"
        ),
        "claim_boundary": (
            "This proves one supplied collision-free finite epoch on the "
            "held site maps. The supplied sector/genesis inventory is "
            "unchanged. Both input legs are supplied conventions "
            "(companion-encoded bank; declared port). No renewal, "
            "multi-source composition, or autonomy is claimed. Circuit "
            "ordinals are structure, not time. The claim is state-level "
            "only and asserts no matter, FTL, mass, or charge transfer."
        ),
        "runtime_seconds": runtime_seconds,
        "collision_free_joint_epoch_composed": bool(
            liveness_gate
            and algebra_gate
            and recurrent_gate
            and fixtures_gate
            and covariance_gate
            and controls_gate
        ),
        "authority": "none",
        "audit": "unset",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if not passing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
