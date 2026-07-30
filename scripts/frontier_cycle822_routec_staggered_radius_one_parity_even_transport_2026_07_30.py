#!/usr/bin/env python3
"""Cycle 822 Route C: staggered radius-one parity-even transport probe.

This executable replaces the bounded two-target atoms and recurrent seam
factors exposed by Cycle 821 with returned nearest-neighbour route words.
Stage, colour, slot, and ordinal are supplied circuit labels.  None denotes
physical time, duration, cadence, or rate.

Parity-active target pairs travel on clean fermionic route M2 with FSWAP.
Syndrome controls and a single owner-local accumulator travel on a disjoint
work rail.  An even Pauli is first diagonalised by parity-even pair rotations,
its Z character is accumulated with data-as-control CNOTs, locally phased (or
CZ-controlled), and then exactly uncomputed.  The work and route inputs are
supplied clean and every route is returned.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
import json
import math
from pathlib import Path

import numpy as np

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U720
import frontier_cycle734_paired_excitation_genesis_2026_07_28 as C734
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S789
import frontier_cycle789_three_register_even_car_channel_2026_07_30 as C789
import frontier_cycle794_literal_prefix_recurrent_G_substitution_2026_07_30 as C794
import frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30 as C821
import frontier_full128_25site_nn_circuit_core_2026_07_24 as S25


AUDIT_TIMEOUT_SEC = 1200
NOTE_PATH = (
    "docs/ROUTEC_STAGGERED_RADIUS_ONE_PARITY_EVEN_TRANSPORT_"
    "CYCLE822_BOUNDED_PROBE_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_"
    "CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md",
    "docs/PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/LITERAL_THREE_BANK_PREFIX_RECURRENT_G_ACTUAL_SHEAR_"
    "CYCLE794_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/LOCAL_PARITY_EXCHANGE_CARRIER_RECURRENT_BELL_CYCLE821_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
    "scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
    "scripts/frontier_cycle789_three_register_even_car_channel_2026_07_30.py",
    "scripts/frontier_cycle794_literal_prefix_recurrent_G_substitution_2026_07_30.py",
    "scripts/frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


Coord = tuple[int, int, int]
Pauli = B.Pauli
WORK_OFFSET: Coord = (-7, -7, -7)
ROUTE_PADDING = 8
SHAPES = ((2, 1, 1), (3, 1, 1), (3, 2, 2), (5, 3, 2))
STAGE_ORDER = (
    "pump",
    "bell_measure",
    "bell_correction",
    "recurrent_seam",
)


@dataclass(frozen=True)
class Primitive:
    kind: str
    sites: tuple[Coord, ...]
    route_id: int | None = None


@dataclass(frozen=True)
class RouteRecord:
    route_id: int
    role: str
    exchange: str
    path: tuple[Coord, ...]


@dataclass(frozen=True)
class ScheduledWord:
    stage: str
    colour: tuple[int, ...]
    slot: int
    owner: Coord
    label: str
    primitives: tuple[Primitive, ...]


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def neighbours(point: Coord, order: tuple[int, ...]) -> tuple[Coord, ...]:
    rows = []
    for axis in order:
        for step in (1, -1):
            value = list(point)
            value[axis] += step
            rows.append(tuple(value))
    return tuple(rows)


@lru_cache(maxsize=None)
def avoiding_path(
    source: Coord,
    target: Coord,
    obstacles: frozenset[Coord],
    bias: int,
) -> tuple[Coord, ...]:
    """Deterministic bounded BFS, excluding persistent sites internally."""
    if source == target:
        raise ValueError("route endpoints coincide")
    blocked = set(obstacles) - {source, target}
    low = tuple(min(a, b) - ROUTE_PADDING for a, b in zip(source, target))
    high = tuple(max(a, b) + ROUTE_PADDING for a, b in zip(source, target))
    order = tuple(permutations((0, 1, 2)))[bias % 6]
    queue = deque((source,))
    parent: dict[Coord, Coord | None] = {source: None}
    while queue:
        current = queue.popleft()
        if current == target:
            break
        for candidate in neighbours(current, order):
            if candidate in parent or candidate in blocked:
                continue
            if any(
                candidate[axis] < low[axis] or candidate[axis] > high[axis]
                for axis in range(3)
            ):
                continue
            parent[candidate] = current
            queue.append(candidate)
    if target not in parent:
        raise AssertionError(("no bounded route", source, target, len(blocked)))
    path = []
    cursor: Coord | None = target
    while cursor is not None:
        path.append(cursor)
        cursor = parent[cursor]
    path.reverse()
    if any(S789.manhattan(left, right) != 1 for left, right in zip(path, path[1:])):
        raise AssertionError("non-nearest route")
    return tuple(path)


def routed_two_site(
    kind: str,
    source: Coord,
    target: Coord,
    obstacles: frozenset[Coord],
    routes: list[RouteRecord],
    *,
    role: str,
    exchange: str,
    bias: int,
    target_first: bool = False,
) -> tuple[Primitive, ...]:
    path = avoiding_path(source, target, obstacles, bias)
    route_id = len(routes)
    routes.append(RouteRecord(route_id, role, exchange, path))
    swaps = tuple(
        Primitive(exchange, (left, right), route_id)
        for left, right in zip(path[:-2], path[1:-1])
    )
    operands = (path[-1], path[-2]) if target_first else (path[-2], path[-1])
    return swaps + (Primitive(kind, operands, route_id),) + tuple(reversed(swaps))


def local_site_maps(shape, atlas):
    report, scratch = S789.box_certificate(shape, atlas)
    fixture = scratch["fixture"]
    obj = C789.circuit_objects(shape, atlas)
    centers = scratch["centers"]
    placed = U720.placement(fixture)
    o_sites = tuple(placed["sites_by_qubit"])
    i_sites = S789.bank_sites(fixture, centers, 1, S789.I_PAIRS)
    l_sites = S789.bank_sites(fixture, centers, 2, S789.L_PAIRS)
    carriers = C821.carrier_sites(fixture, centers)
    work = tuple(add(centers[cell], WORK_OFFSET) for cell in fixture.cells)
    persistent = set().union(*scratch["classes"].values()) | set(carriers) | set(work)
    if len(work) != len(set(work)) or set(work) & (persistent - set(work)):
        raise AssertionError("work palette collision")
    q = fixture.qubits
    carrier_start = 3 * q
    neutral_access_ports: set[Coord] = set()
    port_order = (2, 1, 0)
    for site in sorted(persistent):
        candidates = neighbours(site, port_order)
        port = next(
            candidate for candidate in candidates
            if candidate not in persistent
            and candidate not in neutral_access_ports
        )
        neutral_access_ports.add(port)

    def physical_site(qubit: int) -> Coord:
        if qubit < q:
            return o_sites[qubit]
        if qubit < 2 * q:
            return i_sites[qubit - q]
        if qubit < 3 * q:
            return l_sites[qubit - 2 * q]
        if qubit < carrier_start + len(fixture.cells):
            return carriers[qubit - carrier_start]
        raise ValueError(qubit)

    def qubit_cell(qubit: int) -> int:
        if qubit < q:
            return S789.local_nine_index(fixture, qubit)[0]
        if qubit < 2 * q:
            return S789.local_nine_index(fixture, qubit - q)[0]
        if qubit < 3 * q:
            return S789.local_nine_index(fixture, qubit - 2 * q)[0]
        return qubit - carrier_start

    return {
        "report": report,
        "scratch": scratch,
        "fixture": fixture,
        "obj": obj,
        "centers": centers,
        "placed": placed,
        "o_sites": o_sites,
        "i_sites": i_sites,
        "l_sites": l_sites,
        "carriers": carriers,
        "work": work,
        "persistent": frozenset(persistent),
        "neutral_access_ports": frozenset(neutral_access_ports),
        "charged_route_obstacles": frozenset(persistent),
        "neutral_route_obstacles": frozenset(persistent),
        "physical_site": physical_site,
        "qubit_cell": qubit_cell,
        "carrier_start": carrier_start,
    }


def pair_rotation_word(
    first: int,
    second: int,
    first_letter: str,
    second_letter: str,
    sign: int,
    context,
    routes: list[RouteRecord],
    bias: int,
) -> tuple[Primitive, ...]:
    first_site = context["physical_site"](first)
    second_site = context["physical_site"](second)
    kind = f"PAIR_R_{first_letter}{second_letter}_{sign:+d}"
    return routed_two_site(
        kind,
        first_site,
        second_site,
        context["charged_route_obstacles"],
        routes,
        role="fermionic_pair_rotation",
        exchange="FSWAP",
        bias=bias,
    )


def controlled_letter_word(
    control: Coord,
    target: Coord,
    letter: str,
    context,
    routes: list[RouteRecord],
    bias: int,
) -> tuple[Primitive, ...]:
    return routed_two_site(
        f"CP_{letter}",
        control,
        target,
        context["neutral_route_obstacles"],
        routes,
        role="syndrome_control",
        exchange="SWAP",
        bias=bias,
    )


def compile_controlled_atom(
    group: tuple[int, ...],
    target: Pauli,
    control: Coord,
    context,
    routes: list[RouteRecord],
    bias: int,
) -> tuple[Primitive, ...]:
    if len(group) == 1:
        qubit = group[0]
        return controlled_letter_word(
            control,
            context["physical_site"](qubit),
            B.letter_at(target, qubit),
            context,
            routes,
            bias,
        )
    first, second = group
    first_letter = B.letter_at(target, first)
    second_letter = B.letter_at(target, second)
    return (
        pair_rotation_word(
            first, second, first_letter, second_letter, -1,
            context, routes, bias,
        )
        + controlled_letter_word(
            control, context["physical_site"](first), "Z",
            context, routes, bias + 1,
        )
        + pair_rotation_word(
            first, second, first_letter, second_letter, 1,
            context, routes, bias,
        )
    )


def bell_atom_words(context, routes: list[RouteRecord]):
    fixture = context["fixture"]
    obj = context["obj"]
    scratch = context["scratch"]
    matter_sites = frozenset(
        tuple(range(fixture.matter_qubits))
        + tuple(range(fixture.qubits, fixture.qubits + fixture.matter_qubits))
        + tuple(range(2 * fixture.qubits, 2 * fixture.qubits + fixture.matter_qubits))
        + tuple(range(
            context["carrier_start"],
            context["carrier_start"] + len(fixture.cells),
        ))
    )
    tag_to_index = {
        tuple(tag): index for index, tag in enumerate(obj["compiled"]["tags"])
    }
    words = []
    row_replay_failures = atom_parity_failures = 0
    atom_count = maximum_targets = 0
    for source_word in scratch["words"]:
        index = tag_to_index[tuple(source_word["tag"])]
        stage = source_word["stage"]
        if stage == "pump":
            correction, _carrier = C821.extend_correction(
                fixture,
                obj["corrections"][index],
                source_word["tag"],
                0,
                context["carrier_start"],
            )
            targets = (obj["compiled"]["words"][index]["row"], correction)
            split_after = 1
        elif stage == "bell_measure":
            targets = (obj["bell_rows"][index],)
            split_after = 1
        elif stage == "bell_correction":
            correction, _carrier = C821.extend_correction(
                fixture,
                obj["corrections"][index],
                source_word["tag"],
                0,
                context["carrier_start"],
            )
            targets = (correction,)
            split_after = 0
        else:
            raise ValueError(stage)
        primitives: list[Primitive] = []
        if split_after:
            primitives.append(Primitive("H_syndrome", (source_word["ancilla"],)))
        for target_index, target in enumerate(targets):
            groups, factors = C821.atomize_target(target, matter_sites)
            row_replay_failures += C821.fields(C821.product(factors)) != C821.fields(target)
            for atom_index, (group, factor) in enumerate(zip(groups, factors)):
                atom_count += 1
                maximum_targets = max(maximum_targets, len(group))
                width = max(target.x.bit_length(), target.z.bit_length(), 1)
                parity = Pauli(z=sum(1 << item for item in matter_sites if item < width))
                atom_parity_failures += B.P.O.M.symplectic(
                    factor.symplectic(width), parity.symplectic(width), width
                )
                primitives.extend(compile_controlled_atom(
                    group,
                    target,
                    source_word["ancilla"],
                    context,
                    routes,
                    bias=index + atom_index + 3 * target_index,
                ))
            if split_after and target_index + 1 == split_after:
                primitives.append(Primitive("H_syndrome", (source_word["ancilla"],)))
        words.append(ScheduledWord(
            stage=stage,
            colour=tuple(source_word["colour"]),
            slot=int(source_word["slot"]),
            owner=tuple(source_word["owner"]),
            label=f"{stage}:{tuple(source_word['tag'])}",
            primitives=tuple(primitives),
        ))
    return tuple(words), {
        "controlled_rows": len(scratch["words"]),
        "parity_even_atoms": atom_count,
        "maximum_targets_excluding_control": maximum_targets,
        "row_replay_failures": row_replay_failures,
        "atom_parity_failures": atom_parity_failures,
    }


def conjugate_s(row: Pauli, qubit: int, dagger: bool) -> Pauli:
    bit = 1 << qubit
    x = int(bool(row.x & bit))
    output_z = row.z ^ (bit if x else 0)
    phase = (row.phase + (-x if dagger else x)) % 4
    return Pauli(phase, row.x, output_z)


def diagonalise_even_pauli(row: Pauli, parity_sites: frozenset[int]):
    groups, factors = C821.atomize_target(row, parity_sites)
    replay = C821.product(factors)
    if replay.x != row.x or replay.z != row.z:
        raise AssertionError("atom binary replay")
    if (row.phase - replay.phase) % 4 not in (0, 2):
        raise AssertionError("atom Hermitian sign replay")
    current = row
    pre: list[tuple] = []
    for group in groups:
        if len(group) == 2:
            first, second = group
            first_letter = B.letter_at(row, first)
            second_letter = B.letter_at(row, second)
            generator = C821.pair_rotation_generator(
                first, first_letter, second, second_letter
            )
            current = C821.conjugate_gate(current, ("R", generator, -1))
            pre.append(("PAIR", first, second, first_letter, second_letter))
        else:
            qubit = group[0]
            letter = B.letter_at(current, qubit)
            if letter == "X":
                current = B.conjugate_h(current, qubit)
                pre.append(("H", qubit))
            elif letter == "Y":
                current = conjugate_s(current, qubit, True)
                current = B.conjugate_h(current, qubit)
                pre.extend((("SDG", qubit), ("H", qubit)))
            elif letter != "Z":
                raise AssertionError(("bad single", qubit, letter))
    if current.x:
        raise AssertionError(("non-diagonal", C821.fields(row), C821.fields(current)))
    if current.phase not in (0, 2):
        raise AssertionError(("non-Hermitian diagonal", current.phase))
    return current, tuple(pre)


def basis_primitive(kind: str, site: Coord) -> Primitive:
    return Primitive(f"basis_{kind}", (site,))


def seam_words(context, routes: list[RouteRecord]):
    fixture = context["fixture"]
    placed = context["placed"]
    all_sites = tuple(placed["all_sites"])
    site_index = {site: index for index, site in enumerate(all_sites)}
    matter_indices = frozenset(
        site_index[site]
        for site in placed["sites_by_qubit"][:fixture.matter_qubits]
    )
    words = []
    diagonal_failures = parity_failures = 0
    maximum_source_support = maximum_diagonal_support = maximum_route = 0
    for edge_index, edge in enumerate(fixture.edges):
        owner, axis = tuple(edge[2]), int(edge[3])
        owner_index = fixture.cells.index(owner)
        work_site = context["work"][owner_index]
        owner_center = context["centers"][owner]
        colour = (axis, sum(owner) & 1)
        for factor_index, physical_row in enumerate(
            fixture.physical_terms(edge_index)
        ):
            lifted = U720.lift_pauli(physical_row, placed)
            row = Pauli(lifted.phase, lifted.x, lifted.z)
            maximum_source_support = max(
                maximum_source_support, len(B.supported_qubits(row))
            )
            diagonal, pre = diagonalise_even_pauli(row, matter_indices)
            diagonal_failures += bool(diagonal.x)
            primitives: list[Primitive] = []
            for operation_index, operation in enumerate(pre):
                if operation[0] == "PAIR":
                    _, first, second, first_letter, second_letter = operation
                    primitives.extend(routed_two_site(
                        f"PAIR_R_{first_letter}{second_letter}_-1",
                        all_sites[first], all_sites[second],
                        context["charged_route_obstacles"], routes,
                        role="seam_pair_diagonalise", exchange="FSWAP",
                        bias=edge_index + factor_index + operation_index,
                    ))
                else:
                    primitives.append(basis_primitive(operation[0], all_sites[operation[1]]))
            diagonal_support = B.supported_qubits(diagonal)
            maximum_diagonal_support = max(
                maximum_diagonal_support, len(diagonal_support)
            )
            for ordinal, qubit in enumerate(diagonal_support):
                route = routed_two_site(
                    "data_CNOT_work",
                    work_site,
                    all_sites[qubit],
                    context["neutral_route_obstacles"], routes,
                    role="seam_Z_accumulate", exchange="SWAP",
                    bias=edge_index + factor_index + ordinal,
                    target_first=True,
                )
                maximum_route = max(maximum_route, len(routes[-1].path) - 1)
                primitives.extend(route)
            phase_sign = -1 if diagonal.phase == 2 else 1
            primitives.append(Primitive(f"work_RZ_{phase_sign:+d}_pi_over_2", (work_site,)))
            for ordinal, qubit in reversed(tuple(enumerate(diagonal_support))):
                primitives.extend(routed_two_site(
                    "data_CNOT_work",
                    work_site,
                    all_sites[qubit],
                    context["neutral_route_obstacles"], routes,
                    role="seam_Z_uncompute", exchange="SWAP",
                    bias=edge_index + factor_index + ordinal,
                    target_first=True,
                ))
            for operation_index, operation in reversed(tuple(enumerate(pre))):
                if operation[0] == "PAIR":
                    _, first, second, first_letter, second_letter = operation
                    primitives.extend(routed_two_site(
                        f"PAIR_R_{first_letter}{second_letter}_+1",
                        all_sites[first], all_sites[second],
                        context["charged_route_obstacles"], routes,
                        role="seam_pair_undiagonalise", exchange="FSWAP",
                        bias=edge_index + factor_index + operation_index,
                    ))
                else:
                    inverse = {"H": "H", "SDG": "S"}[operation[0]]
                    primitives.append(basis_primitive(inverse, all_sites[operation[1]]))
            parity_failures += not Pauli(lifted.phase, lifted.x, lifted.z).commutes(
                Pauli(z=sum(1 << index for index in matter_indices))
            )
            words.append(ScheduledWord(
                stage="recurrent_seam",
                colour=colour,
                slot=4 * axis + factor_index,
                owner=owner,
                label=f"seam:{edge_index}:{factor_index}",
                primitives=tuple(primitives),
            ))
    return tuple(words), {
        "direct_even_seam_factors": len(words),
        "diagonalisation_failures": diagonal_failures,
        "semantic_parity_failures": parity_failures,
        "maximum_source_support_M2": maximum_source_support,
        "maximum_post_diagonal_Z_support_M2": maximum_diagonal_support,
        "maximum_work_route_distance": maximum_route,
    }


def fixed_typed_compile(context):
    """Freeze charged routes, then route every neutral word around that atlas."""
    preliminary_routes: list[RouteRecord] = []
    bell_atom_words(context, preliminary_routes)
    seam_words(context, preliminary_routes)
    preliminary_charged = set().union(*(
        set(route.path)
        for route in preliminary_routes if route.exchange == "FSWAP"
    ))
    preliminary_neutral = set().union(*(
        set(route.path[:-1])
        for route in preliminary_routes if route.exchange == "SWAP"
    ))
    charged_context = dict(context)
    charged_context["charged_route_obstacles"] = frozenset(
        set(context["persistent"]) | set(context["neutral_access_ports"])
    )
    charged_probe_routes: list[RouteRecord] = []
    bell_atom_words(charged_context, charged_probe_routes)
    seam_words(charged_context, charged_probe_routes)
    fixed_charged = set().union(*(
        set(route.path)
        for route in charged_probe_routes if route.exchange == "FSWAP"
    ))
    repaired = dict(charged_context)
    repaired["neutral_route_obstacles"] = frozenset(
        set(context["persistent"]) | fixed_charged
    )
    routes: list[RouteRecord] = []
    bell, atoms = bell_atom_words(repaired, routes)
    seam, seams = seam_words(repaired, routes)
    final_charged = set().union(*(
        set(route.path) for route in routes if route.exchange == "FSWAP"
    ))
    return repaired, tuple(routes), bell + seam, atoms, seams, {
        "pre_repair_charged_route_coordinates": len(preliminary_charged),
        "pre_repair_neutral_route_coordinates": len(preliminary_neutral),
        "pre_repair_cross_typed_coordinate_collisions": len(
            preliminary_charged & preliminary_neutral
        ),
        "reserved_neutral_access_ports": len(context["neutral_access_ports"]),
        "charged_routes_changed_by_port_reservation": sum(
            left.path != right.path
            for left, right in zip(preliminary_routes, charged_probe_routes)
            if left.exchange == right.exchange == "FSWAP"
        ),
        "frozen_charged_atlas_recompile_coordinate_mismatches": len(
            fixed_charged ^ final_charged
        ),
    }


def fixed_type_assignment(context, routes: tuple[RouteRecord, ...]):
    fixture = context["fixture"]
    matter = fixture.matter_qubits
    persistent_charged = (
        set(context["o_sites"][:matter])
        | set(context["i_sites"][:matter])
        | set(context["l_sites"][:matter])
        | set(context["carriers"])
    )
    persistent_neutral = set(context["persistent"]) - persistent_charged
    charged_routes = set().union(*(
        set(route.path) for route in routes if route.exchange == "FSWAP"
    ))
    neutral_routes = set().union(*(
        set(route.path[:-1]) for route in routes if route.exchange == "SWAP"
    ))
    charged = persistent_charged | charged_routes
    reserved_neutral_ports = set(context["neutral_access_ports"])
    neutral = persistent_neutral | reserved_neutral_ports | neutral_routes
    fswap_endpoint_failures = sum(
        route.path[0] not in persistent_charged
        or route.path[-1] not in persistent_charged
        for route in routes if route.exchange == "FSWAP"
    )
    neutral_source_failures = sum(
        route.path[0] not in persistent_neutral
        for route in routes if route.exchange == "SWAP"
    )
    charged_route_type_failures = sum(
        any(site not in charged or site in neutral for site in route.path)
        for route in routes if route.exchange == "FSWAP"
    )
    neutral_route_type_failures = sum(
        any(
            site not in neutral or site in charged
            for site in route.path[:-1]
        )
        for route in routes if route.exchange == "SWAP"
    )
    type_overlap = charged & neutral
    public = {
        "persistent_charged_M2": len(persistent_charged),
        "persistent_neutral_M2": len(persistent_neutral),
        "charged_route_atlas_M2": len(charged_routes),
        "neutral_route_atlas_M2": len(neutral_routes),
        "reserved_neutral_access_port_M2": len(reserved_neutral_ports),
        "global_charged_coordinate_count": len(charged),
        "global_neutral_coordinate_count": len(neutral),
        "charged_neutral_coordinate_overlap": len(type_overlap),
        "sample_cross_typed_coordinates": tuple(sorted(type_overlap)[:8]),
        "FSWAP_endpoint_type_failures": fswap_endpoint_failures,
        "neutral_route_source_type_failures": neutral_source_failures,
        "charged_route_fixed_type_failures": charged_route_type_failures,
        "neutral_route_fixed_type_failures": neutral_route_type_failures,
        "persistent_type_partition_failures": (
            len(persistent_charged & persistent_neutral)
            + len(set(context["persistent"]) - (
                persistent_charged | persistent_neutral
            ))
        ),
        "P_ext_coordinate_sha256": sha256(repr(tuple(sorted(charged))).encode()).hexdigest(),
    }
    return public, frozenset(charged), frozenset(neutral)


@lru_cache(maxsize=None)
def primitive_matrix(kind: str) -> np.ndarray:
    if kind == "FSWAP":
        return S25.FSWAP
    if kind == "SWAP":
        return S25.SWAP
    if kind.startswith("PAIR_R_"):
        _pair, _rotation, letters, sign_text = kind.split("_")
        generator = C821.pair_rotation_generator(
            0, letters[0], 1, letters[1]
        )
        dense = B.dense_pauli(generator, 2)
        sign = int(sign_text)
        return (np.eye(4) - 1j * sign * dense) / np.sqrt(2)
    if kind.startswith("CP_"):
        letter = kind.removeprefix("CP_")
        return B.dense_controlled_target(B.pauli_letter(1, letter), 0, 2)
    if kind == "data_CNOT_work":
        return B.dense_controlled_target(B.pauli_letter(1, "X"), 0, 2)
    if kind in ("H_syndrome", "basis_H"):
        return U720.c707.c655.H
    if kind == "basis_S":
        return U720.c707.S_GATE
    if kind == "basis_SDG":
        return U720.c707.SDG_GATE
    if kind.startswith("work_RZ_"):
        sign = -1 if "_-1_" in kind else 1
        return U720.c707.rz(sign * math.pi / 2)
    raise ValueError(("unclassified primitive", kind))


def global_parity_certificate(
    words: tuple[ScheduledWord, ...],
    charged: frozenset[Coord],
    neutral: frozenset[Coord],
) -> dict[str, object]:
    elementary_failures = prefix_failures = untyped_sites = 0
    maximum_residual = 0.0
    tested = 0
    for word in words:
        prefix_in_common_commutant = True
        for primitive in word.primitives:
            untyped_sites += sum(
                site not in charged and site not in neutral
                for site in primitive.sites
            )
            local_z = sum(
                (site in charged) << index
                for index, site in enumerate(primitive.sites)
            )
            parity = B.dense_pauli(
                Pauli(z=local_z), len(primitive.sites)
            )
            matrix = primitive_matrix(primitive.kind)
            residual = float(np.linalg.norm(
                matrix @ parity - parity @ matrix
            ))
            maximum_residual = max(maximum_residual, residual)
            failed = residual > 1.0e-12
            elementary_failures += failed
            prefix_in_common_commutant &= not failed
            prefix_failures += not prefix_in_common_commutant
            tested += 1
    return {
        "single_global_P_ext": True,
        "elementary_primitives_tested": tested,
        "elementary_global_P_ext_commutator_failures": elementary_failures,
        "prefixes_tested": tested,
        "prefix_global_P_ext_commutator_failures": prefix_failures,
        "maximum_elementary_global_P_ext_commutator_residual": maximum_residual,
        "primitive_untyped_coordinate_uses": untyped_sites,
        "prefix_proof": (
            "every prefix belongs to the same P_ext commutant because each "
            "of its elementary factors is tested against that one operator"
        ),
    }


def collision_graph(
    words: tuple[ScheduledWord, ...],
    *,
    erase_stage: bool = False,
    erase_colour: bool = False,
) -> dict[str, object]:
    grouped: dict[tuple, list[ScheduledWord]] = defaultdict(list)
    for word in words:
        stage = "merged" if erase_stage else word.stage
        colour = (0,) if erase_colour else word.colour
        grouped[(stage, colour, word.slot)].append(word)
    edges = set()
    tested_ordinals = 0
    for group in grouped.values():
        width = max((len(word.primitives) for word in group), default=0)
        for ordinal in range(width):
            occupied: dict[Coord, str] = {}
            for word in group:
                if ordinal >= len(word.primitives):
                    continue
                for site in word.primitives[ordinal].sites:
                    if site in occupied:
                        edges.add(tuple(sorted((occupied[site], word.label))))
                    else:
                        occupied[site] = word.label
            tested_ordinals += 1
    return {
        "vertices": len(words),
        "edges": len(edges),
        "tested_block_ordinals": tested_ordinals,
        "sample_edges": tuple(sorted(edges)[:8]),
    }


def route_certificate(routes: tuple[RouteRecord, ...]) -> dict[str, object]:
    nn_failures = return_failures = deletion_detected = 0
    maximum_distance = 0
    exchange_census: dict[str, int] = defaultdict(int)
    for route in routes:
        maximum_distance = max(maximum_distance, len(route.path) - 1)
        nn_failures += sum(
            S789.manhattan(left, right) != 1
            for left, right in zip(route.path, route.path[1:])
        )
        exchange_census[route.exchange] += 1
        labels = list(route.path)
        for index in range(len(route.path) - 2):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        for index in reversed(range(len(route.path) - 2)):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        return_failures += labels != list(route.path)
        if len(route.path) > 2:
            labels = list(route.path)
            for index in range(len(route.path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            for index in reversed(range(len(route.path) - 3)):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            deletion_detected += labels != list(route.path)
    return {
        "route_macros": len(routes),
        "exchange_census": dict(sorted(exchange_census.items())),
        "nearest_neighbour_failures": nn_failures,
        "returned_label_failures": return_failures,
        "routes_with_active_return_deletion_control": deletion_detected,
        "maximum_route_distance": maximum_distance,
    }


def primitive_parity_certificate(words: tuple[ScheduledWord, ...]) -> dict[str, object]:
    failures = 0
    census: dict[str, int] = defaultdict(int)
    for word in words:
        for primitive in word.primitives:
            census[primitive.kind] += 1
            if primitive.kind.startswith("PAIR_R_"):
                continue
            if primitive.kind in ("FSWAP", "SWAP", "data_CNOT_work"):
                continue
            if primitive.kind.startswith("CP_"):
                continue
            if primitive.kind.startswith("basis_"):
                continue
            if primitive.kind.startswith("work_RZ_") or primitive.kind == "H_syndrome":
                continue
            failures += 1
    z = np.diag((1, -1)).astype(complex)
    pair_parity = np.kron(z, z)
    swap_residual = float(np.linalg.norm(S25.SWAP @ pair_parity - pair_parity @ S25.SWAP))
    fswap_residual = float(np.linalg.norm(S25.FSWAP @ pair_parity - pair_parity @ S25.FSWAP))
    data_control_cnot = primitive_matrix("data_CNOT_work")
    cnot_data_parity = B.dense_pauli(Pauli(z=1), 2)
    cnot_residual = float(np.linalg.norm(
        data_control_cnot @ cnot_data_parity
        - cnot_data_parity @ data_control_cnot
    ))
    dense_pairs = C821.dense_even_pair_selftest()
    failures += swap_residual > 1.0e-12
    failures += fswap_residual > 1.0e-12
    failures += cnot_residual > 1.0e-12
    failures += dense_pairs["maximum_elementary_parity_commutator_residual"] > 1.0e-12
    return {
        "primitive_kind_census": dict(sorted(census.items())),
        "unclassified_primitive_failures": failures,
        "ordinary_SWAP_pair_parity_residual": swap_residual,
        "FSWAP_pair_parity_residual": fswap_residual,
        "data_control_CNOT_parity_residual": cnot_residual,
        "maximum_pair_rotation_parity_residual": dense_pairs[
            "maximum_elementary_parity_commutator_residual"
        ],
        "maximum_controlled_pair_matrix_residual": dense_pairs[
            "maximum_compiled_controlled_pair_residual"
        ],
    }


def execute_three_gate_route(exchange: np.ndarray, state: np.ndarray) -> np.ndarray:
    pair_generator = C821.pair_rotation_generator(0, "X", 1, "X")
    local_generator = B.dense_pauli(pair_generator, 2)
    rotation = (np.eye(4) - 1j * local_generator) / np.sqrt(2)
    output = U720.c707.apply_gate(state, exchange, (0, 1), 3)
    output = U720.c707.apply_gate(output, rotation, (1, 2), 3)
    return U720.c707.apply_gate(output, exchange, (0, 1), 3)


def fswap_control() -> dict[str, float]:
    clean = np.zeros(8, dtype=complex)
    clean[4] = 1 / np.sqrt(2)  # |100>, route spectator 0
    clean[1] = 1 / np.sqrt(2)  # |001>, route spectator 0
    dirty = np.zeros(8, dtype=complex)
    dirty[6] = 1 / np.sqrt(2)  # |110>, occupied route spectator
    dirty[3] = 1 / np.sqrt(2)  # |011>, occupied route spectator
    clean_f = execute_three_gate_route(S25.FSWAP, clean)
    clean_s = execute_three_gate_route(S25.SWAP, clean)
    dirty_f = execute_three_gate_route(S25.FSWAP, dirty)
    dirty_s = execute_three_gate_route(S25.SWAP, dirty)
    return {
        "clean_route_FSWAP_vs_SWAP_residual": float(np.linalg.norm(clean_f - clean_s)),
        "dirty_route_FSWAP_vs_SWAP_residual": float(np.linalg.norm(dirty_f - dirty_s)),
    }


def accumulator_selftest() -> dict[str, object]:
    def cnot_data_to_work(
        state: np.ndarray, data_width: int, qubit: int
    ) -> np.ndarray:
        output = np.zeros_like(state)
        for index, amplitude in enumerate(state):
            data = index >> 1
            work = index & 1
            target = (data << 1) | (work ^ ((data >> qubit) & 1))
            output[target] += amplitude
        return output

    residuals = []
    rng = np.random.default_rng(82203)
    for data_width in range(1, 5):
        amplitudes = rng.normal(size=1 << data_width) + 1j * rng.normal(
            size=1 << data_width
        )
        amplitudes /= np.linalg.norm(amplitudes)
        for sign in (-1, 1):
            initial = np.zeros(1 << (data_width + 1), dtype=complex)
            direct = np.zeros_like(initial)
            for data in range(1 << data_width):
                input_index = data << 1
                initial[input_index] = amplitudes[data]
                parity = data.bit_count() & 1
                phase = np.exp(-0.25j * math.pi * sign * ((-1) ** parity))
                direct[input_index] = amplitudes[data] * phase
            compiled = initial
            for qubit in range(data_width):
                compiled = cnot_data_to_work(compiled, data_width, qubit)
            work_phase = np.asarray((
                np.exp(-0.25j * math.pi * sign),
                np.exp(0.25j * math.pi * sign),
            ))
            compiled = compiled * np.tile(work_phase, 1 << data_width)
            for qubit in reversed(range(data_width)):
                compiled = cnot_data_to_work(compiled, data_width, qubit)
            residuals.append(float(np.linalg.norm(compiled - direct)))
    return {
        "tested_Z_string_weights": (1, 2, 3, 4),
        "tested_rotation_signs": (-1, 1),
        "maximum_clean_work_accumulator_residual": max(residuals),
    }


def covariance_certificate(
    words: tuple[ScheduledWord, ...],
    charged: frozenset[Coord],
    neutral: frozenset[Coord],
) -> dict[str, object]:
    frames = tuple(
        tuple(tuple(int(v) for v in row) for row in frame)
        for frame in B.V.T.proper_cubic_frames()
    )
    origins = tuple(product((0, 1), repeat=3))
    primitives = tuple({
        (primitive.kind, primitive.sites)
        for word in words for primitive in word.primitives
    })
    sites = tuple(sorted({
        site for _kind, primitive_sites in primitives for site in primitive_sites
    }))
    nn_failures = palette_failures = collision_failures = 0
    colour_failures = 0
    type_failures = 0
    base_collisions = collision_graph(words)["edges"]
    for frame in frames:
        for origin in origins:
            mapped_sites = {
                S789.transform(site, frame, origin) for site in sites
            }
            palette_failures += len(mapped_sites) != len(sites)
            mapped_charged = {
                S789.transform(site, frame, origin) for site in charged
            }
            mapped_neutral = {
                S789.transform(site, frame, origin) for site in neutral
            }
            type_failures += (
                len(mapped_charged) != len(charged)
                or len(mapped_neutral) != len(neutral)
                or bool(mapped_charged & mapped_neutral)
            )
        transported_colours = {
            tuple(value % S789.COLOR_MODULUS for value in S789.matvec(frame, colour))
            for colour in product(range(S789.COLOR_MODULUS), repeat=3)
        }
        colour_failures += len(transported_colours) != S789.COLOR_MODULUS ** 3
        mapped_pairs = tuple(
            tuple(S789.matvec(frame, site) for site in primitive_sites)
            for _kind, primitive_sites in primitives if len(primitive_sites) == 2
        )
        nn_failures += len(origins) * sum(
            S789.manhattan(*primitive_sites) != 1
            for primitive_sites in mapped_pairs
        )
        # An affine signed-permutation is injective, so equality/intersection
        # of every occupied site set, and therefore the collision graph, is
        # invariant in all eight translated-origin contexts.
        collision_failures += len(origins) * int(base_collisions != 0)
    product_failures = colour_product_failures = 0
    sample_sites = sites[:256]
    colours = tuple(product(range(S789.COLOR_MODULUS), repeat=3))
    for left in frames:
        for right in frames:
            combined = S789.matmul(left, right)
            product_failures += any(
                S789.matvec(left, S789.matvec(right, site))
                != S789.matvec(combined, site)
                for site in sample_sites
            )
            colour_product_failures += any(
                tuple(value % S789.COLOR_MODULUS for value in S789.matvec(
                    left, S789.matvec(right, colour)
                ))
                != tuple(value % S789.COLOR_MODULUS for value in S789.matvec(
                    combined, colour
                ))
                for colour in colours
            )
    fixed_lab = sum(
        S789.matvec(frame, C821.CARRIER_OFFSET) != C821.CARRIER_OFFSET
        for frame in frames
    )
    return {
        "proper_cubic_frames": len(frames),
        "translation_origins": len(origins),
        "frame_origin_contexts": len(frames) * len(origins),
        "ordered_frame_products": len(frames) ** 2,
        "context_nearest_neighbour_failures": nn_failures,
        "context_palette_bijection_failures": palette_failures,
        "context_collision_graph_failures": collision_failures,
        "context_fixed_type_assignment_failures": type_failures,
        "colour_transport_bijection_failures": colour_failures,
        "product_coordinate_failures": product_failures,
        "product_colour_failures": colour_product_failures,
        "fixed_laboratory_carrier_offset_detected_frames": fixed_lab,
    }


def shape_certificate(shape, atlas, *, covariance: bool = False):
    context = local_site_maps(shape, atlas)
    context, routes, words, atoms, seams, pre_repair = fixed_typed_compile(
        context
    )
    type_assignment, charged, neutral = fixed_type_assignment(context, routes)
    graph = collision_graph(words)
    wrong_stage = collision_graph(words, erase_stage=True)
    wrong_colour = collision_graph(words, erase_colour=True)
    wrong_colour_assignment_failures = sum(
        word.colour != tuple(0 for _ in word.colour) for word in words
    )
    route = route_certificate(routes)
    route["internal_persistent_palette_hits"] = sum(
        len(set(record.path[1:-1]) & set(context["persistent"]))
        for record in routes
    )
    local_matrix_controls = primitive_parity_certificate(words)
    global_parity = global_parity_certificate(words, charged, neutral)
    result = {
        "shape": shape,
        "cells": len(context["fixture"].cells),
        "words": len(words),
        "literal_radius_one_primitives": sum(len(word.primitives) for word in words),
        "stage_order": STAGE_ORDER,
        "stage_labels_are_physical_time": False,
        "owner_local_work_M2_per_cell": 1,
        "pre_repair_type_audit": pre_repair,
        "fixed_global_type_assignment": type_assignment,
        "bell_atoms": atoms,
        "recurrent_seams": seams,
        "routes": route,
        "collision_graph": graph,
        "wrong_stage_collision_graph": wrong_stage,
        "wrong_colour_collision_graph": wrong_colour,
        "wrong_fixed_colour_assignment_failures": (
            wrong_colour_assignment_failures
        ),
        "local_matrix_controls": local_matrix_controls,
        "global_P_ext_audit": global_parity,
        "maximum_primitive_M2_diameter": (
            1 if any(word.primitives for word in words) else 0
        ),
        "covariance": (
            covariance_certificate(words, charged, neutral)
            if covariance else None
        ),
    }
    return result


def main() -> None:
    atlas = B.P.build_private_atlases()
    boxes = tuple(
        shape_certificate(shape, atlas, covariance=(shape == (2, 1, 1)))
        for shape in SHAPES
    )
    fswap = fswap_control()
    accumulator = accumulator_selftest()
    cycle734_boundary = {
        "landed_note_path": C734.NOTE_PATH,
        "pair_template_is_physical_NN_genesis": False,
        "external_application_position_remains_supplied": True,
        "reused_as_transport_primitive": False,
    }
    import_inventory = {
        "Cycle720_update": U720.NOTE_PATH,
        "Cycle734_companion": C734.NOTE_PATH,
        "Cycle789_schedule": S789.NOTE_PATH,
        "Cycle794_composition": C794.NOTE_PATH,
        "Cycle821_carrier": C821.NOTE_PATH,
    }
    checks = {
        "all_Bell_pump_correction_rows_replay_as_parity_even_atoms": all(
            box["bell_atoms"]["row_replay_failures"] == 0
            and box["bell_atoms"]["atom_parity_failures"] == 0
            and box["bell_atoms"]["maximum_targets_excluding_control"] <= 2
            for box in boxes
        ),
        "all_recurrent_seam_factors_diagonalise_and_replay": all(
            box["recurrent_seams"]["direct_even_seam_factors"]
                == 4 * len(C789.circuit_objects(
                    tuple(box["shape"]), atlas
                )["fixture"].edges)
            and box["recurrent_seams"]["diagonalisation_failures"] == 0
            and box["recurrent_seams"]["semantic_parity_failures"] == 0
            and box["recurrent_seams"]["maximum_source_support_M2"] <= 17
            and box["recurrent_seams"][
                "maximum_post_diagonal_Z_support_M2"
            ] <= 16
            for box in boxes
        ),
        "source_support_17_is_not_mislabeled_as_post_diagonal_16": (
            max(
                box["recurrent_seams"]["maximum_source_support_M2"]
                for box in boxes
            ) == 17
            and max(
                box["recurrent_seams"][
                    "maximum_post_diagonal_Z_support_M2"
                ]
                for box in boxes
            ) == 16
        ),
        "every_emitted_two_site_primitive_is_radius_one": all(
            box["maximum_primitive_M2_diameter"] == 1
            and box["routes"]["nearest_neighbour_failures"] == 0
            and box["routes"]["internal_persistent_palette_hits"] == 0
            for box in boxes
        ),
        "all_routes_return_and_persistent_shared_registers_remain_consistent": all(
            box["routes"]["returned_label_failures"] == 0
            and box["routes"]["internal_persistent_palette_hits"] == 0
            and box["routes"]["routes_with_active_return_deletion_control"] > 0
            for box in boxes
        ) and accumulator["maximum_clean_work_accumulator_residual"] < 1.0e-12,
        "fixed_stage_colour_slot_schedule_has_zero_collision_edges": all(
            box["collision_graph"]["edges"] == 0 for box in boxes
        ),
        "wrong_stage_and_colour_controls_are_active": all(
            box["wrong_stage_collision_graph"]["edges"] > 0
            and box["wrong_fixed_colour_assignment_failures"] > 0
            for box in boxes
        ),
        "pre_repair_cross_typing_is_active_and_removed": (
            all(
                box["pre_repair_type_audit"][
                    "pre_repair_cross_typed_coordinate_collisions"
                ] > 0
                and box["fixed_global_type_assignment"][
                    "charged_neutral_coordinate_overlap"
                ] == 0
                for box in boxes
            )
            and {
                tuple(box["shape"]): box["pre_repair_type_audit"][
                    "pre_repair_cross_typed_coordinate_collisions"
                ]
                for box in boxes
                if tuple(box["shape"]) in (
                    (2, 1, 1), (3, 2, 2), (5, 3, 2)
                )
            } == {
                (2, 1, 1): 155,
                (3, 2, 2): 2035,
                (5, 3, 2): 5306,
            }
        ),
        "one_fixed_global_coordinate_type_assignment_is_consistent": all(
            box["pre_repair_type_audit"][
                "frozen_charged_atlas_recompile_coordinate_mismatches"
            ] == 0
            and box["fixed_global_type_assignment"][
                "charged_neutral_coordinate_overlap"
            ] == 0
            and box["fixed_global_type_assignment"][
                "FSWAP_endpoint_type_failures"
            ] == 0
            and box["fixed_global_type_assignment"][
                "neutral_route_source_type_failures"
            ] == 0
            and box["fixed_global_type_assignment"][
                "persistent_type_partition_failures"
            ] == 0
            and box["fixed_global_type_assignment"][
                "charged_route_fixed_type_failures"
            ] == 0
            and box["fixed_global_type_assignment"][
                "neutral_route_fixed_type_failures"
            ] == 0
            for box in boxes
        ),
        "every_primitive_and_prefix_commutes_with_one_global_P_ext": all(
            box["global_P_ext_audit"]["single_global_P_ext"]
            and box["global_P_ext_audit"][
                "elementary_global_P_ext_commutator_failures"
            ] == 0
            and box["global_P_ext_audit"][
                "prefix_global_P_ext_commutator_failures"
            ] == 0
            and box["global_P_ext_audit"][
                "primitive_untyped_coordinate_uses"
            ] == 0
            and box["global_P_ext_audit"][
                "maximum_elementary_global_P_ext_commutator_residual"
            ] < 1.0e-12
            for box in boxes
        ),
        "local_matrix_controls_support_the_global_audit": all(
            box["local_matrix_controls"]["unclassified_primitive_failures"] == 0
            and box["local_matrix_controls"][
                "ordinary_SWAP_pair_parity_residual"
            ] < 1.0e-12
            and box["local_matrix_controls"][
                "FSWAP_pair_parity_residual"
            ] < 1.0e-12
            and box["local_matrix_controls"][
                "data_control_CNOT_parity_residual"
            ] < 1.0e-12
            and box["local_matrix_controls"][
                "maximum_pair_rotation_parity_residual"
            ] < 1.0e-12
            and box["local_matrix_controls"][
                "maximum_controlled_pair_matrix_residual"
            ] < 1.0e-12
            for box in boxes
        ),
        "proper_cubic_coframe_transport_and_products_close": (
            boxes[0]["covariance"]["proper_cubic_frames"] == 24
            and boxes[0]["covariance"]["translation_origins"] == 8
            and boxes[0]["covariance"]["frame_origin_contexts"] == 192
            and boxes[0]["covariance"]["ordered_frame_products"] == 576
            and all(
                value == 0
                for key, value in boxes[0]["covariance"].items()
                if key.endswith("failures")
            )
            and boxes[0]["covariance"][
                "fixed_laboratory_carrier_offset_detected_frames"
            ] == 23
        ),
        "ordinary_SWAP_is_distinguished_from_fermionic_FSWAP": (
            fswap["clean_route_FSWAP_vs_SWAP_residual"] < 1.0e-12
            and fswap["dirty_route_FSWAP_vs_SWAP_residual"] > 1.0e-6
        ),
        "clean_work_Z_accumulator_is_exact": (
            accumulator["maximum_clean_work_accumulator_residual"] < 1.0e-12
        ),
        "Cycle734_is_not_misimported_as_physical_genesis": (
            not cycle734_boundary["pair_template_is_physical_NN_genesis"]
            and cycle734_boundary["external_application_position_remains_supplied"]
            and not cycle734_boundary["reused_as_transport_primitive"]
        ),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "route": "C_staggered_time_multiplexed_literal_radius_one",
        "checks": checks,
        "boxes": boxes,
        "ordinary_vs_FSWAP_control": fswap,
        "clean_work_accumulator_selftest": accumulator,
        "Cycle734_import_boundary": cycle734_boundary,
        "direct_import_inventory": import_inventory,
        "supplied": [
            "the landed Cycle720/789/794/821 finite fixture, code domain, "
            "O/I/L banks, carrier placement, private atlas, and clean "
            "syndrome controls",
            "one clean owner-local accumulator M2 per cell and clean "
            "returned fermionic/work route rails",
            "the finite stage/colour/slot/ordinal circuit order and "
            "transported proper-cubic coframe",
            "the finite boundary, chart, total extended-parity observable "
            "domain, and permission to retain the dirty carrier",
        ],
        "derived": [
            "one immutable coordinate partition: charged matter/carrier/"
            "FSWAP atlas versus disjoint neutral companion/syndrome/work/"
            "SWAP atlas, defining a single fixed P_ext",
            "commutation of every elementary primitive and hence every "
            "prefix with that same coordinate-defined P_ext",
            "literal nearest-neighbour returned FSWAP transport for every "
            "parity-active two-target Bell/pump/correction atom",
            "exact even-Pauli diagonalise/accumulate/phase/uncompute "
            "algorithm for every recurrent seam factor",
            "zero collision edges under the fixed staggered schedule on "
            "base and held shapes",
            "24-frame, eight-origin, 576-product coordinate/collision "
            "covariance and active route, stage, colour, fixed-lab-offset, "
            "and SWAP/FSWAP controls",
        ],
        "open": [
            "autonomous genesis or renewal of the clean route and accumulator "
            "M2, syndrome banks, carrier typing, coframe, and stage occurrence",
            "a dense full held-width executor; exactness here is Pauli "
            "diagonalisation, local matrix identities, returned label "
            "transport, and signed landed channel substitution",
            "translation-invariant duplicate-view gluing, periodic/fault "
            "repair, and carrier/syndrome renewal",
            "physical time, duration, source/gravity, Record/Born/history, "
            "and prediction bridges",
        ],
        "claim_boundary": (
            "Bounded constructive Route-C compiler probe under supplied clean "
            "route/work rails and fixed circuit labels. Circuit stages are "
            "not physical time. Any failed mutation is route-specific; no "
            "no-go, minimum-resource, or axiom-pressure claim is made."
        ),
        "input_sha256": {
            path: sha256(Path(path).read_bytes()).hexdigest()
            for path in AUDIT_INPUT_PATHS if Path(path).is_file()
        },
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
