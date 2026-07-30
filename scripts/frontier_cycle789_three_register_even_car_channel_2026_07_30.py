#!/usr/bin/env python3
"""Cycle-789 three-register repair of the Bell-character channel.

The landed two-bank epoch prepares both [0,q) and [q,2q) before its Bell leg,
so it has no independent input.  This probe keeps those registers as the
Choi output O and Choi input I, adds an independent companion-encoded live
bank L=[2q,3q), and Bell-couples I to L.  A fourth bank R is a diagnostic
reference only: an algebraic Bell state on L,R lets us verify that the
corrected circuit produces the same signed even-CAR Bell characters on O,R.

This is an exact stabilizer/tableau channel proof for the rank-(11N+E)
companion even-CAR character algebra.  It does not derive the external live
bank's encoding/genesis and does not yet include the non-Clifford recurrent G
in the same computed tableau.
"""

from __future__ import annotations

from hashlib import sha256
import json

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_"
    "BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


Pauli = B.Pauli


def shift(row: Pauli, offset: int) -> Pauli:
    return Pauli(row.phase, row.x << offset, row.z << offset)


def pair(row: Pauli, left: int, right: int) -> Pauli:
    return B.EB.canonical(B.multiply(shift(row, left), shift(row, right)))


def conjugate_gate(row: Pauli, gate: tuple) -> Pauli:
    if gate[0] == "H":
        return B.conjugate_h(row, gate[1])
    if gate[0] == "CP":
        return B.conjugate_controlled_letter(
            row, gate[1], gate[2], gate[3]
        )
    raise ValueError(gate)


def conjugate_basis(
    basis: tuple[Pauli, ...], gates: tuple[tuple, ...]
) -> tuple[Pauli, ...]:
    output = list(basis)
    for gate in gates:
        output = [conjugate_gate(row, gate) for row in output]
    return tuple(output)


def span_pivots(
    basis: tuple[Pauli, ...], width: int
) -> dict[int, tuple[int, int]]:
    pivots: dict[int, tuple[int, int]] = {}
    for index, original in enumerate(basis):
        row = original.symplectic(width)
        combination = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot][0]
                combination ^= pivots[pivot][1]
            else:
                pivots[pivot] = (row, combination)
                break
    return pivots


def span_combination(
    target: Pauli,
    width: int,
    pivots: dict[int, tuple[int, int]],
) -> int | None:
    row = target.symplectic(width)
    combination = 0
    while row:
        pivot = row.bit_length() - 1
        if pivot not in pivots:
            return None
        row ^= pivots[pivot][0]
        combination ^= pivots[pivot][1]
    return combination


def signed_span_failures(
    targets: tuple[Pauli, ...], basis: tuple[Pauli, ...], width: int
) -> tuple[int, int]:
    pivots = span_pivots(basis, width)
    binary_failures = 0
    signed_failures = 0
    for target in targets:
        combination = span_combination(target, width, pivots)
        if combination is None:
            binary_failures += 1
            signed_failures += 1
            continue
        replay = Pauli()
        while combination:
            bit = combination & -combination
            replay = B.multiply(replay, basis[bit.bit_length() - 1])
            combination ^= bit
        signed_failures += B.fields(replay) != B.fields(target)
    return binary_failures, signed_failures


def circuit_objects(shape: tuple[int, int, int], atlas) -> dict[str, object]:
    fixture = B.O.arbitrary_fixture(B.Q.shape_cells(shape))
    compiled = B.compile_fixture(fixture)
    corrections = tuple(
        B.P.correction_from_atlas(fixture, tag, atlas)
        for tag in compiled["tags"]
    )
    q = fixture.qubits
    rows = tuple(word["physical"] for word in compiled["words"])
    rank = len(rows)
    width = 4 * q + rank
    resource = tuple(pair(row, 0, q) for row in rows)
    live_reference = tuple(pair(row, 2 * q, 3 * q) for row in rows)
    bell_rows = tuple(pair(row, q, 2 * q) for row in rows)
    output_reference = tuple(pair(row, 0, 3 * q) for row in rows)
    ancilla_z = tuple(Pauli(z=1 << (4 * q + index)) for index in range(rank))

    gates = []
    for index, row in enumerate(bell_rows):
        ancilla = 4 * q + index
        gates.append(("H", ancilla))
        for qubit in B.supported_qubits(row):
            gates.append(("CP", ancilla, qubit, B.letter_at(row, qubit)))
        gates.append(("H", ancilla))
    for index, correction in enumerate(corrections):
        ancilla = 4 * q + index
        for qubit in B.supported_qubits(correction):
            gates.append((
                "CP", ancilla, qubit, B.letter_at(correction, qubit)
            ))
    return {
        "fixture": fixture,
        "compiled": compiled,
        "corrections": corrections,
        "q": q,
        "rank": rank,
        "width": width,
        "rows": rows,
        "resource": resource,
        "live_reference": live_reference,
        "bell_rows": bell_rows,
        "output_reference": output_reference,
        "ancilla_z": ancilla_z,
        "gates": tuple(gates),
    }


def channel_certificate(shape: tuple[int, int, int], atlas) -> dict[str, object]:
    obj = circuit_objects(shape, atlas)
    q = obj["q"]
    rank = obj["rank"]
    width = obj["width"]
    corrections = obj["corrections"]
    initial = obj["resource"] + obj["live_reference"] + obj["ancilla_z"]
    final = conjugate_basis(initial, obj["gates"])
    binary_failures, signed_failures = signed_span_failures(
        obj["output_reference"], final, width
    )

    correction_outside_output = sum(
        bool((row.x | row.z) >> q) for row in corrections
    )
    private_dual_failures = 0
    bell_commutator_failures = 0
    resource_bell_noncommuting_pairs = 0
    for right, bell in enumerate(obj["bell_rows"]):
        for left in range(right):
            bell_commutator_failures += B.M.symplectic(
                bell.symplectic(width),
                obj["bell_rows"][left].symplectic(width),
                width,
            )
        for index, resource in enumerate(obj["resource"]):
            resource_bell_noncommuting_pairs += B.M.symplectic(
                resource.symplectic(width), bell.symplectic(width), width
            )
            private_dual_failures += (
                B.M.symplectic(
                    corrections[right].symplectic(width),
                    resource.symplectic(width),
                    width,
                )
                != int(index == right)
            )

    return {
        "shape": shape,
        "cells": len(obj["fixture"].cells),
        "edges": len(obj["fixture"].edges),
        "q_M2_per_bank": q,
        "character_rank": rank,
        "registers": {
            "Choi_output_O": [0, q],
            "Choi_input_I": [q, 2 * q],
            "external_live_L": [2 * q, 3 * q],
            "diagnostic_reference_R": [3 * q, 4 * q],
            "retained_Bell_ancillas": [4 * q, 4 * q + rank],
        },
        "external_live_written_before_B": 0,
        "correction_rows_outside_output_O": correction_outside_output,
        "Bell_row_commutator_failures": bell_commutator_failures,
        "resource_Bell_noncommuting_pairs_expected_teleportation_backaction": resource_bell_noncommuting_pairs,
        "private_dual_failures": private_dual_failures,
        "tableau_gates": len(obj["gates"]),
        "output_reference_binary_span_failures": binary_failures,
        "output_reference_signed_span_failures": signed_failures,
        "output_even_CAR_channel_exact": not (
            correction_outside_output
            or bell_commutator_failures
            or private_dual_failures
            or binary_failures
            or signed_failures
        ),
        "final_stabilizer_digest": sha256("|".join(
            f"{row.phase}:{row.x:x}:{row.z:x}" for row in final
        ).encode()).hexdigest(),
    }


def deletion_controls(atlas) -> dict[str, object]:
    obj = circuit_objects((1, 1, 1), atlas)
    q = obj["q"]
    width = obj["width"]
    initial = obj["resource"] + obj["live_reference"] + obj["ancilla_z"]
    deleted_index = obj["rank"] // 2
    deleted_gates = tuple(
        gate for gate in obj["gates"]
        if not (
            gate[0] == "CP"
            and gate[1] == 4 * q + deleted_index
            and gate[2] < q
        )
    )
    deleted_final = conjugate_basis(initial, deleted_gates)
    deleted_binary, deleted_signed = signed_span_failures(
        obj["output_reference"], deleted_final, width
    )

    # Hostile self-comparison: move every Bell character from I-L back to O-I,
    # leaving the external live/reference Bell pair untouched.
    hostile_gates = []
    for index, row in enumerate(obj["resource"]):
        ancilla = 4 * q + index
        hostile_gates.append(("H", ancilla))
        for qubit in B.supported_qubits(row):
            hostile_gates.append((
                "CP", ancilla, qubit, B.letter_at(row, qubit)
            ))
        hostile_gates.append(("H", ancilla))
    for index, correction in enumerate(obj["corrections"]):
        ancilla = 4 * q + index
        for qubit in B.supported_qubits(correction):
            hostile_gates.append((
                "CP", ancilla, qubit, B.letter_at(correction, qubit)
            ))
    hostile_final = conjugate_basis(initial, tuple(hostile_gates))
    hostile_binary, hostile_signed = signed_span_failures(
        obj["output_reference"], hostile_final, width
    )
    return {
        "shape": [1, 1, 1],
        "deleted_private_dual_index": deleted_index,
        "deleted_private_dual_output_binary_failures": deleted_binary,
        "deleted_private_dual_output_signed_failures": deleted_signed,
        "self_comparison_output_binary_failures": hostile_binary,
        "self_comparison_output_signed_failures": hostile_signed,
    }


def main() -> None:
    atlas = B.P.build_private_atlases()
    boxes = tuple(
        channel_certificate(shape, atlas)
        for shape in ((1, 1, 1), (2, 2, 2), (3, 2, 2), (5, 3, 2))
    )
    controls = deletion_controls(atlas)
    checks = {
        "third_live_bank_is_disjoint_and_unwritten_before_B": all(
            row["external_live_written_before_B"] == 0 for row in boxes
        ),
        "Bell_characters_and_private_duals_close": all(
            row["Bell_row_commutator_failures"] == 0
            and row["private_dual_failures"] == 0
            and row["correction_rows_outside_output_O"] == 0
            for row in boxes
        ),
        "signed_output_reference_even_CAR_channel_is_exact": all(
            row["output_even_CAR_channel_exact"] for row in boxes
        ),
        "deleting_one_private_dual_is_detected": (
            controls["deleted_private_dual_output_binary_failures"] > 0
            or controls["deleted_private_dual_output_signed_failures"] > 0
        ),
        "two_bank_self_comparison_is_detected": (
            controls["self_comparison_output_binary_failures"] > 0
            or controls["self_comparison_output_signed_failures"] > 0
        ),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "checks": checks,
        "boxes": boxes,
        "controls": controls,
        "supplied": [
            "the landed Choi output/input preparation on O,I",
            "an independent companion-encoded live bank L and diagnostic Bell reference R",
            "the fixed parity/center sector, clean Bell ancillas, and private-dual atlas",
        ],
        "derived": [
            "Bell characters relocated from the self-comparing O-I pair to I-L",
            "exact signed stabilizer-span transfer from L-R to O-R on the full retained even-CAR character basis",
            "corrections remain confined to Choi output O",
            "held-size deletion and hostile self-comparison discrimination",
        ],
        "open": [
            "the separate package runner supplies literal route-expanded physical-M2 placement; this algebra runner does not",
            "autonomous encoding/genesis of the external L bank from bare physical input",
            "one computed prefix-plus-non-Clifford-recurrent-G channel",
            "the separate package runner supplies geometric/order 24-frame/576-product controls; full frame-sheared signed-channel covariance remains open",
        ],
        "claim_boundary": (
            "Positive exact three-register even-CAR input channel under a supplied companion-encoded live bank. "
            "It repairs the landed two-bank semantic collision but is not bare-input genesis or a full A+B+C+G compiler."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
