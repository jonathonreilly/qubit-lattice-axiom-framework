#!/usr/bin/env python3
"""Cycle-822 correction: one fixed Cycle-821 type atlas for Route A.

The first Route-A probe incorrectly audited product-Z on every routed mode.
Cycle 821 instead protects matter plus carrier modes; companion, syndrome,
token, and neutral-work modes are neutral.  This runner first measures the
old word against that fixed typing, then constructs one disjoint type atlas
per held box and recompiles the complete seam dictionary.

Charged routes use explicitly counted carrier-relay M2 and neutral routes use
neutral work M2.  The networks never share a coordinate.  X/Y letters are
paired within type.  A charged-control/neutral-token Fredkin is allowed because
it leaves the charged control occupation invariant.  The added carrier relays
are a supplied resource extension, not part of the landed 65-M2/cell palette.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from hashlib import sha256
import heapq
import json
import math
from pathlib import Path

import numpy as np

import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U720
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S789
import frontier_cycle822_route_a_radius_one_parity_even_compiler_2026_07_30 as LEGACY


AUDIT_TIMEOUT_SEC = 1200
NOTE_PATH = (
    "docs/ROUTE_A_FIXED_TYPE_ATLAS_CORRECTION_"
    "CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    "scripts/frontier_cycle822_route_a_fixed_type_atlas_correction_2026_07_30.py",
    "scripts/frontier_cycle822_route_a_radius_one_parity_even_compiler_2026_07_30.py",
    "scripts/frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


Coord = LEGACY.Coord
LocalGate = LEGACY.LocalGate
ReturnedMacro = LEGACY.ReturnedMacro
CHARGED = "charged"
NEUTRAL = "neutral"
TOL = 1.0e-12
SHAPES = ((2, 1, 1), (3, 1, 1), (3, 2, 2), (5, 3, 2))
STEPS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def astar_path(
    source: Coord,
    target: Coord,
    forbidden: frozenset[Coord],
    bounds: tuple[Coord, Coord],
) -> tuple[Coord, ...]:
    if source == target:
        return (source,)
    low, high = bounds

    def inside(site: Coord) -> bool:
        return all(low[axis] <= site[axis] <= high[axis] for axis in range(3))

    queue: list[tuple[int, int, Coord]] = []
    serial = 0
    heapq.heappush(queue, (LEGACY.manhattan(source, target), serial, source))
    distance = {source: 0}
    previous: dict[Coord, Coord] = {}
    while queue:
        _priority, _serial, site = heapq.heappop(queue)
        if site == target:
            path = [site]
            while path[-1] != source:
                path.append(previous[path[-1]])
            path.reverse()
            return tuple(path)
        next_distance = distance[site] + 1
        for step in STEPS:
            candidate = add(site, step)
            if not inside(candidate):
                continue
            if candidate in forbidden and candidate != target:
                continue
            if next_distance >= distance.get(candidate, 1 << 60):
                continue
            distance[candidate] = next_distance
            previous[candidate] = site
            serial += 1
            priority = next_distance + LEGACY.manhattan(candidate, target)
            heapq.heappush(queue, (priority, serial, candidate))
    raise AssertionError(("typed route unavailable", source, target, bounds))


def network_path(
    network: frozenset[Coord], source: Coord, target: Coord
) -> tuple[Coord, ...]:
    if source == target:
        return (source,)
    queue = deque((source,))
    previous: dict[Coord, Coord | None] = {source: None}
    while queue:
        site = queue.popleft()
        for step in STEPS:
            candidate = add(site, step)
            if candidate not in network or candidate in previous:
                continue
            previous[candidate] = site
            if candidate == target:
                path = [candidate]
                while path[-1] != source:
                    old = previous[path[-1]]
                    if old is None:
                        raise AssertionError("network predecessor drift")
                    path.append(old)
                path.reverse()
                return tuple(path)
            queue.append(candidate)
    raise AssertionError(("disconnected typed network", source, target))


@dataclass(frozen=True)
class FixedTypeAtlas:
    shape: tuple[int, int, int]
    types: dict[Coord, str]
    fixed_charged: frozenset[Coord]
    fixed_neutral: frozenset[Coord]
    charged_network: frozenset[Coord]
    neutral_network: frozenset[Coord]
    charged_center: Coord
    neutral_center: Coord
    token_rails: tuple[Coord, Coord]
    type_conflicts: int
    charged_carrier_relays: int
    neutral_route_work: int

    def type_of(self, site: Coord) -> str:
        return self.types[site]

    def path(self, source: Coord, target: Coord) -> tuple[Coord, ...]:
        source_type = self.type_of(source)
        target_type = self.type_of(target)
        if source_type != target_type:
            raise AssertionError(("mixed route request", source, target))
        network = (
            self.charged_network if source_type == CHARGED
            else self.neutral_network
        )
        return network_path(network, source, target)


def build_fixed_type_atlas(fixture, placed, supports) -> FixedTypeAtlas:
    fixed_charged = frozenset(
        placed["sites_by_qubit"][:fixture.matter_qubits]
    )
    fixed_neutral = frozenset(
        placed["sites_by_qubit"][fixture.matter_qubits:]
    )
    occupied = fixed_charged | fixed_neutral
    low_data = tuple(min(site[axis] for site in occupied) for axis in range(3))
    high_data = tuple(max(site[axis] for site in occupied) for axis in range(3))
    rail_left = (
        high_data[0] + 12, high_data[1] + 12, high_data[2] + 12
    )
    rail_right = (
        high_data[0] + 13, high_data[1] + 13, high_data[2] + 12
    )
    charged_center = (
        high_data[0] + 13, high_data[1] + 12, high_data[2] + 12
    )
    neutral_center = (
        high_data[0] + 12, high_data[1] + 13, high_data[2] + 12
    )
    if not (
        LEGACY.manhattan(charged_center, rail_left) == 1
        and LEGACY.manhattan(charged_center, rail_right) == 1
        and LEGACY.manhattan(neutral_center, rail_left) == 1
        and LEGACY.manhattan(neutral_center, rail_right) == 1
    ):
        raise AssertionError("bad two-center token diamond")
    special = {rail_left, rail_right, charged_center, neutral_center}
    if occupied & special:
        raise AssertionError("token patch collides with landed data")

    requested_charged = sorted({
        site for support in supports for site in support
        if site in fixed_charged
    })
    requested_neutral = sorted({
        site for support in supports for site in support
        if site in fixed_neutral
    })
    points = tuple(occupied | special)
    low = tuple(min(site[axis] for site in points) - 6 for axis in range(3))
    high = tuple(max(site[axis] for site in points) + 6 for axis in range(3))
    bounds = (low, high)

    charged_network = {charged_center}
    charged_forbidden = frozenset(
        fixed_neutral | {rail_left, rail_right, neutral_center}
    )
    for source in requested_charged:
        charged_network.update(astar_path(
            source, charged_center, charged_forbidden, bounds
        ))

    neutral_network = {neutral_center}
    neutral_forbidden = frozenset(
        fixed_charged | charged_network
        | {rail_left, rail_right, charged_center}
    )
    for source in requested_neutral:
        neutral_network.update(astar_path(
            source, neutral_center, neutral_forbidden, bounds
        ))

    demands: dict[Coord, set[str]] = defaultdict(set)
    for site in fixed_charged:
        demands[site].add(CHARGED)
    for site in fixed_neutral:
        demands[site].add(NEUTRAL)
    for site in charged_network:
        demands[site].add(CHARGED)
    for site in neutral_network | {rail_left, rail_right}:
        demands[site].add(NEUTRAL)
    conflicts = sum(len(values) != 1 for values in demands.values())
    types = {site: next(iter(values)) for site, values in demands.items()}
    return FixedTypeAtlas(
        tuple(fixture.shape), types, fixed_charged, fixed_neutral,
        frozenset(charged_network), frozenset(neutral_network),
        charged_center, neutral_center, (rail_left, rail_right), conflicts,
        len(charged_network - fixed_charged),
        len(neutral_network - fixed_neutral) + 2,
    )


def typed_two_site_macro(
    kind: str,
    source: Coord,
    target: Coord,
    matrix: np.ndarray,
    path: tuple[Coord, ...],
) -> ReturnedMacro:
    if path[0] != source or path[-1] != target or len(path) < 2:
        raise AssertionError((kind, source, target, path))
    hop_count = len(path) - 2
    forward = tuple(
        gate for index in range(hop_count)
        for gate in LEGACY.transposition_hop(path[index], path[index + 1])
    )
    active = (path[-2], path[-1])
    reverse = tuple(
        gate for index in reversed(range(hop_count))
        for gate in LEGACY.transposition_hop(path[index], path[index + 1])
    )
    audit = LEGACY.label_audit(path, hop_count, star=False)
    return ReturnedMacro(
        kind, source, target, path, active,
        forward + (LocalGate(kind, active, matrix),) + reverse,
        hop_count, *audit,
    )


def typed_star_macro(
    kind: str,
    control: Coord,
    center: Coord,
    rail_left: Coord,
    rail_right: Coord,
    matrix: np.ndarray,
    path: tuple[Coord, ...],
) -> ReturnedMacro:
    if path[0] != control or path[-1] != center:
        raise AssertionError((kind, control, center, path))
    if rail_left in path or rail_right in path:
        raise AssertionError("token rail entered typed route")
    hop_count = len(path) - 1
    forward = tuple(
        gate for index in range(hop_count)
        for gate in LEGACY.transposition_hop(path[index], path[index + 1])
    )
    active = (center, rail_left, rail_right)
    reverse = tuple(
        gate for index in reversed(range(hop_count))
        for gate in LEGACY.transposition_hop(path[index], path[index + 1])
    )
    audit = LEGACY.label_audit(path, hop_count, star=True)
    return ReturnedMacro(
        kind, control, center, path, active,
        forward + (LocalGate(kind, active, matrix),) + reverse,
        hop_count, *audit,
    )


def typed_row_groups(
    x: int,
    z: int,
    support: tuple[Coord, ...],
    atlas: FixedTypeAtlas,
    pivot_second: bool,
):
    odd = {
        CHARGED: tuple(
            index for index, site in enumerate(support)
            if ((x >> index) & 1) and atlas.type_of(site) == CHARGED
        ),
        NEUTRAL: tuple(
            index for index, site in enumerate(support)
            if ((x >> index) & 1) and atlas.type_of(site) == NEUTRAL
        ),
    }
    if any(len(rows) % 2 for rows in odd.values()):
        raise AssertionError(("odd within-type X/Y seam census", odd))
    pairs = []
    for mode_type in (CHARGED, NEUTRAL):
        rows = odd[mode_type]
        for index in range(0, len(rows), 2):
            first, second = rows[index:index + 2]
            pairs.append((second, first) if pivot_second else (first, second))
    singles = tuple(
        index for index in range(len(support))
        if ((z >> index) & 1) and not ((x >> index) & 1)
    )
    return tuple(pairs), singles


def typed_seam_program(
    support: tuple[Coord, ...],
    phase: int,
    x: int,
    z: int,
    atlas: FixedTypeAtlas,
    *,
    pivot_second: bool,
    reverse_controls: bool,
) -> dict[str, object]:
    pairs, singles = typed_row_groups(
        x, z, support, atlas, pivot_second
    )
    rail_left, rail_right = atlas.token_rails
    pair_data = []
    pre_macros = []
    for pivot, other in pairs:
        pivot_letter = ("X", "Y")[int((z >> pivot) & 1)]
        other_letter = ("X", "Y")[int((z >> other) & 1)]
        unitary = LEGACY.pair_diagonalizer(pivot_letter, other_letter)
        pair_data.append((pivot, other, unitary))
        pre_macros.append(typed_two_site_macro(
            "seam_pair_U_dagger", support[pivot], support[other],
            unitary.conj().T,
            atlas.path(support[pivot], support[other]),
        ))
    controls = tuple(pivot for pivot, _other in pairs) + singles
    if reverse_controls:
        controls = tuple(reversed(controls))
    accumulators = []
    for control in controls:
        control_site = support[control]
        center = (
            atlas.charged_center
            if atlas.type_of(control_site) == CHARGED
            else atlas.neutral_center
        )
        accumulators.append(typed_star_macro(
            "token_Fredkin", control_site, center,
            rail_left, rail_right, LEGACY.FREDKIN,
            atlas.path(control_site, center),
        ))
    y_count = (x & z).bit_count()
    exponent = (phase - y_count) % 4
    if exponent not in (0, 2):
        raise AssertionError(("non-Hermitian seam row", phase, x, z))
    row_sign = 1 if exponent == 0 else -1
    effective_angle = row_sign * math.pi / 2
    rail_phase = np.diag((
        np.exp(0.5j * effective_angle),
        np.exp(-0.5j * effective_angle),
    )).astype(complex)
    post_macros = tuple(
        typed_two_site_macro(
            "seam_pair_U", support[pivot], support[other], unitary,
            atlas.path(support[pivot], support[other]),
        )
        for pivot, other, unitary in reversed(pair_data)
    )
    accumulators = tuple(accumulators)
    macros = tuple(pre_macros) + accumulators + tuple(
        reversed(accumulators)
    ) + post_macros
    gates = (
        tuple(gate for macro in pre_macros for gate in macro.gates)
        + tuple(gate for macro in accumulators for gate in macro.gates)
        + (LocalGate("token_Z_phase", (rail_left,), rail_phase),)
        + tuple(
            gate for macro in reversed(accumulators) for gate in macro.gates
        )
        + tuple(gate for macro in post_macros for gate in macro.gates)
    )
    return {
        "gates": gates,
        "macros": macros,
        "pairs": pairs,
        "singles": singles,
        "controls": controls,
        "effective_angle": effective_angle,
    }


def fixed_parity_residual(gate: LocalGate, types: dict[Coord, str]) -> float:
    charged = tuple(
        index for index, site in enumerate(gate.sites)
        if types.get(site, NEUTRAL) == CHARGED
    )
    parity = np.diag(tuple(
        (-1) ** sum((state >> index) & 1 for index in charged)
        for state in range(1 << len(gate.sites))
    )).astype(complex)
    return float(np.linalg.norm(
        gate.matrix @ parity - parity @ gate.matrix
    ))


def dense_typed_word(gates, site_order, types):
    lookup = {site: index for index, site in enumerate(site_order)}
    count = len(site_order)
    charged_mask = sum(
        1 << index for index, site in enumerate(site_order)
        if types[site] == CHARGED
    )
    parity = np.diag(tuple(
        (-1) ** (state & charged_mask).bit_count()
        for state in range(1 << count)
    )).astype(complex)
    output = np.eye(1 << count, dtype=complex)
    prefix_residual = 0.0
    for gate in gates:
        wires = tuple(lookup[site] for site in gate.sites)
        output = LEGACY.embed(gate.matrix, wires, count) @ output
        prefix_residual = max(prefix_residual, float(np.linalg.norm(
            output @ parity - parity @ output
        )))
    return output, prefix_residual


def controlled_pair_typed_certificate() -> dict[str, object]:
    control = (0, 1, 0)
    first = (2, 0, 0)
    second = (0, 0, 0)
    charged_relay = (1, 0, 0)
    neutral_relays = ((1, 1, 0), (2, 1, 0))
    sites = (control, first, second, charged_relay) + neutral_relays
    types = {
        control: NEUTRAL,
        first: CHARGED,
        second: CHARGED,
        charged_relay: CHARGED,
        **{site: NEUTRAL for site in neutral_relays},
    }

    def pair_path(source, target):
        if source == first and target == second:
            return (first, charged_relay, second)
        if source == second and target == first:
            return (second, charged_relay, first)
        if source == control and target == first:
            return (control, neutral_relays[0], neutral_relays[1], first)
        if source == control and target == second:
            return (control, second)
        raise AssertionError((source, target))

    residuals = []
    prefix_residuals = []
    elementary_residuals = []
    mixed_route_hops = 0
    wrong_residuals = []
    deleted_residuals = []
    deleted_labels = []
    for first_letter in ("X", "Y"):
        for second_letter in ("X", "Y"):
            for pivot_second in (False, True):
                if pivot_second:
                    pivot, other = second, first
                    pivot_letter, other_letter = second_letter, first_letter
                else:
                    pivot, other = first, second
                    pivot_letter, other_letter = first_letter, second_letter
                unitary = LEGACY.pair_diagonalizer(
                    pivot_letter, other_letter
                )
                macros = (
                    typed_two_site_macro(
                        "pair_U_dagger", pivot, other, unitary.conj().T,
                        pair_path(pivot, other),
                    ),
                    typed_two_site_macro(
                        "controlled_Z", control, pivot, LEGACY.CZ,
                        pair_path(control, pivot),
                    ),
                    typed_two_site_macro(
                        "pair_U", pivot, other, unitary,
                        pair_path(pivot, other),
                    ),
                )
                gates = tuple(gate for macro in macros for gate in macro.gates)
                observed, prefix = dense_typed_word(gates, sites, types)
                desired = LEGACY.dense_controlled_pair_target(
                    len(sites), sites.index(control), sites.index(first),
                    sites.index(second), first_letter, second_letter,
                )
                wrong, _ = dense_typed_word(
                    LEGACY.mutate_wrong_swap(gates), sites, types
                )
                deleted_word = []
                removed = False
                for macro in macros:
                    if macro.route_hops and not removed:
                        deleted_word.extend(macro.gates[:-2])
                        removed = True
                    else:
                        deleted_word.extend(macro.gates)
                deleted, _ = dense_typed_word(tuple(deleted_word), sites, types)
                residuals.append(float(np.linalg.norm(observed - desired)))
                prefix_residuals.append(prefix)
                wrong_residuals.append(float(np.linalg.norm(wrong - desired)))
                deleted_residuals.append(float(np.linalg.norm(deleted - desired)))
                elementary_residuals.extend(
                    fixed_parity_residual(gate, types) for gate in gates
                )
                deleted_labels.extend(
                    macro.deleted_return_label_mismatches for macro in macros
                    if macro.route_hops
                )
                mixed_route_hops += sum(
                    gate.kind == "route_FSWAP"
                    and types[gate.sites[0]] != types[gate.sites[1]]
                    for gate in gates
                )
    return {
        "cases": len(residuals),
        "maximum_dense_residual": max(residuals),
        "maximum_fixed_P_ext_prefix_residual": max(prefix_residuals),
        "maximum_elementary_fixed_P_ext_residual": max(elementary_residuals),
        "mixed_type_route_FSWAPs": mixed_route_hops,
        "minimum_wrong_SWAP_residual": min(wrong_residuals),
        "minimum_deleted_return_dense_residual": min(deleted_residuals),
        "minimum_deleted_return_label_mismatches": min(deleted_labels),
    }


def typed_semantic_residual(
    phase: int,
    x: int,
    z: int,
    type_word: str,
    *,
    pivot_second: bool,
    reverse_controls: bool,
    token_bits=(1, 0),
) -> float:
    width = len(type_word)
    typed_odd = {
        CHARGED: tuple(
            index for index in range(width)
            if ((x >> index) & 1) and type_word[index] == "C"
        ),
        NEUTRAL: tuple(
            index for index in range(width)
            if ((x >> index) & 1) and type_word[index] == "N"
        ),
    }
    pairs = []
    for mode_type in (CHARGED, NEUTRAL):
        rows = typed_odd[mode_type]
        if len(rows) % 2:
            raise AssertionError((type_word, rows))
        for index in range(0, len(rows), 2):
            first, second = rows[index:index + 2]
            pairs.append((second, first) if pivot_second else (first, second))
    singles = tuple(
        index for index in range(width)
        if ((z >> index) & 1) and not ((x >> index) & 1)
    )
    pair_data = []
    for pivot, other in pairs:
        pivot_letter = ("X", "Y")[int((z >> pivot) & 1)]
        other_letter = ("X", "Y")[int((z >> other) & 1)]
        pair_data.append((
            pivot, other,
            LEGACY.pair_diagonalizer(pivot_letter, other_letter),
        ))
    controls = tuple(pivot for pivot, _other in pairs) + singles
    if reverse_controls:
        controls = tuple(reversed(controls))
    control_mask = sum(1 << control for control in controls)
    exponent = (phase - (x & z).bit_count()) % 4
    row_sign = 1 if exponent == 0 else -1
    effective_angle = row_sign * math.pi / 2
    token = (token_bits[0] << width) | (token_bits[1] << (width + 1))
    cosine = math.cos(math.pi / 4)
    sine = math.sin(math.pi / 4)
    maximum = 0.0
    for source in range(1 << width):
        state = {source | token: 1.0 + 0.0j}
        for pivot, other, unitary in pair_data:
            state = LEGACY.apply_two_sparse(
                state, unitary.conj().T, (pivot, other)
            )
        state = {
            basis: coefficient * np.exp(
                0.5j * effective_angle * (
                    1 if (
                        ((basis >> width) & 1)
                        ^ ((basis & control_mask).bit_count() & 1)
                    ) == 0 else -1
                )
            )
            for basis, coefficient in state.items()
        }
        for pivot, other, unitary in reversed(pair_data):
            state = LEGACY.apply_two_sparse(state, unitary, (pivot, other))
        expected: dict[int, complex] = {source | token: cosine}
        target = (source ^ x) | token
        pauli_amplitude = (1j ** phase) * (
            -1 if (source & z).bit_count() & 1 else 1
        )
        expected[target] = expected.get(target, 0.0j) - (
            1j * sine * pauli_amplitude
        )
        residual = math.sqrt(sum(
            abs(state.get(key, 0.0j) - expected.get(key, 0.0j)) ** 2
            for key in set(state) | set(expected)
        ))
        maximum = max(maximum, float(residual))
    return maximum


def legacy_typing_audit() -> dict[str, object]:
    boxes = []
    totals = Counter()
    kind_failures = Counter()
    for shape in SHAPES:
        fixture = S789.fixture_for(shape)
        placed = U720.placement(fixture)
        all_sites = tuple(placed["all_sites"])
        charged = set(
            placed["sites_by_qubit"][:fixture.matter_qubits]
        )
        neutral_data = set(
            placed["sites_by_qubit"][fixture.matter_qubits:]
        )
        demands: dict[Coord, set[str]] = defaultdict(set)
        conflict_events = 0

        def demand(site: Coord, mode_type: str) -> None:
            nonlocal conflict_events
            conflict_events += bool(
                demands[site] and mode_type not in demands[site]
            )
            demands[site].add(mode_type)

        for site in charged:
            demand(site, CHARGED)
        for site in neutral_data:
            demand(site, NEUTRAL)
        counts = Counter()
        for edge in range(len(fixture.edges)):
            for row in fixture.physical_terms(edge):
                support, phase, x, z = LEGACY.local_row(
                    U720.lift_pauli(row, placed), all_sites
                )
                program = LEGACY.seam_program(
                    support, phase, x, z,
                    pivot_second=False, reverse_controls=False,
                )
                center = program["center"]
                rail_left, rail_right = program["token"]
                for site in (center, rail_left, rail_right):
                    demand(site, NEUTRAL)
                prefix_good = True
                old_types = {
                    site: CHARGED if site in charged else NEUTRAL
                    for gate in program["gates"] for site in gate.sites
                }
                for gate in program["gates"]:
                    failure = fixed_parity_residual(gate, old_types) >= TOL
                    counts["elementary_fixed_P_ext_failures"] += failure
                    counts["elementary_primitives"] += 1
                    if failure:
                        kind_failures[gate.kind] += 1
                    prefix_good = prefix_good and not failure
                    counts[
                        "prefix_factorwise_certificate_failures"
                    ] += not prefix_good
                for macro in program["macros"]:
                    required = CHARGED if macro.source in charged else NEUTRAL
                    stop = (
                        len(macro.path)
                        if macro.kind == "token_Fredkin"
                        else len(macro.path) - 1
                    )
                    for site in macro.path[:stop]:
                        demand(site, required)
                counts["seam_factors"] += 1
        counts["charged_neutral_type_conflict_coordinates"] = sum(
            len(values) > 1 for values in demands.values()
        )
        counts["charged_neutral_type_conflict_demand_events"] = (
            conflict_events
        )
        totals.update(counts)
        boxes.append({"shape": shape, **dict(counts)})
    return {
        "valid_Cycle821_fixed_P_ext_certificate": False,
        "boxes": boxes,
        "totals": dict(totals),
        "elementary_failure_kind_census": dict(sorted(kind_failures.items())),
        "diagnosis": (
            "the old runner charged every local support; with matter-only "
            "seam charge it mixes charged and neutral FSWAP routes, pairs one "
            "charged and one neutral X/Y site, and reuses coordinates across "
            "incompatible route types"
        ),
    }


def corrected_seam_certificate() -> dict[str, object]:
    boxes = []
    templates: dict[tuple, tuple[int, int, int, str]] = {}
    maximum_residuals = []
    dirty_residuals = []
    totals = Counter()
    maximum_elementary = 0.0
    maximum_word = 0
    maximum_hops = 0
    minimum_deleted = []
    family_digest = sha256()
    for shape in SHAPES:
        fixture = S789.fixture_for(shape)
        placed = U720.placement(fixture)
        all_sites = tuple(placed["all_sites"])
        specs = []
        for edge in range(len(fixture.edges)):
            for row in fixture.physical_terms(edge):
                specs.append(LEGACY.local_row(
                    U720.lift_pauli(row, placed), all_sites
                ))
        atlas = build_fixed_type_atlas(
            fixture, placed, tuple(spec[0] for spec in specs)
        )
        counts = Counter()
        box_digest = sha256()
        for support, phase, x, z in specs:
            type_word = "".join(
                "C" if atlas.type_of(site) == CHARGED else "N"
                for site in support
            )
            letters = LEGACY.pauli_letters(x, z, len(support))
            key = (len(support), phase, x.bit_count(), letters, type_word)
            templates.setdefault(key, (phase, x, z, type_word))
            program = typed_seam_program(
                support, phase, x, z, atlas,
                pivot_second=False, reverse_controls=False,
            )
            gates = program["gates"]
            macros = program["macros"]
            maximum_word = max(maximum_word, len(gates))
            maximum_hops = max(
                maximum_hops,
                max((macro.route_hops for macro in macros), default=0),
            )
            prefix_good = True
            for gate in gates:
                residual = fixed_parity_residual(gate, atlas.types)
                maximum_elementary = max(maximum_elementary, residual)
                counts["elementary_fixed_P_ext_failures"] += residual >= TOL
                prefix_good = prefix_good and residual < TOL
                counts["prefix_fixed_P_ext_failures_by_induction"] += (
                    not prefix_good
                )
                counts["radius_one_failures"] += not LEGACY.radius_one(gate)
                counts["mixed_type_route_FSWAPs"] += (
                    gate.kind == "route_FSWAP"
                    and atlas.type_of(gate.sites[0])
                    != atlas.type_of(gate.sites[1])
                )
            counts["route_operand_failures"] += sum(
                macro.operand_failures for macro in macros
            )
            counts["route_return_failures"] += sum(
                macro.return_failures for macro in macros
            )
            minimum_deleted.extend(
                macro.deleted_return_label_mismatches for macro in macros
                if macro.route_hops
            )
            counts["seam_factors"] += 1
            digest = LEGACY.gate_digest(gates)
            box_digest.update(digest.encode())
        counts["global_type_atlas_conflicts"] = atlas.type_conflicts
        totals.update(counts)
        family_digest.update(box_digest.digest())
        boxes.append({
            "shape": shape,
            "cells": len(fixture.cells),
            "edges": len(fixture.edges),
            "charged_carrier_relay_M2": atlas.charged_carrier_relays,
            "neutral_route_work_M2_including_token": atlas.neutral_route_work,
            "typed_atlas_coordinates": len(atlas.types),
            **dict(counts),
            "program_sha256": box_digest.hexdigest(),
        })

    template_rows = []
    for key, (phase, x, z, type_word) in sorted(templates.items()):
        residuals = []
        for pivot_second in (False, True):
            for reverse_controls in (False, True):
                residuals.append(typed_semantic_residual(
                    phase, x, z, type_word,
                    pivot_second=pivot_second,
                    reverse_controls=reverse_controls,
                ))
        dirty = typed_semantic_residual(
            phase, x, z, type_word,
            pivot_second=False, reverse_controls=False,
            token_bits=(0, 1),
        )
        maximum_residuals.extend(residuals)
        dirty_residuals.append(dirty)
        template_rows.append({
            "support": key[0],
            "phase": phase,
            "letters": key[3],
            "type_word": type_word,
            "pivot_order_variants": 4,
            "maximum_exhaustive_operator_residual": max(residuals),
            "dirty_opposite_rail_residual": dirty,
        })
    return {
        "boxes": boxes,
        "totals": dict(totals),
        "literal_seam_factors": totals["seam_factors"],
        "unique_typed_templates": len(templates),
        "template_certificates": template_rows,
        "maximum_exhaustive_operator_residual": max(maximum_residuals),
        "minimum_dirty_opposite_rail_residual": min(dirty_residuals),
        "maximum_elementary_fixed_P_ext_residual": maximum_elementary,
        "minimum_deleted_return_label_mismatches": min(minimum_deleted),
        "maximum_primitives_per_factor": maximum_word,
        "maximum_route_hops": maximum_hops,
        "program_family_sha256": family_digest.hexdigest(),
        "resource_boundary": (
            "charged network coordinates are added carrier-relay M2 and are "
            "included in P_ext; neutral network coordinates and both token "
            "rails are work modes outside P_ext"
        ),
    }


def mixed_accumulator_dense_certificate() -> dict[str, object]:
    # Two charged and two neutral controls, followed by two neutral token rails.
    controls = 4
    rail_left, rail_right = 4, 5
    count = 6
    phase = np.diag((
        np.exp(0.25j * math.pi), np.exp(-0.25j * math.pi)
    )).astype(complex)
    words = []
    for order in (tuple(range(controls)), tuple(reversed(range(controls)))):
        words.append(tuple(
            (LEGACY.FREDKIN, (control, rail_left, rail_right))
            for control in order
        ) + ((phase, (rail_left,)),) + tuple(
            (LEGACY.FREDKIN, (control, rail_left, rail_right))
            for control in reversed(order)
        ))
    p_ext = np.diag(tuple(
        (-1) ** (state & 0b11).bit_count() for state in range(1 << count)
    )).astype(complex)
    prefix_residuals = []
    clean_residuals = []
    for word in words:
        total = np.eye(1 << count, dtype=complex)
        prefix = 0.0
        for matrix, wires in word:
            total = LEGACY.embed(matrix, wires, count) @ total
            prefix = max(prefix, float(np.linalg.norm(
                total @ p_ext - p_ext @ total
            )))
        prefix_residuals.append(prefix)
        embedding = np.zeros((1 << count, 1 << controls), dtype=complex)
        for state in range(1 << controls):
            embedding[state | (1 << rail_left), state] = 1
        target = np.diag(tuple(
            np.exp(-0.25j * math.pi * ((-1) ** state.bit_count()))
            for state in range(1 << controls)
        )).astype(complex)
        clean_residuals.append(float(np.linalg.norm(
            total @ embedding - embedding @ target
        )))
    charged_control = LocalGate(
        "charged_control_neutral_token_Fredkin",
        ((0, 0, 0), (1, 0, 0), (0, 1, 0)),
        LEGACY.FREDKIN,
    )
    fredkin_types = {
        charged_control.sites[0]: CHARGED,
        charged_control.sites[1]: NEUTRAL,
        charged_control.sites[2]: NEUTRAL,
    }
    return {
        "charged_controls": 2,
        "neutral_controls": 2,
        "control_orders": 2,
        "maximum_dense_clean_isometry_residual": max(clean_residuals),
        "maximum_dense_fixed_P_ext_prefix_residual": max(prefix_residuals),
        "charged_control_neutral_token_Fredkin_P_ext_residual": (
            fixed_parity_residual(charged_control, fredkin_types)
        ),
    }


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    legacy = legacy_typing_audit()
    pair = controlled_pair_typed_certificate()
    accumulator = mixed_accumulator_dense_certificate()
    seams = corrected_seam_certificate()
    legacy_totals = legacy["totals"]
    corrected_totals = seams["totals"]
    checks = {
        "legacy_all_charged_certificate_is_rejected_exactly": (
            not legacy["valid_Cycle821_fixed_P_ext_certificate"]
            and legacy_totals["seam_factors"] == 328
            and legacy_totals["elementary_fixed_P_ext_failures"] == 10112
            and legacy_totals[
                "prefix_factorwise_certificate_failures"
            ] == 337496
            and legacy_totals[
                "charged_neutral_type_conflict_coordinates"
            ] == 1445
        ),
        "typed_controlled_pair_commutes_with_one_fixed_P_ext": (
            pair["maximum_dense_residual"] < TOL
            and pair["maximum_fixed_P_ext_prefix_residual"] < TOL
            and pair["maximum_elementary_fixed_P_ext_residual"] < TOL
            and pair["mixed_type_route_FSWAPs"] == 0
        ),
        "mixed_control_dual_rail_accumulator_commutes_with_fixed_P_ext": (
            accumulator["maximum_dense_clean_isometry_residual"] < TOL
            and accumulator[
                "maximum_dense_fixed_P_ext_prefix_residual"
            ] < TOL
            and accumulator[
                "charged_control_neutral_token_Fredkin_P_ext_residual"
            ] < TOL
        ),
        "complete_mixed_seam_dictionary_has_one_conflict_free_atlas": (
            seams["literal_seam_factors"] == 328
            and corrected_totals["global_type_atlas_conflicts"] == 0
            and corrected_totals["mixed_type_route_FSWAPs"] == 0
            and corrected_totals["elementary_fixed_P_ext_failures"] == 0
            and corrected_totals[
                "prefix_fixed_P_ext_failures_by_induction"
            ] == 0
            and corrected_totals["route_operand_failures"] == 0
            and corrected_totals["route_return_failures"] == 0
            and corrected_totals["radius_one_failures"] == 0
            and seams["maximum_exhaustive_operator_residual"] < TOL
        ),
        "typed_mutations_remain_active": (
            pair["minimum_wrong_SWAP_residual"] > 1.0e-3
            and pair["minimum_deleted_return_dense_residual"] > 1.0e-3
            and pair["minimum_deleted_return_label_mismatches"] > 0
            and seams["minimum_deleted_return_label_mismatches"] > 0
            and seams["minimum_dirty_opposite_rail_residual"] > 1.0e-3
        ),
    }
    output = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "legacy_framework_typing_audit": legacy,
        "typed_controlled_pair": pair,
        "mixed_typed_accumulator": accumulator,
        "corrected_typed_seam_compiler": seams,
        "claim_boundary": (
            "the old all-modes-charged Route-A claim is demoted; the corrected "
            "328-factor statement is conditional on the explicitly counted "
            "charged carrier-relay and neutral-work atlas in each held box, "
            "not on the landed Cycle821 65-M2/cell palette alone"
        ),
        "input_sha256": {
            path: file_sha256(Path(path))
            for path in AUDIT_INPUT_PATHS if Path(path).is_file()
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if output["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
