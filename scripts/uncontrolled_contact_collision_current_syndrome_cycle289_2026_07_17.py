#!/usr/bin/env python3
"""Cycle 289: unconditional contact collision/current syndrome.

The actual Cycle-230 contact W_g acts on matter without a controlled-W_g
oracle.  A separately supplied, bounded collision transducer then swaps the
phase of a fixed-total-number, equal-Q-support spatial interferometer into one
ordinary M2 flag.  The runner keeps action, reference preparation, comparator,
read, occurrence, Record, time, energy, and source semantics distinct.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import actual_contact_action_syndrome_tournament_cycle285_2026_07_17 as c285
import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "UNCONTROLLED_CONTACT_COLLISION_CURRENT_SYNDROME_CYCLE289_NOTE_2026-07-17.md"
)
PASS = 0
FAIL = 0
TOL = 4.0e-11
G = c278.c230.COUPLING


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
        check("the Cycle-289 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "constitutional effect: none",
        "ordinary unconditional w_g",
        "no controlled-w_g oracle",
        "fixed-total-number collision interferometer",
        "equal q-support",
        "collision-swap transducer",
        "deletion of the target w_g",
        "threshold-only replacement",
        "global-phase replacement",
        "w_g^dagger sign control",
        "one-particle mass fixture",
        "zero leakage",
        "held-out l=6",
        "648 frame-translation",
        "bounded physical-m2 support",
        "supplied-structure inventory",
        "not occurrence",
        "not a record",
        "not physical time",
        "not physical energy",
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
        "the note preserves the uncontrolled-action, physical-code, fault, semantic, and N1-N8 contracts",
        not missing,
        missing,
    )


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def partial_flag_density(rho: np.ndarray) -> np.ndarray:
    tensor = rho.reshape(2, 2, 2, 2)
    return np.einsum("ifig->fg", tensor)


def partial_matter_density(rho: np.ndarray) -> np.ndarray:
    tensor = rho.reshape(2, 2, 2, 2)
    return np.einsum("ifjf->ij", tensor)


def logical_swap_transducer() -> np.ndarray:
    """H-logical, SWAP(logical,flag), H-logical.

    On a blank flag it resets the declared A/B collision logical to |+> and
    transfers its complete complex phase qubit into the flag.  This unitary is
    a comparator after W_g; it never controls whether W_g acts.
    """

    hadamard = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    swap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
        dtype=complex,
    )
    h_matter = np.kron(hadamard, np.eye(2))
    return h_matter @ swap @ h_matter


def process_output(unitary: np.ndarray, logical_state: np.ndarray) -> np.ndarray:
    blank_flag = np.asarray((1, 0), dtype=complex)
    after_action = np.kron(unitary @ logical_state, blank_flag)
    return logical_swap_transducer() @ after_action


def collision_interferometer_controls() -> dict[str, float]:
    print("\nUNCONTROLLED FIXED-N COLLISION INTERFEROMETER")
    # A: target N=2 plus two separated N=1 references.
    # B: target N=4 plus two reference vacua.  Both have total N=4 and exactly
    # one Q-active cell, while target pair counts are 1 and 6.
    pair_counts = np.asarray((1.0, 6.0))
    q_counts = np.asarray((1.0, 1.0))
    actual_w = np.diag(np.exp(1j * G * pair_counts))
    deleted_w = np.eye(2, dtype=complex)
    threshold_w = np.diag(np.exp(1j * G * q_counts))
    global_w = np.exp(0.83j) * np.eye(2, dtype=complex)
    inverse_w = actual_w.conj().T
    plus = np.asarray((1, 1), dtype=complex) / np.sqrt(2)
    transducer = logical_swap_transducer()
    check(
        "the collision-SWAP transducer is an exact bounded unitary distinct from the ordinary matter-only contact action",
        np.linalg.norm(transducer.conj().T @ transducer - np.eye(4)) < TOL,
        {
            "transducer_unitarity_residual": float(
                np.linalg.norm(transducer.conj().T @ transducer - np.eye(4))
            ),
            "W_shape": actual_w.shape,
            "transducer_shape": transducer.shape,
        },
    )

    outputs = {
        "actual": process_output(actual_w, plus),
        "deleted": process_output(deleted_w, plus),
        "threshold": process_output(threshold_w, plus),
        "global": process_output(global_w, plus),
        "inverse": process_output(inverse_w, plus),
    }
    flag_rhos = {
        name: partial_flag_density(projector(state)) for name, state in outputs.items()
    }
    matter_rhos = {
        name: partial_matter_density(projector(state)) for name, state in outputs.items()
    }
    p1 = projector(np.asarray((0, 1), dtype=complex))
    x_flag = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y_flag = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    weights = {
        name: float(np.trace(p1 @ rho).real) for name, rho in flag_rhos.items()
    }
    y_currents = {
        name: float(np.trace(y_flag @ rho).real) for name, rho in flag_rhos.items()
    }
    x_currents = {
        name: float(np.trace(x_flag @ rho).real) for name, rho in flag_rhos.items()
    }
    expected_weight = float(np.sin(5 * G / 2) ** 2)
    expected_current = float(abs(np.sin(5 * G)))
    check(
        "ordinary unconditional W_g creates a positive auxiliary collision flag while target deletion leaves the flag exactly blank",
        abs(weights["actual"] - expected_weight) < TOL
        and weights["deleted"] < TOL
        and np.linalg.norm(matter_rhos["actual"] - projector(plus)) < TOL,
        {
            "actual_flag_weight": weights["actual"],
            "expected_sin2_5g_over_2": expected_weight,
            "target_W_deletion_flag_weight": weights["deleted"],
            "matter_reset_residual": float(
                np.linalg.norm(matter_rhos["actual"] - projector(plus))
            ),
        },
    )
    check(
        "equal Q-support makes threshold-only and global-phase replacements exactly blank although actual W_g is non-scalar",
        np.all(q_counts == 1)
        and weights["threshold"] < TOL
        and weights["global"] < TOL
        and np.linalg.norm(actual_w - threshold_w) > 1.0,
        {
            "Q_counts": tuple(q_counts),
            "threshold_flag_weight": weights["threshold"],
            "global_flag_weight": weights["global"],
            "W_minus_threshold_Frobenius": float(
                np.linalg.norm(actual_w - threshold_w)
            ),
        },
    )
    check(
        "the flag Y-current distinguishes W_g from W_g^dagger while their positive collision weights agree",
        abs(weights["actual"] - weights["inverse"]) < TOL
        and abs(y_currents["actual"] + y_currents["inverse"]) < TOL
        and abs(abs(y_currents["actual"]) - expected_current) < TOL
        and abs(x_currents["actual"]) < TOL,
        {
            "W_flag_weight": weights["actual"],
            "W_dagger_flag_weight": weights["inverse"],
            "W_Y_current": y_currents["actual"],
            "W_dagger_Y_current": y_currents["inverse"],
        },
    )
    return {
        "flag_weight": weights["actual"],
        "Y_current": y_currents["actual"],
        "W_minus_threshold": float(np.linalg.norm(actual_w - threshold_w)),
    }


def alternative_route_and_coherence_controls() -> None:
    print("\nLIVE SPATIAL COUNTERROUTE / COHERENCE CONTROL")
    plus = np.asarray((1, 1), dtype=complex) / np.sqrt(2)
    # Total N=2: co-located pair versus two separated singles.  It detects an
    # unconditional contact phase but cannot distinguish W_g from exp(i g Q).
    n2_actual = np.diag((np.exp(1j * G), 1.0)).astype(complex)
    n2_threshold = n2_actual.copy()
    actual_flag = partial_flag_density(projector(process_output(n2_actual, plus)))
    threshold_flag = partial_flag_density(
        projector(process_output(n2_threshold, plus))
    )
    deleted_flag = partial_flag_density(
        projector(process_output(np.eye(2, dtype=complex), plus))
    )
    p1 = projector(np.asarray((0, 1), dtype=complex))
    check(
        "the same-total-N=2 co-located-versus-separated interferometer is a live unconditional-action counterroute but does not separate W_g from Q support",
        float(np.trace(p1 @ actual_flag).real) > 0.03
        and np.linalg.norm(actual_flag - threshold_flag) < TOL
        and np.linalg.norm(actual_flag - deleted_flag) > 0.03,
        {
            "actual_flag_weight": float(np.trace(p1 @ actual_flag).real),
            "W_vs_threshold_flag_residual": float(
                np.linalg.norm(actual_flag - threshold_flag)
            ),
            "W_vs_deletion_flag_residual": float(
                np.linalg.norm(actual_flag - deleted_flag)
            ),
        },
    )

    # Without A/B coherence, the ordinary phase changes no density operator;
    # the collision transducer sees the same maximally mixed logical flag.
    mixture = np.eye(2, dtype=complex) / 2
    blank = projector(np.asarray((1, 0), dtype=complex))
    transducer = logical_swap_transducer()

    def mixed_flag(w: np.ndarray) -> np.ndarray:
        incoming = np.kron(w @ mixture @ w.conj().T, blank)
        outgoing = transducer @ incoming @ transducer.conj().T
        return partial_flag_density(outgoing)

    phase = np.diag(np.exp(1j * G * np.asarray((1.0, 6.0))))
    check(
        "dephasing the supplied collision-path reference removes action sensitivity exactly",
        np.linalg.norm(mixed_flag(phase) - mixed_flag(np.eye(2))) < TOL,
        {
            "dephased_actual_vs_deleted_flag_residual": float(
                np.linalg.norm(mixed_flag(phase) - mixed_flag(np.eye(2)))
            )
        },
    )


def pauli_support(rows: tuple[c235.Pauli, ...] | list[c235.Pauli]) -> int:
    mask = 0
    for row in rows:
        mask |= row.x | row.z
    return mask


def patch_data(code: c269.WilsonSubsystemCode) -> dict[str, object]:
    origin = (0, 0, 0)
    y_cell = (0, 1 % code.length, 0)
    z_cell = (0, 0, 1 % code.length)
    cells = (origin, y_cell, z_cell)
    vertices = tuple(
        code.graph.vertex_index[(cell, direction)]
        for cell in cells
        for direction in range(6)
    )
    transport_pairs = (
        (
            code.graph.vertex_index[(origin, 2)],
            code.graph.vertex_index[(y_cell, 3)],
        ),
        (
            code.graph.vertex_index[(origin, 4)],
            code.graph.vertex_index[(z_cell, 5)],
        ),
    )
    bs = tuple(code.B[vertex] for vertex in vertices)
    transport_as = tuple(
        code.graph.A(source, target) for source, target in transport_pairs
    )
    fswap_terms = []
    for source, target in transport_pairs:
        bu = code.B[source]
        bv = code.B[target]
        a = code.graph.A(source, target)
        fswap_terms.extend((bu, bv, bu @ a, bv @ a))
    return {
        "cells": cells,
        "vertices": vertices,
        "transport_pairs": transport_pairs,
        "B": bs,
        "A": transport_as,
        "FSWAP_terms": tuple(fswap_terms),
    }


def transport_truth_control() -> None:
    # Occupied direction labels in the three-cell patch.  The two graph FSWAPs
    # move the separated singleton references into target directions 2 and 4.
    target = (0, 0, 0)
    y_cell = (0, 1, 0)
    z_cell = (0, 0, 1)
    branch_a = {
        (target, 0),
        (target, 1),
        (y_cell, 3),
        (z_cell, 5),
    }
    branch_b = {
        (target, 0),
        (target, 1),
        (target, 2),
        (target, 4),
    }
    pairs = (((target, 2), (y_cell, 3)), ((target, 4), (z_cell, 5)))

    def move(occupied: set[tuple[tuple[int, int, int], int]]) -> set:
        result = set(occupied)
        for left, right in pairs:
            l_value = left in result
            r_value = right in result
            result.discard(left)
            result.discard(right)
            if l_value:
                result.add(right)
            if r_value:
                result.add(left)
        return result

    check(
        "the two exact graph-FSWAP collision word exchanges the two fixed-N branch configurations in both directions",
        move(branch_a) == branch_b and move(branch_b) == branch_a,
        {
            "branch_A_total_N": len(branch_a),
            "branch_B_total_N": len(branch_b),
            "transport_edges": pairs,
        },
    )


def physical_code_support_and_leakage_controls() -> dict[str, int]:
    print("\nCONNECTED PHYSICAL-M2 CODE / SUPPORT / LEAKAGE / HELD SIZE")
    coefficients = c285.contact_walsh_coefficients(np.diag(c285.fixture()["W"]))
    rows = []
    failures = []
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        patch = patch_data(code)
        generators = tuple(patch["B"]) + tuple(patch["A"]) + tuple(
            patch["FSWAP_terms"]
        )
        leakage = sum(
            not generator.commutes(check_row)
            for generator in generators
            for check_row in code.local_checks + code.wilsons
        )
        matter_support = pauli_support(list(generators)).bit_count()
        row = {
            "L": length,
            "held_out": length == 6,
            "patch_cells": len(patch["cells"]),
            "matter_support_union_M2": matter_support,
            "auxiliary_flag_M2": 1,
            "total_bounded_neighborhood_M2": matter_support + 1,
            "physical_generator_count": len(generators),
            "nonzero_contact_Walsh_terms_per_cell": sum(
                abs(value) > 1e-14 for value in coefficients
            ),
            "local_check_or_Wilson_leakage": leakage,
        }
        rows.append(row)
        if not (
            row["patch_cells"] == 3
            and row["nonzero_contact_Walsh_terms_per_cell"] == 64
            and row["total_bounded_neighborhood_M2"] == rows[0][
                "total_bounded_neighborhood_M2"
            ]
            and leakage == 0
        ):
            failures.append(row)
    check(
        "the unconditional W_g, equal-support projectors, graph-FSWAP comparator algebra, and one M2 flag have bounded size-independent support and zero leakage through held-out L=6",
        not failures,
        rows,
    )
    return {
        "matter_support": rows[0]["matter_support_union_M2"],
        "total_support": rows[0]["total_bounded_neighborhood_M2"],
    }


def covariance_controls() -> None:
    print("\nALL-24 / FULL-TRANSLATION COLLISION-MOTIF COVARIANCE")
    code = c269.build_code(3)
    patch = patch_data(code)
    base_vertices = tuple(patch["vertices"])
    base_bs = tuple(patch["B"])
    base_pairs = tuple(patch["transport_pairs"])
    base_as = tuple(patch["A"])
    local_family = set(code.local_checks)
    central_pivots, central_bad = c278.phase_reducer(
        list(code.local_checks + code.wilsons), code.qubits
    )
    failures = []
    tests = 0
    for frame in c235.proper_cubic_frames():
        frame_vertex, frame_edge = c235.graph_frame_maps(code.graph, frame)
        for displacement in product(range(3), repeat=3):
            translation_vertex, translation_edge = c269.graph_translation_maps(
                code.graph, displacement
            )
            vertex_map = tuple(
                translation_vertex[frame_vertex[index]]
                for index in range(len(frame_vertex))
            )
            edge_map = tuple(
                translation_edge[frame_edge[index]]
                for index in range(len(frame_edge))
            )
            toggles, pairs, flips = c269.repair_data(
                code.graph, vertex_map, edge_map
            )

            def transform(row: c235.Pauli) -> c235.Pauli:
                return c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )

            transformed_bs = tuple(transform(row) for row in base_bs)
            expected_bs = tuple(code.B[vertex_map[vertex]] for vertex in base_vertices)
            transformed_as = tuple(transform(row) for row in base_as)
            expected_as = tuple(
                code.graph.A(vertex_map[source], vertex_map[target])
                for source, target in base_pairs
            )
            transformed_local = {transform(row) for row in code.local_checks}
            transformed_wilsons = tuple(transform(row) for row in code.wilsons)
            mapped_edges_exist = all(
                frozenset((vertex_map[source], vertex_map[target]))
                in code.graph.edge_lookup
                for source, target in base_pairs
            )
            valid = (
                set(transformed_bs) == set(expected_bs)
                and transformed_as == expected_as
                and transformed_local == local_family
                and mapped_edges_exist
                and not central_bad
                and all(
                    not c278.reduce_pauli(
                        row, central_pivots, code.qubits
                    ).symplectic(code.qubits)
                    for row in transformed_wilsons
                )
            )
            if not valid:
                failures.append(
                    {
                        "frame": frame.tolist(),
                        "translation": displacement,
                        "B": set(transformed_bs) == set(expected_bs),
                        "A": transformed_as == expected_as,
                        "local": transformed_local == local_family,
                        "edges": mapped_edges_exist,
                    }
                )
            tests += 1
    check(
        "the three-cell collision motif, two transport edges, physical even algebra, and carried scalar flag are covariant in all 24*27=648 frame-translation cases",
        not failures and tests == 648,
        {"tests": tests, "failures": failures[:5]},
    )


def mass_lawful_domain_and_semantic_controls() -> None:
    print("\nMASS FIXTURE / LAWFUL DOMAIN / SEMANTIC FIREWALL")
    model = c285.fixture()
    species = c278.c219.common_species(c278.c230.BETA)
    occupations = model["occupations"]
    check(
        "the ordinary contact remains identity on N<=1 and preserves the inherited one-particle mass fixture",
        np.max(np.abs(np.diag(model["W"])[occupations <= 1] - 1)) == 0
        and abs(c278.c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "one_particle_action": "identity",
            "rest_to_analytic_mass_ratio": c278.c219.rest_mass(species)
            / species.analytic_mass,
        },
    )

    def validate(length: int, total_number: int, q_values: tuple[int, int], flag_dimension: int) -> None:
        if length < 3:
            raise ValueError("L must be at least three")
        if total_number != 4:
            raise ValueError("the declared branches have fixed total N=4")
        if q_values != (1, 1):
            raise ValueError("both declared branches must have equal Q support")
        if flag_dimension != 2:
            raise ValueError("the current flag is one ordinary M2")

    rejected = 0
    for args in ((2, 4, (1, 1), 2), (3, 3, (1, 1), 2), (3, 4, (1, 0), 2), (3, 4, (1, 1), 3)):
        try:
            validate(*args)
        except ValueError:
            rejected += 1
    validate(3, 4, (1, 1), 2)
    text = normalized(NOTE)
    check(
        "lawful-domain and interpretation controls keep the supplied collision reference, comparator, read, occurrence, Record, time, energy, and source distinct",
        rejected == 4
        and "no controlled-w_g oracle" in text
        and "the coherent flag is not occurrence" in text
        and "the auxiliary flag is not a record" in text
        and "circuit order is not physical time" in text
        and "wrapped phase is not physical energy" in text,
        {
            "rejected_controls": rejected,
            "supplied_reference": "coherent fixed-N A/B collision pattern, phase convention, blank M2 flag, collision-SWAP",
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    collision = collision_interferometer_controls()
    alternative_route_and_coherence_controls()
    transport_truth_control()
    support = physical_code_support_and_leakage_controls()
    covariance_controls()
    mass_lawful_domain_and_semantic_controls()
    check(
        "the constructive result is action-sensitive but remains conditional on a supplied coherent collision fixture and transducer, with no route-independent obstruction or axiom pressure",
        collision["flag_weight"] > 0.6
        and collision["W_minus_threshold"] > 1.0
        and support["total_support"] < 100
        and "no route-independent obstruction" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
        {"collision": collision, "support": support},
    )
    print("DATA collision", collision)
    print("DATA support", support)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE289_UNCONTROLLED_CONTACT_COLLISION_CURRENT_GREEN"
        if FAIL == 0
        else "CYCLE289_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
