#!/usr/bin/env python3
"""Cycle 323: fixed bounded physical program carrier and two-use quotient.

Six Cycle-321 apparatus programs are stored as orthogonal states of three
program M2.  One fixed controlled isometry acts coherently on that register,
one fresh three-M2 pointer, and the accepted two-ray physical matter code.
The same isometry is then composed twice without a program-label dispatch.

All equivalence claims use operators, CP maps, Choi matrices, and physical
intertwiners.  No numerical outcome grade or occurrence premise is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import inspect
import re
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_effect_equivalence_normalized_grade_cycle321_2026_07_18 as c321


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FIXED_PROGRAM_CARRIER_TWO_USE_CYCLE323_NOTE_2026-07-18.md"
)
TOL = 8.0e-11
FRESH_MAIN = "2bf604afc30e626428ec86ea082bc96c46b84ab6"
PASS = 0
FAIL = 0

I2 = c321.I2
PROGRAM_M2 = 3
PROGRAM_DIMENSION = 2**PROGRAM_M2
LAWFUL_PROGRAMS = 6
POINTER_M2 = 3
POINTER_DIMENSION = 2**POINTER_M2

N1_ROUTES = (
    "fixed six-state controlled carrier",
    "coherent program-superposition route",
    "two-use coarse-CP refinement route",
    "two-use effect-only axis route",
    "control-block and blank deletion route",
    "coefficient-bearing physical program route",
    "fresh-pointer reuse and recurrence route",
    "occurrence/Record and global-history route",
)
WALLS = (
    "W_program",
    "W_blank",
    "W_coeff",
    "W_quotient",
    "W_occ_record",
    "W_global",
)
TRIGGER_PARTS = (
    ("we", " assume"),
    ("by", " construction"),
    ("as is", " standard"),
    ("the framework", " provides"),
    ("bridge", " context"),
    ("back", "ground"),
    ("natur", "ally"),
    ("obvious", "ly"),
    ("standard", " qft"),
    ("regis", "tered"),
    ("canon", "ical"),
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-323 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "fixed bounded physical program-carrier tournament",
        "same six cycle-321 apparatus programs",
        "three program m2",
        "one fixed controlled isometry",
        "no host program branch query",
        "coherent program superposition",
        "two-use composition",
        "coarse-cp refinement quotient",
        "axis pair remains process-distinguishable",
        "held l=6",
        "all 24 proper-cubic frames",
        "actual cycle-230 contact",
        "program-state preparation remains supplied",
        "coefficients remain supplied",
        "blank pointer remains supplied",
        "program control is not law-selection derivation",
        "pointer output is not occurrence",
        "supplied program-carrier inventory",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "broad gate status: fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the fixed carrier, two-use quotient, supplied boundaries, and N1-N8 gate",
        not missing,
        missing,
    )


def padded_kraus(program: c321.Program) -> tuple[np.ndarray, ...]:
    return program.kraus + tuple(
        np.zeros((2, 2), dtype=complex)
        for _ in range(POINTER_DIMENSION - len(program.kraus))
    )


def make_programs(contact: np.ndarray) -> tuple[c321.Program, ...]:
    axis_left, axis_right, _ = c321.axis_programs(contact)
    ray_unsplit, ray_refined, _ = c321.ray_programs(contact)
    trine, coin = c321.auxiliary_programs(contact)
    return axis_left, axis_right, ray_unsplit, ray_refined, trine, coin


@dataclass(frozen=True)
class FixedProgramCarrier:
    programs: tuple[c321.Program, ...]

    def __post_init__(self) -> None:
        if len(self.programs) != LAWFUL_PROGRAMS:
            raise ValueError("the declared program code has exactly six programs")
        if len({program.name for program in self.programs}) != LAWFUL_PROGRAMS:
            raise ValueError("lawful program labels have distinct names")
        if any(
            np.linalg.norm(program.completeness - I2) >= TOL
            for program in self.programs
        ):
            raise ValueError("every controlled apparatus block must be exhaustive")

    @property
    def block_kraus(self) -> tuple[tuple[np.ndarray, ...], ...]:
        legal = tuple(padded_kraus(program) for program in self.programs)
        idle_extension = (I2,) + tuple(
            np.zeros((2, 2), dtype=complex)
            for _ in range(POINTER_DIMENSION - 1)
        )
        return legal + (idle_extension, idle_extension)

    @property
    def update(self) -> np.ndarray:
        tensor = np.zeros(
            (
                PROGRAM_DIMENSION,
                POINTER_DIMENSION,
                2,
                PROGRAM_DIMENSION,
                2,
            ),
            dtype=complex,
        )
        for label, blocks in enumerate(self.block_kraus):
            tensor[label, :, :, label, :] = np.asarray(blocks)
        return tensor.reshape(PROGRAM_DIMENSION * POINTER_DIMENSION * 2, -1)


def program_basis(label: int) -> np.ndarray:
    if not 0 <= label < LAWFUL_PROGRAMS:
        raise ValueError("the declared program label is outside the six-state code")
    state = np.zeros(PROGRAM_DIMENSION, dtype=complex)
    state[label] = 1
    return state


def validate_program_state(state: np.ndarray) -> None:
    if state.shape != (PROGRAM_DIMENSION,):
        raise ValueError("program state must live on three M2")
    if abs(np.linalg.norm(state) - 1) >= TOL:
        raise ValueError("program state must be normalized")
    if np.linalg.norm(state[LAWFUL_PROGRAMS:]) >= TOL:
        raise ValueError("program state leaves the six-state lawful code")


def validate_pointer_blank(label: int) -> None:
    if label != 0:
        raise ValueError("each isometry use requires the declared blank pointer")


def apply_fixed_update(update: np.ndarray, state: np.ndarray) -> np.ndarray:
    return update @ state


def two_use_from_fixed(update: np.ndarray) -> np.ndarray:
    tensor = update.reshape(
        PROGRAM_DIMENSION,
        POINTER_DIMENSION,
        2,
        PROGRAM_DIMENSION,
        2,
    )
    composed = np.einsum(
        "ckudt,djtbs->cjkubs",
        tensor,
        tensor,
    )
    return composed.reshape(
        PROGRAM_DIMENSION * POINTER_DIMENSION**2 * 2,
        PROGRAM_DIMENSION * 2,
    )


def direct_two_use(carrier: FixedProgramCarrier) -> np.ndarray:
    tensor = np.zeros(
        (
            PROGRAM_DIMENSION,
            POINTER_DIMENSION,
            POINTER_DIMENSION,
            2,
            PROGRAM_DIMENSION,
            2,
        ),
        dtype=complex,
    )
    for label, blocks in enumerate(carrier.block_kraus):
        for first, left in enumerate(blocks):
            for second, right in enumerate(blocks):
                tensor[label, first, second, :, label, :] = right @ left
    return tensor.reshape(PROGRAM_DIMENSION * POINTER_DIMENSION**2 * 2, -1)


def carrier_program_controls(carrier: FixedProgramCarrier) -> dict[str, float]:
    update = carrier.update
    tensor = update.reshape(
        PROGRAM_DIMENSION,
        POINTER_DIMENSION,
        2,
        PROGRAM_DIMENSION,
        2,
    )
    gram = np.asarray(
        [program_basis(label) for label in range(LAWFUL_PROGRAMS)]
    )
    block_residual = 0.0
    off_diagonal = 0.0
    for output_label in range(PROGRAM_DIMENSION):
        for input_label in range(PROGRAM_DIMENSION):
            block = tensor[output_label, :, :, input_label, :].reshape(16, 2)
            if output_label == input_label:
                expected = c321.c317.stack_isometry(
                    carrier.block_kraus[input_label]
                )
                block_residual = max(
                    block_residual,
                    float(np.linalg.norm(block - expected)),
                )
            else:
                off_diagonal = max(off_diagonal, float(np.linalg.norm(block)))

    amplitudes = np.asarray((1, 1j, -1, 2j, 2, -1j, 0, 0), dtype=complex)
    amplitudes /= np.linalg.norm(amplitudes)
    system = np.asarray((1, 1j), dtype=complex) / np.sqrt(2)
    coherent_input = np.kron(amplitudes, system)
    coherent_output = apply_fixed_update(update, coherent_input).reshape(
        PROGRAM_DIMENSION, POINTER_DIMENSION, 2
    )
    expected = np.zeros_like(coherent_output)
    for label in range(LAWFUL_PROGRAMS):
        for pointer, operator in enumerate(carrier.block_kraus[label]):
            expected[label, pointer] = amplitudes[label] * operator @ system
    coherent_residual = float(np.linalg.norm(coherent_output - expected))

    source = " ".join(inspect.getsource(apply_fixed_update).split())
    detail = {
        "program_code_Gram_residual": float(
            np.linalg.norm(gram @ gram.conj().T - np.eye(LAWFUL_PROGRAMS))
        ),
        "full_three_M2_program_basis_dimension": PROGRAM_DIMENSION,
        "lawful_program_code_dimension": LAWFUL_PROGRAMS,
        "fixed_update_isometry_residual": float(
            np.linalg.norm(update.conj().T @ update - np.eye(16))
        ),
        "controlled_block_recovery_residual": block_residual,
        "off_diagonal_program_write_residual": off_diagonal,
        "coherent_superposition_residual": coherent_residual,
        "application_source": source,
    }
    check(
        "one fixed three-M2-program controlled isometry stores and coherently applies all six apparatus blocks without a host program branch query",
        detail["program_code_Gram_residual"] < TOL
        and detail["fixed_update_isometry_residual"] < TOL
        and block_residual < TOL
        and off_diagonal < TOL
        and coherent_residual < TOL
        and source.endswith("return update @ state"),
        detail,
    )
    return detail


def sequence_program(program: c321.Program) -> tuple[
    tuple[np.ndarray, ...], tuple[tuple[int, ...], ...]
]:
    count = len(program.kraus)
    blocks = tuple(
        second @ first
        for first in program.kraus
        for second in program.kraus
    )
    groups = tuple(
        tuple(
            first * count + second
            for first in first_group
            for second in second_group
        )
        for first_group in program.coarse_groups
        for second_group in program.coarse_groups
    )
    return blocks, groups


def grouped_sequence_chois(program: c321.Program) -> tuple[np.ndarray, ...]:
    blocks, groups = sequence_program(program)
    return tuple(
        c321.choi(tuple(blocks[index] for index in group))
        for group in groups
    )


def grouped_sequence_effects(program: c321.Program) -> tuple[np.ndarray, ...]:
    blocks, groups = sequence_program(program)
    return tuple(
        sum(
            (
                blocks[index].conj().T @ blocks[index]
                for index in group
            ),
            start=np.zeros((2, 2), dtype=complex),
        )
        for group in groups
    )


def sequential_composition_controls(
    carrier: FixedProgramCarrier,
) -> dict[str, object]:
    update = carrier.update
    sequential = two_use_from_fixed(update)
    direct = direct_two_use(carrier)
    composition_residual = float(np.linalg.norm(sequential - direct))
    isometry_residual = float(
        np.linalg.norm(sequential.conj().T @ sequential - np.eye(16))
    )
    tensor = sequential.reshape(
        PROGRAM_DIMENSION,
        POINTER_DIMENSION,
        POINTER_DIMENSION,
        2,
        PROGRAM_DIMENSION,
        2,
    )
    off_diagonal = max(
        float(
            np.linalg.norm(
                tensor[output_label, :, :, :, input_label, :]
            )
        )
        for output_label in range(PROGRAM_DIMENSION)
        for input_label in range(PROGRAM_DIMENSION)
        if output_label != input_label
    )
    detail = {
        "fixed_twice_vs_direct_Kraus_product_residual": composition_residual,
        "two_use_isometry_residual": isometry_residual,
        "two_use_program_write_residual": off_diagonal,
        "fresh_pointer_M2": 2 * POINTER_M2,
    }
    check(
        "the identical fixed controlled update composes twice with fresh pointers and no program rewrite or dispatch",
        composition_residual < TOL
        and isometry_residual < TOL
        and off_diagonal < TOL,
        detail,
    )
    return detail


def two_use_equivalence_controls(
    programs: tuple[c321.Program, ...]
) -> tuple[dict[str, float], dict[str, float]]:
    axis_left, axis_right, ray_unsplit, ray_refined = programs[:4]

    ray_effect_residual = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(
            grouped_sequence_effects(ray_unsplit),
            grouped_sequence_effects(ray_refined),
        )
    )
    ray_cp_residual = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(
            grouped_sequence_chois(ray_unsplit),
            grouped_sequence_chois(ray_refined),
        )
    )
    ray_left_blocks, _ = sequence_program(ray_unsplit)
    ray_right_blocks, _ = sequence_program(ray_refined)
    ray_total_residual = float(
        np.linalg.norm(c321.choi(ray_left_blocks) - c321.choi(ray_right_blocks))
    )
    ray_future = float(
        c321.future_process_witness(ray_left_blocks, ray_right_blocks)
    )
    ray_fine_transcript = float(
        np.linalg.norm(
            c321.transcript_choi(
                tuple(operator.conj().T @ operator for operator in ray_left_blocks),
                dimension=64,
            )
            - c321.transcript_choi(
                tuple(operator.conj().T @ operator for operator in ray_right_blocks),
                dimension=64,
            )
        )
    )
    ray_detail = {
        "two_use_coarse_effect_residual": ray_effect_residual,
        "two_use_coarse_instrument_Choi_residual": ray_cp_residual,
        "two_use_pointer_erased_Choi_residual": ray_total_residual,
        "two_use_held_future_witness": ray_future,
        "two_use_fine_transcript_Choi_residual": ray_fine_transcript,
    }
    check(
        "the ray-refinement coarse-CP quotient remains exact after two fixed-carrier uses while its fine two-pointer transcript remains visible",
        ray_effect_residual < TOL
        and ray_cp_residual < TOL
        and ray_total_residual < TOL
        and ray_future < TOL
        and ray_fine_transcript > 0.9,
        ray_detail,
    )

    axis_effect_residual = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(
            grouped_sequence_effects(axis_left),
            grouped_sequence_effects(axis_right),
        )
    )
    axis_cp_residual = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(
            grouped_sequence_chois(axis_left),
            grouped_sequence_chois(axis_right),
        )
    )
    axis_left_blocks, _ = sequence_program(axis_left)
    axis_right_blocks, _ = sequence_program(axis_right)
    axis_total_residual = float(
        np.linalg.norm(
            c321.choi(axis_left_blocks) - c321.choi(axis_right_blocks)
        )
    )
    axis_future = float(
        c321.future_process_witness(axis_left_blocks, axis_right_blocks)
    )
    axis_fine_transcript = float(
        np.linalg.norm(
            c321.transcript_choi(
                tuple(operator.conj().T @ operator for operator in axis_left_blocks),
                dimension=64,
            )
            - c321.transcript_choi(
                tuple(operator.conj().T @ operator for operator in axis_right_blocks),
                dimension=64,
            )
        )
    )
    axis_detail = {
        "two_use_coarse_effect_residual": axis_effect_residual,
        "two_use_coarse_instrument_Choi_residual": axis_cp_residual,
        "two_use_pointer_erased_Choi_residual": axis_total_residual,
        "two_use_held_future_witness": axis_future,
        "two_use_fine_transcript_Choi_residual": axis_fine_transcript,
    }
    check(
        "the equal-effect axis pair remains process-distinguishable after two fixed-carrier uses even though its coarse outcome effects still agree",
        axis_effect_residual < TOL
        and axis_cp_residual > 0.2
        and axis_total_residual > 0.8
        and axis_future > 0.3
        and axis_fine_transcript > 0.6,
        axis_detail,
    )
    return ray_detail, axis_detail


def physical_fixture_controls() -> dict[int, c321.c317.PhysicalFixture]:
    fixtures = {
        length: c321.c317.physical_fixture(length)
        for length in (3, 6)
    }
    rows = []
    for length, fixture in fixtures.items():
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "Gram": float(
                    np.linalg.norm(
                        fixture.two_ray_encoding.conj().T
                        @ fixture.two_ray_encoding
                        - I2
                    )
                ),
                "contact": float(
                    np.linalg.norm(
                        fixture.physical_contact @ fixture.two_ray_encoding
                        - fixture.two_ray_encoding @ fixture.contact
                    )
                ),
                "constraint": float(
                    np.linalg.norm(
                        fixture.constraint @ fixture.two_ray_encoding
                        - fixture.two_ray_encoding
                    )
                ),
            }
        )
    species = c321.c317.c311.c219.common_species(-0.3)
    mass_residual = abs(
        c321.c317.c311.c219.rest_mass(species) / species.analytic_mass - 1
    )
    check(
        "the program carrier retains the accepted same-number physical contact seam and one-particle mass fixture through held L=6",
        all(max(row["Gram"], row["contact"], row["constraint"]) < TOL for row in rows)
        and mass_residual < 3e-12,
        {"rows": rows, "one_particle_mass_relative_residual": mass_residual},
    )
    return fixtures


def encoded_logical_carrier(
    encoding: np.ndarray, update: np.ndarray
) -> np.ndarray:
    tensor = update.reshape(
        PROGRAM_DIMENSION,
        POINTER_DIMENSION,
        2,
        PROGRAM_DIMENSION,
        2,
    )
    encoded = np.einsum("xt,pqtbs->pqxbs", encoding, tensor)
    return encoded.reshape(
        PROGRAM_DIMENSION * POINTER_DIMENSION * encoding.shape[0],
        PROGRAM_DIMENSION * 2,
    )


def direct_physical_carrier(
    encoding: np.ndarray, carrier: FixedProgramCarrier
) -> np.ndarray:
    tensor = np.zeros(
        (
            PROGRAM_DIMENSION,
            POINTER_DIMENSION,
            encoding.shape[0],
            PROGRAM_DIMENSION,
            2,
        ),
        dtype=complex,
    )
    for label, blocks in enumerate(carrier.block_kraus):
        for pointer, operator in enumerate(blocks):
            tensor[label, pointer, :, label, :] = encoding @ operator
    return tensor.reshape(
        PROGRAM_DIMENSION * POINTER_DIMENSION * encoding.shape[0],
        PROGRAM_DIMENSION * 2,
    )


def physical_embedding_and_support_controls(
    fixtures: dict[int, c321.c317.PhysicalFixture],
    carrier: FixedProgramCarrier,
) -> list[dict[str, object]]:
    rows = []
    for length, fixture in fixtures.items():
        encoded = encoded_logical_carrier(fixture.two_ray_encoding, carrier.update)
        direct = direct_physical_carrier(fixture.two_ray_encoding, carrier)
        code_projector = (
            fixture.two_ray_encoding @ fixture.two_ray_encoding.conj().T
        )
        leakage = 0.0
        constraint_residual = 0.0
        for program in carrier.programs:
            first_blocks = program.kraus
            second_blocks = tuple(
                right @ left
                for left in program.kraus
                for right in program.kraus
            )
            for operator in first_blocks + second_blocks:
                physical = fixture.two_ray_encoding @ operator
                leakage = max(
                    leakage,
                    float(np.linalg.norm((np.eye(510) - code_projector) @ physical)),
                )
                constraint_residual = max(
                    constraint_residual,
                    float(np.linalg.norm(fixture.constraint @ physical - physical)),
                )

        representatives = tuple(
            c321.c317.c311.branch_representative(
                fixture.code, fixture.encoder.body, branch, r_value
            )
            for r_value in (0, 1)
            for branch in fixture.basis_rows
        )
        pairs = set()
        for program in carrier.programs:
            blocks = program.kraus + tuple(
                right @ left
                for left in program.kraus
                for right in program.kraus
            )
            for operator in blocks:
                raw = (
                    fixture.two_ray_encoding
                    @ operator
                    @ fixture.two_ray_encoding.conj().T
                )
                pairs.update(
                    (int(row), int(column))
                    for row, column in np.argwhere(abs(raw) > 1e-12)
                )
        support_union = 0
        maximum = 0
        port_failures = sector_failures = 0
        for row, column in pairs:
            transition = representatives[row] @ c321.c317.c311.local.pauli_dagger(
                representatives[column]
            )
            support = transition.x | transition.z
            support_union |= support
            maximum = max(maximum, support.bit_count())
            port_failures += sum(
                not transition.commutes(
                    c321.c317.c311.c305.constraint_pauli(fixture.code, vertex)
                )
                for vertex in range(len(fixture.code.graph.vertices))
            )
            sector_failures += sum(
                not transition.commutes(check_row)
                for check_row in fixture.code.local_checks + fixture.code.wilsons
            )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "logical_to_physical_carrier_residual": float(
                    np.linalg.norm(encoded - direct)
                ),
                "physical_carrier_isometry_residual": float(
                    np.linalg.norm(direct.conj().T @ direct - np.eye(16))
                ),
                "one_and_two_use_leakage": leakage,
                "role_constraint_residual": constraint_residual,
                "matrix_unit_pairs": len(pairs),
                "matter_transition_union_M2": support_union.bit_count(),
                "maximum_matter_transition_M2": maximum,
                "maximum_one_use_controlled_M2": maximum + PROGRAM_M2 + POINTER_M2,
                "maximum_two_use_controlled_M2": maximum + PROGRAM_M2 + 2 * POINTER_M2,
                "one_use_patch_M2": 56 + PROGRAM_M2 + POINTER_M2,
                "two_use_patch_M2": 56 + PROGRAM_M2 + 2 * POINTER_M2,
                "two_use_installed_overhead_M2_per_cell": 23 + PROGRAM_M2 + 2 * POINTER_M2,
                "port_constraint_failures": port_failures,
                "local_check_or_Wilson_failures": sector_failures,
            }
        )
    check(
        "the fixed program carrier and its two-use products have bounded physical M2 support and zero inherited leakage through held L=6",
        all(
            row["logical_to_physical_carrier_residual"] < TOL
            and row["physical_carrier_isometry_residual"] < TOL
            and row["one_and_two_use_leakage"] < TOL
            and row["role_constraint_residual"] < TOL
            and row["matrix_unit_pairs"] == 16
            and row["matter_transition_union_M2"] == 20
            and row["maximum_matter_transition_M2"] <= 20
            and row["maximum_one_use_controlled_M2"] <= 26
            and row["maximum_two_use_controlled_M2"] <= 29
            and row["one_use_patch_M2"] == 62
            and row["two_use_patch_M2"] == 65
            and row["two_use_installed_overhead_M2_per_cell"] == 32
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in rows
        ),
        rows,
    )
    return rows


def covariance_controls(
    fixtures: dict[int, c321.c317.PhysicalFixture],
    carrier: FixedProgramCarrier,
) -> dict[str, object]:
    base = fixtures[3]
    reducer = c321.c317.c311.c305.StabilizerReducer(base.code)
    selected = np.zeros((127, 2), dtype=complex)
    selected[
        [
            c321.c317.c311.SEAM_INDEX[(2, (0, 1), stream_slice)]
            for stream_slice in (0, 1)
        ],
        [0, 1],
    ] = 1
    rows = []
    for frame in c321.c317.c311.c235.proper_cubic_frames():
        logical_r = c321.c317.c311.logical_frame_representation(frame)
        old_r, failures = c321.c317.c311.flagged_frame_representation(
            base.encoder,
            base.basis_rows,
            base.occurrence,
            frame,
            reducer,
        )
        mapping, phases, mapping_failures = c321.c317.c311.signed_mapping(old_r)
        new_mapping = np.concatenate((mapping, mapping + 255))
        new_phases = np.concatenate((phases, phases))
        carried_encoding = base.full_encoding @ logical_r @ selected
        one_use = 0.0
        two_use = 0.0
        for program in carrier.programs:
            for operator in program.kraus:
                mapped = c321.c317.c311.apply_signed_mapping(
                    new_mapping,
                    new_phases,
                    base.two_ray_encoding @ operator,
                )
                one_use = max(
                    one_use,
                    float(np.linalg.norm(mapped - carried_encoding @ operator)),
                )
            for left in program.kraus:
                for right in program.kraus:
                    product = right @ left
                    mapped = c321.c317.c311.apply_signed_mapping(
                        new_mapping,
                        new_phases,
                        base.two_ray_encoding @ product,
                    )
                    two_use = max(
                        two_use,
                        float(np.linalg.norm(mapped - carried_encoding @ product)),
                    )
        rows.append((failures + mapping_failures, one_use, two_use))
    detail = {
        "frames": len(rows),
        "branch_failures": sum(row[0] for row in rows),
        "maximum_one_use_carrier_residual": max(row[1] for row in rows),
        "maximum_two_use_carrier_residual": max(row[2] for row in rows),
    }
    check(
        "the fixed controlled carrier and two-use composition have carried covariance under all 24 proper-cubic frames",
        len(rows) == 24
        and all(
            failures == 0 and one_use < TOL and two_use < TOL
            for failures, one_use, two_use in rows
        ),
        detail,
    )
    return detail


def contact_deletion_and_domain_controls(
    fixture: c321.c317.PhysicalFixture,
    carrier: FixedProgramCarrier,
) -> dict[str, float]:
    deleted_contact_carrier = FixedProgramCarrier(make_programs(I2))
    one_use_contact_residual = float(
        np.linalg.norm(carrier.update - deleted_contact_carrier.update)
    )
    two_use_contact_residual = float(
        np.linalg.norm(
            two_use_from_fixed(carrier.update)
            - two_use_from_fixed(deleted_contact_carrier.update)
        )
    )
    ray = carrier.programs[2]
    transverse = c321.projector((3, -4, 0))
    selected_effect_contact_residual = float(
        np.linalg.norm(ray.coarse_effects[0] - 0.61 * transverse)
    )
    detail = {
        "one_use_fixed_update_contact_deletion_residual": one_use_contact_residual,
        "two_use_fixed_update_contact_deletion_residual": two_use_contact_residual,
        "selected_ray_effect_contact_deletion_residual": selected_effect_contact_residual,
        "physical_contact_intertwiner": float(
            np.linalg.norm(
                fixture.physical_contact @ fixture.two_ray_encoding
                - fixture.two_ray_encoding @ fixture.contact
            )
        ),
    }
    check(
        "the one- and two-use fixed carriers remain actually dependent on the Cycle-230 contact",
        detail["physical_contact_intertwiner"] < TOL
        and one_use_contact_residual > 0.9
        and two_use_contact_residual > 1.6
        and selected_effect_contact_residual > 0.15,
        detail,
    )

    update_tensor = carrier.update.reshape(
        PROGRAM_DIMENSION,
        POINTER_DIMENSION,
        2,
        PROGRAM_DIMENSION,
        2,
    ).copy()
    branch_deleted = update_tensor.copy()
    branch_deleted[3, 1, :, 3, :] = 0
    branch_deleted = branch_deleted.reshape(128, 16)
    branch_defect = float(
        np.linalg.norm(branch_deleted.conj().T @ branch_deleted - np.eye(16), 2)
    )
    control_deleted = update_tensor.copy()
    control_deleted[4, :, :, 4, :] = 0
    control_deleted = control_deleted.reshape(128, 16)
    control_defect = float(
        np.linalg.norm(control_deleted.conj().T @ control_deleted - np.eye(16), 2)
    )
    check(
        "deleting one refinement branch or one complete program-control block breaks the fixed-carrier isometry",
        branch_defect > 0.38 and control_defect > 0.99,
        {
            "refinement_branch_deletion_isometry_defect": branch_defect,
            "program_control_block_deletion_isometry_defect": control_defect,
        },
    )

    rejected = 0
    invalid_program = c321.Program(
        "zero block",
        (np.zeros((2, 2), dtype=complex),),
        ((0,),),
    )
    invalid_calls = (
        lambda: FixedProgramCarrier(carrier.programs[:5]),
        lambda: FixedProgramCarrier(carrier.programs[:5] + (carrier.programs[0],)),
        lambda: FixedProgramCarrier(carrier.programs[:5] + (invalid_program,)),
        lambda: program_basis(6),
        lambda: validate_program_state(np.eye(PROGRAM_DIMENSION)[6]),
        lambda: validate_program_state(np.ones(PROGRAM_DIMENSION)),
        lambda: validate_pointer_blank(1),
        lambda: two_use_from_fixed(np.zeros((127, 16), dtype=complex)),
    )
    for call in invalid_calls:
        try:
            call()
        except (ValueError, IndexError):
            rejected += 1
    check(
        "the lawful domain rejects wrong program counts, duplicate/nonexhaustive blocks, invalid program states, nonblank pointers, and malformed updates",
        rejected == len(invalid_calls),
        {"rejected": rejected, "attempted": len(invalid_calls)},
    )
    return detail


def semantic_firewall_controls() -> None:
    text = normalized(NOTE)
    check(
        "the semantic firewall keeps program control, coefficient supply, pointer output, occurrence, Record, and grade distinct",
        "program control is not law-selection derivation" in text
        and "pointer output is not occurrence" in text
        and "program labels are not records" in text
        and "program-state preparation remains supplied" in text
        and "coefficients remain supplied" in text
        and "blank pointer remains supplied" in text
        and "numerical grade remains open" in text
        and "frequency remains open" in text,
        {
            "fixed_controlled_update": "derived",
            "program_preparation": None,
            "coefficient_selection": None,
            "blank_pointer": None,
            "occurrence": None,
            "Record": None,
            "numerical_grade": None,
            "frequency": None,
        },
    )


def markdown_section(body: str, start: str, end: str | None) -> str:
    left = body.index(start)
    right = len(body) if end is None else body.index(end, left)
    return body[left:right]


def strict_no_go_controls() -> None:
    print("\nSTRICT N1-N8 RELEASE DISCIPLINE")
    note = NOTE.read_text(encoding="utf-8")
    completed = subprocess.run(
        ["git", "rev-parse", "--verify", "origin/main"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    check(
        "the no-go method is pinned to the freshly fetched main ref",
        completed.returncode == 0 and completed.stdout.strip() == FRESH_MAIN,
        {"expected": FRESH_MAIN, "observed": completed.stdout.strip()},
    )

    n1 = markdown_section(note, "### N1", "### N2")
    allowed = {"ATTEMPTED", "RULED OUT BY PRIOR RESULT", "OPEN / UNTESTED"}
    markers = {}
    malformed = []
    for route in N1_ROUTES:
        match = re.search(
            rf"^\|\s*{re.escape(route)}\s*\|[^|]*\|\s*(\*\*[^*]+\*\*)\s*\|",
            n1,
            re.MULTILINE,
        )
        raw = match.group(1) if match else ""
        marker = raw.replace("*", "")
        markers[route] = marker
        if raw != f"**{marker}**" or marker not in allowed:
            malformed.append((route, raw))
    bold = tuple(re.findall(r"\*\*([^*]+)\*\*", n1))
    check(
        "N1 uses only exact bold honesty markers on eight distinct routes",
        not malformed and len(bold) == 8 and set(bold) <= allowed,
        {"markers": markers, "malformed": malformed, "all_bold": bold},
    )

    n2 = markdown_section(note, "### N2", "### N3")
    pair_rows = []
    for left, right in combinations(WALLS, 2):
        match = re.search(
            rf"^\|\s*`{left}/{right}`\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|\s*(yes|no)\s*\|",
            n2,
            re.MULTILINE | re.IGNORECASE,
        )
        pair_rows.append(
            (left, right, tuple(value.lower() for value in match.groups()) if match else None)
        )
    check(
        "N2 validates both closure directions for all fifteen collapsed wall pairs",
        len(pair_rows) == 15
        and all(row[2] == ("no", "no", "yes") for row in pair_rows),
        pair_rows,
    )

    trigger_rows = []
    for path in (Path(__file__).resolve(), NOTE):
        lines = path.read_text(encoding="utf-8").lower().splitlines()
        hits = []
        for parts in TRIGGER_PARTS:
            trigger = "".join(parts)
            hits.extend(
                (trigger, line_number)
                for line_number, line in enumerate(lines, 1)
                if trigger in line
            )
        trigger_rows.append((str(path.relative_to(ROOT)), tuple(hits)))
    check(
        "N3 literal hidden-condition procedure scan has zero hits on both release paths",
        all(not row[1] for row in trigger_rows),
        trigger_rows,
    )

    fragment_parts = (
        (
            "one fixed three-M2-program controlled isometry stores and coherently applies ",
            "all six apparatus blocks without a host program branch query",
        ),
        (
            "the identical fixed controlled update composes twice with fresh pointers ",
            "and no program rewrite or dispatch",
        ),
        (
            "the ray-refinement coarse-CP quotient remains exact after two fixed-carrier uses ",
            "while its fine two-pointer transcript remains visible",
        ),
        (
            "the equal-effect axis pair remains process-distinguishable after two fixed-carrier uses ",
            "even though its coarse outcome effects still agree",
        ),
        (
            "the fixed program carrier and its two-use products have bounded physical M2 support ",
            "and zero inherited leakage through held L=6",
        ),
        (
            "the fixed controlled carrier and two-use composition have carried covariance ",
            "under all 24 proper-cubic frames",
        ),
    )
    fragments = tuple(left + right for left, right in fragment_parts)
    runner_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    relative = str(Path(__file__).resolve().relative_to(ROOT))
    rows = []
    for fragment in fragments:
        hits = tuple(
            line_number
            for line_number, line in enumerate(runner_lines, 1)
            if fragment in line
        )
        reference = f"{relative}:{hits[0]}" if len(hits) == 1 else None
        rows.append((fragment, hits, reference, bool(reference and reference in note)))
    check(
        "N4 pins every decisive current residual to one exact executable line",
        all(len(row[1]) == 1 and row[3] for row in rows),
        rows,
    )

    flat = " ".join(note.split())
    requirements = (
        (
            "N5 separates program, use, CP, pointer, and global resolutions",
            (
                "per-program state",
                "per-use block",
                "per-coarse CP outcome",
                "pointer-visible",
                "two-use",
                "lattice/global",
            ),
        ),
        (
            "N6 retains seven explicit constructive import-retirement paths",
            (
                "fixed controlled update",
                "coherent program carrier",
                "coarse-CP quotient",
                "coefficient-bearing program",
                "fresh-pointer recurrence",
                "occurrence/Record",
                "process-functional/global-history",
            ),
        ),
        (
            "N7 contains the strongest finite-program compiler steelman",
            (
                "hostile constructive reviewer",
                "finite gate synthesis",
                "could still retire",
            ),
        ),
        (
            "N8 records six cross-cycle retirement mechanisms",
            (
                "Cycle 311 M64 seam",
                "Cycle 317 eight-label pointer",
                "Cycle 321 coarse-CP quotient",
                "Cycle 230 contact",
                "Cycle 287 typed Record",
                "PR-5451 instrument nonselection",
            ),
        ),
    )
    for label, required in requirements:
        missing = tuple(item for item in required if item not in flat)
        check(label, not missing, missing)
    broad = (
        "Broad gate status: FAIL / DO NOT SHIP",
        "No shared obstruction and no axiom pressure follow.",
        "coefficient/recurrent/occurrence routes remain open",
    )
    missing = tuple(item for item in broad if item not in flat)
    check(
        "the broad program-autonomy/occurrence/no-go and axiom-pressure release is blocked",
        not missing,
        missing,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    fixtures = physical_fixture_controls()
    programs = make_programs(fixtures[3].contact)
    carrier = FixedProgramCarrier(programs)
    carrier_result = carrier_program_controls(carrier)
    sequence_result = sequential_composition_controls(carrier)
    ray_result, axis_result = two_use_equivalence_controls(programs)
    support_result = physical_embedding_and_support_controls(fixtures, carrier)
    covariance_result = covariance_controls(fixtures, carrier)
    contact_result = contact_deletion_and_domain_controls(fixtures[3], carrier)
    semantic_firewall_controls()
    strict_no_go_controls()
    check(
        "Cycle 323 physicalizes one fixed six-program carrier and two-use coarse-CP refinement stability without selecting coefficients, occurrence, or a general effect quotient",
        carrier_result["fixed_update_isometry_residual"] < TOL
        and sequence_result["fixed_twice_vs_direct_Kraus_product_residual"] < TOL
        and ray_result["two_use_coarse_instrument_Choi_residual"] < TOL
        and axis_result["two_use_coarse_instrument_Choi_residual"] > 0.2
        and all(row["one_and_two_use_leakage"] < TOL for row in support_result)
        and covariance_result["maximum_two_use_carrier_residual"] < TOL
        and contact_result["two_use_fixed_update_contact_deletion_residual"] > 1.6
        and "broad gate status: fail / do not ship" in normalized(NOTE),
        {
            "carrier": carrier_result,
            "sequence": sequence_result,
            "ray": ray_result,
            "axis": axis_result,
        },
    )
    print("DATA carrier", carrier_result)
    print("DATA sequence", sequence_result)
    print("DATA ray", ray_result)
    print("DATA axis", axis_result)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE323_FIXED_PROGRAM_CARRIER_TWO_USE_GREEN"
        if FAIL == 0
        else "CYCLE323_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
