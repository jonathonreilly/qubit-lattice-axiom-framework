#!/usr/bin/env python3
"""Cycle-822 Route-B radius-one synthesis of the Cycle-821 even atoms.

This runner supplies a small physical-M2 dictionary and uses it in two places:

* the Cycle-821 controlled X/Y-pair atom is reconstructed from two parity-even
  quarter rotations and one CZ; and
* every actual Cycle-720 seam Pauli occurring on the held Cycle-789 fixtures is
  Clifford-reduced to one signed Z, rotated, and uncomputed.

The seam reduction needs no clean ancilla.  It separately reduces charged
matter Z sites with an arbitrary-state charged matter spectator and neutral
companion Z sites with an arbitrary-state neutral companion spectator.  When
both residues survive, one exact diagonal ZZ rotation supplies their joint
phase.  The complete conjugate/rotate/unconjugate word is the desired seam
rotation tensor identity on both spectators.  Every non-onsite primitive is
routed through disjoint statically typed charged/neutral returned-work lanes,
so every prefix preserves the Cycle-821 extended matter parity and every
emitted primitive has physical Manhattan support diameter one.

The claim is finite and conditional.  Arbitrary adjacent parity-block
``R_Q`` quarter rotations, including the joint ``R_ZZ``, are declared
primitives.  Some of those rotations
mix the zero- and two-particle states and therefore conserve parity, not exact
particle number.  The runner does not derive that primitive dictionary, a
parallel recolouring of recurrent G, genesis, or autonomous occurrence.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
import heapq
import json
import math
from pathlib import Path

import numpy as np

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U720
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S789
import frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30 as C821


TOL = 1.0e-10
SHAPES = ((2, 1, 1), (3, 1, 1), (3, 2, 2), (5, 3, 2))
ASTAR_BOUND_MARGIN = 8
ASTAR_EXPANSION_LIMIT_PER_MACRO = 250_000
Pauli = U720.c707.Pauli
Coord = tuple[int, int, int]


I2 = np.eye(2, dtype=complex)
X = np.asarray(((0, 1), (1, 0)), dtype=complex)
Y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
Z = np.diag((1, -1)).astype(complex)
SWAP = np.asarray(
    ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
    dtype=complex,
)
CZ = np.diag((1, 1, 1, -1)).astype(complex)


@dataclass(frozen=True)
class ReductionStep:
    tag: str
    source: Pauli
    target: Pauli
    generator: Pauli


@dataclass(frozen=True)
class SeamCompilation:
    source: Pauli
    reduced: Pauli
    spectators: tuple[int, ...]
    steps: tuple[ReductionStep, ...]


def fields(row: Pauli) -> tuple[int, int, int]:
    return row.phase % 4, row.x, row.z


def support(row: Pauli) -> tuple[int, ...]:
    mask = row.x | row.z
    return tuple(index for index in range(mask.bit_length()) if (mask >> index) & 1)


def y_count(row: Pauli) -> int:
    return (row.x & row.z).bit_count()


def hermitian_exponent(row: Pauli) -> int:
    """Exponent of i after replacing each local XZ by the Hermitian Y."""
    return (row.phase - y_count(row)) % 4


def letter_row(row: Pauli, qubit: int) -> Pauli:
    x = (row.x >> qubit) & 1
    z = (row.z >> qubit) & 1
    if x and z:
        return Pauli(phase=1, x=1 << qubit, z=1 << qubit)
    if x:
        return Pauli(x=1 << qubit)
    if z:
        return Pauli(z=1 << qubit)
    return Pauli()


def product(rows) -> Pauli:
    return U720.c707.pauli_product(rows)


def rotation_generator(source: Pauli, target: Pauli) -> Pauli:
    """Return Q=-i source*target, so R_Q source R_Q^dagger=target."""
    if source.commutes(target):
        raise AssertionError(("quarter-turn endpoints commute", source, target))
    row = source @ target
    row = Pauli((row.phase + 3) % 4, row.x, row.z)
    if hermitian_exponent(row) not in (0, 2):
        raise AssertionError(("non-Hermitian generator", row))
    if row.x.bit_count() % 2:
        raise AssertionError(("parity-odd generator", row))
    if len(support(row)) != 2:
        raise AssertionError(("non-two-site generator", row))
    return row


def conjugate_quarter(row: Pauli, generator: Pauli, *, inverse: bool = False) -> Pauli:
    """Conjugate by (I-iQ)/sqrt(2), or its inverse, in exact Pauli algebra."""
    if row.commutes(generator):
        return row
    output = row @ generator
    return Pauli(
        (output.phase + (3 if inverse else 1)) % 4,
        output.x,
        output.z,
    )


def append_reduction_step(
    current: Pauli,
    steps: list[ReductionStep],
    tag: str,
    local_source: Pauli,
    local_target: Pauli,
) -> Pauli:
    generator = rotation_generator(local_source, local_target)
    steps.append(ReductionStep(tag, local_source, local_target, generator))
    return conjugate_quarter(current, generator)


def reduce_typed_xy(
    source: Pauli, charged: frozenset[int], width: int
) -> tuple[Pauli, tuple[ReductionStep, ...]]:
    """Remove X/Y sites in charged-charged or neutral-neutral pairs only."""
    current = source
    steps: list[ReductionStep] = []
    for is_charged in (True, False):
        while True:
            sites = tuple(
                index for index in range(width)
                if ((current.x >> index) & 1)
                and ((index in charged) == is_charged)
            )
            if not sites:
                break
            if len(sites) < 2:
                raise AssertionError(("odd typed X/Y residue", is_charged, current))
            first, second = sites[:2]
            current = append_reduction_step(
                current,
                steps,
                "charged-pair-to-Z" if is_charged else "neutral-pair-to-Z",
                product((letter_row(current, first), letter_row(current, second))),
                Pauli(z=1 << first),
            )
    return current, tuple(steps)


def reduce_typed_z_group(
    source: Pauli,
    charged: frozenset[int],
    is_charged: bool,
    spectator: int,
    width: int,
) -> tuple[Pauli, tuple[ReductionStep, ...]]:
    """Reduce one Z type to one Z using a spectator of that same type."""
    if (spectator in charged) != is_charged:
        raise AssertionError(("wrong spectator type", spectator, is_charged))
    current = source
    steps: list[ReductionStep] = []
    while True:
        sites = tuple(
            index for index in range(width)
            if ((current.z >> index) & 1)
            and ((index in charged) == is_charged)
        )
        if len(sites) <= 1:
            break
        first, second = sites[:2]
        if ((current.x | current.z) >> spectator) & 1:
            raise AssertionError(("typed spectator did not clear", current, spectator))
        prefix = "charged" if is_charged else "neutral"
        current = append_reduction_step(
            current,
            steps,
            f"{prefix}-Z-to-pair",
            Pauli(z=1 << first),
            product((Pauli(x=1 << first), Pauli(x=1 << spectator))),
        )
        current = append_reduction_step(
            current,
            steps,
            f"{prefix}-odd-transfer",
            product((Pauli(z=1 << second), Pauli(x=1 << spectator))),
            Pauli(x=1 << second),
        )
        current = append_reduction_step(
            current,
            steps,
            f"{prefix}-pair-to-Z",
            product((Pauli(x=1 << first), Pauli(x=1 << second))),
            Pauli(z=1 << first),
        )
    return current, tuple(steps)


def legacy_retyped_reduction(
    source: Pauli, neutral_spectator: int, width: int
) -> tuple[ReductionStep, ...]:
    """Reproduce the superseded all-M2 parity reduction for the hostile census."""
    current = source
    steps: list[ReductionStep] = []
    while current.x:
        sites = tuple(index for index in range(width) if (current.x >> index) & 1)
        first, second = sites[:2]
        current = append_reduction_step(
            current,
            steps,
            "legacy-pair-to-Z",
            product((letter_row(current, first), letter_row(current, second))),
            Pauli(z=1 << first),
        )
    while current.z.bit_count() > 1:
        first, second = tuple(
            index for index in range(width) if (current.z >> index) & 1
        )[:2]
        current = append_reduction_step(
            current,
            steps,
            "legacy-Z-to-pair",
            Pauli(z=1 << first),
            product((Pauli(x=1 << first), Pauli(x=1 << neutral_spectator))),
        )
        current = append_reduction_step(
            current,
            steps,
            "legacy-odd-transfer",
            product((Pauli(z=1 << second), Pauli(x=1 << neutral_spectator))),
            Pauli(x=1 << second),
        )
        current = append_reduction_step(
            current,
            steps,
            "legacy-pair-to-Z",
            product((Pauli(x=1 << first), Pauli(x=1 << second))),
            Pauli(z=1 << first),
        )
    return tuple(steps)


def restrict_row(row: Pauli, indices: tuple[int, ...]) -> Pauli:
    positions = {global_index: local for local, global_index in enumerate(indices)}
    x = z = 0
    for global_index, local in positions.items():
        x |= ((row.x >> global_index) & 1) << local
        z |= ((row.z >> global_index) & 1) << local
    return Pauli(row.phase, x, z)


def embed_gate(matrix: np.ndarray, wires: tuple[int, ...], width: int) -> np.ndarray:
    output = np.zeros((1 << width, 1 << width), dtype=complex)
    for column in range(1 << width):
        state = np.zeros(1 << width, dtype=complex)
        state[column] = 1
        output[:, column] = U720.c707.apply_gate(state, matrix, wires, width)
    return output


def two_site_dense(row: Pauli, first: int, second: int) -> np.ndarray:
    local = restrict_row(row, (first, second))
    return B.dense_pauli(B.Pauli(local.phase, local.x, local.z), 2)


def quarter_matrix(row: Pauli, first: int, second: int, inverse=False) -> np.ndarray:
    dense = two_site_dense(row, first, second)
    sign = 1j if inverse else -1j
    return (np.eye(4, dtype=complex) + sign * dense) / math.sqrt(2)


def primitive_dictionary_certificate() -> dict[str, object]:
    pair_parity = np.diag((1, -1, -1, 1)).astype(complex)
    pair_number = np.diag((0, 1, 1, 2)).astype(complex)
    matrices = {"SWAP": SWAP, "CZ": CZ}
    for first_letter in ("X", "Y"):
        for second_letter in ("X", "Y"):
            source = product((
                B.pauli_letter(0, first_letter),
                B.pauli_letter(1, second_letter),
            ))
            dense = B.dense_pauli(source, 2)
            matrices[f"R_{first_letter}{second_letter}"] = (
                np.eye(4, dtype=complex) - 1j * dense
            ) / math.sqrt(2)
    matrices["R_ZZ"] = (
        np.eye(4, dtype=complex) - 1j * np.kron(Z, Z)
    ) / math.sqrt(2)

    unitarity = tuple(
        float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(4)))
        for matrix in matrices.values()
    )
    parity = tuple(
        float(np.linalg.norm(matrix @ pair_parity - pair_parity @ matrix))
        for matrix in matrices.values()
    )
    number = {
        name: float(np.linalg.norm(matrix @ pair_number - pair_number @ matrix))
        for name, matrix in matrices.items()
    }

    # Explicit radius-one controlled-swap semantic primitive.  It is checked
    # here but deliberately not emitted by the diameter-one compiler below.
    swap_targets = embed_gate(SWAP, (1, 2), 3)
    z_control = embed_gate(Z, (0,), 3)
    projector_zero = (np.eye(8) + z_control) / 2
    projector_one = (np.eye(8) - z_control) / 2
    fredkin = projector_zero + projector_one @ swap_targets
    ideal = np.eye(8, dtype=complex)
    ideal[:, (3, 5)] = ideal[:, (5, 3)]
    total_number = np.diag(tuple(state.bit_count() for state in range(8))).astype(complex)
    total_parity = np.diag(tuple((-1) ** state.bit_count() for state in range(8))).astype(complex)
    even = (0, 3, 5, 6)
    odd = (1, 2, 4, 7)

    return {
        "declared_primitives": (
            "onsite_RZ(theta)",
            "adjacent_number_conserving_SWAP",
            "adjacent_CZ",
            "adjacent_parity_block_R_Q(pi/2), Q in {XX,XY,YX,YY,ZZ}",
        ),
        "maximum_two_site_unitarity_residual": max(unitarity),
        "maximum_two_site_parity_commutator_residual": max(parity),
        "number_commutator_residuals": number,
        "pair_rotation_classes_not_exact_number_conserving": sum(
            value > TOL for name, value in number.items() if name.startswith("R_")
        ),
        "fredkin_projector_decomposition_residual": float(np.linalg.norm(fredkin - ideal)),
        "fredkin_unitarity_residual": float(np.linalg.norm(fredkin.conj().T @ fredkin - np.eye(8))),
        "fredkin_total_number_commutator_residual": float(np.linalg.norm(
            fredkin @ total_number - total_number @ fredkin
        )),
        "fredkin_total_parity_commutator_residual": float(np.linalg.norm(
            fredkin @ total_parity - total_parity @ fredkin
        )),
        "fredkin_radius_about_control": 1,
        "fredkin_support_diameter_on_cubic_path": 2,
        "fredkin_even_odd_block_determinant_ratio": complex(
            np.linalg.det(fredkin[np.ix_(even, even)])
            / np.linalg.det(fredkin[np.ix_(odd, odd)])
        ).real,
        "fredkin_lane_disposition": (
            "checked semantic controlled-swap only; not emitted because a "
            "three-site cubic path has diameter two, while the admitted word "
            "below uses only diameter-zero/one primitives"
        ),
    }


def pair_compiler_certificate() -> dict[str, object]:
    control, first, second, width = 0, 1, 2, 3
    identity = np.eye(1 << width, dtype=complex)
    matter_parity = B.dense_pauli(
        B.Pauli(z=(1 << first) | (1 << second)), width
    )
    residuals = []
    map_residuals = []
    prefix_residuals = []
    deleted_residuals = []
    sign_mutation_residuals = []
    generator_mismatches = 0
    for first_letter in ("X", "Y"):
        for second_letter in ("X", "Y"):
            target = product((
                B.pauli_letter(first, first_letter),
                B.pauli_letter(second, second_letter),
            ))
            generator = rotation_generator(
                B.pauli_letter(first, "Z"), target
            )
            landed = C821.pair_rotation_generator(
                first, first_letter, second, second_letter
            )
            generator_mismatches += fields(generator) != fields(landed)
            dense_k = B.dense_pauli(generator, width)
            u = (identity - 1j * dense_k) / math.sqrt(2)
            cz = B.dense_controlled_target(B.Pauli(z=1 << first), control, width)
            compiled = u @ cz @ u.conj().T
            desired = B.dense_controlled_target(target, control, width)
            residuals.append(float(np.linalg.norm(compiled - desired)))
            map_residuals.append(float(np.linalg.norm(
                u @ B.dense_pauli(B.Pauli(z=1 << first), width) @ u.conj().T
                - B.dense_pauli(target, width)
            )))
            prefix = np.eye(1 << width, dtype=complex)
            for primitive in (u.conj().T, cz, u):
                prefix = primitive @ prefix
                prefix_residuals.append(float(np.linalg.norm(
                    prefix @ matter_parity - matter_parity @ prefix
                )))
            deleted_residuals.append(float(np.linalg.norm(
                u @ cz - desired
            )))
            sign_mutation_residuals.append(float(np.linalg.norm(
                u.conj().T @ cz @ u - desired
            )))

    return {
        "letter_pairs_exhausted": 4,
        "generator_phase_sign_mismatches_vs_Cycle821": generator_mismatches,
        "maximum_rotation_conjugacy_residual": max(map_residuals),
        "maximum_controlled_pair_residual": max(residuals),
        "maximum_prefix_Cycle821_matter_parity_commutator_residual": max(
            prefix_residuals
        ),
        "minimum_deleted_quarter_rotation_residual": min(deleted_residuals),
        "minimum_quarter_rotation_sign_mutation_residual": min(sign_mutation_residuals),
        "emitted_semantic_word": "R_Q(-pi/2); CZ(control,first); R_Q(+pi/2)",
        "maximum_unrouted_primitive_support_M2": 2,
    }


def palette_for(shape: tuple[int, int, int]) -> dict[str, object]:
    fixture = S789.fixture_for(shape)
    centers, placed = S789.centers_and_placement(fixture)
    i_sites = S789.bank_sites(fixture, centers, 1, S789.I_PAIRS)
    l_sites = S789.bank_sites(fixture, centers, 2, S789.L_PAIRS)
    carriers = set(C821.carrier_sites(fixture, centers))
    classes = {
        "I": set(i_sites),
        "L": set(l_sites),
        "coframe": set(S789.coframe_sites(fixture, centers)),
        "pump_ancilla": {
            S789.ancilla_site(centers[cell], slot, "pump")
            for cell in fixture.cells for slot in range(S789.FAMILY_SLOTS)
        },
        "bell_ancilla": {
            S789.ancilla_site(centers[cell], slot, "bell")
            for cell in fixture.cells for slot in range(S789.FAMILY_SLOTS)
        },
        "Cycle821_carrier": carriers,
    }
    charged_persistent = (
        set(placed["sites_by_qubit"][:fixture.matter_qubits])
        | set(i_sites[:fixture.matter_qubits])
        | set(l_sites[:fixture.matter_qubits])
        | carriers
    )
    neutral_persistent = (
        set(placed["sites_by_qubit"][fixture.matter_qubits:])
        | set(i_sites[fixture.matter_qubits:])
        | set(l_sites[fixture.matter_qubits:])
        | classes["coframe"]
        | classes["pump_ancilla"]
        | classes["bell_ancilla"]
    )
    if charged_persistent & neutral_persistent:
        raise AssertionError("persistent parity types collide")
    return {
        "fixture": fixture,
        "placed": placed,
        "centers": centers,
        "classes": classes,
        "forbidden": set().union(*classes.values()),
        "charged_persistent": charged_persistent,
        "neutral_persistent": neutral_persistent,
    }


ROUTE_DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)


def add_coord(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


class TypedRouter:
    """Finite charged/neutral route-work assignment with fixed P_ext typing."""

    def __init__(self, palette: dict[str, object]):
        self.network = {
            True: set(palette["charged_persistent"]),
            False: set(palette["neutral_persistent"]),
        }
        self.forbidden = set(palette["forbidden"])
        self.maximum_distance = 0
        self.route_return_failures = 0
        self.deleted_return_swap_mismatches = 0
        self.typed_prefix_failures = 0
        self.touched: set[Coord] = set()
        self.macros: list[dict[str, object]] = []
        self.astar_calls = 0
        self.astar_total_expansions = 0
        self.astar_maximum_expansions = 0
        points = self.network[True] | self.network[False] | self.forbidden
        self.bounds = tuple(
            (
                min(point[axis] for point in points) - ASTAR_BOUND_MARGIN,
                max(point[axis] for point in points) + ASTAR_BOUND_MARGIN,
            )
            for axis in range(3)
        )

    def astar(self, start: Coord, goals, blocked: set[Coord]) -> tuple[Coord, ...]:
        goal_set = set(goals)

        def heuristic(point: Coord) -> int:
            return min(S789.manhattan(point, goal) for goal in goal_set)

        queue = [(heuristic(start), 0, start)]
        distance = {start: 0}
        previous: dict[Coord, Coord | None] = {start: None}
        expansions = 0
        self.astar_calls += 1
        while queue:
            _priority, depth, point = heapq.heappop(queue)
            if depth != distance[point]:
                continue
            expansions += 1
            if expansions > ASTAR_EXPANSION_LIMIT_PER_MACRO:
                raise AssertionError(("A* expansion bound", start, tuple(goal_set)))
            if point in goal_set:
                path = []
                cursor: Coord | None = point
                while cursor is not None:
                    path.append(cursor)
                    cursor = previous[cursor]
                self.astar_total_expansions += expansions
                self.astar_maximum_expansions = max(
                    self.astar_maximum_expansions, expansions
                )
                return tuple(reversed(path))
            for direction in ROUTE_DIRECTIONS:
                neighbor = add_coord(point, direction)
                if any(
                    neighbor[axis] < self.bounds[axis][0]
                    or neighbor[axis] > self.bounds[axis][1]
                    for axis in range(3)
                ):
                    continue
                if neighbor in blocked and neighbor not in goal_set:
                    continue
                candidate = depth + 1
                if candidate < distance.get(neighbor, 1 << 60):
                    distance[neighbor] = candidate
                    previous[neighbor] = point
                    heapq.heappush(
                        queue,
                        (candidate + heuristic(neighbor), candidate, neighbor),
                    )
        raise AssertionError(("typed route not found", start, tuple(goal_set)))

    def macro(self, left: Coord, right: Coord, is_charged: bool, *, cross_zz=False):
        blocked = (self.network[not is_charged] | self.forbidden) - {left, right}
        if cross_zz:
            goals = tuple(
                add_coord(right, direction) for direction in ROUTE_DIRECTIONS
                if add_coord(right, direction) not in blocked
                and add_coord(right, direction) not in self.forbidden
            )
            path = self.astar(left, goals, blocked)
            full_path = path + (right,)
        else:
            path = self.astar(left, (right,), blocked)
            full_path = path
        if any(
            S789.manhattan(first, second) != 1
            for first, second in zip(full_path, full_path[1:])
        ):
            raise AssertionError(("non-NN typed path", full_path))

        # Only path, not the opposite-typed final ZZ target, joins this lane.
        self.network[is_charged].update(path)
        self.typed_prefix_failures += len(
            self.network[True] & self.network[False]
        )
        self.touched.update(full_path)
        self.maximum_distance = max(self.maximum_distance, len(full_path) - 1)

        swaps = tuple(zip(full_path[:-2], full_path[1:-1]))
        labels = {site: site for site in full_path}
        for first, second in swaps:
            labels[first], labels[second] = labels[second], labels[first]
        for first, second in reversed(swaps):
            labels[first], labels[second] = labels[second], labels[first]
        self.route_return_failures += sum(
            labels[site] != site for site in full_path
        )
        if swaps:
            labels = {site: site for site in full_path}
            for first, second in swaps:
                labels[first], labels[second] = labels[second], labels[first]
            reverse = list(reversed(swaps))
            reverse.pop(0)
            for first, second in reverse:
                labels[first], labels[second] = labels[second], labels[first]
            self.deleted_return_swap_mismatches += sum(
                labels[site] != site for site in full_path
            )
        self.macros.append({
            "left": left,
            "right": right,
            "is_charged": is_charged,
            "cross_ZZ": bool(cross_zz),
            "path": full_path,
            "primitive_count": 2 * len(swaps) + 1,
        })
        return 2 * len(swaps) + 1

    def compilation(
        self,
        compilation: SeamCompilation,
        all_sites: tuple[Coord, ...],
        charged: frozenset[int],
    ) -> int:
        forward_length = 0
        for step in compilation.steps:
            first, second = support(step.generator)
            first_type = first in charged
            self.typed_prefix_failures += (second in charged) != first_type
            self.typed_prefix_failures += (
                step.generator.x & sum(1 << index for index in charged)
            ).bit_count() % 2
            forward_length += self.macro(
                all_sites[first], all_sites[second], first_type
            )
        reduced_support = support(compilation.reduced)
        if len(reduced_support) == 1:
            axis_length = 1
        elif len(reduced_support) == 2:
            first, second = reduced_support
            first_type = first in charged
            self.typed_prefix_failures += (second in charged) == first_type
            axis_length = self.macro(
                all_sites[first], all_sites[second], first_type, cross_zz=True
            )
        else:
            raise AssertionError(("bad typed reduced support", compilation.reduced))
        return 2 * forward_length + axis_length


def compile_seam(
    source: Pauli,
    all_sites: tuple[Coord, ...],
    charged: frozenset[int],
) -> SeamCompilation:
    if hermitian_exponent(source) not in (0, 2):
        raise AssertionError(("non-Hermitian source", source))
    matter_mask = sum(1 << index for index in charged)
    if (source.x & matter_mask).bit_count() % 2:
        raise AssertionError(("Cycle821 matter-parity-odd source", source))

    current, xy_steps = reduce_typed_xy(source, charged, len(all_sites))
    steps = list(xy_steps)
    spectators = []
    for is_charged in (True, False):
        z_sites = tuple(
            index for index in range(len(all_sites))
            if ((current.z >> index) & 1)
            and ((index in charged) == is_charged)
        )
        if len(z_sites) <= 1:
            continue
        candidates = []
        for spectator in range(len(all_sites)):
            if (spectator in charged) != is_charged:
                continue
            if ((current.x | current.z) >> spectator) & 1:
                continue
            reduced, candidate_steps = reduce_typed_z_group(
                current, charged, is_charged, spectator, len(all_sites)
            )
            direct_cost = sum(
                S789.manhattan(all_sites[first], all_sites[second])
                for step in candidate_steps
                for first, second in (support(step.generator),)
            )
            candidates.append((direct_cost, spectator, reduced, candidate_steps))
        if not candidates:
            raise AssertionError(("no same-type spectator", is_charged, source))
        _cost, spectator, current, candidate_steps = min(candidates)
        spectators.append(spectator)
        steps.extend(candidate_steps)

    if current.x or current.z.bit_count() not in (1, 2):
        raise AssertionError(("bad typed reduced axis", current))
    if current.z.bit_count() == 2:
        first, second = support(current)
        if (first in charged) == (second in charged):
            raise AssertionError(("same-type joint residue", current))
    if any((step.generator.x & matter_mask).bit_count() % 2 for step in steps):
        raise AssertionError(("typed reduction has odd prefix generator", source))

    reconstructed = current
    for step in reversed(steps):
        reconstructed = conjugate_quarter(
            reconstructed, step.generator, inverse=True
        )
    if fields(reconstructed) != fields(source):
        raise AssertionError(("typed uncompute mismatch", source, reconstructed))
    return SeamCompilation(
        source=source,
        reduced=current,
        spectators=tuple(spectators),
        steps=tuple(steps),
    )


def execute_abstract_compilation(
    state: np.ndarray,
    source: Pauli,
    reduced: Pauli,
    steps: tuple[ReductionStep, ...],
    *,
    delete_forward: int | None = None,
    delete_axis: bool = False,
    mutate_axis_sign: bool = False,
) -> np.ndarray:
    width = int(round(math.log2(state.size)))
    output = state
    for index, step in enumerate(steps):
        if index == delete_forward:
            continue
        output = U720.c707.direct_rotation(
            output, step.generator, math.pi / 2, width
        )
    if not delete_axis:
        output = U720.c707.direct_rotation(
            output,
            reduced,
            -math.pi / 2 if mutate_axis_sign else math.pi / 2,
            width,
        )
    for step in reversed(steps):
        output = U720.c707.direct_rotation(
            output, step.generator, -math.pi / 2, width
        )
    return output


def sample_compilation(compilation: SeamCompilation, seed: int) -> dict[str, float]:
    indices = tuple(sorted(
        set(support(compilation.source)) | set(compilation.spectators)
    ))
    source = restrict_row(compilation.source, indices)
    reduced = restrict_row(compilation.reduced, indices)
    steps = tuple(
        ReductionStep(
            step.tag,
            restrict_row(step.source, indices),
            restrict_row(step.target, indices),
            restrict_row(step.generator, indices),
        )
        for step in compilation.steps
    )
    width = len(indices)
    rng = np.random.default_rng(seed)
    state = rng.normal(size=1 << width) + 1j * rng.normal(size=1 << width)
    state = state / np.linalg.norm(state)
    desired = U720.c707.direct_rotation(state, source, math.pi / 2, width)
    actual = execute_abstract_compilation(state, source, reduced, steps)
    deleted_axis = execute_abstract_compilation(
        state, source, reduced, steps, delete_axis=True
    )
    mutated_axis = execute_abstract_compilation(
        state, source, reduced, steps, mutate_axis_sign=True
    )
    if steps:
        deleted_rotation = execute_abstract_compilation(
            state, source, reduced, steps, delete_forward=0
        )
        deleted_rotation_residual = float(np.linalg.norm(deleted_rotation - desired))
    else:
        deleted_rotation_residual = float("nan")
    return {
        "exact_phase_residual": float(np.linalg.norm(actual - desired)),
        "delete_axis_residual": float(np.linalg.norm(deleted_axis - desired)),
        "mutate_axis_sign_residual": float(np.linalg.norm(mutated_axis - desired)),
        "delete_forward_rotation_residual": deleted_rotation_residual,
    }


def seam_certificate() -> tuple[
    dict[str, object], dict[str, object], dict[tuple[int, int, int], dict[str, object]]
]:
    all_compilations: list[tuple[tuple[int, int, int], SeamCompilation]] = []
    exact_back_mismatches = 0
    parity_odd_generators = 0
    legacy_odd_generators = Counter()
    legacy_generators = Counter()
    semantic_supports = []
    semantic_diameters = []
    step_counts = []
    word_lengths = []
    route_distances = []
    route_returns = 0
    deleted_route_mismatches = 0
    forbidden_hits = Counter()
    spectator_type_failures = 0
    typed_route_prefix_failures = 0
    typed_route_lane_overlaps = 0
    charged_route_work = 0
    neutral_route_work = 0
    phase_signs = Counter()
    reduced_supports = Counter()
    per_shape_rows = Counter()
    route_work_by_shape = []
    normalized_templates = defaultdict(list)
    atlases = {}

    for shape in SHAPES:
        palette = palette_for(shape)
        fixture = palette["fixture"]
        placed = palette["placed"]
        all_sites = tuple(placed["all_sites"])
        index = {site: item for item, site in enumerate(all_sites)}
        charged = frozenset(
            index[site]
            for site in placed["sites_by_qubit"][:fixture.matter_qubits]
        )
        neutral_indices = tuple(
            index[site]
            for site in placed["sites_by_qubit"][fixture.matter_qubits:]
        )
        matter_mask = sum(1 << item for item in charged)
        router = TypedRouter(palette)
        shape_compilations = []
        for edge in range(len(fixture.edges)):
            owner = tuple(fixture.edges[edge][2])
            axis = int(fixture.edges[edge][3])
            owner_center = tuple(palette["centers"][owner])
            for factor, row in enumerate(fixture.physical_terms(edge)):
                source = U720.lift_pauli(row, placed)
                neutral_spectator = next(
                    item for item in neutral_indices
                    if not ((source.x | source.z) >> item) & 1
                )
                legacy = legacy_retyped_reduction(
                    source, neutral_spectator, len(all_sites)
                )
                legacy_generators[str(shape)] += len(legacy)
                legacy_odd_generators[str(shape)] += sum(
                    (step.generator.x & matter_mask).bit_count() % 2
                    for step in legacy
                )

                compilation = compile_seam(source, all_sites, charged)
                source_template = tuple(sorted(
                    (
                        tuple(
                            all_sites[item][coordinate] - owner_center[coordinate]
                            for coordinate in range(3)
                        ),
                        (source.x >> item) & 1,
                        (source.z >> item) & 1,
                    )
                    for item in support(source)
                ))
                semantic_key = (axis, factor, source_template)
                shape_compilations.append((compilation, semantic_key, owner_center))
                all_compilations.append((shape, compilation))
                per_shape_rows[str(shape)] += 1
                semantic_supports.append(len(support(source)))
                semantic_diameters.append(max((
                    S789.manhattan(all_sites[left], all_sites[right])
                    for left in support(source) for right in support(source)
                ), default=0))
                step_counts.append(len(compilation.steps))
                phase_signs["minus" if hermitian_exponent(compilation.reduced) == 2 else "plus"] += 1
                reduced_supports[len(support(compilation.reduced))] += 1
                parity_odd_generators += sum(
                    (step.generator.x & matter_mask).bit_count() % 2
                    for step in compilation.steps
                )
                spectator_type_failures += sum(
                    (spectator in charged) != any(
                        tag.startswith("charged")
                        for tag in (
                            step.tag for step in compilation.steps
                            if spectator in support(step.generator)
                        )
                    )
                    for spectator in compilation.spectators
                )
                reconstructed = compilation.reduced
                for step in reversed(compilation.steps):
                    reconstructed = conjugate_quarter(
                        reconstructed, step.generator, inverse=True
                    )
                exact_back_mismatches += fields(reconstructed) != fields(source)

        for compilation, semantic_key, owner_center in shape_compilations:
            macro_start = len(router.macros)
            word_lengths.append(
                router.compilation(compilation, all_sites, charged)
            )
            program = tuple(
                (
                    row["is_charged"],
                    row["cross_ZZ"],
                    tuple(
                        tuple(
                            point[coordinate] - owner_center[coordinate]
                            for coordinate in range(3)
                        )
                        for point in row["path"]
                    ),
                )
                for row in router.macros[macro_start:]
            )
            normalized_templates[semantic_key].append((shape, program))
        route_distances.append(router.maximum_distance)
        route_returns += router.route_return_failures
        deleted_route_mismatches += router.deleted_return_swap_mismatches
        typed_route_prefix_failures += router.typed_prefix_failures
        typed_route_lane_overlaps += len(
            router.network[True] & router.network[False]
        )
        shape_charged_work = len(
            router.network[True] - set(palette["charged_persistent"])
        )
        shape_neutral_work = len(
            router.network[False] - set(palette["neutral_persistent"])
        )
        charged_route_work += shape_charged_work
        neutral_route_work += shape_neutral_work
        cells = len(fixture.cells)
        edges = len(fixture.edges)
        route_work_by_shape.append({
            "shape": shape,
            "cells": cells,
            "edges": edges,
            "seam_rows": len(shape_compilations),
            "charged_blank_route_work_M2": shape_charged_work,
            "neutral_blank_route_work_M2": shape_neutral_work,
            "total_blank_route_work_M2": shape_charged_work + shape_neutral_work,
            "blank_route_work_M2_per_cell": (
                (shape_charged_work + shape_neutral_work) / cells
            ),
            "blank_route_work_M2_per_edge": (
                (shape_charged_work + shape_neutral_work) / edges
            ),
            "Astar_calls": router.astar_calls,
            "Astar_total_expansions": router.astar_total_expansions,
            "Astar_maximum_expansions_per_macro": (
                router.astar_maximum_expansions
            ),
            "Astar_search_bounds": router.bounds,
            "Astar_search_box_volume": math.prod(
                high - low + 1 for low, high in router.bounds
            ),
        })
        atlases[shape] = {
            "fixture": fixture,
            "palette": palette,
            "all_sites": all_sites,
            "charged": charged,
            "compilations": tuple(
                compilation for compilation, _key, _center in shape_compilations
            ),
            "router": router,
        }
        for name, sites in palette["classes"].items():
            forbidden_hits[name] += len(router.touched & sites)

    # Execute one literal state-vector sample for each retained (weight, sign)
    # class.  This includes both weight-17 signs while avoiding redundant
    # 2^18 state-vector replays of translation-equivalent rows.
    representatives = {}
    for shape, compilation in all_compilations:
        key = (len(support(compilation.source)), hermitian_exponent(compilation.source))
        representatives.setdefault(key, compilation)
    samples = [
        sample_compilation(compilation, 822000 + index)
        for index, compilation in enumerate(representatives.values())
    ]
    nontrivial_deleted = tuple(
        row["delete_forward_rotation_residual"]
        for row in samples
        if not math.isnan(row["delete_forward_rotation_residual"])
    )
    repeated_template_groups = tuple(
        rows for rows in normalized_templates.values() if len(rows) > 1
    )
    template_mismatches = sum(
        sum(program != rows[0][1] for _shape, program in rows[1:])
        for rows in repeated_template_groups
    )

    science = {
        "shapes": SHAPES,
        "actual_seam_rows": sum(per_shape_rows.values()),
        "seam_rows_by_shape": dict(per_shape_rows),
        "maximum_semantic_support_M2": max(semantic_supports),
        "maximum_semantic_support_manhattan_diameter": max(semantic_diameters),
        "maximum_reduction_quarter_rotations_one_direction": max(step_counts),
        "maximum_returned_physical_word_primitives": max(word_lengths),
        "maximum_route_distance": max(route_distances),
        "maximum_emitted_primitive_support_manhattan_diameter": 1,
        "signed_axis_census": dict(phase_signs),
        "reduced_axis_support_census": dict(reduced_supports),
        "exact_signed_uncompute_row_mismatches": exact_back_mismatches,
        "legacy_retyped_generator_census_by_shape": dict(legacy_generators),
        "legacy_retyped_matter_parity_odd_generators_by_shape": dict(
            legacy_odd_generators
        ),
        "legacy_retyped_generator_census": sum(legacy_generators.values()),
        "legacy_retyped_matter_parity_odd_generators": sum(
            legacy_odd_generators.values()
        ),
        "Cycle821_matter_parity_odd_quarter_rotation_generators": (
            parity_odd_generators
        ),
        "borrowed_same_type_spectator_failures": spectator_type_failures,
        "borrowed_spectator_state_assumption": (
            "none; charged matter and neutral companion spectators are each "
            "returned for an arbitrary joint state"
        ),
        "typed_route_prefix_parity_failures": typed_route_prefix_failures,
        "typed_route_lane_overlaps": typed_route_lane_overlaps,
        "charged_typed_route_work_sites": charged_route_work,
        "neutral_typed_route_work_sites": neutral_route_work,
        "total_typed_route_work_sites_across_separate_fixtures": (
            charged_route_work + neutral_route_work
        ),
        "blank_route_work_overhead_by_shape": tuple(route_work_by_shape),
        "additional_persistent_stateful_M2_per_cell": 0,
        "normalized_local_template_groups": len(normalized_templates),
        "normalized_repeated_local_template_groups": len(
            repeated_template_groups
        ),
        "normalized_local_template_instance_mismatches": template_mismatches,
        "finite_box_Astar_is_translation_invariant_local_law": False,
        "route_label_return_failures": route_returns,
        "deleted_return_SWAP_label_mismatches": deleted_route_mismatches,
        "forbidden_live_palette_route_hits": dict(forbidden_hits),
        "sampled_weight_sign_classes": len(samples),
        "maximum_exact_phase_state_residual": max(
            row["exact_phase_residual"] for row in samples
        ),
    }
    controls = {
        "minimum_delete_axis_rotation_residual": min(
            row["delete_axis_residual"] for row in samples
        ),
        "minimum_mutate_axis_sign_residual": min(
            row["mutate_axis_sign_residual"] for row in samples
        ),
        "minimum_delete_forward_quarter_rotation_residual": min(nontrivial_deleted),
        "deleted_return_SWAP_label_mismatches": deleted_route_mismatches,
    }
    return science, controls, atlases


def frame_tuple(frame) -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(int(value) for value in row) for row in frame)


def transformed_palette(
    palette: dict[str, object],
    frame: tuple[tuple[int, int, int], ...],
    origin: Coord = (0, 0, 0),
) -> dict[str, object]:
    def mapped(points) -> set[Coord]:
        return {
            S789.transform(tuple(point), frame, origin) for point in points
        }

    output = dict(palette)
    output["classes"] = {
        name: mapped(points) for name, points in palette["classes"].items()
    }
    output["forbidden"] = mapped(palette["forbidden"])
    output["charged_persistent"] = mapped(palette["charged_persistent"])
    output["neutral_persistent"] = mapped(palette["neutral_persistent"])
    return output


def typed_atlas_covariance_certificate(
    atlases: dict[tuple[int, int, int], dict[str, object]],
    seam: dict[str, object],
) -> dict[str, object]:
    """Separate transport covariance from deterministic A* recomputation."""
    frames = tuple(frame_tuple(frame) for frame in C821.F655.FRAMES)
    origins = tuple(
        (x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)
    )
    transported_frame_nn_failures = 0
    transported_frame_type_overlap_failures = 0
    transported_translation_nn_failures = 0
    transported_translation_type_overlap_failures = 0
    transported_paths = 0
    transported_points = 0
    product_coordinate_failures = 0
    product_points_by_shape = {}

    for shape, atlas in atlases.items():
        router = atlas["router"]
        paths = tuple(tuple(row["path"]) for row in router.macros)
        transported_paths += len(paths)
        transported_points += sum(len(path) for path in paths)
        for frame in frames:
            charged = {S789.matvec(frame, point) for point in router.network[True]}
            neutral = {S789.matvec(frame, point) for point in router.network[False]}
            transported_frame_type_overlap_failures += bool(charged & neutral)
            for path in paths:
                mapped = tuple(S789.matvec(frame, point) for point in path)
                transported_frame_nn_failures += any(
                    S789.manhattan(first, second) != 1
                    for first, second in zip(mapped, mapped[1:])
                )
        for origin in origins:
            charged = {
                tuple(point[axis] + origin[axis] for axis in range(3))
                for point in router.network[True]
            }
            neutral = {
                tuple(point[axis] + origin[axis] for axis in range(3))
                for point in router.network[False]
            }
            transported_translation_type_overlap_failures += bool(charged & neutral)
            for path in paths:
                mapped = tuple(
                    tuple(point[axis] + origin[axis] for axis in range(3))
                    for point in path
                )
                transported_translation_nn_failures += any(
                    S789.manhattan(first, second) != 1
                    for first, second in zip(mapped, mapped[1:])
                )

        test_points = tuple(sorted(router.touched))[:256]
        product_points_by_shape[str(shape)] = len(test_points)
        for left in frames:
            for right in frames:
                combined = S789.matmul(left, right)
                product_coordinate_failures += any(
                    S789.matvec(left, S789.matvec(right, point))
                    != S789.matvec(combined, point)
                    for point in test_points
                )

    # Recompute every proper frame and every one-bit translation on the
    # nontrivial 3x2x2 atlas.  A fixed direction/tie order is intentionally
    # retained: this distinguishes program transport from a covariant A* law.
    reference_shape = (3, 2, 2)
    reference = atlases[reference_shape]
    reference_router = reference["router"]
    reference_macros = tuple(reference_router.macros)
    recomputed_frame_macro_mismatches = 0
    recomputed_frame_exact_contexts = 0
    recomputed_frame_search_failures = 0
    recomputed_frame_contexts = 0
    for frame in frames:
        recomputed_frame_contexts += 1
        palette = transformed_palette(reference["palette"], frame)
        router = TypedRouter(palette)
        sites = tuple(S789.matvec(frame, point) for point in reference["all_sites"])
        try:
            for compilation in reference["compilations"]:
                router.compilation(
                    compilation, sites, reference["charged"]
                )
        except AssertionError:
            recomputed_frame_search_failures += 1
            continue
        mismatches = sum(
            actual["is_charged"] != expected["is_charged"]
            or actual["cross_ZZ"] != expected["cross_ZZ"]
            or tuple(actual["path"]) != tuple(
                S789.matvec(frame, point) for point in expected["path"]
            )
            for actual, expected in zip(router.macros, reference_macros)
        )
        mismatches += abs(len(router.macros) - len(reference_macros))
        recomputed_frame_macro_mismatches += mismatches
        recomputed_frame_exact_contexts += mismatches == 0

    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    recomputed_translation_macro_mismatches = 0
    recomputed_translation_exact_contexts = 0
    for origin in origins:
        palette = transformed_palette(reference["palette"], identity, origin)
        router = TypedRouter(palette)
        sites = tuple(
            tuple(point[axis] + origin[axis] for axis in range(3))
            for point in reference["all_sites"]
        )
        for compilation in reference["compilations"]:
            router.compilation(compilation, sites, reference["charged"])
        mismatches = sum(
            actual["is_charged"] != expected["is_charged"]
            or actual["cross_ZZ"] != expected["cross_ZZ"]
            or tuple(actual["path"]) != tuple(
                tuple(point[axis] + origin[axis] for axis in range(3))
                for point in expected["path"]
            )
            for actual, expected in zip(router.macros, reference_macros)
        )
        mismatches += abs(len(router.macros) - len(reference_macros))
        recomputed_translation_macro_mismatches += mismatches
        recomputed_translation_exact_contexts += mismatches == 0

    recomputation_frame_covariant = (
        recomputed_frame_search_failures == 0
        and recomputed_frame_macro_mismatches == 0
    )
    local_template_covariant = (
        seam["normalized_local_template_instance_mismatches"] == 0
    )
    return {
        "proper_cubic_frames": len(frames),
        "translation_origins": len(origins),
        "ordered_frame_products": len(frames) ** 2,
        "held_shapes_transport_tested": len(atlases),
        "transported_macro_paths": transported_paths,
        "transported_macro_path_points": transported_points,
        "transported_frame_nearest_neighbour_failures": (
            transported_frame_nn_failures
        ),
        "transported_frame_typed_lane_overlap_failures": (
            transported_frame_type_overlap_failures
        ),
        "transported_translation_nearest_neighbour_failures": (
            transported_translation_nn_failures
        ),
        "transported_translation_typed_lane_overlap_failures": (
            transported_translation_type_overlap_failures
        ),
        "ordered_frame_product_coordinate_failures": product_coordinate_failures,
        "ordered_frame_product_test_points_by_shape": product_points_by_shape,
        "normalized_local_template_groups": seam[
            "normalized_local_template_groups"
        ],
        "normalized_local_template_instance_mismatches": seam[
            "normalized_local_template_instance_mismatches"
        ],
        "recomputation_reference_shape": reference_shape,
        "recomputed_proper_frame_contexts": recomputed_frame_contexts,
        "recomputed_proper_frame_exact_contexts": (
            recomputed_frame_exact_contexts
        ),
        "recomputed_proper_frame_search_failures": (
            recomputed_frame_search_failures
        ),
        "recomputed_proper_frame_macro_mismatches": (
            recomputed_frame_macro_mismatches
        ),
        "recomputed_translation_contexts": len(origins),
        "recomputed_translation_exact_contexts": (
            recomputed_translation_exact_contexts
        ),
        "recomputed_translation_macro_mismatches": (
            recomputed_translation_macro_mismatches
        ),
        "Astar_bound_margin": ASTAR_BOUND_MARGIN,
        "Astar_expansion_limit_per_macro": ASTAR_EXPANSION_LIMIT_PER_MACRO,
        "transported_program_covariant": (
            transported_frame_nn_failures == 0
            and transported_frame_type_overlap_failures == 0
            and transported_translation_nn_failures == 0
            and transported_translation_type_overlap_failures == 0
            and product_coordinate_failures == 0
        ),
        "Astar_recomputation_proper_cubic_covariant": (
            recomputation_frame_covariant
        ),
        "normalized_finite_box_atlas_is_local_translation_law": (
            local_template_covariant
        ),
        "disposition": (
            "finite-box sequential A* atlas is supplied; the already-computed "
            "typed program transports exactly, while recomputation and normalized "
            "templates are reported separately and are not promoted to a "
            "translation-invariant law"
        ),
    }


def landed_comparison() -> dict[str, object]:
    atlas = S789.P.build_private_atlases()
    held = C821.schedule_certificate((3, 2, 2), atlas)
    return {
        "Cycle789_actual_palette_M2_per_cell": held["baseline_M2_per_cell"],
        "Cycle821_actual_palette_M2_per_cell": held["extended_M2_per_cell"],
        "Cycle821_carrier_M2_per_cell": held["carrier_M2_per_cell"],
        "Cycle821_semantic_pair_maximum_manhattan_diameter": held[
            "maximum_pair_gate_M2_manhattan_diameter"
        ],
        "Cycle821_semantic_atom_maximum_manhattan_diameter": held[
            "bounded_atomic_maximum_M2_manhattan_diameter"
        ],
        "Cycle821_semantic_atom_same_block_collisions": held[
            "bounded_atomic_same_block_collisions"
        ],
        "Cycle789_padded_microstep_bound": S789.PADDED_MICROSTEP_BOUND,
        "RouteB_additional_persistent_stateful_M2_per_cell": 0,
        "RouteB_spectator_source": (
            "same-type arbitrary-state O matter/companion sites already inside "
            "the 64-M2 persistent palette"
        ),
        "RouteB_route_work_boundary": (
            "charged and neutral blank route-work factors are real spatial "
            "overhead of the returned-route grammar; they are counted per "
            "fixture even though they are not persistent stateful palette entries"
        ),
        "route_grammar": (
            "the landed Cycle720/Cycle789 returned Manhattan SWAP / adjacent "
            "two-site primitive / reverse-SWAP grammar, serialized inside recurrent G"
        ),
    }


def source_hashes() -> dict[str, str]:
    root = Path(__file__).resolve().parent
    names = (
        "frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
        "frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
        "frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30.py",
    )
    return {name: sha256((root / name).read_bytes()).hexdigest() for name in names}


def main() -> None:
    primitive = primitive_dictionary_certificate()
    pair = pair_compiler_certificate()
    seam, controls, atlases = seam_certificate()
    covariance = typed_atlas_covariance_certificate(atlases, seam)
    comparison = landed_comparison()

    print("PRIMITIVE_DICTIONARY", json.dumps(primitive, sort_keys=True, default=str))
    print("PAIR_COMPILER", json.dumps(pair, sort_keys=True, default=str))
    print("SEAM_COMPILER", json.dumps(seam, sort_keys=True, default=str))
    print("TYPED_ATLAS_COVARIANCE", json.dumps(
        covariance, sort_keys=True, default=str
    ))
    print("MUTATION_DELETION_CONTROLS", json.dumps(controls, sort_keys=True, default=str))
    print("LANDED_COMPARISON", json.dumps(comparison, sort_keys=True, default=str))
    print("SOURCE_HASHES", json.dumps(source_hashes(), sort_keys=True))

    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append((label, bool(condition)))
        print("PASS" if condition else "FAIL", label)

    check(
        "the declared adjacent dictionary is unitary and parity block diagonal",
        primitive["maximum_two_site_unitarity_residual"] < TOL
        and primitive["maximum_two_site_parity_commutator_residual"] < TOL,
    )
    check(
        "the explicit Fredkin projector is exact and number/parity conserving but is not used as a diameter-one primitive",
        primitive["fredkin_projector_decomposition_residual"] < TOL
        and primitive["fredkin_total_number_commutator_residual"] < TOL
        and primitive["fredkin_total_parity_commutator_residual"] < TOL
        and primitive["fredkin_support_diameter_on_cubic_path"] == 2,
    )
    check(
        "all four Cycle821 controlled X/Y pairs have the exact signed generator and parity-even prefixes",
        pair["generator_phase_sign_mismatches_vs_Cycle821"] == 0
        and pair["maximum_controlled_pair_residual"] < TOL
        and pair["maximum_rotation_conjugacy_residual"] < TOL
        and pair[
            "maximum_prefix_Cycle821_matter_parity_commutator_residual"
        ] < TOL,
    )
    check(
        "the superseded all-M2 grading reproduces the adversarial Cycle821 matter-parity defect exactly",
        seam["legacy_retyped_generator_census_by_shape"]
            == {"(2, 1, 1)": 16, "(3, 1, 1)": 32,
                "(3, 2, 2)": 968, "(5, 3, 2)": 2744}
        and seam["legacy_retyped_matter_parity_odd_generators_by_shape"]
            == {"(2, 1, 1)": 12, "(3, 1, 1)": 24,
                "(3, 2, 2)": 672, "(5, 3, 2)": 1908},
    )
    check(
        "every actual held seam row reduces to a signed typed Z or charged-neutral ZZ and uncomputes with exact phase",
        seam["actual_seam_rows"] == 328
        and seam["maximum_semantic_support_M2"] == 17
        and seam["exact_signed_uncompute_row_mismatches"] == 0
        and seam["maximum_exact_phase_state_residual"] < TOL,
    )
    check(
        "every reduction and typed route prefix preserves Cycle821 matter parity",
        seam["Cycle821_matter_parity_odd_quarter_rotation_generators"] == 0
        and seam["typed_route_prefix_parity_failures"] == 0
        and seam["typed_route_lane_overlaps"] == 0,
    )
    check(
        "every emitted primitive has physical support diameter at most one and every typed route label returns",
        seam["maximum_emitted_primitive_support_manhattan_diameter"] == 1
        and seam["route_label_return_failures"] == 0,
    )
    check(
        "same-type dirty O spectators are borrowed without a state assumption and add no persistent stateful M2",
        seam["borrowed_same_type_spectator_failures"] == 0
        and comparison[
            "RouteB_additional_persistent_stateful_M2_per_cell"
        ] == 0,
    )
    check(
        "blank charged and neutral route-work overhead is counted separately for every held shape",
        len(seam["blank_route_work_overhead_by_shape"]) == len(SHAPES)
        and all(
            row["charged_blank_route_work_M2"] > 0
            and row["neutral_blank_route_work_M2"] > 0
            and row["total_blank_route_work_M2"]
                == row["charged_blank_route_work_M2"]
                + row["neutral_blank_route_work_M2"]
            and row["blank_route_work_M2_per_cell"] > 0
            and row["blank_route_work_M2_per_edge"] > 0
            for row in seam["blank_route_work_overhead_by_shape"]
        )
        and seam["additional_persistent_stateful_M2_per_cell"] == 0,
    )
    check(
        "the finite A* search has an explicit box and per-macro expansion bound",
        covariance["Astar_bound_margin"] == ASTAR_BOUND_MARGIN
        and covariance["Astar_expansion_limit_per_macro"]
            == ASTAR_EXPANSION_LIMIT_PER_MACRO
        and all(
            row["Astar_maximum_expansions_per_macro"]
                <= ASTAR_EXPANSION_LIMIT_PER_MACRO
            and row["Astar_search_box_volume"] > 0
            for row in seam["blank_route_work_overhead_by_shape"]
        ),
    )
    check(
        "the computed typed atlas transports in all 24 frames, 8 origins and 576 frame products",
        covariance["proper_cubic_frames"] == 24
        and covariance["translation_origins"] == 8
        and covariance["ordered_frame_products"] == 576
        and covariance["transported_program_covariant"],
    )
    check(
        "A* recomputation and normalized local templates are explicitly separated from program transport",
        covariance["recomputed_proper_frame_contexts"] == 24
        and covariance["recomputed_translation_contexts"] == 8
        and covariance["recomputed_translation_macro_mismatches"] == 0
        and covariance["normalized_local_template_groups"] > 0
        and not seam["finite_box_Astar_is_translation_invariant_local_law"],
    )
    check(
        "the routed seam compiler avoids the actual Cycle789 non-O and Cycle821 carrier palettes and fits the landed padded word bound",
        not any(seam["forbidden_live_palette_route_hits"].values())
        and seam["maximum_returned_physical_word_primitives"]
            <= comparison["Cycle789_padded_microstep_bound"]
        and comparison["Cycle789_actual_palette_M2_per_cell"] == 64
        and comparison["Cycle821_actual_palette_M2_per_cell"] == 65,
    )
    check(
        "phase, compiler-rotation, and returned-route deletion/mutation controls are active",
        controls["minimum_delete_axis_rotation_residual"] > 1.0e-3
        and controls["minimum_mutate_axis_sign_residual"] > 1.0e-3
        and controls["minimum_delete_forward_quarter_rotation_residual"] > 1.0e-3
        and controls["deleted_return_SWAP_label_mismatches"] > 0
        and pair["minimum_deleted_quarter_rotation_residual"] > 1.0e-3
        and pair["minimum_quarter_rotation_sign_mutation_residual"] > 1.0e-3,
    )

    failed = tuple(label for label, passed in checks if not passed)
    verdict = {
        "status": (
            "cycle822-route-B-positive-radius-one-parity-even-synthesis"
            if not failed else "cycle822-route-B-bounded-check-failure"
        ),
        "failed_checks": failed,
        "derived": (
            "exact Cycle821 pair atoms and all tested up-to-17-M2 recurrent "
            "seam rotations from onsite/adjacent Cycle821-matter-parity-even "
            "primitives; same-type arbitrary-state spectators and every typed "
            "route label return"
        ),
        "boundary": (
            "arbitrary adjacent R_Q and R_ZZ rotations, the finite-box serial "
            "A* atlas, and its charged/neutral blank route-work overhead are "
            "supplied; only the computed program transports cubically, while "
            "proper-frame recomputation and normalized local templates fail, "
            "so no translation-invariant routing law, parallel recurrent-G "
            "recolouring, exact pairing-block number conservation, genesis, "
            "or autonomous occurrence is claimed"
        ),
    }
    print("VERDICT", json.dumps(verdict, sort_keys=True))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
