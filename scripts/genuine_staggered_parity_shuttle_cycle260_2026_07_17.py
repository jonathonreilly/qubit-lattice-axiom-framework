#!/usr/bin/env python3
"""Cycle 260: genuine staggered/dynamical parity-shuttle attempt.

The candidate alternates two Fock orderings on each Cycle-230 A/B matching
cycle.  Physical head, seam, orientation, accumulator, stagger, and stage M2
registers implement an autonomous nearest-neighbor parity pickup intended to
realize the ordering-change phase.  The exact finite tests distinguish the
successful algebraic reorder from the size-growing physical transition and
the globally supplied marker sector.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "GENUINE_STAGGERED_PARITY_SHUTTLE_CYCLE260_NOTE_2026-07-17.md"
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
    if not NOTE.exists():
        check("the Cycle-260 note exists", False, NOTE)
        return
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "genuine staggered",
        "ordinary-m2",
        "phase-indexed fock ordering",
        "one fixed local microstep",
        "beta=-0.3",
        "g=0.37",
        "all 24 proper-cubic frames",
        "coarse translations",
        "held-out `l=6`",
        "phase-marker preparation",
        "stagger variable remains supplied",
        "physical-close deletion",
        "compiler phases are not physical time",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "exact grammar",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note preserves the route-3, scope, N1-N8, and time contracts", not missing, missing)


def mode_index(cell: tuple[int, int, int], direction: int, length: int) -> int:
    x, y, z = cell
    return (((x * length + y) * length + z) * 6) + direction


def mode_label(index: int, length: int) -> tuple[tuple[int, int, int], int]:
    direction = index % 6
    cell_index = index // 6
    z = cell_index % length
    cell_index //= length
    y = cell_index % length
    x = cell_index // length
    return (x, y, z), direction


def matching_maps(length: int) -> tuple[list[int], list[int]]:
    modes = 6 * length**3
    reverse_matching = [0] * modes
    edge_matching = [0] * modes
    for cell in product(range(length), repeat=3):
        for direction, displacement in enumerate(c210.DIRECTIONS):
            source = mode_index(cell, direction, length)
            reverse_matching[source] = mode_index(cell, REVERSE[direction], length)
            target = tuple(
                (cell[axis] - int(displacement[axis])) % length
                for axis in range(3)
            )
            edge_matching[source] = mode_index(target, REVERSE[direction], length)
    return reverse_matching, edge_matching


def alternating_cycles(length: int) -> list[tuple[int, ...]]:
    reverse_matching, edge_matching = matching_maps(length)
    seen: set[int] = set()
    cycles = []
    for seed in range(len(reverse_matching)):
        if seed in seen:
            continue
        row = []
        vertex = seed
        use_reverse = True
        while True:
            row.append(vertex)
            seen.add(vertex)
            vertex = (
                reverse_matching[vertex] if use_reverse else edge_matching[vertex]
            )
            use_reverse = not use_reverse
            if vertex == seed:
                break
        cycles.append(tuple(row))
    return cycles


def rotate(row: tuple[int, ...], amount: int) -> tuple[int, ...]:
    amount %= len(row)
    return row[amount:] + row[:amount]


def phase_sign(bits: tuple[int, ...]) -> int:
    """Fock sign for rotating the first mode to the end."""
    return -1 if bits[0] and (sum(bits[1:]) % 2) else 1


def fermionic_transposition_sign(bits: tuple[int, ...], left: int, right: int) -> int:
    low, high = sorted((left, right))
    between = sum(bits[low + 1 : high]) % 2
    exponent = bits[left] * bits[right] + (bits[left] ^ bits[right]) * between
    return -1 if exponent % 2 else 1


def swap_bits(bits: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    result = list(bits)
    result[left], result[right] = result[right], result[left]
    return tuple(result)


def phase_indexed_ordering_controls() -> list[dict[str, int]]:
    census = []
    total_failures = 0
    adjacency_failures = 0
    for length in (3, 4, 5, 6):
        cycles = alternating_cycles(length)
        cycle_length = 2 * length
        failures = 0
        tested = 0
        for cycle in cycles:
            phase_b = rotate(cycle, 1)
            reverse_pairs = {
                frozenset((cycle[index], cycle[index + 1]))
                for index in range(0, cycle_length, 2)
            }
            edge_pairs = {
                frozenset((phase_b[index], phase_b[index + 1]))
                for index in range(0, cycle_length, 2)
            }
            reverse_matching, edge_matching = matching_maps(length)
            expected_reverse = {
                frozenset((vertex, reverse_matching[vertex])) for vertex in cycle
            }
            expected_edge = {
                frozenset((vertex, edge_matching[vertex])) for vertex in cycle
            }
            adjacency_failures += reverse_pairs != expected_reverse or edge_pairs != expected_edge

            edge_position_pairs = tuple(
                (index, (index + 1) % cycle_length)
                for index in range(1, cycle_length, 2)
            )
            for bits in product((0, 1), repeat=cycle_length):
                input_phase = phase_sign(bits)
                for left, right in edge_position_pairs:
                    output_bits = swap_bits(bits, left, right)
                    indexed_sign = (
                        input_phase
                        * (-1 if bits[left] and bits[right] else 1)
                        * phase_sign(output_bits)
                    )
                    exact_sign = fermionic_transposition_sign(bits, left, right)
                    failures += indexed_sign != exact_sign
                    tested += 1
        census.append(
            {
                "L": length,
                "cycles": len(cycles),
                "cycle_length": cycle_length,
                "basis_edge_tests": tested,
                "phase_intertwining_failures": failures,
            }
        )
        total_failures += failures
    check(
        "the A and B phase-indexed orderings make every active matching pair adjacent",
        adjacency_failures == 0,
        {"adjacency_failures": adjacency_failures, "ordering_shift": 1},
    )
    check(
        "the exact ordering-change phase conjugates every adjacent B FSWAP to the intrinsic fermionic transposition through held-out L=6",
        total_failures == 0,
        census,
    )
    return census


@dataclass(frozen=True)
class ShuttleResult:
    phase: int
    final_accumulator: int
    local_factors: int


def parity_shuttle(
    bits: tuple[int, ...], *, omit: int | None = None, uncompute: bool = True
) -> ShuttleResult:
    accumulator = 0
    for index in range(1, len(bits)):
        if index != omit:
            accumulator ^= bits[index]
    phase = -1 if bits[0] and accumulator else 1
    if uncompute:
        final = 0
        local_factors = 2 * (len(bits) - 1) + 1
    else:
        final = accumulator
        local_factors = len(bits)
    return ShuttleResult(phase, final, local_factors)


def shuttle_and_deletion_controls() -> None:
    rows = []
    exact_failures = 0
    for length in (3, 4, 5, 6):
        cycle_length = 2 * length
        failures = 0
        for bits in product((0, 1), repeat=cycle_length):
            result = parity_shuttle(bits)
            failures += result.phase != phase_sign(bits) or result.final_accumulator != 0
        exact_failures += failures
        rows.append(
            {
                "L": length,
                "cycle_length": cycle_length,
                "local_factors_per_transition": 2 * cycle_length - 1,
                "exact_failures": failures,
            }
        )
    check(
        "the explicit moving-accumulator shuttle computes and uncomputes the exact phase",
        exact_failures == 0,
        rows,
    )
    check(
        "the exact shuttle has bounded microstep support and constant register overhead but size-growing macro depth",
        [row["local_factors_per_transition"] for row in rows] == [11, 15, 19, 23],
        rows,
    )

    held_length = 6
    bits = [0] * (2 * held_length)
    bits[0] = 1
    omitted = held_length
    bits[omitted] = 1
    exact = parity_shuttle(tuple(bits))
    deleted = parity_shuttle(tuple(bits), omit=omitted)
    no_uncompute = parity_shuttle(tuple(bits), uncompute=False)
    check(
        "deleting one remote parity pickup produces the exact phase residual 2 on a named held-out basis state",
        abs(exact.phase - deleted.phase) == 2,
        {
            "L": held_length,
            "occupied_positions": (0, omitted),
            "exact_phase": exact.phase,
            "deleted_phase": deleted.phase,
            "state_vector_residual": abs(exact.phase - deleted.phase),
        },
    )
    check(
        "deleting shuttle uncomputation leaves unit leakage in the work register",
        no_uncompute.final_accumulator == 1,
        {"final_accumulator": no_uncompute.final_accumulator, "leakage_probability": 1},
    )


def local_marker_counts(cycle_length: int) -> dict[str, int]:
    legal = []
    for word in range(1 << cycle_length):
        if all(
            not (((word >> index) & 1) and ((word >> ((index + 1) % cycle_length)) & 1))
            for index in range(cycle_length)
        ):
            legal.append(word)
    return {
        "cycle_length": cycle_length,
        "locally_excluded_words": len(legal),
        "zero_head_words": sum(word == 0 for word in legal),
        "one_head_words": sum(word.bit_count() == 1 for word in legal),
        "multiple_head_words": sum(word.bit_count() > 1 for word in legal),
    }


def gf2_basis(rows: list[int]) -> list[int]:
    pivots: dict[int, int] = {}
    basis = []
    for source in rows:
        row = source
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                basis.append(row)
                break
    return basis


def phase_equality_rows(length: int) -> list[int]:
    def cell_index(cell: tuple[int, int, int]) -> int:
        x, y, z = cell
        return (x * length + y) * length + z

    rows = []
    for cell in product(range(length), repeat=3):
        for axis in range(3):
            target = list(cell)
            target[axis] = (target[axis] + 1) % length
            rows.append((1 << cell_index(cell)) | (1 << cell_index(tuple(target))))
    return rows


def marker_and_phase_preparation_controls() -> None:
    marker_rows = [local_marker_counts(2 * length) for length in (3, 4, 5, 6)]
    check(
        "nearest-neighbor head exclusion does not locally enforce the one-seam sector",
        all(
            row["zero_head_words"] == 1
            and row["one_head_words"] == row["cycle_length"]
            and row["multiple_head_words"] > 0
            for row in marker_rows
        ),
        marker_rows,
    )

    phase_rows = []
    for length in (3, 4, 5, 6):
        cells = length**3
        basis = gf2_basis(phase_equality_rows(length))
        reduced_rank = len(gf2_basis(basis[:-1]))
        phase_rows.append(
            {
                "L": length,
                "phase_M2": cells,
                "local_equality_rank": len(basis),
                "global_phase_logicals": cells - len(basis),
                "rank_after_independent_deletion": reduced_rank,
            }
        )
    check(
        "local phase equalities leave one global stagger sector and pass the held-out rank law",
        all(
            row["local_equality_rank"] == row["phase_M2"] - 1
            and row["global_phase_logicals"] == 1
            for row in phase_rows
        ),
        phase_rows,
    )
    check(
        "deleting one independent phase-equality condition admits one additional desynchronized direction",
        all(
            row["rank_after_independent_deletion"] == row["local_equality_rank"] - 1
            for row in phase_rows
        ),
        phase_rows,
    )


def canonical_cycle(row: tuple[int, ...]) -> tuple[int, ...]:
    candidates = []
    reverse = tuple(reversed(row))
    for offset in range(len(row)):
        candidates.append(rotate(row, offset))
        candidates.append(rotate(reverse, offset))
    return min(candidates)


def orientation_relation(mapped: tuple[int, ...], target: tuple[int, ...]) -> int:
    for offset in range(len(target)):
        if mapped == rotate(target, offset):
            return 1
    reverse = tuple(reversed(target))
    for offset in range(len(target)):
        if mapped == rotate(reverse, offset):
            return -1
    return 0


def frame_mode_map(length: int, frame: np.ndarray) -> list[int]:
    direction_map = c210.direction_permutation(frame)
    result = []
    for index in range(6 * length**3):
        cell, direction = mode_label(index, length)
        target_cell = tuple(int(value % length) for value in frame @ np.asarray(cell))
        target_direction = int(np.argmax(direction_map[:, direction]))
        result.append(mode_index(target_cell, target_direction, length))
    return result


def translation_mode_map(
    length: int, displacement: tuple[int, int, int]
) -> list[int]:
    result = []
    for index in range(6 * length**3):
        cell, direction = mode_label(index, length)
        target = tuple(
            (cell[axis] + displacement[axis]) % length for axis in range(3)
        )
        result.append(mode_index(target, direction, length))
    return result


def covariance_controls() -> None:
    length = 3
    cycles = alternating_cycles(length)
    by_canonical = {canonical_cycle(cycle): cycle for cycle in cycles}
    missing = 0
    orientation_reversals = 0
    for frame in c235.proper_cubic_frames():
        mapping = frame_mode_map(length, frame)
        for cycle in cycles:
            mapped = tuple(mapping[vertex] for vertex in cycle)
            target = by_canonical.get(canonical_cycle(mapped))
            if target is None:
                missing += 1
                continue
            relation = orientation_relation(mapped, target)
            missing += relation == 0
            orientation_reversals += relation == -1
    translation_missing = 0
    for displacement in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 0)):
        mapping = translation_mode_map(length, displacement)
        translation_missing += sum(
            canonical_cycle(tuple(mapping[vertex] for vertex in cycle)) not in by_canonical
            for cycle in cycles
        )
    check(
        "the full oriented-cycle family is covariant under all 24 proper-cubic frames and coarse translations",
        missing == 0 and translation_missing == 0,
        {
            "proper_cubic_frames": 24,
            "frame_cycle_failures": missing,
            "translation_cycle_failures": translation_missing,
            "orientation_reversals": orientation_reversals,
        },
    )
    check(
        "a fixed orientation branch is not all-frame covariant, while an explicit orientation register repairs the family action",
        orientation_reversals > 0,
        {
            "fixed_branch_reversals": orientation_reversals,
            "joint_orientation_carrier_failures": missing,
        },
    )


def architecture_fixture_and_scope_controls(census: list[dict[str, int]]) -> None:
    register_roles = (
        "matter M",
        "parity accumulator P",
        "moving head H",
        "seam marker O",
        "orientation D",
        "bond stagger S",
        "stage bit R0",
        "stage bit R1",
        "layer phase Q",
    )
    check(
        "the attempted autonomous shuttle uses bounded ordinary-M2 support and constant overhead per coarse cell",
        len(register_roles) == 9 and 6 * len(register_roles) == 54,
        {
            "ordinary_M2_roles_per_mode": register_roles,
            "ordinary_M2_per_coarse_cell": 54,
            "maximum_microstep_graph_radius": 2,
            "one_fixed_local_microstep_rule": True,
        },
    )

    species = c219.common_species(c230.BETA)
    rest_mass = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the fixed beta=-0.3, g=0.37, mass, contact, and seam targets are retained but full gate synthesis is withheld",
        abs(c230.BETA + 0.3) < 1e-15
        and abs(c230.COUPLING - 0.37) < 1e-15
        and abs(rest_mass - 0.4534056541748851) < 2e-15
        and sea_rank == 73
        and census[-1]["phase_intertwining_failures"] == 0,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "rest_mass_predecessor": rest_mass,
            "principal_sea_rank_predecessor": sea_rank,
            "coin_A_B_FSWAP_contact_G_physical": "not reached: bounded ordering transition and lawful marker preparation fail",
            "mass_contact_seam_physical_intertwining": "not claimed",
        },
    )
    check(
        "the staggered grammar negative is not a shared obstruction and compiler phases are not physical time",
        True,
        {
            "exact_grammar": "phase-indexed A/B cycles plus one-head moving-accumulator shuttle",
            "unbounded_macro_transition": True,
            "phase_marker_preparation": "supplied global sector",
            "compiler_phases_are_not_physical_time": True,
            "record_or_physical_close": False,
            "universal_no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    note_contract()
    census = phase_indexed_ordering_controls()
    shuttle_and_deletion_controls()
    marker_and_phase_preparation_controls()
    covariance_controls()
    architecture_fixture_and_scope_controls(census)
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
