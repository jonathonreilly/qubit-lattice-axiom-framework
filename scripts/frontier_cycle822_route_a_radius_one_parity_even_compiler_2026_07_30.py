#!/usr/bin/env python3
"""Cycle-822 Route A radius-one parity-even physical compiler.

This runner closes two elementary-synthesis surfaces left open by Cycle 821:

* the two-target controlled Pauli atom is compiled by returned nearest-
  neighbour routes, the Cycle-821 two-mode diagonalizer, and a local CZ; and
* every landed Cycle-720 recurrent seam factor is compiled with a clean
  dual-rail one-excitation parity token, local Fredkins, a one-mode phase, and
  exact uncomputation.

The fixed tensor-frame Pauli convention matters.  A routed transposition is
implemented as CZ FSWAP = SWAP.  Thus every hop contains the physical FSWAP
factor and its local even CZ sign firewall.  Deleting the firewall, or
replacing FSWAP by SWAP while retaining it, produces the wrong graded route.

All gates have support in one cubic radius-one ball.  The compiler assumes the
two clean token rails, route workspace, chart, and program occurrence.  It
does not derive their genesis or autonomous renewal.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
import json
import math
from pathlib import Path

import numpy as np

import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U720
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S789
import frontier_full128_25site_nn_circuit_core_2026_07_24 as S25


AUDIT_TIMEOUT_SEC = 1200
NOTE_PATH = (
    "docs/ROUTE_A_RADIUS_ONE_PARITY_EVEN_COMPILER_"
    "CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    "scripts/frontier_cycle822_route_a_radius_one_parity_even_compiler_2026_07_30.py",
    "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md",
    "docs/THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/LITERAL_THREE_BANK_PREFIX_RECURRENT_G_ACTUAL_SHEAR_CYCLE794_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/LOCAL_PARITY_EXCHANGE_CARRIER_RECURRENT_BELL_CYCLE821_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle789_three_register_even_car_channel_2026_07_30.py",
    "scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
    "scripts/frontier_cycle794_literal_prefix_recurrent_G_substitution_2026_07_30.py",
    "scripts/frontier_cycle794_literal_three_bank_prefix_core_2026_07_30.py",
    "scripts/frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30.py",
    "scripts/frontier_cycle821_local_parity_exchange_carrier_independent_2026_07_30.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


Coord = tuple[int, int, int]
TOL = 1.0e-12
I2 = np.eye(2, dtype=complex)
X = np.asarray(((0, 1), (1, 0)), dtype=complex)
Y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
Z = np.diag((1, -1)).astype(complex)
CZ = np.diag((1, 1, 1, -1)).astype(complex)
FSWAP = np.asarray(S25.FSWAP, dtype=complex)
SWAP = np.asarray(S25.SWAP, dtype=complex)
PAULI = {"X": X, "Y": Y, "Z": Z}


def fredkin_matrix() -> np.ndarray:
    """Control is local bit 0; the two token rails are local bits 1 and 2."""
    output = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        control = source & 1
        left = (source >> 1) & 1
        right = (source >> 2) & 1
        if control:
            left, right = right, left
        target = control | (left << 1) | (right << 2)
        output[target, source] = 1
    return output


FREDKIN = fredkin_matrix()


@dataclass(frozen=True)
class LocalGate:
    kind: str
    sites: tuple[Coord, ...]
    matrix: np.ndarray


@dataclass(frozen=True)
class ReturnedMacro:
    kind: str
    source: Coord
    target: Coord
    path: tuple[Coord, ...]
    active_sites: tuple[Coord, ...]
    gates: tuple[LocalGate, ...]
    route_hops: int
    operand_failures: int
    return_failures: int
    deleted_return_label_mismatches: int


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def axis_path(
    source: Coord, target: Coord, axes: tuple[int, int, int]
) -> tuple[Coord, ...]:
    path = [source]
    cursor = list(source)
    for axis in axes:
        step = 1 if target[axis] > cursor[axis] else -1
        while cursor[axis] != target[axis]:
            cursor[axis] += step
            path.append(tuple(cursor))
    if path[-1] != target or any(
        manhattan(left, right) != 1
        for left, right in zip(path, path[1:])
    ):
        raise AssertionError((source, target, axes, path))
    return tuple(path)


def transposition_hop(left: Coord, right: Coord) -> tuple[LocalGate, ...]:
    """Tensor-label transposition, factored into two local even gates."""
    if manhattan(left, right) != 1:
        raise AssertionError((left, right))
    return (
        LocalGate("route_FSWAP", (left, right), FSWAP),
        LocalGate("route_CZ_sign_firewall", (left, right), CZ),
    )


def label_audit(
    path: tuple[Coord, ...], hop_count: int, *, star: bool,
) -> tuple[int, int, int]:
    labels = {site: site for site in path}
    for index in range(hop_count):
        left, right = path[index], path[index + 1]
        labels[left], labels[right] = labels[right], labels[left]
    if star:
        operand_failures = int(labels[path[-1]] != path[0])
    else:
        operand_failures = int(labels[path[-2]] != path[0])
        operand_failures += int(labels[path[-1]] != path[-1])
    for index in reversed(range(hop_count)):
        left, right = path[index], path[index + 1]
        labels[left], labels[right] = labels[right], labels[left]
    return_failures = sum(labels[site] != site for site in path)

    dirty = {site: site for site in path}
    for index in range(hop_count):
        left, right = path[index], path[index + 1]
        dirty[left], dirty[right] = dirty[right], dirty[left]
    reverse = list(reversed(range(hop_count)))
    if reverse:
        reverse.pop(0)
    for index in reverse:
        left, right = path[index], path[index + 1]
        dirty[left], dirty[right] = dirty[right], dirty[left]
    deleted = sum(dirty[site] != site for site in path)
    return operand_failures, return_failures, deleted


def returned_two_site_macro(
    kind: str,
    source: Coord,
    target: Coord,
    matrix: np.ndarray,
) -> ReturnedMacro:
    path = axis_path(source, target, (0, 1, 2))
    if len(path) < 2:
        raise AssertionError((kind, source, target))
    hop_count = len(path) - 2
    forward = tuple(
        gate
        for index in range(hop_count)
        for gate in transposition_hop(path[index], path[index + 1])
    )
    active = (path[-2], path[-1])
    reverse = tuple(
        gate
        for index in reversed(range(hop_count))
        for gate in transposition_hop(path[index], path[index + 1])
    )
    audit = label_audit(path, hop_count, star=False)
    return ReturnedMacro(
        kind, source, target, path, active,
        forward + (LocalGate(kind, active, matrix),) + reverse,
        hop_count, *audit,
    )


def returned_star_macro(
    kind: str,
    control: Coord,
    center: Coord,
    rail_left: Coord,
    rail_right: Coord,
    matrix: np.ndarray,
) -> ReturnedMacro:
    # The token rails lie on the z-axis.  Approaching along x avoids both.
    path = axis_path(control, center, (2, 1, 0))
    if rail_left in path or rail_right in path:
        raise AssertionError(("token rail entered route", path))
    hop_count = len(path) - 1
    forward = tuple(
        gate
        for index in range(hop_count)
        for gate in transposition_hop(path[index], path[index + 1])
    )
    active = (center, rail_left, rail_right)
    reverse = tuple(
        gate
        for index in reversed(range(hop_count))
        for gate in transposition_hop(path[index], path[index + 1])
    )
    audit = label_audit(path, hop_count, star=True)
    return ReturnedMacro(
        kind, control, center, path, active,
        forward + (LocalGate(kind, active, matrix),) + reverse,
        hop_count, *audit,
    )


def local_pair_matrix(first_letter: str, second_letter: str) -> np.ndarray:
    # First listed mode is local bit zero.
    return np.kron(PAULI[second_letter], PAULI[first_letter])


def pair_diagonalizer(first_letter: str, second_letter: str) -> np.ndarray:
    """Cycle-821 U with U Z_first U^dag = first_letter second_letter."""
    if first_letter == "X":
        generator = np.kron(PAULI[second_letter], Y)
    elif first_letter == "Y":
        generator = np.kron(PAULI[second_letter], -X)
    else:
        raise ValueError((first_letter, second_letter))
    return (np.eye(4, dtype=complex) - 1j * generator) / math.sqrt(2)


def compile_controlled_pair(
    control: Coord,
    first: Coord,
    second: Coord,
    first_letter: str,
    second_letter: str,
    *,
    pivot_second: bool,
) -> tuple[tuple[LocalGate, ...], tuple[ReturnedMacro, ...]]:
    if pivot_second:
        pivot, other = second, first
        pivot_letter, other_letter = second_letter, first_letter
    else:
        pivot, other = first, second
        pivot_letter, other_letter = first_letter, second_letter
    unitary = pair_diagonalizer(pivot_letter, other_letter)
    macros = (
        returned_two_site_macro("pair_U_dagger", pivot, other, unitary.conj().T),
        returned_two_site_macro("controlled_Z", control, pivot, CZ),
        returned_two_site_macro("pair_U", pivot, other, unitary),
    )
    return tuple(gate for macro in macros for gate in macro.gates), macros


def embed(matrix: np.ndarray, wires: tuple[int, ...], count: int) -> np.ndarray:
    return S25.embed_gate(matrix, wires, count)


def dense_word(
    gates: tuple[LocalGate, ...], site_order: tuple[Coord, ...]
) -> tuple[np.ndarray, float]:
    lookup = {site: index for index, site in enumerate(site_order)}
    count = len(site_order)
    output = np.eye(1 << count, dtype=complex)
    parity = np.diag(tuple(
        (-1) ** state.bit_count() for state in range(1 << count)
    )).astype(complex)
    prefix_residual = 0.0
    for gate in gates:
        wires = tuple(lookup[site] for site in gate.sites)
        output = embed(gate.matrix, wires, count) @ output
        prefix_residual = max(prefix_residual, float(np.linalg.norm(
            output @ parity - parity @ output
        )))
    return output, prefix_residual


def dense_controlled_pair_target(
    count: int, control: int, first: int, second: int,
    first_letter: str, second_letter: str,
) -> np.ndarray:
    identity = np.eye(1 << count, dtype=complex)
    z_control = embed(Z, (control,), count)
    pair = embed(
        local_pair_matrix(first_letter, second_letter),
        (first, second), count,
    )
    return (identity + z_control) / 2 + pair @ (identity - z_control) / 2


def mutate_wrong_swap(gates: tuple[LocalGate, ...]) -> tuple[LocalGate, ...]:
    return tuple(
        LocalGate(gate.kind, gate.sites, SWAP)
        if gate.kind == "route_FSWAP" else gate
        for gate in gates
    )


def local_parity_residual(gate: LocalGate) -> float:
    count = len(gate.sites)
    parity = np.diag(tuple(
        (-1) ** state.bit_count() for state in range(1 << count)
    )).astype(complex)
    return float(np.linalg.norm(gate.matrix @ parity - parity @ gate.matrix))


def radius_one(gate: LocalGate) -> bool:
    return any(
        all(manhattan(center, site) <= 1 for site in gate.sites)
        for center in gate.sites
    )


def controlled_pair_certificate() -> dict[str, object]:
    sites = tuple((index, 0, 0) for index in range(5))
    control, first, second = sites[0], sites[4], sites[2]
    residuals = []
    wrong_swap_residuals = []
    deleted_return_residuals = []
    conjugacy_residuals = []
    prefix_residuals = []
    elementary_residuals = []
    deleted_returns = []
    route_returns = []
    operand_failures = []
    word_lengths = []
    for first_letter in ("X", "Y"):
        for second_letter in ("X", "Y"):
            for pivot_second in (False, True):
                gates, macros = compile_controlled_pair(
                    control, first, second, first_letter, second_letter,
                    pivot_second=pivot_second,
                )
                observed, prefix = dense_word(gates, sites)
                desired = dense_controlled_pair_target(
                    len(sites), 0, 4, 2, first_letter, second_letter
                )
                wrong, _ = dense_word(mutate_wrong_swap(gates), sites)
                deleted_word = []
                deleted = False
                for macro in macros:
                    if macro.route_hops and not deleted:
                        deleted_word.extend(macro.gates[:-2])
                        deleted = True
                    else:
                        deleted_word.extend(macro.gates)
                deleted_matrix, _ = dense_word(tuple(deleted_word), sites)
                pivot_letter, other_letter = (
                    (second_letter, first_letter)
                    if pivot_second else (first_letter, second_letter)
                )
                diagonalizer = pair_diagonalizer(
                    pivot_letter, other_letter
                )
                conjugacy_residuals.append(float(np.linalg.norm(
                    diagonalizer @ np.kron(I2, Z)
                    @ diagonalizer.conj().T
                    - local_pair_matrix(pivot_letter, other_letter)
                )))
                residuals.append(float(np.linalg.norm(observed - desired)))
                wrong_swap_residuals.append(float(np.linalg.norm(wrong - desired)))
                deleted_return_residuals.append(float(np.linalg.norm(
                    deleted_matrix - desired
                )))
                prefix_residuals.append(prefix)
                elementary_residuals.extend(
                    local_parity_residual(gate) for gate in gates
                )
                deleted_returns.extend(
                    macro.deleted_return_label_mismatches for macro in macros
                    if macro.route_hops
                )
                route_returns.extend(macro.return_failures for macro in macros)
                operand_failures.extend(macro.operand_failures for macro in macros)
                word_lengths.append(len(gates))
    return {
        "letter_pair_pivot_cases": len(residuals),
        "maximum_dense_compiled_residual": max(residuals),
        "maximum_Cycle821_U_conjugacy_residual": max(conjugacy_residuals),
        "maximum_dense_cumulative_prefix_parity_residual": max(prefix_residuals),
        "maximum_elementary_parity_commutator_residual": max(elementary_residuals),
        "route_operand_failures": sum(operand_failures),
        "route_return_failures": sum(route_returns),
        "minimum_deleted_return_label_mismatches": min(deleted_returns),
        "minimum_deleted_return_dense_residual": min(
            deleted_return_residuals
        ),
        "minimum_wrong_SWAP_for_FSWAP_mutation_residual": min(
            wrong_swap_residuals
        ),
        "maximum_primitives_per_compiled_pair": max(word_lengths),
        "transposition_factor_residual_CZ_FSWAP_minus_SWAP": float(
            np.linalg.norm(CZ @ FSWAP - SWAP)
        ),
    }


def pauli_letters(x: int, z: int, width: int) -> str:
    output = []
    for qubit in range(width):
        if ((x | z) >> qubit) & 1:
            xb, zb = (x >> qubit) & 1, (z >> qubit) & 1
            output.append(("I", "X", "Z", "Y")[xb + 2 * zb])
    return "".join(output)


def token_patch(support: tuple[Coord, ...]) -> tuple[Coord, Coord, Coord]:
    center = (
        max(site[0] for site in support) + 4,
        max(site[1] for site in support) + 4,
        max(site[2] for site in support) + 4,
    )
    return center, (center[0], center[1], center[2] - 1), (
        center[0], center[1], center[2] + 1
    )


def local_row(lifted, all_sites: tuple[Coord, ...]):
    indices = tuple(
        index for index in range(len(all_sites))
        if ((lifted.x | lifted.z) >> index) & 1
    )
    support = tuple(all_sites[index] for index in indices)
    x = sum(((lifted.x >> source) & 1) << target
            for target, source in enumerate(indices))
    z = sum(((lifted.z >> source) & 1) << target
            for target, source in enumerate(indices))
    return support, int(lifted.phase % 4), x, z


def row_groups(x: int, z: int, width: int, pivot_second: bool):
    odd = tuple(index for index in range(width) if (x >> index) & 1)
    if len(odd) % 2:
        raise AssertionError(("odd seam row", x, z, width))
    pairs = []
    for index in range(0, len(odd), 2):
        first, second = odd[index:index + 2]
        pairs.append((second, first) if pivot_second else (first, second))
    singles = tuple(
        index for index in range(width)
        if ((z >> index) & 1) and not ((x >> index) & 1)
    )
    return tuple(pairs), singles


def seam_program(
    support: tuple[Coord, ...], phase: int, x: int, z: int,
    *, pivot_second: bool, reverse_controls: bool,
) -> dict[str, object]:
    width = len(support)
    pairs, singles = row_groups(x, z, width, pivot_second)
    center, rail_left, rail_right = token_patch(support)
    pair_data = []
    pre_macros = []
    for pivot, other in pairs:
        pivot_letter = ("X", "Y")[int((z >> pivot) & 1)]
        other_letter = ("X", "Y")[int((z >> other) & 1)]
        unitary = pair_diagonalizer(pivot_letter, other_letter)
        pair_data.append((pivot, other, unitary))
        pre_macros.append(returned_two_site_macro(
            "seam_pair_U_dagger", support[pivot], support[other],
            unitary.conj().T,
        ))
    controls = tuple(pivot for pivot, _other in pairs) + singles
    if reverse_controls:
        controls = tuple(reversed(controls))
    accumulators = tuple(
        returned_star_macro(
            "token_Fredkin", support[control], center,
            rail_left, rail_right, FREDKIN,
        )
        for control in controls
    )
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
        returned_two_site_macro(
            "seam_pair_U", support[pivot], support[other], unitary
        )
        for pivot, other, unitary in reversed(pair_data)
    )
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
        "row_sign": row_sign,
        "effective_angle": effective_angle,
        "token": (rail_left, rail_right),
        "center": center,
    }


def apply_two_sparse(
    state: dict[int, complex], matrix: np.ndarray, wires: tuple[int, ...]
) -> dict[int, complex]:
    output: dict[int, complex] = {}
    for source, coefficient in state.items():
        local_source = sum(
            ((source >> wire) & 1) << index
            for index, wire in enumerate(wires)
        )
        for local_target in range(1 << len(wires)):
            amplitude = matrix[local_target, local_source]
            if abs(amplitude) < 1.0e-15:
                continue
            target = source
            for index, wire in enumerate(wires):
                if (local_target >> index) & 1:
                    target |= 1 << wire
                else:
                    target &= ~(1 << wire)
            output[target] = output.get(target, 0.0j) + amplitude * coefficient
    return output


def exhaustive_semantic_residual(
    phase: int, x: int, z: int, width: int,
    *, pivot_second: bool, reverse_controls: bool,
    token_bits: tuple[int, int] = (1, 0),
) -> float:
    pairs, singles = row_groups(x, z, width, pivot_second)
    pair_data = []
    for pivot, other in pairs:
        pivot_letter = ("X", "Y")[int((z >> pivot) & 1)]
        other_letter = ("X", "Y")[int((z >> other) & 1)]
        pair_data.append((
            pivot, other, pair_diagonalizer(pivot_letter, other_letter)
        ))
    controls = tuple(pivot for pivot, _other in pairs) + singles
    if reverse_controls:
        controls = tuple(reversed(controls))
    control_mask = sum(1 << control for control in controls)
    exponent = (phase - (x & z).bit_count()) % 4
    row_sign = 1 if exponent == 0 else -1
    effective_angle = row_sign * math.pi / 2
    token = (token_bits[0] << width) | (token_bits[1] << (width + 1))
    maximum = 0.0
    cosine = math.cos(math.pi / 4)
    sine = math.sin(math.pi / 4)
    for source in range(1 << width):
        state = {source | token: 1.0 + 0.0j}
        for pivot, other, unitary in pair_data:
            state = apply_two_sparse(
                state, unitary.conj().T, (pivot, other)
            )
        phased = {}
        for basis, coefficient in state.items():
            accumulated = (basis & control_mask).bit_count() & 1
            rail_left = ((basis >> width) & 1) ^ accumulated
            eigenvalue = 1 if rail_left == 0 else -1
            phased[basis] = coefficient * np.exp(
                0.5j * effective_angle * eigenvalue
            )
        state = phased
        for pivot, other, unitary in reversed(pair_data):
            state = apply_two_sparse(state, unitary, (pivot, other))

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


def dense_accumulator_certificate() -> dict[str, object]:
    controls = 4
    count = controls + 2
    rail_left, rail_right = controls, controls + 1
    theta = math.pi / 2
    phase = np.diag((
        np.exp(0.5j * theta), np.exp(-0.5j * theta)
    )).astype(complex)
    parity = np.diag(tuple(
        (-1) ** state.bit_count() for state in range(1 << count)
    )).astype(complex)
    residuals = []
    prefixes = []
    dirty_residuals = []
    for order in (tuple(range(controls)), tuple(reversed(range(controls)))):
        word = tuple(
            (FREDKIN, (control, rail_left, rail_right)) for control in order
        ) + ((phase, (rail_left,)),) + tuple(
            (FREDKIN, (control, rail_left, rail_right))
            for control in reversed(order)
        )
        total = np.eye(1 << count, dtype=complex)
        prefix = 0.0
        for matrix, wires in word:
            total = embed(matrix, wires, count) @ total
            prefix = max(prefix, float(np.linalg.norm(
                total @ parity - parity @ total
            )))
        prefixes.append(prefix)
        target = np.diag(tuple(
            np.exp(-0.5j * theta * ((-1) ** state.bit_count()))
            for state in range(1 << controls)
        )).astype(complex)
        for token_bits, destination in (((1, 0), residuals), ((0, 1), dirty_residuals)):
            embedding = np.zeros((1 << count, 1 << controls), dtype=complex)
            token = (token_bits[0] << rail_left) | (
                token_bits[1] << rail_right
            )
            for state in range(1 << controls):
                embedding[state | token, state] = 1
            destination.append(float(np.linalg.norm(
                total @ embedding - embedding @ target
            )))
    return {
        "controls": controls,
        "control_orders": 2,
        "maximum_clean_dense_isometry_residual": max(residuals),
        "maximum_dense_cumulative_prefix_parity_residual": max(prefixes),
        "minimum_dirty_opposite_rail_residual": min(dirty_residuals),
    }


def gate_digest(gates: tuple[LocalGate, ...]) -> str:
    digest = sha256()
    for gate in gates:
        digest.update(gate.kind.encode())
        digest.update(repr(gate.sites).encode())
        digest.update(np.round(gate.matrix, 14).tobytes())
    return digest.hexdigest()


def held_seam_certificate(shapes) -> dict[str, object]:
    template_rows: dict[tuple[int, int, int, str], tuple[int, int, int, int]] = {}
    boxes = []
    all_gate_parity = []
    all_gate_radius = []
    all_prefix_failures = 0
    all_label_returns = 0
    all_operand_failures = 0
    deleted_returns = []
    program_digests = []
    maximum_gate_count = 0
    maximum_route_hops = 0
    maximum_support = 0
    maximum_diameter = 0
    primitive_kinds = Counter()
    for shape in shapes:
        fixture = S789.fixture_for(shape)
        placed = U720.placement(fixture)
        all_sites = tuple(placed["all_sites"])
        rows = 0
        box_gates = 0
        box_digest = sha256()
        for edge in range(len(fixture.edges)):
            for row in fixture.physical_terms(edge):
                rows += 1
                lifted = U720.lift_pauli(row, placed)
                support, phase, x, z = local_row(lifted, all_sites)
                letters = pauli_letters(x, z, len(support))
                key = (len(support), phase, x.bit_count(), letters)
                template_rows.setdefault(key, (phase, x, z, len(support)))
                maximum_support = max(maximum_support, len(support))
                maximum_diameter = max(maximum_diameter, max((
                    manhattan(left, right)
                    for left in support for right in support
                ), default=0))
                program = seam_program(
                    support, phase, x, z,
                    pivot_second=False, reverse_controls=False,
                )
                gates = program["gates"]
                macros = program["macros"]
                maximum_gate_count = max(maximum_gate_count, len(gates))
                box_gates += len(gates)
                digest = gate_digest(gates)
                box_digest.update(digest.encode())
                primitive_kinds.update(gate.kind for gate in gates)
                maximum_route_hops = max(
                    maximum_route_hops,
                    max((macro.route_hops for macro in macros), default=0),
                )
                local_failures = []
                prefix_good = True
                for gate in gates:
                    residual = local_parity_residual(gate)
                    all_gate_parity.append(residual)
                    all_gate_radius.append(radius_one(gate))
                    prefix_good = prefix_good and residual < TOL
                    local_failures.append(not prefix_good)
                all_prefix_failures += sum(local_failures)
                all_label_returns += sum(
                    macro.return_failures for macro in macros
                )
                all_operand_failures += sum(
                    macro.operand_failures for macro in macros
                )
                deleted_returns.extend(
                    macro.deleted_return_label_mismatches for macro in macros
                    if macro.route_hops
                )
        program_digests.append(box_digest.hexdigest())
        boxes.append({
            "shape": shape,
            "cells": len(fixture.cells),
            "edges": len(fixture.edges),
            "seam_factors": rows,
            "compiled_local_primitives": box_gates,
            "program_sha256": box_digest.hexdigest(),
        })

    dense_rows = []
    dense_residuals = []
    dirty_residuals = []
    for key, (phase, x, z, width) in sorted(template_rows.items()):
        variants = []
        for pivot_second in (False, True):
            for reverse_controls in (False, True):
                residual = exhaustive_semantic_residual(
                    phase, x, z, width,
                    pivot_second=pivot_second,
                    reverse_controls=reverse_controls,
                )
                variants.append(residual)
                dense_residuals.append(residual)
        dirty = exhaustive_semantic_residual(
            phase, x, z, width,
            pivot_second=False, reverse_controls=False,
            token_bits=(0, 1),
        )
        dirty_residuals.append(dirty)
        dense_rows.append({
            "support": width,
            "phase": phase,
            "x_weight": x.bit_count(),
            "letters": key[3],
            "pivot_and_order_variants": 4,
            "maximum_exhaustive_sparse_column_dense_residual": max(variants),
            "dirty_opposite_rail_residual": dirty,
        })
    return {
        "boxes": boxes,
        "held_shapes": len(boxes),
        "literal_seam_factors": sum(box["seam_factors"] for box in boxes),
        "unique_translated_factor_templates": len(template_rows),
        "template_dense_certificates": dense_rows,
        "maximum_exhaustive_sparse_column_dense_residual": max(dense_residuals),
        "minimum_dirty_opposite_rail_residual": min(dirty_residuals),
        "maximum_elementary_parity_commutator_residual": max(all_gate_parity),
        "cumulative_prefix_parity_failures_by_induction": all_prefix_failures,
        "radius_one_gate_failures": sum(not value for value in all_gate_radius),
        "route_operand_failures": all_operand_failures,
        "route_return_failures": all_label_returns,
        "minimum_deleted_return_label_mismatches": min(deleted_returns),
        "maximum_direct_seam_support_M2": maximum_support,
        "maximum_direct_seam_M2_manhattan_diameter": maximum_diameter,
        "maximum_primitives_per_seam_factor": maximum_gate_count,
        "maximum_route_hops": maximum_route_hops,
        "primitive_kind_census": dict(sorted(primitive_kinds.items())),
        "semantic_multi_site_rotation_primitives": sum(
            count for kind, count in primitive_kinds.items()
            if "semantic" in kind or "multi_site_rotation" in kind
        ),
        "program_family_sha256": sha256(
            "|".join(program_digests).encode()
        ).hexdigest(),
    }


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    pair = controlled_pair_certificate()
    accumulator = dense_accumulator_certificate()
    seams = held_seam_certificate(
        ((2, 1, 1), (3, 1, 1), (3, 2, 2), (5, 3, 2))
    )
    checks = {
        "Cycle821_controlled_pair_has_literal_radius_one_even_compiler": (
            pair["maximum_dense_compiled_residual"] < TOL
            and pair["maximum_dense_cumulative_prefix_parity_residual"] < TOL
            and pair["maximum_elementary_parity_commutator_residual"] < TOL
            and pair["route_operand_failures"] == 0
            and pair["route_return_failures"] == 0
        ),
        "dual_rail_accumulator_is_exact_order_independent_and_parity_even": (
            accumulator["maximum_clean_dense_isometry_residual"] < TOL
            and accumulator[
                "maximum_dense_cumulative_prefix_parity_residual"
            ] < TOL
        ),
        "all_landed_recurrent_seam_factors_compile_without_semantic_rotation": (
            seams["maximum_exhaustive_sparse_column_dense_residual"] < TOL
            and seams["maximum_elementary_parity_commutator_residual"] < TOL
            and seams["cumulative_prefix_parity_failures_by_induction"] == 0
            and seams["radius_one_gate_failures"] == 0
            and seams["route_operand_failures"] == 0
            and seams["route_return_failures"] == 0
            and seams["semantic_multi_site_rotation_primitives"] == 0
            and seams["maximum_direct_seam_support_M2"] <= 17
        ),
        "mutations_are_active": (
            pair["minimum_wrong_SWAP_for_FSWAP_mutation_residual"] > 1.0e-3
            and pair["minimum_deleted_return_label_mismatches"] > 0
            and pair["minimum_deleted_return_dense_residual"] > 1.0e-3
            and seams["minimum_deleted_return_label_mismatches"] > 0
            and accumulator["minimum_dirty_opposite_rail_residual"] > 1.0e-3
            and seams["minimum_dirty_opposite_rail_residual"] > 1.0e-3
        ),
        "held_shapes_and_order_pivot_variants_pass": (
            seams["held_shapes"] == 4
            and seams["unique_translated_factor_templates"] == 7
            and all(
                row["pivot_and_order_variants"] == 4
                and row[
                    "maximum_exhaustive_sparse_column_dense_residual"
                ] < TOL
                for row in seams["template_dense_certificates"]
            )
        ),
    }
    output = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "controlled_pair_compiler": pair,
        "dual_rail_accumulator": accumulator,
        "recurrent_seam_compiler": seams,
        "algorithm": {
            "tensor_route_hop": "chronological FSWAP then CZ, so the state operator is CZ*FSWAP=SWAP; reverse the same factors",
            "controlled_pair": "returned-route pivot beside partner; U_dagger; return; returned-route control beside pivot; CZ; return; returned-route pivot beside partner; U; return",
            "seam_rotation": "pair all X/Y letters; apply returned U_dagger macros; accumulate every pivot and Z singleton into clean |10> token by returned local Fredkins; apply exp(+i sign*pi*Z_left/4); uncompute Fredkins; apply returned U macros",
            "parity": "each elementary factor commutes with product-Z P_ext, hence every cumulative prefix does by induction",
        },
        "supplied": (
            "two clean dual-rail token M2 in |10> for each serialized seam factor; "
            "routing workspace modes; fixed chart, factor order, route program, "
            "and occurrence; the landed Cycle720/789/794/821 registers"
        ),
        "derived": (
            "literal radius-one parity-even elementary words for the Cycle821 "
            "controlled two-target atom and every up-to-17-M2 recurrent seam "
            "rotation, with returned labels and token"
        ),
        "open": (
            "genesis/renewal and autonomous scheduling of token/workspace modes; "
            "a two-body-only decomposition of the allowed radius-one Fredkin; "
            "translation-invariant enforcement and physical time"
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
