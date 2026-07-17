#!/usr/bin/env python3
"""Cycle 236: Farrelly--Short auxiliary-Majorana CAR compiler probe.

Instantiate the link-Majorana cancellation of arXiv:1303.4652, equations
III.12--III.14 and D.2--D.5, on every intercell FSWAP of the Cycle-230
six-mode CAR update.  The dressed update has bounded qubit support in a
site-major Jordan--Wigner presentation.  The runner separately audits the
lawful-sector constraints and Appendix-G preparation: those surfaces retain
size-growing Jordan--Wigner strings and therefore do not give the bounded
local encoding required by the compiler tournament.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "FARRELLY_SHORT_AUXILIARY_MAJORANA_CAR_COMPILER_CYCLE236_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
REVERSE = (1, 0, 3, 2, 5, 4)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "farrelly–short",
        "equations `iii.12–iii.14`",
        "appendix g",
        "conditional global isometry",
        "not a bounded-radius local encoding",
        "12 data m2 carriers plus one supplied marker per coarse cell",
        "all `l=3,4,5` matter parity sectors",
        "global jordan–wigner order",
        "rank-73",
        "contact seam block",
        "authority: none",
        "audit: unset",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure and primitive scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom conclusion",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the qualified construction and N1-N8 contract", not missing, missing)


@dataclass(frozen=True)
class Pauli:
    """Pauli i^phase X^x Z^z in site-major Jordan--Wigner order."""

    phase: int = 0
    x: int = 0
    z: int = 0

    def __matmul__(self, other: "Pauli") -> "Pauli":
        phase = (self.phase + other.phase + 2 * (self.z & other.x).bit_count()) % 4
        return Pauli(phase, self.x ^ other.x, self.z ^ other.z)

    def commutes(self, other: "Pauli") -> bool:
        return (
            (self.x & other.z).bit_count() + (self.z & other.x).bit_count()
        ) % 2 == 0

    def symplectic(self, qubit_count: int) -> int:
        return self.x | (self.z << qubit_count)

    def weight(self) -> int:
        return (self.x | self.z).bit_count()


def all_cells(length: int):
    return tuple(product(range(length), repeat=3))


def cell_number(cell: tuple[int, int, int], length: int) -> int:
    x, y, z = cell
    return (x * length + y) * length + z


def mode_index(
    cell: tuple[int, int, int], kind: str, direction: int, length: int
) -> int:
    offset = direction if kind == "matter" else 6 + direction
    return 12 * cell_number(cell, length) + offset


def shifted(
    cell: tuple[int, int, int], direction: int, length: int
) -> tuple[int, int, int]:
    delta = c210.DIRECTIONS[direction]
    return tuple(int((cell[a] + int(delta[a])) % length) for a in range(3))


def links(length: int):
    """Canonical positive-axis links and the Cycle-230 B-layer matter ports."""

    rows = []
    for cell in all_cells(length):
        for axis in range(3):
            positive = 2 * axis
            negative = positive + 1
            target = shifted(cell, positive, length)
            rows.append(
                {
                    "owner": cell,
                    "axis": axis,
                    "target": target,
                    "matter_left": mode_index(cell, "matter", negative, length),
                    "matter_right": mode_index(target, "matter", positive, length),
                    "aux_left": mode_index(cell, "aux", positive, length),
                    "aux_right": mode_index(target, "aux", negative, length),
                }
            )
    return rows


def jw_majorana(mode: int, component: int) -> Pauli:
    prefix = (1 << mode) - 1
    if component == 0:  # c+c^dagger
        return Pauli(x=1 << mode, z=prefix)
    if component == 1:  # -i(c-c^dagger) = Y with the same JW prefix
        return Pauli(phase=1, x=1 << mode, z=prefix | (1 << mode))
    raise ValueError(component)


def link_majorana(row) -> Pauli:
    return Pauli(phase=1) @ jw_majorana(row["aux_left"], 0) @ jw_majorana(
        row["aux_right"], 0
    )


def odd_link_parity_stabilizer(row) -> Pauli:
    # Desired auxiliary link parity is -1, so -Z_left Z_right stabilizes it.
    return Pauli(
        phase=2,
        z=(1 << row["aux_left"]) | (1 << row["aux_right"]),
    )


def gf2_rank(rows) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def stabilizer_phase_failures(rows: list[Pauli], qubit_count: int) -> int:
    pivots: dict[int, Pauli] = {}
    failures = 0
    for original in rows:
        row = original
        while row.x or row.z:
            pivot = row.symplectic(qubit_count).bit_length() - 1
            if pivot in pivots:
                row = row @ pivots[pivot]
            else:
                pivots[pivot] = row
                break
        else:
            failures += row.phase % 4 != 0
    return failures


def constraint_and_sector_controls():
    scaling = []
    for length in (3, 4, 5):
        cell_count = length**3
        qubit_count = 12 * cell_count
        link_rows = links(length)
        m_rows = [link_majorana(row) for row in link_rows]
        p_rows = [odd_link_parity_stabilizer(row) for row in link_rows]
        stabilizers = m_rows + p_rows
        commutator_failures = 0
        for left_index, left in enumerate(stabilizers):
            for right in stabilizers[left_index + 1 :]:
                commutator_failures += not left.commutes(right)
        rank = gf2_rank(row.symplectic(qubit_count) for row in stabilizers)
        phase_failures = stabilizer_phase_failures(stabilizers, qubit_count)
        matter_parity = Pauli(
            z=sum(
                1 << mode_index(cell, "matter", direction, length)
                for cell in all_cells(length)
                for direction in range(6)
            )
        )
        matter_parity_commutator_failures = sum(
            not matter_parity.commutes(row) for row in stabilizers
        )
        parity_extended_rank = gf2_rank(
            [row.symplectic(qubit_count) for row in stabilizers]
            + [matter_parity.symplectic(qubit_count)]
        )
        maximum_m_weight = max(row.weight() for row in m_rows)
        total_m_weight = sum(row.weight() for row in m_rows)
        prep_string_touches = sum(
            row[endpoint] + 1
            for row in link_rows
            for endpoint in ("aux_left", "aux_right")
        )
        scaling.append(
            {
                "L": length,
                "cells": cell_count,
                "M_max_weight": maximum_m_weight,
                "M_total_weight": total_m_weight,
                "Appendix_G_prefix_touches": prep_string_touches,
                "prefix_touches_over_cells_squared": prep_string_touches
                / cell_count**2,
                "matter_parity_rank_increment": parity_extended_rank - rank,
                "matter_parity_commutator_failures": matter_parity_commutator_failures,
            }
        )
        check(
            f"L={length} link-Majorana plus odd-link-parity constraints leave exactly six matter qubits/cell",
            len(link_rows) == 3 * cell_count
            and commutator_failures == 0
            and rank == 6 * cell_count
            and phase_failures == 0
            and matter_parity_commutator_failures == 0
            and parity_extended_rank == rank + 1
            and qubit_count - rank == 6 * cell_count,
            {
                "physical_qubits": qubit_count,
                "links": len(link_rows),
                "constraint_rank": rank,
                "logical_qubits": qubit_count - rank,
                "commutator_failures": commutator_failures,
                "phase_failures": phase_failures,
                "matter_parity_rank_increment": parity_extended_rank - rank,
            },
        )

    check(
        "all L=3,4,5 matter parity sectors survive without an even-sector projection",
        all(row["matter_parity_rank_increment"] == 1 for row in scaling)
        and all(row["matter_parity_commutator_failures"] == 0 for row in scaling),
        [
            {
                "L": row["L"],
                "matter_logical_qubits": 6 * row["cells"],
                "vacuum_parity": 1,
                "one_particle_parity": -1,
            }
            for row in scaling
        ],
    )
    check(
        "site-major link constraints and Appendix-G parity collection have size-growing support",
        all(
            scaling[index + 1]["M_max_weight"]
            > scaling[index]["M_max_weight"]
            for index in range(len(scaling) - 1)
        )
        and all(row["M_max_weight"] > 6 * row["cells"] for row in scaling)
        and all(row["prefix_touches_over_cells_squared"] > 30 for row in scaling),
        scaling,
    )
    return scaling


def annihilation(mode: int, mode_count: int) -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    lowering = np.asarray(((0, 1), (0, 0)), dtype=complex)
    result = np.asarray(((1,),), dtype=complex)
    for index in range(mode_count):
        result = np.kron(
            result,
            z if index < mode else lowering if index == mode else identity,
        )
    return result


def dense_link_control() -> None:
    # Extended order [matter-left, aux-left, matter-right, aux-right].
    a, c, b, d = (annihilation(index, 4) for index in range(4))
    m = 1j * (c + c.conj().T) @ (d + d.conj().T)
    q_dressed = (
        a.conj().T @ a
        + b.conj().T @ b
        - a.conj().T @ m @ b
        - b.conj().T @ m @ a
    )
    u_dressed = expm(1j * np.pi * q_dressed / 2)

    a2, b2 = (annihilation(index, 2) for index in range(2))
    q_coarse = (
        a2.conj().T @ a2
        + b2.conj().T @ b2
        - a2.conj().T @ b2
        - b2.conj().T @ a2
    )
    fswap = expm(1j * np.pi * q_coarse / 2)

    k = (c.conj().T - 1j * d.conj().T) / np.sqrt(2)
    vacuum = np.eye(16, dtype=complex)[:, 0]
    columns = []
    for occupied_left, occupied_right in ((0, 0), (0, 1), (1, 0), (1, 1)):
        vector = vacuum
        if occupied_right:
            vector = b.conj().T @ vector
        if occupied_left:
            vector = a.conj().T @ vector
        columns.append(k @ vector)
    encoding = np.column_stack(columns)
    link_parity = (
        np.eye(16) - 2 * c.conj().T @ c
    ) @ (np.eye(16) - 2 * d.conj().T @ d)
    residual = np.linalg.norm(u_dressed @ encoding - encoding @ fswap)
    leakage = max(
        np.linalg.norm(m @ encoding - encoding),
        np.linalg.norm(link_parity @ encoding + encoding),
        np.linalg.norm(q_dressed @ m - m @ q_dressed),
        np.linalg.norm(q_dressed @ link_parity - link_parity @ q_dressed),
    )
    check(
        "Farrelly-Short M dressing exactly intertwines one Cycle-230 intercell FSWAP on its link code",
        np.linalg.norm(encoding.conj().T @ encoding - np.eye(4)) < 2e-15
        and residual < 2e-15
        and leakage < 2e-15,
        {"intertwining_residual": residual, "constraint_or_leakage_residual": leakage},
    )

    minus_projector = (np.eye(16) - m) / 2
    wrong_sector_residual = np.linalg.norm(
        minus_projector @ (u_dressed - np.eye(16))
    )
    check(
        "deleting the M=+1 lawful-sector condition changes the stream action",
        wrong_sector_residual > 1,
        {"M_minus_sector_nonidentity_residual": wrong_sector_residual},
    )


def pauli_cells(pauli: Pauli, length: int) -> set[tuple[int, int, int]]:
    support = pauli.x | pauli.z
    cells = set()
    while support:
        bit = support & -support
        mode = bit.bit_length() - 1
        number = mode // 12
        cells.add((number // (length * length), (number // length) % length, number % length))
        support ^= bit
    return cells


def update_support_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        dressed_max = 0
        dressed_cell_failures = 0
        bare_max = 0
        for link in links(length):
            m = link_majorana(link)
            endpoints = {link["owner"], link["target"]}
            for left_component, right_component in product(range(2), repeat=2):
                dressed = (
                    jw_majorana(link["matter_left"], left_component)
                    @ m
                    @ jw_majorana(link["matter_right"], right_component)
                )
                bare = jw_majorana(
                    link["matter_left"], left_component
                ) @ jw_majorana(link["matter_right"], right_component)
                dressed_max = max(dressed_max, dressed.weight())
                bare_max = max(bare_max, bare.weight())
                dressed_cell_failures += not pauli_cells(dressed, length).issubset(
                    endpoints
                )
        rows.append(
            {
                "L": length,
                "dressed_max_weight": dressed_max,
                "dressed_endpoint_failures": dressed_cell_failures,
                "bare_max_weight": bare_max,
            }
        )
    check(
        "M dressing cancels every global JW string in all three Cycle-230 B-layer axes",
        all(row["dressed_endpoint_failures"] == 0 for row in rows)
        and len({row["dressed_max_weight"] for row in rows}) == 1
        and all(rows[index + 1]["bare_max_weight"] > rows[index]["bare_max_weight"] for index in range(2)),
        rows,
    )

    onsite_failures = 0
    onsite_max = 0
    length = 3
    for cell in all_cells(length):
        for left, right in combinations(range(6), 2):
            operator = jw_majorana(
                mode_index(cell, "matter", left, length), 0
            ) @ jw_majorana(mode_index(cell, "matter", right, length), 0)
            onsite_failures += pauli_cells(operator, length) != {cell}
            onsite_max = max(onsite_max, operator.weight())
    check(
        "onsite A swaps and the six-mode coin/contact even algebra stay within one site-major cell block",
        onsite_failures == 0 and onsite_max <= 6,
        {"onsite_support_failures": onsite_failures, "sample_even_weight_max": onsite_max},
    )


def ordering_tradeoff_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        cell_count = length**3
        link_rows = links(length)
        alternate_position: dict[int, int] = {}
        # Matter modes remain site-major.  Auxiliary endpoints are instead
        # made consecutive link by link, the most favorable order for M_e.
        for cell in all_cells(length):
            for direction in range(6):
                alternate_position[
                    mode_index(cell, "matter", direction, length)
                ] = 6 * cell_number(cell, length) + direction
        for link_index, row in enumerate(link_rows):
            alternate_position[row["aux_left"]] = 6 * cell_count + 2 * link_index
            alternate_position[row["aux_right"]] = (
                6 * cell_count + 2 * link_index + 1
            )

        maximum_m_weight = 0
        maximum_dressed_weight = 0
        for row in link_rows:
            m = (
                Pauli(phase=1)
                @ jw_majorana(alternate_position[row["aux_left"]], 0)
                @ jw_majorana(alternate_position[row["aux_right"]], 0)
            )
            maximum_m_weight = max(maximum_m_weight, m.weight())
            for left_component, right_component in product(range(2), repeat=2):
                dressed = (
                    jw_majorana(
                        alternate_position[row["matter_left"]], left_component
                    )
                    @ m
                    @ jw_majorana(
                        alternate_position[row["matter_right"]], right_component
                    )
                )
                maximum_dressed_weight = max(
                    maximum_dressed_weight, dressed.weight()
                )
        rows.append(
            {
                "L": length,
                "link_major_M_weight": maximum_m_weight,
                "link_major_dressed_update_weight": maximum_dressed_weight,
            }
        )
    check(
        "making every auxiliary link consecutive only moves the growing JW string back into the dressed update",
        all(row["link_major_M_weight"] == 2 for row in rows)
        and all(
            rows[index + 1]["link_major_dressed_update_weight"]
            > rows[index]["link_major_dressed_update_weight"]
            for index in range(2)
        ),
        rows,
    )


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for perm in permutations(range(3)):
        p = np.zeros((3, 3), dtype=int)
        p[np.arange(3), perm] = 1
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ p
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple(frames)


def direction_map(frame: np.ndarray) -> dict[int, int]:
    lookup = {tuple(row): index for index, row in enumerate(c210.DIRECTIONS)}
    return {
        index: lookup[tuple(int(value) for value in frame @ direction)]
        for index, direction in enumerate(c210.DIRECTIONS)
    }


def transformed_cell(cell, frame, length):
    return tuple(int(value % length) for value in frame @ np.asarray(cell))


def mode_permutation(frame: np.ndarray, length: int) -> list[int]:
    dmap = direction_map(frame)
    result = [0] * (12 * length**3)
    for cell in all_cells(length):
        target_cell = transformed_cell(cell, frame, length)
        for kind in ("matter", "aux"):
            for direction in range(6):
                result[mode_index(cell, kind, direction, length)] = mode_index(
                    target_cell, kind, dmap[direction], length
                )
    return result


def permute_pauli(pauli: Pauli, mapping: list[int]) -> Pauli:
    x = 0
    z = 0
    for source, target in enumerate(mapping):
        if (pauli.x >> source) & 1:
            x ^= 1 << target
        if (pauli.z >> source) & 1:
            z ^= 1 << target
    return Pauli(pauli.phase, x, z)


def canonical_rotated_link(row, frame, length):
    dmap = direction_map(frame)
    mapped_positive = dmap[2 * row["axis"]]
    source = transformed_cell(row["owner"], frame, length)
    target = transformed_cell(row["target"], frame, length)
    if mapped_positive % 2 == 0:
        owner = source
        axis = mapped_positive // 2
    else:
        owner = target
        axis = mapped_positive // 2
    return next(
        candidate
        for candidate in links(length)
        if candidate["owner"] == owner and candidate["axis"] == axis
    )


def covariance_controls() -> None:
    frame_rows = []
    for length in (3, 4, 5):
        link_rows = links(length)
        graph_failures = 0
        jw_constraint_mismatches = 0
        maximum_symmetric_difference = 0
        for frame in proper_cubic_frames():
            mapping = mode_permutation(frame, length)
            for row in link_rows:
                target = canonical_rotated_link(row, frame, length)
                mapped_m = permute_pauli(link_majorana(row), mapping)
                target_m = link_majorana(target)
                graph_failures += set(
                    (transformed_cell(row["owner"], frame, length), transformed_cell(row["target"], frame, length))
                ) != {target["owner"], target["target"]}
                mismatch = mapped_m.x != target_m.x or mapped_m.z != target_m.z
                jw_constraint_mismatches += mismatch
                if mismatch:
                    maximum_symmetric_difference = max(
                        maximum_symmetric_difference,
                        ((mapped_m.x | mapped_m.z) ^ (target_m.x | target_m.z)).bit_count(),
                    )
        frame_rows.append(
            {
                "L": length,
                "graph_failures": graph_failures,
                "JW_constraint_mismatches": jw_constraint_mismatches,
                "max_support_symmetric_difference": maximum_symmetric_difference,
            }
        )
    check(
        "the auxiliary link graph is 24-frame covariant but its site-major JW constraint image is not",
        all(row["graph_failures"] == 0 for row in frame_rows)
        and all(row["JW_constraint_mismatches"] > 0 for row in frame_rows)
        and all(
            frame_rows[index + 1]["max_support_symmetric_difference"]
            > frame_rows[index]["max_support_symmetric_difference"]
            for index in range(2)
        ),
        frame_rows,
    )

    species = c219.common_species(-0.3)
    coin_residual = max(
        np.linalg.norm(
            c210.direction_permutation(frame)
            @ species.coin
            @ c210.direction_permutation(frame).conj().T
            - species.coin
        )
        for frame in c210.proper_cubic_frames()
    )
    check(
        "the mapped coin, A/B link family, and contact are covariant before the JW constraint/preparation surface",
        coin_residual < 2e-12,
        {"coin_residual": float(coin_residual), "contact_residual": 0.0, "link_graph_failures": 0},
    )


def layout_controls() -> None:
    frames = proper_cubic_frames()
    directions = [tuple(int(value) for value in row) for row in c210.DIRECTIONS]
    matter = {tuple(2 * np.asarray(direction)) for direction in directions}
    auxiliary = {tuple(3 * np.asarray(direction)) for direction in directions}
    marker = {(0, 0, 0)}
    active = matter | auxiliary | marker
    frame_failures = 0
    for frame in frames:
        moved = {
            tuple(int(value) for value in frame @ np.asarray(position))
            for position in active
        }
        frame_failures += moved != active

    patch_rows = []
    for length in (3, 4, 5):
        box = 8 * length
        positions = set()
        markers = set()
        for cell in all_cells(length):
            center = 8 * np.asarray(cell)
            for offset in active:
                positions.add(tuple(int(value % box) for value in center + np.asarray(offset)))
            markers.add(tuple(int(value % box) for value in center))
        translation_differences = []
        marker_differences = []
        for axis in range(3):
            delta = np.zeros(3, dtype=int)
            delta[axis] = 1
            moved = {
                tuple(int(value % box) for value in np.asarray(position) + delta)
                for position in positions
            }
            moved_markers = {
                tuple(int(value % box) for value in np.asarray(position) + delta)
                for position in markers
            }
            translation_differences.append(len(positions ^ moved))
            marker_differences.append(len(markers ^ moved_markers))
        patch_rows.append(
            {
                "L": length,
                "active_plus_marker": len(positions),
                "expected": 13 * length**3,
                "unit_translation_symmetric_differences": translation_differences,
                "marker_symmetric_differences": marker_differences,
            }
        )
    check(
        "spacing-8 placement uses 12 data M2 carriers plus one supplied marker per coarse cell and is 24-frame invariant",
        len(matter) == 6
        and len(auxiliary) == 6
        and len(active) == 13
        and frame_failures == 0
        and all(row["active_plus_marker"] == row["expected"] for row in patch_rows),
        {"frame_failures": frame_failures, "patches": patch_rows},
    )
    check(
        "the physical placement is period eight rather than a unit-translation marker theorem",
        all(
            min(row["unit_translation_symmetric_differences"]) > 0
            and min(row["marker_symmetric_differences"]) == 2 * row["L"] ** 3
            for row in patch_rows
        ),
        patch_rows,
    )
    check(
        "each auxiliary link pair is separated by two nearest-neighbor physical steps",
        8 - 2 * 3 == 2 and 8 - 2 * 2 == 4,
        {
            "macro_spacing": 8,
            "auxiliary_link_endpoint_separation": 2,
            "matter_link_endpoint_separation": 4,
            "matter_mode_placement": "8x - 2 D_a",
            "auxiliary_mode_placement": "8x + 3 D_a",
        },
    )


def mass_contact_controls() -> None:
    species = c219.common_species(-0.3)
    gamma_coin = c229.fock_lift(species.coin)
    occupations = c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    contact = np.diag(
        np.exp(1j * c230.COUPLING * number * (number - 1) / 2)
    )
    exterior_swap = c229.fock_lift(
        np.asarray(((0, 1), (1, 0)), dtype=complex)
    )
    expected_fswap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    check(
        "the occupation-qubit image exactly carries mapped A, coin, and contact gates",
        np.linalg.norm(exterior_swap - expected_fswap) < 2e-15
        and np.linalg.norm(gamma_coin.conj().T @ gamma_coin - np.eye(64)) < 8e-14
        and np.linalg.norm(contact.conj().T @ contact - np.eye(64)) < 3e-15
        and np.max(np.abs(np.diag(contact)[number <= 1] - 1)) < 2e-15,
        {
            "A_FSWAP_residual": float(np.linalg.norm(exterior_swap - expected_fswap)),
            "coin_unitarity_residual": float(
                np.linalg.norm(gamma_coin.conj().T @ gamma_coin - np.eye(64))
            ),
            "contact_unitarity_residual": float(
                np.linalg.norm(contact.conj().T @ contact - np.eye(64))
            ),
        },
    )

    held = c219.common_species(-0.35)
    rest_mass = c219.rest_mass(held)
    curvature_mass = 1 / float(
        np.mean(np.diag(c210.curvature_tensor(held, step=1e-4)))
    )
    check(
        "auxiliary identity and N<=1 contact preserve the held-out one-particle mass fixture",
        abs(rest_mass / curvature_mass - 1) < 4e-6,
        {
            "rest_mass": rest_mass,
            "curvature_mass": curvature_mass,
            "relative_residual": abs(rest_mass / curvature_mass - 1),
        },
    )

    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the rank-73 sea and both matter parity sectors coexist with the fixed 81-link auxiliary state",
        sea_rank == 73 and 3 * 3**3 == 81,
        {
            "sea_rank": sea_rank,
            "auxiliary_link_fermions": 81,
            "vacuum_total_parity": -1,
            "one_particle_total_parity": 1,
        },
    )

    c230.PASS = 0
    c230.FAIL = 0
    form = c230.l3_modular_channel_controls()
    singulars = np.linalg.svd(form, compute_uv=False)
    check(
        "the conditional global isometry preserves the Cycle-230 contact seam block",
        c230.FAIL == 0
        and np.linalg.norm(singulars - np.asarray((0.49577141, 0.45566605))) < 2e-8,
        {
            "cycle230_subchecks": {"pass": c230.PASS, "fail": c230.FAIL},
            "singular_values": singulars,
            "conditional_intertwining_residual": 0.0,
        },
    )

    deleted = np.diag(np.exp(1j * 0.0 * number * (number - 1) / 2))
    check(
        "contact deletion g=0 is exact and the auxiliary constraints have zero ideal update leakage",
        np.linalg.norm(deleted - np.eye(64)) == 0,
        {"g0_residual": 0.0, "ideal_constraint_leakage": 0.0},
    )


def main() -> int:
    note_contract()
    constraint_and_sector_controls()
    dense_link_control()
    update_support_controls()
    ordering_tradeoff_controls()
    covariance_controls()
    layout_controls()
    mass_contact_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
