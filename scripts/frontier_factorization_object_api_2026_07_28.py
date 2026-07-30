#!/usr/bin/env python3
"""Immutable access to the exact Cycle-720 mixed-gauge factorization.

This module provides finite-box support code.  It reconstructs the
convention-sensitive Cycle-720 tableau without changing either landed runner,
exposes the finite operator dictionary in factor coordinates, and refuses to
return an object whose ordered physical signed-tableau digest differs from the
landed factorization certificate.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/FACTORIZATION_OBJECT_API_SUPPORT_NOTE_2026-07-28.md"
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

from dataclasses import FrozenInstanceError, dataclass
from hashlib import sha256
import json
from time import perf_counter

import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M


Pauli = M.Pauli


@dataclass(frozen=True)
class DictionaryCoordinate:
    """One signed physical/target dictionary row in factor coordinates."""

    index: int
    family: str
    physical_row: Pauli
    target_row: Pauli
    logical_v_mask: int
    logical_w_mask: int
    gauge_v_mask: int
    gauge_w_mask: int
    center_v_mask: int
    center_w_mask: int
    target_logical_v_mask: int
    target_logical_w_mask: int
    target_center_v_mask: int
    target_center_w_mask: int
    physical_even_phase: int
    physical_odd_phase: int
    target_even_phase: int
    target_odd_phase: int


@dataclass(frozen=True)
class FactorizationObject:
    """Immutable finite-box signed-tableau factorization object."""

    shape: tuple[int, int, int]
    physical_w: tuple[Pauli, ...]
    physical_v: tuple[Pauli, ...]
    target_w: tuple[Pauli, ...]
    target_v: tuple[Pauli, ...]
    logical_count: int
    gauge_count: int
    center_count: int
    dictionary_coordinates: tuple[DictionaryCoordinate, ...]
    tableau_digest: str


def _tableau_digest(
    physical_w: tuple[Pauli, ...], physical_v: tuple[Pauli, ...]
) -> str:
    rows = physical_w + physical_v
    payload = "|".join(f"{row.phase}:{row.x:x}:{row.z:x}" for row in rows)
    return sha256(payload.encode()).hexdigest()


def _dictionary_coordinate(
    index: int,
    family: str,
    physical: Pauli,
    target: Pauli,
    physical_coordinates: object,
    target_coordinates: object,
    logical_count: int,
    gauge_count: int,
    center_count: int,
) -> DictionaryCoordinate:
    logical_mask = (1 << logical_count) - 1
    gauge_mask = (1 << gauge_count) - 1
    center_mask = (1 << center_count) - 1
    logical_v_mask = physical_coordinates.v_mask & logical_mask
    logical_w_mask = physical_coordinates.w_mask & logical_mask
    gauge_v_mask = (
        physical_coordinates.v_mask >> logical_count
    ) & gauge_mask
    gauge_w_mask = (
        physical_coordinates.w_mask >> logical_count
    ) & gauge_mask
    center_offset = logical_count + gauge_count
    center_v_mask = (physical_coordinates.v_mask >> center_offset) & center_mask
    center_w_mask = (physical_coordinates.w_mask >> center_offset) & center_mask
    target_logical_v_mask = target_coordinates.v_mask & logical_mask
    target_logical_w_mask = target_coordinates.w_mask & logical_mask
    target_center_v_mask = (target_coordinates.v_mask >> logical_count) & 1
    target_center_w_mask = (target_coordinates.w_mask >> logical_count) & 1
    physical_parity = (center_w_mask >> (center_count - 1)) & 1
    target_parity = target_center_w_mask
    return DictionaryCoordinate(
        index=index,
        family=family,
        physical_row=physical,
        target_row=target,
        logical_v_mask=logical_v_mask,
        logical_w_mask=logical_w_mask,
        gauge_v_mask=gauge_v_mask,
        gauge_w_mask=gauge_w_mask,
        center_v_mask=center_v_mask,
        center_w_mask=center_w_mask,
        target_logical_v_mask=target_logical_v_mask,
        target_logical_w_mask=target_logical_w_mask,
        target_center_v_mask=target_center_v_mask,
        target_center_w_mask=target_center_w_mask,
        physical_even_phase=physical_coordinates.phase,
        physical_odd_phase=(
            physical_coordinates.phase + 2 * physical_parity
        ) % 4,
        target_even_phase=target_coordinates.phase,
        target_odd_phase=(target_coordinates.phase + 2 * target_parity) % 4,
    )


def build_factorization_object(
    shape: tuple[int, int, int],
) -> FactorizationObject:
    """Reconstruct and digest-bind F's exact canonical mixed-gauge tableau."""

    fixture = M.CompanionFixture.build(shape)
    rows = M.operator_rows(fixture)
    physical_paulis = tuple(row[1] for row in rows)
    target_paulis = tuple(row[2] for row in rows)
    physical_vectors = tuple(
        row.symplectic(fixture.qubits) for row in physical_paulis
    )
    target_vectors = tuple(
        row.symplectic(fixture.matter_qubits) for row in target_paulis
    )

    paired_basis = F.independent_paired_basis(physical_vectors, target_vectors)
    _algebra_radicals, logical_pairs = F.symplectic_split_paired(
        paired_basis, fixture.qubits
    )
    relation_rows = M.relation_certificate(fixture)["relation_rows"]
    _gauge_report, gauge = F.U.gauge_structure(
        fixture, physical_paulis, relation_rows
    )
    gauge_radicals, gauge_pairs = F.symplectic_split_vectors(
        gauge, fixture.qubits
    )
    local_center_by_radius = {
        radius: F.local_center_basis(fixture, gauge, radius)
        for radius in (0, 1, 2)
    }

    matter_parity = Pauli(z=(1 << fixture.matter_qubits) - 1)
    parity_vector = matter_parity.symplectic(fixture.qubits)
    pivots: dict[int, int] = {}
    row = parity_vector
    while row:
        pivot = row.bit_length() - 1
        pivots[pivot] = row
        break
    local_center_rows = []
    for original in local_center_by_radius[2]:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                local_center_rows.append(original)
                break
    local_center = tuple(local_center_rows[: len(gauge_radicals) - 1])
    center = local_center + (parity_vector,)

    logical_count = len(logical_pairs)
    gauge_count = len(gauge_pairs)
    center_count = len(center)
    physical_w = [
        F.canonical_pauli(pair[0][0], fixture.qubits)
        for pair in logical_pairs
    ] + [
        F.canonical_pauli(pair[0], fixture.qubits)
        for pair in gauge_pairs
    ] + [
        F.canonical_pauli(row, fixture.qubits) for row in center
    ]
    physical_v_explicit = [
        F.canonical_pauli(pair[1][0], fixture.qubits)
        for pair in logical_pairs
    ] + [
        F.canonical_pauli(pair[1], fixture.qubits)
        for pair in gauge_pairs
    ]
    physical_v = list(F.B.complete_tableau(
        physical_w, physical_v_explicit, fixture.qubits
    ))

    target_w = [
        F.canonical_pauli(pair[0][1], fixture.matter_qubits)
        for pair in logical_pairs
    ] + [Pauli(z=(1 << fixture.matter_qubits) - 1)]
    target_v_explicit = [
        F.canonical_pauli(pair[1][1], fixture.matter_qubits)
        for pair in logical_pairs
    ]
    target_v = tuple(F.B.complete_tableau(
        target_w, target_v_explicit, fixture.matter_qubits
    ))

    phase_equations = []
    preliminary_coordinates = []
    for physical, target in zip(physical_paulis, target_paulis):
        physical_coordinates = F.B.decode(
            physical, tuple(physical_w), tuple(physical_v), fixture.qubits
        )
        target_coordinates = F.B.decode(
            target, tuple(target_w), target_v, fixture.matter_qubits
        )
        preliminary_coordinates.append((physical_coordinates, target_coordinates))
        delta = (target_coordinates.phase - physical_coordinates.phase) % 4
        mask = (
            (physical_coordinates.v_mask & ((1 << logical_count) - 1))
            | (
                (physical_coordinates.w_mask & ((1 << logical_count) - 1))
                << logical_count
            )
            | (
                (
                    (
                        physical_coordinates.w_mask
                        >> (logical_count + gauge_count)
                    )
                    & ((1 << (center_count - 1)) - 1)
                )
                << (2 * logical_count)
            )
        )
        phase_equations.append((mask, delta // 2))
    phase_solution, _phase_rank, phase_contradictions = F.C.gf2_solve(
        phase_equations
    )
    phase_parity_failures = sum(
        (target.phase - physical.phase) % 2
        for physical, target in preliminary_coordinates
    )
    if phase_parity_failures or phase_contradictions:
        raise AssertionError(
            "Cycle-720 phase solve is inconsistent: "
            f"parity_failures={phase_parity_failures}, "
            f"contradictions={phase_contradictions}"
        )

    for index in range(logical_count):
        if (phase_solution >> index) & 1:
            row = physical_v[index]
            physical_v[index] = Pauli((row.phase + 2) % 4, row.x, row.z)
        if (phase_solution >> (logical_count + index)) & 1:
            row = physical_w[index]
            physical_w[index] = Pauli((row.phase + 2) % 4, row.x, row.z)
    for index in range(center_count - 1):
        if (phase_solution >> (2 * logical_count + index)) & 1:
            position = logical_count + gauge_count + index
            row = physical_w[position]
            physical_w[position] = Pauli((row.phase + 2) % 4, row.x, row.z)

    physical_w_tuple = tuple(physical_w)
    physical_v_tuple = tuple(physical_v)
    target_w_tuple = tuple(target_w)
    coordinates = tuple(
        _dictionary_coordinate(
            index=index,
            family=family,
            physical=physical,
            target=target,
            physical_coordinates=F.B.decode(
                physical,
                physical_w_tuple,
                physical_v_tuple,
                fixture.qubits,
            ),
            target_coordinates=F.B.decode(
                target,
                target_w_tuple,
                target_v,
                fixture.matter_qubits,
            ),
            logical_count=logical_count,
            gauge_count=gauge_count,
            center_count=center_count,
        )
        for index, (family, physical, target) in enumerate(rows)
    )
    digest = _tableau_digest(physical_w_tuple, physical_v_tuple)
    reference = F.phase_fixed_factorization(shape)
    reference_digest = reference["tableau_digest"]
    if digest != reference_digest:
        raise AssertionError(
            "factorization tableau digest mismatch for "
            f"{shape}: reconstructed={digest}, landed={reference_digest}"
        )
    actual_counts = (logical_count, gauge_count, center_count)
    reference_counts = (
        reference["logical_qubits_in_fixed_parity_sector"],
        reference["gauge_qubits"],
        reference["center_sector_bits"],
    )
    if actual_counts != reference_counts:
        raise AssertionError(
            f"factorization counts differ for {shape}: "
            f"reconstructed={actual_counts}, landed={reference_counts}"
        )

    return FactorizationObject(
        shape=shape,
        physical_w=physical_w_tuple,
        physical_v=physical_v_tuple,
        target_w=target_w_tuple,
        target_v=target_v,
        logical_count=logical_count,
        gauge_count=gauge_count,
        center_count=center_count,
        dictionary_coordinates=coordinates,
        tableau_digest=digest,
    )


def _encode(
    phase: int,
    v_mask: int,
    w_mask: int,
    w_rows: tuple[Pauli, ...],
    v_rows: tuple[Pauli, ...],
) -> Pauli:
    output = Pauli(phase=phase)
    for index, row in enumerate(v_rows):
        if (v_mask >> index) & 1:
            output = output @ row
    for index, row in enumerate(w_rows):
        if (w_mask >> index) & 1:
            output = output @ row
    return output


def _signed_equal(left: Pauli, right: Pauli) -> bool:
    return (
        left.phase == right.phase
        and left.x == right.x
        and left.z == right.z
    )


def _coordinate_failures(
    factorization: FactorizationObject,
) -> tuple[int, int]:
    physical_failures = 0
    target_failures = 0
    logical_count = factorization.logical_count
    gauge_count = factorization.gauge_count
    for coordinate in factorization.dictionary_coordinates:
        physical_v_mask = (
            coordinate.logical_v_mask
            | (coordinate.gauge_v_mask << logical_count)
            | (
                coordinate.center_v_mask
                << (logical_count + gauge_count)
            )
        )
        physical_w_mask = (
            coordinate.logical_w_mask
            | (coordinate.gauge_w_mask << logical_count)
            | (
                coordinate.center_w_mask
                << (logical_count + gauge_count)
            )
        )
        replay = _encode(
            coordinate.physical_even_phase,
            physical_v_mask,
            physical_w_mask,
            factorization.physical_w,
            factorization.physical_v,
        )
        physical_failures += not _signed_equal(replay, coordinate.physical_row)

        target_v_mask = (
            coordinate.target_logical_v_mask
            | (coordinate.target_center_v_mask << logical_count)
        )
        target_w_mask = (
            coordinate.target_logical_w_mask
            | (coordinate.target_center_w_mask << logical_count)
        )
        target_replay = _encode(
            coordinate.target_even_phase,
            target_v_mask,
            target_w_mask,
            factorization.target_w,
            factorization.target_v,
        )
        target_failures += not _signed_equal(
            target_replay, coordinate.target_row
        )
    return physical_failures, target_failures


def _contract_failures(
    factorization: FactorizationObject,
    source_rows: tuple[tuple[str, Pauli, Pauli], ...],
) -> dict[str, int]:
    failures = {
        "cross_frame_phase": 0,
        "dictionary_count": abs(
            len(factorization.dictionary_coordinates) - len(source_rows)
        ),
        "gauge_coordinate": 0,
        "logical_coordinate": 0,
        "mask_or_phase_range": 0,
        "parity_coordinate": int(factorization.center_count < 1),
        "phase_formula": 0,
        "source_association": 0,
        "zero_center_dual": 0,
    }
    logical_count = factorization.logical_count
    gauge_count = factorization.gauge_count
    center_count = factorization.center_count
    logical_mask = (1 << logical_count) - 1
    gauge_mask = (1 << gauge_count) - 1
    center_mask = (1 << center_count) - 1
    for index, (coordinate, source) in enumerate(
        zip(factorization.dictionary_coordinates, source_rows)
    ):
        family, physical_row, target_row = source
        failures["source_association"] += (
            coordinate.index != index
            or coordinate.family != family
            or not _signed_equal(coordinate.physical_row, physical_row)
            or not _signed_equal(coordinate.target_row, target_row)
        )
        failures["logical_coordinate"] += (
            coordinate.logical_v_mask != coordinate.target_logical_v_mask
            or coordinate.logical_w_mask != coordinate.target_logical_w_mask
        )
        failures["gauge_coordinate"] += bool(
            coordinate.gauge_v_mask or coordinate.gauge_w_mask
        )
        failures["zero_center_dual"] += bool(
            coordinate.center_v_mask or coordinate.target_center_v_mask
        )
        physical_parity = (
            coordinate.center_w_mask >> max(center_count - 1, 0)
        ) & 1
        target_parity = coordinate.target_center_w_mask
        failures["parity_coordinate"] += physical_parity != target_parity
        failures["phase_formula"] += (
            coordinate.physical_odd_phase
            != (coordinate.physical_even_phase + 2 * physical_parity) % 4
            or coordinate.target_odd_phase
            != (coordinate.target_even_phase + 2 * target_parity) % 4
        )
        failures["cross_frame_phase"] += (
            coordinate.physical_even_phase != coordinate.target_even_phase
            or coordinate.physical_odd_phase != coordinate.target_odd_phase
        )
        failures["mask_or_phase_range"] += (
            coordinate.logical_v_mask & ~logical_mask != 0
            or coordinate.logical_w_mask & ~logical_mask != 0
            or coordinate.gauge_v_mask & ~gauge_mask != 0
            or coordinate.gauge_w_mask & ~gauge_mask != 0
            or coordinate.center_v_mask & ~center_mask != 0
            or coordinate.center_w_mask & ~center_mask != 0
            or coordinate.target_logical_v_mask & ~logical_mask != 0
            or coordinate.target_logical_w_mask & ~logical_mask != 0
            or coordinate.target_center_v_mask not in (0, 1)
            or coordinate.target_center_w_mask not in (0, 1)
            or any(
                phase not in range(4)
                for phase in (
                    coordinate.physical_even_phase,
                    coordinate.physical_odd_phase,
                    coordinate.target_even_phase,
                    coordinate.target_odd_phase,
                )
            )
        )
    return failures


def _deeply_immutable(factorization: FactorizationObject) -> bool:
    targets = (
        (factorization, "logical_count"),
        (factorization.physical_w[0], "phase"),
        (factorization.dictionary_coordinates[0], "index"),
    )
    for target, field in targets:
        try:
            setattr(target, field, getattr(target, field))
        except (AttributeError, FrozenInstanceError):
            continue
        return False
    return True


EXPECTED_FIXTURES = {
    (2, 1, 1): (
        (11, 6, 1),
        76,
        "3cb9e9c14de10b3cab61c029d2f599d320233c82a26fc7d060eab7e5dcf204f3",
    ),
    (3, 1, 1): (
        (17, 9, 1),
        116,
        "6abf5c5f2c4d009b38405c4cad1d6801f925b1c9525cb42e8c41f7a876b6f44f",
    ),
    (2, 2, 1): (
        (23, 11, 2),
        160,
        "9157f2b7bf8230ba3b20fb343d2a50929ded4f20fb6fdbf9350377eab23ca126",
    ),
    (2, 2, 2): (
        (47, 19, 6),
        336,
        "e83b7b242297a8e613073dc1984a17ee07d632708676f4ff786c9bca943fcd0b",
    ),
    (3, 2, 2): (
        (71, 27, 10),
        512,
        "10ec1180a23dd781c406fca7a9a6f0b2d5bf75da74fd1712849904bdc2197a47",
    ),
    (3, 3, 2): (
        (107, 38, 17),
        780,
        "5850eff1c1053f6290f97da45eeefe4b3116bc3adc95fd2a4c269b380b58389b",
    ),
    (5, 3, 2): (
        (179, 60, 31),
        1316,
        "f8558593050632725da0d78cd540a7ebda74fb4c67649428844551181096bec9",
    ),
}


def main() -> None:
    started = perf_counter()
    checks: list[dict[str, object]] = []
    shape_reports = []

    def check(label: str, condition: bool) -> None:
        result = bool(condition)
        checks.append({"label": label, "pass": result})
        print(f"check() {'PASS' if result else 'FAIL'} {label}")

    for shape, expected in EXPECTED_FIXTURES.items():
        shape_started = perf_counter()
        try:
            first = build_factorization_object(shape)
            second = build_factorization_object(shape)
            fixture = M.CompanionFixture.build(shape)
            source_rows = M.operator_rows(fixture)
            physical_failures, target_failures = _coordinate_failures(first)
            contract_failures = _contract_failures(first, source_rows)
            expected_counts, expected_dictionary_rows, expected_digest = expected
            digest_matches = first.tableau_digest == expected_digest
            counts = (
                first.logical_count,
                first.gauge_count,
                first.center_count,
            )
            dimension_matches = (
                sum(counts) == fixture.qubits
                and counts == expected_counts
            )
            dictionary_count_matches = (
                len(first.dictionary_coordinates)
                == len(source_rows)
                == expected_dictionary_rows
            )
            deterministic = first == second
            immutable = _deeply_immutable(first)

            check(f"{shape} digest equals landed Cycle-720 digest", digest_matches)
            check(
                f"{shape} dimensions and counts equal the landed report",
                dimension_matches,
            )
            check(
                f"{shape} dictionary coordinates replay every signed row",
                dictionary_count_matches
                and physical_failures == 0
                and target_failures == 0,
            )
            check(
                f"{shape} source pairing and cross-frame contract are exact",
                dictionary_count_matches
                and all(value == 0 for value in contract_failures.values()),
            )
            check(
                f"{shape} exposed value graph rejects nested field assignment",
                immutable,
            )
            check(
                f"{shape} two independent builds are deeply identical",
                deterministic,
            )
            shape_reports.append({
                "center_count": first.center_count,
                "contract_failures": contract_failures,
                "dictionary_rows": len(first.dictionary_coordinates),
                "digest": first.tableau_digest,
                "expected_dictionary_rows": expected_dictionary_rows,
                "expected_digest": expected_digest,
                "gauge_count": first.gauge_count,
                "logical_count": first.logical_count,
                "physical_coordinate_failures": physical_failures,
                "physical_qubits": fixture.qubits,
                "runtime_sec": round(perf_counter() - shape_started, 6),
                "shape": shape,
                "target_coordinate_failures": target_failures,
            })
        except Exception as error:
            check(f"{shape} factorization object builds cleanly", False)
            shape_reports.append({
                "error": f"{type(error).__name__}: {error}",
                "runtime_sec": round(perf_counter() - shape_started, 6),
                "shape": shape,
            })

    scope = {
        "bounded_local_compiler": "not_constructed",
        "changes_landed_claim": False,
        "derives_new_physics": False,
        "role": "exact finite-box support contract",
    }

    passed = all(item["pass"] for item in checks)
    report = {
        "audit": "unset",
        "authority": "none",
        "checks": checks,
        "claim_ceiling": "exact_support",
        "pass": passed,
        "runtime_sec": round(perf_counter() - started, 6),
        "scope": scope,
        "shapes": shape_reports,
        "status": "PASS" if passed else "FAIL",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
