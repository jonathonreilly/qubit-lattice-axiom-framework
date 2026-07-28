#!/usr/bin/env python3
"""Immutable access to the exact Cycle-720 mixed-gauge factorization.

This module is support infrastructure.  It reconstructs the convention-sensitive
Cycle-720 tableau without changing either landed runner, exposes the finite
operator dictionary in factor coordinates, and refuses to return an object whose
ordered signed-tableau digest differs from the landed factorization certificate.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/FACTORIZATION_OBJECT_API_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
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
    """Decision-D2 immutable signed-tableau factorization object."""

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


def main() -> None:
    started = perf_counter()
    shapes = ((2, 2, 2), (3, 2, 2), (3, 3, 2))
    checks: list[dict[str, object]] = []
    shape_reports = []

    def check(label: str, condition: bool) -> None:
        result = bool(condition)
        checks.append({"label": label, "pass": result})
        print(f"check() {'PASS' if result else 'FAIL'} {label}")

    for shape in shapes:
        shape_started = perf_counter()
        try:
            first = build_factorization_object(shape)
            second = build_factorization_object(shape)
            reference = F.phase_fixed_factorization(shape)
            fixture = M.CompanionFixture.build(shape)
            physical_failures, target_failures = _coordinate_failures(first)
            digest_matches = (
                first.tableau_digest == reference["tableau_digest"]
            )
            counts = (
                first.logical_count,
                first.gauge_count,
                first.center_count,
            )
            reference_counts = (
                reference["logical_qubits_in_fixed_parity_sector"],
                reference["gauge_qubits"],
                reference["center_sector_bits"],
            )
            dimension_matches = (
                sum(counts) == fixture.qubits
                and counts == reference_counts
            )
            dictionary_count_matches = (
                len(first.dictionary_coordinates)
                == len(M.operator_rows(fixture))
            )
            deterministic = (
                first == second
                and all(
                    _signed_equal(left, right)
                    for left, right in zip(
                        first.physical_w + first.physical_v,
                        second.physical_w + second.physical_v,
                    )
                )
            )
            try:
                first.logical_count = first.logical_count
            except FrozenInstanceError:
                immutable = True
            else:
                immutable = False

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
                f"{shape} frozen dataclass rejects field assignment",
                immutable,
            )
            check(
                f"{shape} two independent builds are row-wise identical",
                deterministic,
            )
            shape_reports.append({
                "center_count": first.center_count,
                "dictionary_rows": len(first.dictionary_coordinates),
                "digest": first.tableau_digest,
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
        "changes_landed_claim": False,
        "consumer_V_s_restriction_compiler": "open",
        "derives_new_physics": False,
        "role": "support infrastructure",
    }
    check(
        "scope is support-only: no new physics or landed claim; "
        "the V_s-restriction compiler remains open",
        scope["role"] == "support infrastructure"
        and not scope["derives_new_physics"]
        and not scope["changes_landed_claim"]
        and scope["consumer_V_s_restriction_compiler"] == "open",
    )

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
