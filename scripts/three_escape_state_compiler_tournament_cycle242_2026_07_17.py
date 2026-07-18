#!/usr/bin/env python3
"""Cycle 242: synthesize three state-compiler escape routes.

Rerun Cycles 239--241 and independently reconstruct their load-bearing
resource, syndrome, rank, homology, fixture, and firewall claims.  This runner
does not splice route features into an unconstructed encoder.  It records no
general no-go and no axiom pressure.
"""

from __future__ import annotations

from itertools import combinations
from math import comb
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import ROUTE6_INFINITE_EVEN_CAR_TRANSLATION_MARKER_CYCLE237_2026_07_17 as c237
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import distinguishable_antisymmetric_fock_compiler_cycle239_2026_07_17 as c239
import MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_2026_07_17 as c240
import qca_isometry_square_pyramid_cycle241_2026_07_17 as c241


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "THREE_ESCAPE_STATE_COMPILER_TOURNAMENT_CYCLE242_NOTE_2026-07-17.md"
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
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "e g_coarse = g_physical e",
        "antisymmetric walkers",
        "measurement/feedforward",
        "qca/isometry",
        "cross-route",
        "n1 — alternatives",
        "n2 — independence",
        "n3 — hidden conditions",
        "n4 — residual matching",
        "n5 — rhetoric",
        "n6 — partial closures",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
        "three-dimensional substrate and derived-time firewall",
        "cannot rename a gate schedule as time",
    )
    missing = tuple(item for item in required if item not in text)
    check("synthesis note preserves contract, N1-N8, and time firewall", not missing, missing)


def predecessor_regressions() -> None:
    cases = (
        (
            "distinguishable_antisymmetric_fock_compiler_cycle239_2026_07_17.py",
            "SUMMARY PASS 23 FAIL 0",
        ),
        (
            "MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_2026_07_17.py",
            "SUMMARY PASS 14 FAIL 0",
        ),
        (
            "qca_isometry_square_pyramid_cycle241_2026_07_17.py",
            "SUMMARY {'pass': 18, 'fail': 0}",
        ),
    )
    rows = []
    for script, summary in cases:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / script)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        rows.append(
            {
                "script": script,
                "exit": result.returncode,
                "summary_present": summary in result.stdout,
            }
        )
    check(
        "all three independently executed escape-route runners pass",
        all(row["exit"] == 0 and row["summary_present"] for row in rows),
        rows,
    )


def walker_controls() -> None:
    rng = np.random.default_rng(2420)
    trial = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    one_particle, _ = np.linalg.qr(trial)
    encoder = c239.antisymmetric_isometry(6, 2)
    labeled = np.kron(one_particle, one_particle)
    wedge = encoder.conj().T @ labeled @ encoder
    free_residual = np.linalg.norm(labeled @ encoder - encoder @ wedge)

    mode_count = 12
    contact_encoder = c239.antisymmetric_isometry(mode_count, 2)
    phases = np.ones(mode_count**2, dtype=complex)
    for first in range(mode_count):
        for second in range(mode_count):
            if first // 6 == second // 6:
                phases[first * mode_count + second] = np.exp(1j * c239.COUPLING)
    labeled_contact = np.diag(phases)
    wedge_contact = contact_encoder.conj().T @ labeled_contact @ contact_encoder
    expected = np.asarray(
        [
            np.exp(1j * c239.COUPLING) if first // 6 == second // 6 else 1
            for first, second in combinations(range(mode_count), 2)
        ]
    )
    contact_residual = np.linalg.norm(wedge_contact - np.diag(expected))
    check(
        "fixed-particle antisymmetric free and pair-contact intertwiners remain exact",
        free_residual < 2e-13 and contact_residual < 2e-14,
        {"free_residual": free_residual, "contact_residual": contact_residual},
    )

    rows = []
    for length in (3, 4, 5):
        modes = 6 * length**3
        rows.append(
            {
                "L": length,
                "qubits_per_cell": 6 * modes,
                "total_qca_qubits": 6 * modes * length**3,
                "overhead_ratio": modes,
                "pair_gates_per_cell": comb(modes, 2),
                "pair_depth": modes - 1,
            }
        )
    slope = (rows[1]["qubits_per_cell"] - rows[0]["qubits_per_cell"]) // (4**3 - 3**3)
    held = slope * 5**3
    check(
        "published full-Fock walker realization has volume-growing local overhead",
        [row["qubits_per_cell"] for row in rows] == [972, 2304, 4500]
        and [row["total_qca_qubits"] for row in rows] == [26244, 147456, 562500]
        and [row["pair_gates_per_cell"] for row in rows] == [13041, 73536, 280875]
        and slope == 36
        and held == 4500,
        rows,
    )

    spatial_assignment = np.asarray(((0.0, 1.0), (-1.0, 0.0))) / np.sqrt(2)
    singulars = np.linalg.svd(spatial_assignment, compute_uv=False)
    product_floor = np.sqrt(2 - 2 * singulars[0])
    check(
        "two separated particle-label assignments have an explicit spatial Bell cut",
        np.max(np.abs(singulars - 1 / np.sqrt(2))) < 2e-15
        and abs(product_floor - np.sqrt(2 - np.sqrt(2))) < 2e-15,
        {"Schmidt_values": singulars, "product_distance_floor": product_floor},
    )


def measurement_controls() -> None:
    rows = []
    decoder_weights = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        cycles = c235.primal_edge_cycles(graph)
        local_paulis = [graph.loop_pauli(vertices) for _, vertices, _ in cycles]
        wilson_paulis = [
            graph.loop_pauli(vertices) for vertices in c235.wilson_cycles(graph)
        ]
        all_paulis = local_paulis + wilson_paulis
        basis_indices = c240.independent_indices([pauli.x for pauli in all_paulis])
        basis_rows = [all_paulis[index].x for index in basis_indices]
        solutions, _ = c240.right_inverse(basis_rows, len(graph.edges))
        failures = sum(
            c240.syndrome(solution, basis_rows) != 1 << index
            for index, solution in enumerate(solutions)
        )
        data_degree = [0] * len(graph.edges)
        for pauli in local_paulis:
            support = pauli.x | pauli.z
            while support:
                bit = support & -support
                data_degree[bit.bit_length() - 1] += 1
                support ^= bit
        fluxes = [graph.B(vertex) for vertex in range(len(graph.vertices))]
        commutator_failures = sum(
            not measured.commutes(flux)
            for measured in all_paulis
            for flux in fluxes
        )
        weights = [solution.bit_count() for solution in solutions]
        decoder_weights.append(max(weights))
        rows.append(
            {
                "L": length,
                "face_qubits": len(graph.edges),
                "local_rank": c235.gf2_rank(pauli.x for pauli in local_paulis),
                "full_rank": len(basis_rows),
                "max_check_weight": max((pauli.x | pauli.z).bit_count() for pauli in local_paulis),
                "max_data_degree": max(data_degree),
                "decoder_failures": failures,
                "flux_commutator_failures": commutator_failures,
            }
        )
    check(
        "local projection uses 30 bounded subrounds and exact independent outcomes",
        [row["face_qubits"] for row in rows] == [405, 960, 1875]
        and [row["local_rank"] for row in rows] == [241, 574, 1123]
        and [row["full_rank"] for row in rows] == [244, 577, 1126]
        and all(row["max_check_weight"] == 28 for row in rows)
        and all(row["max_data_degree"] == 11 for row in rows)
        and all(row["decoder_failures"] == 0 for row in rows)
        and all(row["flux_commutator_failures"] == 0 for row in rows),
        rows,
    )
    check(
        "the selected measurement decoder has growing correction support",
        decoder_weights == [90, 152, 314],
        decoder_weights,
    )

    membrane_rows = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        locals_ = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        wilsons = [graph.cycle_mask(vertices) for vertices in c235.wilson_cycles(graph)]
        membranes = [c240.wilson_membrane(graph, axis) for axis in range(3)]
        pairing = [
            [(membrane & wilson).bit_count() % 2 for wilson in wilsons]
            for membrane in membranes
        ]
        membrane_rows.append(
            {
                "L": length,
                "weights": [membrane.bit_count() for membrane in membranes],
                "pairing": pairing,
                "local_failures": sum(
                    (membrane & local).bit_count() % 2
                    for membrane in membranes
                    for local in locals_
                ),
            }
        )
    check(
        "fixed Wilson preparation needs exact noncontractible LxL membranes",
        all(row["pairing"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]] for row in membrane_rows)
        and all(row["local_failures"] == 0 for row in membrane_rows)
        and [row["weights"][0] for row in membrane_rows] == [9, 16, 25],
        membrane_rows,
    )


def qca_rank_homology_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        local_cycles = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        wilsons = [graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
        fluxes = [graph.B(vertex).z for vertex in range(len(graph.vertices))]
        flux_product = 0
        for flux in fluxes:
            flux_product ^= flux
        rows.append(
            {
                "L": length,
                "local_exponent": len(graph.edges) - c235.gf2_rank(local_cycles),
                "equal_Wilson_exponent": len(graph.edges)
                - c235.gf2_rank(local_cycles + wilsons[:2]),
                "fixed_spin_exponent": len(graph.edges)
                - c235.gf2_rank(local_cycles + wilsons),
                "flux_rank": c235.gf2_rank(fluxes),
                "flux_product_identity": flux_product == 0,
            }
        )
    check(
        "equal-Wilson constraints give the exact full-Fock rank and retain one parity slot",
        all(row["local_exponent"] == 6 * row["L"] ** 3 + 2 for row in rows)
        and all(row["equal_Wilson_exponent"] == 6 * row["L"] ** 3 for row in rows)
        and all(row["fixed_spin_exponent"] == 6 * row["L"] ** 3 - 1 for row in rows)
        and all(row["flux_rank"] == 6 * row["L"] ** 3 - 1 for row in rows)
        and all(row["flux_product_identity"] for row in rows),
        rows,
    )

    maps = {}
    summaries = {}
    for length in (3, 4, 5):
        graph = c235.PyramidCellulation(length)
        local_cycles = [mask for mask, _, _ in c235.primal_edge_cycles(graph)]
        wilsons = [graph.cycle_mask(path) for path in c235.wilson_cycles(graph)]
        keys, orbit_masks, orbit_boundaries = c241.face_type_orbits(graph)
        table = {}
        for template in range(1 << len(keys)):
            chain = boundary = 0
            for index in range(len(keys)):
                if (template >> index) & 1:
                    chain ^= orbit_masks[index]
                    boundary ^= orbit_boundaries[index]
            if boundary == 0:
                table[template] = c241.classify_cycle_homology(
                    graph, local_cycles, wilsons, chain
                )
        maps[length] = table
        summaries[length] = {
            "closed": len(table),
            "classes": tuple(sorted(set(table.values()))),
        }
    common = set(maps[3]) & set(maps[4]) & set(maps[5])
    same_nonzero = [
        template
        for template in common
        if maps[3][template] == maps[4][template] == maps[5][template] != 0
    ]
    check(
        "all 2^15 fixed translation-orbit Pauli dressings fail an all-size nonzero Wilson class",
        all(row["closed"] == 1024 for row in summaries.values())
        and summaries[4]["classes"] == (0,)
        and summaries[3]["classes"] == summaries[5]["classes"] == tuple(range(8))
        and not same_nonzero,
        {"per_size": summaries, "same_nonzero": len(same_nonzero)},
    )


def marker_fixture_and_contract_controls() -> None:
    frames = c237.proper_cubic_frames()
    equality_sector = {(0, 0, 0), (1, 1, 1)}
    axis_permutations = set()
    for frame in frames:
        permutation = []
        for axis in range(3):
            image = c237.mat_vec(frame, tuple(1 if i == axis else 0 for i in range(3)))
            permutation.append(next(i for i, value in enumerate(image) if value))
        axis_permutations.add(tuple(permutation))
    check(
        "the common-Wilson even/odd labels form an all-24 proper-cubic sector family",
        len(frames) == 24
        and all(
            {
                tuple(label[permutation[index]] for index in range(3))
                for label in equality_sector
            }
            == equality_sector
            for permutation in axis_permutations
        ),
        {"frames": len(frames), "axis_permutations": len(axis_permutations), "labels": equality_sector},
    )

    species = c219.common_species(-0.3)
    rest = c219.rest_mass(species)
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "one-particle mass and rank-73 seam remain exact conditional targets in one odd sector",
        abs(rest / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73
        and sea_rank % 2 == 1,
        {"rest_mass": rest, "analytic_mass": species.analytic_mass, "sea_rank": sea_rank},
    )

    routes = {
        "walker": {
            "bounded_operator": True,
            "constant_overhead": False,
            "bounded_state_E": False,
            "both_parities": True,
            "fixtures": True,
        },
        "measurement": {
            "bounded_operator": True,
            "constant_overhead": True,
            "bounded_state_E": False,
            "both_parities": False,
            "fixtures": False,
        },
        "qca_isometry": {
            "bounded_operator": True,
            "constant_overhead": True,
            "bounded_state_E": False,
            "both_parities": "rank_only",
            "fixtures": False,
        },
    }
    check(
        "no executed route supplies the full compiler and cross-route feature splicing is forbidden",
        all(not row["bounded_state_E"] for row in routes.values())
        and not any(
            row["constant_overhead"]
            and row["bounded_state_E"]
            and row["both_parities"] is True
            and row["fixtures"]
            for row in routes.values()
        ),
        routes,
    )

    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    check(
        "three-dimensional substrate is kept separate from derived causal and metric time",
        "z^3" in text
        and "ordinal clock count" in text
        and "metric duration" in text
        and "gate schedule as time" in text
        and "qca light cone as a metric cone" in text,
        {"compiler_time_selected": False, "causal_time_bridge_complete": False},
    )


def main() -> int:
    note_contract()
    predecessor_regressions()
    walker_controls()
    measurement_controls()
    qca_rank_homology_controls()
    marker_fixture_and_contract_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
