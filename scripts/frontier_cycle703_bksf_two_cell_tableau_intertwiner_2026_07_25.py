#!/usr/bin/env python3
"""Exact two-cell BKSF stabilizer-tableau intertwiner for Cycle 703.

This runner closes the finite state-encoding seam left by the local-Gauss
runner.  It constructs the smallest connected graph containing two complete
six-matter-plus-reference cells, fixes a fundamental-cycle character and one
independent local-D character, and completes the resulting 12-logical-qubit
code to a canonical Clifford tableau.  All checks use GF(2) Pauli algebra;
no dense 2**38 edge-qubit matrix or state vector is formed.

The tableau is also deliberately *not* advertised as a bounded-depth local
preparation.  Its deterministic symplectic completion is global Gaussian
elimination, so locality/depth scaling remains a separate compiler seam.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CYCLE703_BKSF_TWO_CELL_TABLEAU_INTERTWINER_NOTE_2026-07-25.md"
)
PASS = 0
FAIL = 0
REVERSE = (1, 0, 3, 2, 5, 4)
EXPECTED_TABLEAU_SHA256 = (
    "78be12ae5978315eb977ebc92ba81df2c7d10f0cd8c1d096ec5ed85248d5ae32"
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def pauli_product(rows) -> base.Pauli:
    result = base.Pauli()
    for row in rows:
        result = result @ row
    return result


def pauli_weight(row: base.Pauli) -> int:
    return (row.x | row.z).bit_count()


def is_hermitian(row: base.Pauli) -> bool:
    return row.phase % 2 == (row.x & row.z).bit_count() % 2


class TwoCellGraph(base.ReferenceGraph):
    """Two complete cells joined by one matter and one reference edge."""

    def __init__(self):
        self.length = 2
        self.periodic = False
        self.cells = ((0, 0, 0), (1, 0, 0))
        self.vertices: list[tuple[tuple[int, int, int], int]] = []
        self.vertex_index: dict[tuple[tuple[int, int, int], int], int] = {}
        for cell in self.cells:
            for mode in range(7):
                key = (cell, mode)
                self.vertex_index[key] = len(self.vertices)
                self.vertices.append(key)

        self.edges: list[tuple[int, int, str, tuple[int, int, int]]] = []
        self.edge_lookup: dict[frozenset[int], int] = {}
        self.internal_edge: dict[tuple[tuple[int, int, int], int, int], int] = {}
        self.spoke_edge: dict[tuple[tuple[int, int, int], int], int] = {}
        self.cross_edge: dict[tuple[tuple[int, int, int], int, int], int] = {}

        def add_edge(u: int, v: int, kind: str, owner) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate edge", u, v))
            edge = len(self.edges)
            self.edges.append((u, v, kind, owner))
            self.edge_lookup[key] = edge
            return edge

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if REVERSE[left] == right:
                    continue
                u = self.vertex_index[(cell, left)]
                v = self.vertex_index[(cell, right)]
                edge = add_edge(u, v, "octahedral", cell)
                self.internal_edge[(cell, left, right)] = edge
                self.internal_edge[(cell, right, left)] = edge
            reference = self.vertex_index[(cell, 6)]
            for mode in range(6):
                matter = self.vertex_index[(cell, mode)]
                self.spoke_edge[(cell, mode)] = add_edge(
                    reference, matter, "spoke", cell
                )

        left, right = self.cells
        matter_u = self.vertex_index[(left, 1)]
        matter_v = self.vertex_index[(right, 0)]
        reference_u = self.vertex_index[(left, 6)]
        reference_v = self.vertex_index[(right, 6)]
        self.cross_edge[(left, 0, 0)] = add_edge(
            matter_u, matter_v, "matter_stream", left
        )
        self.cross_edge[(left, 0, 1)] = add_edge(
            reference_u, reference_v, "reference_bond", left
        )

        self.incident: list[list[int]] = [[] for _ in self.vertices]
        for edge, (u, v, _, _) in enumerate(self.edges):
            self.incident[u].append(edge)
            self.incident[v].append(edge)
        for row in self.incident:
            row.sort()


def tree_path(
    source: int, target: int, parent: list[int | None]
) -> list[int]:
    source_chain = []
    vertex: int | None = source
    while vertex is not None:
        source_chain.append(vertex)
        vertex = parent[vertex]
    target_chain = []
    vertex = target
    while vertex is not None:
        target_chain.append(vertex)
        vertex = parent[vertex]
    source_positions = {vertex: index for index, vertex in enumerate(source_chain)}
    common = next(vertex for vertex in target_chain if vertex in source_positions)
    left = source_chain[: source_positions[common] + 1]
    right = target_chain[: target_chain.index(common)]
    return left + list(reversed(right))


def fundamental_loop_rows(graph: TwoCellGraph) -> list[base.Pauli]:
    adjacency: list[list[tuple[int, int]]] = [[] for _ in graph.vertices]
    for edge, (u, v, _, _) in enumerate(graph.edges):
        adjacency[u].append((v, edge))
        adjacency[v].append((u, edge))
    for row in adjacency:
        row.sort()

    parent: list[int | None] = [None] * len(graph.vertices)
    seen = {0}
    queue = deque([0])
    tree_edges: set[int] = set()
    while queue:
        u = queue.popleft()
        for v, edge in adjacency[u]:
            if v in seen:
                continue
            seen.add(v)
            parent[v] = u
            tree_edges.add(edge)
            queue.append(v)
    if len(seen) != len(graph.vertices):
        raise ValueError("two-cell graph is disconnected")

    rows = []
    for edge, (u, v, _, _) in enumerate(graph.edges):
        if edge not in tree_edges:
            rows.append(graph.loop_pauli(tree_path(u, v, parent)))
    return rows


def local_d(graph: TwoCellGraph, cell) -> base.Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(cell, mode)]) for mode in range(7)
    )


def logical_rows(
    graph: TwoCellGraph,
) -> tuple[list[base.Pauli], list[base.Pauli]]:
    logical_z = []
    logical_x = []
    for cell in graph.cells:
        reference = graph.vertex_index[(cell, 6)]
        for mode in range(6):
            matter = graph.vertex_index[(cell, mode)]
            logical_z.append(graph.B(matter))
            suffix = pauli_product(
                graph.B(graph.vertex_index[(cell, suffix_mode)])
                for suffix_mode in range(mode, 6)
            )
            logical_x.append(
                base.Pauli(phase=3) @ suffix @ graph.A(matter, reference)
            )
    return logical_z, logical_x


def swap_halves(vector: int, qubits: int) -> int:
    low_mask = (1 << qubits) - 1
    x = vector & low_mask
    z = vector >> qubits
    return z | (x << qubits)


def symplectic(left: int, right: int, qubits: int) -> int:
    low_mask = (1 << qubits) - 1
    lx = left & low_mask
    lz = left >> qubits
    rx = right & low_mask
    rz = right >> qubits
    return ((lx & rz).bit_count() + (lz & rx).bit_count()) & 1


def gf2_solve(equations: list[tuple[int, int]]) -> int:
    """Return the deterministic free-variables-zero solution."""

    pivots: dict[int, tuple[int, int]] = {}
    for original_mask, original_rhs in equations:
        mask, rhs = original_mask, original_rhs & 1
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                previous_mask, previous_rhs = pivots[pivot]
                mask ^= previous_mask
                rhs ^= previous_rhs
            else:
                pivots[pivot] = (mask, rhs)
                break
        else:
            if rhs:
                raise ValueError("inconsistent GF(2) system")

    solution = 0
    for pivot in sorted(pivots):
        mask, rhs = pivots[pivot]
        known = (mask & solution).bit_count() & 1
        if rhs ^ known:
            solution |= 1 << pivot
    return solution


def complete_tableau(
    w_rows: list[base.Pauli], explicit_logical_x: list[base.Pauli], qubits: int
) -> list[base.Pauli]:
    w_vectors = [row.symplectic(qubits) for row in w_rows]
    v_rows = list(explicit_logical_x)
    for index in range(len(v_rows), qubits):
        equations = [
            (swap_halves(vector, qubits), int(index == column))
            for column, vector in enumerate(w_vectors)
        ]
        equations.extend(
            (swap_halves(row.symplectic(qubits), qubits), 0)
            for row in v_rows
        )
        vector = gf2_solve(equations)
        mask = (1 << qubits) - 1
        x = vector & mask
        z = vector >> qubits
        v_rows.append(base.Pauli(phase=(x & z).bit_count() & 1, x=x, z=z))
    return v_rows


@dataclass(frozen=True)
class TableauCoordinates:
    phase: int
    v_mask: int
    w_mask: int


def decode_full(
    row: base.Pauli,
    w_rows: list[base.Pauli],
    v_rows: list[base.Pauli],
    qubits: int,
) -> TableauCoordinates:
    vector = row.symplectic(qubits)
    v_mask = sum(
        symplectic(vector, w.symplectic(qubits), qubits) << index
        for index, w in enumerate(w_rows)
    )
    w_mask = sum(
        symplectic(vector, v.symplectic(qubits), qubits) << index
        for index, v in enumerate(v_rows)
    )
    reconstructed = pauli_product(
        v_rows[index] for index in range(qubits) if (v_mask >> index) & 1
    ) @ pauli_product(
        w_rows[index] for index in range(qubits) if (w_mask >> index) & 1
    )
    if reconstructed.x != row.x or reconstructed.z != row.z:
        raise ValueError("tableau coordinate reconstruction failed")
    return TableauCoordinates(
        phase=(row.phase - reconstructed.phase) % 4,
        v_mask=v_mask,
        w_mask=w_mask,
    )


def encode_full(
    coordinates: TableauCoordinates,
    w_rows: list[base.Pauli],
    v_rows: list[base.Pauli],
    qubits: int,
) -> base.Pauli:
    row = base.Pauli(phase=coordinates.phase)
    row = row @ pauli_product(
        v_rows[index]
        for index in range(qubits)
        if (coordinates.v_mask >> index) & 1
    )
    return row @ pauli_product(
        w_rows[index]
        for index in range(qubits)
        if (coordinates.w_mask >> index) & 1
    )


def local_gamma(state: tuple[int, ...], target: int):
    out = list(state)
    phase = -1 if sum(state[:target]) & 1 else 1
    out[target] ^= 1
    return tuple(out), phase


def local_a_action(bits: tuple[int, ...], mode: int):
    out, right_phase = local_gamma(bits, 6)
    out, left_phase = local_gamma(out, mode)
    # A_(mode,6)=-i gamma_mode gamma_6; the left gamma acts second.
    return out, -1j * left_phase * right_phase


def local_jw_x_action(bits: tuple[int, ...], mode: int):
    """Act with -i product_{k=mode}^5 B_k A_(mode,r) on seven modes."""

    out, a_phase = local_a_action(bits, mode)
    suffix_phase = -1 if sum(out[mode:6]) & 1 else 1
    return out, (-1j) * suffix_phase * a_phase


def local_jw_prefix_action(bits: tuple[int, ...], mode: int):
    """Act with A_(mode,r) product_{k<mode} B_k on seven modes."""

    prefix_phase = -1 if sum(bits[:mode]) & 1 else 1
    out, a_phase = local_a_action(bits, mode)
    return out, prefix_phase * a_phase


def pauli_action(row: base.Pauli, bits: int) -> tuple[int, complex]:
    amplitude = (1j) ** row.phase
    if (row.z & bits).bit_count() & 1:
        amplitude *= -1
    return bits ^ row.x, amplitude


def add_term_action(
    accumulator: dict[int, complex],
    row: base.Pauli,
    coefficient: complex,
    bits: int,
) -> None:
    out, amplitude = pauli_action(row, bits)
    accumulator[out] = accumulator.get(out, 0.0) + coefficient * amplitude


def normalized_action(action: dict[int, complex]) -> dict[int, complex]:
    return {key: value for key, value in action.items() if abs(value) > 1.0e-12}


def apply_c_action(
    bits: int, mode: int, creation: bool
) -> tuple[int, complex] | None:
    occupied = (bits >> mode) & 1
    if occupied == int(creation):
        return None
    phase = -1.0 if (bits & ((1 << mode) - 1)).bit_count() & 1 else 1.0
    return bits ^ (1 << mode), phase


def target_hop_action(bits: int, left: int, right: int) -> dict[int, complex]:
    """Build c_right^dagger c_left + c_left^dagger c_right directly."""

    action: dict[int, complex] = {}
    for annihilated, created in ((left, right), (right, left)):
        first = apply_c_action(bits, annihilated, False)
        if first is None:
            continue
        intermediate, first_phase = first
        second = apply_c_action(intermediate, created, True)
        if second is None:
            continue
        out, second_phase = second
        action[out] = action.get(out, 0.0) + first_phase * second_phase
    return normalized_action(action)


def target_fswap_action(bits: int, left: int, right: int) -> dict[int, complex]:
    """Second-quantize the transposition and count occupied inversions."""

    permutation = list(range(12))
    permutation[left], permutation[right] = right, left
    occupied = [mode for mode in range(12) if (bits >> mode) & 1]
    targets = [permutation[mode] for mode in occupied]
    inversions = sum(
        targets[first] > targets[second]
        for first in range(len(targets))
        for second in range(first + 1, len(targets))
    )
    out = sum(1 << target for target in targets)
    return {out: -1.0 if inversions & 1 else 1.0}


def decoded_logical_pauli(
    row: base.Pauli,
    w_rows: list[base.Pauli],
    v_rows: list[base.Pauli],
    qubits: int,
) -> tuple[base.Pauli, int]:
    coordinates = decode_full(row, w_rows, v_rows, qubits)
    if coordinates.v_mask >> 12:
        raise ValueError("operator leaks from the stabilizer code")
    logical = base.Pauli(
        phase=coordinates.phase,
        x=coordinates.v_mask & ((1 << 12) - 1),
        z=coordinates.w_mask & ((1 << 12) - 1),
    )
    return logical, coordinates.w_mask >> 12


def note_contract() -> None:
    text = " ".join(
        NOTE.read_text(encoding="utf-8").lower().replace("*", "").split()
    )
    required = (
        "38 edge qubits",
        "25 independent fundamental-loop constraints",
        "one independent local-d constraint",
        "12 logical matter qubits",
        "fixed +1 loop character",
        "no noncontractible wilson generator",
        "global gaussian elimination",
        "does not prove bounded-depth",
        "e_bksf",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure and primitive scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom conclusion",
        "authority: none",
        "audit: unset",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the scoped positive and N1-N8 boundary", not missing, missing)


def run() -> dict[str, object]:
    graph = TwoCellGraph()
    qubits = len(graph.edges)
    loops = fundamental_loop_rows(graph)
    d_left = local_d(graph, graph.cells[0])
    d_right = local_d(graph, graph.cells[1])
    stabilizers = loops + [d_left]
    logical_z, explicit_logical_x = logical_rows(graph)
    w_rows = logical_z + stabilizers

    graph_detail = {
        "vertices": len(graph.vertices),
        "edges": qubits,
        "cycle_rank": qubits - len(graph.vertices) + 1,
        "loop_rank": base.gf2_rank(row.symplectic(qubits) for row in loops),
        "stabilizer_rank": base.gf2_rank(
            row.symplectic(qubits) for row in stabilizers
        ),
        "logical_exponent": qubits
        - base.gf2_rank(row.symplectic(qubits) for row in stabilizers),
        "wilson_rank": 0,
    }
    check(
        "the smallest connected two-complete-cell graph has the exact 38-to-12 stabilizer capacity",
        graph_detail
        == {
            "vertices": 14,
            "edges": 38,
            "cycle_rank": 25,
            "loop_rank": 25,
            "stabilizer_rank": 26,
            "logical_exponent": 12,
            "wilson_rank": 0,
        }
        and base.stabilizer_phase_failures(stabilizers, qubits) == 0
        and all(
            left.commutes(right)
            for left in stabilizers
            for right in stabilizers
        )
        and all(is_hermitian(row) for row in stabilizers)
        and d_left @ d_right == base.Pauli(),
        graph_detail,
    )

    x_orientation_failures = 0
    prefix_expected_failures = 0
    prefix_plain_x_mismatches = 0
    for mode in range(6):
        for matter_bits in range(1 << 6):
            matter = tuple((matter_bits >> index) & 1 for index in range(6))
            extended = matter + (sum(matter) & 1,)
            out, phase = local_jw_x_action(extended, mode)
            target_matter = list(matter)
            target_matter[mode] ^= 1
            target = tuple(target_matter) + (sum(target_matter) & 1,)
            x_orientation_failures += out != target or abs(phase - 1.0) > 1.0e-12
            prefix_out, prefix_phase = local_jw_prefix_action(extended, mode)
            expected_prefix_phase = (-1j) * (
                -1.0 if sum(matter) & 1 else 1.0
            )
            prefix_expected_failures += (
                prefix_out != target
                or abs(prefix_phase - expected_prefix_phase) > 1.0e-12
            )
            prefix_plain_x_mismatches += (
                prefix_out != target or abs(prefix_phase - 1.0) > 1.0e-12
            )

    canonical_logical_failures = sum(
        int(not x.commutes(z)) != int(x_index == z_index)
        for x_index, x in enumerate(explicit_logical_x)
        for z_index, z in enumerate(logical_z)
    ) + sum(
        not left.commutes(right)
        for left in explicit_logical_x
        for right in explicit_logical_x
    ) + sum(
        not row.commutes(stabilizer)
        for row in logical_z + explicit_logical_x
        for stabilizer in stabilizers
    )
    stabilizer_rank = base.gf2_rank(
        row.symplectic(qubits) for row in stabilizers
    )
    logical_pair_rank = base.gf2_rank(
        row.symplectic(qubits)
        for row in stabilizers + logical_z + explicit_logical_x
    )
    logical_deletion_ranks = tuple(
        base.gf2_rank(
            row.symplectic(qubits)
            for index, row in enumerate(
                stabilizers + logical_z + explicit_logical_x
            )
            if index != deleted
        )
        for deleted in range(len(stabilizers), len(stabilizers) + 24)
    )
    check(
        "the logical basis is phase-oriented to twelve matter bits and cell-local reference parity",
        x_orientation_failures == 0
        and prefix_expected_failures == 0
        and prefix_plain_x_mismatches == 6 * (1 << 6)
        and canonical_logical_failures == 0
        and base.gf2_rank(row.symplectic(qubits) for row in w_rows) == qubits
        and logical_pair_rank - stabilizer_rank == 24
        and set(logical_deletion_ranks) == {logical_pair_rank - 1},
        {
            "independent_JW_columns": 6 * (1 << 6),
            "orientation_failures": x_orientation_failures,
            "prefix_decodes_as_minus_i_X_times_cell_Z_parity_failures": (
                prefix_expected_failures
            ),
            "prefix_is_not_plain_X_columns": prefix_plain_x_mismatches,
            "canonical_failures": canonical_logical_failures,
            "logical_XZ_rank_mod_stabilizers": logical_pair_rank
            - stabilizer_rank,
            "logical_row_delete_ranks": sorted(set(logical_deletion_ranks)),
            "max_logical_X_weight": max(map(pauli_weight, explicit_logical_x)),
            "max_logical_Z_weight": max(map(pauli_weight, logical_z)),
        },
    )

    v_rows = complete_tableau(w_rows, explicit_logical_x, qubits)
    w_vectors = [row.symplectic(qubits) for row in w_rows]
    v_vectors = [row.symplectic(qubits) for row in v_rows]
    canonical_failures = sum(
        symplectic(w_vectors[i], w_vectors[j], qubits)
        for i in range(qubits)
        for j in range(qubits)
    ) + sum(
        symplectic(v_vectors[i], v_vectors[j], qubits)
        for i in range(qubits)
        for j in range(qubits)
    ) + sum(
        symplectic(v_vectors[i], w_vectors[j], qubits) != int(i == j)
        for i in range(qubits)
        for j in range(qubits)
    )
    inverse_failures = 0
    for row in w_rows + v_rows:
        inverse_failures += encode_full(
            decode_full(row, w_rows, v_rows, qubits), w_rows, v_rows, qubits
        ) != row
    serialized_tableau = "\n".join(
        f"{kind}:{index}:{row.phase}:{row.x:010x}:{row.z:010x}"
        for kind, rows in (("W", w_rows), ("V", v_rows))
        for index, row in enumerate(rows)
    )
    tableau_digest = sha256(serialized_tableau.encode("ascii")).hexdigest()
    check(
        "the 76-row phase-aware Clifford tableau is canonical, full-rank, and exactly invertible",
        canonical_failures == 0
        and inverse_failures == 0
        and base.gf2_rank(w_vectors + v_vectors) == 2 * qubits
        and all(is_hermitian(row) for row in w_rows + v_rows)
        and tableau_digest == EXPECTED_TABLEAU_SHA256,
        {
            "canonical_failures": canonical_failures,
            "inverse_failures": inverse_failures,
            "symplectic_rank": base.gf2_rank(w_vectors + v_vectors),
            "tableau_sha256": tableau_digest,
            "max_destabilizer_weight": max(map(pauli_weight, v_rows[12:])),
        },
    )

    # The stream is cell-0 mode 1 -> cell-1 mode 0, with a parallel reference
    # edge.  These are exactly the two Pauli words in the dressed CAR hop.
    left, right = graph.cells
    u = graph.vertex_index[(left, 1)]
    v = graph.vertex_index[(right, 0)]
    ru = graph.vertex_index[(left, 6)]
    rv = graph.vertex_index[(right, 6)]
    core = graph.A(u, v) @ graph.A(ru, rv)
    spectator = pauli_product(
        graph.B(graph.vertex_index[(right, mode)]) for mode in range(1, 6)
    )
    hop_terms = (
        base.Pauli(phase=2) @ spectator @ core,
        spectator @ graph.B(u) @ graph.B(v) @ core,
    )
    fswap_terms = (graph.B(u), graph.B(v), *hop_terms)

    decoded_hop = [
        decoded_logical_pauli(row, w_rows, v_rows, qubits)[0]
        for row in hop_terms
    ]
    decoded_fswap = [
        decoded_logical_pauli(row, w_rows, v_rows, qubits)[0]
        for row in fswap_terms
    ]
    code_preservation_failures = sum(
        not row.commutes(stabilizer)
        for row in fswap_terms
        for stabilizer in stabilizers
    )
    tableau_inverse_operator_failures = sum(
        encode_full(
            decode_full(row, w_rows, v_rows, qubits), w_rows, v_rows, qubits
        ) != row
        for row in fswap_terms
    )

    hop_failures = 0
    fswap_failures = 0
    for bits in range(1 << 12):
        observed_hop: dict[int, complex] = {}
        for row in decoded_hop:
            add_term_action(observed_hop, row, 0.5, bits)
        hop_failures += normalized_action(observed_hop) != target_hop_action(
            bits, 1, 6
        )

        observed_fswap: dict[int, complex] = {}
        for row in decoded_fswap:
            add_term_action(observed_fswap, row, 0.5, bits)
        fswap_failures += normalized_action(observed_fswap) != target_fswap_action(
            bits, 1, 6
        )

    check(
        "tableau conjugation certifies E_BKSF U = U_phys E_BKSF for the dressed hop and FSWAP",
        hop_failures == 0
        and fswap_failures == 0
        and code_preservation_failures == 0
        and tableau_inverse_operator_failures == 0,
        {
            "logical_columns": 1 << 12,
            "hop_failures": hop_failures,
            "FSWAP_failures": fswap_failures,
            "code_preservation_failures": code_preservation_failures,
            "inverse_operator_failures": tableau_inverse_operator_failures,
            "physical_term_weights": tuple(map(pauli_weight, fswap_terms)),
            "dense_edge_matrix_shape_not_formed": (1 << qubits, 1 << qubits),
        },
    )

    onsite_failures = 0
    onsite_inverse_failures = 0
    onsite_rows = []
    for cell_index, cell in enumerate(graph.cells):
        for mode in range(6):
            logical_index = 6 * cell_index + mode
            physical_b = graph.B(graph.vertex_index[(cell, mode)])
            logical_b, stabilizer_mask = decoded_logical_pauli(
                physical_b, w_rows, v_rows, qubits
            )
            onsite_failures += logical_b != base.Pauli(z=1 << logical_index)
            onsite_failures += stabilizer_mask != 0
            onsite_rows.append(physical_b)
        for first, second in combinations(range(6), 2):
            physical_contact = graph.B(
                graph.vertex_index[(cell, first)]
            ) @ graph.B(graph.vertex_index[(cell, second)])
            logical_contact, _ = decoded_logical_pauli(
                physical_contact, w_rows, v_rows, qubits
            )
            expected = base.Pauli(
                z=(1 << (6 * cell_index + first))
                | (1 << (6 * cell_index + second))
            )
            onsite_failures += logical_contact != expected
            onsite_rows.append(physical_contact)
    for row in onsite_rows:
        onsite_inverse_failures += encode_full(
            decode_full(row, w_rows, v_rows, qubits), w_rows, v_rows, qubits
        ) != row
    check(
        "onsite B and B-contact terms conjugate exactly with zero leakage",
        onsite_failures == 0
        and onsite_inverse_failures == 0
        and all(
            row.commutes(stabilizer)
            for row in onsite_rows
            for stabilizer in stabilizers
        ),
        {
            "B_terms": 12,
            "onsite_contacts": 30,
            "decode_failures": onsite_failures,
            "inverse_failures": onsite_inverse_failures,
        },
    )

    onsite_coin_failures = 0
    onsite_coin_preservation_failures = 0
    onsite_coin_inverse_failures = 0
    onsite_coin_rows: list[base.Pauli] = []
    onsite_coin_edges = 0
    for cell_index, cell in enumerate(graph.cells):
        for first, second in combinations(range(6), 2):
            if REVERSE[first] == second:
                continue
            onsite_coin_edges += 1
            u_coin = graph.vertex_index[(cell, first)]
            v_coin = graph.vertex_index[(cell, second)]
            a_coin = graph.A(u_coin, v_coin)
            # -i B_u (1-B_u B_v) A_uv / 2, split into Pauli words.
            coin_terms = (
                base.Pauli(phase=3) @ graph.B(u_coin) @ a_coin,
                base.Pauli(phase=1) @ graph.B(v_coin) @ a_coin,
            )
            decoded_coin = [
                decoded_logical_pauli(row, w_rows, v_rows, qubits)[0]
                for row in coin_terms
            ]
            onsite_coin_rows.extend(coin_terms)
            onsite_coin_preservation_failures += sum(
                not row.commutes(stabilizer)
                for row in coin_terms
                for stabilizer in stabilizers
            )
            onsite_coin_inverse_failures += sum(
                encode_full(
                    decode_full(row, w_rows, v_rows, qubits),
                    w_rows,
                    v_rows,
                    qubits,
                )
                != row
                for row in coin_terms
            )
            logical_first = 6 * cell_index + first
            logical_second = 6 * cell_index + second
            for bits in range(1 << 12):
                observed_coin: dict[int, complex] = {}
                for row in decoded_coin:
                    add_term_action(observed_coin, row, 0.5, bits)
                onsite_coin_failures += normalized_action(
                    observed_coin
                ) != target_hop_action(bits, logical_first, logical_second)
    check(
        "all onsite octahedral coin generators conjugate to the independent CAR target",
        onsite_coin_edges == 24
        and onsite_coin_failures == 0
        and onsite_coin_preservation_failures == 0
        and onsite_coin_inverse_failures == 0,
        {
            "coin_edges": onsite_coin_edges,
            "logical_columns_per_edge": 1 << 12,
            "action_failures": onsite_coin_failures,
            "code_preservation_failures": onsite_coin_preservation_failures,
            "inverse_failures": onsite_coin_inverse_failures,
        },
    )

    full_rank = base.gf2_rank(row.symplectic(qubits) for row in stabilizers)
    loop_delete_ranks = [
        base.gf2_rank(
            row.symplectic(qubits)
            for index, row in enumerate(stabilizers)
            if index != deleted
        )
        for deleted in range(len(loops))
    ]
    d_delete_rank = base.gf2_rank(
        row.symplectic(qubits) for row in stabilizers[:-1]
    )
    redundant_d_rank = base.gf2_rank(
        row.symplectic(qubits) for row in loops + [d_left, d_right]
    )
    redundant_delete_ranks = tuple(
        base.gf2_rank(
            row.symplectic(qubits)
            for index, row in enumerate(loops + [d_left, d_right])
            if index != deleted
        )
        for deleted in (len(loops), len(loops) + 1)
    )
    check(
        "every selected loop and the selected independent D row is active, while the two-D presentation is redundant",
        full_rank == 26
        and set(loop_delete_ranks) == {25}
        and d_delete_rank == 25
        and redundant_d_rank == 26
        and redundant_delete_ranks == (26, 26),
        {
            "full_rank": full_rank,
            "loop_delete_ranks": sorted(set(loop_delete_ranks)),
            "independent_D_delete_rank": d_delete_rank,
            "two_D_rank": redundant_d_rank,
            "two_D_delete_ranks": redundant_delete_ranks,
        },
    )

    support = {
        "max_loop_weight": max(map(pauli_weight, loops)),
        "D_weight": pauli_weight(d_left),
        "max_logical_X_weight": max(map(pauli_weight, explicit_logical_x)),
        "max_logical_Z_weight": max(map(pauli_weight, logical_z)),
        "max_update_term_weight": max(
            map(pauli_weight, fswap_terms + tuple(onsite_coin_rows))
        ),
        "max_global_completion_destabilizer_weight": max(
            map(pauli_weight, v_rows[12:])
        ),
    }
    check(
        "local physical terms stay within the two-cell patch, distinct from global tableau completion",
        support["max_update_term_weight"] < qubits
        and support["max_logical_X_weight"] < qubits
        and support["max_global_completion_destabilizer_weight"] <= qubits,
        support,
    )

    note_contract()
    result = {
        "terminal": (
            "TWO_CELL_BKSF_TABLEAU_INTERTWINER_POSITIVE_"
            "SCALABLE_LOCAL_PREPARATION_OPEN"
        ),
        "graph": graph_detail,
        "tableau": {
            "rows": 2 * qubits,
            "sha256": tableau_digest,
            "inverse_generator_checks": 2 * qubits,
            "construction": "global_GF2_symplectic_completion",
            "bounded_depth_or_range_proved": False,
        },
        "intertwiner": {
            "logical_columns_checked_without_dense_edge_states": 1 << 12,
            "dressed_hop_exact": hop_failures == 0,
            "FSWAP_exact": fswap_failures == 0,
            "onsite_B_and_contacts_exact": onsite_failures == 0,
            "all_24_onsite_coin_edges_exact": onsite_coin_failures == 0,
            "zero_leakage_by_stabilizer_commutation": code_preservation_failures
            == 0,
        },
        "deletion": {
            "all_25_loop_rows_active": set(loop_delete_ranks) == {25},
            "selected_independent_D_active": d_delete_rank == 25,
            "all_D_presentation_has_one_redundancy": redundant_delete_ranks
            == (26, 26),
            "all_24_logical_XZ_rows_active_mod_stabilizers": set(
                logical_deletion_ranks
            )
            == {logical_pair_rank - 1},
        },
        "support": support,
        "pass": PASS,
        "fail": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"])
    return result


if __name__ == "__main__":
    outcome = run()
    raise SystemExit(0 if outcome["fail"] == 0 else 1)
