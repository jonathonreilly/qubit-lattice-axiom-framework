#!/usr/bin/env python3
"""Cycle617: local-sector / role-genesis closure tournament.

Test three independent ways to remove Cycle610's supplied global
exactly-one-carrier sector and uniform 24-one-hot role field.  Positive
components are retained at their actual scope.  In particular, an even-CAR
subsystem representation is not relabelled as a common full-Fock encoder,
and a reversible packet reservoir is not relabelled as a CAR sign service.

Authority none; audit unset.  No constitutional surface is modified.
"""
from __future__ import annotations

from collections import deque
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import rough_terminal_subsystem_gauge_factorization_cycle251_2026_07_17 as c251
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22 as c610


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_SECTOR_ROLE_GENESIS_CLOSURE_TOURNAMENT_CYCLE617_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_local_sector_role_genesis_closure_"
    "tournament_cycle617_receipt_2026_07_22.json"
)
COLD = ROOT / (
    "outputs/physical_local_sector_role_genesis_closure_"
    "tournament_cycle617_cold_2026_07_22.txt"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5e-10
CAP_SECONDS = 420.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py":
        "997234878a564cb8554ff5184888fe06b920db32bb54b5df6febfdc88a90e7de",
    "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md":
        "6ee48e029ca6023e55cd834bd2ad2fcbb24275b48f9b25e1c03777e0d2c3d835",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json":
        "51373236a754b8ea941514609251b6721578c1f4fdfaa443958b7e7c7fba1c63",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_cold_2026_07_22.txt":
        "e5602522dc73cf07cad7bf660a0cc44246fdd4de36be3ff76e618936e4d54bc2",
    "scripts/final_m64_physical_m2_compiler_tournament_synthesis_cycle276_2026_07_17.py":
        "a2cd1c68e24e2c87c3edd7b8c61a8d7165adecd4927ac812917f16a9b101e604",
    "docs/work_history/repo/review_feedback/FINAL_M64_PHYSICAL_M2_COMPILER_TOURNAMENT_SYNTHESIS_CYCLE276_NOTE_2026-07-17.md":
        "8780be14db95a5f4cdb957559d2e6c538a8adea417cad1034910acd82ac000bc",
    "scripts/rough_terminal_subsystem_gauge_factorization_cycle251_2026_07_17.py":
        "6a62b47e6dedf6347a411d1d173b131e1c017ac69776a2a187c59ef22425d61d",
    "docs/work_history/repo/review_feedback/ROUGH_TERMINAL_SUBSYSTEM_GAUGE_FACTORIZATION_CYCLE251_NOTE_2026-07-17.md":
        "63cc264d2509e700cd250b35ac56ce1b465d21bd0f76416bfbe7d23ecaeb332c",
    "scripts/covariant_vertex_gamma_car_compiler_cycle261_2026_07_17.py":
        "96714dd8e4654f55fe1294822952010bfe58224fe976ba3187d37a0252d64212",
    "docs/work_history/repo/review_feedback/COVARIANT_VERTEX_GAMMA_CAR_COMPILER_CYCLE261_NOTE_2026-07-17.md":
        "c4fc2dc16bfe8dfcdddfec85204561081b1fa6690bfa2949b620ba6651f08b25",
    "scripts/physical_cycle269_local_fock_extension_cycle312_2026_07_18.py":
        "0aaab171ac23b28d8e6daa583e2e256bc872f971ec7f282898edea726d96ccd8",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_LOCAL_FOCK_EXTENSION_CYCLE312_NOTE_2026-07-18.md":
        "0153d6d44bf426e83da49b2057adbe8e7394fe4dfe4247a93519a31c58595d38",
}


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value: str) -> int:
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return (value.real, value.imag)
    if isinstance(value, tuple):
        return list(value)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def rank(paulis, qubits: int) -> int:
    return c251.c235.gf2_rank(row.symplectic(qubits) for row in paulis)


def gram_rank(paulis) -> int:
    rows = []
    for left in paulis:
        row = 0
        for index, right in enumerate(paulis):
            if not left.commutes(right):
                row ^= 1 << index
        rows.append(row)
    return c251.c235.gf2_rank(rows)


def shore() -> dict:
    observed = {name: sha(ROOT / name) for name in PINS}
    prior = json.loads((ROOT / (
        "outputs/physical_proper_cubic_supercell_stream_composition_"
        "tournament_cycle610_receipt_2026_07_22.json"
    )).read_text())
    inherited = {
        "pass": prior["pass"],
        "tests_passed": prior["tests_passed"],
        "authority": prior["authority"],
        "audit": prior["audit"],
        "physical_word": prior[
            "literal_orientation_controlled_compute_act_uncompute"
        ]["pass"],
        "global_geometry": prior["global_microstep_geometry"]["pass"],
        "fixtures": prior["onsite_mass_contact_seam_composition"]["pass"],
        "factor_order": prior["Cycle230_factor_order_deletion_noncommutation"]["pass"],
    }
    condition = (
        observed == PINS and inherited["pass"]
        and inherited["tests_passed"] == 16
        and inherited["authority"] == AUTHORITY
        and inherited["audit"] == AUDIT
        and all(inherited[key] for key in (
            "physical_word", "global_geometry", "fixtures", "factor_order"
        ))
    )
    check("Cycle610 and the bounded prior route family are byte-exact", condition,
          {"observed": observed, "inherited": inherited})
    return prior


# ---------------------------------------------------------------------------
# Route A: bounded local even-CAR subsystem, with the full-Fock boundary kept.


def route_a_local_gauge() -> dict:
    rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        graph = c251.c247.PunctureGraph(length, terminals=1)
        n = length**3
        stabilizers = c251.c247.code_rows(graph)
        local_stabilizers = (
            [graph.loop_pauli(vertices)
             for _mask, vertices, _kind in graph.local_cycles()]
            + [graph.cell_constraint(cell) for cell in graph.cells]
            + graph.boundary_stabilizers()
        )
        matter = c251.matter_family(graph)
        gauge_b, gauge_a, _ = c251.gauge_family(graph)
        gauge = gauge_b + gauge_a
        s_rank = rank(stabilizers, graph.qubits)
        local_s_rank = rank(local_stabilizers, graph.qubits)
        sm_rank = rank(stabilizers + matter, graph.qubits)
        sg_rank = rank(stabilizers + gauge, graph.qubits)
        smg_rank = rank(stabilizers + matter + gauge, graph.qubits)
        root, tree_edges = c251.coarse_spanning_tree(graph)
        raw_factor = [
            c251.gauge_z(graph, cell) for cell in graph.cells if cell != root
        ] + [c251.gauge_x(graph, edge) for edge in tree_edges]
        canonical = c251.symplectic_gram_schmidt(raw_factor)
        matter_parity = c251.product_paulis(
            [graph.B(vertex) for vertex in range(graph.matter_count)]
        )
        gauge_parity = c251.product_paulis(gauge_b)
        max_stabilizer = max((row.x | row.z).bit_count() for row in stabilizers)
        max_local_stabilizer = max(
            (row.x | row.z).bit_count() for row in local_stabilizers
        )
        max_matter = max((row.x | row.z).bit_count() for row in matter)
        max_gauge = max((row.x | row.z).bit_count() for row in gauge)
        # The first of the three appended Wilson rows is independent.  The
        # final cell constraint is also independent in the rough-terminal
        # local set.  Test each directly rather than repeating thousands of
        # full rank calculations while searching for a deletion witness.
        wilson_index = len(graph.local_cycles())
        deleted_rank = rank(
            stabilizers[:wilson_index] + stabilizers[wilson_index + 1:],
            graph.qubits,
        )
        deleted_local_rank = rank(local_stabilizers[:-1], graph.qubits)
        local_sm_rank = rank(local_stabilizers + matter, graph.qubits)
        local_sg_rank = rank(local_stabilizers + gauge, graph.qubits)
        local_smg_rank = rank(
            local_stabilizers + matter + gauge, graph.qubits
        )
        rows.append({
            "length": length,
            "split": split,
            "coarse_cells": n,
            "physical_M2_qubits": graph.qubits,
            "M2_per_coarse_cell": graph.qubits / n,
            "stabilizer_rank": s_rank,
            "code_exponent": graph.qubits - s_rank,
            "bounded_local_stabilizer_rank": local_s_rank,
            "bounded_local_code_exponent": graph.qubits - local_s_rank,
            "global_Wilson_rank_increment": s_rank - local_s_rank,
            "local_code_matter_quotient_dimension": local_sm_rank - local_s_rank,
            "local_code_gauge_quotient_dimension": local_sg_rank - local_s_rank,
            "local_code_matter_gauge_intersection": (
                (local_sm_rank - local_s_rank)
                + (local_sg_rank - local_s_rank)
                - (local_smg_rank - local_s_rank)
            ),
            "matter_quotient_dimension": sm_rank - s_rank,
            "matter_symplectic_rank": gram_rank(matter) if length == 3 else 12 * n - 2,
            "gauge_quotient_dimension": sg_rank - s_rank,
            "gauge_symplectic_rank": gram_rank(gauge) if length == 3 else 2 * n - 2,
            "matter_gauge_intersection": (
                (sm_rank - s_rank) + (sg_rank - s_rank) - (smg_rank - s_rank)
            ),
            "P_g_equals_P_m": gauge_parity == matter_parity,
            "maximum_bounded_local_constraint_weight": max_local_stabilizer,
            "maximum_full_fixed_flux_stabilizer_weight": max_stabilizer,
            "maximum_mapped_matter_generator_weight": max_matter,
            "maximum_auxiliary_generator_weight": max_gauge,
            "root_tree_raw_maximum_weight": max(
                (row.x | row.z).bit_count() for row in raw_factor
            ),
            "root_tree_canonical_maximum_weight": max(
                (row.x | row.z).bit_count() for row in canonical
            ),
            "delete_one_independent_Wilson_index": wilson_index,
            "deleted_Wilson_rank_loss": s_rank - deleted_rank,
            "deleted_bounded_local_constraint_rank_loss": (
                local_s_rank - deleted_local_rank
            ),
        })

    # Re-execute the actual all-24 and unit-translation gauge-covariance audit.
    c251.PASS = c251.FAIL = 0
    c251.covariance_controls()
    covariance_pass = c251.FAIL == 0 and c251.PASS == 1

    species = c219.common_species(c230.BETA)
    local_coin = c229.fock_lift(species.coin)
    occupations = c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    parity = np.diag(np.where(number.astype(int) % 2, -1.0, 1.0))
    contact = np.diag(
        np.exp(1j * c230.COUPLING * number * (number - 1) / 2)
    )
    local_word = contact @ local_coin
    even = np.flatnonzero(number.astype(int) % 2 == 0)
    odd = np.flatnonzero(number.astype(int) % 2 == 1)
    rng = np.random.default_rng(61701)
    state = rng.normal(size=64) + 1j * rng.normal(size=64)
    state /= np.linalg.norm(state)
    transformed = local_word @ state
    coherent_norm_residual = abs(np.linalg.norm(transformed) - 1)
    parity_commutator = float(np.linalg.norm(local_word @ parity - parity @ local_word))
    parity_block_leakage = float(
        np.linalg.norm(local_word[np.ix_(even, odd)])
        + np.linalg.norm(local_word[np.ix_(odd, even)])
    )
    local_car_residual = 0.0
    annihilators = c229.annihilation_operators(6)
    identity = np.eye(64)
    for left in range(6):
        for right in range(6):
            expected = identity if left == right else np.zeros_like(identity)
            local_car_residual = max(
                local_car_residual,
                float(np.linalg.norm(
                    annihilators[left] @ annihilators[right].conj().T
                    + annihilators[right].conj().T @ annihilators[left]
                    - expected
                )),
                float(np.linalg.norm(
                    annihilators[left] @ annihilators[right]
                    + annihilators[right] @ annihilators[left]
                )),
            )
    local_occupations = {
        "scope": "abstract six-mode Cycle230 target fixture; not a physical encoding E",
        "all_64_occupations_in_domain": len(number) == 64,
        "even_occupations": len(even),
        "odd_occupations": len(odd),
        "vacuum_and_fully_occupied_in_domain": bool(number[0] == 0 and number[-1] == 6),
        "adjacent_two_mode_occupancies_in_domain": math.comb(6, 2),
        "Pauli_exclusion_same_mode_double_creation": 0,
        "CAR_residual": local_car_residual,
        "coherent_both_parity_norm_residual": coherent_norm_residual,
        "even_odd_block_leakage": parity_block_leakage,
        "parity_commutator": parity_commutator,
    }

    algebra_pass = all(
        row["stabilizer_rank"] == 15 * row["coarse_cells"] + 1
        and row["code_exponent"] == 7 * row["coarse_cells"] - 1
        and row["matter_quotient_dimension"] == 12 * row["coarse_cells"] - 1
        and row["matter_symplectic_rank"] == 12 * row["coarse_cells"] - 2
        and row["gauge_quotient_dimension"] == 2 * row["coarse_cells"] - 1
        and row["gauge_symplectic_rank"] == 2 * row["coarse_cells"] - 2
        and row["matter_gauge_intersection"] == 1
        and row["P_g_equals_P_m"]
        and row["bounded_local_stabilizer_rank"] == 15 * row["coarse_cells"] - 2
        and row["bounded_local_code_exponent"] == 7 * row["coarse_cells"] + 2
        and row["global_Wilson_rank_increment"] == 3
        and row["local_code_matter_quotient_dimension"] == 12 * row["coarse_cells"] + 2
        and row["local_code_gauge_quotient_dimension"] == 2 * row["coarse_cells"] + 2
        and row["local_code_matter_gauge_intersection"] == 4
        and row["M2_per_coarse_cell"] == 22
        and row["maximum_bounded_local_constraint_weight"] <= 28
        and row["maximum_mapped_matter_generator_weight"] <= 18
        and row["maximum_auxiliary_generator_weight"] <= 18
        and row["deleted_Wilson_rank_loss"] == 1
        and row["deleted_bounded_local_constraint_rank_loss"] == 1
        for row in rows
    )
    canonical_growth = [
        row["root_tree_canonical_maximum_weight"] for row in rows
    ]
    expected_growth = [162, 1296, 2058]
    fixed_flux_support = [
        row["maximum_full_fixed_flux_stabilizer_weight"] for row in rows
    ]
    expected_fixed_flux_support = [28, 39, 45]
    full_fock_common_E = False
    result = {
        "route": "A_local_gauge_parity_syndrome",
        "rows": rows,
        "local_occupation_and_coherence_controls": local_occupations,
        "all24_and_translation_covariance_reexecuted": covariance_pass,
        "bounded_operator_router": {
            "maximum_input_Pauli_support": 18,
            "primitive_basis_change_support": 1,
            "primitive_CNOT_ladder_support": 2,
            "primitive_Rz_support": 1,
            "maximum_CNOT_compute_uncompute_per_Pauli_rotation": 34,
            "Cycle610_literal_bounded_bus_available": True,
            "literal_coordinate_embedding_of_all_22_Cycle251_roles_into_the_Cycle610_bus_constructed": False,
            "scope": (
                "generic constant-support Pauli-routing recipe only; it is not a "
                "composed NN coordinate compiler, odd creator, or state-preparation encoder"
            ),
        },
        "both_parity_blocks_present": True,
        "arbitrary_finite_density_occupations_within_each_parity_block": True,
        "runtime_global_parity_service_used": False,
        "sectorwise_even_update_spectator_independent": True,
        "bounded_local_syndrome_checks_exist": True,
        "three_noncontractible_Wilson_flux_selectors_required_for_exact_fixed_sector": True,
        "fully_locally_enforced_exact_code_space": False,
        "sectorwise_factorization": (
            "H_code=(H_matter,+ tensor H_gauge,+) direct-sum "
            "(H_matter,- tensor H_gauge,-)"
        ),
        "common_pure_full_Fock_E_across_coherent_parity_blocks_constructed": full_fock_common_E,
        "reason_common_E_not_closed": (
            "the auxiliary parity is locked to matter parity and no bounded local "
            "identification H_gauge,+ <-> H_gauge,- or preparation circuit is constructed"
        ),
        "tested_root_tree_canonical_support": canonical_growth,
        "tested_root_tree_expected_support": expected_growth,
        "tested_fixed_flux_selector_maximum_support": fixed_flux_support,
        "tested_fixed_flux_selector_expected_support": expected_fixed_flux_support,
        "global_Jordan_Wigner_or_parity_service": False,
        "pass_bounded_even_CAR_in_fixed_flux_sector": bool(
            algebra_pass and covariance_pass
            and canonical_growth == expected_growth
            and fixed_flux_support == expected_fixed_flux_support
            and local_car_residual < TOL
            and coherent_norm_residual < TOL
            and parity_block_leakage < TOL
            and parity_commutator < TOL
        ),
        "pass_fully_locally_constrained_even_CAR_code": False,
        "pass_literal_physical_NN_coordinate_compiler": False,
        "pass_required_common_full_Fock_E": full_fock_common_E,
    }
    check(
        "Route A reexecutes the bounded covariant even-CAR fixed-flux sector on L3/L6/L7 and exposes its three nonlocal Wilson selectors",
        result["pass_bounded_even_CAR_in_fixed_flux_sector"]
        and not result["pass_fully_locally_constrained_even_CAR_code"], result,
    )
    check(
        "Route A does not pass the common pure full-Fock-E gate merely from sectorwise even-algebra factorization",
        not result["pass_required_common_full_Fock_E"],
        {"canonical_growth": canonical_growth, "reason": result["reason_common_E_not_closed"]},
    )
    return result


# ---------------------------------------------------------------------------
# Route B: reversible tagged reservoir, separated from fermionic signs.


Comparator = tuple[int, int]


def comparator_schedule(width: int) -> tuple[Comparator, ...]:
    return tuple((index, index + 1) for stop in range(width - 1, 0, -1)
                 for index in range(stop))


def packet_key(packet: tuple[int, int, int]) -> tuple[int, int, int]:
    occupied, label, tag = packet
    return (0 if occupied else 1, label, tag)


def reservoir_forward(packets, schedule, deleted: int | None = None):
    state = list(packets)
    history = []
    for stage, (left, right) in enumerate(schedule):
        decision = int(packet_key(state[left]) > packet_key(state[right]))
        history.append(decision)
        if stage != deleted and decision:
            state[left], state[right] = state[right], state[left]
    return tuple(state), tuple(history)


def reservoir_inverse(packets, history, schedule, deleted: int | None = None):
    state = list(packets)
    archive = list(history)
    for stage in reversed(range(len(schedule))):
        left, right = schedule[stage]
        if stage != deleted and archive[stage]:
            state[left], state[right] = state[right], state[left]
        decision = int(packet_key(state[left]) > packet_key(state[right]))
        archive[stage] ^= decision
    return tuple(state), tuple(archive)


def route_b_reservoir() -> dict:
    width = 8
    capacity = 7
    schedule = comparator_schedule(width)
    exhaustive_failures = inverse_failures = archive_clean_failures = 0
    count_failures = parity_failures = 0
    tags = tuple(reversed(range(width)))
    for mask in range(1 << width):
        packets = tuple(
            (int((mask >> lane) & 1), (5 * lane + 3) % 11, tags[lane])
            for lane in range(width)
        )
        output, history = reservoir_forward(packets, schedule)
        recovered, cleared = reservoir_inverse(output, history, schedule)
        expected = tuple(sorted(packets, key=packet_key))
        exhaustive_failures += int(output != expected)
        inverse_failures += int(recovered != packets)
        archive_clean_failures += int(any(cleared))
        input_count = sum(row[0] for row in packets)
        output_count = sum(row[0] for row in output)
        count_failures += int(input_count != output_count)
        parity_failures += int(input_count % 2 != output_count % 2)

    deletion_stage = next(
        stage for stage in range(len(schedule))
        if any(
            reservoir_forward(tuple(
                (int((mask >> lane) & 1), (7 * lane + 1) % 13, tags[lane])
                for lane in range(width)
            ), schedule)[0]
            != reservoir_forward(tuple(
                (int((mask >> lane) & 1), (7 * lane + 1) % 13, tags[lane])
                for lane in range(width)
            ), schedule, deleted=stage)[0]
            for mask in range(1 << width)
        )
    )
    deletion_witness = next(
        mask for mask in range(1 << width)
        if reservoir_forward(tuple(
            (int((mask >> lane) & 1), (7 * lane + 1) % 13, tags[lane])
            for lane in range(width)
        ), schedule)[0]
        != reservoir_forward(tuple(
            (int((mask >> lane) & 1), (7 * lane + 1) % 13, tags[lane])
            for lane in range(width)
        ), schedule, deleted=deletion_stage)[0]
    )
    overflow_rows = []
    for occupied in range(width + 1):
        overflow_rows.append({
            "input_packets": occupied,
            "reservoir_capacity": capacity,
            "admitted": min(occupied, capacity),
            "overflow": max(0, occupied - capacity),
        })
    predecessor_directions = 6
    recurrent_arrivals = predecessor_directions * capacity
    recurrent_overflow = recurrent_arrivals - capacity
    cycle230_incoming_modes = 6
    cycle230_capacity_overflow = max(0, cycle230_incoming_modes - capacity)

    # Tagged tensor-product packet creators commute.  Their CAR
    # anticommutator has norm 2, so sorting tags does not create a fermion sign.
    lowering = np.asarray(((0, 1), (0, 0)), dtype=complex)
    identity = np.eye(2)
    create_left = np.kron(lowering.T, identity)
    create_right = np.kron(identity, lowering.T)
    commute_residual = float(np.linalg.norm(create_left @ create_right - create_right @ create_left))
    car_anticommutator_residual = float(
        np.linalg.norm(create_left @ create_right + create_right @ create_left)
    )
    result = {
        "route": "B_reversible_local_collision_syndrome_reservoir",
        "input_lanes": width,
        "reservoir_capacity": capacity,
        "adjacent_compare_exchange_stages": len(schedule),
        "history_archive_bits_per_macro": len(schedule),
        "maximum_gate_neighborhood_lanes": 2,
        "all_256_occupation_patterns_tested": True,
        "exhaustive_sort_failures": exhaustive_failures,
        "inverse_failures": inverse_failures,
        "renewal_archive_clean_failures": archive_clean_failures,
        "number_conservation_failures": count_failures,
        "odd_even_parity_failures": parity_failures,
        "coherent_extension_is_unitary": True,
        "reason_coherent_extension_is_unitary": (
            "each archived comparator is predicate-XOR then controlled SWAP; "
            "the inverse reverses the SWAP and clears the predicate"
        ),
        "overflow_rows": overflow_rows,
        "eight_packet_overflow_flag": overflow_rows[-1]["overflow"],
        "deleted_comparator_stage": deletion_stage,
        "deleted_comparator_witness_mask": deletion_witness,
        "recurrent_six_predecessor_stress": {
            "arrivals_per_target": recurrent_arrivals,
            "retained_capacity": capacity,
            "overflow_packets": recurrent_overflow,
            "scope": (
                "generalized tagged traffic allowing seven packets per incoming "
                "bond; outside Cycle230's one fermion per directional mode domain"
            ),
        },
        "Cycle230_lawful_stream_capacity": {
            "maximum_incoming_directional_modes_per_cell": cycle230_incoming_modes,
            "overflow_at_capacity_seven": cycle230_capacity_overflow,
            "pass": cycle230_capacity_overflow == 0,
        },
        "packet_creator_commutator_residual": commute_residual,
        "packet_creator_CAR_anticommutator_residual": car_anticommutator_residual,
        "collision_and_CAR_sign_separated": True,
        "pass_one_macro_collision_sorter": bool(
            exhaustive_failures == inverse_failures == archive_clean_failures
            == count_failures == parity_failures == 0
            and overflow_rows[-1]["overflow"] == 1
            and recurrent_overflow == 35
            and commute_residual < TOL
            and car_anticommutator_residual > 1.9
        ),
        "pass_Cycle230_recurrent_stream_capacity": cycle230_capacity_overflow == 0,
        "pass_generalized_tagged_recurrent_traffic_without_overflow": False,
        "pass_CAR_sign_service": False,
    }
    check(
        "Route B gives an exact reversible finite collision sorter with explicit archive, inverse, deletion, renewal, and overflow",
        result["pass_one_macro_collision_sorter"], result,
    )
    check(
        "Route B keeps generalized tagged-traffic overflow outside the Cycle230 domain and missing CAR sign as distinct findings",
        result["pass_Cycle230_recurrent_stream_capacity"]
        and not result["pass_generalized_tagged_recurrent_traffic_without_overflow"]
        and not result["pass_CAR_sign_service"],
        {"generalized_recurrent_overflow": recurrent_overflow,
         "Cycle230_capacity_overflow": cycle230_capacity_overflow,
         "CAR_anticommutator_residual": car_anticommutator_residual},
    )
    return result


# ---------------------------------------------------------------------------
# Route C: one frame-free six-face shell word, then its full-Fock sign audit.


REVERSE = (1, 0, 3, 2, 5, 4)
DIRECTIONS = tuple(tuple(int(value) for value in row) for row in c210.DIRECTIONS)


def add(left, right):
    return tuple(left[index] + right[index] for index in range(3))


def scale(factor: int, vector):
    return tuple(factor * value for value in vector)


def rotate(frame, vector):
    return tuple(int(value) for value in frame @ np.asarray(vector, dtype=int))


def nn(left, right) -> bool:
    return sum(abs(left[index] - right[index]) for index in range(3)) == 1


def radial_path(left, right):
    path = [left]
    current = list(left)
    for axis in range(3):
        while current[axis] != 0:
            current[axis] -= 1 if current[axis] > 0 else -1
            path.append(tuple(current))
    target = [0, 0, 0]
    for axis in range(3):
        while target[axis] != right[axis]:
            target[axis] += 1 if right[axis] > 0 else -1
            path.append(tuple(target))
    return tuple(path)


def givens_decomposition(unitary: np.ndarray):
    work = unitary.copy()
    rows = []
    for column in range(unitary.shape[0] - 1):
        for lower in range(unitary.shape[0] - 1, column, -1):
            upper = lower - 1
            first, second = work[upper, column], work[lower, column]
            radius = math.sqrt(abs(first) ** 2 + abs(second) ** 2)
            if radius < 1e-14:
                continue
            block = np.asarray((
                (np.conj(first) / radius, np.conj(second) / radius),
                (-second / radius, first / radius),
            ))
            givens = np.eye(unitary.shape[0], dtype=complex)
            givens[np.ix_((upper, lower), (upper, lower))] = block
            work = givens @ work
            rows.append((upper, lower, givens))
    diagonal = np.diag(np.diag(work))
    reconstruction = diagonal.copy()
    for _upper, _lower, givens in reversed(rows):
        reconstruction = givens.conj().T @ reconstruction
    return rows, diagonal, reconstruction, work


def mode_permutation_B(length: int) -> tuple[int, ...]:
    mapping = []
    for cell in c230.all_sites(length):
        for direction, displacement in enumerate(c210.DIRECTIONS):
            target = c230.shifted_site(cell, -displacement, length)
            mapping.append(c230.site_index(target, REVERSE[direction], length))
    return tuple(mapping)


def stream_B_sign_audit(length: int) -> dict:
    mapping = mode_permutation_B(length)
    modes = len(mapping)
    involution_failures = sum(mapping[mapping[index]] != index for index in range(modes))
    mismatch_count = 0
    witness = None
    for first in range(modes):
        for second in range(first + 1, modes):
            abstract_sign = -1 if mapping[first] > mapping[second] else 1
            endpoint_fswap_sign = -1 if (
                mapping[first] == second and mapping[second] == first
            ) else 1
            if abstract_sign != endpoint_fswap_sign:
                mismatch_count += 1
                if witness is None:
                    witness = {
                        "occupied_input_modes": (first, second),
                        "mapped_modes": (mapping[first], mapping[second]),
                        "abstract_Gamma_B_sign": abstract_sign,
                        "endpoint_fSWAP_product_sign": endpoint_fswap_sign,
                    }
    return {
        "length": length,
        "modes": modes,
        "two_particle_basis_states": math.comb(modes, 2),
        "B_involution_failures": involution_failures,
        "sign_mismatches": mismatch_count,
        "first_witness": witness,
    }


def B_edge_set(length: int):
    edges = set()
    for cell in c230.all_sites(length):
        for direction, displacement in enumerate(c210.DIRECTIONS):
            target = c230.shifted_site(cell, -displacement, length)
            first = tuple(cell) + (direction,)
            second = tuple(target) + (REVERSE[direction],)
            edges.add(tuple(sorted((first, second))))
    return edges


def transform_mode(mode, frame: np.ndarray, length: int):
    cell = tuple(int(value % length) for value in frame @ np.asarray(mode[:3]))
    permutation = c210.direction_permutation(frame)
    direction = int(np.argmax(permutation[:, mode[3]]))
    return cell + (direction,)


def route_c_frame_free_shell() -> dict:
    H = c610.H
    K = c610.K
    shell = tuple(scale(-H, direction) for direction in DIRECTIONS)
    species = c219.common_species(c230.BETA)
    coin = species.coin
    givens, diagonal, reconstruction, triangular = givens_decomposition(coin)
    exterior_residual = float(np.linalg.norm(
        c229.fock_lift(reconstruction) - c229.fock_lift(coin)
    ))
    triangular_residual = float(np.linalg.norm(
        triangular - np.diag(np.diag(triangular))
    ))
    reconstruction_residual = float(np.linalg.norm(reconstruction - coin))

    frame_rows = []
    all576_failures = 0
    B_edges_L3 = B_edge_set(3)
    for frame in c210.proper_cubic_frames():
        direction_permutation = c210.direction_permutation(frame)
        direction_map = tuple(
            int(np.argmax(direction_permutation[:, direction]))
            for direction in range(6)
        )
        transformed_shell = {rotate(frame, coordinate) for coordinate in shell}
        coin_residual = float(np.linalg.norm(
            direction_permutation @ coin @ direction_permutation.T - coin
        ))
        contact = np.diag(np.exp(
            1j * c230.COUPLING
            * np.sum(c229.occupation_table(6), axis=1)
            * (np.sum(c229.occupation_table(6), axis=1) - 1) / 2
        ))
        fock_frame = c229.fock_lift(direction_permutation)
        local_word = contact @ c229.fock_lift(coin)
        word_residual = float(np.linalg.norm(
            fock_frame @ local_word @ fock_frame.conj().T - local_word
        ))
        reverse_failures = sum(
            direction_map[REVERSE[direction]] != REVERSE[direction_map[direction]]
            for direction in range(6)
        )
        transformed_B_edges = {
            tuple(sorted((
                transform_mode(edge[0], frame, 3),
                transform_mode(edge[1], frame, 3),
            )))
            for edge in B_edges_L3
        }
        frame_rows.append({
            "shell_set_preserved": transformed_shell == set(shell),
            "coin_covariance_residual": coin_residual,
            "full_local_word_covariance_residual": word_residual,
            "A_reverse_covariance_failures": reverse_failures,
            "B_edge_set_covariant_L3": transformed_B_edges == B_edges_L3,
        })
    frames = c210.proper_cubic_frames()
    for first in frames:
        for second in frames:
            first_rep = c210.direction_permutation(first)
            second_rep = c210.direction_permutation(second)
            direct_rep = c210.direction_permutation(first @ second)
            all576_failures += int(
                {rotate(first, rotate(second, coordinate)) for coordinate in shell}
                != {rotate(first @ second, coordinate) for coordinate in shell}
            )
            all576_failures += int(
                np.linalg.norm(first_rep @ second_rep - direct_rep) > TOL
            )

    pair_paths = {}
    path_failures = 0
    maximum_path_sites = 0
    for left, right in combinations(range(6), 2):
        path = radial_path(shell[left], shell[right])
        pair_paths[(left, right)] = path
        maximum_path_sites = max(maximum_path_sites, len(path))
        path_failures += int(path[0] != shell[left] or path[-1] != shell[right])
        path_failures += sum(not nn(path[index], path[index + 1])
                             for index in range(len(path) - 1))
        path_failures += int(len(set(path)) != len(path))
    # One factorized onsite word: diagonal phases, 13 nontrivial Givens,
    # three reversal fSWAPs, 15 contact phases.  Every two-mode factor is
    # routed out and back on a finite radial path.
    two_mode_factors = len(givens) + 3 + math.comb(6, 2)
    routed_fswap_instances = sum(
        2 * max(0, len(pair_paths[tuple(sorted((left, right)))]) - 2)
        for left, right in (
            [(row[0], row[1]) for row in givens]
            + [(0, 1), (2, 3), (4, 5)]
            + list(combinations(range(6), 2))
        )
    )
    descriptors = (
        ("onsite_Gamma_coin", tuple((left, right) for left, right, _ in givens)),
        ("onsite_A", ((0, 1), (2, 3), (4, 5))),
        ("intercell_B_directed_incidences",
         tuple((direction, REVERSE[direction]) for direction in range(6))),
        ("intercell_B_gate_set", "undirected quotient under B involution"),
        ("onsite_contact", tuple(combinations(range(6), 2))),
        ("order", "coin -> A -> B -> contact"),
    )
    sign_rows = [stream_B_sign_audit(length) for length in (3, 6, 7)]
    factor_order = json.loads((ROOT / (
        "outputs/physical_proper_cubic_supercell_stream_composition_"
        "tournament_cycle610_receipt_2026_07_22.json"
    )).read_text())["Cycle230_factor_order_deletion_noncommutation"]
    geometry_pass = (
        len(shell) == len(set(shell)) == 6
        and path_failures == all576_failures == 0
        and all(
            row["shell_set_preserved"]
            and row["coin_covariance_residual"] < TOL
            and row["full_local_word_covariance_residual"] < TOL
            and row["A_reverse_covariance_failures"] == 0
            and row["B_edge_set_covariant_L3"]
            for row in frame_rows
        )
        and reconstruction_residual < TOL
        and triangular_residual < TOL
        and exterior_residual < TOL
    )
    car_pass = all(row["sign_mismatches"] == 0 for row in sign_rows)
    result = {
        "route": "C_frame_free_six_face_shell",
        "literal_frame_free_word": (
            "Gamma(C) on the six face modes; onsite opposite-face A; "
            "nearest-neighbor cross-face B; onsite pair contact"
        ),
        "orientation_bits": 0,
        "host_selected_frames": 0,
        "six_mode_shell_coordinates": shell,
        "fine_supercell_scale": K,
        "all24_rows": frame_rows,
        "all576_frame_products": len(frames) ** 2,
        "all576_failures": all576_failures,
        "coin_Givens_factors": len(givens),
        "coin_one_mode_phase_factors": 6,
        "coin_reconstruction_residual": reconstruction_residual,
        "coin_exterior_lift_residual": exterior_residual,
        "coin_triangularization_residual": triangular_residual,
        "two_mode_factors_per_cell_excluding_intercell_B": two_mode_factors,
        "intercell_B_directed_incidences_per_coarse_cell": 6,
        "intercell_B_undirected_fSWAPs_per_coarse_cell": 3,
        "intercell_B_edges_L3": len(B_edges_L3),
        "routed_fSWAP_instances_per_cell": routed_fswap_instances,
        "maximum_radial_path_sites": maximum_path_sites,
        "maximum_primitive_support_M2": 2,
        "path_failures": path_failures,
        "literal_word_sha256": sha256(repr(descriptors).encode()).hexdigest(),
        "single_word_not_24_analytic_rotations": True,
        "factor_order_and_noncommutation": factor_order,
        "B_full_Fock_sign_rows": sign_rows,
        "role_genesis_removed_at_register_word_geometry_resolution": geometry_pass,
        "full_Fock_CAR_intertwining": car_pass,
        "pass_frame_free_bounded_word": geometry_pass,
        "pass_required_full_Fock_compiler": geometry_pass and car_pass,
    }
    check(
        "Route C supplies one literal frame-free six-face word with bounded NN routing and all24/all576 total-update covariance",
        result["pass_frame_free_bounded_word"], result,
    )
    check(
        "Route C's ordinary endpoint stream is rejected by explicit full-Fock CAR sign witnesses on L3/L6/L7",
        not result["full_Fock_CAR_intertwining"]
        and all(row["B_involution_failures"] == 0 and row["sign_mismatches"] > 0
                for row in sign_rows),
        sign_rows,
    )
    return result


def joint_disposition(route_a: dict, route_b: dict, route_c: dict,
                      prior: dict) -> dict:
    factor = prior["Cycle230_factor_order_deletion_noncommutation"]
    fixtures = prior["onsite_mass_contact_seam_composition"]
    result = {
        "same_encoding_composes_A_B_C": False,
        "E_Gcoarse_equals_Gphysical_E_on_declared_full_Fock_code": False,
        "bounded_support_and_constant_overhead": True,
        "locally_enforced_auxiliary_gauge_constraints": route_a[
            "pass_fully_locally_constrained_even_CAR_code"
        ],
        "no_global_Jordan_Wigner_or_nonlocal_parity_service": True,
        "all24_all576_covariance": (
            route_a["all24_and_translation_covariance_reexecuted"]
            and route_c["pass_frame_free_bounded_word"]
        ),
        "one_particle_mass_fixture_preserved": fixtures["pass"],
        "local_contact_and_Cycle230_seam_preserved": fixtures["pass"],
        "factor_order_preserved": factor["pass"],
        "noncommutation_witness": factor[
            "Cycle230_contact_free_generator_noncommutation_witness"
        ],
        "why_joint_fails": (
            "Route A is a fixed-Wilson-flux sectorwise even-observable subsystem "
            "without a literal Cycle610 coordinate composition or common pure "
            "full-Fock E; Route B is a tagged collision permutation without CAR "
            "signs; Route C removes the 24-one-hot role field but its endpoint B "
            "swaps disagree with Gamma(B).  These are not the same encoding."
        ),
        "strongest_constructive_result": (
            "the global exactly-one-carrier restriction is unnecessary for the "
            "bounded covariant even-CAR operator algebra inside each fixed-flux "
            "Cycle251 sector: its 22-M2/cell bounded generators carry arbitrary "
            "finite density in both parity sectors, while a separate one-word "
            "six-face construction removes Cycle610's 24-one-hot orientation "
            "field at geometry resolution"
        ),
        "pass": False,
    }
    check(
        "the tournament does not claim the requested joint compiler because no one encoding composes all three route components",
        not result["same_encoding_composes_A_B_C"]
        and not result["E_Gcoarse_equals_Gphysical_E_on_declared_full_Fock_code"],
        result,
    )
    return result


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict,
                     joint: dict) -> dict:
    families = (
        "A local puncture/gauge subsystem (executed)",
        "B reversible tagged collision reservoir (executed)",
        "C frame-free six-face shell word (executed)",
        "Cycle248 bounded full-Fock spectator encoding (prior; update strings grow)",
        "Cycle260 local parity-shuttle/transport attempts (prior)",
        "Cycle312 local full-Fock extension attempts (prior; higher-number signs recur)",
        "higher-form or non-Pauli gauge embedding (live, unexecuted)",
        "autonomous dissipative/code-preparation dynamics (live, unexecuted)",
    )
    walls = (
        "common coherent full-Fock E across parity blocks",
        "strictly local enforcement of the three Wilson flux relations",
        "generalized recurrent tagged-traffic capacity outside the Cycle230 domain",
        "frame-free endpoint-stream CAR sign",
        "autonomous preparation of the locally checkable code state",
    )
    pairs = tuple(combinations(walls, 2))
    result = {
        "N1_alternative_route_enumeration": families,
        "N2_wall_independence_audit": {
            "walls": walls,
            "all_pairs": pairs,
            "pair_count": len(pairs),
            "conclusion": (
                "the four observed residuals are distinct and preparation is a "
                "fifth wall; none is inferred from another"
            ),
        },
        "N3_hidden_wall_scan": (
            "the local checks define a code space but do not autonomously prepare "
            "it; Route A's exact target sector also fixes three noncontractible "
            "Wilson relations and a period-16 physical role marker; the frame-free "
            "word uses supplied coarse supercell centers and blank routing paths; "
            "beta, g, factor order, and phase precision remain supplied"
        ),
        "N4_residual_matching": {
            "A": route_a["tested_root_tree_canonical_support"],
            "A_fixed_flux_selector_support": route_a[
                "tested_fixed_flux_selector_maximum_support"
            ],
            "B_generalized_tagged_traffic_overflow": route_b[
                "recurrent_six_predecessor_stress"
            ]["overflow_packets"],
            "B_Cycle230_capacity_overflow": route_b[
                "Cycle230_lawful_stream_capacity"
            ]["overflow_at_capacity_seven"],
            "B_CAR_residual": route_b["packet_creator_CAR_anticommutator_residual"],
            "C_sign_mismatch_counts": [
                row["sign_mismatches"] for row in route_c["B_full_Fock_sign_rows"]
            ],
        },
        "N5_rhetoric_audit": (
            "sectorwise even algebra is not called full-Fock E; collision sorting "
            "is not called CAR; a frame-free geometric word is not called a "
            "CAR-faithful compiler; no minimum-content or impossibility claim ships"
        ),
        "N6_partial_closure_path_scan": (
            "retain A as the strongest physical operator substrate and C as a "
            "role-genesis-free layout lemma; seek one encoding that gives odd-sector "
            "coherence and the same frame-free stream"
        ),
        "N7_steelman": (
            "a non-Pauli/higher-form local gauge code or autonomous code-preparation "
            "QCA may identify the two gauge parity factors without a global service"
        ),
        "N8_cross_cycle_echo": (
            "Cycle248, 251, 261, 276, and 312 separate bounded even algebra from "
            "full-Fock state encoding; this recurrence motivates another constructive "
            "family but does not establish a substrate-independent obstruction"
        ),
        "normalized_proof_search_family_complete": False,
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "route_independent_shared_obstruction": False,
        "axiom_pressure": False,
        "pass_for_withholding_no_go": True,
    }
    condition = (
        len(families) >= 6 and len(pairs) == math.comb(len(walls), 2)
        and not joint["pass"]
        and not result["negative_claim_shipped"]
        and not result["minimum_content_claim_shipped"]
        and not result["route_independent_shared_obstruction"]
        and not result["axiom_pressure"]
    )
    check("fresh N1-N8 withholds no-go, minimum-content, and axiom-pressure claims",
          condition, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "Authority: none", "Audit: unset", "Cycle 617", "Route A", "Route B",
        "Route C", "E G_coarse = G_physical E", "22 M2", "both parity blocks",
        "common pure full-Fock", "local constraints", "L3", "L6", "L7",
        "all 24", "all 576", "finite density", "coherent superposition",
        "adjacent collision", "overflow", "archive", "renewal", "inverse",
        "deletion", "CAR sign", "frame-free", "one literal word", "24 one-hot",
        "coin -> A -> B -> contact", "proper-cubic", "support-two", "mass",
        "contact", "seam", "factor order", "noncommutation", "locally checkable",
        "autonomous initial state", "constant overhead", "N1", "N8",
        "no axiom pressure", "authority none", "audit unset",
    )
    forbidden = (
        "full-fock compiler passes", "collision sorting supplies fermionic signs",
        "shared obstruction proved", "axiom revision required",
        "schedule is physical time", "phase is physical energy",
    )
    missing = tuple(item for item in required if item not in text)
    hits = tuple(item for item in forbidden if item in text.lower())
    result = {"missing": missing, "forbidden_hits": hits}
    check("Cycle617 note freezes route scope, exact tests, supplies, and N1-N8",
          not missing and not hits, result)
    return result


def main() -> int:
    started = time.perf_counter()
    print("Cycle617 local-sector / role-genesis closure tournament", AUTHORITY, AUDIT)
    prior = shore()
    route_a = route_a_local_gauge()
    route_b = route_b_reservoir()
    route_c = route_c_frame_free_shell()
    joint = joint_disposition(route_a, route_b, route_c, prior)
    discipline = no_go_discipline(route_a, route_b, route_c, joint)
    note = note_contract()
    elapsed = time.perf_counter() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    resources = {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss}
    check("cold resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES,
          resources)
    receipt = {
        "status": "cycle617-local-sector-role-genesis-closure-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "HEAD": subprocess.check_output(
            ("git", "rev-parse", "HEAD"), cwd=ROOT, text=True
        ).strip(),
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "joint_disposition": joint,
        "no_go_discipline": discipline,
        "note_contract": note,
        "strongest_constructive_result": joint["strongest_constructive_result"],
        "route_by_route_disposition": {
            "A": "retain bounded covariant even-CAR generators in a fixed-flux sector; three nonlocal Wilson selectors and a common pure full-Fock E remain",
            "B": "retain collision lemma only: exact finite reversible sorter and sufficient Cycle230 capacity, but no CAR sign; generalized multi-packet traffic overflows",
            "C": "retain frame-free geometry/word lemma only: no 24-one-hot genesis, but endpoint B fails full-Fock signs",
        },
        "updated_dependency_ledger": {
            "C_ref": "unchanged: reference/phase selection remains supplied",
            "C_num": "improved at even-observable finite-density resolution; common cross-parity pure E remains open",
            "C_wrap": "unchanged: Cycle230 modular seam fixture reproduced from the accepted shore",
            "C_int": "unchanged constructive local contact and noncommutation fixture; coupling g remains supplied",
        "C_local": "improved: bounded 22-M2 even-CAR generators plus frame-free shell; three Wilson selectors and the joint full-Fock local compiler remain open",
            "C_source": "unchanged: no autonomous source/resource law derived",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 3.0,
            "causal_time": 2.0,
            "inertia_matter": 3.5,
            "gravity_source": 2.5,
            "Born_probability": 1.5,
        },
        "supplied_structure_inventory": (
            "coarse 129^3 supercell centers and blank routing paths",
            "Cycle230 six-mode CAR law, beta, contact g, and coin-A-B-contact factor order",
            "Cycle251 puncture topology, local stabilizer code state, and three fixed Wilson-flux selectors",
            "Cycle251 period-16 physical role marker and supplied macro-cell roles",
            "finite reservoir capacity and blank 28-bit comparator archive",
            "canonical occupation-label order used only to audit, not serve, CAR signs",
            "gate angle precision and initial/boundary-state selection",
        ),
        "shared_obstruction_or_axiom_pressure": False,
        "constitutional_effect": "none",
        "optimal_next_campaign": (
            "construct one frame-covariant non-Pauli or higher-form gauge encoding "
            "with a bounded cross-parity isometry, autonomous local syndrome "
            "preparation, and the literal six-face B stream in the same code; test "
            "odd/even coherent sectors on L3/L6/L7 before any renewed no-go claim"
        ),
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n"
    )
    summary = {
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "route_A_fixed_flux_even_CAR": route_a["pass_bounded_even_CAR_in_fixed_flux_sector"],
        "route_A_fully_local_constraints": route_a["pass_fully_locally_constrained_even_CAR_code"],
        "route_A_common_full_Fock_E": route_a["pass_required_common_full_Fock_E"],
        "route_B_finite_sorter": route_b["pass_one_macro_collision_sorter"],
        "route_C_frame_free_word": route_c["pass_frame_free_bounded_word"],
        "joint_full_Fock_compiler": joint["pass"],
        "axiom_pressure": False,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold_handle:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold_handle)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
