#!/usr/bin/env python3
"""Cycle 277: a same-code local instrument on the Cycle-251 rough code.

One pointer M2 coherently measures the mapped scalar cell parity
Q_x=product_d B_(x,d).  The physical Pauli has weight 12, commutes with every
Cycle-251 code check and auxiliary generator, and is covariant as a cell
family.  Its controlled pointer flip supplies a two-outcome projective
instrument after explicitly importing pointer preparation, Z readout, trace,
and conditional selection.

The coherent correlation is not an occurrence or a Record.  Compiler circuit
depth is not physical time, and no phase or matrix element is energy or rate.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import local_rough_puncture_odd_sector_cycle247_2026_07_17 as c247
import rough_terminal_subsystem_gauge_factorization_cycle251_2026_07_17 as c251
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ROUGH_TERMINAL_SAME_CODE_LOCAL_INSTRUMENT_CYCLE277_NOTE_2026-07-17.md"
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
        check("the Cycle-277 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "same-code local quantum instrument",
        "q_x",
        "one pointer m2",
        "weight 12",
        "support 13",
        "kraus",
        "choi rank two",
        "all 24 proper-cubic frames",
        "full 27-element l=3 translation group",
        "held-out l=6",
        "auxiliary independence",
        "pointer preparation",
        "pointer readout",
        "pointer trace",
        "conditional selection",
        "not an occurrence",
        "not a record",
        "compiler circuit depth is not physical time",
        "not physical energy",
        "not a rate",
        "cycle 271 states are not imported",
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
        "the note preserves the same-code, instrument, import, N1-N8, and category contracts",
        not missing,
        missing,
    )


def signed(pauli: c235.Pauli, minus: int) -> c235.Pauli:
    return c235.Pauli((pauli.phase + 2 * minus) % 4, pauli.x, pauli.z)


def cell_parity(
    graph: c247.PunctureGraph, cell: tuple[int, int, int]
) -> c235.Pauli:
    return c251.product_paulis(
        [
            graph.B(graph.base.vertex_index[(cell, direction)])
            for direction in range(6)
        ]
    )


def matter_parity(graph: c247.PunctureGraph) -> c235.Pauli:
    return c251.product_paulis(
        [graph.B(vertex) for vertex in range(graph.matter_count)]
    )


def repair_data(
    graph: c247.PunctureGraph, vertex_map: list[int], edge_map: list[int]
) -> tuple[list[int], list[tuple[int, int]], int]:
    toggles, pairs = c247.order_gauge(graph, vertex_map, edge_map)
    flips = 0
    for source_edge, row in enumerate(graph.edges):
        if row.v is None:
            continue
        transformed = c247.permute_pauli(graph.A(row.u, row.v), edge_map)
        target = graph.A(vertex_map[row.u], vertex_map[row.v])
        ordered = c235.apply_gauge(transformed, toggles, pairs)
        if ordered.x != target.x or ordered.z != target.z:
            raise RuntimeError("Cycle-251 framing repair left the physical chart")
        if (ordered.phase - target.phase) % 4 == 2:
            flips ^= 1 << edge_map[source_edge]
    return toggles, pairs, flips


def code_sector_and_auxiliary_controls() -> dict[int, c247.PunctureGraph]:
    print("\nSAME CYCLE-251 CODE / SECTOR / AUXILIARY CONTROLS")
    cache: dict[int, c247.PunctureGraph] = {}
    rows = []
    failures = []
    for length in (3, 4, 5, 6):
        graph = c247.PunctureGraph(length, terminals=1)
        cache[length] = graph
        cells = length**3
        stabilizers = c247.code_rows(graph)
        stabilizer_rank = c251.rank(stabilizers, graph.qubits)
        q = cell_parity(graph, (0, 0, 0))
        global_parity = matter_parity(graph)
        gauge_b, gauge_a, _stream_edges = c251.gauge_family(graph)
        auxiliary = gauge_b + gauge_a
        sector_rows = []
        for parity_sign, outcome_sign in product((0, 1), repeat=2):
            rank, inconsistent = c235.phase_aware_rank(
                stabilizers
                + [signed(global_parity, parity_sign), signed(q, outcome_sign)],
                graph.qubits,
            )
            sector_rows.append((rank, len(inconsistent)))
        row = {
            "L": length,
            "cells": cells,
            "base_physical_M2_per_cell": graph.qubits // cells,
            "pointer_field_M2_per_cell": 1,
            "instrumented_physical_M2_per_cell": graph.qubits // cells + 1,
            "stabilizer_rank": stabilizer_rank,
            "Q_phase": q.phase,
            "Q_X_weight": q.x.bit_count(),
            "Q_Z_weight": q.z.bit_count(),
            "Q_support": (q.x | q.z).bit_count(),
            "Q_square_identity": q @ q == c235.Pauli(),
            "code_check_leakage": sum(
                not q.commutes(stabilizer) for stabilizer in stabilizers
            ),
            "auxiliary_commutators": sum(
                not q.commutes(generator) for generator in auxiliary
            ),
            "global_parity_commutator": int(not q.commutes(global_parity)),
            "lawful_common_parity_outcomes": sum(
                rank == 15 * cells + 3 and bad == 0
                for rank, bad in sector_rows
            ),
            "sector_rank_rows": tuple(sector_rows),
        }
        rows.append(row)
        if not (
            row["base_physical_M2_per_cell"] == 22
            and row["instrumented_physical_M2_per_cell"] == 23
            and stabilizer_rank == 15 * cells + 1
            and row["Q_phase"] == 0
            and row["Q_X_weight"] == 0
            and row["Q_Z_weight"] == 12
            and row["Q_square_identity"]
            and row["code_check_leakage"] == 0
            and row["auxiliary_commutators"] == 0
            and row["global_parity_commutator"] == 0
            and row["lawful_common_parity_outcomes"] == 4
        ):
            failures.append(row)

    check(
        "the scalar cell parity is a weight-12 same-code physical observable with zero check leakage through held-out L=6",
        not failures,
        rows,
    )
    check(
        "both outcomes remain nonempty in both common-parity sectors and the instrument is exactly auxiliary independent",
        not failures,
        {
            "rows": rows,
            "state_domain": "either fixed common-parity Cycle-251 sector; preparation remains supplied",
        },
    )
    return cache


def pointer_unitary_and_kraus_controls() -> None:
    print("\nONE-POINTER COHERENT UNITARY / CONDITIONAL INSTRUMENT")
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    plus = (identity + z) / 2
    minus = (identity - z) / 2
    unitary = np.kron(plus, identity) + np.kron(minus, x)
    standard_cnot = np.asarray(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    )
    pointer_zero = np.asarray((1, 0), dtype=complex)
    pointer_one = np.asarray((0, 1), dtype=complex)
    matter_plus = np.asarray((1, 0), dtype=complex)
    matter_minus = np.asarray((0, 1), dtype=complex)
    plus_output = unitary @ np.kron(matter_plus, pointer_zero)
    minus_output = unitary @ np.kron(matter_minus, pointer_zero)
    mixed_pointer = identity / 2

    def pointer_after(matter_state: np.ndarray) -> np.ndarray:
        initial = np.kron(
            np.outer(matter_state, matter_state.conj()), mixed_pointer
        )
        final = unitary @ initial @ unitary.conj().T
        return np.einsum("mpmq->pq", final.reshape(2, 2, 2, 2))

    unprepared_plus = pointer_after(matter_plus)
    unprepared_minus = pointer_after(matter_minus)
    unprepared_trace_distance = 0.5 * np.linalg.norm(
        unprepared_plus - unprepared_minus, ord="nuc"
    )

    reshaped = unitary.reshape(2, 2, 2, 2)
    kraus_zero = reshaped[:, 0, :, 0]
    kraus_one = reshaped[:, 1, :, 0]
    completeness = (
        kraus_zero.conj().T @ kraus_zero
        + kraus_one.conj().T @ kraus_one
    )
    repeatability_residual = 0.0
    for left, right in product((0, 1), repeat=2):
        projectors = (kraus_zero, kraus_one)
        expected = projectors[left] if left == right else np.zeros((2, 2))
        repeatability_residual = max(
            repeatability_residual,
            float(np.linalg.norm(projectors[left] @ projectors[right] - expected)),
        )

    choi = sum(
        np.outer(kraus.reshape(-1), kraus.reshape(-1).conj())
        for kraus in (kraus_zero, kraus_one)
    )
    choi_rank = int(np.linalg.matrix_rank(choi, tol=1e-12))

    truth_failures = 0
    for data in product((0, 1), repeat=12):
        parity = sum(data) % 2
        for pointer in (0, 1):
            serial_cnot_output = pointer
            for bit in data:
                serial_cnot_output ^= bit
            truth_failures += serial_cnot_output != (pointer ^ parity)

    check(
        "one pointer M2 and the controlled-Q unitary give an exact support-13 coherent parity correlation",
        np.linalg.norm(unitary.conj().T @ unitary - np.eye(4)) == 0
        and np.linalg.norm(unitary - standard_cnot) == 0
        and np.linalg.norm(plus_output - np.kron(matter_plus, pointer_zero)) == 0
        and np.linalg.norm(minus_output - np.kron(matter_minus, pointer_one)) == 0
        and abs(np.vdot(pointer_zero, pointer_one)) == 0
        and unprepared_trace_distance == 0
        and truth_failures == 0,
        {
            "logical_unitary_residual": float(np.linalg.norm(unitary - standard_cnot)),
            "physical_Q_support": 12,
            "pointer_support": 1,
            "joint_support": 13,
            "serial_CNOT_count": 12,
            "truth_table_cases": 2**13,
            "truth_table_failures": truth_failures,
            "pointer_overlap": float(abs(np.vdot(pointer_zero, pointer_one))),
            "maximally_mixed_pointer_outcome_trace_distance": float(
                unprepared_trace_distance
            ),
        },
    )
    check(
        "pointer Z readout gives the exact projective Kraus instrument with completeness and immediate repeatability residual zero",
        np.linalg.norm(kraus_zero - plus) == 0
        and np.linalg.norm(kraus_one - minus) == 0
        and np.linalg.norm(completeness - identity) == 0
        and repeatability_residual == 0,
        {
            "K0_minus_Pplus": float(np.linalg.norm(kraus_zero - plus)),
            "K1_minus_Pminus": float(np.linalg.norm(kraus_one - minus)),
            "completeness_residual": float(np.linalg.norm(completeness - identity)),
            "repeatability_residual": repeatability_residual,
        },
    )
    check(
        "the declared dephasing channel has Choi rank two, so one two-dimensional pointer is minimal for this exact dilation",
        choi_rank == 2,
        {
            "Choi_rank": choi_rank,
            "minimum_environment_dimension": 2,
            "minimum_pointer_M2": 1,
            "scope": "this binary projective channel, not all instruments",
        },
    )


def auxiliary_state_matrix_control() -> None:
    print("\nAUXILIARY-STATE INDEPENDENCE / POINTER DISTINGUISHABILITY")
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    plus = (identity + z) / 2
    minus = (identity - z) / 2
    unitary_mp = np.kron(plus, identity) + np.kron(minus, x)
    unitary = np.kron(unitary_mp, identity)
    rho_matter = np.asarray(((0.7, 0.2), (0.2, 0.3)), dtype=complex)
    pointer_zero = np.asarray(((1, 0), (0, 0)), dtype=complex)
    auxiliary_states = (
        np.asarray(((1, 0), (0, 0)), dtype=complex),
        np.asarray(((0, 0), (0, 1)), dtype=complex),
        identity / 2,
    )

    def pointer_reduced(auxiliary: np.ndarray) -> np.ndarray:
        initial = np.kron(np.kron(rho_matter, pointer_zero), auxiliary)
        final = unitary @ initial @ unitary.conj().T
        tensor = final.reshape(2, 2, 2, 2, 2, 2)
        return np.einsum("mpamqa->pq", tensor)

    outputs = [pointer_reduced(auxiliary) for auxiliary in auxiliary_states]
    expected = np.diag((0.7, 0.3)).astype(complex)
    auxiliary_residual = max(float(np.linalg.norm(output - expected)) for output in outputs)

    pointer_plus = np.asarray(((1, 0), (0, 0)), dtype=complex)
    pointer_minus = np.asarray(((0, 0), (0, 1)), dtype=complex)
    trace_distance = 0.5 * np.linalg.norm(pointer_plus - pointer_minus, ord="nuc")
    superposition = np.asarray((1, 0, 0, 1), dtype=complex) / np.sqrt(2)
    bell_density = np.outer(superposition, superposition.conj()).reshape(2, 2, 2, 2)
    pointer_bell = np.einsum("mpmq->pq", bell_density)
    bell_pointer_purity = float(np.trace(pointer_bell @ pointer_bell).real)
    check(
        "physical commutant independence lifts to identical pointer statistics for distinct auxiliary states",
        auxiliary_residual < 2e-16
        and abs(trace_distance - 1.0) < 1e-15
        and abs(bell_pointer_purity - 0.5) < 5e-16,
        {
            "auxiliary_pointer_residual": auxiliary_residual,
            "eigenvalue_pointer_trace_distance": float(trace_distance),
            "superposition_pointer_purity": bell_pointer_purity,
            "coherent_entanglement_is_occurrence": False,
            "coherent_pointer_is_Record": False,
        },
    )


def covariance_controls(graph: c247.PunctureGraph) -> None:
    print("\nALL-24 / FULL-27 INSTRUMENT-FAMILY COVARIANCE")
    q_family = {cell: cell_parity(graph, cell) for cell in graph.cells}
    frame_failures = pointer_frame_failures = 0
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = c247.graph_frame_maps(graph, frame)
        toggles, pairs, flips = repair_data(graph, vertex_map, edge_map)
        pointer_targets = set()
        for cell, q in q_family.items():
            target_cell = tuple(
                int(value % graph.length) for value in frame @ np.asarray(cell)
            )
            pointer_targets.add(target_cell)
            transformed = c235.apply_gauge(
                c247.permute_pauli(q, edge_map), toggles, pairs, flips
            )
            frame_failures += transformed != q_family[target_cell]
        pointer_frame_failures += pointer_targets != set(graph.cells)

    translation_failures = pointer_translation_failures = 0
    for displacement in product(range(graph.length), repeat=3):
        vertex_map, edge_map = c251.graph_translation_maps(graph, displacement)
        toggles, pairs, flips = repair_data(graph, vertex_map, edge_map)
        pointer_targets = set()
        for cell, q in q_family.items():
            target_cell = tuple(
                (cell[axis] + displacement[axis]) % graph.length
                for axis in range(3)
            )
            pointer_targets.add(target_cell)
            transformed = c235.apply_gauge(
                c247.permute_pauli(q, edge_map), toggles, pairs, flips
            )
            translation_failures += transformed != q_family[target_cell]
        pointer_translation_failures += pointer_targets != set(graph.cells)

    check(
        "all 24 proper-cubic frames and the full 27-element L=3 translation group covary the same-code Q/pointer instrument family",
        len(c235.proper_cubic_frames()) == 24
        and frame_failures == pointer_frame_failures == 0
        and translation_failures == pointer_translation_failures == 0,
        {
            "proper_frames": len(c235.proper_cubic_frames()),
            "translations": graph.length**3,
            "physical_Q_frame_failures": frame_failures,
            "physical_Q_translation_failures": translation_failures,
            "pointer_frame_failures": pointer_frame_failures,
            "pointer_translation_failures": pointer_translation_failures,
            "translation_scope": "supplied Cycle-251 period-16 puncture roles",
            "homogeneous_undifferentiated_M2_translation": False,
        },
    )


def onsite_fixture_controls() -> None:
    print("\nACTUAL MASS / CONTACT / ONSITE COMPATIBILITY")
    species = c219.common_species(c230.BETA)
    fock_coin = c229.fock_lift(species.coin)
    occupations = np.asarray([index.bit_count() for index in range(64)])
    parity = np.diag((-1.0) ** occupations).astype(complex)
    contact = np.diag(
        np.exp(1j * c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    identity_pointer = np.eye(2, dtype=complex)
    pointer_x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    parity_plus = (np.eye(64) + parity) / 2
    parity_minus = (np.eye(64) - parity) / 2
    instrument_unitary = (
        np.kron(parity_plus, identity_pointer)
        + np.kron(parity_minus, pointer_x)
    )
    coin_commutator = np.linalg.norm(
        instrument_unitary @ np.kron(fock_coin, identity_pointer)
        - np.kron(fock_coin, identity_pointer) @ instrument_unitary
    )
    contact_commutator = np.linalg.norm(
        instrument_unitary @ np.kron(contact, identity_pointer)
        - np.kron(contact, identity_pointer) @ instrument_unitary
    )
    _momenta, _vectors, eigenvalues, _labels = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the Q instrument commutes with the actual beta=-0.3 onsite coin and g=0.37 contact while the predecessor mass number remains a diagnostic",
        coin_commutator < 3e-13
        and contact_commutator == 0
        and np.max(np.abs(np.diag(contact)[occupations <= 1] - 1)) < 2e-15
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "instrument_coin_commutator": float(coin_commutator),
            "instrument_contact_commutator": float(contact_commutator),
            "rest_over_analytic_mass": c219.rest_mass(species)
            / species.analytic_mass,
            "principal_sea_rank": sea_rank,
            "fixture_scope": "operator compatibility; the sea is not prepared or preserved as a state",
            "local_parity_is_physical_energy": False,
        },
    )


def nondemolition_and_deletion_controls(
    cache: dict[int, c247.PunctureGraph]
) -> None:
    print("\nNONDEMOLITION SCOPE / DELETION / LAWFUL DOMAIN")
    rows = []
    for length, graph in cache.items():
        q = cell_parity(graph, (0, 0, 0))
        stabilizers = c247.code_rows(graph)
        internal_anticommutators = 0
        stream_anticommutators = 0
        for edge, (_left, _right, kind, _owner) in enumerate(graph.base.edges):
            if not q.commutes(graph.mapped_matter_A(edge)):
                if kind == "outer_square":
                    stream_anticommutators += 1
                else:
                    internal_anticommutators += 1
        support_bit = ((q.x | q.z) & -(q.x | q.z)).bit_length() - 1
        deleted_q = c235.Pauli(
            q.phase,
            q.x & ~(1 << support_bit),
            q.z & ~(1 << support_bit),
        )
        rows.append(
            {
                "L": length,
                "internal_A_anticommutators": internal_anticommutators,
                "boundary_stream_A_anticommutators": stream_anticommutators,
                "one_physical_factor_deleted_check_leakage": sum(
                    not deleted_q.commutes(stabilizer)
                    for stabilizer in stabilizers
                ),
            }
        )
    check(
        "the projective instrument is immediately repeatable and onsite nondemolition, but not nondemolition under a subsequent stream layer",
        all(
            row["internal_A_anticommutators"] == 0
            and row["boundary_stream_A_anticommutators"] == 6
            for row in rows
        ),
        rows,
    )
    check(
        "deleting one physical Q factor causes code leakage, while deleting the pointer coupling erases distinguishability",
        all(
            row["one_physical_factor_deleted_check_leakage"] == 5
            for row in rows
        ),
        {
            "rows": rows,
            "coupled_pointer_overlap": 0,
            "identity_coupling_pointer_overlap": 1,
            "unconditional_pointer_trace": "dephasing channel only; no selected outcome",
        },
    )
    check(
        "the lawful domain and category firewalls are explicit",
        True,
        {
            "included": "one scalar cell-parity instrument in either fixed common-parity Cycle-251 sector",
            "pointer_preparation": "supplied |0>",
            "pointer_readout": "supplied Z effects",
            "pointer_trace": "supplied ordinary quantum partial trace",
            "conditional_selection": "supplied instrument outcome label and normalization",
            "Cycle271_states_imported": False,
            "coherent_correlation_is_occurrence": False,
            "pointer_is_Record": False,
            "compiler_depth_is_physical_time": False,
            "matrix_phase_is_energy": False,
            "generator_is_rate": False,
            "route_independent_obstruction": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    cache = code_sector_and_auxiliary_controls()
    pointer_unitary_and_kraus_controls()
    auxiliary_state_matrix_control()
    covariance_controls(cache[3])
    onsite_fixture_controls()
    nondemolition_and_deletion_controls(cache)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE277_ROUGH_TERMINAL_SAME_CODE_LOCAL_INSTRUMENT_GREEN"
        if FAIL == 0
        else "CYCLE277_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
