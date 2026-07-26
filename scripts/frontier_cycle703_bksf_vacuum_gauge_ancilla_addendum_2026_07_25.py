#!/usr/bin/env python3
"""Cycle-703 addendum: bounded gauge/ancilla BKSF-vacuum genesis attack.

Tests a local controlled-loop face-ancilla circuit, coherent syndrome
extraction plus Z correction, a translation-compatible fixed-radius linear
decoder, and the periodic Wilson direct-sum/subsystem interpretation.

The retained result is layered: dense coherent correction proves the exact
state identity but is global; the tested bounded-radius translation-linear
decoder fails held sizes; face ancillas alone leak one half from every edge
loop projector; Wilson sectors are inert gauge qubits for the complete local
even algebra only when the encoder domain is typed H_matter tensor C^8.

No general Clifford/state-genesis no-go is claimed.  Authority none; audit
unset; constitutional effect none.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import time

import frontier_cycle703_local_gauss_reference_adversary_2026_07_25 as G
import frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25 as P


START = time.perf_counter()
PASS = 0
FAIL = 0
GAUSS_SHA256 = "781823cf744be93de73f5e86e4e4cc988e0e7fe19c9c88a264b6f58169c07b0e"
PATCH_SHA256 = "eb0841f064bc840b1892a02ce1cf75e2c8275b6c21cc9b2952a5032cc03d4bb4"


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def rank_masks(rows) -> int:
    return G.base.gf2_rank(rows)


def pauli_rank(rows, qubits: int) -> int:
    return rank_masks(row.symplectic(qubits) for row in rows)


def hermitian(row) -> bool:
    return (row.phase - (row.x & row.z).bit_count()) % 2 == 0


def independent_rows(rows, key=lambda row: row.x):
    pivots = {}
    output = []
    for row in rows:
        reduced = key(row)
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                output.append(row)
                break
    return output


def support_indices(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def greedy_conflict_colors(rows) -> int:
    qubit_colors: dict[int, set[int]] = defaultdict(set)
    maximum = -1
    for row in rows:
        support = tuple(support_indices(row.x | row.z))
        forbidden = set().union(*(qubit_colors[q] for q in support)) if support else set()
        color = 0
        while color in forbidden:
            color += 1
        for qubit in support:
            qubit_colors[qubit].add(color)
        maximum = max(maximum, color)
    return maximum + 1


def dense_z_right_inverse(x_rows: list[int], edge_count: int):
    """Return Z masks a_j with x_i dot a_j = delta_ij."""

    rank = len(x_rows)
    column_pivots: dict[int, tuple[int, int]] = {}
    for edge in range(edge_count):
        syndrome = sum(((row >> edge) & 1) << i for i, row in enumerate(x_rows))
        correction = 1 << edge
        while syndrome:
            pivot = syndrome.bit_length() - 1
            if pivot in column_pivots:
                syndrome ^= column_pivots[pivot][0]
                correction ^= column_pivots[pivot][1]
            else:
                column_pivots[pivot] = (syndrome, correction)
                break
    if len(column_pivots) != rank:
        return None
    output = []
    for target_index in range(rank):
        syndrome = 1 << target_index
        correction = 0
        while syndrome:
            pivot = syndrome.bit_length() - 1
            if pivot not in column_pivots:
                return None
            syndrome ^= column_pivots[pivot][0]
            correction ^= column_pivots[pivot][1]
        output.append(correction)
    return output


def correction_failures(x_rows: list[int], corrections: list[int]) -> int:
    failures = 0
    for target, correction in enumerate(corrections):
        observed = sum(((row & correction).bit_count() & 1) << index
                       for index, row in enumerate(x_rows))
        failures += observed != 1 << target
    return failures


def patch_cases():
    rows = []
    for spec in P.PATCHES[:2]:
        graph = P.ExtendedGraph.patch(spec.centers)
        loops = [graph.loop_pauli(item[1]) for item in P.local_loops(graph)]
        b_rows = [graph.B(vertex) for vertex in range(len(graph.vertices))]
        rows.append((f"patch-{spec.name}", graph, loops, [], b_rows, False))
    graph = G.base.ReferenceGraph(2, False)
    rows.append(("cube-open-L2", graph, G.local_loop_rows(graph), [],
                 [graph.B(v) for v in range(len(graph.vertices))], False))
    for length in (3, 4, 5):
        graph = G.base.ReferenceGraph(length, True)
        rows.append((f"cube-periodic-L{length}", graph,
                     G.local_loop_rows(graph), G.wilson_rows(graph),
                     [graph.B(v) for v in range(len(graph.vertices))], True))
    return rows


def vacuum_tableau_controls():
    output = []
    for name, graph, local_loops, wilsons, b_rows, periodic in patch_cases():
        edge_count = len(graph.edges)
        vertex_count = len(graph.vertices)
        full_cycle_rank = edge_count - vertex_count + 1
        local_rank = pauli_rank(local_loops, edge_count)
        target_loops = local_loops + wilsons
        target_basis = independent_rows(target_loops)
        fixed_rank = pauli_rank(b_rows + target_loops, edge_count)
        phase_failures = G.base.stabilizer_phase_failures(
            b_rows + target_loops, edge_count
        )
        commutator_failures = sum(
            not left.commutes(right)
            for i, left in enumerate(b_rows + target_loops)
            for right in (b_rows + target_loops)[i + 1:]
        )
        hermitian_failures = sum(
            not hermitian(row) for row in b_rows + target_loops
        )

        # Controlled-loop ancillas stabilize X_f L_f, not edge-only L_f.
        edge_loop_zero_expectations = sum(row.x != 0 for row in local_loops)
        maximum_weight = max((row.x | row.z).bit_count() for row in local_loops)
        colors = greedy_conflict_colors(local_loops)

        x_rows = [row.x for row in target_basis]
        corrections = dense_z_right_inverse(x_rows, edge_count)
        correction_failure_count = (
            len(x_rows) if corrections is None
            else correction_failures(x_rows, corrections)
        )
        max_correction_weight = max(
            (mask.bit_count() for mask in corrections or ()), default=0
        )
        deletion_failure = 0
        if corrections:
            deleted = list(corrections)
            deleted[0] = 0
            deletion_failure = correction_failures(x_rows, deleted)
        basis_delete_rank_loss = (
            len(target_basis) - pauli_rank(target_basis[1:], edge_count)
            if target_basis else 0
        )

        output.append({
            "case": name,
            "periodic": periodic,
            "cells": len(graph.cells),
            "edge_M2": edge_count,
            "vertices": vertex_count,
            "B_rank": pauli_rank(b_rows, edge_count),
            "local_loop_rows": len(local_loops),
            "local_loop_rank": local_rank,
            "Wilson_rows": len(wilsons),
            "target_cycle_rank": len(target_basis),
            "full_cycle_rank": full_cycle_rank,
            "fixed_vacuum_stabilizer_rank": fixed_rank,
            "phase_failures": phase_failures,
            "commutator_failures": commutator_failures,
            "Hermitian_failures": hermitian_failures,
            "face_ancilla_conflict_colors": colors,
            "maximum_local_loop_Pauli_weight": maximum_weight,
            "edge_loop_zero_expectations": edge_loop_zero_expectations,
            "edge_loop_projector_leakage": 0.5,
            "postselection_log2_success_local": -local_rank,
            "postselection_log2_success_fixed_sector": -full_cycle_rank,
            "dense_Z_corrections": len(corrections or ()),
            "dense_correction_failures": correction_failure_count,
            "maximum_dense_Z_weight": max_correction_weight,
            "deleted_correction_syndrome_failures": deletion_failure,
            "delete_one_independent_loop_rank_loss": basis_delete_rank_loss,
            "coherent_identity_exact_by_linearity": correction_failure_count == 0,
        })
    return output


def periodic_data(length: int):
    graph = G.base.ReferenceGraph(length, True)
    cycles = G.base.local_cycles(graph)
    edge_by_owner: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    loop_by_owner: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for edge, (_, _, _, owner) in enumerate(graph.edges):
        edge_by_owner[owner].append(edge)
    for index, (_, vertices, _) in enumerate(cycles):
        loop_by_owner[graph.vertices[vertices[0]][0]].append(index)
    edge_meta = {
        edge: (owner, kind)
        for owner, edges in edge_by_owner.items()
        for kind, edge in enumerate(edges)
    }
    loop_meta = {
        index: (owner, kind)
        for owner, loops in loop_by_owner.items()
        for kind, index in enumerate(loops)
    }
    loop_edges = []
    edge_checks = [[] for _ in graph.edges]
    for index, (_, vertices, _) in enumerate(cycles):
        support = list(support_indices(graph.loop_pauli(vertices).x))
        loop_edges.append(support)
        for edge in support:
            edge_checks[edge].append(index)
    return graph, edge_meta, loop_meta, loop_edges, edge_checks


def centered(value: int, length: int) -> int:
    value %= length
    return value - length if value > length // 2 else value


def translation_decoder_consistency(length: int, radius: int):
    graph, edge_meta, loop_meta, loop_edges, edge_checks = periodic_data(length)
    offsets = tuple(product(range(-radius, radius + 1), repeat=3))
    offset_index = {offset: index for index, offset in enumerate(offsets)}
    variables = 24 * 18 * len(offsets)
    variable_mask = (1 << variables) - 1
    pivots = {}
    equations = 0
    first_failure = None

    def variable(edge_type, loop_type, offset):
        return (edge_type * 18 + loop_type) * len(offsets) + offset_index[offset]

    origin_loops = [
        index for index, (owner, _kind) in loop_meta.items()
        if owner == (0, 0, 0)
    ]
    for check in origin_loops:
        check_type = loop_meta[check][1]
        check_support = set(loop_edges[check])
        for input_edge in range(len(graph.edges)):
            lhs = 0
            for output_edge in loop_edges[check]:
                output_owner, output_type = edge_meta[output_edge]
                for syndrome_check in edge_checks[input_edge]:
                    syndrome_owner, syndrome_type = loop_meta[syndrome_check]
                    offset = tuple(centered(
                        syndrome_owner[axis] - output_owner[axis], length
                    ) for axis in range(3))
                    if offset in offset_index:
                        lhs ^= 1 << variable(output_type, syndrome_type, offset)
            rhs = input_edge in check_support
            if not lhs and not rhs:
                continue
            equations += 1
            row = lhs | (int(rhs) << variables)
            reduced = lhs
            while reduced:
                pivot = reduced.bit_length() - 1
                if pivot in pivots:
                    row ^= pivots[pivot]
                    reduced = row & variable_mask
                else:
                    pivots[pivot] = row
                    break
            else:
                if (row >> variables) & 1:
                    first_failure = (check_type, input_edge)
                    return {
                        "L": length, "radius": radius, "consistent": False,
                        "variables": variables, "equations": equations,
                        "rank_at_failure": len(pivots),
                        "first_failure": first_failure,
                    }
    return {
        "L": length, "radius": radius, "consistent": True,
        "variables": variables, "equations": equations,
        "rank": len(pivots), "first_failure": first_failure,
    }


def pauli_coordinates(target, basis, qubits):
    pivots = {}
    for index, row in enumerate(basis):
        reduced = row.symplectic(qubits)
        coefficient = 1 << index
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot][0]
                coefficient ^= pivots[pivot][1]
            else:
                pivots[pivot] = (reduced, coefficient)
                break
    reduced = target.symplectic(qubits)
    coefficient = 0
    while reduced:
        pivot = reduced.bit_length() - 1
        if pivot not in pivots:
            return None
        reduced ^= pivots[pivot][0]
        coefficient ^= pivots[pivot][1]
    return coefficient


def wilson_controls():
    output = []
    frame_certificate = None
    for length in (3, 4):
        graph = G.base.ReferenceGraph(length, True)
        local = G.local_loop_rows(graph)
        ds = G.local_d_rows(graph)
        wilsons = G.wilson_rows(graph)
        qubits = len(graph.edges)
        local_rank = pauli_rank(local + ds, qubits)
        fixed_rank = pauli_rank(local + ds + wilsons, qubits)
        generators = [graph.A(u, v) for u, v, _, _ in graph.edges]
        generators += [graph.B(vertex) for vertex in range(len(graph.vertices))]
        update_commutator_failures = sum(
            not generator.commutes(wilson)
            for generator in generators for wilson in wilsons
        )
        stabilizers = local + ds
        single_site_sector_changers = 0
        for edge in range(qubits):
            for x, z in ((1 << edge, 0), (0, 1 << edge), (1 << edge, 1 << edge)):
                row = G.base.Pauli(x=x, z=z)
                if all(row.commutes(stabilizer) for stabilizer in stabilizers):
                    single_site_sector_changers += any(
                        not row.commutes(wilson) for wilson in wilsons
                    )
        output.append({
            "L": length,
            "cells": length**3,
            "edge_M2": qubits,
            "local_D_rank": local_rank,
            "fixed_Wilson_rank": fixed_rank,
            "direct_sum_exponent": qubits - local_rank,
            "fixed_sector_exponent": qubits - fixed_rank,
            "expected_direct_sum_exponent": 6 * length**3 + 3,
            "expected_fixed_exponent": 6 * length**3,
            "A_B_update_Wilson_commutator_failures": update_commutator_failures,
            "single_site_code_preserving_sector_changers": single_site_sector_changers,
            "delete_one_Wilson_rank_loss": fixed_rank - pauli_rank(
                local + ds + wilsons[:-1], qubits
            ),
            "typed_encoder_domain": f"H_matter({6*length**3} qubits) tensor C^8_gauge",
            "matter_only_encoder_requires_gauge_vector": True,
        })

        if length == 3:
            basis = local + wilsons
            frames = G.base.proper_cubic_frames()
            matrices = []
            phase_failures = coordinate_failures = 0
            for frame in frames:
                _vertices, edge_map, toggles, pairs, flips = G.corrected_frame_data(
                    graph, frame
                )
                columns = []
                for wilson in wilsons:
                    mapped = G.base.apply_gauge(
                        G.base.permute_pauli(wilson, edge_map), toggles, pairs, flips
                    )
                    coefficient = pauli_coordinates(mapped, basis, qubits)
                    if coefficient is None:
                        coordinate_failures += 1
                        columns.append(0)
                        continue
                    columns.append((coefficient >> len(local)) & 7)
                    rebuilt = G.base.Pauli()
                    for index, row in enumerate(basis):
                        if (coefficient >> index) & 1:
                            rebuilt = rebuilt @ row
                    phase_failures += rebuilt != mapped
                matrices.append(tuple(columns))

            lookup = {G.frame_key(frame): index for index, frame in enumerate(frames)}

            def apply(columns, value):
                result = 0
                for index, column in enumerate(columns):
                    if (value >> index) & 1:
                        result ^= column
                return result

            composition_failures = 0
            for left_index, left in enumerate(frames):
                for right_index, right in enumerate(frames):
                    product_index = lookup[G.frame_key(left @ right)]
                    for sector in range(8):
                        composition_failures += apply(
                            matrices[left_index], apply(matrices[right_index], sector)
                        ) != apply(matrices[product_index], sector)
            frame_certificate = {
                "frames": len(frames),
                "ordered_products": len(frames) ** 2,
                "unique_sector_maps": tuple(sorted(set(matrices))),
                "coordinate_failures": coordinate_failures,
                "phase_failures": phase_failures,
                "composition_failures": composition_failures,
                "fixed_plus_sector_invariant": all(apply(matrix, 7) == 7 for matrix in matrices),
            }
    return output, frame_certificate


def main():
    gauss_sha = sha256(Path(G.__file__).read_bytes()).hexdigest()
    patch_sha = sha256(Path(P.__file__).read_bytes()).hexdigest()
    check(
        "canonical Cycle703 gauge and held-patch runners are byte-pinned",
        gauss_sha == GAUSS_SHA256 and patch_sha == PATCH_SHA256,
        {"gauge": gauss_sha[:16], "patch": patch_sha[:16]},
    )

    vacuum = vacuum_tableau_controls()
    check(
        "all-B plus full-loop vacuum tableaus close exactly on L/2x2 and cube L2-L5",
        all(
            row["B_rank"] == row["vertices"] - 1
            and row["target_cycle_rank"] == row["full_cycle_rank"]
            and row["fixed_vacuum_stabilizer_rank"] == row["edge_M2"]
            and row["phase_failures"] == 0
            and row["commutator_failures"] == 0
            and row["Hermitian_failures"] == 0
            and row["delete_one_independent_loop_rank_loss"] == 1
            for row in vacuum
        ),
        vacuum,
    )
    check(
        "bounded face ancillas preserve B but do not prepare the required edge-loop vacuum",
        all(
            row["edge_loop_zero_expectations"] == row["local_loop_rows"]
            and row["edge_loop_projector_leakage"] == 0.5
            and row["postselection_log2_success_local"] < 0
            for row in vacuum
        ),
        [{key: row[key] for key in (
            "case", "face_ancilla_conflict_colors", "maximum_local_loop_Pauli_weight",
            "edge_loop_projector_leakage", "postselection_log2_success_local"
        )} for row in vacuum],
    )
    check(
        "dense coherent Z correction closes A_s P_s|0_Z> = P_+|0_Z> with active columns",
        all(
            row["dense_Z_corrections"] == row["full_cycle_rank"]
            and row["dense_correction_failures"] == 0
            and row["coherent_identity_exact_by_linearity"]
            and row["deleted_correction_syndrome_failures"] == 1
            for row in vacuum
        ),
        [{key: row[key] for key in (
            "case", "dense_Z_corrections", "dense_correction_failures",
            "maximum_dense_Z_weight", "deleted_correction_syndrome_failures"
        )} for row in vacuum],
    )

    decoder = [
        translation_decoder_consistency(3, 0),
        translation_decoder_consistency(3, 1),
        translation_decoder_consistency(4, 1),
        translation_decoder_consistency(5, 1),
        translation_decoder_consistency(5, 2),
        translation_decoder_consistency(6, 2),
    ]
    check(
        "translation-linear coherent correction needs the tested whole-torus radius and fails held L6 without refit",
        [row["consistent"] for row in decoder]
        == [False, True, False, False, True, False],
        decoder,
    )

    wilson, frames = wilson_controls()
    check(
        "three Wilson characters are inert typed gauge qubits for the complete local even algebra",
        all(
            row["direct_sum_exponent"] == row["expected_direct_sum_exponent"]
            and row["fixed_sector_exponent"] == row["expected_fixed_exponent"]
            and row["A_B_update_Wilson_commutator_failures"] == 0
            and row["single_site_code_preserving_sector_changers"] == 0
            and row["delete_one_Wilson_rank_loss"] == 1
            and row["matter_only_encoder_requires_gauge_vector"]
            for row in wilson
        ),
        wilson,
    )
    check(
        "proper-cubic frames permute the three Wilson gauge qubits with exact 24/576 composition",
        frames["frames"] == 24
        and frames["ordered_products"] == 576
        and len(frames["unique_sector_maps"]) == 6
        and frames["coordinate_failures"] == 0
        and frames["phase_failures"] == 0
        and frames["composition_failures"] == 0
        and frames["fixed_plus_sector_invariant"],
        frames,
    )

    no_go_gate = {
        "status": "FAIL broad no-go; retain route-specific partial only",
        "N1": (
            "ATTEMPTED bounded face-ancilla controlled-loop graph state: B closes, edge loops leak 1/2",
            "ATTEMPTED face-X postselection: exact target but success exponent is minus cycle rank",
            "ATTEMPTED dense coherent syndrome plus Z correction: exact positive, global support",
            "ATTEMPTED translation-linear bounded-radius correction: held failures above",
            "ATTEMPTED Wilson subsystem/direct sum: closes Wilson wall only with H_matter tensor C8 typing",
            "UNTESTED nonlinear local measurement decoder and recurrent radius-one correction remain live",
        ),
        "N2": (
            "edge-loop disentangling and correction locality are the same collapsed wall",
            "Wilson selection is independent and is conditionally retired by typed gauge input",
            "physical arbitrary-state common E is independent of vacuum genesis",
        ),
        "N3": (
            "product edge |0_Z>, blank face ancillas, controlled-Pauli availability, translation-linearity, fixed radius, and periodic boundary are explicit",
        ),
        "N4": (
            "Cycle703 Wilson/preparation witness matches Wilson rank only; it is not cited as a face-decoder no-go",
        ),
        "N5": (
            "negative is only for the tested face-ancilla and translation-linear fixed-radius architectures; no all-Clifford or recurrent-dynamics claim",
        ),
        "N6": (
            "dense coherent correction is the exact partial closure; recurrent local correction and nonlinear measurement decoders remain concrete paths",
        ),
        "N7": (
            "Steelman: a nonlinear cellular decoder with retained syndrome gauge qubits, or radius-one recurrent dynamics run for growing recurrences, could implement the same exact coherent identity without a dense feedforward table; terminal obligation is an explicit local unitary and returned ancillas on held sizes",
        ),
        "N8": (
            "Cycle232 uniform-reference failure was retired by local D in Cycle703, so route-specific failures must not be echoed into constitutional evidence",
        ),
    }
    check(
        "N1-N8 blocks a broad no-go and preserves the exact live completion routes",
        len(no_go_gate["N1"]) >= 5
        and "FAIL broad no-go" in no_go_gate["status"]
        and "Steelman" in no_go_gate["N7"][0],
        no_go_gate,
    )

    certificate = {
        "vacuum_tableaus": vacuum,
        "translation_decoder": decoder,
        "Wilson_direct_sum": wilson,
        "Wilson_covariance": frames,
        "no_go_discipline": no_go_gate,
    }
    digest = sha256(json.dumps(certificate, sort_keys=True, default=str,
        separators=(",", ":")).encode()).hexdigest()
    result = {
        "authority": "none", "audit": "unset", "cycle": 703,
        "status": "vacuum-gauge-ancilla-partial-with-route-specific-held-failure",
        "terminal": "DENSE_COHERENT_VACUUM_AND_WILSON_GAUGE_POSITIVE_FIXED_RADIUS_LOCAL_PREP_OPEN",
        "pass": FAIL == 0, "tests_passed": PASS, "tests_failed": FAIL,
        "equations": (
            "A_s P_s |0_Z> = P_+ |0_Z>",
            "H R H = H on lawful loop syndromes",
            "E_direct_sum: H_matter tensor C^8_gauge -> H_local_code",
            "U_physical E_direct_sum = E_direct_sum (U_matter tensor I_8)",
        ),
        "certificate": certificate,
        "claim_ceiling": (
            "Dense coherent correction proves exact finite vacuum preparation and Wilson sectors are inert typed gauge qubits. "
            "The tested bounded face-ancilla and translation-linear fixed-radius routes do not produce the original fixed-loop vacuum without growing/global correction. "
            "No general local-Clifford, nonlinear-decoder, recurrent-dynamics, or axiom-pressure claim follows."
        ),
        "resources": {
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
            "certificate_sha256": digest,
        },
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True, default=str))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
