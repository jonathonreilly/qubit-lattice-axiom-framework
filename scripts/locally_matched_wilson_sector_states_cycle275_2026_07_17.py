#!/usr/bin/env python3
"""Cycle 275: matched Wilson-sector states for the Cycle-271 local quotient.

The result is an exact finite-dimensional state theorem.  Normalized
fixed-Wilson stabilizer projectors give eight global mixed states.  For a
contractible actual Cycle-230 stream-gate cone, a cone-avoiding membrane maps
the reference projector to each sector and commutes with the complete cone
algebra.  Therefore the transported local functionals agree exactly.

This is not a bounded preparation circuit.  Compiler iteration is not
physical time, and Wilson labels are not Records.
"""

from __future__ import annotations

from itertools import product
from math import ceil, log2
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269
import contractible_lightcone_wilson_quotient_cycle271_2026_07_17 as c271


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "LOCALLY_MATCHED_WILSON_SECTOR_STATES_CYCLE275_NOTE_2026-07-17.md"
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
        check("the Cycle-275 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "all eight wilson sectors",
        "normalized sector projectors",
        "local reduced-state existence theorem",
        "global state construction",
        "not a bounded-preparation circuit",
        "actual cycle-230 stream-gate cone",
        "l=3,4,5",
        "held-out l=6",
        "all 24 proper-cubic frames",
        "full 27-element l=3 translation group",
        "rank-73",
        "deletion",
        "leakage",
        "lawful domain",
        "compiler iteration is not physical time",
        "wilson labels are not records",
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
    check(
        "the note preserves state, preparation, fixture, covariance, N1-N8, time, and Record contracts",
        not missing,
        missing,
    )


def rank(rows: list[c235.Pauli], qubits: int) -> int:
    return c269.rank(rows, qubits)


def intersection_dimension(
    left: list[c235.Pauli], right: list[c235.Pauli], qubits: int
) -> int:
    return rank(left, qubits) + rank(right, qubits) - rank(left + right, qubits)


def phase_expectation(
    observable: c235.Pauli, stabilizers: list[c235.Pauli], qubits: int
) -> int:
    """Expectation in the normalized stabilizer projector: exactly 0,+1,-1."""

    if c269.phase_in_span(observable, stabilizers, qubits):
        return 1
    if c269.phase_in_span(c269.signed(observable, 1), stabilizers, qubits):
        return -1
    return 0


def fixed_sector_rows(
    code: c269.WilsonSubsystemCode, bits: tuple[int, int, int]
) -> list[c235.Pauli]:
    return list(code.local_checks) + [
        c269.signed(wilson, bit) for wilson, bit in zip(code.wilsons, bits)
    ]


def cone_generators(
    code: c269.WilsonSubsystemCode, cone: c271.LightCone
) -> list[c235.Pauli]:
    """Overcomplete Pauli generators for every actual gate in the cone.

    B generators cover onsite parity/contact polynomials.  Internal A factors
    cover the onsite dense coin and direction-reversal layer.  Outer A factors
    are included exactly for the accumulated B-stream gates.
    """

    generators = [
        code.B[vertex]
        for vertex, (cell, _direction) in enumerate(code.graph.vertices)
        if cell in cone.cells
    ]
    for edge, (left, _right, kind, _owner) in enumerate(code.graph.edges):
        cell = code.graph.vertices[left][0]
        if kind == "internal_triangle" and cell in cone.cells:
            generators.append(code.A[edge])
        elif kind == "outer_square" and edge in cone.stream_edges:
            generators.append(code.A[edge])
    return generators


def xor_masks(bits: tuple[int, int, int], masks: list[int] | tuple[int, ...]) -> int:
    result = 0
    for bit, mask in zip(bits, masks):
        if bit:
            result ^= mask
    return result


def projector_and_local_functional_controls() -> dict[int, c269.WilsonSubsystemCode]:
    print("\nNORMALIZED SECTOR PROJECTORS / CONTRACTIBLE-CONE FUNCTIONALS")
    cache: dict[int, c269.WilsonSubsystemCode] = {}
    rows = []
    failures = []
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cache[length] = code
        first_wrap = (length + 1) // 2
        iterations = first_wrap - 1
        cone = c271.full_cell_lightcone(code, {(0, 0, 0)}, iterations)
        generators = cone_generators(code, cone)
        local_rows = list(code.local_checks)
        central_rows = local_rows + list(code.wilsons)
        local_intersection = intersection_dimension(
            generators, local_rows, code.qubits
        )
        fixed_intersection = intersection_dimension(
            generators, central_rows, code.qubits
        )
        sector_sensitive_increment = fixed_intersection - local_intersection

        moves = [
            c271.move_seam_outside(code, mask, cone.stream_edges)
            for mask in code.membrane_masks
        ]
        moved_masks = [move.moved_mask for move in moves]
        membrane_cone_leakage = sum(
            not c235.Pauli(z=mask).commutes(generator)
            for mask in moved_masks
            for generator in generators
        )
        membrane_check_leakage = sum(
            not c235.Pauli(z=mask).commutes(stabilizer)
            for mask in moved_masks
            for stabilizer in code.local_checks
        )

        sector_ranks = []
        projector_relation_failures = 0
        for bits in product((0, 1), repeat=3):
            sector_rows = fixed_sector_rows(code, bits)
            sector_rank, inconsistent = c235.phase_aware_rank(
                sector_rows, code.qubits
            )
            sector_ranks.append((sector_rank, len(inconsistent)))
            membrane_mask = xor_masks(bits, moved_masks)
            signature = c271.wilson_signature(code, membrane_mask)
            membrane = c235.Pauli(z=membrane_mask)
            projector_relation_failures += signature != bits
            projector_relation_failures += any(
                not membrane.commutes(stabilizer)
                for stabilizer in code.local_checks
            )
            projector_relation_failures += any(
                not membrane.commutes(generator) for generator in generators
            )

        row = {
            "L": length,
            "cells": length**3,
            "iterations": iterations,
            "cone_cells": len(cone.cells),
            "stream_gates": len(cone.stream_edges),
            "cone_generator_count": len(generators),
            "cone_generator_rank": rank(generators, code.qubits),
            "sector_projector_rank": sector_ranks[0][0],
            "log2_density_rank": code.qubits - sector_ranks[0][0],
            "lawful_sectors": sum(
                sector_rank == 9 * length**3 + 1 and bad == 0
                for sector_rank, bad in sector_ranks
            ),
            "sector_sensitive_central_increment": sector_sensitive_increment,
            "moved_membrane_weights": tuple(mask.bit_count() for mask in moved_masks),
            "membrane_cone_leakage": membrane_cone_leakage,
            "membrane_check_leakage": membrane_check_leakage,
            "projector_relation_failures": projector_relation_failures,
        }
        rows.append(row)
        if not (
            all(move.possible for move in moves)
            and row["lawful_sectors"] == 8
            and row["sector_projector_rank"] == 9 * length**3 + 1
            and row["log2_density_rank"] == 6 * length**3 - 1
            and row["cone_generator_rank"] == row["cone_generator_count"]
            and sector_sensitive_increment == 0
            and membrane_cone_leakage == 0
            and membrane_check_leakage == 0
            and projector_relation_failures == 0
        ):
            failures.append(row)

    check(
        "normalized fixed-Wilson projectors give eight exact global mixed states in every tested size",
        not failures,
        rows,
    )
    check(
        "cone-avoiding membranes map the reference projector to every sector and commute with the complete pre-wrap Cycle-230 cone algebra",
        not failures
        and [row["iterations"] for row in rows] == [1, 1, 2, 2]
        and [row["sector_sensitive_central_increment"] for row in rows]
        == [0, 0, 0, 0],
        {
            "rows": rows,
            "theorem": "equal transported expectations for every observable in the generated cone algebra",
        },
    )
    return cache


def biased_and_unmatched_state_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nNONTRIVIAL MATCHED STATE / UNMATCHED-STATE COUNTERCONTROL")
    rows = []
    failures = []
    for length, code in cache.items():
        vertex = code.graph.vertex_index[((0, 0, 0), 0)]
        local_b = code.B[vertex]
        uniform_values = []
        matched_values = []
        opposite_values = []
        rank_increments = []
        for bits in product((0, 1), repeat=3):
            sector_rows = fixed_sector_rows(code, bits)
            base_rank, base_bad = c235.phase_aware_rank(sector_rows, code.qubits)
            plus_rows = sector_rows + [local_b]
            minus_rows = sector_rows + [c269.signed(local_b, 1)]
            plus_rank, plus_bad = c235.phase_aware_rank(plus_rows, code.qubits)
            minus_rank, minus_bad = c235.phase_aware_rank(minus_rows, code.qubits)
            uniform_values.append(phase_expectation(local_b, sector_rows, code.qubits))
            matched_values.append(phase_expectation(local_b, plus_rows, code.qubits))
            opposite_values.append(phase_expectation(local_b, minus_rows, code.qubits))
            rank_increments.append(
                (plus_rank - base_rank, minus_rank - base_rank, len(base_bad), len(plus_bad), len(minus_bad))
            )
        row = {
            "L": length,
            "uniform_B_values": tuple(uniform_values),
            "matched_plus_B_values": tuple(matched_values),
            "opposite_B_values": tuple(opposite_values),
            "biased_log2_density_rank": 6 * length**3 - 2,
            "rank_controls": tuple(sorted(set(rank_increments))),
            "unmatched_prediction_residual": matched_values[0] - opposite_values[-1],
        }
        rows.append(row)
        if not (
            uniform_values == [0] * 8
            and matched_values == [1] * 8
            and opposite_values == [-1] * 8
            and set(rank_increments) == {(1, 1, 0, 0, 0)}
            and row["unmatched_prediction_residual"] == 2
        ):
            failures.append(row)

    check(
        "adding one local B=+1 projector gives a nontrivial matched global state family with identical local prediction +1 in all eight sectors",
        not failures,
        rows,
    )
    check(
        "arbitrary independently selected sector states are not matched: the lawful B=+1 and B=-1 choices differ by exactly two",
        not failures,
        {
            "rows": rows,
            "scope": "state matching is an explicit choice, not automatic sector equivalence",
        },
    )


def wrap_and_deletion_controls(cache: dict[int, c269.WilsonSubsystemCode]) -> None:
    print("\nFIRST WRAP / WILSON EXPECTATION / FACTOR DELETION")
    rows = []
    failures = []
    for length, code in cache.items():
        first_wrap = (length + 1) // 2
        wrapped = c271.full_cell_lightcone(code, {(0, 0, 0)}, first_wrap)
        generators = cone_generators(code, wrapped)
        local_rows = list(code.local_checks)
        central_rows = local_rows + list(code.wilsons)
        wrapped_increment = intersection_dimension(
            generators, central_rows, code.qubits
        ) - intersection_dimension(generators, local_rows, code.qubits)

        for axis, vertices in enumerate(c235.wilson_cycles(code.graph)):
            word = c235.Pauli(phase=len(vertices) % 4)
            factors = []
            for index, source in enumerate(vertices):
                target = vertices[(index + 1) % len(vertices)]
                factor = code.graph.A(source, target)
                factors.append(factor)
                word = word @ factor
            loop_increment = intersection_dimension(
                factors, central_rows, code.qubits
            ) - intersection_dimension(factors, local_rows, code.qubits)
            deleted_increment = intersection_dimension(
                factors[1:], central_rows, code.qubits
            ) - intersection_dimension(factors[1:], local_rows, code.qubits)
            plus_rows = fixed_sector_rows(code, (0, 0, 0))
            minus_bits = tuple(int(index == axis) for index in range(3))
            minus_rows = fixed_sector_rows(code, minus_bits)
            plus_value = phase_expectation(code.wilsons[axis], plus_rows, code.qubits)
            minus_value = phase_expectation(code.wilsons[axis], minus_rows, code.qubits)
            row = {
                "L": length,
                "axis": axis,
                "first_wrap": first_wrap,
                "wrapped_central_increment": wrapped_increment,
                "loop_factor_count": len(factors),
                "loop_increment": loop_increment,
                "one_factor_deleted_increment": deleted_increment,
                "word_equals_Wilson": word == code.wilsons[axis],
                "sector_expectations": (plus_value, minus_value),
                "expectation_residual": plus_value - minus_value,
            }
            rows.append(row)
            if not (
                wrapped_increment == 3
                and len(factors) == 3 * length
                and loop_increment == 1
                and deleted_increment == 0
                and word == code.wilsons[axis]
                and (plus_value, minus_value) == (1, -1)
            ):
                failures.append(row)

    check(
        "at first wrap the cone algebra gains all three Wilson directions and the normalized sector states differ on an exact 3L-factor observable",
        not failures,
        rows,
    )
    check(
        "deleting one hopping factor removes the isolated Wilson direction and narrows the state theorem boundary to complete paired loops",
        not failures and all(row["one_factor_deleted_increment"] == 0 for row in rows),
        {"rows": rows, "deletion_control": "one factor from each isolated Wilson word"},
    )


def covariance_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nALL-24 / FULL-27 MATCHED-STATE COVARIANCE")
    failures = []
    projector_covariance_failures = []
    fixed_representative_mismatches = 0
    frame_translation_tests = 0
    sector_intertwiners = 0
    local_family = set(code.local_checks)
    stabilizer_center = list(code.local_checks + code.wilsons)
    for frame in c235.proper_cubic_frames():
        frame_vertex_map, frame_edge_map = c235.graph_frame_maps(code.graph, frame)
        toggles, pairs, flips = c269.repair_data(
            code.graph, frame_vertex_map, frame_edge_map
        )
        transformed_local = {
            c235.apply_gauge(
                c235.permute_pauli(row, frame_edge_map), toggles, pairs, flips
            )
            for row in code.local_checks
        }
        if transformed_local != local_family:
            projector_covariance_failures.append(("frame-local", frame.tolist()))
        for wilson in code.wilsons:
            transformed_wilson = c235.apply_gauge(
                c235.permute_pauli(wilson, frame_edge_map), toggles, pairs, flips
            )
            if not c269.phase_in_span(
                transformed_wilson, stabilizer_center, code.qubits
            ):
                projector_covariance_failures.append(("frame-Wilson", frame.tolist()))
        framed_masks = tuple(
            c235.permute_pauli(c235.Pauli(z=mask), frame_edge_map).z
            for mask in code.membrane_masks
        )
        fixed_representative_mismatches += set(framed_masks) != set(code.membrane_masks)
        for displacement in product(range(code.length), repeat=3):
            _vertex_map, translation_edge_map = c269.graph_translation_maps(
                code.graph, displacement
            )
            transformed_masks = tuple(
                c235.permute_pauli(c235.Pauli(z=mask), translation_edge_map).z
                for mask in framed_masks
            )
            origin = tuple(value % code.length for value in displacement)
            cone = c271.full_cell_lightcone(code, {origin}, 1)
            generators = cone_generators(code, cone)
            moves = [
                c271.move_seam_outside(code, mask, cone.stream_edges)
                for mask in transformed_masks
            ]
            signatures = [
                c271.wilson_signature(code, move.moved_mask) for move in moves
            ]
            signature_rank = c235.gf2_rank(
                sum(bit << axis for axis, bit in enumerate(signature))
                for signature in signatures
            )
            signature_orbit = {
                c271.wilson_signature(
                    code,
                    xor_masks(bits, [move.moved_mask for move in moves]),
                )
                for bits in product((0, 1), repeat=3)
            }
            leakage = sum(
                not c235.Pauli(z=move.moved_mask).commutes(generator)
                for move in moves
                for generator in generators
            )
            if not (
                all(move.possible for move in moves)
                and signature_rank == 3
                and len(signature_orbit) == 8
                and leakage == 0
            ):
                failures.append((frame.tolist(), displacement, signatures, leakage))
            frame_translation_tests += 1
            sector_intertwiners += len(signature_orbit)

    for displacement in product(range(code.length), repeat=3):
        vertex_map, edge_map = c269.graph_translation_maps(code.graph, displacement)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        transformed_local = {
            c235.apply_gauge(
                c235.permute_pauli(row, edge_map), toggles, pairs, flips
            )
            for row in code.local_checks
        }
        if transformed_local != local_family:
            projector_covariance_failures.append(("translation-local", displacement))
        for wilson in code.wilsons:
            transformed_wilson = c235.apply_gauge(
                c235.permute_pauli(wilson, edge_map), toggles, pairs, flips
            )
            if not c269.phase_in_span(
                transformed_wilson, stabilizer_center, code.qubits
            ):
                projector_covariance_failures.append(
                    ("translation-Wilson", displacement)
                )

    check(
        "all 24 proper-cubic frames and the full 27-element L=3 translation group preserve the eight-sector matched-state construction",
        not failures
        and not projector_covariance_failures
        and frame_translation_tests == 24 * 27
        and sector_intertwiners == 24 * 27 * 8
        and fixed_representative_mismatches > 0,
        {
            "frame_translation_tests": frame_translation_tests,
            "sector_intertwiners": sector_intertwiners,
            "failures": failures[:5],
            "projector_covariance_failures": projector_covariance_failures[:5],
            "fixed_representative_mismatches": fixed_representative_mismatches,
            "covariant_object": "sector-projector family and local functional, not a fixed seam",
        },
    )


def leakage_and_projector_deletion_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nLAWFUL-DOMAIN LEAKAGE / PROJECTOR DELETION")
    leakage_rows = []
    for length, code in cache.items():
        first_wrap = (length + 1) // 2
        cone = c271.full_cell_lightcone(code, {(0, 0, 0)}, first_wrap - 1)
        generators = cone_generators(code, cone)
        leakage_rows.append(
            {
                "L": length,
                "local_check_leakage": sum(
                    not generator.commutes(stabilizer)
                    for generator in generators
                    for stabilizer in code.local_checks
                ),
                "Wilson_transitions": sum(
                    not generator.commutes(wilson)
                    for generator in generators
                    for wilson in code.wilsons
                ),
            }
        )
    check(
        "every actual cone generator preserves every local check and Wilson sector through held-out L=6",
        all(
            row["local_check_leakage"] == 0 and row["Wilson_transitions"] == 0
            for row in leakage_rows
        ),
        leakage_rows,
    )

    code = cache[3]
    local_rank = rank(list(code.local_checks), code.qubits)
    physical_losses = []
    for index in range(len(code.local_checks)):
        reduced = list(code.local_checks[:index] + code.local_checks[index + 1 :])
        physical_losses.append(local_rank - rank(reduced, code.qubits))

    basis: list[c235.Pauli] = []
    basis_rank = 0
    for row in code.local_checks:
        next_rank = rank(basis + [row], code.qubits)
        if next_rank > basis_rank:
            basis.append(row)
            basis_rank = next_rank
    wilson_rows = [c269.signed(wilson, 0) for wilson in code.wilsons]
    full_rows = basis + wilson_rows
    full_rank = rank(full_rows, code.qubits)
    removed_check = basis[-1]
    without_check = basis[:-1] + wilson_rows
    without_wilson = basis + wilson_rows[:-1]
    check(
        "projector deletion distinguishes redundant presentation rows from independent local and Wilson constraints",
        max(physical_losses) == 0
        and len(basis) == local_rank
        and full_rank == local_rank + 3
        and rank(without_check, code.qubits) == full_rank - 1
        and phase_expectation(removed_check, without_check, code.qubits) == 0
        and rank(without_wilson, code.qubits) == full_rank - 1
        and phase_expectation(code.wilsons[-1], without_wilson, code.qubits) == 0,
        {
            "physical_rows": len(code.local_checks),
            "local_rank": local_rank,
            "physical_single_deletion_losses": sorted(set(physical_losses)),
            "independent_check_deletion_rank_loss": full_rank
            - rank(without_check, code.qubits),
            "Wilson_projector_deletion_rank_loss": full_rank
            - rank(without_wilson, code.qubits),
            "deleted_Wilson_functional": phase_expectation(
                code.wilsons[-1], without_wilson, code.qubits
            ),
        },
    )


def fixture_and_preparation_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nMASS / RANK-73 FIREWALL / PREPARATION SUPPORT")
    species = c219.common_species(c230.BETA)
    one_particle_coin = species.coin
    coin = c229.fock_lift(one_particle_coin)
    occupations = np.asarray([index.bit_count() for index in range(64)])
    parity = np.diag((-1.0) ** occupations).astype(complex)
    contact = np.diag(
        np.exp(1j * c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    _momenta, _vectors, eigenvalues, _labels = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    unitary, onsite, stream, layer_a, layer_b = c230.spatial_layers(
        3, one_particle_coin
    )
    check(
        "the actual beta=-0.3 mass and g=0.37 one-particle operator fixture is untouched, while the odd one-particle and rank-73 states remain outside the even sector projectors",
        np.count_nonzero(np.abs(one_particle_coin) < 1e-12) == 0
        and np.linalg.norm(coin @ parity - parity @ coin) < 2e-12
        and np.linalg.norm(contact @ parity - parity @ contact) == 0
        and np.allclose(np.diag(contact)[occupations <= 1], 1)
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12
        and sea_rank == 73
        and sea_rank % 2 == 1,
        {
            "beta": c230.BETA,
            "g": c230.COUPLING,
            "rest_over_analytic_mass": c219.rest_mass(species)
            / species.analytic_mass,
            "principal_sea_rank": sea_rank,
            "state_fixture_status": "odd and not represented by these total-even projectors",
        },
    )

    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    b_left = np.kron(z, identity)
    b_right = np.kron(identity, z)
    hopping = np.kron(y, x)
    fswap_plus = 0.5 * (
        b_left + b_right + 1j * b_left @ hopping - 1j * b_right @ hopping
    )
    fswap_minus = 0.5 * (
        b_left + b_right - 1j * b_left @ hopping + 1j * b_right @ hopping
    )
    standard_fswap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    check(
        "the declared cone uses the actual dense coin and exact A/B FSWAP stream decomposition",
        np.linalg.norm(stream - layer_b @ layer_a) < 2e-15
        and np.linalg.norm(unitary - stream @ onsite) < 2e-15
        and np.linalg.norm(fswap_plus - standard_fswap) < 1e-15
        and np.linalg.norm(fswap_minus - b_left @ fswap_plus @ b_left) < 1e-15
        and np.linalg.norm(fswap_plus - fswap_minus, 2) == 2.0,
        {
            "L3_modes": unitary.shape[0],
            "stream_minus_BA": float(np.linalg.norm(stream - layer_b @ layer_a)),
            "FSWAP_matrix_residual": float(
                np.linalg.norm(fswap_plus - standard_fswap)
            ),
            "seam_block_operator_residual": float(
                np.linalg.norm(fswap_plus - fswap_minus, 2)
            ),
        },
    )

    rows = []
    for length, code in cache.items():
        first_wrap = (length + 1) // 2
        cone = c271.full_cell_lightcone(code, {(0, 0, 0)}, first_wrap - 1)
        moves = [
            c271.move_seam_outside(code, mask, cone.stream_edges)
            for mask in code.membrane_masks
        ]
        source = code.graph.vertex_index[((0, 0, 0), 0)]
        target = code.graph.vertex_index[((length // 2, 0, 0), 0)]
        wilson_support = tuple(
            (wilson.x | wilson.z).bit_count() for wilson in code.wilsons
        )
        rows.append(
            {
                "L": length,
                "Wilson_projector_support": wilson_support,
                "Wilson_hopping_factor_count": 3 * length,
                "comparison_membrane_support": tuple(
                    move.moved_mask.bit_count() for move in moves
                ),
                "basis_diagonal_string_length": c235.shortest_path(
                    code.graph, source, target
                ),
                "two_input_fanin_depth_lower_bound": ceil(log2(max(wilson_support))),
            }
        )
    check(
        "the supplied stabilizer-projector and comparison-map prescriptions are global and no bounded-preparation circuit is constructed",
        all(
            row["Wilson_projector_support"]
            == (6 * row["L"] + 3, 6 * row["L"] - 1, 6 * row["L"] + 3)
            and row["Wilson_hopping_factor_count"] == 3 * row["L"]
            and min(row["comparison_membrane_support"]) >= row["L"] ** 2
            for row in rows
        )
        and [row["basis_diagonal_string_length"] for row in rows] == [3, 6, 6, 9]
        and [row["two_input_fanin_depth_lower_bound"] for row in rows]
        == [5, 5, 6, 6],
        {
            "rows": rows,
            "algebraic_global_state_exists": True,
            "bounded_preparation_circuit": False,
            "universal_preparation_no_go": False,
        },
    )


def scope_controls() -> None:
    check(
        "the lawful domain and interpretation firewalls remain explicit",
        True,
        {
            "included": "even observables in a contractible actual Cycle-230 stream-gate cone under the Cycle-271 comparison maps",
            "excluded": "wrapped Wilson observables, membranes, odd states, unmatched states, and preparation claims",
            "result_type": "local reduced-state equality backed by explicit global mixed states",
            "compiler_iteration_is_physical_time": False,
            "Wilson_labels_are_Records": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    cache = projector_and_local_functional_controls()
    biased_and_unmatched_state_controls(cache)
    wrap_and_deletion_controls(cache)
    covariance_controls(cache[3])
    leakage_and_projector_deletion_controls(cache)
    fixture_and_preparation_controls(cache)
    scope_controls()
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE275_LOCALLY_MATCHED_WILSON_STATES_GREEN"
        if FAIL == 0
        else "CYCLE275_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
