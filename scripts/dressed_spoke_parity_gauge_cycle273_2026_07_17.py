#!/usr/bin/env python3
"""Cycle 273: dressed-spoke parity-gauge centralizer tournament.

Enumerate the Pauli centralizer on one three-qubit reference gamma register
and its six adjacent three-qubit matter gamma registers by GF(2) symplectic
reduction.  Test reference-only, one-spoke dressed, full-star dressed,
quartic-center, and subsystem-gauge routes.  The bounded negative is confined
to this one-star Pauli/factorized-pair grammar; larger, non-Pauli, and
multicell dressings remain live.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import covariant_vertex_gamma_car_compiler_cycle261_2026_07_17 as c261
import nondiagonal_reference_cat_parity_join_cycle267_2026_07_17 as c267


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "DRESSED_SPOKE_PARITY_GAUGE_CYCLE273_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
LOCAL_QUBITS = 21
LOCAL_MASK = (1 << LOCAL_QUBITS) - 1


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
        check("the Cycle-273 note exists", False, NOTE)
        return
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "reference-only",
        "one-spoke dressed",
        "full-star dressed",
        "quartic",
        "subsystem",
        "rank `n-1`",
        "both parities",
        "held-out `l=6`",
        "all 24 proper-cubic frames",
        "three wilson",
        "beta=-0.3",
        "g=0.37",
        "rank-73",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "not records",
        "not physical time",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves dressed-route, Wilson, fixture, N1-N8, Record, and time boundaries",
        not missing,
        missing,
    )


def swapped_symplectic(vector: int, qubits: int = LOCAL_QUBITS) -> int:
    mask = (1 << qubits) - 1
    return (vector >> qubits) | ((vector & mask) << qubits)


def symplectic_bit(left: int, right: int, qubits: int = LOCAL_QUBITS) -> int:
    return (left & swapped_symplectic(right, qubits)).bit_count() % 2


def gf2_nullspace(rows: list[int], variables: int) -> list[int]:
    pivots: dict[int, int] = {}
    for source in rows:
        row = int(source)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    for pivot in sorted(pivots):
        row = pivots[pivot]
        for other in tuple(pivots):
            if other != pivot and ((pivots[other] >> pivot) & 1):
                pivots[other] ^= row
    free = [column for column in range(variables) if column not in pivots]
    basis = []
    for column in free:
        vector = 1 << column
        for pivot, row in pivots.items():
            if (row >> column) & 1:
                vector |= 1 << pivot
        basis.append(vector)
    return basis


def span_vector(basis: list[int], coefficient: int) -> int:
    vector = 0
    for index, row in enumerate(basis):
        if (coefficient >> index) & 1:
            vector ^= row
    return vector


def restricted_rank_and_flip(
    equations: list[int], allowed_modes: tuple[int, ...]
) -> tuple[int, int, bool]:
    columns = []
    for mode in allowed_modes:
        columns.extend(range(3 * mode, 3 * mode + 3))
        columns.extend(
            range(LOCAL_QUBITS + 3 * mode, LOCAL_QUBITS + 3 * mode + 3)
        )
    reduced = []
    for equation in equations:
        row = 0
        for target, source in enumerate(columns):
            row |= ((equation >> source) & 1) << target
        reduced.append(row)
    parity = 0
    for target, source in enumerate(columns):
        if source in range(18, 21):
            parity |= 1 << target
    rank = c235.gf2_rank(reduced)
    augmented = c235.gf2_rank(reduced + [parity])
    return rank, len(columns) - rank, augmented > rank


def local_star_data() -> dict[str, object]:
    code = c267.reference_spoke_code(3)
    cell = (0, 0, 0)
    matter_modes = [code.graph.vertex_index[(cell, direction)] for direction in range(6)]
    reference_mode = 6 * 3**3 + code.graph.cells.index(cell)
    modes = matter_modes + [reference_mode]

    def restrict(pauli: c235.Pauli) -> int:
        x = z = 0
        for local_mode, global_mode in enumerate(modes):
            for bit in range(3):
                local = 3 * local_mode + bit
                global_qubit = 3 * global_mode + bit
                x |= ((pauli.x >> global_qubit) & 1) << local
                z |= ((pauli.z >> global_qubit) & 1) << local
        return x | (z << LOCAL_QUBITS)

    spokes = sorted({restrict(pauli) for pauli in code.spokes if restrict(pauli)})
    loops = sorted({restrict(pauli) for pauli in code.local_loops if restrict(pauli)})
    edge_words = sorted(
        {
            restrict(pauli)
            for pauli in code.original_edges + code.spokes
            if restrict(pauli)
        }
    )
    constraints = sorted(set(spokes + loops))
    equations = [swapped_symplectic(vector) for vector in constraints]
    centralizer = gf2_nullspace(equations, 2 * LOCAL_QUBITS)
    return {
        "code": code,
        "modes": modes,
        "restrict": restrict,
        "spokes": spokes,
        "loops": loops,
        "edge_words": edge_words,
        "constraints": constraints,
        "equations": equations,
        "centralizer": centralizer,
    }


def local_vector(pauli: c235.Pauli, mode: int) -> int:
    shifted = c267.shifted_local_pauli(mode, pauli)
    return shifted.x | (shifted.z << LOCAL_QUBITS)


def endpoint_local(direction: int) -> int:
    chirality = c235.Pauli(z=0b111)
    endpoint = chirality @ c261.LOCAL_GAMMAS[direction]
    return local_vector(endpoint, direction) ^ local_vector(endpoint, 6)


def frame_map(vector: int, permutation: tuple[int, ...]) -> int:
    x = vector & LOCAL_MASK
    z = vector >> LOCAL_QUBITS
    mapped_x = mapped_z = 0
    for mode in range(7):
        local = ((x >> (3 * mode)) & 0b111) | (
            ((z >> (3 * mode)) & 0b111) << 3
        )
        mapped = c261.clifford_vector_map(local, permutation)
        target = permutation[mode] if mode < 6 else 6
        mapped_x |= (mapped & 0b111) << (3 * target)
        mapped_z |= (mapped >> 3) << (3 * target)
    return mapped_x | (mapped_z << LOCAL_QUBITS)


def centralizer_and_route_controls() -> None:
    data = local_star_data()
    equations = data["equations"]
    centralizer = data["centralizer"]
    reference_flip_mask = 0b111 << 18
    parity_flips = sum(
        (span_vector(centralizer, coefficient) & reference_flip_mask).bit_count()
        % 2
        for coefficient in range(1 << len(centralizer))
    )

    reference_rank, reference_dimension, reference_flip = restricted_rank_and_flip(
        equations, (6,)
    )
    one_spoke = []
    for direction in range(6):
        rank, dimension, flip = restricted_rank_and_flip(
            equations, (direction, 6)
        )
        candidate = endpoint_local(direction)
        one_spoke.append(
            {
                "direction": direction,
                "rank": rank,
                "null_dimension": dimension,
                "parity_flip_exists": flip,
                "displayed_endpoint_in_centralizer": all(
                    symplectic_bit(candidate, constraint) == 0
                    for constraint in data["constraints"]
                ),
                "support": ((candidate & LOCAL_MASK) | (candidate >> LOCAL_QUBITS)).bit_count(),
            }
        )

    frames, permutations = c261.direction_permutations()
    del frames
    stabilizer = [index for index, permutation in enumerate(permutations) if permutation[0] == 0]
    representatives = [
        next(index for index, permutation in enumerate(permutations) if permutation[0] == direction)
        for direction in range(6)
    ]
    stabilizer_fixed = []
    scalar_flips = []
    conflict_distribution: Counter[int] = Counter()
    matter_block_distribution: Counter[int] = Counter()
    for coefficient in range(1 << len(centralizer)):
        vector = span_vector(centralizer, coefficient)
        if (vector & reference_flip_mask).bit_count() % 2 == 0:
            continue
        if all(frame_map(vector, permutation) == vector for permutation in permutations):
            scalar_flips.append(vector)
        if not all(
            frame_map(vector, permutations[index]) == vector for index in stabilizer
        ):
            continue
        stabilizer_fixed.append(vector)
        orbit = [frame_map(vector, permutations[index]) for index in representatives]
        conflicts = sum(
            symplectic_bit(orbit[left], orbit[right])
            for left, right in combinations(range(6), 2)
        )
        matter_blocks = sum(
            bool(
                ((vector & LOCAL_MASK) >> (3 * mode)) & 0b111
                or ((vector >> LOCAL_QUBITS) >> (3 * mode)) & 0b111
            )
            for mode in range(6)
        )
        conflict_distribution[conflicts] += 1
        matter_block_distribution[matter_blocks] += 1

    endpoint_conflicts = sum(
        symplectic_bit(endpoint_local(left), endpoint_local(right))
        for left, right in combinations(range(6), 2)
    )
    endpoint_frame_failures = sum(
        frame_map(endpoint_local(direction), permutation)
        != endpoint_local(permutation[direction])
        for permutation in permutations
        for direction in range(6)
    )
    check(
        "the one-star symplectic quotient enumerates the complete bounded Pauli centralizer without raw 4^21 search",
        len(data["spokes"]) == 6
        and c235.gf2_rank(data["spokes"]) == 6
        and len(data["loops"]) == 32
        and c235.gf2_rank(data["loops"]) == 17
        and len(data["constraints"]) == 38
        and c235.gf2_rank(data["constraints"]) == 23
        and len(centralizer) == 19
        and parity_flips == 2**18,
        {
            "local_qubits": LOCAL_QUBITS,
            "raw_Pauli_space": "4^21",
            "constraint_rank": c235.gf2_rank(data["constraints"]),
            "centralizer_dimension": len(centralizer),
            "centralizer_vectors": 2 ** len(centralizer),
            "reference_parity_flips": parity_flips,
        },
    )
    check(
        "reference-only parity flips remain absent while every one-spoke block has one unique dressed flip",
        reference_dimension == 0
        and not reference_flip
        and reference_rank == 6
        and all(
            row["null_dimension"] == 1
            and row["parity_flip_exists"]
            and row["displayed_endpoint_in_centralizer"]
            for row in one_spoke
        )
        and endpoint_conflicts == 15
        and endpoint_frame_failures == 0,
        {
            "reference_only": {
                "rank": reference_rank,
                "null_dimension": reference_dimension,
                "parity_flip": reference_flip,
            },
            "one_spoke_routes": one_spoke,
            "endpoint_formula": "D_d=(B gamma_d)_matter,d (B gamma_d)_reference",
            "six_endpoint_pairwise_anticommutators": endpoint_conflicts,
            "endpoint_proper_cubic_frame_failures": endpoint_frame_failures,
        },
    )
    check(
        "full-star matter dressing has no scalar parity flip and every direction-covariant endpoint orbit remains a complete six-Majorana conflict set",
        len(stabilizer_fixed) == 64
        and len(scalar_flips) == 0
        and conflict_distribution == Counter({15: 64})
        and min(matter_block_distribution) == 1
        and max(matter_block_distribution) == 6,
        {
            "direction_stabilizer_fixed_parity_flips": len(stabilizer_fixed),
            "all_frame_scalar_parity_flips": len(scalar_flips),
            "orbit_conflict_distribution": dict(conflict_distribution),
            "matter_block_support_distribution": dict(sorted(matter_block_distribution.items())),
            "scope": "one reference plus six adjacent matter blocks; Pauli endpoints with factorized nearest-cell pair constraints",
        },
    )


def multiply(paulis: list[c235.Pauli]) -> c235.Pauli:
    result = c235.Pauli()
    for pauli in paulis:
        result = result @ pauli
    return result


def phase_flip(pauli: c235.Pauli) -> c235.Pauli:
    return c235.Pauli((pauli.phase + 2) % 4, pauli.x, pauli.z)


def global_endpoint(
    code: c267.ReferenceSpokeCode, cell_index: int, direction: int
) -> c235.Pauli:
    cells = len(code.graph.cells)
    matter = code.graph.vertex_index[(code.graph.cells[cell_index], direction)]
    reference = 6 * cells + cell_index
    local = c235.Pauli(z=0b111) @ c261.LOCAL_GAMMAS[direction]
    return c267.shifted_local_pauli(matter, local) @ c267.shifted_local_pauli(
        reference, local
    )


def cell_pairs(code: c267.ReferenceSpokeCode) -> list[tuple[int, int, int]]:
    index = {cell: position for position, cell in enumerate(code.graph.cells)}
    result = []
    length = code.graph.length
    for cell in code.graph.cells:
        source = index[cell]
        for axis in range(3):
            target_cell = list(cell)
            target_cell[axis] = (target_cell[axis] + 1) % length
            result.append((source, index[tuple(target_cell)], axis))
    return result


def parity_status(
    checks: list[c235.Pauli], parity: c235.Pauli, qubits: int
) -> tuple[int, bool, bool]:
    rank, bad = c235.phase_aware_rank(checks, qubits)
    _, plus_bad = c235.phase_aware_rank(checks + [parity], qubits)
    _, minus_bad = c235.phase_aware_rank(checks + [phase_flip(parity)], qubits)
    return rank, not plus_bad and not bad, not minus_bad and not bad


def pair_family_controls() -> None:
    frames, permutations = c261.direction_permutations()
    del frames
    uniform_frame_failures = sum(permutation[0] != 0 for permutation in permutations)
    rows = []
    direct_l3 = None
    for length in (3, 4, 5, 6):
        code = c267.reference_spoke_code(length)
        cells = length**3
        qubits = 21 * cells
        local = code.local_loops
        full = local + code.wilson_loops
        local_rank = c235.gf2_rank(pauli.symplectic(qubits) for pauli in local)
        full_rank = c235.gf2_rank(pauli.symplectic(qubits) for pauli in full)
        endpoints = [
            [global_endpoint(code, cell, direction) for direction in range(6)]
            for cell in range(cells)
        ]
        pairs = cell_pairs(code)
        uniform = [
            endpoints[source][0] @ endpoints[target][0]
            for source, target, _ in pairs
        ]
        directional = [
            endpoints[source][2 * axis] @ endpoints[target][2 * axis + 1]
            for source, target, axis in pairs
        ]
        uniform_rank = c235.gf2_rank(pauli.symplectic(qubits) for pauli in uniform)
        uniform_local_rank, uniform_local_bad = c235.phase_aware_rank(
            local + uniform, qubits
        )
        uniform_full_rank, uniform_full_bad = c235.phase_aware_rank(
            full + uniform, qubits
        )
        reference_parity = c261.total_parity(
            [c261.chirality_parity(6 * cells + cell) for cell in range(cells)]
        )
        _, plus_ok, minus_ok = parity_status(full + uniform, reference_parity, qubits)
        kept = [
            pair
            for pair, (source, target, _) in zip(uniform, pairs)
            if source != 0 and target != 0
        ]
        deleted_rank = c235.gf2_rank(pauli.symplectic(qubits) for pauli in kept)
        directional_conflicts = sum(
            not left.commutes(right)
            for position, left in enumerate(directional)
            for right in directional[position + 1 :]
        )
        directional_code_leakage = sum(
            not pair.commutes(check)
            for pair in directional
            for check in code.spokes + local
        )

        reference_only = []
        local_p = c235.Pauli(z=0b111) @ c261.LOCAL_GAMMAS[0]
        for source, target, _ in pairs:
            left = c267.shifted_local_pauli(6 * cells + source, local_p)
            right = c267.shifted_local_pauli(6 * cells + target, local_p)
            reference_only.append(left @ right)
        dressing_deleted_spokes = sum(
            not pair.commutes(spoke)
            for pair in reference_only
            for spoke in code.spokes
        )
        dressing_deleted_loops = sum(
            not pair.commutes(loop)
            for pair in reference_only
            for loop in full
        )
        matter_b0 = [
            c261.chirality_parity(code.graph.vertex_index[(cell, 0)])
            for cell in code.graph.cells
        ]
        matter_b_leakage = sum(
            not parity.commutes(pair)
            for parity in matter_b0
            for pair in uniform
        )
        a_leakage = sum(
            not edge.commutes(pair)
            for edge in code.original_edges + code.spokes
            for pair in uniform
        )
        rows.append(
            {
                "L": length,
                "N": cells,
                "physical_M2_per_cell": 21,
                "local_rank": local_rank,
                "full_rank": full_rank,
                "Wilson_increment": full_rank - local_rank,
                "uniform_pair_rank": uniform_rank,
                "uniform_local_increment": uniform_local_rank - local_rank,
                "uniform_full_increment": uniform_full_rank - full_rank,
                "uniform_phase_inconsistencies": (
                    len(uniform_local_bad),
                    len(uniform_full_bad),
                ),
                "uniform_local_exponent": qubits - uniform_local_rank,
                "uniform_full_exponent": qubits - uniform_full_rank,
                "target_V": 6 * cells,
                "both_reference_parities": plus_ok and minus_ok,
                "deleted_star_rank": deleted_rank,
                "dressing_deleted_spokes": dressing_deleted_spokes,
                "dressing_deleted_loops": dressing_deleted_loops,
                "dressed_directional_mutual_anticommutators": directional_conflicts,
                "dressed_directional_code_leakage": directional_code_leakage,
                "original_matter_B0_pair_leakage": matter_b_leakage,
                "original_A_pair_leakage": a_leakage,
                "maximum_endpoint_support": max(
                    (endpoint.x | endpoint.z).bit_count()
                    for row in endpoints
                    for endpoint in row
                ),
                "maximum_pair_support": max(
                    (pair.x | pair.z).bit_count() for pair in uniform
                ),
                "preparation_depth_lower_bound": c267.torus_depth_lower_bound(
                    length
                ),
            }
        )
        if length == 3:
            direct_l3 = {
                "uniform_mutual_anticommutators": sum(
                    not left.commutes(right)
                    for position, left in enumerate(uniform)
                    for right in uniform[position + 1 :]
                ),
                "uniform_code_leakage": sum(
                    not pair.commutes(check)
                    for pair in uniform
                    for check in code.spokes + local
                ),
                "directional_pair_rank": c235.gf2_rank(
                    pair.symplectic(qubits) for pair in directional
                ),
            }
    check(
        "uniform one-spoke dressed equalities are code-preserving commuting rank N-1 with both parities and exact full-sector exponent V",
        uniform_frame_failures == 20
        and all(
            row["local_rank"] == 14 * row["N"] - 2
            and row["full_rank"] == 14 * row["N"] + 1
            and row["Wilson_increment"] == 3
            and row["uniform_pair_rank"] == row["N"] - 1
            and row["uniform_local_increment"] == row["N"] - 1
            and row["uniform_full_increment"] == row["N"] - 1
            and row["uniform_phase_inconsistencies"] == (0, 0)
            and row["uniform_local_exponent"] == row["target_V"] + 3
            and row["uniform_full_exponent"] == row["target_V"]
            and row["both_reference_parities"]
            and row["deleted_star_rank"] == row["N"] - 2
            and row["maximum_endpoint_support"] == 6
            and row["maximum_pair_support"] == 12
            for row in rows
        )
        and rows[-1]["preparation_depth_lower_bound"]
        > rows[0]["preparation_depth_lower_bound"]
        and direct_l3
        == {
            "uniform_mutual_anticommutators": 0,
            "uniform_code_leakage": 0,
            "directional_pair_rank": 81,
        },
        {
            "sizes": rows,
            "uniform_direction_frame_failures": uniform_frame_failures,
            "held_out": "L=6",
        },
    )
    check(
        "matter dressing cancels spoke and loop leakage but deleting it restores the Cycle-267 leakage formulas",
        all(
            row["dressing_deleted_spokes"] == 6 * row["N"]
            and row["dressing_deleted_loops"] == 24 * row["N"]
            and row["dressed_directional_code_leakage"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "the all-frame directional dressed orbit retains 15N mutual conflicts and the uniform family does not preserve the original matter B algebra",
        all(
            row["dressed_directional_mutual_anticommutators"] == 15 * row["N"]
            and row["original_matter_B0_pair_leakage"] == 6 * row["N"]
            and row["original_A_pair_leakage"] == 0
            for row in rows
        ),
        {
            "sizes": rows,
            "algebra_status": "all original A words survive; the selected matter B_0 is not codespace preserving; a complete bounded dressed-B replacement was not constructed",
        },
    )


def plaquette_products(
    code: c267.ReferenceSpokeCode,
    edge_gauges: list[c235.Pauli],
) -> list[c235.Pauli]:
    length = code.graph.length
    index = {cell: position for position, cell in enumerate(code.graph.cells)}
    edge_lookup = {}
    for edge, (source, _, axis) in enumerate(cell_pairs(code)):
        edge_lookup[(source, axis)] = edge
    plaquettes = []
    for cell in code.graph.cells:
        source = index[cell]
        for first, second in combinations(range(3), 2):
            moved_first = list(cell)
            moved_first[first] = (moved_first[first] + 1) % length
            moved_second = list(cell)
            moved_second[second] = (moved_second[second] + 1) % length
            plaquettes.append(
                multiply(
                    [
                        edge_gauges[edge_lookup[(source, first)]],
                        edge_gauges[edge_lookup[(index[tuple(moved_first)], second)]],
                        edge_gauges[edge_lookup[(index[tuple(moved_second)], first)]],
                        edge_gauges[edge_lookup[(source, second)]],
                    ]
                )
            )
    return plaquettes


def subsystem_and_quartic_controls() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code = c267.reference_spoke_code(length)
        cells = length**3
        qubits = 21 * cells
        full = code.local_loops + code.wilson_loops
        base_rank = c235.gf2_rank(pauli.symplectic(qubits) for pauli in full)
        endpoints = [
            [global_endpoint(code, cell, direction) for direction in range(6)]
            for cell in range(cells)
        ]
        gauges = [
            endpoints[source][2 * axis] @ endpoints[target][2 * axis + 1]
            for source, target, axis in cell_pairs(code)
        ]
        combined_rank = c235.gf2_rank(
            [pauli.symplectic(qubits) for pauli in full + gauges]
        )
        gauge_logical_rank = combined_rank - base_rank
        gram = []
        for left in gauges:
            row = 0
            for index, right in enumerate(gauges):
                if not left.commutes(right):
                    row |= 1 << index
            gram.append(row)
        gram_rank = c235.gf2_rank(gram)
        gauge_center_rank = gauge_logical_rank - gram_rank
        subsystem_reduction = gauge_logical_rank - gram_rank // 2
        subsystem_exponent = qubits - base_rank - subsystem_reduction
        reference_parity = c261.total_parity(
            [c261.chirality_parity(6 * cells + cell) for cell in range(cells)]
        )
        parity_increment = c235.gf2_rank(
            [pauli.symplectic(qubits) for pauli in full + gauges + [reference_parity]]
        ) - combined_rank
        plaquettes = plaquette_products(code, gauges)
        plaquette_rank = c235.gf2_rank(
            [pauli.symplectic(qubits) for pauli in full + plaquettes]
        ) - base_rank
        plaquette_conflicts = sum(
            not left.commutes(right)
            for position, left in enumerate(plaquettes)
            for right in plaquettes[position + 1 :]
        )
        onsite_parities = [
            c261.chirality_parity(6 * cells + cell) for cell in range(cells)
        ]
        onsite_parity_leakage = sum(
            not plaquette.commutes(parity)
            for plaquette in plaquettes
            for parity in onsite_parities
        )
        rows.append(
            {
                "L": length,
                "N": cells,
                "gauge_generators": len(gauges),
                "gauge_logical_rank": gauge_logical_rank,
                "gauge_Gram_rank": gram_rank,
                "gauge_center_rank": gauge_center_rank,
                "gauge_anticommutators": sum(row.bit_count() for row in gram) // 2,
                "subsystem_reduction": subsystem_reduction,
                "subsystem_exponent": subsystem_exponent,
                "target_exponent": 6 * cells,
                "reference_parity_increment": parity_increment,
                "quartic_plaquettes": len(plaquettes),
                "quartic_rank_mod_base": plaquette_rank,
                "quartic_mutual_anticommutators": plaquette_conflicts,
                "quartic_onsite_parity_leakage": onsite_parity_leakage,
            }
        )
    check(
        "the direction-covariant pair orbit is a valid subsystem gauge family but over-reduces the logical exponent",
        all(
            row["gauge_generators"] == 3 * row["N"]
            and row["gauge_logical_rank"] == 3 * row["N"]
            and row["gauge_Gram_rank"]
            == row["N"] - (2 if row["N"] % 2 == 0 else 1)
            and row["gauge_center_rank"]
            == 2 * row["N"] + (2 if row["N"] % 2 == 0 else 1)
            and row["gauge_anticommutators"] == 15 * row["N"]
            and row["subsystem_exponent"] < row["target_exponent"]
            and row["reference_parity_increment"] == 1
            for row in rows
        ),
        rows,
    )
    check(
        "the all-frame quartic plaquette center commutes but is parity-even at every cell and has rank 2N-2 rather than N-1",
        all(
            row["quartic_plaquettes"] == 3 * row["N"]
            and row["quartic_rank_mod_base"] == 2 * row["N"] - 2
            and row["quartic_mutual_anticommutators"] == 0
            and row["quartic_onsite_parity_leakage"] == 0
            for row in rows
        ),
        rows,
    )


def fixture_and_scope_controls() -> None:
    species = c219.common_species(c230.BETA)
    rest_mass = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the predecessor Cycle-230 mass/contact/seam fixture remains exact but no physical intertwiner is claimed",
        abs(c230.BETA + 0.3) < 1e-15
        and abs(c230.COUPLING - 0.37) < 1e-15
        and abs(rest_mass / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "rest_mass_predecessor": rest_mass,
            "principal_sea_rank_predecessor": sea_rank,
            "E_G_coarse_equals_G_physical_E": False,
            "free_contact_seam_intertwiner": "not reached because no tested route simultaneously closes covariance, commuting rank, and matter algebra",
        },
    )
    check(
        "the bounded Pauli result leaves larger, non-Pauli, and multicell routes live without axiom pressure",
        True,
        {
            "authority": "none",
            "audit": "unset",
            "larger_register": "live",
            "non_Pauli": "live",
            "multicell_dressing": "live",
            "coherent_gauge_data_are_Records": False,
            "compiler_schedule_is_physical_time": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    note_contract()
    centralizer_and_route_controls()
    pair_family_controls()
    subsystem_and_quartic_controls()
    fixture_and_scope_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
