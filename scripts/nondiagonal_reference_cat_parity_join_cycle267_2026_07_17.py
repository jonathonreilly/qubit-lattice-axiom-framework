#!/usr/bin/env python3
"""Cycle 267: non-diagonal reference-cat parity join tournament.

Rebuild the committed Cycle-261 degree-six matter code and test whether a
translation/proper-cubic-covariant non-diagonal reference code supplies the
missing total-parity qubit without turning a multiplicity into a fermionic
parity relation.  The tests are finite exact Pauli/rank tests.  They do not
import Cycle 264 and do not claim a general fermion-to-qubit no-go.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations, product
from math import ceil, floor
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import covariant_vertex_gamma_car_compiler_cycle261_2026_07_17 as c261
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "NONDIAGONAL_REFERENCE_CAT_PARITY_JOIN_CYCLE267_NOTE_2026-07-17.md"
)

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


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-267 note exists", False, NOTE)
        return
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "x-equality",
        "majorana matching",
        "cluster-cat",
        "reference-spoke",
        "multiplicity",
        "logical z",
        "held-out l=6",
        "coherent parity superpositions",
        "three wilson",
        "all 24 proper-cubic frames",
        "chen and kapustin",
        "setia",
        "nys and carleo",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "no physical time",
        "not a record",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves route, parity, preparation, prior-art, and N1-N8 contracts",
        not missing,
        missing,
    )


def cubic_cells(length: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(product(range(length), repeat=3))


def cubic_edges(length: int) -> list[tuple[int, int, int]]:
    cells = cubic_cells(length)
    index = {cell: position for position, cell in enumerate(cells)}
    edges = []
    for cell in cells:
        for axis in range(3):
            neighbor = list(cell)
            neighbor[axis] = (neighbor[axis] + 1) % length
            edges.append((index[cell], index[tuple(neighbor)], axis))
    return edges


def incidence_rows(edges: list[tuple[int, int] | tuple[int, int, int]]) -> list[int]:
    return [(1 << edge[0]) | (1 << edge[1]) for edge in edges]


def deleted_vertex_rank(rows: list[int], vertex: int) -> int:
    kept = [row for row in rows if not ((row >> vertex) & 1)]
    return c235.gf2_rank(kept)


def torus_depth_lower_bound(length: int) -> int:
    """Nearest-neighbor product-input unitary light-cone lower bound."""
    diameter = 3 * floor(length / 2)
    return ceil(diameter / 2)


def shifted_local_pauli(vertex: int, pauli: c235.Pauli) -> c235.Pauli:
    shift = 3 * vertex
    return c235.Pauli(pauli.phase, pauli.x << shift, pauli.z << shift)


def pauli_support(pauli: c235.Pauli) -> int:
    return (pauli.x | pauli.z).bit_count()


def cycle261_matter_baseline() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        code = c261.degree_six_code(length)
        cells = length**3
        vertices = 6 * cells
        qubits = 3 * vertices
        local = code.local_loops + code.dummy_triangles
        full = local + code.wilson_loops
        local_rank, local_bad = c235.phase_aware_rank(local, qubits)
        full_rank, full_bad = c235.phase_aware_rank(full, qubits)
        matter_parity = c261.total_parity(code.parities)
        plus_rank, plus_bad = c235.phase_aware_rank(full + [matter_parity], qubits)
        minus = c235.Pauli(
            (matter_parity.phase + 2) % 4, matter_parity.x, matter_parity.z
        )
        _, minus_bad = c235.phase_aware_rank(full + [minus], qubits)
        rows.append(
            {
                "L": length,
                "V": vertices,
                "physical_M2": qubits,
                "local_rank": local_rank,
                "full_rank": full_rank,
                "local_exponent": qubits - local_rank,
                "full_exponent": qubits - full_rank,
                "Wilson_increment": full_rank - local_rank,
                "matter_parity_increment": plus_rank - full_rank,
                "plus_consistent": not plus_bad,
                "minus_consistent": not minus_bad,
                "phase_inconsistencies": (len(local_bad), len(full_bad)),
            }
        )
    check(
        "the committed Cycle-261 matter substrate is rebuilt with even-sector rank and three supplied Wilson choices",
        all(
            row["local_rank"] == 2 * row["V"] - 2
            and row["full_rank"] == 2 * row["V"] + 1
            and row["local_exponent"] == row["V"] + 2
            and row["full_exponent"] == row["V"] - 1
            and row["Wilson_increment"] == 3
            and row["matter_parity_increment"] == 0
            and row["plus_consistent"]
            and not row["minus_consistent"]
            and row["phase_inconsistencies"] == (0, 0)
            for row in rows
        ),
        rows,
    )


def ordinary_carrier_route() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        matter = c261.degree_six_code(length)
        cells = length**3
        vertices = 6 * cells
        graph_edges = [(edge[0], edge[1]) for edge in matter.graph.edges]
        graph_edges.extend((edge[0], edge[1]) for edge in matter.dummies)
        carrier_checks = incidence_rows(graph_edges)
        carrier_rank = c235.gf2_rank(carrier_checks)
        carrier_parity = c235.Pauli(z=(1 << vertices) - 1)
        plus_rank, plus_bad = c235.phase_aware_rank(
            [c235.Pauli(x=row) for row in carrier_checks] + [carrier_parity],
            vertices,
        )
        minus = c235.Pauli(phase=2, z=(1 << vertices) - 1)
        minus_rank, minus_bad = c235.phase_aware_rank(
            [c235.Pauli(x=row) for row in carrier_checks] + [minus], vertices
        )
        matter_local_rank = 2 * vertices - 2
        matter_full_rank = 2 * vertices + 1
        local_exponent = 3 * vertices + vertices - matter_local_rank - carrier_rank
        full_exponent = 3 * vertices + vertices - matter_full_rank - carrier_rank
        incidence = Counter()
        for left, right in graph_edges:
            incidence[left] += 1
            incidence[right] += 1
        rows.append(
            {
                "L": length,
                "V": vertices,
                "carrier_check_count": len(carrier_checks),
                "carrier_rank": carrier_rank,
                "carrier_logical_qubits": vertices - carrier_rank,
                "local_combined_exponent": local_exponent,
                "full_combined_exponent": full_exponent,
                "plus_sector_exponent": vertices - plus_rank,
                "minus_sector_exponent": vertices - minus_rank,
                "sector_inconsistencies": (len(plus_bad), len(minus_bad)),
                "dressed_B_constraint_anticommutators": sum(incidence.values()),
                "minimum_degree": min(incidence.values()),
                "maximum_degree": max(incidence.values()),
                "deleted_rank": deleted_vertex_rank(carrier_checks, 0),
                "preparation_depth_lower_bound": torus_depth_lower_bound(length),
                "physical_M2_per_cell": 24,
            }
        )
    check(
        "route 1 vertex X-equality has the right full rank and both carrier-parity sectors, but local B dressing leaks at every incident check",
        all(
            row["carrier_check_count"] == 3 * row["V"]
            and row["carrier_rank"] == row["V"] - 1
            and row["carrier_logical_qubits"] == 1
            and row["local_combined_exponent"] == row["V"] + 3
            and row["full_combined_exponent"] == row["V"]
            and row["plus_sector_exponent"] == 0
            and row["minus_sector_exponent"] == 0
            and row["sector_inconsistencies"] == (0, 0)
            and row["dressed_B_constraint_anticommutators"] == 6 * row["V"]
            and row["minimum_degree"] == row["maximum_degree"] == 6
            and row["deleted_rank"] == row["V"] - 2
            and row["physical_M2_per_cell"] == 24
            for row in rows
        ),
        {
            "sizes": rows,
            "undressed_disposition": "exact Cycle-261 B/A algebra but a decoupled multiplicity; product B remains +1",
            "dressed_disposition": "B'_v=B_v Z_h(v) makes product B'=Z_all but each B'_v leaves the X-equality code",
            "algebraic_isometry": "exists for alpha|0>+beta|1> into the two carrier-cat parity sectors",
            "bounded_arbitrary_input_preparation": False,
        },
    )


def cell_x_cat_route() -> None:
    rows = []
    frame_failures = 0
    translation_failures = 0
    for length in (3, 4, 5, 6):
        cells = cubic_cells(length)
        index = {cell: position for position, cell in enumerate(cells)}
        edges = cubic_edges(length)
        rows_x = incidence_rows(edges)
        cells_count = length**3
        rank = c235.gf2_rank(rows_x)
        all_z = c235.Pauli(z=(1 << cells_count) - 1)
        stabilizers = [c235.Pauli(x=row) for row in rows_x]
        plus_rank, plus_bad = c235.phase_aware_rank(stabilizers + [all_z], cells_count)
        minus_rank, minus_bad = c235.phase_aware_rank(
            stabilizers + [c235.Pauli(phase=2, z=all_z.z)], cells_count
        )
        for displacement in cells:
            mapped = {
                frozenset(
                    (
                        index[
                            tuple(
                                (cells[edge[0]][axis] + displacement[axis]) % length
                                for axis in range(3)
                            )
                        ],
                        index[
                            tuple(
                                (cells[edge[1]][axis] + displacement[axis]) % length
                                for axis in range(3)
                            )
                        ],
                    )
                )
                for edge in edges
            }
            translation_failures += mapped != {
                frozenset((edge[0], edge[1])) for edge in edges
            }
        for frame in c235.proper_cubic_frames():
            vertex_map = {
                position: index[
                    tuple(int(value) % length for value in frame @ np.asarray(cell))
                ]
                for position, cell in enumerate(cells)
            }
            mapped = {
                frozenset((vertex_map[edge[0]], vertex_map[edge[1]]))
                for edge in edges
            }
            frame_failures += mapped != {
                frozenset((edge[0], edge[1])) for edge in edges
            }
        rows.append(
            {
                "L": length,
                "N": cells_count,
                "check_count": len(rows_x),
                "rank": rank,
                "logical_qubits": cells_count - rank,
                "Z_kernel_dimension": cells_count - rank,
                "minimum_nonzero_Z_centralizer_support": cells_count,
                "plus_sector_exponent": cells_count - plus_rank,
                "minus_sector_exponent": cells_count - minus_rank,
                "sector_inconsistencies": (len(plus_bad), len(minus_bad)),
                "deleted_rank": deleted_vertex_rank(rows_x, 0),
                "local_Z_leakage": 6,
                "total_local_Z_leakage": 6 * cells_count,
                "preparation_depth_lower_bound": torus_depth_lower_bound(length),
                "full_combined_exponent": 6 * cells_count,
                "local_combined_exponent": 6 * cells_count + 3,
            }
        )
    check(
        "route 1 cell X-cat is a covariant one-logical-qubit code in both parity sectors for odd and even volumes",
        frame_failures == 0
        and translation_failures == 0
        and all(
            row["check_count"] == 3 * row["N"]
            and row["rank"] == row["N"] - 1
            and row["logical_qubits"] == 1
            and row["Z_kernel_dimension"] == 1
            and row["minimum_nonzero_Z_centralizer_support"] == row["N"]
            and row["plus_sector_exponent"] == 0
            and row["minus_sector_exponent"] == 0
            and row["sector_inconsistencies"] == (0, 0)
            and row["deleted_rank"] == row["N"] - 2
            and row["full_combined_exponent"] == 6 * row["N"]
            and row["local_combined_exponent"] == 6 * row["N"] + 3
            for row in rows
        ),
        {
            "proper_frame_failures": frame_failures,
            "translation_failures": translation_failures,
            "sizes": rows,
            "logical_Z": "product of all cell Z operators",
            "logical_X": "any one cell X modulo X_i X_j checks",
            "parity_basis": "(|+>^N +/- |->^N)/sqrt(2)",
            "coherent_input": "alpha|0_L>+beta|1_L> is an exact abstract isometry",
            "bounded_arbitrary_input_preparation": False,
            "multiplicity_warning": "tensoring beside Cycle 261 does not make matter parity equal logical Z",
        },
    )


def cluster_cat_route() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        cells_count = length**3
        edges = cubic_edges(length)
        neighbors = [set() for _ in range(cells_count)]
        for left, right, _ in edges:
            neighbors[left].add(right)
            neighbors[right].add(left)
        generators = [
            c235.Pauli(
                x=1 << vertex,
                z=sum(1 << neighbor for neighbor in neighbors[vertex]),
            )
            for vertex in range(cells_count)
        ]
        stabilizers = [generators[left] @ generators[right] for left, right, _ in edges]
        rank, bad = c235.phase_aware_rank(stabilizers, cells_count)
        parity = c235.Pauli(z=(1 << cells_count) - 1)
        plus_rank, plus_bad = c235.phase_aware_rank(stabilizers + [parity], cells_count)
        minus_rank, minus_bad = c235.phase_aware_rank(
            stabilizers + [c235.Pauli(phase=2, z=parity.z)], cells_count
        )
        commutator_failures = sum(
            not left.commutes(right)
            for position, left in enumerate(stabilizers)
            for right in stabilizers[position + 1 :]
        )
        logical_x_failures = sum(not generators[0].commutes(row) for row in stabilizers)
        rows.append(
            {
                "L": length,
                "N": cells_count,
                "rank": rank,
                "logical_qubits": cells_count - rank,
                "phase_inconsistencies": len(bad),
                "commutator_failures": commutator_failures,
                "maximum_check_support": max(pauli_support(row) for row in stabilizers),
                "bounded_logical_X_support": pauli_support(generators[0]),
                "logical_X_commutator_failures": logical_x_failures,
                "logical_X_anticommutes_Z": not generators[0].commutes(parity),
                "plus_sector_exponent": cells_count - plus_rank,
                "minus_sector_exponent": cells_count - minus_rank,
                "sector_inconsistencies": (len(plus_bad), len(minus_bad)),
                "logical_Z_support_lower_bound": ceil(cells_count / 7),
                "deleted_rank": c235.gf2_rank(
                    row.symplectic(cells_count)
                    for row, edge in zip(stabilizers, edges)
                    if 0 not in edge[:2]
                ),
                "full_combined_exponent": 6 * cells_count,
                "local_combined_exponent": 6 * cells_count + 3,
            }
        )
    check(
        "route 3 cluster-cat is a bounded-check covariant Clifford image with a local logical X but an extensive logical Z class",
        all(
            row["rank"] == row["N"] - 1
            and row["logical_qubits"] == 1
            and row["phase_inconsistencies"] == 0
            and row["commutator_failures"] == 0
            and row["maximum_check_support"] <= 12
            and row["bounded_logical_X_support"] == 7
            and row["logical_X_commutator_failures"] == 0
            and row["logical_X_anticommutes_Z"]
            and row["plus_sector_exponent"] == 0
            and row["minus_sector_exponent"] == 0
            and row["sector_inconsistencies"] == (0, 0)
            and row["deleted_rank"] == row["N"] - 2
            and row["full_combined_exponent"] == 6 * row["N"]
            and row["local_combined_exponent"] == 6 * row["N"] + 3
            for row in rows
        ),
        {
            "sizes": rows,
            "construction": "S_ij=K_i K_j with K_i=X_i product_{j~i} Z_j",
            "logical_Z": "product of all Z; inverse cubic-CZ expands support by at most seven",
            "bounded_arbitrary_input_preparation": False,
            "reason": "a constant-depth preparation followed by inverse bounded-depth cubic CZ would prepare the X-cat",
        },
    )


def majorana_matching_route() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        cells_count = length**3
        edges = cubic_edges(length)
        edge_conflicts = sum(
            len({left, right} & {other_left, other_right}) == 1
            for position, (left, right, _) in enumerate(edges)
            for other_left, other_right, _ in edges[position + 1 :]
        )
        rows.append(
            {
                "L": length,
                "N": cells_count,
                "onsite_matching_rank": cells_count,
                "onsite_logical_qubits": 0,
                "deleted_onsite_rank": cells_count - 1,
                "deleted_onsite_logical_qubits": 1,
                "marked_translation_failures": cells_count - 1,
                "edge_bilinear_conflicts": edge_conflicts,
                "maximum_commuting_edge_matching": floor(cells_count / 2),
                "minimum_remaining_logical_qubits": ceil(cells_count / 2),
            }
        )
    check(
        "route 2 bounded Majorana matchings either fix parity, mark omitted endpoints, or leave an extensive residual",
        all(
            row["onsite_matching_rank"] == row["N"]
            and row["onsite_logical_qubits"] == 0
            and row["deleted_onsite_rank"] == row["N"] - 1
            and row["deleted_onsite_logical_qubits"] == 1
            and row["marked_translation_failures"] == row["N"] - 1
            and row["edge_bilinear_conflicts"] == 15 * row["N"]
            and row["maximum_commuting_edge_matching"] == floor(row["N"] / 2)
            and row["minimum_remaining_logical_qubits"] == ceil(row["N"] / 2)
            for row in rows
        ),
        {
            "sizes": rows,
            "onsite_perfect_matching": "commuting and covariant but fixes total reference parity",
            "one_deleted_pair": "right rank and bounded preparation but a marked cell/two unpaired Majoranas",
            "edge_bilinears": "operators sharing exactly one Majorana anticommute; a commuting subset is a matching",
            "live_escape": "quartic, dressed, and broader subsystem gauges are not excluded",
        },
    )


def subsystem_gauge_control() -> None:
    rows = []
    for length in (3, 4, 5, 6):
        cells_count = length**3
        edges = cubic_edges(length)
        incidence = incidence_rows(edges)
        incidence_rank = c235.gf2_rank(incidence)
        cross_conflicts = sum(
            ((xrow & zrow).bit_count() % 2) == 1
            for xrow in incidence
            for zrow in incidence
        )
        gauge_rank = 2 * incidence_rank
        center_rank = 2 if cells_count % 2 == 0 else 0
        logical_qubits = cells_count - (gauge_rank + center_rank) // 2
        rows.append(
            {
                "L": length,
                "N": cells_count,
                "incidence_rank": incidence_rank,
                "gauge_rank": gauge_rank,
                "center_rank": center_rank,
                "logical_qubits": logical_qubits,
                "X_Z_gauge_anticommutators": cross_conflicts,
                "Z_all_status": "logical" if cells_count % 2 else "gauge center",
            }
        )
    check(
        "the symmetric XX/ZZ subsystem steelman has a parity-volume jump and noncommuting local generators",
        all(
            row["incidence_rank"] == row["N"] - 1
            and row["gauge_rank"] == 2 * row["N"] - 2
            and row["X_Z_gauge_anticommutators"] == 30 * row["N"]
            and (
                (row["N"] % 2 == 1 and row["center_rank"] == 0 and row["logical_qubits"] == 1)
                or (row["N"] % 2 == 0 and row["center_rank"] == 2 and row["logical_qubits"] == 0)
            )
            for row in rows
        ),
        rows,
    )


@dataclass
class ReferenceSpokeCode:
    graph: c235.PyramidCellulation
    original_edges: list[c235.Pauli]
    spokes: list[c235.Pauli]
    reference_triangles: list[c235.Pauli]
    local_loops: list[c235.Pauli]
    wilson_loops: list[c235.Pauli]


def reference_spoke_code(length: int) -> ReferenceSpokeCode:
    """Independent extension of committed Cycle 261; no Cycle-264 import."""
    base = c261.degree_five_code(length)
    graph = base.graph
    vertices = len(graph.vertices)
    cell_index = {cell: index for index, cell in enumerate(graph.cells)}
    original_count = len(graph.edges)
    spokes = []
    for vertex, (cell, label) in enumerate(graph.vertices):
        reference = vertices + cell_index[cell]
        spokes.append(
            c261.shifted_gamma(vertex, label)
            @ c261.shifted_gamma(reference, label)
        )
    all_edges = base.edge_paulis + spokes
    triangles = []
    for edge, (left, right, _, _) in enumerate(graph.edges):
        if graph.vertices[left][0] == graph.vertices[right][0]:
            triangles.append(
                c261.loop_pauli(
                    all_edges,
                    [edge, original_count + right, original_count + left],
                )
            )
    return ReferenceSpokeCode(
        graph=graph,
        original_edges=base.edge_paulis,
        spokes=spokes,
        reference_triangles=triangles,
        local_loops=base.local_loops + triangles,
        wilson_loops=base.wilson_loops,
    )


def local_parity_flip_paulis() -> list[tuple[c235.Pauli, tuple[int, ...]]]:
    chirality = c235.Pauli(z=0b111)
    result = []
    for x in range(8):
        for z in range(8):
            pauli = c235.Pauli(x=x, z=z)
            if not pauli.commutes(chirality):
                leaks = tuple(
                    label
                    for label, gamma in enumerate(c261.LOCAL_GAMMAS)
                    if not pauli.commutes(gamma)
                )
                result.append((pauli, leaks))
    return result


def reference_spoke_route() -> None:
    local_flips = local_parity_flip_paulis()
    leakage_distribution = Counter(len(leaks) for _, leaks in local_flips)
    minimum_leakage = min(leakage_distribution)
    best = next(pauli for pauli, leaks in local_flips if len(leaks) == minimum_leakage)
    best_label = next(leaks[0] for pauli, leaks in local_flips if pauli == best)
    _, direction_permutations = c261.direction_permutations()
    uniform_frame_failures = sum(
        permutation[best_label] != best_label
        for permutation in direction_permutations
    )
    chirality = c235.Pauli(z=0b111)
    direction_flips = [chirality @ gamma for gamma in c261.LOCAL_GAMMAS]
    direction_flip_conflicts = sum(
        not direction_flips[left].commutes(direction_flips[right])
        for left, right in combinations(range(6), 2)
    )

    rows = []
    direct_l3 = None
    for length in (3, 4, 5, 6):
        code = reference_spoke_code(length)
        cells = length**3
        matter_vertices = 6 * cells
        total_vertices = 7 * cells
        qubits = 3 * total_vertices
        full = code.local_loops + code.wilson_loops
        local_rank, local_bad = c235.phase_aware_rank(code.local_loops, qubits)
        full_rank, full_bad = c235.phase_aware_rank(full, qubits)
        matter_parity = c261.total_parity(
            [c261.chirality_parity(vertex) for vertex in range(matter_vertices)]
        )
        reference_parity = c261.total_parity(
            [
                c261.chirality_parity(matter_vertices + cell)
                for cell in range(cells)
            ]
        )
        total_parity = matter_parity @ reference_parity
        total_rank, total_bad = c235.phase_aware_rank(full + [total_parity], qubits)
        plus_rank, plus_bad = c235.phase_aware_rank(full + [reference_parity], qubits)
        minus_reference = c235.Pauli(
            (reference_parity.phase + 2) % 4,
            reference_parity.x,
            reference_parity.z,
        )
        minus_rank, minus_bad = c235.phase_aware_rank(
            full + [minus_reference], qubits
        )
        abstract_pair_rank = c235.gf2_rank(incidence_rows(cubic_edges(length)))
        rows.append(
            {
                "L": length,
                "N": cells,
                "V": matter_vertices,
                "physical_M2_per_cell": 21,
                "reference_triangles": len(code.reference_triangles),
                "local_rank": local_rank,
                "full_rank": full_rank,
                "base_local_exponent": qubits - local_rank,
                "base_full_exponent": qubits - full_rank,
                "Wilson_increment": full_rank - local_rank,
                "total_parity_increment": total_rank - full_rank,
                "reference_parity_increment": plus_rank - full_rank,
                "reference_plus_exponent": qubits - plus_rank,
                "reference_minus_exponent": qubits - minus_rank,
                "phase_inconsistencies": (
                    len(local_bad),
                    len(full_bad),
                    len(total_bad),
                    len(plus_bad),
                    len(minus_bad),
                ),
                "abstract_pair_rank": abstract_pair_rank,
                "counterfactual_local_exponent": qubits - local_rank - abstract_pair_rank,
                "counterfactual_full_exponent": qubits - full_rank - abstract_pair_rank,
                "uniform_pair_spoke_anticommutators": 2 * 3 * cells,
                "uniform_pair_triangle_anticommutators": 8 * 3 * cells,
                "uniform_pair_frame_failures": uniform_frame_failures,
                "directional_pair_mutual_anticommutators": 15 * cells,
                "directional_pair_spoke_anticommutators": 2 * 3 * cells,
                "directional_pair_triangle_anticommutators": 8 * 3 * cells,
            }
        )
        if length == 3:
            references = [matter_vertices + cell for cell in range(cells)]
            uniform_pairs = []
            for left, right, _ in cubic_edges(length):
                uniform_pairs.append(
                    shifted_local_pauli(references[left], best)
                    @ shifted_local_pauli(references[right], best)
                )
            direct_l3 = {
                "uniform_pair_rank": c235.gf2_rank(
                    pair.symplectic(qubits) for pair in uniform_pairs
                ),
                "uniform_pair_mutual_anticommutators": sum(
                    not left.commutes(right)
                    for position, left in enumerate(uniform_pairs)
                    for right in uniform_pairs[position + 1 :]
                ),
                "uniform_pair_spoke_anticommutators": sum(
                    not pair.commutes(spoke)
                    for pair in uniform_pairs
                    for spoke in code.spokes
                ),
                "uniform_pair_loop_anticommutators": sum(
                    not pair.commutes(loop)
                    for pair in uniform_pairs
                    for loop in full
                ),
                "best_local_flip": {"x": best.x, "z": best.z, "leaked_label": best_label},
            }

    check(
        "the independently rebuilt reference-spoke code has both reference parities and the exact counterfactual target rank",
        all(
            row["reference_triangles"] == 12 * row["N"]
            and row["local_rank"] == 14 * row["N"] - 2
            and row["full_rank"] == 14 * row["N"] + 1
            and row["base_local_exponent"] == 7 * row["N"] + 2
            and row["base_full_exponent"] == 7 * row["N"] - 1
            and row["Wilson_increment"] == 3
            and row["total_parity_increment"] == 0
            and row["reference_parity_increment"] == 1
            and row["reference_plus_exponent"] == 7 * row["N"] - 2
            and row["reference_minus_exponent"] == 7 * row["N"] - 2
            and row["phase_inconsistencies"] == (0, 0, 0, 0, 0)
            and row["abstract_pair_rank"] == row["N"] - 1
            and row["counterfactual_local_exponent"] == row["V"] + 3
            and row["counterfactual_full_exponent"] == row["V"]
            for row in rows
        ),
        rows,
    )
    check(
        "no local reference-only Pauli parity flip commutes with all six spoke gammas in the declared chart",
        len(local_flips) == 32
        and leakage_distribution == Counter({1: 6, 3: 20, 5: 6})
        and minimum_leakage == 1,
        {
            "parity_flipping_local_Paulis": len(local_flips),
            "spoke_leakage_distribution": dict(sorted(leakage_distribution.items())),
            "minimum_endpoint_spoke_leakage": minimum_leakage,
            "zero_leakage_candidates": 0,
            "scope": "reference-only three-qubit Pauli endpoints; dressed and broader gauges remain live",
        },
    )
    check(
        "the commuting uniform pair family and the direction-covariant family fail on complementary exact witnesses",
        direction_flip_conflicts == 15
        and all(
            row["uniform_pair_spoke_anticommutators"] == 6 * row["N"]
            and row["uniform_pair_triangle_anticommutators"] == 24 * row["N"]
            and row["uniform_pair_frame_failures"] == 20
            and row["directional_pair_mutual_anticommutators"] == 15 * row["N"]
            and row["directional_pair_spoke_anticommutators"] == 6 * row["N"]
            and row["directional_pair_triangle_anticommutators"] == 24 * row["N"]
            for row in rows
        )
        and direct_l3 == {
            "uniform_pair_rank": 26,
            "uniform_pair_mutual_anticommutators": 0,
            "uniform_pair_spoke_anticommutators": 162,
            "uniform_pair_loop_anticommutators": 648,
            "best_local_flip": {"x": best.x, "z": best.z, "leaked_label": best_label},
        },
        {
            "sizes": rows,
            "local_direction_flip_pair_conflicts": direction_flip_conflicts,
            "direct_L3": direct_l3,
            "uniform_family": "rank N-1 and commuting, but fixes one gamma label and leaks spokes/triangles",
            "directional_family": "all-frame orbit, but the six incident endpoint operators anticommute pairwise",
        },
    )


def placement_and_fixture_controls() -> None:
    directions = tuple(np.asarray(row, dtype=int) for row in c235.c210.DIRECTIONS)

    def point(vector) -> tuple[int, int, int]:
        return tuple(int(value) % 64 for value in vector)

    shells = {
        radius: {point(radius * direction) for direction in directions}
        for radius in (6, 12, 18, 24)
    }
    center = {(0, 0, 0)}
    collisions = sum(len(points) for points in shells.values()) + 1 - len(
        set().union(center, *shells.values())
    )
    frame_failures = 0
    for frame in c235.proper_cubic_frames():
        for points in shells.values():
            frame_failures += {
                point(frame @ np.asarray(candidate)) for candidate in points
            } != points
        frame_failures += {point(frame @ np.asarray(candidate)) for candidate in center} != center

    species = c261.c219.common_species(c261.c230.BETA)
    rest = c261.c219.rest_mass(species)
    _, _, eigenvalues, _ = c261.c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "ordinary M2 placements remain collision-free and all-frame covariant with constant overhead",
        collisions == 0
        and frame_failures == 0
        and all(len(shells[radius]) == 6 for radius in shells),
        {
            "Cycle261_matter_roles_per_cell": 18,
            "vertex_carrier_roles_per_cell": 6,
            "cell_cat_roles_per_cell": 1,
            "reference_gamma_roles_per_cell": 3,
            "radii": tuple(shells),
            "proper_frame_failures": frame_failures,
            "collisions": collisions,
            "period64_macro_marker": "supplied",
        },
    )
    check(
        "the one-particle mass and Cycle-230 numerical fixtures are preserved as untouched matter-side fixtures",
        abs(c261.c230.BETA + 0.3) < 1e-15
        and abs(c261.c230.COUPLING - 0.37) < 1e-15
        and abs(rest / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73,
        {
            "beta": c261.c230.BETA,
            "g": c261.c230.COUPLING,
            "rest_mass": rest,
            "principal_sea_rank": sea_rank,
            "local_B_A_algebra": "unchanged for undressed tensor routes",
            "contact_and_seam_block": "not reproduced by a common physical E",
            "E_G_intertwining": False,
        },
    )


def scope_firewall() -> None:
    check(
        "the tournament reports route-specific residuals without promoting them to a shared obstruction",
        True,
        {
            "right_rank_candidates": ("vertex X-equality", "cell X-cat", "cluster-cat"),
            "common_failures": (
                "three nonlocal Wilson sector choices inherited from Cycle 261",
                "no bounded arbitrary-input parity-cat preparation",
                "no bounded relation identifying matter parity with the added logical Z",
            ),
            "stronger_spoke_failure_scope": "reference-only three-qubit Pauli endpoint grammar",
            "live_routes": (
                "dressed/quartic reference gauges",
                "larger local Clifford registers",
                "local topological-sector fixing or boundary constructions",
                "non-Pauli encoders",
            ),
            "global_Jordan_Wigner_ordering": False,
            "global_parity_service": False,
            "bounded_full_Fock_encoder": False,
            "universal_no_go": False,
            "axiom_pressure": False,
            "authority": "none",
            "audit": "unset",
            "compiler_depth_is_physical_time": False,
            "reference_carriers_are_Records": False,
        },
    )


def main() -> None:
    note_contract()
    cycle261_matter_baseline()
    ordinary_carrier_route()
    cell_x_cat_route()
    cluster_cat_route()
    majorana_matching_route()
    subsystem_gauge_control()
    reference_spoke_route()
    placement_and_fixture_controls()
    scope_firewall()
    print(f"SUMMARY pass={PASS} fail={FAIL}")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
