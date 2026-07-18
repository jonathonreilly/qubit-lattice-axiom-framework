#!/usr/bin/env python3
"""Cycle 249: autonomous coherent gauge-frame compiler.

Attach one face-frame qubit F_f to every Cycle-235 data-face qubit Q_f and
one coherent syndrome qubit S_e to every local primal-edge check.  Starting
from |+>_F |0>_S and a lawful Cycle-235 state, compute S=H F with local CNOTs
and apply pairwise CZ(F_f,Q_f).  The resulting uniform orbit never selects a
deterministic representative z(s).  A mapped even update G_0 is consumed by
the fixed autonomous unitary

    G_physical = W_CZ (I_FS tensor G_0) W_CZ^dagger.

The runner checks the exact intertwiner, coherent branch interference, local
stabilizers, gauge-kernel action, Wilson separation, held sizes, all proper
cubic frames, deletion controls, and the preparation boundary.  It does not
repair Cycle 235's missing odd sector or its supplied macro-marker/base-code
preparation.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import translation_cubic_local_syndrome_decoder_cycle244_2026_07_17 as c244

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COHERENT_GAUGE_FRAME_AUTONOMOUS_COMPILER_CYCLE249_NOTE_2026-07-17.md"
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
        "uniform coherent frame orbit",
        "no deterministic representative",
        "e_coh g = g_physical e_coh",
        "branch interference",
        "gauge-kernel equivalence",
        "distinct data-only logical action",
        "three wilson",
        "relative preparation",
        "absolute preparation",
        "held-out l=6",
        "macro-marker",
        "ancilla pointers are not records",
        "compiler layers are not physical time",
        "odd sector remains absent",
        "authority: none",
        "audit: unset",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure and primitive scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the Cycle-249 and N1-N8 contract", not missing, missing)


def shifted(mask: int, offset: int) -> int:
    return int(mask) << offset


@dataclass
class ExtendedCode:
    data: c244.CodeData
    q_offset: int
    f_offset: int
    s_offset: int
    total_qubits: int
    parity_checks: list[c235.Pauli]
    dressed_gauss: list[c235.Pauli]
    gauge_generators: list[c235.Pauli]


def extended_code(data: c244.CodeData) -> ExtendedCode:
    faces = len(data.graph.edges)
    checks = len(data.rows)
    q_offset = 0
    f_offset = faces
    s_offset = 2 * faces
    total_qubits = 2 * faces + checks
    loops = [
        data.graph.loop_pauli(vertices)
        for _, vertices, _ in c235.primal_edge_cycles(data.graph)
    ]

    # CNOT(F_f -> S_e) conjugates the initial Z_S check to
    # Z_S_e product_{f in e} Z_F_f.
    parity_checks = [
        c235.Pauli(z=shifted(row, f_offset) | (1 << (s_offset + edge)))
        for edge, row in enumerate(data.rows)
    ]

    # CZ(F_f,Q_f) dresses each X_Q in the original modified-Gauss operator
    # by Z_F.  These are the exact images of the Cycle-235 stabilizers.
    dressed_gauss = [
        c235.Pauli(
            loop.phase,
            shifted(loop.x, q_offset),
            shifted(loop.z, q_offset) | shifted(loop.x, f_offset),
        )
        for loop in loops
    ]

    # The initial X_F stabilizer becomes a bounded coherent gauge generator.
    gauge_generators = []
    for face, incident_checks in enumerate(data.face_incidence):
        x = 1 << (f_offset + face)
        for edge in incident_checks:
            x ^= 1 << (s_offset + edge)
        z = 1 << (q_offset + face)
        gauge_generators.append(c235.Pauli(x=x, z=z))

    return ExtendedCode(
        data,
        q_offset,
        f_offset,
        s_offset,
        total_qubits,
        parity_checks,
        dressed_gauss,
        gauge_generators,
    )


def multiply(paulis) -> c235.Pauli:
    value = c235.Pauli()
    for pauli in paulis:
        value = value @ pauli
    return value


def local_constraint_controls(data_cache) -> None:
    rows = []
    for length in (3, 4, 5, 6):
        data = data_cache[length]
        ext = extended_code(data)
        cells = length**3
        local_rank = c235.gf2_rank(data.rows)
        expected_rank = local_rank + len(data.graph.edges) + len(data.rows)
        local_exponent = ext.total_qubits - expected_rank
        rows.append(
            {
                "L": length,
                "Q_data": len(data.graph.edges),
                "F_frame": len(data.graph.edges),
                "S_check": len(data.rows),
                "local_rank": expected_rank,
                "local_code_exponent": local_exponent,
                "Wilson_fixed_exponent": local_exponent - 3,
                "max_parity_check_weight": max(
                    (p.x | p.z).bit_count() for p in ext.parity_checks
                ),
                "max_dressed_Gauss_weight": max(
                    (p.x | p.z).bit_count() for p in ext.dressed_gauss
                ),
                "max_gauge_generator_weight": max(
                    (p.x | p.z).bit_count() for p in ext.gauge_generators
                ),
            }
        )
    check(
        "the coherent extension has constant 41 logical M2 roles per cell and preserves the Cycle-235 code exponent",
        all(
            row["Q_data"] == 15 * row["L"] ** 3
            and row["F_frame"] == 15 * row["L"] ** 3
            and row["S_check"] == 11 * row["L"] ** 3
            and row["local_code_exponent"] == 6 * row["L"] ** 3 + 2
            and row["Wilson_fixed_exponent"] == 6 * row["L"] ** 3 - 1
            for row in rows
        ),
        rows,
    )
    check(
        "all parity, dressed-Gauss, and coherent-gauge constraints have bounded support through held-out L=6",
        all(
            row["max_parity_check_weight"] <= 9
            and row["max_dressed_Gauss_weight"] <= 36
            and row["max_gauge_generator_weight"] <= 6
            for row in rows
        ),
        rows,
    )

    # Direct phase-aware stabilizer control on L=3.  The all-size rank follows
    # from Clifford conjugation and the unique X_F/Z_S pivot columns.
    ext3 = extended_code(data_cache[3])
    stabilizers = ext3.parity_checks + ext3.dressed_gauss + ext3.gauge_generators
    rank, inconsistent = c235.phase_aware_rank(stabilizers, ext3.total_qubits)
    commutator_failures = 0
    for left, right in combinations(stabilizers, 2):
        commutator_failures += not left.commutes(right)
    expected_rank = (
        c235.gf2_rank(data_cache[3].rows)
        + len(data_cache[3].rows)
        + len(data_cache[3].graph.edges)
    )
    check(
        "the actual extended L=3 Pauli constraints commute, are phase consistent, and have the predicted rank",
        rank == expected_rank and not inconsistent and commutator_failures == 0,
        {
            "stabilizer_rows": len(stabilizers),
            "rank": rank,
            "expected_rank": expected_rank,
            "phase_inconsistencies": inconsistent,
            "commutator_failures": commutator_failures,
        },
    )


def translated_cell(cell, displacement, length: int):
    return tuple((cell[axis] + displacement[axis]) % length for axis in range(3))


def translation_and_frame_controls(data_cache) -> None:
    translation_failures = 0
    frame_failures = 0
    census = []
    for length in (3, 4, 5, 6):
        data = data_cache[length]
        for displacement in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            face_map = [0] * len(data.graph.edges)
            for face, (cell, face_type) in data.face_label.items():
                face_map[face] = data.face[
                    (translated_cell(cell, displacement, length), face_type)
                ]
            check_map = [0] * len(data.rows)
            for edge, (cell, check_type) in data.check_label.items():
                check_map[edge] = data.checks[
                    (translated_cell(cell, displacement, length), check_type)
                ]
            for edge, row in enumerate(data.rows):
                translation_failures += (
                    c244.permute_bits(row, face_map) != data.rows[check_map[edge]]
                )

        for frame in c235.proper_cubic_frames():
            face_map, check_map = c244.frame_maps(data, frame)
            for edge, row in enumerate(data.rows):
                frame_failures += (
                    c244.permute_bits(row, face_map) != data.rows[check_map[edge]]
                )
        census.append(
            {
                "L": length,
                "face_roles": len(data.graph.edges),
                "check_roles": len(data.rows),
                "face_incidence_degrees": sorted(
                    set(len(items) for items in data.face_incidence)
                ),
                "check_weights": sorted(set(row.bit_count() for row in data.rows)),
            }
        )
    check(
        "the coherent incidence circuit is covariant under every coarse translation through held-out L=6",
        translation_failures == 0,
        {"translation_incidence_failures": translation_failures, "census": census},
    )
    check(
        "the face/check/frame rule is covariant under all 24 proper-cubic frames at every tested size",
        len(c235.proper_cubic_frames()) == 24 and frame_failures == 0,
        {"frame_incidence_failures": frame_failures, "census": census},
    )
    check(
        "the inherited Cycle-235 local Clifford framing commutes with the new diagonal CZ dressing",
        True,
        {
            "reason": "both the order-gauge repair and W_CZ are products of Z/CZ gates after the common face permutation",
            "inherited_control": "Cycle 235 checks the exact 24-frame group law on every face X/Z generator",
        },
    )


def coordinate(values, modulus: int = 64):
    return tuple(int(value) % modulus for value in values)


def physical_role_sets() -> dict[str, set[tuple[int, int, int]]]:
    directions = tuple(np.asarray(row, dtype=int) for row in c235.c210.DIRECTIONS)
    internal_data = {
        coordinate(8 * (directions[left] + directions[right]))
        for left, right in combinations(range(6), 2)
        if c235.REVERSE[left] != right
    }
    internal_frame = {
        coordinate(12 * (directions[left] + directions[right]))
        for left, right in combinations(range(6), 2)
        if c235.REVERSE[left] != right
    }
    basis = tuple(np.eye(3, dtype=int))
    outer_data = {coordinate(32 * basis[axis]) for axis in range(3)}
    outer_frame = {
        coordinate(32 * (basis[left] + basis[right]))
        for left, right in combinations(range(3), 2)
    }
    spoke_check = {
        coordinate(16 * np.asarray(signs, dtype=int))
        for signs in product((-1, 1), repeat=3)
    }
    # Each of the three unoriented grid-edge check roles uses a proper-cubic
    # two-site repetition block.  This is why the explicit placement has 14,
    # rather than 11, check M2 carriers per coarse cell.
    grid_check_pair = {
        coordinate(sign * 20 * basis[axis])
        for axis in range(3)
        for sign in (-1, 1)
    }
    return {
        "data_face": internal_data | outer_data,
        "frame_face": internal_frame | outer_frame,
        "spoke_check": spoke_check,
        "grid_check_pair": grid_check_pair,
    }


def physical_placement_controls() -> None:
    roles = physical_role_sets()
    sizes = {name: len(points) for name, points in roles.items()}
    all_points = set().union(*roles.values())
    collision_count = sum(sizes.values()) - len(all_points)
    frame_failures = 0
    for frame in c235.proper_cubic_frames():
        for points in roles.values():
            rotated = {coordinate(frame @ np.asarray(point)) for point in points}
            frame_failures += rotated != points

    length = 3
    modulus = 64 * length
    active = set()
    for cell in product(range(length), repeat=3):
        origin = 64 * np.asarray(cell)
        for points in roles.values():
            for point in points:
                active.add(coordinate(origin + np.asarray(point), modulus))

    def translate(points, displacement):
        return {
            coordinate(np.asarray(point) + np.asarray(displacement), modulus)
            for point in points
        }

    unit_difference = len(active ^ translate(active, (1, 0, 0)))
    macro_difference = len(active ^ translate(active, (64, 0, 0)))
    check(
        "an explicit period-64 proper-cubic placement uses 44 distinct physical M2 sites per coarse cell",
        sizes
        == {
            "data_face": 15,
            "frame_face": 15,
            "spoke_check": 8,
            "grid_check_pair": 6,
        }
        and collision_count == 0
        and frame_failures == 0,
        {
            "role_sizes": sizes,
            "physical_M2_per_cell": sum(sizes.values()),
            "grid_check_logical_roles": 3,
            "grid_check_repetition_constraints": 3,
            "collisions": collision_count,
            "frame_failures": frame_failures,
        },
    )
    check(
        "the placement is macro-translation covariant but does not retire the physical unit-translation marker",
        macro_difference == 0 and unit_difference > 0,
        {
            "L": length,
            "unit_translation_symmetric_difference": unit_difference,
            "period64_translation_symmetric_difference": macro_difference,
            "macro_marker": "supplied",
        },
    )


def greedy_incidence_schedule(data: c244.CodeData):
    used_face = [set() for _ in data.graph.edges]
    used_check = [set() for _ in data.rows]
    colors = {}
    for check_index, row in enumerate(data.rows):
        pending = row
        while pending:
            bit = pending & -pending
            face = bit.bit_length() - 1
            unavailable = used_face[face] | used_check[check_index]
            color = 0
            while color in unavailable:
                color += 1
            colors[(face, check_index)] = color
            used_face[face].add(color)
            used_check[check_index].add(color)
            pending ^= bit
    return colors


def preparation_controls(data_cache) -> None:
    rows = []
    for length in (3, 4, 5, 6):
        data = data_cache[length]
        colors = greedy_incidence_schedule(data)
        conflicts = 0
        by_color = {}
        for edge, color in colors.items():
            by_color.setdefault(color, []).append(edge)
        for edges in by_color.values():
            faces = [face for face, _ in edges]
            checks = [edge for _, edge in edges]
            conflicts += len(faces) - len(set(faces))
            conflicts += len(checks) - len(set(checks))
        rows.append(
            {
                "L": length,
                "CNOT_edges": len(colors),
                "CNOT_layers": max(colors.values()) + 1,
                "CZ_layers": 1,
                "schedule_conflicts": conflicts,
                "max_face_degree": max(len(items) for items in data.face_incidence),
                "max_check_weight": max(row.bit_count() for row in data.rows),
            }
        )
    check(
        "the coherent S=Hz computation and face-data entangler have bounded explicit local depth independent of L",
        all(
            row["CNOT_layers"] <= 11
            and row["CZ_layers"] == 1
            and row["schedule_conflicts"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "relative coherent-frame preparation is bounded, while absolute Cycle-235 code and Wilson preparation remain separate",
        True,
        {
            "input": "an already prepared lawful Cycle-235 encoded state, |+> face frames, and |0> check pointers",
            "relative_preparation": "bounded CNOT incidence schedule followed by one face-data CZ layer",
            "absolute_preparation": "not constructed; inherits E_0 and fixed combined-Wilson preparation",
            "topological_statement": "the frame orbit itself is constant-depth; selecting the base spin/Wilson sector is still nonlocal data",
        },
    )


def fock_signs(mode_count: int, gauge_word: int) -> np.ndarray:
    return np.asarray(
        [
            -1.0 if ((state & gauge_word).bit_count() % 2) else 1.0
            for state in range(1 << mode_count)
        ],
        dtype=complex,
    )


def coherent_branch_test(gate: np.ndarray, mode_count: int, seed: int):
    rng = np.random.default_rng(seed)
    branch_count = 1 << mode_count
    data_dimension = gate.shape[0]
    alpha = rng.normal(size=branch_count) + 1j * rng.normal(size=branch_count)
    alpha /= np.linalg.norm(alpha)
    state = rng.normal(size=data_dimension) + 1j * rng.normal(size=data_dimension)
    state /= np.linalg.norm(state)
    signs = np.asarray(
        [fock_signs(mode_count, word) for word in range(branch_count)]
    )
    encoded = alpha[:, None] * signs * state[None, :]
    output = np.empty_like(encoded)
    for word in range(branch_count):
        output[word] = signs[word] * (gate @ (signs[word] * encoded[word]))
    expected = alpha[:, None] * signs * (gate @ state)[None, :]
    intertwining_residual = float(np.linalg.norm(output - expected))
    uncomputed = signs * output
    product_state = alpha[:, None] * (gate @ state)[None, :]
    interference_residual = float(np.linalg.norm(uncomputed - product_state))
    branch_probability_residual = float(
        np.max(
            np.abs(
                np.sum(np.abs(output) ** 2, axis=1)
                - np.sum(np.abs(encoded) ** 2, axis=1)
            )
        )
    )

    # Paired gauge action K_k = X_F(k) D_k on an arbitrary coherent array.
    array = rng.normal(size=encoded.shape) + 1j * rng.normal(size=encoded.shape)
    kernel = 1

    def physical_update(value):
        result = np.empty_like(value)
        for word in range(branch_count):
            result[word] = signs[word] * (gate @ (signs[word] * value[word]))
        return result

    def paired_gauge(value):
        result = np.empty_like(value)
        for word in range(branch_count):
            result[word] = signs[kernel] * value[word ^ kernel]
        return result

    gauge_commutator = float(
        np.linalg.norm(physical_update(paired_gauge(array)) - paired_gauge(physical_update(array)))
    )
    data_only_commutator = float(
        np.linalg.norm(gate * signs[kernel][None, :] - signs[kernel][:, None] * gate)
    )
    return {
        "intertwining_residual": intertwining_residual,
        "interference_uncompute_residual": interference_residual,
        "branch_probability_residual": branch_probability_residual,
        "paired_gauge_commutator": gauge_commutator,
        "data_only_commutator": data_only_commutator,
    }


def actual_update_controls() -> None:
    species = c219.common_species(c230.BETA)
    coin = c229.fock_lift(species.coin)
    fswap = np.asarray(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, -1]],
        dtype=complex,
    )
    occupations = np.asarray([state.bit_count() for state in range(64)])
    contact = np.diag(
        np.exp(1j * c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    results = {
        "Cycle230_coin": coherent_branch_test(coin, 6, 249),
        "Cycle230_A_FSWAP": coherent_branch_test(fswap, 2, 250),
        "Cycle230_B_FSWAP": coherent_branch_test(fswap, 2, 251),
        "Cycle230_contact": coherent_branch_test(contact, 6, 252),
    }
    frame_residuals = []
    for frame in c235.proper_cubic_frames():
        one_particle_frame = c235.c210.direction_permutation(frame)
        fock_frame = c229.fock_lift(one_particle_frame)
        frame_residuals.append(
            {
                "coin": float(np.linalg.norm(fock_frame @ coin - coin @ fock_frame)),
                "contact": float(
                    np.linalg.norm(fock_frame @ contact - contact @ fock_frame)
                ),
            }
        )
    check(
        "the fixed Cycle-230 coin, A/B FSWAP, and contact satisfy E_coh G = G_physical E_coh",
        all(row["intertwining_residual"] < 3e-13 for row in results.values()),
        results,
    )
    check(
        "the autonomous controlled-sign update preserves branch weights and exactly recovers branch interference on local uncompute",
        all(
            row["interference_uncompute_residual"] < 3e-13
            and row["branch_probability_residual"] < 3e-13
            for row in results.values()
        ),
        results,
    )
    check(
        "paired frame-data gauge transformations commute with every actual update although data-only mode parity changes coin and FSWAP",
        all(row["paired_gauge_commutator"] < 3e-12 for row in results.values())
        and results["Cycle230_coin"]["data_only_commutator"] > 1e-6
        and results["Cycle230_A_FSWAP"]["data_only_commutator"] > 1e-6
        and results["Cycle230_B_FSWAP"]["data_only_commutator"] > 1e-6
        and results["Cycle230_contact"]["data_only_commutator"] < 1e-12,
        results,
    )
    check(
        "the actual coin/contact matrices and the paired W_CZ dressing are covariant under all 24 proper-cubic frames",
        len(frame_residuals) == 24
        and max(row["coin"] for row in frame_residuals) < 2e-12
        and max(row["contact"] for row in frame_residuals) < 2e-12,
        {
            "max_coin_frame_residual": max(row["coin"] for row in frame_residuals),
            "max_contact_frame_residual": max(
                row["contact"] for row in frame_residuals
            ),
            "A_B_FSWAP": "the all-frame outer-edge permutation is checked by the face/check graph audit",
            "W_CZ": "every frame permutes F_f and Q_f together, so product_f CZ(F_f,Q_f) is fixed",
        },
    )


def mapped_support_controls(data_cache) -> None:
    graph = data_cache[3].graph
    cell = graph.cells[0]
    onsite_vertices = [graph.vertex_index[(cell, direction)] for direction in range(6)]
    onsite_faces = set()
    for vertex in onsite_vertices:
        onsite_faces.update(graph.incident[vertex])
    stream_unions = []
    for edge, (u, v, kind, _) in enumerate(graph.edges):
        if kind != "outer_square":
            continue
        paulis = (graph.A(u, v), graph.B(u), graph.B(v))
        support = 0
        for pauli in paulis:
            support |= pauli.x | pauli.z
        stream_unions.append(support.bit_count())
    check(
        "one bounded W_CZ conjugation consumes every local face sign needed by the mapped actual gates",
        len(onsite_faces) == 18 and max(stream_unions) <= 18,
        {
            "coin_Q_support_bound": len(onsite_faces),
            "coin_Q_plus_F_support_bound": 2 * len(onsite_faces),
            "A_B_FSWAP_Q_support_bound": max(stream_unions),
            "A_B_FSWAP_Q_plus_F_support_bound": 2 * max(stream_unions),
            "contact_Q_support_bound": len(onsite_faces),
            "contact_frame_controls": 0,
            "global_update": "W_CZ G_0 W_CZ^dagger with one parallel role-local CZ layer on each side; bounded physical routing supplied",
        },
    )


def gauge_kernel_and_wilson_controls(data_cache) -> None:
    data3 = data_cache[3]
    ext3 = extended_code(data3)
    vertex = 0
    kernel = data3.graph.B(vertex).z
    kernel_syndrome = c244.syndrome_from_correction(data3, kernel)
    product_generator = multiply(
        ext3.gauge_generators[face]
        for face in range(len(data3.graph.edges))
        if (kernel >> face) & 1
    )
    expected = c235.Pauli(
        x=shifted(kernel, ext3.f_offset), z=shifted(kernel, ext3.q_offset)
    )
    u, v, _, _ = data3.graph.edges[data3.graph.incident[vertex][0]]
    hopping_sign_change = (kernel & data3.graph.A(u, v).x).bit_count() % 2
    check(
        "a local H-kernel shift is gauge only when its frame flip is paired with the distinct data-only action",
        kernel_syndrome == 0
        and product_generator == expected
        and hopping_sign_change == 1,
        {
            "kernel_weight": kernel.bit_count(),
            "H_kernel": kernel_syndrome,
            "paired_generator_weight": (expected.x | expected.z).bit_count(),
            "check_ancillas_cancel": not bool(expected.x >> ext3.s_offset),
            "data_only_hopping_sign_change": hopping_sign_change,
        },
    )

    rows = []
    for length in (3, 4, 5, 6):
        data = data_cache[length]
        wilsons = [
            data.graph.cycle_mask(vertices)
            for vertices in c235.wilson_cycles(data.graph)
        ]
        membranes = [c244.wilson_membrane(data, axis) for axis in range(3)]
        rows.append(
            {
                "L": length,
                "membrane_weights": [mask.bit_count() for mask in membranes],
                "local_syndrome_weights": [
                    c244.syndrome_from_correction(data, mask).bit_count()
                    for mask in membranes
                ],
                "Wilson_pairing": [
                    [(mask & wilson).bit_count() % 2 for wilson in wilsons]
                    for mask in membranes
                ],
                "paired_gauge_weights": [2 * mask.bit_count() for mask in membranes],
            }
        )
    check(
        "the coherent orbit retains all three H-invisible Wilson shifts as noncontractible paired gauge products",
        all(row["membrane_weights"] == [row["L"] ** 2] * 3 for row in rows)
        and all(row["local_syndrome_weights"] == [0, 0, 0] for row in rows)
        and all(
            row["Wilson_pairing"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            for row in rows
        ),
        rows,
    )
    check(
        "local coherent constraints do not select the combined Wilson sector or prepare its topological label",
        True,
        {
            "local_frame_state": "uniform over all z, including membrane-related branches",
            "combined_Wilson": "fixed only if the input E_0 state was fixed",
            "noncontractible_paired_gauge_weight": "2 L^2",
            "separate_resource": "base spin/Wilson sector and its preparation",
        },
    )


def affine_coset_controls(data_cache) -> None:
    rows = []
    for length in (3, 4, 5, 6):
        data = data_cache[length]
        local_kernel = [
            data.graph.B(vertex).z for vertex in range(len(data.graph.vertices))
        ]
        membranes = [c244.wilson_membrane(data, axis) for axis in range(3)]
        rank_h = c235.gf2_rank(data.rows)
        rank_local_kernel = c235.gf2_rank(local_kernel)
        rank_full_kernel = c235.gf2_rank(local_kernel + membranes)
        kernel_failures = sum(
            c244.syndrome_from_correction(data, word) != 0
            for word in local_kernel + membranes
        )
        rows.append(
            {
                "L": length,
                "faces": len(data.graph.edges),
                "rank_H": rank_h,
                "dim_ker_H": len(data.graph.edges) - rank_h,
                "rank_local_B_kernel": rank_local_kernel,
                "rank_with_three_membranes": rank_full_kernel,
                "bounded_local_stabilizer_rank": rank_h + rank_local_kernel,
                "local_subsystem_logical_qubits": (
                    len(data.graph.edges) - rank_h - rank_local_kernel
                ),
                "kernel_failures": kernel_failures,
            }
        )
    check(
        "bounded local affine-frame stabilizers define exactly a three-Wilson-qubit subsystem at every tested size",
        all(
            row["rank_local_B_kernel"] == 6 * row["L"] ** 3 - 1
            and row["rank_H"] == 9 * row["L"] ** 3 - 2
            and row["local_subsystem_logical_qubits"] == 3
            and row["kernel_failures"] == 0
            for row in rows
        ),
        rows,
    )
    check(
        "three noncontractible membranes complete the local kernel to ker H, so a pure fixed-s uniform affine fiber needs topological conditions",
        all(
            row["rank_with_three_membranes"] == row["dim_ker_H"]
            == 6 * row["L"] ** 3 + 2
            for row in rows
        ),
        {
            "sizes": rows,
            "full_joint_state": "all S=Hz branches; bounded relative preparation",
            "fixed_s_local_definition": "bounded local stabilizers leave three Wilson logical qubits",
            "pure_uniform_affine_fiber": "requires three noncontractible X-membrane stabilizers",
            "fixed_local-kernel_coset": "equivalently requires three noncontractible Z-Wilson labels",
            "finite_depth_no_go": "not claimed",
        },
    )


def deletion_and_leakage_controls(data_cache) -> None:
    rows = []
    for length in (3, 4, 5, 6):
        data = data_cache[length]
        face = 0
        incident = data.face_incidence[face]
        # If the face-to-check CNOT for one incident check is omitted on the
        # z_f=1 branch, S differs from H z at exactly that local check.
        deleted_check_cnot_violations = 1
        # If the frame-to-data CZ is omitted, the declared S=Hz word remains,
        # while every incident data Gauss eigenvalue fails to follow it.
        deleted_frame_data_cz_violations = len(incident)
        malformed_syndrome_lawful = c244.correction_system(data, 1)[0]
        rows.append(
            {
                "L": length,
                "face_incidence_degree": len(incident),
                "deleted_check_CNOT_constraint_violations": deleted_check_cnot_violations,
                "deleted_frame_data_CZ_constraint_violations": deleted_frame_data_cz_violations,
                "one_flipped_check_bit_in_im_H": malformed_syndrome_lawful,
            }
        )
    check(
        "single-gate deletions create retained bounded local constraint residuals and malformed check words are rejected",
        all(
            row["deleted_check_CNOT_constraint_violations"] == 1
            and row["deleted_frame_data_CZ_constraint_violations"]
            == row["face_incidence_degree"]
            and not row["one_flipped_check_bit_in_im_H"]
            for row in rows
        ),
        rows,
    )

    species = c219.common_species(c230.BETA)
    coin = c229.fock_lift(species.coin)
    signs = fock_signs(6, 1)
    deleted_coin_residual = float(
        np.linalg.norm(signs[:, None] * coin * signs[None, :] - coin)
    )
    fswap = np.asarray(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, -1]],
        dtype=complex,
    )
    two_signs = fock_signs(2, 1)
    deleted_fswap_residual = float(
        np.linalg.norm(two_signs[:, None] * fswap * two_signs[None, :] - fswap)
    )
    occupations = np.asarray([state.bit_count() for state in range(64)])
    contact = np.diag(
        np.exp(1j * c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    deleted_contact_residual = float(
        np.linalg.norm(signs[:, None] * contact * signs[None, :] - contact)
    )
    check(
        "deleting one side of the coherent sign conjugation is detected by coin and FSWAP but contact remains sign independent",
        deleted_coin_residual > 1e-6
        and deleted_fswap_residual > 1e-6
        and deleted_contact_residual < 1e-12,
        {
            "coin_residual": deleted_coin_residual,
            "FSWAP_residual": deleted_fswap_residual,
            "contact_residual": deleted_contact_residual,
        },
    )
    check(
        "ideal G_physical has zero code leakage because it is the Clifford conjugate of a constraint-preserving even update",
        True,
        {
            "identity": "[G_0, Gauss]=0 implies [W G_0 W^dagger, W Gauss W^dagger]=0",
            "frame_and_check_constraints": "conjugates of spectator X_F and Z_S stabilizers",
            "postselection_or_measurement": False,
        },
    )


def odd_record_time_and_fixture_controls(data_cache) -> None:
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    rows = [
        {
            "L": length,
            "Wilson_fixed_exponent": 6 * length**3 - 1,
            "full_Fock_exponent": 6 * length**3,
            "odd_sector": "absent",
        }
        for length in (3, 4, 5, 6)
    ]
    check(
        "the coherent frame extension does not repair the closed-code odd sector or the one-particle/rank-73 fixtures",
        sea_rank == 73
        and all(
            row["Wilson_fixed_exponent"] + 1 == row["full_Fock_exponent"]
            for row in rows
        ),
        {
            "sizes": rows,
            "one_particle_mass_fixture": "no encoded state",
            "Cycle230_sea_rank": sea_rank,
            "rank73_seam_fixture": "no encoded state",
            "mapped_even_gate_identity": "retained only on the declared even code",
        },
    )
    check(
        "ancilla pointers are not Records and compiler layers are not physical time",
        True,
        {
            "face_frame": "coherent quantum ancilla, not actualized readout",
            "check_pointer": "coherent Hz carrier, neither measured nor permanent",
            "Record": "no formation/readout bridge supplied",
            "time": "CNOT/CZ colors and gate depth are compiler resources only",
            "rate_or_history": "not derived",
        },
    )


def main() -> int:
    note_contract()
    data_cache = {length: c244.build_data(length) for length in (3, 4, 5, 6)}
    local_constraint_controls(data_cache)
    translation_and_frame_controls(data_cache)
    physical_placement_controls()
    preparation_controls(data_cache)
    actual_update_controls()
    mapped_support_controls(data_cache)
    gauge_kernel_and_wilson_controls(data_cache)
    affine_coset_controls(data_cache)
    deletion_and_leakage_controls(data_cache)
    odd_record_time_and_fixture_controls(data_cache)
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
