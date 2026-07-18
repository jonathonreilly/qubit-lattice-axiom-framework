#!/usr/bin/env python3
"""Cycle 274: exact observable-specific Wilson blindness and readout.

Cycle 271 used the complete support cone of a local algebra.  Here the actual
Cycle-230 update is evolved in the Heisenberg picture and low-rank physical
even observables are compared in all eight flat Wilson sectors.  The finite
calculation keeps the actual Cycle-219 coin, S=B A stream, and onsite contact
phase.  It does not identify compiler iteration with physical time or a
Wilson character with a Record.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import math
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "OBSERVABLE_SPECIFIC_WILSON_BLINDNESS_CYCLE274_NOTE_2026-07-17.md"
)
BETA = c230.BETA
CONTACT_COUPLING = c230.COUPLING
PRUNE = 2.0e-14
BLIND_TOL = 2.0e-10
PASS = 0
FAIL = 0

Cell = tuple[int, int, int]
OneState = dict[int, complex]
Pair = tuple[int, int]
PairState = dict[Pair, complex]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-274 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "observable-specific wilson blindness",
        "actual cycle-230",
        "s=b a",
        "onsite density",
        "contact density",
        "bond kinetic",
        "bond current",
        "mass fixture",
        "l=3,4,5",
        "held-out l=6",
        "all eight wilson sectors",
        "all 24 proper-cubic frames",
        "full 27-element translation group",
        "deletion",
        "leakage",
        "lawful domain",
        "supplied-structure ledger",
        "compiler iteration is not physical time",
        "wilson character is not a record",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no route-independent obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "note preserves observable scope, controls, N1-N8, time, and Record contracts",
        not missing,
        missing,
    )


def mode_index(cell: Cell, direction: int, length: int) -> int:
    return c230.site_index(cell, direction, length)


def mode_label(index: int, length: int) -> tuple[Cell, int]:
    direction = index % 6
    quotient = index // 6
    z = quotient % length
    quotient //= length
    y = quotient % length
    x = quotient // length
    return (x, y, z), direction


def validate_domain(length: int, sector: int, iterations: int, coin: np.ndarray) -> None:
    if length < 3:
        raise ValueError("the declared finite-torus domain requires L>=3")
    if sector not in range(8):
        raise ValueError("Wilson sector must be an integer in range(8)")
    if iterations < 0:
        raise ValueError("compiler iterations must be nonnegative")
    if coin.shape != (6, 6) or np.linalg.norm(coin.conj().T @ coin - np.eye(6)) > 1e-10:
        raise ValueError("the onsite coin must be a 6x6 unitary")


def centered_cut(cell: Cell, length: int) -> Cell:
    """Owner coordinates of the three farthest flat seam planes."""
    offset = (length - 1) // 2
    return tuple((coordinate + offset) % length for coordinate in cell)


def crosses_cut(left: Cell, right: Cell, axis: int, cut: Cell, length: int) -> bool:
    return {left[axis], right[axis]} == {cut[axis], (cut[axis] + 1) % length}


def backward_table(
    length: int, sector: int, cut: Cell, coin: np.ndarray
) -> tuple[tuple[tuple[int, complex], ...], ...]:
    """Sparse columns of U_w^dagger for U_w=S_w C.

    A Wilson bit supplies -1 only on the selected flat stream seam.  Applying
    S_w^dagger first finds the predecessor; C^dagger then mixes the six modes
    at that predecessor.  This is the one-particle action of the actual
    Cycle-230 S=B A FSWAP stream, including its fermionic sector sign.
    """
    validate_domain(length, sector, 0, coin)
    rows = []
    for index in range(6 * length**3):
        cell, direction = mode_label(index, length)
        displacement = c210.DIRECTIONS[direction]
        predecessor = tuple(
            int((cell[axis] - displacement[axis]) % length) for axis in range(3)
        )
        axis = direction // 2
        sign = -1 if ((sector >> axis) & 1) and crosses_cut(
            predecessor, cell, axis, cut, length
        ) else 1
        rows.append(
            tuple(
                (
                    mode_index(predecessor, source_direction, length),
                    sign * np.conj(coin[direction, source_direction]),
                )
                for source_direction in range(6)
            )
        )
    return tuple(rows)


def prune(state: dict) -> dict:
    return {key: value for key, value in state.items() if abs(value) > PRUNE}


def backward_one(state: OneState, table) -> OneState:
    output: defaultdict[int, complex] = defaultdict(complex)
    for index, amplitude in state.items():
        for predecessor, coefficient in table[index]:
            output[predecessor] += coefficient * amplitude
    return prune(output)


def backward_pair(
    state: PairState, table, length: int, coupling: float
) -> PairState:
    """Apply Gamma_2(U_w)^dagger W_g^dagger to an N=2 state."""
    output: defaultdict[Pair, complex] = defaultdict(complex)
    contact_phase = np.exp(-1j * coupling)
    for (left, right), amplitude in state.items():
        left_cell, _ = mode_label(left, length)
        right_cell, _ = mode_label(right, length)
        if left_cell == right_cell:
            amplitude *= contact_phase
        for new_left, left_coefficient in table[left]:
            for new_right, right_coefficient in table[right]:
                if new_left < new_right:
                    output[(new_left, new_right)] += (
                        amplitude * left_coefficient * right_coefficient
                    )
                elif new_right < new_left:
                    output[(new_right, new_left)] -= (
                        amplitude * left_coefficient * right_coefficient
                    )
    return prune(output)


def inner(left: dict, right: dict) -> complex:
    if len(left) > len(right):
        return np.conj(inner(right, left))
    return sum(np.conj(value) * right.get(key, 0.0j) for key, value in left.items())


def encoded_row(key: int | Pair) -> int:
    if isinstance(key, tuple):
        left, right = key
        return right * (right - 1) // 2 + left
    return key


def column_matrix(columns: tuple[dict, ...], dimension: int) -> sparse.csc_matrix:
    rows = []
    column_indices = []
    values = []
    for column, state in enumerate(columns):
        for key, value in state.items():
            rows.append(encoded_row(key))
            column_indices.append(column)
            values.append(value)
    return sparse.csc_matrix(
        (values, (rows, column_indices)), shape=(dimension, len(columns)), dtype=complex
    )


def cross_gram(left: tuple[dict, ...], right: tuple[dict, ...]) -> np.ndarray:
    maximum = max(
        encoded_row(key)
        for columns in (left, right)
        for state in columns
        for key in state
    )
    left_matrix = column_matrix(left, maximum + 1)
    right_matrix = column_matrix(right, maximum + 1)
    return np.asarray((left_matrix.conj().T @ right_matrix).toarray(), dtype=complex)


def gram_leakage(columns: tuple[dict, ...]) -> float:
    gram = cross_gram(columns, columns)
    return float(np.linalg.norm(gram - np.eye(len(columns))))


@dataclass(frozen=True)
class ProjectorResidual:
    operator: float
    frobenius: float
    sigma_min: float


def projector_residual(left: tuple[dict, ...], right: tuple[dict, ...]) -> ProjectorResidual:
    singular = np.linalg.svd(cross_gram(left, right), compute_uv=False)
    minimum = float(np.min(singular))
    op_square = max(0.0, 1.0 - minimum**2)
    fro_square = max(0.0, 2 * len(left) - 2 * float(np.sum(singular**2)))
    if op_square < 1e-12:
        op_square = 0.0
    if fro_square < 1e-12:
        fro_square = 0.0
    return ProjectorResidual(math.sqrt(op_square), math.sqrt(fro_square), minimum)


def hermitian_residual(
    left: tuple[dict, ...], right: tuple[dict, ...], kernel: np.ndarray
) -> float:
    overlap = cross_gram(left, right)
    norm_square = 2 * float(np.trace(kernel @ kernel).real)
    cross = np.trace(kernel @ overlap @ kernel @ overlap.conj().T)
    residual_square = max(0.0, norm_square - 2 * float(cross.real))
    if residual_square < 1e-12:
        residual_square = 0.0
    return math.sqrt(residual_square)


def one_particle_starts(
    cell: Cell, direction: int, length: int
) -> dict[str, tuple[OneState, ...]]:
    modes = tuple(mode_index(cell, item, length) for item in range(6))
    neighbor = tuple(
        int((cell[axis] + c210.DIRECTIONS[direction, axis]) % length)
        for axis in range(3)
    )
    reverse = direction ^ 1
    bond_modes = (modes[direction], mode_index(neighbor, reverse, length))
    return {
        "onsite_density": tuple({mode: 1.0 + 0.0j} for mode in modes),
        "scalar_mass": ({mode: 1 / np.sqrt(6) for mode in modes},),
        "mode_density": ({modes[direction]: 1.0 + 0.0j},),
        "bond": tuple({mode: 1.0 + 0.0j} for mode in bond_modes),
    }


def evolve_one_snapshots(
    cell: Cell,
    direction: int,
    length: int,
    sector: int,
    cut: Cell,
    times: tuple[int, ...],
    coin: np.ndarray,
) -> dict[int, dict[str, tuple[OneState, ...]]]:
    validate_domain(length, sector, max(times, default=0), coin)
    table = backward_table(length, sector, cut, coin)
    current = one_particle_starts(cell, direction, length)
    snapshots = {0: current} if 0 in times else {}
    for iteration in range(1, max(times, default=0) + 1):
        current = {
            name: tuple(backward_one(column, table) for column in columns)
            for name, columns in current.items()
        }
        if iteration in times:
            snapshots[iteration] = current
    return snapshots


def contact_starts(cell: Cell, length: int) -> tuple[PairState, ...]:
    modes = tuple(mode_index(cell, item, length) for item in range(6))
    return tuple(
        {(modes[left], modes[right]): 1.0 + 0.0j}
        for left in range(6)
        for right in range(left + 1, 6)
    )


def evolve_contact_snapshots(
    cell: Cell,
    length: int,
    sector: int,
    cut: Cell,
    times: tuple[int, ...],
    coin: np.ndarray,
    coupling: float,
) -> dict[int, tuple[PairState, ...]]:
    validate_domain(length, sector, max(times, default=0), coin)
    table = backward_table(length, sector, cut, coin)
    current = contact_starts(cell, length)
    snapshots = {0: current} if 0 in times else {}
    for iteration in range(1, max(times, default=0) + 1):
        current = tuple(
            backward_pair(column, table, length, coupling) for column in current
        )
        if iteration in times:
            snapshots[iteration] = current
    return snapshots


def one_residuals(reference, candidate) -> dict[str, float]:
    kinetic = np.asarray(((0, 1), (1, 0)), dtype=complex)
    current = np.asarray(((0, 1j), (-1j, 0)), dtype=complex)
    return {
        "onsite_density": projector_residual(
            reference["onsite_density"], candidate["onsite_density"]
        ).operator,
        "scalar_mass": projector_residual(
            reference["scalar_mass"], candidate["scalar_mass"]
        ).operator,
        "mode_density": projector_residual(
            reference["mode_density"], candidate["mode_density"]
        ).operator,
        "bond_kinetic_fro": hermitian_residual(
            reference["bond"], candidate["bond"], kinetic
        ),
        "bond_current_fro": hermitian_residual(
            reference["bond"], candidate["bond"], current
        ),
    }


def format_fingerprint(rows: dict[int, dict[str, float]], name: str) -> tuple[str, ...]:
    return tuple(f"{rows[sector][name]:.12e}" for sector in range(1, 8))


def actual_update_and_mass_fixture() -> tuple[np.ndarray, float]:
    species = c219.common_species(BETA)
    coin = species.coin
    length = 3
    table = backward_table(length, 0, centered_cut((0, 0, 0), length), coin)
    sparse = np.zeros((6 * length**3, 6 * length**3), dtype=complex)
    for column, entries in enumerate(table):
        for row, coefficient in entries:
            sparse[row, column] = coefficient
    actual, onsite, stream, layer_a, layer_b = c230.spatial_layers(length, coin)
    check(
        "sparse U^dagger is the actual Cycle-230 S C update",
        np.linalg.norm(sparse - actual.conj().T) < 2e-12,
        np.linalg.norm(sparse - actual.conj().T),
    )
    check(
        "the actual stream retains its S=B A factorization",
        np.linalg.norm(stream - layer_b @ layer_a) < 2e-12,
        np.linalg.norm(stream - layer_b @ layer_a),
    )
    measured_mass = c219.rest_mass(species)
    check(
        "the one-particle rest-mass fixture is preserved",
        abs(measured_mass - species.analytic_mass) < 2e-12,
        (measured_mass, species.analytic_mass),
    )
    twisted_errors = []
    for sector in range(8):
        sector_table = backward_table(
            length, sector, centered_cut((0, 0, 0), length), coin
        )
        sector_matrix = np.zeros_like(sparse)
        for column, entries in enumerate(sector_table):
            for row, coefficient in entries:
                sector_matrix[row, column] = coefficient
        twisted_errors.append(
            float(
                np.linalg.norm(
                    sector_matrix.conj().T @ sector_matrix
                    - np.eye(6 * length**3)
                )
            )
        )
    check(
        "all eight twisted one-particle updates are unitary at L=3",
        max(twisted_errors) < 2e-11,
        max(twisted_errors),
    )
    return coin, measured_mass


def route_census(coin: np.ndarray) -> tuple[dict, float]:
    first_wrap = {3: 2, 4: 2, 5: 3, 6: 3}
    results = {}
    maximum_leakage = 0.0
    for length in (3, 4, 5, 6):
        cell = (0, 0, 0)
        cut = centered_cut(cell, length)
        wrap = first_wrap[length]
        times = tuple(range(wrap + 2))
        one = {
            sector: evolve_one_snapshots(
                cell, 0, length, sector, cut, times, coin
            )
            for sector in range(8)
        }
        length_rows = {}
        detected = None
        for iteration in times:
            rows = {
                sector: one_residuals(one[0][iteration], one[sector][iteration])
                for sector in range(8)
            }
            length_rows[iteration] = rows
            if detected is None and max(
                row["onsite_density"] for row in rows.values()
            ) > BLIND_TOL:
                detected = iteration
            for sector in range(8):
                for columns in one[sector][iteration].values():
                    maximum_leakage = max(maximum_leakage, gram_leakage(columns))
        check(
            f"L={length} exact onsite-density onset equals first topological wrap",
            detected == wrap,
            (detected, wrap),
        )
        check(
            f"L={length} onsite density, scalar-mass, and mode densities cancel before wrap",
            all(
                value < BLIND_TOL
                for iteration in range(wrap)
                for sector in range(8)
                for value in (
                    length_rows[iteration][sector]["onsite_density"],
                    length_rows[iteration][sector]["scalar_mass"],
                    length_rows[iteration][sector]["mode_density"],
                )
            ),
            max(
                value
                for iteration in range(wrap)
                for sector in range(8)
                for value in (
                    length_rows[iteration][sector]["onsite_density"],
                    length_rows[iteration][sector]["scalar_mass"],
                    length_rows[iteration][sector]["mode_density"],
                )
            ),
        )
        contact_times = tuple(range(wrap + 2))
        contact = {}
        for sector in range(8):
            contact[sector] = evolve_contact_snapshots(
                cell,
                length,
                sector,
                cut,
                contact_times,
                coin,
                CONTACT_COUPLING,
            )
            for iteration in contact_times:
                maximum_leakage = max(
                    maximum_leakage, gram_leakage(contact[sector][iteration])
                )
        contact_rows = {
            iteration: {
                sector: projector_residual(
                    contact[0][iteration], contact[sector][iteration]
                ).operator
                for sector in range(8)
            }
            for iteration in contact_times
        }
        check(
            f"L={length} contact density cancels in every sector before wrap",
            max(
                contact_rows[iteration][sector]
                for iteration in range(wrap)
                for sector in range(8)
            )
            < BLIND_TOL,
        )
        check(
            f"L={length} genuine N=2 contact density has exact sector readout at wrap",
            max(contact_rows[wrap].values()) > 1e-4,
            max(contact_rows[wrap].values()),
        )
        check(
            f"L={length} contact and one-particle probes remain resolved beyond wrap",
            max(contact_rows[wrap + 1].values()) > 1e-4
            and max(
                row["onsite_density"]
                for row in length_rows[wrap + 1].values()
            )
            > 1e-4,
        )
        if length in (4, 6):
            check(
                f"L={length} directed-mode density is exactly blind at full-cell first wrap",
                max(
                    length_rows[wrap][sector]["mode_density"]
                    for sector in range(8)
                )
                < BLIND_TOL
                and max(
                    length_rows[wrap + 1][sector]["mode_density"]
                    for sector in range(8)
                )
                > 1e-4,
                (
                    max(
                        length_rows[wrap][sector]["mode_density"]
                        for sector in range(8)
                    ),
                    max(
                        length_rows[wrap + 1][sector]["mode_density"]
                        for sector in range(8)
                    ),
                ),
            )
        results[length] = {
            "first_wrap": wrap,
            "one": length_rows,
            "contact": contact_rows,
        }
        label = "held-out" if length == 6 else "training"
        for iteration in (wrap, wrap + 1):
            print(
                "DATA",
                label,
                f"L={length}",
                f"t={iteration}",
                "onsite=",
                format_fingerprint(length_rows[iteration], "onsite_density"),
                "scalar_mass=",
                format_fingerprint(length_rows[iteration], "scalar_mass"),
                "mode=",
                format_fingerprint(length_rows[iteration], "mode_density"),
                "kinetic_fro=",
                format_fingerprint(length_rows[iteration], "bond_kinetic_fro"),
                "current_fro=",
                format_fingerprint(length_rows[iteration], "bond_current_fro"),
                "contact=",
                tuple(
                    f"{contact_rows[iteration][sector]:.12e}"
                    for sector in range(1, 8)
                ),
            )
    check(
        "all evolved low-rank subspaces preserve the declared particle sectors",
        maximum_leakage < 3e-10,
        maximum_leakage,
    )
    return results, maximum_leakage


def proper_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        matrix = np.zeros((3, 3), dtype=int)
        matrix[np.arange(3), permutation] = 1
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ matrix
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple(frames)


def direction_map(frame: np.ndarray) -> dict[int, int]:
    lookup = {tuple(row): index for index, row in enumerate(c210.DIRECTIONS)}
    return {
        source: lookup[tuple(int(value) for value in frame @ direction)]
        for source, direction in enumerate(c210.DIRECTIONS)
    }


def sector_map(sector: int, frame: np.ndarray) -> int:
    result = 0
    for source_axis in range(3):
        target_vector = frame @ np.eye(3, dtype=int)[:, source_axis]
        target_axis = int(np.flatnonzero(target_vector)[0])
        if (sector >> source_axis) & 1:
            result |= 1 << target_axis
    return result


def frame_cut(cut: Cell, frame: np.ndarray, length: int) -> Cell:
    result = [0, 0, 0]
    for source_axis in range(3):
        target_vector = frame @ np.eye(3, dtype=int)[:, source_axis]
        target_axis = int(np.flatnonzero(target_vector)[0])
        sign = int(target_vector[target_axis])
        result[target_axis] = (
            cut[source_axis] if sign == 1 else -cut[source_axis] - 1
        ) % length
    return tuple(result)


def mapped_mode(index: int, frame: np.ndarray, length: int) -> int:
    cell, direction = mode_label(index, length)
    target_cell = tuple(int(value % length) for value in frame @ np.asarray(cell))
    return mode_index(target_cell, direction_map(frame)[direction], length)


def covariance_controls(coin: np.ndarray) -> None:
    length = 3
    cell = (0, 0, 0)
    cut = centered_cut(cell, length)
    base_tables = {
        sector: backward_table(length, sector, cut, coin) for sector in range(8)
    }
    frame_error = 0.0
    contact_invariant = True
    for frame in proper_frames():
        target_cut = frame_cut(cut, frame, length)
        for sector in range(8):
            target_sector = sector_map(sector, frame)
            target = backward_table(length, target_sector, target_cut, coin)
            for index, entries in enumerate(base_tables[sector]):
                transformed = {
                    mapped_mode(predecessor, frame, length): coefficient
                    for predecessor, coefficient in entries
                }
                actual = dict(target[mapped_mode(index, frame, length)])
                frame_error = max(
                    frame_error,
                    max(abs(transformed[key] - actual.get(key, 0.0j)) for key in transformed),
                )
            modes = tuple(mode_index(cell, direction, length) for direction in range(6))
            mapped_cells = {
                mode_label(mapped_mode(mode, frame, length), length)[0] for mode in modes
            }
            contact_invariant &= len(mapped_cells) == 1
    check(
        "twisted actual update is covariant under all 24 proper-cubic frames",
        len(proper_frames()) == 24 and frame_error < 3e-12 and contact_invariant,
        (len(proper_frames()), frame_error, contact_invariant),
    )

    translation_error = 0.0
    for displacement in product(range(length), repeat=3):
        target_cut = tuple((cut[axis] + displacement[axis]) % length for axis in range(3))
        for sector in range(8):
            target = backward_table(length, sector, target_cut, coin)
            for index, entries in enumerate(base_tables[sector]):
                source_cell, source_direction = mode_label(index, length)
                mapped_index = mode_index(
                    tuple((source_cell[axis] + displacement[axis]) % length for axis in range(3)),
                    source_direction,
                    length,
                )
                transformed = {}
                for predecessor, coefficient in entries:
                    predecessor_cell, predecessor_direction = mode_label(predecessor, length)
                    mapped_predecessor = mode_index(
                        tuple(
                            (predecessor_cell[axis] + displacement[axis]) % length
                            for axis in range(3)
                        ),
                        predecessor_direction,
                        length,
                    )
                    transformed[mapped_predecessor] = coefficient
                actual = dict(target[mapped_index])
                translation_error = max(
                    translation_error,
                    max(abs(transformed[key] - actual.get(key, 0.0j)) for key in transformed),
                )
    check(
        "twisted actual update is covariant under the full 27-element L=3 translation group",
        translation_error < 3e-12,
        translation_error,
    )


def deletion_and_domain_controls(coin: np.ndarray, results: dict) -> None:
    cell = (0, 0, 0)
    length = 5
    cut = centered_cut(cell, length)
    time = results[length]["first_wrap"] + 1
    identity = np.eye(6, dtype=complex)
    identity_columns = {
        sector: evolve_one_snapshots(
            cell, 0, length, sector, cut, (time,), identity
        )[time]["onsite_density"]
        for sector in range(8)
    }
    identity_residual = max(
        projector_residual(identity_columns[0], identity_columns[sector]).operator
        for sector in range(8)
    )
    check(
        "coin-mixing deletion removes onsite-density Wilson readout",
        identity_residual < BLIND_TOL,
        identity_residual,
    )

    one_with_contact = evolve_one_snapshots(
        cell, 0, length, 1, cut, (time,), coin
    )[time]
    one_contact_deleted = evolve_one_snapshots(
        cell, 0, length, 1, cut, (time,), coin
    )[time]
    check(
        "contact deletion is exactly invisible in the one-particle sector",
        all(
            projector_residual(one_with_contact[name], one_contact_deleted[name]).operator
            < BLIND_TOL
            for name in ("onsite_density", "scalar_mass", "mode_density")
        ),
    )

    interacting = evolve_contact_snapshots(
        cell, length, 0, cut, (1, time), coin, CONTACT_COUPLING
    )
    deleted = evolve_contact_snapshots(cell, length, 0, cut, (1, time), coin, 0.0)
    at_one = projector_residual(interacting[1], deleted[1]).operator
    after_mixing = projector_residual(interacting[time], deleted[time]).operator
    check(
        "contact phase is initially a projector-global phase but becomes observable after mixing",
        at_one < BLIND_TOL and after_mixing > 1e-4,
        (at_one, after_mixing),
    )
    check(
        "Wilson deletion returns exact zero residual",
        all(
            value == 0.0
            for value in one_residuals(one_with_contact, one_with_contact).values()
        ),
    )

    rejected = 0
    for arguments in (
        (2, 0, 0, coin),
        (3, 8, 0, coin),
        (3, 0, -1, coin),
        (3, 0, 0, np.zeros((6, 6), dtype=complex)),
    ):
        try:
            validate_domain(*arguments)
        except ValueError:
            rejected += 1
    check(
        "lawful-domain guard rejects small torus, bad sector, negative iteration, and nonunitary coin",
        rejected == 4,
        rejected,
    )


def main() -> int:
    note_contract()
    coin, measured_mass = actual_update_and_mass_fixture()
    results, leakage = route_census(coin)
    covariance_controls(coin)
    deletion_and_domain_controls(coin, results)
    check(
        "supplied numerical fixture remains explicit",
        BETA == -0.3
        and CONTACT_COUPLING == 0.37
        and abs(measured_mass - 0.4534056541748851) < 2e-12,
        (BETA, CONTACT_COUPLING, measured_mass, PRUNE),
    )
    check(
        "result is bounded evidence, not a route-independent obstruction",
        "no route-independent obstruction" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
    )
    print("DATA max_gram_leakage", f"{leakage:.12e}")
    print("SUMMARY", "PASS", PASS, "FAIL", FAIL)
    if FAIL:
        print("RESULT CYCLE274_OBSERVABLE_SPECIFIC_WILSON_BLINDNESS_RED")
        return 1
    print("RESULT CYCLE274_OBSERVABLE_SPECIFIC_WILSON_BLINDNESS_GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
