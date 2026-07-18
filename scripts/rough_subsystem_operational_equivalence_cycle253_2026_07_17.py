#!/usr/bin/env python3
"""Cycle 253: operational-equivalence audit of the Cycle-251 subsystem.

The runner separates three statements which must not be conflated:

1. states related by the auxiliary even-CAR commutant are exactly
   indistinguishable by the mapped matter-even algebra and its fixed update;
2. the same states are distinguished by bounded physical M2-algebra effects
   in the auxiliary commutant; and
3. the current Record axiom does not itself supply a measurement/readout
   instrument for those effects or a pure-state encoding isometry E.

All update, preparation, and twirling indices are algebraic/compiler
coordinates, never physical time.
"""

from __future__ import annotations

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
    "ROUGH_SUBSYSTEM_OPERATIONAL_EQUIVALENCE_CYCLE253_NOTE_2026-07-17.md"
)
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
SITE_RECORD = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md"
)
CYCLE251 = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ROUGH_TERMINAL_SUBSYSTEM_GAUGE_FACTORIZATION_CYCLE251_NOTE_2026-07-17.md"
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
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "restricted matter-even operational equivalence",
        "full bounded local m2 algebra",
        "bounded local physical m2 algebra effect",
        "only records are readable",
        "law-selected record category",
        "not automatically gauge",
        "pure-state isometry e",
        "weight 6",
        "weight 18",
        "held-out l=6",
        "mapped update invariance",
        "gauge twirl",
        "record instrument",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "time firewall",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the Cycle-253 note preserves its operational, N1-N8, and time contracts", not missing, missing)


def source_contract_controls() -> None:
    axioms = normalized(AXIOMS)
    site_record = normalized(SITE_RECORD)
    cycle251 = normalized(CYCLE251)
    axiom_phrases = (
        "the full one-site possibility domain has algebraic presentation m_2(c)",
        "no possibility is privileged",
        "only records are readable",
        "local observability",
        "physical-observable identification",
    )
    category_phrases = (
        "foundation-maximal site-record category",
        "law-selected record category",
        "it is not automatically gauge",
        "exact record-net closure is still required",
    )
    cycle_phrases = (
        "auxiliary even-car",
        "parity-locked",
        "full pauli commutant",
        "no bounded parity-sector identification",
        "no bounded state-preparation circuit",
    )
    check(
        "the current foundation supplies the M2 possibility net and Record readability but leaves observability bridges open",
        all(phrase in axioms for phrase in axiom_phrases),
        {phrase: phrase in axioms for phrase in axiom_phrases},
    )
    check(
        "the retained equivalence classification separates maximal-site and law-selected record categories",
        all(phrase in site_record for phrase in category_phrases),
        {phrase: phrase in site_record for phrase in category_phrases},
    )
    check(
        "Cycle 251 supplies an exact local commutant but not a bounded pure-state encoder",
        all(phrase in cycle251 for phrase in cycle_phrases),
        {phrase: phrase in cycle251 for phrase in cycle_phrases},
    )


def signed(pauli: c235.Pauli, eigenvalue: int) -> c235.Pauli:
    if eigenvalue not in (-1, 1):
        raise ValueError(eigenvalue)
    return pauli if eigenvalue == 1 else c235.Pauli((pauli.phase + 2) % 4, pauli.x, pauli.z)


def actual_code_distinguishers() -> None:
    print("\nACTUAL ROUGH-CODE LOCAL DISTINGUISHERS")
    rows = []
    for length in (3, 4, 5, 6):
        graph = c247.PunctureGraph(length, terminals=1)
        stabilizers = c247.code_rows(graph)
        matter = c251.matter_family(graph)
        gauge_b, gauge_a, stream_edges = c251.gauge_family(graph)
        stabilizer_rank = c251.rank(stabilizers, graph.qubits)
        first_edge = stream_edges[0]
        source, target, _, _ = graph.base.edges[first_edge]
        endpoint_cells = (
            graph.base.vertices[source][0],
            graph.base.vertices[target][0],
        )
        endpoint_indices = tuple(graph.cell_index[cell] for cell in endpoint_cells)
        rows.append(
            {
                "L": length,
                "N": length**3,
                "B_weight": max((row.x | row.z).bit_count() for row in gauge_b),
                "A_weight": max((row.x | row.z).bit_count() for row in gauge_a),
                "B_nontrivial": c251.rank(stabilizers + [gauge_b[0]], graph.qubits)
                == stabilizer_rank + 1,
                "A_nontrivial": c251.rank(stabilizers + [gauge_a[0]], graph.qubits)
                == stabilizer_rank + 1,
                "code_leakage": sum(
                    not auxiliary.commutes(row)
                    for auxiliary in gauge_b + gauge_a
                    for row in stabilizers
                ),
                "matter_commutators": sum(
                    not auxiliary.commutes(row)
                    for auxiliary in gauge_b + gauge_a
                    for row in matter
                ),
                "first_A_B_anticommutators": sum(
                    not gauge_a[0].commutes(row) for row in gauge_b
                ),
                "endpoint_indices": endpoint_indices,
            }
        )

    check(
        "bounded auxiliary B and A are nontrivial physical M2 algebra elements through held-out L=6",
        all(
            row["B_weight"] == 6
            and row["A_weight"] <= 18
            and row["B_nontrivial"]
            and row["A_nontrivial"]
            and row["code_leakage"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "the distinguishing algebra commutes with every mapped matter generator while each auxiliary hop flips exactly two local parities",
        all(
            row["matter_commutators"] == 0
            and row["first_A_B_anticommutators"] == 2
            for row in rows
        ),
        rows,
    )

    graph = c247.PunctureGraph(3, terminals=1)
    stabilizers = c247.code_rows(graph)
    matter = c251.matter_family(graph)
    gauge_b, gauge_a, stream_edges = c251.gauge_family(graph)
    stabilizer_rank = c251.rank(stabilizers, graph.qubits)
    first_edge = stream_edges[0]
    source, target, _, _ = graph.base.edges[first_edge]
    left_cell = graph.base.vertices[source][0]
    right_cell = graph.base.vertices[target][0]
    left = graph.cell_index[left_cell]
    right = graph.cell_index[right_cell]
    plus_rank, plus_inconsistent = c235.phase_aware_rank(
        stabilizers + [signed(gauge_b[left], 1)], graph.qubits
    )
    minus_rank, minus_inconsistent = c235.phase_aware_rank(
        stabilizers + [signed(gauge_b[left], -1)], graph.qubits
    )
    check(
        "both local auxiliary-parity outcomes define nonempty code sectors and a bounded auxiliary hop exchanges them",
        plus_rank == minus_rank == stabilizer_rank + 1
        and not plus_inconsistent
        and not minus_inconsistent
        and not gauge_a[0].commutes(gauge_b[left])
        and not gauge_a[0].commutes(gauge_b[right])
        and all(
            gauge_a[0].commutes(gauge_b[index])
            for index in range(len(gauge_b))
            if index not in (left, right)
        ),
        {
            "plus_sector_rank": plus_rank,
            "minus_sector_rank": minus_rank,
            "sector_phase_inconsistencies": (plus_inconsistent, minus_inconsistent),
            "distinguishing_effects": "(I +/- B_aux,x)/2",
            "expectation_gap": 2,
        },
    )

    weight_one = 0
    for qubit in range(graph.qubits):
        for x, z in (
            (1 << qubit, 0),
            (0, 1 << qubit),
            (1 << qubit, 1 << qubit),
        ):
            candidate = c235.Pauli(x=x, z=z)
            weight_one += all(candidate.commutes(row) for row in stabilizers + matter)

    cell = graph.cells[0]
    spokes = [graph.spoke_lookup[(cell, direction)] for direction in range(6)]
    spoke_only = []
    for word in range(1, 4**6):
        x = z = 0
        remaining = word
        for qubit in spokes:
            digit = remaining % 4
            remaining //= 4
            if digit in (1, 3):
                x |= 1 << qubit
            if digit in (2, 3):
                z |= 1 << qubit
        candidate = c235.Pauli(x=x, z=z)
        if all(candidate.commutes(row) for row in stabilizers + matter):
            spoke_only.append(candidate)
    check(
        "the tested single-site Pauli commutant is trivial while the six-spoke block has exactly the displayed B distinguisher",
        weight_one == 0 and spoke_only == [gauge_b[0]],
        {
            "weight_one_code_preserving_matter_commutant": weight_one,
            "nonidentity_six_spoke_commutant_count": len(spoke_only),
            "tested_resolution": "weight one and the full 4^6 spoke-only Pauli ansatz",
            "unclaimed": "a global minimum over every bounded mixed-face ansatz",
        },
    )


def paulis() -> tuple[np.ndarray, ...]:
    identity = np.eye(2, dtype=complex)
    x = np.asarray([[0, 1], [1, 0]], dtype=complex)
    y = np.asarray([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    return identity, x, y, z


def reduced_matter(state: np.ndarray, matter_dimension: int, gauge_dimension: int) -> np.ndarray:
    reshaped = state.reshape(matter_dimension, gauge_dimension)
    return reshaped @ reshaped.conj().T


def operational_equivalence_and_update_controls() -> None:
    print("\nRESTRICTED EQUIVALENCE / FULL-ALGEBRA DISTINCTION")
    species = c219.common_species(c230.BETA)
    coin = c229.fock_lift(species.coin)
    occupations = c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    contact = np.diag(
        np.exp(1j * c230.COUPLING * number * (number - 1) / 2)
    )
    update = contact @ coin

    rng = np.random.default_rng(253)
    matter_state = rng.normal(size=64) + 1j * rng.normal(size=64)
    matter_state[number % 2 == 1] = 0
    matter_state /= np.linalg.norm(matter_state)

    identity, x, y, z = paulis()
    gauge_zero = np.kron(np.asarray([1, 0]), np.asarray([1, 0])).astype(complex)
    gauge_one = np.kron(np.asarray([0, 1]), np.asarray([0, 1])).astype(complex)
    state_zero = np.kron(matter_state, gauge_zero)
    state_one = np.kron(matter_state, gauge_one)
    physical_update = np.kron(update, np.eye(4))
    gauge_flip = np.kron(np.eye(64), np.kron(x, x))
    gauge_parity_left = np.kron(np.eye(64), np.kron(z, identity))
    plus_effect = (np.eye(256) + gauge_parity_left) / 2

    reduced_zero = reduced_matter(state_zero, 64, 4)
    reduced_one = reduced_matter(state_one, 64, 4)
    updated_zero = physical_update @ state_zero
    updated_one = physical_update @ state_one
    updated_reduced_zero = reduced_matter(updated_zero, 64, 4)
    updated_reduced_one = reduced_matter(updated_one, 64, 4)
    expectation_zero = float(np.real(state_zero.conj() @ gauge_parity_left @ state_zero))
    expectation_one = float(np.real(state_one.conj() @ gauge_parity_left @ state_one))
    probability_zero = float(np.real(state_zero.conj() @ plus_effect @ state_zero))
    probability_one = float(np.real(state_one.conj() @ plus_effect @ state_one))
    updated_expectation_zero = float(
        np.real(updated_zero.conj() @ gauge_parity_left @ updated_zero)
    )
    updated_expectation_one = float(
        np.real(updated_one.conj() @ gauge_parity_left @ updated_one)
    )

    check(
        "auxiliary-related states have identical restricted matter-even density functionals before and after the fixed mapped update",
        np.linalg.norm(state_one - gauge_flip @ state_zero) == 0
        and np.linalg.norm(reduced_zero - reduced_one) < 2e-14
        and np.linalg.norm(updated_reduced_zero - updated_reduced_one) < 2e-14
        and np.linalg.norm(physical_update @ gauge_flip - gauge_flip @ physical_update) == 0,
        {
            "initial_restricted_residual": np.linalg.norm(reduced_zero - reduced_one),
            "updated_restricted_residual": np.linalg.norm(updated_reduced_zero - updated_reduced_one),
            "update_gauge_commutator": np.linalg.norm(
                physical_update @ gauge_flip - gauge_flip @ physical_update
            ),
        },
    )
    check(
        "a bounded auxiliary M2 effect distinguishes the same states perfectly and mapped update invariance preserves the distinction",
        abs(expectation_zero - 1) < 2e-14
        and abs(expectation_one + 1) < 2e-14
        and abs(probability_zero - 1) < 2e-14
        and abs(probability_one) < 2e-14
        and abs(updated_expectation_zero - expectation_zero) < 2e-14
        and abs(updated_expectation_one - expectation_one) < 2e-14
        and np.linalg.norm(
            physical_update @ gauge_parity_left
            - gauge_parity_left @ physical_update
        )
        == 0,
        {
            "B_expectations": (expectation_zero, expectation_one),
            "plus_effect_probabilities": (probability_zero, probability_one),
            "updated_B_expectations": (
                updated_expectation_zero,
                updated_expectation_one,
            ),
        },
    )

    gauge_paulis = tuple(
        np.kron(left, right)
        for left in (identity, x, y, z)
        for right in (identity, x, y, z)
    )
    density_zero = np.outer(state_zero, state_zero.conj())
    density_one = np.outer(state_one, state_one.conj())
    twirled_zero = np.zeros_like(density_zero)
    twirled_one = np.zeros_like(density_one)
    for gauge_pauli in gauge_paulis:
        physical = np.kron(np.eye(64), gauge_pauli)
        twirled_zero += physical @ density_zero @ physical.conj().T / 16
        twirled_one += physical @ density_one @ physical.conj().T / 16
    check(
        "an explicitly supplied gauge twirl erases the auxiliary distinction without changing the matter state",
        np.linalg.norm(twirled_zero - twirled_one) < 2e-14
        and np.linalg.norm(
            twirled_zero - np.kron(reduced_zero, np.eye(4) / 4)
        )
        < 2e-14,
        {
            "twirled_state_residual": np.linalg.norm(twirled_zero - twirled_one),
            "conditional_expectation_residual": np.linalg.norm(
                twirled_zero - np.kron(reduced_zero, np.eye(4) / 4)
            ),
            "twirl_status": "supplied operational quotient, not a framework axiom or pure isometry",
        },
    )


def covariance_controls() -> None:
    print("\nCOVARIANT DISTINGUISHER FAMILY")
    graph = c247.PunctureGraph(3, terminals=1)
    z_failures = x_failures = 0
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = c247.graph_frame_maps(graph, frame)
        toggles, pairs = c247.order_gauge(graph, vertex_map, edge_map)
        flips = 0
        for source_edge, row in enumerate(graph.edges):
            if row.v is None:
                continue
            transformed = c247.permute_pauli(graph.A(row.u, row.v), edge_map)
            target = graph.A(vertex_map[row.u], vertex_map[row.v])
            ordered = c235.apply_gauge(transformed, toggles, pairs)
            if ordered.x != target.x or ordered.z != target.z:
                x_failures += 1
            elif (ordered.phase - target.phase) % 4 == 2:
                flips ^= 1 << edge_map[source_edge]

        for cell in graph.cells:
            target_cell = tuple(
                int(value % graph.length) for value in frame @ np.asarray(cell)
            )
            transformed = c235.apply_gauge(
                c247.permute_pauli(c251.gauge_z(graph, cell), edge_map),
                toggles,
                pairs,
                flips,
            )
            z_failures += transformed != c251.gauge_z(graph, target_cell)

        for source, target, kind, _ in graph.base.edges:
            if kind != "outer_square":
                continue
            transformed = c235.apply_gauge(
                c247.permute_pauli(
                    c251.gauge_x_oriented(graph, source, target), edge_map
                ),
                toggles,
                pairs,
                flips,
            )
            expected = c251.gauge_x_oriented(
                graph, vertex_map[source], vertex_map[target]
            )
            x_failures += transformed != expected

    translation_failures = 0
    z_family = {c251.gauge_z(graph, cell) for cell in graph.cells}
    for axis in range(3):
        shifted = set()
        for cell in graph.cells:
            target = list(cell)
            target[axis] = (target[axis] + 1) % graph.length
            shifted.add(c251.gauge_z(graph, tuple(target)))
        translation_failures += shifted != z_family
    check(
        "the bounded distinguishing family is all-24-frame and coarse-translation covariant rather than a marked measurement port",
        len(c235.proper_cubic_frames()) == 24
        and z_failures == x_failures == translation_failures == 0,
        {
            "frames": len(c235.proper_cubic_frames()),
            "B_frame_failures": z_failures,
            "A_frame_failures": x_failures,
            "translation_family_failures": translation_failures,
            "scope": "coarse puncture roles; period-16 physical marker remains supplied",
        },
    )


def main() -> int:
    note_contract()
    source_contract_controls()
    actual_code_distinguishers()
    operational_equivalence_and_update_controls()
    covariance_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
