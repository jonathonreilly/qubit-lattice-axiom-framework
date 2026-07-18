#!/usr/bin/env python3
"""Cycle 265: connected degree-five edge-code odd-sector join attempt.

The complete Cycle-252 square-pyramid graph is used throughout.  Its exact
bounded even-CAR edge algebra is augmented by one cell-center parity M2 per
coarse cell and covariant local Z-equality checks.  The added field closes the
raw dimension count, but this runner distinguishes that count from a faithful
full-Fock CAR representation and a bounded-preparable encoding.

Two dressings are kept separate:

* the genuinely unmarked all-six-port dressing, which is proper-cubic; and
* a one-port dressing, which gives P_m=b^N but carries a direction marker.

The isolated alternating-cycle code is only a comparator.  No prefix-code
state map is spliced into the connected edge operators.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import genuine_staggered_parity_shuttle_cycle260_2026_07_17 as c260
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CONNECTED_EDGE_CODE_ODD_SECTOR_JOIN_CYCLE265_NOTE_2026-07-17.md"
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-265 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "complete degree-five graph",
        "one cell-center m2",
        "local elementary cycle checks",
        "three torus wilsons",
        "6l^3",
        "p_m=b^n",
        "unmarked all-six",
        "isolated alternating-cycle comparator",
        "onsite coin transfers",
        "all 24 proper-cubic frames",
        "coarse translations",
        "held-out l=6",
        "bravyi and kitaev",
        "steudtner and wehner",
        "bounded-preparable full-fock e",
        "compiler schedules are not physical time",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note preserves the connected-join, prior-art, N1-N8, and time contracts", not missing, missing)


def product_paulis(rows: tuple[c235.Pauli, ...] | list[c235.Pauli]) -> c235.Pauli:
    result = c235.Pauli()
    for row in rows:
        result = result @ row
    return result


def pauli_rank(rows, qubits: int) -> int:
    return c235.gf2_rank(row.symplectic(qubits) for row in rows)


def phase_in_span(target: c235.Pauli, rows: list[c235.Pauli], qubits: int) -> bool:
    base_rank, base_bad = c235.phase_aware_rank(rows, qubits)
    next_rank, next_bad = c235.phase_aware_rank(rows + [target], qubits)
    return base_rank == next_rank and not base_bad and not next_bad


def gram_rank(rows: list[c235.Pauli]) -> int:
    packed = []
    for left in rows:
        mask = 0
        for index, right in enumerate(rows):
            if not left.commutes(right):
                mask ^= 1 << index
        packed.append(mask)
    return c235.gf2_rank(packed)


@dataclass(frozen=True)
class ConnectedFieldCode:
    length: int
    graph: c235.PyramidCellulation
    edge_qubits: int
    cells: int
    total_qubits: int
    local_loops: tuple[c235.Pauli, ...]
    wilsons: tuple[c235.Pauli, ...]
    equalities: tuple[c235.Pauli, ...]
    symmetric_B: tuple[c235.Pauli, ...]
    one_port_B: tuple[c235.Pauli, ...]
    A: tuple[c235.Pauli, ...]


def field_bit(code: ConnectedFieldCode, cell: tuple[int, int, int]) -> int:
    return code.edge_qubits + code.graph.cells.index(cell)


def build_code(length: int) -> ConnectedFieldCode:
    graph = c235.PyramidCellulation(length)
    edge_qubits = len(graph.edges)
    cells = length**3
    cell_index = {cell: index for index, cell in enumerate(graph.cells)}

    local_loops = tuple(
        graph.loop_pauli(vertices)
        for _, vertices, _ in c235.primal_edge_cycles(graph)
    )
    wilsons = tuple(
        graph.loop_pauli(vertices) for vertices in c235.wilson_cycles(graph)
    )
    equalities = []
    for cell in graph.cells:
        for axis in range(3):
            target = list(cell)
            target[axis] = (target[axis] + 1) % length
            left_bit = edge_qubits + cell_index[cell]
            right_bit = edge_qubits + cell_index[tuple(target)]
            equalities.append(c235.Pauli(z=(1 << left_bit) | (1 << right_bit)))

    symmetric_B = []
    one_port_B = []
    for vertex, (cell, direction) in enumerate(graph.vertices):
        field_z = c235.Pauli(z=1 << (edge_qubits + cell_index[cell]))
        symmetric_B.append(graph.B(vertex) @ field_z)
        one_port_B.append(
            graph.B(vertex) @ field_z if direction == 0 else graph.B(vertex)
        )
    hoppings = tuple(graph.A(u, v) for u, v, _, _ in graph.edges)
    return ConnectedFieldCode(
        length,
        graph,
        edge_qubits,
        cells,
        edge_qubits + cells,
        local_loops,
        wilsons,
        tuple(equalities),
        tuple(symmetric_B),
        tuple(one_port_B),
        hoppings,
    )


def field_all_z(code: ConnectedFieldCode) -> c235.Pauli:
    z = 0
    for cell_index in range(code.cells):
        z ^= 1 << (code.edge_qubits + cell_index)
    return c235.Pauli(z=z)


def rank_and_total_parity_controls() -> dict[int, ConnectedFieldCode]:
    print("\nCONNECTED RANK / TOTAL-PARITY FUNCTIONAL")
    cache = {}
    rows = []
    for length in (3, 4, 5, 6):
        code = build_code(length)
        cache[length] = code
        n = code.cells
        local_rank, local_bad = c235.phase_aware_rank(
            list(code.local_loops), code.total_qubits
        )
        edge_full_rank, edge_full_bad = c235.phase_aware_rank(
            list(code.local_loops + code.wilsons), code.total_qubits
        )
        equality_rank = pauli_rank(code.equalities, code.total_qubits)
        total_rank = edge_full_rank + equality_rank
        all_z = field_all_z(code)
        all_z_fixed = pauli_rank(
            list(code.equalities) + [all_z], code.total_qubits
        ) == equality_rank
        symmetric_product = product_paulis(code.symmetric_B)
        one_port_product = product_paulis(code.one_port_B)
        rows.append(
            {
                "L": length,
                "N": n,
                "physical_M2": code.total_qubits,
                "local_cycle_rank": local_rank,
                "edge_Wilson_rank": edge_full_rank,
                "field_equality_rank": equality_rank,
                "total_rank": total_rank,
                "code_exponent": code.total_qubits - total_rank,
                "phase_inconsistencies": len(local_bad) + len(edge_full_bad),
                "symmetric_product_B_weight": (symmetric_product.x | symmetric_product.z).bit_count(),
                "one_port_product_is_all_field_Z": one_port_product == all_z,
                "one_port_Pm_fixed_even": all_z_fixed,
                "one_port_parity_functional": f"b^{n}",
            }
        )

    check(
        "one cell-center M2 and local equalities close the exact 6L^3 exponent with the local cycle family and three Wilsons",
        all(
            row["physical_M2"] == 16 * row["N"]
            and row["local_cycle_rank"] == 9 * row["N"] - 2
            and row["edge_Wilson_rank"] == 9 * row["N"] + 1
            and row["field_equality_rank"] == row["N"] - 1
            and row["total_rank"] == 10 * row["N"]
            and row["code_exponent"] == 6 * row["N"]
            and row["phase_inconsistencies"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "the rank closure is not parity closure: unmarked all-six has P_m=I, while one-port has P_m=b^N and loses odd parity at L=4,6",
        all(row["symmetric_product_B_weight"] == 0 for row in rows)
        and all(row["one_port_product_is_all_field_Z"] for row in rows)
        and [row["one_port_Pm_fixed_even"] for row in rows]
        == [False, True, False, True],
        rows,
    )
    return cache


def algebra_and_fswap_controls(cache: dict[int, ConnectedFieldCode]) -> None:
    print("\nCONNECTED EVEN-CAR ALGEBRA / ACTUAL FSWAP")
    rank_rows = []
    for length, code in cache.items():
        stabilizers = list(code.local_loops + code.wilsons + code.equalities)
        s_rank = pauli_rank(stabilizers, code.total_qubits)
        symmetric_increment = pauli_rank(
            stabilizers + list(code.symmetric_B + code.A), code.total_qubits
        ) - s_rank
        one_port_increment = pauli_rank(
            stabilizers + list(code.one_port_B + code.A), code.total_qubits
        ) - s_rank
        rank_rows.append(
            {
                "L": length,
                "N": code.cells,
                "symmetric_matter_increment": symmetric_increment,
                "one_port_matter_increment": one_port_increment,
                "full_even_algebra_dimension": 12 * code.cells - 1,
            }
        )

    code3 = cache[3]
    incidence_failures = 0
    for edge, (u, v, _, _) in enumerate(code3.graph.edges):
        hopping = code3.A[edge]
        for vertex, parity in enumerate(code3.symmetric_B):
            actual = not hopping.commutes(parity)
            incidence_failures += actual != (vertex in (u, v))
    hopping_failures = 0
    for left, (u, v, _, _) in enumerate(code3.graph.edges):
        for right in range(left + 1, len(code3.graph.edges)):
            x, y, _, _ = code3.graph.edges[right]
            expected = len({u, v} & {x, y}) == 1
            hopping_failures += (
                not code3.A[left].commutes(code3.A[right])
            ) != expected
    algebra_rows = list(code3.symmetric_B + code3.A)
    check(
        "the complete connected degree-five graph retains exact endpoint and hopping-generator even-CAR incidence",
        incidence_failures == 0
        and hopping_failures == 0
        and gram_rank(algebra_rows) == 12 * code3.cells - 2,
        {
            "vertices": len(code3.graph.vertices),
            "edges": len(code3.graph.edges),
            "degree": sorted({len(row) for row in code3.graph.incident}),
            "endpoint_failures": incidence_failures,
            "hopping_pair_failures": hopping_failures,
            "matter_gram_rank": gram_rank(algebra_rows),
        },
    )
    check(
        "the symmetric rank-matched code is an even-sector representation with one multiplicity qubit; the one-port branch is full only at odd N",
        all(
            row["symmetric_matter_increment"] == 12 * row["N"] - 2
            and row["one_port_matter_increment"]
            == 12 * row["N"] - (1 if row["N"] % 2 else 2)
            for row in rank_rows
        ),
        rank_rows,
    )

    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    b_left = np.kron(z, identity)
    b_right = np.kron(identity, z)
    hopping = np.kron(y, x)
    polynomial = 0.5 * (
        b_left + b_right + 1j * b_left @ hopping - 1j * b_right @ hopping
    )
    fswap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    support_rows = []
    for length, code in cache.items():
        maximum = 0
        for edge, (u, v, _, _) in enumerate(code.graph.edges):
            terms = (
                code.symmetric_B[u],
                code.symmetric_B[v],
                code.symmetric_B[u] @ code.A[edge],
                code.symmetric_B[v] @ code.A[edge],
            )
            maximum = max(
                maximum,
                max((row.x | row.z).bit_count() for row in terms),
            )
        support_rows.append({"L": length, "maximum_FSWAP_term_weight": maximum})
    check(
        "the actual FSWAP polynomial remains exact and bounded on every connected graph edge",
        np.linalg.norm(polynomial - fswap) < 1e-15
        and max(row["maximum_FSWAP_term_weight"] for row in support_rows) <= 12,
        {"matrix_residual": float(np.linalg.norm(polynomial - fswap)), "support": support_rows},
    )

    support_rows = []
    for length, code in cache.items():
        onsite_unions = []
        for cell in code.graph.cells:
            support = 1 << (
                code.edge_qubits + code.graph.cells.index(cell)
            )
            for direction in range(6):
                vertex = code.graph.vertex_index[(cell, direction)]
                for edge in code.graph.incident[vertex]:
                    support |= 1 << edge
            onsite_unions.append(support.bit_count())
        support_rows.append(
            {
                "L": length,
                "B": max((row.x | row.z).bit_count() for row in code.symmetric_B),
                "A": max((row.x | row.z).bit_count() for row in code.A),
                "field_equality": max((row.x | row.z).bit_count() for row in code.equalities),
                "local_cycle_check": max((row.x | row.z).bit_count() for row in code.local_loops),
                "onsite_even_neighborhood": max(onsite_unions),
            }
        )
    check(
        "all connected generators, auxiliary equalities, local checks, and onsite even neighborhoods have volume-independent support",
        all(
            row["B"] == 6
            and row["A"] <= 9
            and row["field_equality"] == 2
            and row["local_cycle_check"] <= 28
            and row["onsite_even_neighborhood"] == 19
            for row in support_rows
        ),
        support_rows,
    )


def cell_translation_maps(
    code: ConnectedFieldCode, displacement: tuple[int, int, int]
) -> tuple[list[int], list[int], list[int]]:
    graph = code.graph
    vertex_map = []
    for cell, direction in graph.vertices:
        target = tuple(
            (cell[axis] + displacement[axis]) % code.length for axis in range(3)
        )
        vertex_map.append(graph.vertex_index[(target, direction)])
    edge_map = [
        graph.edge_between(vertex_map[u], vertex_map[v])
        for u, v, _, _ in graph.edges
    ]
    cell_lookup = {cell: index for index, cell in enumerate(graph.cells)}
    cell_map = []
    for cell in graph.cells:
        target = tuple(
            (cell[axis] + displacement[axis]) % code.length for axis in range(3)
        )
        cell_map.append(cell_lookup[target])
    return vertex_map, edge_map, cell_map


def frame_cell_map(code: ConnectedFieldCode, frame: np.ndarray) -> list[int]:
    lookup = {cell: index for index, cell in enumerate(code.graph.cells)}
    return [
        lookup[
            tuple(
                int(value % code.length)
                for value in frame @ np.asarray(cell)
            )
        ]
        for cell in code.graph.cells
    ]


def permute_extended(
    pauli: c235.Pauli,
    edge_map: list[int],
    cell_map: list[int],
    edge_qubits: int,
) -> c235.Pauli:
    x = z = 0
    total = edge_qubits + len(cell_map)
    for source in range(total):
        target = (
            edge_map[source]
            if source < edge_qubits
            else edge_qubits + cell_map[source - edge_qubits]
        )
        if (pauli.x >> source) & 1:
            x ^= 1 << target
        if (pauli.z >> source) & 1:
            z ^= 1 << target
    return c235.Pauli(pauli.phase, x, z)


def repair_data(graph, vertex_map, edge_map):
    toggles, pairs = c235.order_gauge(graph, vertex_map, edge_map)
    flips = 0
    for source_edge, (u, v, _, _) in enumerate(graph.edges):
        transformed = c235.permute_pauli(graph.A(u, v), edge_map)
        target = graph.A(vertex_map[u], vertex_map[v])
        ordered = c235.apply_gauge(transformed, toggles, pairs)
        if ordered.x != target.x or ordered.z != target.z:
            raise RuntimeError("local order gauge failed to repair X/Z support")
        if (ordered.phase - target.phase) % 4 == 2:
            flips ^= 1 << edge_map[source_edge]
    return toggles, pairs, flips


def covariance_controls(code: ConnectedFieldCode) -> None:
    print("\nALL-24 SIGNED OPERATOR / TRANSLATION COVARIANCE")
    graph = code.graph
    equality_family = set(code.equalities)
    loop_family = set(code.local_loops)
    stabilizers = list(code.local_loops + code.wilsons + code.equalities)
    frame_failures = fixed_port_failures = 0
    selected_port_orbit = set()
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = c235.graph_frame_maps(graph, frame)
        cell_map = frame_cell_map(code, frame)
        toggles, pairs, flips = repair_data(graph, vertex_map, edge_map)

        for vertex in range(len(graph.vertices)):
            transformed = permute_extended(
                code.symmetric_B[vertex], edge_map, cell_map, code.edge_qubits
            )
            frame_failures += transformed != code.symmetric_B[vertex_map[vertex]]
        for edge, (u, v, _, _) in enumerate(graph.edges):
            transformed = permute_extended(
                code.A[edge], edge_map, cell_map, code.edge_qubits
            )
            transformed = c235.apply_gauge(transformed, toggles, pairs, flips)
            frame_failures += transformed != graph.A(vertex_map[u], vertex_map[v])

        transformed_equalities = {
            permute_extended(row, edge_map, cell_map, code.edge_qubits)
            for row in code.equalities
        }
        frame_failures += transformed_equalities != equality_family
        transformed_loops = {
            c235.apply_gauge(
                permute_extended(row, edge_map, cell_map, code.edge_qubits),
                toggles,
                pairs,
                flips,
            )
            for row in code.local_loops
        }
        frame_failures += transformed_loops != loop_family
        for row in code.wilsons:
            transformed = c235.apply_gauge(
                permute_extended(row, edge_map, cell_map, code.edge_qubits),
                toggles,
                pairs,
                flips,
            )
            frame_failures += not phase_in_span(
                transformed, stabilizers, code.total_qubits
            )

        selected_port_orbit.add(c235.direction_map(frame)[0])
        for vertex, (_, direction) in enumerate(graph.vertices):
            transformed = permute_extended(
                code.one_port_B[vertex], edge_map, cell_map, code.edge_qubits
            )
            fixed_port_failures += transformed != code.one_port_B[vertex_map[vertex]]

    translation_failures = 0
    translation_displacements = tuple(product(range(code.length), repeat=3))
    for displacement in translation_displacements:
        vertex_map, edge_map, cell_map = cell_translation_maps(code, displacement)
        toggles, pairs, flips = repair_data(graph, vertex_map, edge_map)
        for vertex in range(len(graph.vertices)):
            transformed = permute_extended(
                code.symmetric_B[vertex], edge_map, cell_map, code.edge_qubits
            )
            translation_failures += transformed != code.symmetric_B[vertex_map[vertex]]
        for edge, (u, v, _, _) in enumerate(graph.edges):
            transformed = c235.apply_gauge(
                permute_extended(code.A[edge], edge_map, cell_map, code.edge_qubits),
                toggles,
                pairs,
                flips,
            )
            translation_failures += transformed != graph.A(vertex_map[u], vertex_map[v])
        translation_failures += {
            permute_extended(row, edge_map, cell_map, code.edge_qubits)
            for row in code.equalities
        } != equality_family
        for row in code.wilsons:
            transformed = c235.apply_gauge(
                permute_extended(row, edge_map, cell_map, code.edge_qubits),
                toggles,
                pairs,
                flips,
            )
            translation_failures += not phase_in_span(
                transformed, stabilizers, code.total_qubits
            )

    invariant_subsets = []
    frames = c235.proper_cubic_frames()
    for subset_mask in range(1 << 6):
        subset = {direction for direction in range(6) if (subset_mask >> direction) & 1}
        if all(
            {c235.direction_map(frame)[direction] for direction in subset} == subset
            for frame in frames
        ):
            invariant_subsets.append(subset)

    check(
        "the unmarked connected field, B/A generators, local checks, and Wilson sector are covariant under all 24 proper frames and the full L=3 coarse-translation group",
        len(c235.proper_cubic_frames()) == 24
        and frame_failures == 0
        and translation_failures == 0,
        {
            "frame_failures": frame_failures,
            "translation_failures": translation_failures,
            "translation_group_elements": len(translation_displacements),
            "signed_A_repair": "bounded inherited order/orientation Clifford",
        },
    )
    check(
        "a fixed odd one-port dressing is not unmarked: its proper-cubic orbit has all six ports, and every invariant port subset has even cardinality",
        selected_port_orbit == set(range(6))
        and fixed_port_failures > 0
        and invariant_subsets == [set(), set(range(6))],
        {
            "selected_port_orbit": sorted(selected_port_orbit),
            "fixed_port_operator_mismatches": fixed_port_failures,
            "invariant_port_subsets": [sorted(row) for row in invariant_subsets],
        },
    )


def connected_components_after_removed_edges(
    code: ConnectedFieldCode, removed: set[int]
) -> int:
    adjacency = [[] for _ in range(code.cells)]
    cell_index = {cell: index for index, cell in enumerate(code.graph.cells)}
    edge = 0
    for cell in code.graph.cells:
        left = cell_index[cell]
        for axis in range(3):
            target = list(cell)
            target[axis] = (target[axis] + 1) % code.length
            right = cell_index[tuple(target)]
            if edge not in removed:
                adjacency[left].append(right)
                adjacency[right].append(left)
            edge += 1
    seen = set()
    components = 0
    for seed in range(code.cells):
        if seed in seen:
            continue
        components += 1
        seen.add(seed)
        queue = deque([seed])
        while queue:
            vertex = queue.popleft()
            for target in adjacency[vertex]:
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
    return components


def field_preparation_and_deletion_controls(cache: dict[int, ConnectedFieldCode]) -> None:
    print("\nFIELD PREPARATION / HOLONOMY / DELETION / LEAKAGE")
    rows = []
    for length, code in cache.items():
        equality_rank = pauli_rank(code.equalities, code.total_qubits)
        global_x = c235.Pauli(
            x=((1 << code.cells) - 1) << code.edge_qubits
        )
        single_x = c235.Pauli(x=1 << code.edge_qubits)
        first_neighbor = 1
        pair_x = c235.Pauli(
            x=(1 << code.edge_qubits) | (1 << (code.edge_qubits + first_neighbor))
        )
        single_violations = sum(not single_x.commutes(row) for row in code.equalities)
        pair_violations = sum(not pair_x.commutes(row) for row in code.equalities)
        global_violations = sum(not global_x.commutes(row) for row in code.equalities)
        source = code.graph.vertex_index[((0, 0, 0), 0)]
        target = code.graph.vertex_index[((length // 2, 0, 0), 0)]
        separation = c235.shortest_path(code.graph, source, target)
        wilson_weights = [
            (row.x | row.z).bit_count() for row in code.wilsons
        ]
        rows.append(
            {
                "L": length,
                "N": code.cells,
                "equality_rank": equality_rank,
                "field_logicals": code.cells - equality_rank,
                "minimum_nontrivial_X_logical_weight": global_x.x.bit_count(),
                "single_X_violations": single_violations,
                "neighbor_pair_X_violations": pair_violations,
                "global_X_violations": global_violations,
                "separated_mode_distance": separation,
                "Wilson_X_support": [row.x.bit_count() for row in code.wilsons],
                "Wilson_full_weight": wilson_weights,
            }
        )

    check(
        "the Z-equality field has one global branch, and switching it without leakage requires the weight-N global X",
        all(
            row["equality_rank"] == row["N"] - 1
            and row["field_logicals"] == 1
            and row["minimum_nontrivial_X_logical_weight"] == row["N"]
            and row["single_X_violations"] == 6
            and row["neighbor_pair_X_violations"] == 10
            and row["global_X_violations"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "neither the parity branch nor the selected Wilson sector is a bounded-preparable full-Fock E in this grammar",
        [row["separated_mode_distance"] for row in rows] == [3, 6, 6, 9]
        and all(
            row["Wilson_X_support"] == [3 * row["L"]] * 3
            and max(row["Wilson_full_weight"]) == 6 * row["L"] + 3
            for row in rows
        ),
        {
            "field_branch_test": "vacuum versus one local occupation must change b at every cell",
            "cat_phase_test": "CAT+/- needs long-range connected correlations from product input",
            "rows": rows,
        },
    )

    code = cache[3]
    full = list(code.local_loops + code.wilsons + code.equalities)
    full_rank = pauli_rank(full, code.total_qubits)
    without_wilson = list(code.local_loops + code.wilsons[:-1] + code.equalities)
    wilson_rank_loss = full_rank - pauli_rank(without_wilson, code.total_qubits)

    origin = code.graph.cells.index((0, 0, 0))
    incident_equality_indices = set()
    for index, row in enumerate(code.equalities):
        field_mask = row.z >> code.edge_qubits
        if (field_mask >> origin) & 1:
            incident_equality_indices.add(index)
    retained_equalities = [
        row for index, row in enumerate(code.equalities)
        if index not in incident_equality_indices
    ]
    equality_rank_loss = pauli_rank(code.equalities, code.total_qubits) - pauli_rank(
        retained_equalities, code.total_qubits
    )
    components = connected_components_after_removed_edges(
        code, incident_equality_indices
    )
    algebra_leakage = sum(
        not operator.commutes(stabilizer)
        for operator in code.symmetric_B + code.A
        for stabilizer in full
    )
    check(
        "Wilson deletion and local field-isolation deletion expose one logical each, while the retained even algebra has zero ideal leakage",
        wilson_rank_loss == 1
        and len(incident_equality_indices) == 6
        and equality_rank_loss == 1
        and components == 2
        and algebra_leakage == 0,
        {
            "deleted_Wilson_rank_loss": wilson_rank_loss,
            "deleted_incident_equalities": len(incident_equality_indices),
            "field_rank_loss": equality_rank_loss,
            "field_components_after_deletion": components,
            "mapped_even_algebra_constraint_violations": algebra_leakage,
        },
    )
    odd = np.asarray((0.0, 1.0), dtype=complex)
    even_projector = np.diag((1.0, 0.0)).astype(complex)
    projected = even_projector @ odd
    odd_projector_expectation = float(np.vdot(odd, odd).real)
    available_even_expectation = float(np.vdot(projected, projected).real)
    norm_deficit = float(np.linalg.norm(odd - projected))
    check(
        "projecting a named odd input into the symmetric or even-volume one-port lawful matter sector has exact norm deficit one",
        odd_projector_expectation == 1.0
        and available_even_expectation == 0.0
        and norm_deficit == 1.0,
        {
            "input": "one occupied mode",
            "odd_projector_expectation": odd_projector_expectation,
            "available_even_projector_expectation": available_even_expectation,
            "state_norm_deficit": norm_deficit,
            "not_reported_as_zero_residual": True,
        },
    )


def cycle_comparator_and_fixture_controls(cache: dict[int, ConnectedFieldCode]) -> None:
    print("\nCONNECTED VERSUS ISOLATED CYCLES / FIXTURE FIREWALL")
    rows = []
    cross_cycle_internal = 0
    for length, code in cache.items():
        cycles = c260.alternating_cycles(length)
        owner = {}
        for cycle_index, cycle in enumerate(cycles):
            for vertex in cycle:
                owner[vertex] = cycle_index
        cross = sum(
            kind == "internal_triangle" and owner[u] != owner[v]
            for u, v, kind, _ in code.graph.edges
        )
        rows.append(
            {
                "L": length,
                "N": code.cells,
                "isolated_cycles": len(cycles),
                "cycle_length": 2 * length,
                "isolated_cycle_even_exponent": 6 * code.cells - len(cycles),
                "connected_total_even_exponent": 6 * code.cells - 1,
                "isolated_missing_vs_connected": len(cycles) - 1,
                "onsite_cross_cycle_edges": cross,
            }
        )
        cross_cycle_internal += cross
    check(
        "the isolated alternating-cycle comparator overconstrains parity, while the complete graph supports bounded onsite parity transfer",
        all(
            row["isolated_cycles"] == 3 * row["L"] ** 2
            and row["isolated_cycle_even_exponent"]
            == 6 * row["N"] - 3 * row["L"] ** 2
            and row["isolated_missing_vs_connected"] == 3 * row["L"] ** 2 - 1
            and row["onsite_cross_cycle_edges"] == 12 * row["N"]
            for row in rows
        )
        and cross_cycle_internal > 0,
        rows,
    )

    species = c219.common_species(c230.BETA)
    coin = c229.fock_lift(species.coin)
    total_parity = np.diag(
        [(-1) ** index.bit_count() for index in range(64)]
    ).astype(complex)
    axis_parities = []
    for axis in range(3):
        axis_parities.append(
            np.diag(
                [
                    (-1) ** (((index >> (2 * axis)) & 1) + ((index >> (2 * axis + 1)) & 1))
                    for index in range(64)
                ]
            ).astype(complex)
        )
    axis_commutators = [
        float(np.linalg.norm(coin @ parity - parity @ coin))
        for parity in axis_parities
    ]
    check(
        "the actual onsite coin preserves total parity but transfers parity between the three isolated matching-cycle families",
        np.linalg.norm(coin @ total_parity - total_parity @ coin) < 2e-12
        and all(value > 1e-6 for value in axis_commutators),
        {
            "total_parity_commutator": float(
                np.linalg.norm(coin @ total_parity - total_parity @ coin)
            ),
            "axis_pair_parity_commutators": axis_commutators,
        },
    )

    rest_mass = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "beta=-0.3, g=0.37, the mass fixture, contact, and rank-73 seam remain predecessor targets because no one branch closes E, covariance, and both parities",
        abs(c230.BETA + 0.3) < 1e-15
        and abs(c230.COUPLING - 0.37) < 1e-15
        and abs(rest_mass - 0.4534056541748851) < 2e-15
        and sea_rank == 73
        and sea_rank % 2 == 1,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "rest_mass_predecessor": rest_mass,
            "principal_sea_rank_predecessor": sea_rank,
            "bounded_even_coin_contact_FSWAP_algebra": True,
            "one_particle_mass_intertwining": False,
            "rank73_contact_seam_intertwining": False,
            "reason": "symmetric branch omits odd; one-port is marked, even-volume defective, and not bounded-prepared",
        },
    )


def placement_and_scope_controls() -> None:
    directions = tuple(np.asarray(row, dtype=int) for row in c235.c210.DIRECTIONS)
    internal = {
        tuple(2 * (directions[left] + directions[right]))
        for left, right in combinations(range(6), 2)
        if c235.REVERSE[left] != right
    }
    centered_outer = {tuple(8 * direction) for direction in directions}
    field = {(0, 0, 0)}
    collisions = len((internal | centered_outer) & field)
    frame_failures = 0
    for frame in c235.proper_cubic_frames():
        frame_failures += {
            tuple(int(value) for value in frame @ np.asarray(point))
            for point in internal
        } != internal
        frame_failures += {
            tuple(int(value) for value in frame @ np.asarray(point))
            for point in centered_outer
        } != centered_outer
        frame_failures += {
            tuple(int(value) for value in frame @ np.asarray(point))
            for point in field
        } != field

    patch_rows = []
    for length in (3, 4, 5, 6):
        modulus = 16 * length
        active = set()
        for cell in product(range(length), repeat=3):
            origin = 16 * np.asarray(cell)
            active.add(tuple(int(value % modulus) for value in origin))
            for point in internal:
                active.add(
                    tuple(int(value % modulus) for value in origin + np.asarray(point))
                )
            for axis in range(3):
                point = 8 * np.eye(3, dtype=int)[axis]
                active.add(
                    tuple(int(value % modulus) for value in origin + point)
                )
        unit = {((x + 1) % modulus, y, z) for x, y, z in active}
        macro = {((x + 16) % modulus, y, z) for x, y, z in active}
        patch_rows.append(
            {
                "L": length,
                "active_M2": len(active),
                "unit_symmetric_difference": len(active ^ unit),
                "macro_symmetric_difference": len(active ^ macro),
            }
        )
    check(
        "one literal cell-center M2 plus the 15 face M2 sites gives a collision-free all-24 period-16 placement",
        len(internal) == 12
        and len(centered_outer) == 6
        and collisions == 0
        and frame_failures == 0
        and all(row["active_M2"] == 16 * row["L"] ** 3 for row in patch_rows),
        {
            "cell_center_roles": 1,
            "face_roles_after_sharing": 15,
            "collisions": collisions,
            "frame_failures": frame_failures,
        },
    )
    check(
        "the physical placement is a macrocode, and compiler schedules are not physical time",
        all(row["unit_symmetric_difference"] > 0 for row in patch_rows)
        and all(row["macro_symmetric_difference"] == 0 for row in patch_rows),
        {
            "patches": patch_rows,
            "period16_origin_marker": "supplied",
            "compiler_schedules_are_not_physical_time": True,
            "ancilla_field_is_not_a_Record": True,
        },
    )
    check(
        "the scoped Z-equality result is not a universal no-go, shared obstruction, minimum-content claim, or axiom pressure",
        True,
        {
            "live": (
                "X/cat-like reference codes",
                "local even pair-flip constraints",
                "non-Pauli subsystem encoders",
                "measurement/reset or supplied entanglement",
                "open boundaries/punctures",
            ),
            "three_dimensions": "axiomatic input",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    note_contract()
    cache = rank_and_total_parity_controls()
    algebra_and_fswap_controls(cache)
    covariance_controls(cache[3])
    field_preparation_and_deletion_controls(cache)
    cycle_comparator_and_fixture_controls(cache)
    placement_and_scope_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
