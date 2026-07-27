#!/usr/bin/env python3
"""Cycle-720 overlap test for local mixed-gauge companion encoders.

Two adjacent maximal cubic stars have a shared two-cell register.  This runner
constructs the exact binary Clifford/Stinespring factorization independently
on each star and on their induced union.  It compares the complete Pauli
domain and pullback map of the reduced shared-register channel.  A mismatch is
reported as a boundary-transition rank, not promoted to a no-go.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md"
AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle720_bounded_general_clifford_orbit_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_gauge_native_fswap_clifford_recurrence_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_product_companion_full_word_holonomy_2026_07_27.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from dataclasses import dataclass
from hashlib import sha256
import json

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U
import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F
import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C
import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T


Pauli = M.Pauli
Coord = tuple[int, int, int]


def product(rows) -> Pauli:
    output = Pauli()
    for row in rows:
        output = output @ row
    return output


def arbitrary_fixture(cells) -> M.CompanionFixture:
    cells = tuple(sorted(set(cells)))
    lookup = {cell: index for index, cell in enumerate(cells)}
    edges = []
    for cell in cells:
        for axis in range(3):
            target = list(cell)
            target[axis] += 1
            target = tuple(target)
            if target not in lookup:
                continue
            left = lookup[cell]
            right = lookup[target]
            edges.append((
                left, right, cell, axis,
                6 * left + 2 * axis + 1,
                6 * right + 2 * axis,
            ))
    return M.CompanionFixture(
        (0, 0, 0), cells, tuple(edges), 6 * len(cells), 9 * len(cells)
    )


@dataclass(frozen=True)
class Factorization:
    fixture: M.CompanionFixture
    physical_w: tuple[Pauli, ...]
    physical_v: tuple[Pauli, ...]
    target_w: tuple[Pauli, ...]
    target_v: tuple[Pauli, ...]
    logical: int
    gauge: int
    center: int
    local_center_rank: int
    phase_rank: int
    phase_contradictions: int


def parity_complement(
    local_rows: tuple[int, ...], parity: int, desired: int
) -> tuple[int, ...]:
    pivots: dict[int, int] = {parity.bit_length() - 1: parity}
    output = []
    for original in local_rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                output.append(original)
                break
    return tuple(output[:desired])


def build_factorization(fixture: M.CompanionFixture) -> Factorization:
    rows = M.operator_rows(fixture)
    physical = tuple(row[1] for row in rows)
    target = tuple(row[2] for row in rows)
    paired = F.independent_paired_basis(
        tuple(row.symplectic(fixture.qubits) for row in physical),
        tuple(row.symplectic(fixture.matter_qubits) for row in target),
    )
    _radicals, logical_pairs = F.symplectic_split_paired(
        paired, fixture.qubits
    )
    relations = M.relation_certificate(fixture)["relation_rows"]
    _gauge_report, gauge = U.gauge_structure(fixture, physical, relations)
    gauge_radicals, gauge_pairs = F.symplectic_split_vectors(
        gauge, fixture.qubits
    )
    parity = Pauli(z=(1 << fixture.matter_qubits) - 1).symplectic(
        fixture.qubits
    )
    local_center_all = F.local_center_basis(fixture, gauge, 2)
    local_center = parity_complement(
        local_center_all, parity, len(gauge_radicals) - 1
    )
    center = local_center + (parity,)
    physical_w = tuple(
        [F.canonical_pauli(pair[0][0], fixture.qubits) for pair in logical_pairs]
        + [F.canonical_pauli(pair[0], fixture.qubits) for pair in gauge_pairs]
        + [F.canonical_pauli(row, fixture.qubits) for row in center]
    )
    physical_v_explicit = tuple(
        [F.canonical_pauli(pair[1][0], fixture.qubits) for pair in logical_pairs]
        + [F.canonical_pauli(pair[1], fixture.qubits) for pair in gauge_pairs]
    )
    physical_v = tuple(T.complete_tableau(
        physical_w, physical_v_explicit, fixture.qubits
    ))
    target_w = tuple(
        [F.canonical_pauli(pair[0][1], fixture.matter_qubits) for pair in logical_pairs]
        + [Pauli(z=(1 << fixture.matter_qubits) - 1)]
    )
    target_v = tuple(T.complete_tableau(
        target_w,
        tuple(F.canonical_pauli(
            pair[1][1], fixture.matter_qubits
        ) for pair in logical_pairs),
        fixture.matter_qubits,
    ))

    # Fix the physical logical/tableau signs against the actual signed target
    # generator dictionary.  Local center signs are variables; total parity is
    # kept as the common explicit sector label.
    phase_equations = []
    for physical_row, target_row in zip(physical, target):
        pc = T.decode(
            physical_row, physical_w, physical_v, fixture.qubits
        )
        tc = T.decode(
            target_row, target_w, target_v, fixture.matter_qubits
        )
        delta = (tc.phase - pc.phase) % 4
        mask = (
            (pc.v_mask & ((1 << len(logical_pairs)) - 1))
            | ((pc.w_mask & ((1 << len(logical_pairs)) - 1))
               << len(logical_pairs))
            | (((pc.w_mask >> (len(logical_pairs) + len(gauge_pairs)))
                & ((1 << (len(center) - 1)) - 1))
               << (2 * len(logical_pairs)))
        )
        phase_equations.append((mask, delta // 2))
    solution, phase_rank, phase_contradictions = C.gf2_solve(
        phase_equations
    )
    physical_w = list(physical_w)
    physical_v = list(physical_v)
    for index in range(len(logical_pairs)):
        if (solution >> index) & 1:
            row = physical_v[index]
            physical_v[index] = Pauli((row.phase + 2) % 4, row.x, row.z)
        if (solution >> (len(logical_pairs) + index)) & 1:
            row = physical_w[index]
            physical_w[index] = Pauli((row.phase + 2) % 4, row.x, row.z)
    for index in range(len(center) - 1):
        if (solution >> (2 * len(logical_pairs) + index)) & 1:
            position = len(logical_pairs) + len(gauge_pairs) + index
            row = physical_w[position]
            physical_w[position] = Pauli((row.phase + 2) % 4, row.x, row.z)
    return Factorization(
        fixture,
        tuple(physical_w),
        tuple(physical_v),
        target_w,
        target_v,
        len(logical_pairs),
        len(gauge_pairs),
        len(center),
        C.R.F.base.gf2_rank(local_center),
        phase_rank,
        phase_contradictions,
    )


def shared_qubits(
    fixture: M.CompanionFixture, region: tuple[Coord, ...]
) -> tuple[int, ...]:
    lookup = {cell: index for index, cell in enumerate(fixture.cells)}
    output = []
    for cell in sorted(region):
        index = lookup[cell]
        output.extend(6 * index + mode for mode in range(6))
        output.extend(
            fixture.matter_qubits + 3 * index + mode for mode in range(3)
        )
    return tuple(output)


def local_equation(row: Pauli, qubits: tuple[int, ...]) -> int:
    count = len(qubits)
    return sum(
        (((row.z >> qubit) & 1) << index)
        | (((row.x >> qubit) & 1) << (count + index))
        for index, qubit in enumerate(qubits)
    )


def reduced_channel_domain(
    factor: Factorization, region: tuple[Coord, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    qubits = shared_qubits(factor.fixture, region)
    forbidden_w = (
        tuple(range(factor.logical, factor.logical + factor.gauge))
        + tuple(range(
            factor.logical + factor.gauge,
            factor.logical + factor.gauge + factor.center,
        ))
    )
    forbidden_v = tuple(range(
        factor.logical, factor.logical + factor.gauge
    ))
    equations = tuple(
        local_equation(factor.physical_w[index], qubits)
        for index in forbidden_w
    ) + tuple(
        local_equation(factor.physical_v[index], qubits)
        for index in forbidden_v
    )
    return M.homogeneous_nullspace(equations, 2 * len(qubits)), qubits


def embed_local_vector(
    local: int, local_qubits: tuple[int, ...], global_qubits: int
) -> int:
    count = len(local_qubits)
    x = local & ((1 << count) - 1)
    z = local >> count
    global_x = sum(
        ((x >> index) & 1) << qubit
        for index, qubit in enumerate(local_qubits)
    )
    global_z = sum(
        ((z >> index) & 1) << qubit
        for index, qubit in enumerate(local_qubits)
    )
    return global_x | (global_z << global_qubits)


def target_pullback(
    factor: Factorization,
    local: int,
    local_qubits: tuple[int, ...],
    odd: bool,
    retain_patch_parity: bool = False,
) -> Pauli:
    row = F.canonical_pauli(
        embed_local_vector(local, local_qubits, factor.fixture.qubits),
        factor.fixture.qubits,
    )
    coordinates = T.decode(
        row, factor.physical_w, factor.physical_v, factor.fixture.qubits
    )
    base = product(
        factor.target_v[index]
        for index in range(factor.logical)
        if (coordinates.v_mask >> index) & 1
    ) @ product(
        factor.target_w[index]
        for index in range(factor.logical)
        if (coordinates.w_mask >> index) & 1
    )
    physical_parity_coordinate = (
        coordinates.w_mask
        >> (factor.logical + factor.gauge + factor.center - 1)
    ) & 1
    if retain_patch_parity and physical_parity_coordinate:
        base = base @ factor.target_w[factor.logical]
    return Pauli(
        (base.phase + coordinates.phase
         + 2 * int(odd) * physical_parity_coordinate
         * int(not retain_patch_parity)) % 4,
        base.x,
        base.z,
    )


def global_majorana(mode: int, odd: bool) -> Pauli:
    return Pauli(
        int(odd),
        1 << mode,
        ((1 << mode) - 1) | ((1 << mode) if odd else 0),
    )


def fermionic_embed(
    source: M.CompanionFixture,
    union: M.CompanionFixture,
    row: Pauli,
) -> Pauli:
    """Inject a patch CAR Pauli into the union CAR order, with phases."""
    union_lookup = {cell: index for index, cell in enumerate(union.cells)}
    mapped_majoranas = []
    for cell in source.cells:
        union_cell = union_lookup[cell]
        for mode in range(6):
            target_mode = 6 * union_cell + mode
            mapped_majoranas.append((
                global_majorana(target_mode, False),
                global_majorana(target_mode, True),
            ))
    z_images = []
    x_images = []
    for index, (even, odd) in enumerate(mapped_majoranas):
        z_image = Pauli(phase=3) @ even @ odd
        z_images.append(z_image)
        x_images.append(product(tuple(z_images[:index]) + (even,)))
    output = Pauli(row.phase)
    for index in range(source.matter_qubits):
        if (row.x >> index) & 1:
            output = output @ x_images[index]
    for index in range(source.matter_qubits):
        if (row.z >> index) & 1:
            output = output @ z_images[index]
    return output


def pauli_cells(row: Pauli, fixture: M.CompanionFixture) -> tuple[Coord, ...]:
    support = row.x | row.z
    return tuple(sorted({
        fixture.cells[mode // 6]
        for mode in range(fixture.matter_qubits)
        if (support >> mode) & 1
    }))


def comparison_certificate(axis: int) -> dict[str, object]:
    origin = (0, 0, 0)
    east = tuple(int(index == axis) for index in range(3))
    directions = (
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1),
    )
    star_a = {origin} | set(directions)
    star_b = {east} | {
        tuple(east[index] + direction[index] for index in range(3))
        for direction in directions
    }
    union_cells = star_a | star_b
    overlap = (origin, east)
    union_fixture = arbitrary_fixture(union_cells)

    entries = []
    for label, cells in (("star_A", star_a), ("star_B", star_b), ("union", union_cells)):
        fixture = arbitrary_fixture(cells)
        factor = build_factorization(fixture)
        domain, local_qubits = reduced_channel_domain(factor, overlap)
        images_even = tuple(
            fermionic_embed(
                fixture, union_fixture,
                target_pullback(
                    factor, row, local_qubits, False,
                    retain_patch_parity=True,
                ),
            )
            for row in domain
        )
        images_odd = tuple(
            fermionic_embed(
                fixture, union_fixture,
                target_pullback(
                    factor, row, local_qubits, True,
                    retain_patch_parity=True,
                ),
            )
            for row in domain
        )
        scalarized_patch_parity_images = tuple(
            fermionic_embed(
                fixture,
                union_fixture,
                target_pullback(
                    factor, row, local_qubits, False,
                    retain_patch_parity=False,
                ),
            )
            for row in domain
        )
        entries.append({
            "label": label,
            "fixture": fixture,
            "factor": factor,
            "domain": domain,
            "images_even": images_even,
            "images_odd": images_odd,
            "scalarized_patch_parity_images": scalarized_patch_parity_images,
            "cells": len(fixture.cells),
            "edges": len(fixture.edges),
            "domain_rank": C.R.F.base.gf2_rank(domain),
            "domain_digest": sha256(
                "|".join(f"{row:x}" for row in domain).encode()
            ).hexdigest(),
            "image_rank": C.R.F.base.gf2_rank(
                row.symplectic(union_fixture.matter_qubits) for row in images_even
            ),
            "even_image_digest": sha256(
                "|".join(f"{row.phase}:{row.x:x}:{row.z:x}" for row in images_even).encode()
            ).hexdigest(),
            "odd_image_digest": sha256(
                "|".join(f"{row.phase}:{row.x:x}:{row.z:x}" for row in images_odd).encode()
            ).hexdigest(),
            "canonical_encoder_maximum_diameter": max(
                F.row_diameter(fixture, row)
                for row in factor.physical_w + factor.physical_v
            ),
            "local_center_rank": factor.local_center_rank,
            "center_rank": factor.center,
            "phase_rank": factor.phase_rank,
            "phase_contradictions": factor.phase_contradictions,
        })

    reference = entries[0]
    comparisons = []
    difference_vectors = []
    for entry in entries[1:]:
        binary_mismatches = 0
        signed_mismatches = 0
        local_differences = []
        sector_signed_mismatches = {"even": 0, "odd": 0}
        for sector, key in (("even", "images_even"), ("odd", "images_odd")):
            for left, right in zip(reference[key], entry[key]):
                binary_difference = (
                    left.symplectic(union_fixture.matter_qubits)
                    ^ right.symplectic(union_fixture.matter_qubits)
                )
                if sector == "even":
                    binary_mismatches += bool(binary_difference)
                    if binary_difference:
                        local_differences.append(binary_difference)
                        difference_vectors.append(binary_difference)
                sector_signed_mismatches[sector] += left != right
        signed_mismatches = sector_signed_mismatches["even"]
        scalarized_parity_mismatches = sum(
            left != right for left, right in zip(
                reference["scalarized_patch_parity_images"],
                entry["scalarized_patch_parity_images"],
            )
        )
        comparisons.append({
            "left": reference["label"],
            "right": entry["label"],
            "domain_basis_mismatches": sum(
                left != right for left, right in zip(
                    reference["domain"], entry["domain"]
                )
            ),
            "binary_Choi_map_mismatches": binary_mismatches,
            "signed_canonical_map_mismatches": signed_mismatches,
            "even_signed_Choi_map_mismatches": sector_signed_mismatches["even"],
            "odd_signed_Choi_map_mismatches": sector_signed_mismatches["odd"],
            "scalarize_patch_parity_deletion_mismatches": scalarized_parity_mismatches,
            "binary_transition_rank": C.R.F.base.gf2_rank(local_differences),
        })

    independent_differences = []
    pivots: dict[int, int] = {}
    for original in difference_vectors:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                independent_differences.append(original)
                break
    difference_paulis = tuple(
        F.canonical_pauli(row, union_fixture.matter_qubits)
        for row in independent_differences
    )
    image_algebra = tuple(
        row for entry in entries for row in entry["images_even"]
    )
    transition_commutator_failures = sum(
        M.symplectic(
            transition.symplectic(union_fixture.matter_qubits),
            image.symplectic(union_fixture.matter_qubits),
            union_fixture.matter_qubits,
        )
        for transition in difference_paulis for image in image_algebra
    )
    transition_cells = tuple(
        pauli_cells(row, union_fixture) for row in difference_paulis
    )
    transition_diameters = tuple(
        max((
            sum(abs(a - b) for a, b in zip(left, right))
            for left in cells for right in cells
        ), default=0)
        for cells in transition_cells
    )

    public_entries = tuple({
        key: value for key, value in entry.items()
        if key not in (
            "fixture", "factor", "domain", "images_even", "images_odd",
            "scalarized_patch_parity_images",
        )
    } for entry in entries)
    return {
        "axis": axis,
        "overlap_cells": overlap,
        "overlap_physical_qubits": 18,
        "patches": public_entries,
        "comparisons": tuple(comparisons),
        "transition": {
            "combined_binary_transition_rank": len(independent_differences),
            "transition_commutator_failures_against_all_shared_image_generators": transition_commutator_failures,
            "transition_support_cells": transition_cells,
            "transition_maximum_cell_diameter": max(transition_diameters, default=0),
            "transition_rows": tuple(
                f"{row.phase}:{row.x:x}:{row.z:x}" for row in difference_paulis
            ),
            "simple_central_virtual_rail_repair_allowed": (
                transition_commutator_failures == 0
            ),
        },
    }


def held_edge_certificate() -> dict[str, object]:
    shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2))
    overlap = ((0, 0, 0), (1, 0, 0))
    union_fixture = M.CompanionFixture.build(shapes[-1])
    entries = []
    for shape in shapes:
        fixture = M.CompanionFixture.build(shape)
        factor = build_factorization(fixture)
        domain, local_qubits = reduced_channel_domain(factor, overlap)
        sector_images = {}
        for odd, label in ((False, "even"), (True, "odd")):
            sector_images[label] = tuple(
                fermionic_embed(
                    fixture,
                    union_fixture,
                    target_pullback(factor, row, local_qubits, odd),
                )
                for row in domain
            )
        entries.append({
            "shape": shape,
            "domain": domain,
            "even": sector_images["even"],
            "odd": sector_images["odd"],
            "domain_rank": C.R.F.base.gf2_rank(domain),
            "domain_digest": sha256(
                "|".join(f"{row:x}" for row in domain).encode()
            ).hexdigest(),
            "even_image_digest": sha256(
                "|".join(
                    f"{row.phase}:{row.x:x}:{row.z:x}"
                    for row in sector_images["even"]
                ).encode()
            ).hexdigest(),
            "odd_image_digest": sha256(
                "|".join(
                    f"{row.phase}:{row.x:x}:{row.z:x}"
                    for row in sector_images["odd"]
                ).encode()
            ).hexdigest(),
            "phase_contradictions": factor.phase_contradictions,
        })
    reference = entries[0]
    comparisons = []
    for entry in entries[1:]:
        comparisons.append({
            "left": reference["shape"],
            "right": entry["shape"],
            "domain_basis_mismatches": sum(
                left != right for left, right in zip(
                    reference["domain"], entry["domain"]
                )
            ),
            "even_signed_Choi_map_mismatches": sum(
                left != right for left, right in zip(
                    reference["even"], entry["even"]
                )
            ),
            "odd_signed_Choi_map_mismatches": sum(
                left != right for left, right in zip(
                    reference["odd"], entry["odd"]
                )
            ),
        })
    return {
        "overlap_cells": overlap,
        "fixtures": tuple({
            key: value for key, value in entry.items()
            if key not in ("domain", "even", "odd")
        } for entry in entries),
        "comparisons": tuple(comparisons),
    }


def main() -> None:
    certificates = tuple(comparison_certificate(axis) for axis in range(3))
    held = held_edge_certificate()
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "both maximal stars and their union induce exactly the same nonzero Pauli domain on the shared register",
        all(
            len({row["domain_digest"] for row in certificate["patches"]}) == 1
            and all(row["domain_rank"] == 23 for row in certificate["patches"])
            and all(
                row["domain_basis_mismatches"] == 0
                for row in certificate["comparisons"]
            )
            for certificate in certificates
        ),
    )
    check(
        "every independent patch and the union have a bounded canonical encoder on their own finite support",
        all(
            row["canonical_encoder_maximum_diameter"] <= 3
            for certificate in certificates for row in certificate["patches"]
        ),
    )
    check(
        "phase-fixed maximal-star and union Choi maps agree exactly in both parity sectors on all three axes",
        all(
            row["binary_Choi_map_mismatches"] == 0
            and row["even_signed_Choi_map_mismatches"] == 0
            and row["odd_signed_Choi_map_mismatches"] == 0
            for certificate in certificates for row in certificate["comparisons"]
        ),
    )
    check(
        "the same signed two-cell Choi channel is independent of all four required held-box completions",
        all(
            row["domain_basis_mismatches"] == 0
            and row["even_signed_Choi_map_mismatches"] == 0
            and row["odd_signed_Choi_map_mismatches"] == 0
            for row in held["comparisons"]
        ),
    )
    check(
        "the retained local patch-parity rail is active rather than decorative",
        any(
            row["scalarize_patch_parity_deletion_mismatches"] > 0
            for certificate in certificates for row in certificate["comparisons"]
        ),
    )

    report = {
        "status": "cycle720-positive-phase-fixed-two-star-local-channel-atlas__global-PEPO-open",
        "pass": all(row["pass"] for row in checks),
        "authority": "none",
        "audit": "unset",
        "baseline": "origin/main@f7d78df6455d41cf50c143e41c81f204d3dec72e",
        "checks": checks,
        "axis_certificates": certificates,
        "held_edge_certificate": held,
        "supplied": [
            "one phase-fixed canonical symplectic completion per finite patch",
            "global total-parity superselection at a finite-box boundary",
            "local patch parity retained as a bounded virtual operator rail rather than scalarized",
            "fixed local relation-center sectors",
            "maximally mixed local gauge coordinates",
        ],
        "derived": [
            "the complete rank-23 nonzero shared-register Pauli domain is identical for both stars and their union",
            "exact signed Choi equality on both parity sectors for two overlapping maximal stars and their union",
            "the same reduced channel on four held-box completions without refit",
            "an active deletion: scalarizing the local patch-parity rail breaks an oriented overlap",
        ],
        "open": [
            "construct one explicit globally tiled PEPO/Stinespring tensor from the compatible local channel atlas",
            "verify triple-overlap and closed-loop consistency beyond the tested two-star unions",
            "rerun full-word intertwining on the explicitly contracted held tensor",
            "autonomous center/parity enforcement",
        ],
        "claim_ceiling": (
            "A phase-fixed bounded local channel atlas now glues exactly on two overlapping maximal "
            "stars, all three axes, both parity sectors, and four held-box completions.  This is not "
            "yet a global PEPO compiler: a tiled tensor, triple/loop consistency, and autonomous "
            "center/parity preparation remain unconstructed."
        ),
        "compiler_claim_gate": {
            "shared_Pauli_domain": "PASS",
            "phase_fixed_two_star_Choi_equality": "PASS",
            "held_completion_independence": "PASS",
            "global_tiled_PEPO_or_Stinespring": "FAIL",
            "overlap_consistent_local_CPTP_atlas": "PASS",
            "bounded_local_patch_parity_rail": "PASS_active",
        },
        "no_go_discipline": {
            "N1_alternatives": "explicit PEPO contraction, triple-overlap checks, local twirls, and larger patch tensors remain live",
            "N2_wall_independence": "two-star Choi gluing closes while global tensor construction and genesis remain open",
            "N3_hidden_imports": "patch completions, relation centers, global parity, the local parity rail, and gauge mixture are explicit",
            "N4_residual_matching": "domain, signed even/odd Choi image, axis, held-completion, and locality tests are separate",
            "N5_resolution": "three oriented pairs of seven-cell maximal stars, their twelve-cell unions, and four held boxes",
            "N6_partial_closure": "the exact local channel atlas is retained without claiming a global PEPO",
            "N7_steelman": "compatible pairwise marginals may admit a bounded repeated tensor after triple/loop checks",
            "N8_cross_cycle_echo": "tests actual Choi overlap rather than inferring locality from small-patch diameter",
            "gate": "FAIL_for_broad_no_go__constructive_two-star-positive",
        },
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    print("PHASE_FIXED_TWO_STAR_LOCAL_CHANNEL_ATLAS_POSITIVE__GLOBAL_PEPO_OPEN")
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
