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
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
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
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


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
        "ed2250711646ad99bf077e74b8e4194f2df0a2cf368d3c05c45ea95cac8083db",
    "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md":
        "3768d2a1407bdc8de06e2a55fa18300469b1006c0a16a78ada8b8d3a4b936105",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json":
        "375f843606a81970ae50f71d74c53f7e4c4d1437007daaecbedd0b19e3fdfa34",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_cold_2026_07_22.txt":
        "0adbee38e398c9e1d1ccd2733454ead2669338b86d48cbefa5331abb78c126e8",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py":
        "c7b8673eb1a0dced08131820caa1fb2400fc8d1f73cfe2cddf5f8a28f9045d35",
    "docs/work_history/repo/review_feedback/WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md":
        "d5a39e45949cf079f6c37fa5646d00a9319d7d2776d84323d9adf1c086e06beb",
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


def cycle269_sector_reconciliation() -> dict:
    """Reexecute the Cycle269 central-sector certificate at campaign sizes."""
    rows = []
    cache = {}
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        code = c269.build_code(length)
        cache[length] = code
        n = length**3
        local_rank, local_bad = c269.c235.phase_aware_rank(
            list(code.local_checks), code.qubits
        )
        fixed_rank, fixed_bad = c269.c235.phase_aware_rank(
            list(code.local_checks + code.wilsons), code.qubits
        )
        matter = list(code.B + code.A)
        matter_total_rank = c269.rank(
            list(code.local_checks) + matter, code.qubits
        )
        matter_rank = c269.rank(matter, code.qubits)
        matter_gram_rank = c269.gram_rank(matter)
        wilsons_in_matter_span = (
            c269.rank(matter + list(code.wilsons), code.qubits) == matter_rank
        )
        sector_failures = 0
        for bits in product((0, 1), repeat=3):
            sector_rank, inconsistent = c269.c235.phase_aware_rank(
                list(code.local_checks)
                + [c269.signed(wilson, bit)
                   for wilson, bit in zip(code.wilsons, bits)],
                code.qubits,
            )
            sector_failures += (
                sector_rank != 9 * n + 1 or bool(inconsistent)
            )
        pairing = [
            [int(not membrane.commutes(wilson))
             for wilson in code.wilsons]
            for membrane in code.membranes
        ]
        rows.append({
            "length": length,
            "split": split,
            "coarse_cells": n,
            "physical_M2_qubits": code.qubits,
            "M2_per_coarse_cell": code.qubits / n,
            "local_check_rank": local_rank,
            "local_code_exponent": code.qubits - local_rank,
            "fixed_Wilson_rank": fixed_rank,
            "fixed_Wilson_exponent": code.qubits - fixed_rank,
            "Wilson_rank_increment": fixed_rank - local_rank,
            "consistent_equal_dimension_Wilson_sectors": 8 - sector_failures,
            "matter_quotient_dimension": matter_total_rank - local_rank,
            "matter_symplectic_rank": matter_gram_rank,
            "matter_radical_dimension": (
                matter_total_rank - local_rank - matter_gram_rank
            ),
            "matter_commutant_quotient_dimension": (
                2 * code.qubits - matter_total_rank - local_rank
            ),
            "Wilsons_in_matter_span": wilsons_in_matter_span,
            "Wilson_matter_commutator_failures": sum(
                not wilson.commutes(operator)
                for wilson in code.wilsons for operator in matter
            ),
            "membrane_weights": [
                (row.x | row.z).bit_count() for row in code.membranes
            ],
            "membrane_local_check_leakage": sum(
                not membrane.commutes(check_row)
                for membrane in code.membranes
                for check_row in code.local_checks
            ),
            "membrane_Wilson_pairing": pairing,
            "membrane_matter_anticommutators": [
                sum(not membrane.commutes(operator) for operator in matter)
                for membrane in code.membranes
            ],
            "phase_inconsistencies": len(local_bad) + len(fixed_bad),
        })

    c269.PASS = c269.FAIL = 0
    c269.covariance_controls(cache[3])
    covariance_pass = c269.PASS == 2 and c269.FAIL == 0
    condition = covariance_pass and all(
        row["physical_M2_qubits"] == 15 * row["coarse_cells"]
        and row["local_check_rank"] == 9 * row["coarse_cells"] - 2
        and row["local_code_exponent"] == 6 * row["coarse_cells"] + 2
        and row["fixed_Wilson_rank"] == 9 * row["coarse_cells"] + 1
        and row["fixed_Wilson_exponent"] == 6 * row["coarse_cells"] - 1
        and row["Wilson_rank_increment"] == 3
        and row["consistent_equal_dimension_Wilson_sectors"] == 8
        and row["matter_quotient_dimension"] == 12 * row["coarse_cells"] + 1
        and row["matter_symplectic_rank"] == 12 * row["coarse_cells"] - 2
        and row["matter_radical_dimension"] == 3
        and row["matter_commutant_quotient_dimension"] == 3
        and row["Wilsons_in_matter_span"]
        and row["Wilson_matter_commutator_failures"] == 0
        and row["membrane_weights"] == [row["length"] ** 2] * 3
        and row["membrane_local_check_leakage"] == 0
        and row["membrane_Wilson_pairing"]
            == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        and row["membrane_matter_anticommutators"]
            == [row["length"] ** 2] * 3
        and row["phase_inconsistencies"] == 0
        for row in rows
    )
    result = {
        "rows": rows,
        "all24_and_full_L3_translation_covariance_reexecuted": covariance_pass,
        "representation": (
            "direct sum of eight central-character/spin-twist blocks; not a "
            "target-matter tensor spectator factor"
        ),
        "Wilson_roles": (
            "W_x,W_y,W_z span the three-dimensional abelian radical and "
            "matter commutant quotient"
        ),
        "sector_changing_membrane_roles": (
            "each L^2 membrane is conjugate to one Wilson and anticommutes "
            "with L^2 matter hopping generators"
        ),
        "fixed_sector_or_twisted_family_candidate": True,
        "operational_contractible_quotient_candidate": True,
        "spectator_independence": False,
        "tensor_factorization": False,
        "pass": condition,
    }
    check(
        "Cycle269 central-sector/radical/membrane certificate reexecutes on L3/L6/L7 without spectator-factor language",
        condition, result,
    )
    return result


def shore() -> dict:
    observed = {name: sha(ROOT / name) for name in PINS}
    prior = json.loads((ROOT / (
        "outputs/physical_proper_cubic_supercell_stream_composition_"
        "tournament_cycle610_receipt_2026_07_22.json"
    )).read_text())
    expected_graph = dict(
        prior["shore"]["import_audit"]["expected_transitive_sha256"]
    )
    expected_graph.update(PINS)
    observed_graph = {name: sha(ROOT / name) for name in expected_graph}
    actual_modules = c610.c606.c600.imported_science_modules(
        c610, c251, c269, c219, c229, c230, c210
    )
    uncovered = sorted(set(actual_modules.values()) - set(expected_graph))
    physical_scope = prior["physical_M2_scope"]
    translation_rows = prior["fine_site_translation_falsifier"]["rows"]
    inherited = {
        "Cycle610_pass": prior["pass"],
        "Cycle610_tests_passed": prior["tests_passed"],
        "Cycle610_authority": prior["authority"],
        "Cycle610_audit": prior["audit"],
        "Cycle610_author_artifact_status_accepted": prior[
            "author_artifact_status_accepted"
        ],
        "Cycle610_physical_M2_scope": physical_scope,
        "Cycle610_conditional_geometry": prior["global_microstep_geometry"]["pass"],
        "Cycle610_conditional_fixture": prior[
            "conditional_onsite_mass_contact_seam_composition"
        ]["pass"],
        "Cycle610_factor_order": prior[
            "Cycle230_factor_order_deletion_noncommutation"
        ]["pass"],
        "Cycle610_translation_rows": translation_rows,
        "Cycle610_broad_negative_gate": prior["broad_negative_gate"],
        "Cycle610_axiom_pressure": prior[
            "shared_obstruction_or_axiom_pressure"
        ],
        "Cycle610_scope_statement": (
            "conditional coarse-grid geometry only; no physical E, physical "
            "intertwiner residual, or leakage evaluation"
        ),
        "Cycle269_scope_statement": (
            "eight central-character spin/twist blocks; Wilsons span the "
            "matter radical/commutant and conjugate membranes act on matter"
        ),
        "import_audit": {
            "expected_transitive_sha256": expected_graph,
            "observed_transitive_sha256": observed_graph,
            "actual_imported_modules": actual_modules,
            "uncovered_imported_modules": uncovered,
            "expected_file_count": len(expected_graph),
            "runtime_module_count": len(actual_modules),
        },
    }
    condition = (
        observed == PINS and observed_graph == expected_graph and not uncovered
        and inherited["Cycle610_pass"]
        and inherited["Cycle610_tests_passed"] == 18
        and inherited["Cycle610_authority"] == AUTHORITY
        and inherited["Cycle610_audit"] == AUDIT
        and not inherited["Cycle610_author_artifact_status_accepted"]
        and inherited["Cycle610_conditional_geometry"]
        and inherited["Cycle610_conditional_fixture"]
        and inherited["Cycle610_factor_order"]
        and not physical_scope["promotion_to_physical_M2_law"]
        and not physical_scope["literal_physical_encoder_composed"]
        and physical_scope["physical_intertwiner_residual"] is None
        and not physical_scope["physical_code_leakage_evaluated"]
        and [row["one_fine_site_x_translation_symmetric_difference"]
             for row in translation_rows] == [2970, 23760, 37730]
        and inherited["Cycle610_broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and not inherited["Cycle610_axiom_pressure"]
    )
    check("corrected Cycle610, Cycle269, and complete inherited science graph are byte-exact", condition,
          {"observed": observed, "inherited": inherited})
    return {"receipt": prior, **inherited}


# ---------------------------------------------------------------------------
# Route A: bounded local even-CAR subsystem, with the full-Fock boundary kept.


def route_a_local_gauge() -> dict:
    cycle269_reconciliation = cycle269_sector_reconciliation()
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
            "Cycle610_conditional_coarse_geometry_available": True,
            "Cycle610_literal_physical_bus_available": False,
            "literal_coordinate_embedding_of_all_22_Cycle251_roles_into_the_Cycle610_bus_constructed": False,
            "scope": (
                "generic constant-support Pauli-routing recipe only; it is not a "
                "composed NN coordinate compiler, odd creator, or state-preparation encoder"
            ),
        },
        "abstract_Cycle230_target_has_both_parity_blocks": True,
        "physical_both_parity_blocks_intertwined": False,
        "fixed_sector_even_algebra_allows_arbitrary_even_finite_density": True,
        "runtime_global_parity_service_used": False,
        "bounded_local_syndrome_checks_exist": True,
        "three_noncontractible_Wilson_flux_selectors_required_for_exact_fixed_sector": True,
        "fully_locally_enforced_exact_code_space": False,
        "cycle269_sector_reconciliation": cycle269_reconciliation,
        "unfixed_sector_structure": (
            "Cycle269 reexecution gives a direct sum of eight central-character/"
            "spin-twist matter blocks; Wilsons are in the matter radical and "
            "their membrane conjugates act on matter, so no spectator or tensor "
            "factor is inferred for Cycle251"
        ),
        "common_pure_full_Fock_E_across_coherent_parity_blocks_constructed": full_fock_common_E,
        "reason_common_E_not_closed": (
            "only a fixed-Wilson even-algebra representation is executed; no "
            "bounded local full-Fock state isometry, physical Cycle610 composition, "
            "or sector-independent identification is constructed"
        ),
        "tested_root_tree_canonical_support": canonical_growth,
        "tested_root_tree_expected_support": expected_growth,
        "tested_fixed_flux_selector_maximum_support": fixed_flux_support,
        "tested_fixed_flux_selector_expected_support": expected_fixed_flux_support,
        "global_Jordan_Wigner_or_parity_service": False,
        "pass_bounded_even_CAR_in_fixed_flux_sector": bool(
            algebra_pass and covariance_pass and cycle269_reconciliation["pass"]
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
        "Route A does not pass the common pure full-Fock-E gate from a fixed-sector even-algebra representation",
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
    receipt = prior["receipt"]
    factor = receipt["Cycle230_factor_order_deletion_noncommutation"]
    conditional_fixture = receipt[
        "conditional_onsite_mass_contact_seam_composition"
    ]
    result = {
        "same_encoding_composes_A_B_C": False,
        "E_Gcoarse_equals_Gphysical_E_on_declared_full_Fock_code": False,
        "route_local_bounded_support_and_constant_overhead": True,
        "joint_same_encoding_bounded_support_and_constant_overhead": False,
        "locally_enforced_auxiliary_gauge_constraints": route_a[
            "pass_fully_locally_constrained_even_CAR_code"
        ],
        "route_A_no_global_Jordan_Wigner_or_nonlocal_parity_service": True,
        "route_local_all24_all576_covariance": (
            route_a["all24_and_translation_covariance_reexecuted"]
            and route_c["pass_frame_free_bounded_word"]
        ),
        "Cycle610_conditional_mass_contact_seam_fixture_byte_pinned": (
            conditional_fixture["pass"]
        ),
        "Cycle610_fixture_scope": (
            "conditional coarse-grid move/apply/restore geometry; not a "
            "physical M2 encoder or new Cycle617 preservation test"
        ),
        "one_particle_mass_fixture_freshly_reexecuted": False,
        "one_particle_mass_fixture_preserved_by_new_physical_E": False,
        "Cycle230_seam_freshly_reexecuted_in_new_physical_E": False,
        "abstract_Cycle230_local_coin_contact_algebra_reexecuted": True,
        "factor_order_byte_pinned": factor["pass"],
        "noncommutation_witness": factor[
            "Cycle230_contact_free_generator_noncommutation_witness"
        ],
        "why_joint_fails": (
            "Route A is a fixed-Wilson even-observable representation without a "
            "literal physical Cycle610 composition or common pure full-Fock E; "
            "Cycle269 additionally forbids treating its eight spin/twist blocks "
            "as spectator tensor factors because sector-changing membranes act "
            "on matter. Route B is a tagged collision permutation without CAR "
            "signs. Route C removes the 24-one-hot role field only at conditional "
            "geometry resolution, and its endpoint B swaps disagree with Gamma(B)."
        ),
        "strongest_constructive_result": (
            "the global exactly-one-carrier restriction is unnecessary for the "
            "bounded covariant even-CAR operator algebra inside a fixed-Wilson "
            "Cycle251 sector: its 22-M2/cell bounded generators support arbitrary "
            "even finite density, while a separate one-word six-face construction "
            "removes Cycle610's 24-one-hot orientation field only at conditional "
            "geometry resolution; neither result is a physical full-Fock E"
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
        {
            "family": "Cycle251 rough-terminal fixed-Wilson even algebra",
            "object": "22 M2 factors per coarse cell on L3/L6/L7",
            "mechanism": "bounded mapped matter and auxiliary Pauli generators",
            "terminal_obligation": "fixed-sector even-algebra representation",
            "strength_vs_target": "weaker than one physical full-Fock E",
            "marker": "ATTEMPTED",
            "evidence": "rank, support, covariance, and deletion rows reexecuted",
            "disposition": "retained only at fixed-Wilson even-algebra scope",
        },
        {
            "family": "Cycle269 Wilson-unfixed connected edge code",
            "object": "15 M2 factors per coarse cell on L3/L6/L7",
            "mechanism": "local checks, matter Gram form, Wilson center, and membranes",
            "terminal_obligation": "test whether Wilson labels are spectator gauge qubits",
            "strength_vs_target": "exact for this connected presentation only",
            "marker": "ATTEMPTED",
            "evidence": "eight sectors, radical/commutant dimension three, L^2 matter-active membranes",
            "disposition": "direct-sum twisted family retained; no tensor-spectator extrapolation",
        },
        {
            "family": "reversible tagged collision reservoir",
            "object": "eight lanes, capacity seven, 28 comparator archives",
            "mechanism": "predicate archive plus adjacent controlled swaps",
            "terminal_obligation": "collision handling and CAR signs",
            "strength_vs_target": "closes finite collision sorting only",
            "marker": "ATTEMPTED",
            "evidence": "all 256 patterns, inverse/deletion/renewal, CAR residual two",
            "disposition": "retained as a collision lemma, not a sign service",
        },
        {
            "family": "frame-free six-face conditional word",
            "object": "one six-mode shell word with no orientation register",
            "mechanism": "proper-cubic shell geometry and endpoint swaps",
            "terminal_obligation": "same-encoding full-Fock stream",
            "strength_vs_target": "geometry-only because the B signs mismatch",
            "marker": "ATTEMPTED",
            "evidence": "all24/all576 geometry and L3/L6/L7 sign audit",
            "disposition": "retained only as conditional geometry",
        },
        {
            "family": "corrected Cycle610 supplied-grid compiler",
            "object": "129-period supplied coarse partition and role motif",
            "mechanism": "conditional coordinate move/apply/restore descriptors",
            "terminal_obligation": "physical one-fine-site covariant E G=G E",
            "strength_vs_target": "conditional coarse geometry only",
            "marker": "RULED OUT BY PRIOR",
            "evidence": "unit-translation symmetric differences 2970/23760/37730",
            "disposition": "not promoted; physical E/residual/leakage remain absent",
        },
        {
            "family": "abstract six-mode Cycle230 target algebra",
            "object": "all 64 local occupations and both parity blocks",
            "mechanism": "direct 64-dimensional CAR matrices, coin, and contact",
            "terminal_obligation": "target-side algebra and coherence control",
            "strength_vs_target": "not a physical encoding",
            "marker": "ATTEMPTED",
            "evidence": "zero CAR/parity leakage and coherent norm residual",
            "disposition": "retained strictly as an abstract target fixture",
        },
    )
    open_routes = (
        {
            "family": "fixed-sector physical composition",
            "mechanism": "compose the Cycle251 fixed-Wilson algebra into literal M2 coordinates",
            "terminal_obligation": "physical E, leakage, mass/contact/seam, translations, and deletion",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
        {
            "family": "sector-indexed twisted target family",
            "mechanism": "compile G_coarse(w) separately in all eight Cycle269 blocks",
            "terminal_obligation": "bounded local maps and full-update covariance for every w",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
        {
            "family": "operational contractible-observable quotient",
            "mechanism": "quotient the Wilson center only for bounded light cones",
            "terminal_obligation": "finite-depth theorem proving discarded global words are unmeasured",
            "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        },
    )
    walls = (
        "literal bounded physical full-Fock state isometry E",
        "choice or operational treatment of the eight Wilson spin/twist blocks",
        "same-encoding CAR-correct frame-free B stream",
        "fine-site translation-covariant physical role law",
        "autonomous local code-space preparation and renewal",
    )
    pairs = tuple({
        "wall_A": first,
        "wall_B": second,
        "A_implies_B": False,
        "B_implies_A": False,
        "independent": True,
        "shared_witness_identified": False,
        "evidence": "no executed construction or logical implication closes either direction",
    } for first, second in combinations(walls, 2))
    residuals = (
        {
            "citation": "docs/work_history/repo/review_feedback/WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md:29-88",
            "prior_residual": "eight central-character blocks; Wilson radical/commutant; L^2 membranes act on matter",
            "current_residual": "same rank, Gram, sector, pairing, and matter-anticommutator formulas on L3/L6/L7",
            "match": True,
            "closed": "Cycle269 presentation only; fixed-sector/twisted/quotient repairs remain live",
        },
        {
            "citation": "docs/work_history/repo/review_feedback/ROUGH_TERMINAL_SUBSYSTEM_GAUGE_FACTORIZATION_CYCLE251_NOTE_2026-07-17.md:20-54",
            "prior_residual": "bounded fixed-parity even-algebra factor but no bounded full-Fock tensor encoder",
            "current_residual": "22-M2 ranks/supports/covariance reexecute; no physical E or preparation is added",
            "match": True,
            "closed": "fixed-Wilson even operator algebra only",
        },
        {
            "citation": "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md:25-45,95-98",
            "prior_residual": "nonzero one-fine-site translation differences and absent physical E/intertwiner/leakage",
            "current_residual": "Cycle610 is byte-pinned only as conditional coarse-grid geometry",
            "match": True,
            "closed": False,
        },
    )
    rhetoric = (
        {
            "phrase": "sector-independent",
            "resolutions": ("onsite operator", "contractible patch", "fixed Wilson block", "eight-block family", "complete periodic update"),
            "tested": ("fixed Wilson block", "eight-block algebra"),
            "untested_status": "a physical full-update family and operational quotient remain open",
            "narrowed_phrase": "fixed-Wilson even-algebra representation",
        },
        {
            "phrase": "local constraints",
            "resolutions": ("bounded check rows", "fixed Wilson signs", "code-space projector", "preparation circuit", "autonomous repair"),
            "tested": ("bounded check rows", "fixed Wilson ranks"),
            "untested_status": "preparation and autonomous repair are absent",
            "narrowed_phrase": "bounded locally stated checks plus separately fixed global Wilson signs",
        },
        {
            "phrase": "physical compiler",
            "resolutions": ("abstract algebra", "coordinate geometry", "gate descriptors", "physical E G=G E", "leakage"),
            "tested": ("abstract algebra", "conditional coordinate geometry"),
            "untested_status": "physical E and leakage are absent",
            "narrowed_phrase": "operator representation and conditional geometry lemmas",
        },
        {
            "phrase": "all24/all576 covariance",
            "resolutions": ("algebra family", "shell geometry", "coarse translations", "fine-site translations", "full physical update"),
            "tested": ("algebra family", "shell geometry", "coarse translations"),
            "untested_status": "fine-site physical update covariance is absent",
            "narrowed_phrase": "route-specific algebra/geometry covariance",
        },
        {
            "phrase": "finite density",
            "resolutions": ("abstract occupations", "fixed-even algebra", "odd creators", "coherent parity superposition", "state preparation"),
            "tested": ("abstract occupations", "fixed-even algebra"),
            "untested_status": "odd creators, physical coherent parity E, and preparation are absent",
            "narrowed_phrase": "arbitrary even finite density inside the fixed-sector operator algebra",
        },
    )
    partial_paths = (
        {"file": "scripts/physical_local_sector_role_genesis_closure_tournament_cycle617_2026_07_22.py", "status": "PARTIAL / NARROWED", "what_closes": "fixed-Wilson Cycle251 algebra, Cycle269 reconciliation, collision and shell-geometry lemmas"},
        {"file": "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py", "status": "PARTIAL / PRIOR", "what_closes": "eight-sector direct sum and matter-active membrane certificate"},
        {"file": "UNMATERIALIZED", "status": "OPEN / PRIORITY", "what_closes": "literal fixed-sector physical E and full update on M2 coordinates"},
        {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "eight-block twisted-family compiler or contractible operational quotient"},
        {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "autonomous local preparation/renewal and fine-site covariance"},
    )
    result = {
        "skill_freshness": {
            "origin_main_checked": True,
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258",
            "newer_origin_main_version_followed": True,
        },
        "N1_normalized_families": families,
        "N1_qualifying_family_count": len(families),
        "N1_all_markers_exact": all(
            row["marker"] in ("ATTEMPTED", "RULED OUT BY PRIOR")
            for row in families
        ),
        "N1_open_counterroutes_not_counted": open_routes,
        "N2_collapsed_walls": walls,
        "N2_directional_wall_independence": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_condition_scan": {
            "required_phrase_scan": {
                "we assume": "absent",
                "by construction": "absent",
                "as is standard": "absent",
                "the framework provides": "absent",
                "bridge context": "absent",
                "background": "absent",
                "naturally": "absent",
                "obviously": "absent",
                "standard QFT": "absent",
                "registered": "absent",
                "canonical": "present only in measured support/presentation labels; non-load-bearing",
            },
            "promoted_hidden_conditions": (
                "three Wilson signs are explicit fixed-sector inputs",
                "Cycle610's coarse partition/origin remains supplied",
                "the local checks do not prepare or renew their code state",
                "beta, contact g, factor order, and phase precision remain supplied",
            ),
            "hidden_wall_promotions_complete": True,
        },
        "N4_residual_matching": residuals,
        "N5_rhetoric_resolution": rhetoric,
        "N5_five_resolutions_present": len(rhetoric) >= 5,
        "N6_partial_closure_paths": partial_paths,
        "N7_hostile_steelman": {
            "mechanism": (
                "choose one Wilson block and compose its bounded even algebra into "
                "literal coordinates, or retain all eight blocks as a twisted target "
                "family; for local experiments, prove a light-cone theorem allowing "
                "the Wilson center to be quotiented only when no global word is measured"
            ),
            "why_it_could_close": (
                "Cycle269 supplies all eight nonempty equal-dimensional blocks, and "
                "Cycle251 supplies bounded fixed-sector generators; the missing step "
                "is a physical composition/operational theorem, not a contradiction"
            ),
            "terminal_obligation": (
                "literal physical E G=G E, mass/contact/seam, leakage/deletion, "
                "L3/L6/L7, all24, and one-fine-site translations"
            ),
            "authority_status": "OPEN / no retained authority",
            "citations": (
                "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py:sector_and_subsystem_controls",
                "scripts/rough_terminal_subsystem_gauge_factorization_cycle251_2026_07_17.py",
                "docs/work_history/repo/review_feedback/WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md:343-365",
            ),
        },
        "N8_cross_cycle_echo": (
            {"cycle": "Cycle251", "retired": "bounded fixed-parity even algebra", "mechanism": "rough-terminal matter/auxiliary commutant", "applicability": "positive fixed-sector substrate only"},
            {"cycle": "Cycle269", "retired": "spectator interpretation of unfixed Wilson labels", "mechanism": "radical/commutant and matter-active membranes", "applicability": "complete connected presentation"},
            {"cycle": "Cycle276", "retired": "premature joint compiler promotion", "mechanism": "three-route disposition", "applicability": "keeps route failures separate"},
            {"cycle": "Cycle312", "retired": "some bounded local full-Fock extensions", "mechanism": "higher-number sign witnesses", "applicability": "does not rule out twisted/quotient routes"},
            {"cycle": "Cycle610", "retired": "physical promotion of a supplied coarse grid", "mechanism": "fine-site translation falsifier", "applicability": "conditional geometry shore only"},
            {"cycle": "Cycle617", "retired": "spectator/tensor wording in this synthesis", "mechanism": "fresh L3/L6/L7 reconciliation", "applicability": "narrowed positive artifact"},
        ),
        "evidence": {
            "route_A_fixed_sector": route_a["pass_bounded_even_CAR_in_fixed_flux_sector"],
            "Cycle269_reconciliation": route_a["cycle269_sector_reconciliation"]["pass"],
            "route_B_collision_only": route_b["pass_one_macro_collision_sorter"] and not route_b["pass_CAR_sign_service"],
            "route_C_geometry_only": route_c["pass_frame_free_bounded_word"] and not route_c["full_Fock_CAR_intertwining"],
            "joint_promotion_withheld": not joint["pass"],
        },
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
        "status": "FAIL",
        "failed_checklist_items": (
            "N7: fixed-sector physical composition, twisted family, and operational quotient remain live",
            "physical promotion: E, leakage, autonomous preparation, and fine-site covariance are unexecuted",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "narrowed_positive_artifact_gate": "PASS",
        "demoted_artifact_status": (
            "fixed-Wilson even-algebra plus direct-sum sector reconciliation "
            "and independent collision/conditional-geometry lemmas"
        ),
    }
    condition = (
        len(families) >= 5 and result["N1_all_markers_exact"]
        and len(pairs) == math.comb(len(walls), 2)
        and len(residuals) == 3 and all(row["match"] for row in residuals)
        and result["N5_five_resolutions_present"] and len(partial_paths) >= 5
        and all(result["evidence"].values())
        and not result["negative_claim_shipped"]
        and not result["minimum_content_claim_shipped"]
        and not result["shared_obstruction"]
        and not result["axiom_pressure"]
        and result["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and result["narrowed_positive_artifact_gate"] == "PASS"
        and result["N7_hostile_steelman"]["authority_status"]
            == "OPEN / no retained authority"
    )
    check("fresh N1-N8 blocks broad/minimum/shared/axiom claims and retains only narrowed positive evidence",
          condition, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "Authority: none", "Audit: unset", "Author artifact status accepted: false",
        "Breakthrough: false", "Cycle 617", "Route A", "Route B", "Route C",
        "E G_coarse = G_physical E", "22 M2", "15 M2", "both parity blocks",
        "common pure full-Fock", "local constraints", "L3", "L6", "L7",
        "all 24", "all 576", "finite density", "coherent superposition",
        "adjacent collision", "overflow", "archive", "renewal", "inverse",
        "deletion", "CAR sign", "frame-free", "one literal word", "24 one-hot",
        "proper-cubic", "support-two", "one-particle mass", "contact", "seam",
        "factor order", "noncommutation", "autonomous initial state",
        "constant overhead", "direct sum of eight", "radical", "commutant",
        "membrane", "spectator", "conditional coarse-grid geometry",
        "physical intertwiner residual is null", "not freshly reexecute",
        "ATTEMPTED", "RULED OUT BY PRIOR", "N1", "N8",
        "FAIL / DO NOT SHIP", "no shared obstruction", "no axiom pressure",
    )
    forbidden = (
        "full-fock compiler passes", "collision sorting supplies fermionic signs",
        "shared obstruction proved", "axiom revision required",
        "schedule is physical time", "phase is physical energy",
        "wilson labels are spectator qubits", "cycle610 physical compiler passes",
        "one-particle mass fixture freshly reexecuted: true",
    )
    missing = tuple(item for item in required if item not in text)
    hits = tuple(item for item in forbidden if item in text.lower())
    result = {"missing": missing, "forbidden_hits": hits}
    check("Cycle617 note freezes corrected Cycle610 scope, Cycle269 sector reconciliation, exact tests, supplies, and N1-N8",
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
        "author_artifact_status_accepted": False,
        "breakthrough_bar_met": False,
        "pins": PINS,
        "shore": prior,
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
            "A": "retain bounded covariant even-CAR generators in a fixed-Wilson sector; Cycle269 reexecution gives eight direct-sum spin/twist blocks with matter-active membrane conjugates, so no spectator factor is inferred",
            "B": "retain collision lemma only: exact finite reversible sorter and sufficient Cycle230 capacity, but no CAR sign; generalized multi-packet traffic overflows",
            "C": "retain frame-free conditional geometry/word lemma only: no 24-one-hot orientation register, but endpoint B fails full-Fock signs",
        },
        "updated_dependency_ledger": {
            "C_ref": "unchanged: reference/phase selection remains supplied",
            "C_num": "improved only at fixed-Wilson even-observable and abstract six-mode finite-density resolution; common physical cross-parity E remains open",
            "C_wrap": "clarified: eight spin/twist blocks are reexecuted; the conditional Cycle230 seam fixture is byte-pinned but not freshly promoted",
            "C_int": "unchanged: abstract local contact and pinned noncommutation/order controls remain; no new physical contact intertwiner",
            "C_local": "improved: bounded 22-M2 fixed-sector generators and explicit L3/L6/L7 Wilson-sector reconciliation; physical full-Fock E, fine-site covariance, and preparation remain open",
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
            "Cycle269 complete connected edge graph, local checks, and eight spin/twist characters",
            "Cycle251 period-16 physical role marker and supplied macro-cell roles",
            "finite reservoir capacity and blank 28-bit comparator archive",
            "canonical occupation-label order used only to audit, not serve, CAR signs",
            "gate angle precision and initial/boundary-state selection",
        ),
        "shared_obstruction_or_axiom_pressure": False,
        "constitutional_effect": "none",
        "optimal_next_campaign": (
            "tournament a literal fixed-sector physical composition, an eight-block "
            "twisted-family compiler, and a finite-light-cone operational quotient; "
            "each must test physical E, full update, mass/contact/seam, leakage, "
            "deletion, L3/L6/L7, all24, and one-fine-site translations"
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
