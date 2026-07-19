#!/usr/bin/env python3
"""Cycle 439: reversible quadrupole receiver label-to-candidate packets.

Couple the Cycle-435 three-cell one-particle receiver to two pointer M2 with
the exact XOR unitary sum_j P_j tensor XOR(j).  Retain the pointer and source,
then route each coherent fine label into its own Cycle-433-pattern reversible
writer for one independent Cycle-370-compatible 79-M2 candidate packet.

The receiver-projector controlled 120-M2 block, its primitive synthesis, the
three-label writer router, candidate payloads, formation bits, and blanks are
supplied.  Candidate packets are not Records; labels are not outcomes or
occurrences; squared weights are not a Born law.  No readout is selected.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_detector_to_protected_record_formation_compiler_cycle433_2026_07_19 as c433
import physical_quadrupole_packet_width_bridge_cycle435_2026_07_19 as c435


c370 = c433.c370
c364 = c433.c364
c319 = c435.c319
c210 = c435.c210
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_QUADRUPOLE_RECEIVER_CANDIDATE_PACKET_INSTRUMENT_CYCLE439_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOLERANCE = 9e-10
POINTER_M2 = 2
POINTER_DIMENSION = 4
POINTER_VALUES = np.asarray((-1.0, 0.0, 1.0, 0.0))
PASS = 0
FAIL = 0

ReceiverState = dict[int, np.ndarray]
PointerState = dict[int, np.ndarray]
PacketBankSignature = tuple[tuple[int, ...], ...]
CoherentPacketKey = tuple[int, int, PacketBankSignature]
CoherentPacketState = dict[CoherentPacketKey, np.ndarray]
WRITER_TRANSITIONS: dict[
    str, tuple[PacketBankSignature, tuple[PacketBankSignature, ...]]
] = {}


@dataclass(frozen=True)
class InstrumentCase:
    geometry: c435.Geometry
    formation_length: int
    label_cases: tuple[c433.FormationCase, ...]


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
    required = (
        "authority: none",
        "audit: unset",
        "exact self-adjoint xor pointer unitary",
        "three fine position labels",
        "two pointer m2",
        "120-m2 projector-controlled block",
        "primitive synthesis remains supplied",
        "actual cycle-435 train and held evolved packets",
        "both physical strength analogues",
        "pointer weights and compression agree",
        "three independent 79-m2 candidate packets",
        "cycle-433-pattern writer",
        "field-by-field",
        "coherent three-label output",
        "e_439 g_439 = g_physical,439 e_439",
        "exact inverse with pointer and source retained",
        "all 24 proper-cubic frames",
        "held a=2",
        "label, pointer, writer, payload, occupancy, and router deletions",
        "candidate packet is not a record",
        "no outcome, occurrence, born weight, or selected readout",
        "cycle-420 named and numeric flags remain false",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-439 note freezes the reversible candidate-instrument boundary", not missing, missing)


def pointer_label(receiver_index: int) -> int:
    if receiver_index not in range(c435.RECEIVER_DIM):
        raise ValueError("receiver index is outside the one-particle three-cell code")
    return receiver_index // 6


def pointer_xor(
    logical: np.ndarray,
    *,
    deleted_bit: int | None = None,
) -> np.ndarray:
    logical = np.asarray(logical, dtype=complex)
    if logical.shape != (c435.RECEIVER_DIM, POINTER_DIMENSION):
        raise ValueError("pointer unitary requires an 18 by 4 logical array")
    if deleted_bit not in (None, 0, 1):
        raise ValueError("deleted pointer bit must be zero, one, or unset")
    output = np.zeros_like(logical)
    for receiver_index in range(c435.RECEIVER_DIM):
        label = pointer_label(receiver_index)
        if deleted_bit is not None:
            label &= ~(1 << deleted_bit)
        for source_pointer in range(POINTER_DIMENSION):
            output[receiver_index, source_pointer ^ label] += logical[
                receiver_index, source_pointer
            ]
    return output


def pointer_unitary() -> np.ndarray:
    output = np.zeros(
        (c435.RECEIVER_DIM * POINTER_DIMENSION,) * 2, dtype=complex
    )
    for source in range(output.shape[1]):
        receiver_index, pointer = divmod(source, POINTER_DIMENSION)
        target = POINTER_DIMENSION * receiver_index + (pointer ^ pointer_label(receiver_index))
        output[target, source] = 1
    return output


def pointer_state(state: ReceiverState) -> PointerState:
    output = {}
    for key, value in state.items():
        extended = np.zeros(
            (c435.SOURCE_DIM, c435.RECEIVER_DIM, POINTER_DIMENSION),
            dtype=complex,
        )
        extended[:, :, 0] = value
        output[key] = extended
    return output


def apply_pointer(
    state: PointerState,
    *,
    deleted_bit: int | None = None,
) -> PointerState:
    output = {}
    for key, value in state.items():
        transformed = np.empty_like(value)
        for source_index in range(c435.SOURCE_DIM):
            transformed[source_index] = pointer_xor(
                value[source_index], deleted_bit=deleted_bit
            )
        output[key] = transformed
    return output


def pointer_state_residual(left: PointerState, right: PointerState) -> float:
    zero = np.zeros(
        (c435.SOURCE_DIM, c435.RECEIVER_DIM, POINTER_DIMENSION), dtype=complex
    )
    return float(
        np.sqrt(
            sum(
                np.vdot(
                    left.get(key, zero) - right.get(key, zero),
                    left.get(key, zero) - right.get(key, zero),
                ).real
                for key in left.keys() | right.keys()
            )
        )
    )


def pointer_weights(state: PointerState) -> np.ndarray:
    weights = np.zeros(POINTER_DIMENSION, dtype=float)
    for value in state.values():
        for label in range(POINTER_DIMENSION):
            weights[label] += float(np.vdot(value[:, :, label], value[:, :, label]).real)
    return weights


def pointer_moments(weights: np.ndarray) -> dict[str, float]:
    total = float(np.sum(weights))
    centroid = float(weights @ POINTER_VALUES / total)
    second = float(weights @ (POINTER_VALUES**2) / total)
    return {
        "total": total,
        "centroid": centroid,
        "second_moment": second,
        "width": float(np.sqrt(max(0, second - centroid**2))),
    }


def evolved_state(geometry: c435.Geometry, occupation: float) -> ReceiverState:
    if not 0 <= occupation <= 1:
        raise ValueError("Q1 occupation must be in [0,1]")
    vacuum = c435.evolve(c435.vacuum_state(), geometry)
    quadrupole = c435.evolve(c435.quadrupole_state(geometry), geometry)
    return c435.combine(
        (vacuum, quadrupole),
        np.asarray((np.sqrt(1 - occupation), np.sqrt(occupation))),
    )


def instrument_case(geometry: c435.Geometry) -> InstrumentCase:
    if geometry.held:
        length = 6
        targets = tuple((17, -12 + label, 5) for label in range(3))
    else:
        length = 3
        targets = tuple((5, -1 + label, 0) for label in range(3))
    cases = tuple(
        c433.make_case(
            length,
            target,
            (target[0] - 1, target[1], target[2]),
            held=geometry.held,
        )
        for target in targets
    )
    return InstrumentCase(geometry, length, cases)


CASES = tuple(instrument_case(geometry) for geometry in c435.GEOMETRIES)


def pointer_operator_controls() -> None:
    print("\nREVERSIBLE TWO-M2 THREE-LABEL POINTER")
    unitary = pointer_unitary()
    identity = np.eye(unitary.shape[0], dtype=complex)
    blank = np.zeros((c435.RECEIVER_DIM, POINTER_DIMENSION), dtype=complex)
    for receiver_index in range(c435.RECEIVER_DIM):
        blank[receiver_index, 0] = 1 / np.sqrt(c435.RECEIVER_DIM)
    labeled = pointer_xor(blank)
    restored = pointer_xor(labeled)
    label_weights = np.sum(abs(labeled) ** 2, axis=0)
    receiver_diagonal_before = np.sum(abs(blank) ** 2, axis=1)
    receiver_diagonal_after = np.sum(abs(labeled) ** 2, axis=1)
    receiver_mass_residual = float(
        np.linalg.norm(receiver_diagonal_after - receiver_diagonal_before)
    )
    check(
        "the exact self-adjoint XOR pointer unitary reversibly couples three position labels into two pointer M2",
        np.linalg.norm(unitary.conj().T @ unitary - identity) == 0
        and np.linalg.norm(unitary - unitary.conj().T) == 0
        and np.linalg.norm(restored - blank) == 0
        and receiver_mass_residual == 0
        and np.linalg.norm(label_weights - np.asarray((1, 1, 1, 0)) / 3) < TOLERANCE,
        {
            "logical_receiver_dimension": c435.RECEIVER_DIM,
            "pointer_dimension": POINTER_DIMENSION,
            "pointer_M2": POINTER_M2,
            "unitarity_residual": float(np.linalg.norm(unitary.conj().T @ unitary - identity)),
            "self_adjoint_residual": float(np.linalg.norm(unitary - unitary.conj().T)),
            "inverse_residual": float(np.linalg.norm(restored - blank)),
            "one_particle_receiver_mass_residual": receiver_mass_residual,
            "one_particle_receiver_number_before_after": (
                float(np.sum(receiver_diagonal_before)),
                float(np.sum(receiver_diagonal_after)),
            ),
            "unused_pointer_label_weight": label_weights[3],
            "projector_controlled_block_supplied": True,
            "primitive_synthesis_constructed": False,
            "bounded_physical_support_M2": 120,
        },
    )


def physical_pointer_apply(matrix: np.ndarray, encoding) -> np.ndarray:
    if matrix.shape != (encoding.shape[0], POINTER_DIMENSION):
        raise ValueError("physical receiver-pointer matrix has the wrong shape")
    decoded = encoding.getH() @ matrix
    transformed = pointer_xor(decoded)
    return matrix + encoding @ (transformed - decoded)


def pointer_physical_compiler_controls() -> dict:
    print("\nPHYSICAL POINTER E/G / INVERSE / LEAKAGE")
    rng = np.random.default_rng(43901)
    rows = []
    encodings = {}
    for item in CASES:
        geometry = item.geometry
        all_encodings, _reducer, support = c435.c432.build_shell(
            geometry.length, geometry.receivers
        )
        encoding = all_encodings[c319.ORDER_INDEX[(0, 1, 2)]][
            :, c435.RECEIVER_INDICES
        ]
        encodings[geometry.name] = encoding
        gram = c319.c315.raw_maximum_abs(
            encoding.getH() @ encoding - sparse.eye(c435.RECEIVER_DIM, format="csc")
        )
        logical = rng.normal(size=(c435.RECEIVER_DIM, POINTER_DIMENSION)) + 1j * rng.normal(
            size=(c435.RECEIVER_DIM, POINTER_DIMENSION)
        )
        logical /= np.linalg.norm(logical)
        encoded = encoding @ logical
        physical = physical_pointer_apply(encoded, encoding)
        expected = encoding @ pointer_xor(logical)
        restored = physical_pointer_apply(physical, encoding)
        decoded = encoding.getH() @ physical
        code_projection = encoding @ decoded
        rows.append(
            {
                "geometry": geometry.name,
                "held": geometry.held,
                "encoding_shape": encoding.shape,
                "Gram_raw_maximum": gram,
                "EG_residual": float(np.linalg.norm(physical - expected)),
                "inverse_residual": float(np.linalg.norm(restored - encoded)),
                "code_leakage": float(np.linalg.norm(physical - code_projection)),
                "receiver_support_M2": support["face_port_cell_role_union_M2"],
                "pointer_M2": POINTER_M2,
                "joint_support_M2": support["face_port_cell_role_union_M2"] + POINTER_M2,
            }
        )
    check(
        "E_439 G_439 = G_physical,439 E_439 and the exact pointer inverse close on train and held receiver codes",
        max(
            max(
                row["Gram_raw_maximum"],
                row["EG_residual"],
                row["inverse_residual"],
                row["code_leakage"],
            )
            for row in rows
        )
        < TOLERANCE,
        {
            "rows": rows,
            "physical_completion": "identity outside the encoded receiver image",
            "projector_controlled_block_and_primitive_synthesis": "supplied",
        },
    )
    return {"rows": rows, "encodings": encodings}


def actual_evolved_instrument_controls() -> dict:
    print("\nACTUAL CYCLE-435 TRAIN/HELD PACKET COMPOSITION")
    rows = []
    states = {}
    for item in CASES:
        geometry = item.geometry
        for strength, occupation in c435.PHYSICAL_STRENGTHS.items():
            evolved = evolved_state(geometry, occupation)
            prepared = pointer_state(evolved)
            coupled = apply_pointer(prepared)
            restored = apply_pointer(coupled)
            receiver_weights = c435.packet_weights(evolved)
            fine_weights = pointer_weights(coupled)
            receiver_moments = c435.packet_moments(receiver_weights)
            fine_moments = pointer_moments(fine_weights)
            row = {
                "geometry": geometry.name,
                "held": geometry.held,
                "separation": geometry.separation,
                "strength": strength,
                "Q1_occupation": occupation,
                "receiver_weights": receiver_weights,
                "pointer_weights": fine_weights,
                "weight_residual": float(
                    np.linalg.norm(fine_weights[:3] - receiver_weights)
                ),
                "unused_label_weight": fine_weights[3],
                "receiver_moments": receiver_moments,
                "pointer_moments": fine_moments,
                "compression_residual": max(
                    abs(receiver_moments[key] - fine_moments[key])
                    for key in ("centroid", "second_moment", "width")
                ),
                "inverse_residual": pointer_state_residual(restored, prepared),
            }
            rows.append(row)
            states[(geometry.name, strength)] = coupled
    check(
        "the actual Cycle-435 train and held a=2 packets at both strengths compose with exact pointer weights, moments, and inverse",
        len(rows) == 4
        and sum(row["held"] for row in rows) == 2
        and max(
            max(
                row["weight_residual"],
                row["unused_label_weight"],
                row["compression_residual"],
                row["inverse_residual"],
            )
            for row in rows
        )
        < TOLERANCE,
        {"rows": rows, "source_and_pointer_retained": True, "selected_label": None},
    )
    return {"rows": rows, "states": states}


def target_word(state: c433.BasisState) -> tuple[int, ...]:
    return c433.selected(state.bits, state.layout.target)


def writer_registers(item: InstrumentCase, label: int) -> tuple[c433.BasisState, ...]:
    if label not in range(POINTER_DIMENSION):
        raise ValueError("fine pointer label must be in 0..3")
    registers = []
    for candidate_label, case in enumerate(item.label_cases):
        source = c433.prepare(c433.LAYOUT, case)
        registers.append(
            c433.apply_coupled(source, int(label == candidate_label))
        )
    return tuple(registers)


def writer_transition_table(
    item: InstrumentCase,
) -> tuple[PacketBankSignature, tuple[PacketBankSignature, ...]]:
    """Return the actual prepared and controlled-writer basis signatures.

    The signatures contain every M2 in each of the three independent writer
    patches, not merely the 79 target lanes.  They therefore retain the
    supplied proposal, predecessor, formation, certificate, and workspace
    bits needed by the Cycle-433-pattern action.
    """
    cached = WRITER_TRANSITIONS.get(item.geometry.name)
    if cached is not None:
        return cached
    prepared = tuple(
        tuple(c433.prepare(c433.LAYOUT, case).bits) for case in item.label_cases
    )
    outputs = tuple(
        tuple(tuple(register.bits) for register in writer_registers(item, label))
        for label in range(POINTER_DIMENSION)
    )
    WRITER_TRANSITIONS[item.geometry.name] = (prepared, outputs)
    return prepared, outputs


def coherent_packet_input(
    item: InstrumentCase,
    state: PointerState,
) -> CoherentPacketState:
    """Factorwise-exact sparse state before the controlled writer.

    Each nonzero block is keyed by the physical field sector, pointer label,
    and complete three-bank M2 signature.  The retained dense block axes are
    the 216 source labels and 18 receiver labels; this avoids enumerating
    millions of scalar entries without tracing out either factor.
    """
    prepared, _outputs = writer_transition_table(item)
    output: CoherentPacketState = {}
    for field_sector, value in state.items():
        for pointer_label_value in range(POINTER_DIMENSION):
            block = value[:, :, pointer_label_value]
            if np.any(block):
                output[(field_sector, pointer_label_value, prepared)] = block.copy()
    return output


def apply_coherent_writers(
    item: InstrumentCase,
    state: CoherentPacketState,
    *,
    reverse: bool = False,
) -> CoherentPacketState:
    """Apply the three actual basis-writer permutations block-linearly."""
    prepared, outputs = writer_transition_table(item)
    transformed: CoherentPacketState = {}
    for (field_sector, pointer_label_value, banks), amplitude in state.items():
        expected = outputs[pointer_label_value] if reverse else prepared
        if banks != expected:
            raise ValueError("coherent writer input is outside its declared basis domain")
        target = prepared if reverse else outputs[pointer_label_value]
        key = (field_sector, pointer_label_value, target)
        if key in transformed:
            transformed[key] = transformed[key] + amplitude
        else:
            transformed[key] = amplitude.copy()
    return transformed


def coherent_state_residual(
    left: CoherentPacketState,
    right: CoherentPacketState,
) -> float:
    residual = 0.0
    zero = np.zeros((c435.SOURCE_DIM, c435.RECEIVER_DIM), dtype=complex)
    for key in left.keys() | right.keys():
        difference = left.get(key, zero) - right.get(key, zero)
        residual += float(np.vdot(difference, difference).real)
    return float(np.sqrt(residual))


def coherent_pointer_weights(state: CoherentPacketState) -> np.ndarray:
    weights = np.zeros(POINTER_DIMENSION, dtype=float)
    for (_field_sector, pointer_label_value, _banks), amplitude in state.items():
        weights[pointer_label_value] += float(np.vdot(amplitude, amplitude).real)
    return weights


def coherent_candidate_weights(state: CoherentPacketState) -> np.ndarray:
    weights = np.zeros(3, dtype=float)
    for (_field_sector, _pointer_label_value, banks), amplitude in state.items():
        sector_weight = float(np.vdot(amplitude, amplitude).real)
        for candidate_label, bank in enumerate(banks):
            if any(c433.selected(bank, c433.LAYOUT.target)):
                weights[candidate_label] += sector_weight
    return weights


def inverse_writer_registers(
    item: InstrumentCase,
    label: int,
    registers: tuple[c433.BasisState, ...],
) -> tuple[c433.BasisState, ...]:
    if len(registers) != 3:
        raise ValueError("three independent writer registers are required")
    return tuple(
        c433.apply_coupled(
            register,
            int(label == candidate_label),
            reverse=True,
        )
        for candidate_label, register in enumerate(registers)
    )


def writer_controls() -> dict:
    print("\nTHREE INDEPENDENT CYCLE-433-PATTERN 79-M2 WRITERS")
    rows = []
    register_maps = {}
    for item in CASES:
        blank = tuple(
            c433.prepare(c433.LAYOUT, case) for case in item.label_cases
        )
        for label in range(POINTER_DIMENSION):
            output = writer_registers(item, label)
            restored = inverse_writer_registers(item, label, output)
            occupied = []
            decoded = []
            lane_residuals = []
            leakage = []
            for candidate_label, (case, register) in enumerate(
                zip(item.label_cases, output)
            ):
                word = target_word(register)
                expected_word = (
                    c370.encode_replica(case.fixture, c433.expected_replica(case))
                    if label == candidate_label
                    else (0,) * c370.CARRIER_BITS
                )
                occupied.append(int(any(word)))
                lane_residuals.append(sum(left != right for left, right in zip(word, expected_word)))
                decoded.append(c370.decode_replica(case.fixture, word))
                leakage.append(c433.workspace_leakage(register))
            rows.append(
                {
                    "geometry": item.geometry.name,
                    "held": item.geometry.held,
                    "pointer_label": label,
                    "occupied_candidate_packets": tuple(occupied),
                    "field_lane_residuals": tuple(lane_residuals),
                    "workspace_leakage": tuple(leakage),
                    "inverse_exact": restored == blank,
                    "decoded_targets": tuple(
                        None if replica is None else replica.record.site
                        for replica in decoded
                    ),
                }
            )
            register_maps[(item.geometry.name, label)] = output
    check(
        "each fine position label coherently routes field-by-field into one independent Cycle-370-compatible 79-M2 candidate packet with exact inverse",
        len(rows) == 8
        and all(
            row["occupied_candidate_packets"]
            == (
                tuple(int(index == row["pointer_label"]) for index in range(3))
                if row["pointer_label"] < 3
                else (0, 0, 0)
            )
            and max(row["field_lane_residuals"]) == 0
            and max(row["workspace_leakage"]) == 0
            and row["inverse_exact"]
            for row in rows
        ),
        {
            "rows": rows,
            "writer_type": "Cycle433-pattern writer; actual detector/predicate interface absent",
            "candidate_packet_M2_each": c370.CARRIER_BITS,
            "independent_candidate_packets": 3,
            "selected_label": None,
        },
    )
    return {"rows": rows, "register_maps": register_maps}


def coherent_packet_weight_controls(actual_data, writer_data) -> None:
    print("\nCOHERENT LABEL / CANDIDATE-PACKET WEIGHT AGREEMENT")
    rows = []
    for row in actual_data["rows"]:
        key = (row["geometry"], row["strength"])
        item = next(case for case in CASES if case.geometry.name == row["geometry"])
        pointer_state_value = actual_data["states"][key]
        prepared = coherent_packet_input(item, pointer_state_value)
        output = apply_coherent_writers(item, prepared)
        restored = apply_coherent_writers(item, output, reverse=True)
        input_pointer_weights = coherent_pointer_weights(prepared)
        output_pointer_weights = coherent_pointer_weights(output)
        candidate_weights = coherent_candidate_weights(output)
        rows.append(
            {
                "geometry": row["geometry"],
                "held": row["held"],
                "strength": row["strength"],
                "factorwise_sparse_input_blocks": len(prepared),
                "factorwise_sparse_output_blocks": len(output),
                "pointer_weights": input_pointer_weights,
                "output_pointer_weights": output_pointer_weights,
                "candidate_packet_weights": candidate_weights,
                "pointer_retention_residual": float(
                    np.linalg.norm(output_pointer_weights - input_pointer_weights)
                ),
                "weight_residual": float(
                    np.linalg.norm(candidate_weights - input_pointer_weights[:3])
                ),
                "inverse_residual": coherent_state_residual(restored, prepared),
                "coherent_labels_retained": tuple(
                    label
                    for label, weight in enumerate(input_pointer_weights[:3])
                    if weight > 1e-12
                ),
            }
        )
    check(
        "the coherent three-label output carries each pointer weight into its matching independent candidate-packet sector without selection",
        len(writer_data["rows"]) == 8
        and max(
            max(
                row["pointer_retention_residual"],
                row["weight_residual"],
                row["inverse_residual"],
            )
            for row in rows
        )
        < TOLERANCE
        and all(row["coherent_labels_retained"] == (0, 1, 2) for row in rows),
        {
            "rows": rows,
            "state_representation": "exact block-sparse amplitudes keyed by field sector, pointer label, and all three complete 468-M2 writer-bank signatures; source and receiver labels retained as block axes",
            "candidate_weights_reduced_from_composed_output": True,
            "pointer_or_packet_weight_called_outcome_occurrence_or_Born_weight": False,
            "source_receiver_pointer_retained": True,
            "candidate_packet_is_Record": False,
        },
    )


def rotated_case(
    case: c433.FormationCase,
    frame: np.ndarray,
    fixture: object,
    mapping: dict,
) -> c433.FormationCase:
    return c433.FormationCase(
        case.length,
        fixture,
        c433.rotated_coord(case.target, frame),
        c433.rotated_coord(case.predecessor, frame),
        c364.rotate_payload(case.payload, mapping),
        c364.rotate_payload(case.prior_payload, mapping),
        case.held,
    )


def covariance_controls() -> None:
    print("\nALL-24 POSITION / POINTER / PAYLOAD COVARIANCE")
    unitary = pointer_unitary()
    pointer_rows = []
    writer_failures = inverse_failures = support_failures = 0
    frame_cases = 0
    for frame in c210.proper_cubic_frames():
        representation = np.zeros(
            (c435.RECEIVER_DIM, c435.RECEIVER_DIM), dtype=complex
        )
        for source in range(c435.RECEIVER_DIM):
            cell, direction = divmod(source, 6)
            target = 6 * cell + c319.c311.direction_map(frame, direction)
            representation[target, source] = 1
        joint_representation = np.kron(representation, np.eye(POINTER_DIMENSION))
        pointer_rows.append(
            float(
                np.linalg.norm(
                    joint_representation @ unitary
                    - unitary @ joint_representation
                )
            )
        )
        framed_layout = c433.rotated_layout(c433.LAYOUT, frame)
        try:
            c433.validate_layout(framed_layout)
        except ValueError:
            support_failures += 1
        for item in CASES:
            fixture, mapping, failures = c364.c342.mapped_fixture(
                item.label_cases[0].fixture, frame
            )
            if failures:
                raise RuntimeError("Cycle342 payload frame map failed")
            for label, case in enumerate(item.label_cases):
                moved = rotated_case(case, frame, fixture, mapping)
                source = c433.prepare(framed_layout, moved)
                output = c433.apply_coupled(source, 1)
                writer_failures += int(
                    c433.target_replica(output, moved.fixture)
                    != c433.expected_replica(moved)
                )
                inverse_failures += int(
                    c433.apply_coupled(output, 1, reverse=True) != source
                )
                frame_cases += 1
    check(
        "receiver position labels, XOR pointer, and all three field-by-field candidate payloads form an all-24 proper-cubic family through held a=2",
        len(pointer_rows) == 24
        and max(pointer_rows) < TOLERANCE
        and frame_cases == 24 * 2 * 3
        and writer_failures == inverse_failures == support_failures == 0,
        {
            "proper_cubic_frames": len(pointer_rows),
            "maximum_pointer_frame_residual": max(pointer_rows),
            "train_held_label_frame_cases": frame_cases,
            "writer_payload_failures": writer_failures,
            "writer_inverse_failures": inverse_failures,
            "rotated_support_failures": support_failures,
        },
    )


def deletions_and_domains(actual_data) -> None:
    print("\nLABEL / POINTER / WRITER / PAYLOAD / OCCUPANCY / ROUTER DELETIONS")
    item = CASES[0]
    state = actual_data["states"][(item.geometry.name, "coefficient_two_analogue")]
    expected_weights = pointer_weights(state)
    uncoupled = pointer_state(
        evolved_state(
            item.geometry,
            c435.PHYSICAL_STRENGTHS["coefficient_two_analogue"],
        )
    )
    uncoupled_weights = pointer_weights(uncoupled)
    deleted_bit_state = apply_pointer(
        pointer_state(
            evolved_state(
                item.geometry,
                c435.PHYSICAL_STRENGTHS["coefficient_two_analogue"],
            )
        ),
        deleted_bit=1,
    )
    deleted_bit_weights = pointer_weights(deleted_bit_state)

    label = 1
    case = item.label_cases[label]
    source = c433.prepare(c433.LAYOUT, case)
    nominal = c433.apply_coupled(source, 1)
    router_deleted = c433.apply_coupled(source, 0)
    desired = c370.encode_replica(case.fixture, c433.expected_replica(case))
    payload_lane = next(
        lane for lane in range(3, 76) if desired[lane] and c433.LAYOUT.source_for_target[lane] is not None
    )
    payload_layers, payload_removed = c433.without_gate(
        c433.LAYOUT.layers, f"field-write:lane{payload_lane}"
    )
    payload_deleted = c433.apply_coupled(source, 1, layers=payload_layers)
    occupancy_layers, occupancy_removed = c433.without_gate(
        c433.LAYOUT.layers, "constant-write:lane0"
    )
    occupancy_deleted = c433.apply_coupled(source, 1, layers=occupancy_layers)
    occupancy_rejected = False
    try:
        c370.decode_replica(case.fixture, target_word(occupancy_deleted))
    except ValueError:
        occupancy_rejected = True
    label_writer_deleted = writer_registers(item, 3)[label]

    rejected = 0
    for function in (
        lambda: pointer_label(18),
        lambda: pointer_xor(np.zeros((18, 3))),
        lambda: pointer_xor(np.zeros((18, 4)), deleted_bit=2),
        lambda: evolved_state(item.geometry, -0.1),
        lambda: writer_registers(item, 4),
        lambda: inverse_writer_registers(item, 0, (source, source)),
    ):
        try:
            function()
        except ValueError:
            rejected += 1

    check(
        "pointer coupling/bit, label writer, router, payload lane, and protected occupancy deletions are independently visible",
        np.linalg.norm(uncoupled_weights - expected_weights) > 1e-4
        and np.linalg.norm(deleted_bit_weights - expected_weights) > 1e-4
        and any(target_word(nominal))
        and not any(target_word(router_deleted))
        and not any(target_word(label_writer_deleted))
        and payload_removed == occupancy_removed == 1
        and target_word(payload_deleted) != desired
        and occupancy_rejected,
        {
            "nominal_pointer_weights": expected_weights,
            "pointer_coupling_deleted_weights": uncoupled_weights,
            "pointer_high_bit_deleted_weights": deleted_bit_weights,
            "router_deleted_target_blank": not any(target_word(router_deleted)),
            "label_writer_deleted_target_blank": not any(target_word(label_writer_deleted)),
            "payload_gate_removed": payload_removed,
            "payload_deleted_lane_mismatch": sum(
                left != right for left, right in zip(target_word(payload_deleted), desired)
            ),
            "occupancy_gate_removed": occupancy_removed,
            "occupancy_deleted_packet_rejected": occupancy_rejected,
        },
    )
    check(
        "lawful-domain controls reject malformed pointer, strength, and writer inputs",
        rejected == 6,
        {"domain_rejections": rejected, "expected": 6},
    )


def resource_and_boundary_controls(pointer_compiler) -> None:
    print("\nRESOURCE / SUPPLIED-STRUCTURE / CYCLE-420 BOUNDARY")
    layout_gates = sum(len(layer.gates) for layer in c433.LAYOUT.layers)
    maximum_receiver = max(
        row["receiver_support_M2"] for row in pointer_compiler["rows"]
    )
    inventory = {
        "supplied": (
            "Cycle435 receiver encodings, evolved source/receiver packet states, and fixed physical strength analogues",
            "receiver position projectors and their 120-M2 projector-controlled XOR block",
            "primitive synthesis of the projector-controlled block and three-label writer multiplexor remains supplied and unconstructed",
            "three Cycle433-pattern layouts, blank 79-M2 targets, proposal fields, protected predecessors, formation/certificate bits, payloads, and router controls",
            "identity completion outside the physical receiver code image",
        ),
        "derived": (
            "exact reversible two-M2 fine-position pointer coupling on train and held physical receiver codes",
            "actual Cycle435 packet composition at both strengths with pointer weight/moment agreement",
            "coherent fine-label routing into three independent Cycle370-compatible candidate packets",
            "exact inverse with source/pointer retained, all-frame covariance, deletion, leakage, domain, and resource controls",
        ),
        "open": (
            "primitive local synthesis of the 120-M2 receiver-projector block and autonomous router/formation-bit genesis",
            "actual Cycle424 detector/predicate interface for these position labels",
            "candidate admission, occurrence, actual history, Record formation, and autonomous protected-capacity renewal",
            "Cycle420 legacy packet/readout/numeric join, Born law, force, energy/stress/source selection, metric, and gravity",
        ),
        "candidate_packet_is_Record": False,
        "pointer_label_is_outcome_or_occurrence": False,
        "squared_weight_is_Born_weight": False,
        "centroid_ensemble_selected": False,
        "force_or_gravity_claim": False,
        "Cycle420_named_readout_selected": False,
        "Cycle420_numeric_rows_reproduced": False,
        "negative_or_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the receiver pointer plus three independent writer patches retain bounded support with every supplied block inventoried",
        maximum_receiver == 118
        and c370.CARRIER_BITS == 79
        and len(c433.LAYOUT.sites) == 468
        and layout_gates == 1026,
        {
            "receiver_matter_support_M2": maximum_receiver,
            "pointer_M2": POINTER_M2,
            "supplied_projector_block_support_M2": maximum_receiver + POINTER_M2,
            "independent_writer_patches": 3,
            "writer_added_M2_each": len(c433.LAYOUT.sites),
            "writer_M2_total": 3 * len(c433.LAYOUT.sites),
            "candidate_packet_M2_each": c370.CARRIER_BITS,
            "writer_layers_each": len(c433.LAYOUT.layers),
            "writer_gates_each_excluding_pointer_router": layout_gates,
            "maximum_writer_primitive_support_M2": 3,
            "bounded_total_installed_M2": maximum_receiver + POINTER_M2 + 3 * len(c433.LAYOUT.sites),
            "bounded_added_M2_beyond_existing_receiver": POINTER_M2 + 3 * len(c433.LAYOUT.sites),
        },
    )
    check(
        "the supplied/derived/open inventory keeps candidate packets, labels, weights, and Cycle-420 readout semantics unselected",
        not inventory["candidate_packet_is_Record"]
        and not inventory["pointer_label_is_outcome_or_occurrence"]
        and not inventory["squared_weight_is_Born_weight"]
        and not inventory["centroid_ensemble_selected"]
        and not inventory["force_or_gravity_claim"]
        and not inventory["Cycle420_named_readout_selected"]
        and not inventory["Cycle420_numeric_rows_reproduced"]
        and not inventory["negative_or_no_go_claim"]
        and not inventory["minimum_content_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 439: QUADRUPOLE RECEIVER LABEL INSTRUMENT TO CANDIDATE PACKETS")
    print("authority=none; audit=unset")
    note_contract()
    pointer_operator_controls()
    pointer_compiler = pointer_physical_compiler_controls()
    actual_data = actual_evolved_instrument_controls()
    writer_data = writer_controls()
    coherent_packet_weight_controls(actual_data, writer_data)
    covariance_controls()
    deletions_and_domains(actual_data)
    resource_and_boundary_controls(pointer_compiler)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_QUADRUPOLE_RECEIVER_CANDIDATE_PACKET_INSTRUMENT_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_QUADRUPOLE_RECEIVER_CANDIDATE_PACKET_INSTRUMENT_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
