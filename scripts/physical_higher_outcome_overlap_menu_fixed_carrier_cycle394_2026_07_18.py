#!/usr/bin/env python3
"""Cycle 394: install four further overlap menus in a fixed M2 carrier.

The root-reviewed Cycle-390 seven-menu installation is retained verbatim.  A
second fixed carrier installs one landed Cycle-317 host-merge presentation,
two further five-outcome presentations, and one seven-outcome presentation.
All effects belong to the same 55 exact Cycle-381 functionality classes.

This is a constructive finite installation.  Numerical-grade selection,
probability/actuality, Records, global obstruction, minimum content, and axiom
pressure are outside its claims.  Authority is none; audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass
from hashlib import sha256
from inspect import getsource
from io import StringIO
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_HIGHER_OUTCOME_OVERLAP_MENU_FIXED_CARRIER_CYCLE394_NOTE_2026-07-18.md"
)

import physical_seven_overlap_menu_fixed_carrier_cycle390_2026_07_18 as c390


c385 = c390.c385
c381 = c390.c381
c383 = c390.c383
c323 = c390.c323
c321 = c390.c321
c317 = c390.c317
TOL = c390.TOL
I2 = c390.I2
PROGRAM_M2 = 3
PROGRAM_DIMENSION = 2**PROGRAM_M2
LAWFUL_PROGRAMS = 4
POINTER_M2 = 3
POINTER_DIMENSION = 2**POINTER_M2
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0


# The first row is the Cycle-385 host merge made with the landed Cycle-317
# compiler and expressed in the Cycle-381 effect-class quotient.  Its concrete
# components/grouping are host supplied.  The remaining rows are exact supplied
# higher-outcome presentations selected from that same finite class inventory.
ADDITIONAL_CLASS_ROWS = (
    (8, 1, 3, 5, 7),
    (0, 1, 7, 7, 27),
    (4, 4, 24, 25, 27),
    (0, 1, 4, 5, 5, 5, 26),
)
ROW_SOURCES = (
    "Cycle385 host merge using the landed Cycle317 compiler",
    "supplied exact five-outcome overlap presentation A",
    "supplied exact five-outcome overlap presentation B",
    "supplied exact seven-outcome overlap presentation C",
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
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-394 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    required = (
        "authority: none",
        "audit: unset",
        "rank 27 to 31",
        "47 menus, 55 classes, rank 31",
        "one host-merge, two five-outcome, and one seven-outcome presentation",
        "11 unique effect blocks",
        "22 pointer outcomes",
        "four lawful programs plus four idle extensions",
        "three-m2 program register",
        "three-m2 pointer register",
        "contact-postcomposed positive-square-root",
        "one fixed controlled isometry",
        "e g_logical = g_physical e",
        "l=3 and held l=6",
        "all 24 proper-cubic frames",
        "one-particle mass fixture",
        "all eleven overlap-row deletion ranks are 30",
        "effect-class and row tables remain supplied",
        "program-state preparation remains supplied",
        "blank pointer remains supplied",
        "menu genesis remains supplied",
        "pointer output is not a record",
        "born selection: not claimed",
        "global obstruction: not claimed",
        "minimum content: not claimed",
        "axiom pressure: not claimed",
    )
    text = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the four-menu extension, physical controls, inventory, status split, and claim boundary",
        not missing,
        missing,
    )
    return {"missing": missing}


def candidate_source(
    fixtures: dict[int, c317.PhysicalFixture],
) -> tuple[c385.EffectSystem, c390.CompiledMenus, c390.CompiledMenus, float]:
    base, prior_rows, _carriers, _tables = c390.candidate_source(fixtures)
    prior = c390.compile_menus(base, prior_rows, fixtures[3].contact)
    additional = compile_additional(base, ADDITIONAL_CLASS_ROWS, fixtures[3].contact)

    host_merge = c385.host_instantiated_menus(fixtures[3])[-1]
    host_system = c385.build_effect_system(
        base.menus + (host_merge,), effect_functionality_premise=True
    )
    host_row_residual = float(np.linalg.norm(
        host_system.incidence[-1]
        - np.bincount(ADDITIONAL_CLASS_ROWS[0], minlength=len(base.effects))
    ))
    if host_system.menu_classes[-1] != ADDITIONAL_CLASS_ROWS[0]:
        raise ValueError("the landed host-merge class row changed")
    return base, prior, additional, host_row_residual


def compile_additional(
    base: c385.EffectSystem,
    class_rows: tuple[tuple[int, ...], ...],
    contact: np.ndarray,
) -> c390.CompiledMenus:
    if len(class_rows) != LAWFUL_PROGRAMS:
        raise ValueError("the Cycle-394 code requires four menu rows")
    if tuple(class_rows) != ADDITIONAL_CLASS_ROWS:
        raise ValueError("the supplied Cycle-394 menu table changed")
    if any(not 1 <= len(row) <= POINTER_DIMENSION for row in class_rows):
        raise ValueError("an additional menu does not fit the pointer register")
    return c390.compile_menus(base, class_rows, contact)


@dataclass(frozen=True)
class FourMenuCarrier:
    programs: tuple[c321.Program, ...]

    def __post_init__(self) -> None:
        if len(self.programs) != LAWFUL_PROGRAMS:
            raise ValueError("the declared code requires exactly four programs")
        if len({program.name for program in self.programs}) != LAWFUL_PROGRAMS:
            raise ValueError("lawful program names must be distinct")
        if any(
            len(program.kraus) > POINTER_DIMENSION
            or np.linalg.norm(program.completeness - I2) >= TOL
            for program in self.programs
        ):
            raise ValueError("every lawful program must fit and be exhaustive")

    @property
    def block_kraus(self) -> tuple[tuple[np.ndarray, ...], ...]:
        idle = (I2,) + tuple(
            np.zeros((2, 2), dtype=complex)
            for _ in range(POINTER_DIMENSION - 1)
        )
        lawful = tuple(c390.padded_kraus(program) for program in self.programs)
        return lawful + (idle,) * (PROGRAM_DIMENSION - LAWFUL_PROGRAMS)

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
        return tensor.reshape(
            PROGRAM_DIMENSION * POINTER_DIMENSION * 2,
            PROGRAM_DIMENSION * 2,
        )


def program_basis(label: int) -> np.ndarray:
    if not 0 <= label < LAWFUL_PROGRAMS:
        raise ValueError("program label is outside the four-state lawful code")
    state = np.zeros(PROGRAM_DIMENSION, dtype=complex)
    state[label] = 1
    return state


def validate_program_state(state: np.ndarray) -> None:
    if state.shape != (PROGRAM_DIMENSION,) or abs(np.linalg.norm(state) - 1) >= TOL:
        raise ValueError("program preparation must be one normalized three-M2 state")
    if np.linalg.norm(state[LAWFUL_PROGRAMS:]) >= TOL:
        raise ValueError("program preparation leaves the four-state lawful code")


def validate_pointer_blank(label: int) -> None:
    if label != 0:
        raise ValueError("the fixed dilation requires the supplied blank pointer")


def apply_fixed_update(update: np.ndarray, state: np.ndarray) -> np.ndarray:
    return update @ state


def direct_two_use(carrier: FourMenuCarrier) -> np.ndarray:
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
    return tensor.reshape(
        PROGRAM_DIMENSION * POINTER_DIMENSION**2 * 2,
        PROGRAM_DIMENSION * 2,
    )


def compiler_controls(
    base: c385.EffectSystem,
    compiled: c390.CompiledMenus,
    carrier: FourMenuCarrier,
    actual_contact: np.ndarray,
    host_row_residual: float,
) -> dict[str, object]:
    target_residual = max(
        float(np.linalg.norm(effect - target))
        for program, targets in zip(compiled.programs, compiled.target_effects)
        for effect, target in zip(program.coarse_effects, targets)
    )
    completeness_residual = max(
        float(np.linalg.norm(program.completeness - I2))
        for program in compiled.programs
    )
    pointer_outcomes = sum(len(program.kraus) for program in compiled.programs)
    identity_reuse_failures = sum(
        compiled.programs[program].kraus[outcome]
        is not compiled.unique_blocks[class_index]
        for program, row in enumerate(compiled.class_rows)
        for outcome, class_index in enumerate(row)
    )
    process_by_class: dict[int, list[np.ndarray]] = {}
    process_keys = []
    for program, row in zip(compiled.programs, compiled.class_rows):
        for operator, class_index in zip(program.kraus, row):
            choi = c321.choi((operator,))
            process_by_class.setdefault(class_index, []).append(choi)
            process_keys.append(c383.matrix_key(choi))
    same_class_process_residual = max(
        float(np.linalg.norm(choi - group[0]))
        for group in process_by_class.values()
        for choi in group
    )

    update = carrier.update
    tensor = update.reshape(8, 8, 2, 8, 2)
    block_residual = off_diagonal = 0.0
    for output_label in range(PROGRAM_DIMENSION):
        for input_label in range(PROGRAM_DIMENSION):
            block = tensor[output_label, :, :, input_label, :].reshape(16, 2)
            if output_label == input_label:
                expected = c317.stack_isometry(carrier.block_kraus[input_label])
                block_residual = max(block_residual, float(np.linalg.norm(block - expected)))
            else:
                off_diagonal = max(off_diagonal, float(np.linalg.norm(block)))

    amplitudes = np.asarray((1, 1j, -1, 2j, 0, 0, 0, 0), dtype=complex)
    amplitudes /= np.linalg.norm(amplitudes)
    system = np.asarray((1, 1j), dtype=complex) / np.sqrt(2)
    output = apply_fixed_update(update, np.kron(amplitudes, system)).reshape(8, 8, 2)
    expected = np.zeros_like(output)
    for label in range(LAWFUL_PROGRAMS):
        for pointer, operator in enumerate(carrier.block_kraus[label]):
            expected[label, pointer] = amplitudes[label] * operator @ system
    coherent_residual = float(np.linalg.norm(output - expected))

    sequential = c323.two_use_from_fixed(update)
    direct = direct_two_use(carrier)
    deleted_compilation = compile_additional(base, compiled.class_rows, I2)
    deleted_carrier = FourMenuCarrier(deleted_compilation.programs)
    contact_update_residual = float(np.linalg.norm(update - deleted_carrier.update))
    contact_effect_residual = max(
        float(np.linalg.norm(left - right))
        for actual, deleted in zip(compiled.programs, deleted_compilation.programs)
        for left, right in zip(actual.coarse_effects, deleted.coarse_effects)
    )
    contact_process_residual = max(
        float(np.linalg.norm(c321.choi((actual,)) - c321.choi((deleted,))))
        for actual_program, deleted_program in zip(
            compiled.programs, deleted_compilation.programs
        )
        for actual, deleted in zip(actual_program.kraus, deleted_program.kraus)
    )
    detail = {
        "programs": len(compiled.programs),
        "outcome_counts": tuple(map(len, compiled.class_rows)),
        "unique_effect_blocks": len(compiled.unique_blocks),
        "pointer_outcomes": pointer_outcomes,
        "reused_block_occurrences": pointer_outcomes - len(compiled.unique_blocks),
        "block_object_reuse_failures": identity_reuse_failures,
        "maximum_target_effect_recovery_residual": target_residual,
        "maximum_program_completeness_residual": completeness_residual,
        "landed_host_merge_row_residual": host_row_residual,
        "unique_coarse_CP_process_tags": len(set(process_keys)),
        "maximum_same_class_process_tag_residual": same_class_process_residual,
        "program_M2": PROGRAM_M2,
        "pointer_M2": POINTER_M2,
        "lawful_program_states": LAWFUL_PROGRAMS,
        "idle_extension_states": PROGRAM_DIMENSION - LAWFUL_PROGRAMS,
        "fixed_update_isometry_residual": float(np.linalg.norm(
            update.conj().T @ update - np.eye(PROGRAM_DIMENSION * 2)
        )),
        "controlled_block_recovery_residual": block_residual,
        "off_diagonal_program_write_residual": off_diagonal,
        "coherent_program_superposition_residual": coherent_residual,
        "two_use_fixed_vs_direct_residual": float(np.linalg.norm(sequential - direct)),
        "two_use_isometry_residual": float(np.linalg.norm(
            sequential.conj().T @ sequential - np.eye(PROGRAM_DIMENSION * 2)
        )),
        "contact_deletion_update_residual": contact_update_residual,
        "contact_deletion_effect_residual": contact_effect_residual,
        "contact_deletion_process_residual": contact_process_residual,
        "actual_contact_is_unitary_residual": float(np.linalg.norm(
            actual_contact.conj().T @ actual_contact - I2
        )),
        "fixed_update_application_source": " ".join(getsource(apply_fixed_update).split()),
        "host_program_branch_query": False,
    }
    check(
        "four higher-outcome presentations compile into one fixed contact-sensitive carrier with exact block reuse",
        detail["programs"] == 4
        and detail["outcome_counts"] == (5, 5, 5, 7)
        and detail["unique_effect_blocks"] == 11
        and pointer_outcomes == 22
        and detail["reused_block_occurrences"] == 11
        and identity_reuse_failures == 0
        and target_residual < TOL
        and completeness_residual < TOL
        and host_row_residual < TOL
        and detail["unique_coarse_CP_process_tags"] == 11
        and same_class_process_residual < TOL
        and detail["lawful_program_states"] == 4
        and detail["idle_extension_states"] == 4
        and detail["fixed_update_isometry_residual"] < TOL
        and block_residual < TOL
        and off_diagonal < TOL
        and coherent_residual < TOL
        and detail["two_use_fixed_vs_direct_residual"] < TOL
        and detail["two_use_isometry_residual"] < TOL
        and contact_update_residual > 0.7
        and contact_effect_residual < TOL
        and contact_process_residual > 0.2
        and detail["actual_contact_is_unitary_residual"] < TOL
        and detail["fixed_update_application_source"].endswith("return update @ state")
        and not detail["host_program_branch_query"],
        detail,
    )
    return detail


def additional_presentations(
    compiled: c390.CompiledMenus,
) -> tuple[c385.MenuPresentation, ...]:
    return tuple(
        c385.MenuPresentation(
            name=f"Cycle394-fixed-carrier/{index}/{ROW_SOURCES[index]}/coarse",
            carrier="Cycle394-four-menu-fixed-carrier",
            program_index=index,
            surface="compiled-coarse",
            provenance="Cycle394 current campaign supplied row and fixed carrier",
            effects=tuple(program.coarse_effects),
        )
        for index, program in enumerate(compiled.programs)
    )


def incidence_controls(
    base: c385.EffectSystem,
    prior: c390.CompiledMenus,
    additional: c390.CompiledMenus,
) -> dict[str, object]:
    prior_menus = c390.compiled_menu_presentations(prior)
    new_menus = additional_presentations(additional)
    prior_system = c385.build_effect_system(
        base.menus + prior_menus, effect_functionality_premise=True
    )
    installed = c385.build_effect_system(
        base.menus + prior_menus + new_menus,
        effect_functionality_premise=True,
    )
    base_rank = c385.matrix_rank(base.incidence)
    prior_rank = c385.matrix_rank(prior_system.incidence)
    installed_rank = c385.matrix_rank(installed.incidence)
    new_rows = installed.incidence[-len(new_menus):]
    all_overlap_start = len(base.menus)
    all_deletion_ranks = tuple(
        c385.matrix_rank(np.delete(installed.incidence, row, axis=0))
        for row in range(all_overlap_start, len(installed.menus))
    )
    new_deletion_ranks = all_deletion_ranks[-len(new_menus):]
    trace_grade = np.asarray([
        float(np.trace(effect).real / 2) for effect in installed.effects
    ])
    detail = {
        "base_menus": len(base.menus),
        "Cycle390_menus": len(prior_menus),
        "Cycle394_menus": len(new_menus),
        "installed_menus": len(installed.menus),
        "effect_classes_before": len(base.effects),
        "effect_classes_after": len(installed.effects),
        "rank_before_Cycle390": base_rank,
        "rank_after_Cycle390": prior_rank,
        "rank_after_Cycle394": installed_rank,
        "Cycle394_rank_gain": installed_rank - prior_rank,
        "total_overlap_rank_gain": installed_rank - base_rank,
        "new_rows_independent_modulo_Cycle390": c385.matrix_rank(np.vstack((
            prior_system.incidence, new_rows
        ))) - prior_rank,
        "all_overlap_row_deletion_ranks": all_deletion_ranks,
        "Cycle394_row_deletion_ranks": new_deletion_ranks,
        "trace_normalization_residual": float(np.linalg.norm(
            installed.incidence @ trace_grade - 1
        )),
        "trace_grade_minimum": float(np.min(trace_grade)),
        "effect_functionality_premise_supplied": True,
        "numerical_grade_selected": False,
    }
    check(
        "the four additional physical menus preserve 55 classes and raise installed incidence rank from 27 to 31",
        prior_system.incidence.shape == (43, 55)
        and installed.incidence.shape == (47, 55)
        and base_rank == 20
        and prior_rank == 27
        and installed_rank == 31
        and detail["Cycle394_rank_gain"] == 4
        and detail["total_overlap_rank_gain"] == 11
        and detail["new_rows_independent_modulo_Cycle390"] == 4
        and all_deletion_ranks == (30,) * 11
        and new_deletion_ranks == (30,) * 4
        and detail["trace_normalization_residual"] < TOL
        and detail["trace_grade_minimum"] > 0.05
        and detail["effect_functionality_premise_supplied"]
        and not detail["numerical_grade_selected"],
        detail,
    )
    return {**detail, "system": installed}


def held_corpus_controls(carrier: FourMenuCarrier) -> dict[str, object]:
    schedule = (0, 1, 2, 3, 3, 2, 1, 0, 0, 2, 1, 3)
    outputs = []
    for label, rho in zip(schedule, c321.held_states()):
        basis = program_basis(label)
        input_density = np.kron(np.outer(basis, basis.conj()), rho)
        outputs.append(carrier.update @ input_density @ carrier.update.conj().T)
    trace_residual = max(abs(float(np.trace(output).real) - 1) for output in outputs)
    hermitian_residual = max(float(np.linalg.norm(output - output.conj().T)) for output in outputs)
    minimum_eigenvalue = min(float(np.min(np.linalg.eigvalsh(output))) for output in outputs)
    digest = sha256()
    for label, output in zip(schedule, outputs):
        digest.update(bytes((label,)))
        for value in output.reshape(-1):
            digest.update(f"{value.real:.13f},{value.imag:.13f};".encode())
    detail = {
        "held_L": 6,
        "held_N": len(outputs),
        "program_schedule": schedule,
        "distinct_program_labels_seen": len(set(schedule)),
        "maximum_trace_residual": trace_residual,
        "maximum_Hermitian_residual": hermitian_residual,
        "minimum_output_density_eigenvalue": minimum_eigenvalue,
        "held_output_hash": digest.hexdigest(),
        "held_outputs_are_Records": False,
        "held_outputs_are_occurrences": False,
        "held_outputs_are_frequency_samples": False,
    }
    check(
        "held L6 N12 density controls exercise every lawful program without Record or frequency promotion",
        len(outputs) == 12
        and len(set(schedule)) == 4
        and trace_residual < TOL
        and hermitian_residual < TOL
        and minimum_eigenvalue > -TOL
        and len(detail["held_output_hash"]) == 64
        and not detail["held_outputs_are_Records"]
        and not detail["held_outputs_are_occurrences"]
        and not detail["held_outputs_are_frequency_samples"],
        detail,
    )
    return detail


def physical_controls(
    fixtures: dict[int, c317.PhysicalFixture],
    carrier: FourMenuCarrier,
    installed: c385.EffectSystem,
) -> dict[str, object]:
    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        support = c323.physical_embedding_and_support_controls(fixtures, carrier)
        covariance = c323.covariance_controls(fixtures, carrier)
    inherited_checks = (c323.PASS, c323.FAIL)
    c323.PASS, c323.FAIL = old_pass, old_fail
    held = next(row for row in support if row["held"])

    frames = c317.c311.c235.proper_cubic_frames()
    incidence_failures = 0
    maximum_rotated_completeness = 0.0
    for frame in frames:
        rotated_menus = tuple(c385.MenuPresentation(
            menu.name,
            menu.carrier,
            menu.program_index,
            menu.surface,
            menu.provenance,
            tuple(c385.rotate_effect(effect, frame) for effect in menu.effects),
        ) for menu in installed.menus)
        rotated = c385.build_effect_system(
            rotated_menus, effect_functionality_premise=True
        )
        incidence_failures += int(
            rotated.incidence.shape != installed.incidence.shape
            or not np.array_equal(rotated.incidence, installed.incidence)
            or c385.matrix_rank(rotated.incidence) != c385.matrix_rank(installed.incidence)
        )
        maximum_rotated_completeness = max(
            maximum_rotated_completeness,
            max(float(np.linalg.norm(sum(
                menu.effects, start=np.zeros((2, 2), dtype=complex)
            ) - I2)) for menu in rotated_menus),
        )
    species = c317.c311.c219.common_species(-0.3)
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    contact_intertwiner = max(float(np.linalg.norm(
        fixture.physical_contact @ fixture.two_ray_encoding
        - fixture.two_ray_encoding @ fixture.contact
    )) for fixture in fixtures.values())
    detail = {
        "imported_physical_checks": inherited_checks,
        "E_G_intertwiner_rows": tuple({
            "L": row["L"],
            "held": row["held"],
            "E_G_logical_minus_G_physical_E": row[
                "logical_to_physical_carrier_residual"
            ],
            "physical_isometry_residual": row["physical_carrier_isometry_residual"],
        } for row in support),
        "held_L6_leakage": held["one_and_two_use_leakage"],
        "held_L6_constraint_residual": held["role_constraint_residual"],
        "matrix_unit_pairs": held["matrix_unit_pairs"],
        "maximum_matter_transition_M2": held["maximum_matter_transition_M2"],
        "maximum_one_use_controlled_M2": held["maximum_one_use_controlled_M2"],
        "maximum_two_use_controlled_M2": held["maximum_two_use_controlled_M2"],
        "one_use_patch_M2": held["one_use_patch_M2"],
        "two_use_patch_M2": held["two_use_patch_M2"],
        "two_use_installed_overhead_M2_per_cell": held[
            "two_use_installed_overhead_M2_per_cell"
        ],
        "port_constraint_failures": held["port_constraint_failures"],
        "local_check_or_Wilson_failures": held["local_check_or_Wilson_failures"],
        "proper_cubic_frames": covariance["frames"],
        "physical_frame_branch_failures": covariance["branch_failures"],
        "maximum_physical_one_use_frame_residual": covariance[
            "maximum_one_use_carrier_residual"
        ],
        "maximum_physical_two_use_frame_residual": covariance[
            "maximum_two_use_carrier_residual"
        ],
        "incidence_frame_failures": incidence_failures,
        "maximum_rotated_menu_completeness_residual": maximum_rotated_completeness,
        "one_particle_mass_relative_residual": mass_residual,
        "physical_contact_intertwiner_residual": contact_intertwiner,
    }
    check(
        "E G_logical = G_physical E holds at L3/held L6 with bounded support, constraints, mass/contact, and 24 frames",
        inherited_checks == (2, 0)
        and all(
            row["E_G_logical_minus_G_physical_E"] < TOL
            and row["physical_isometry_residual"] < TOL
            for row in detail["E_G_intertwiner_rows"]
        )
        and detail["held_L6_leakage"] < TOL
        and detail["held_L6_constraint_residual"] < TOL
        and detail["matrix_unit_pairs"] == 16
        and detail["maximum_matter_transition_M2"] <= 20
        and detail["maximum_one_use_controlled_M2"] <= 26
        and detail["maximum_two_use_controlled_M2"] <= 29
        and detail["one_use_patch_M2"] == 62
        and detail["two_use_patch_M2"] == 65
        and detail["two_use_installed_overhead_M2_per_cell"] == 32
        and detail["port_constraint_failures"] == 0
        and detail["local_check_or_Wilson_failures"] == 0
        and detail["proper_cubic_frames"] == 24
        and detail["physical_frame_branch_failures"] == 0
        and detail["maximum_physical_one_use_frame_residual"] < TOL
        and detail["maximum_physical_two_use_frame_residual"] < TOL
        and incidence_failures == 0
        and maximum_rotated_completeness < TOL
        and mass_residual < 3e-12
        and contact_intertwiner < TOL,
        detail,
    )
    return detail


def deletion_and_domain_controls(
    base: c385.EffectSystem,
    compiled: c390.CompiledMenus,
    carrier: FourMenuCarrier,
    installed: c385.EffectSystem,
) -> dict[str, object]:
    branch_defects = []
    for program in compiled.programs:
        completeness = sum(
            (operator.conj().T @ operator for operator in program.kraus[:-1]),
            start=np.zeros((2, 2), dtype=complex),
        )
        branch_defects.append(float(np.linalg.norm(completeness - I2)))
    tensor = carrier.update.reshape(8, 8, 2, 8, 2).copy()
    tensor[3, :, :, 3, :] = 0
    deleted_control = tensor.reshape(128, 16)
    control_defect = float(np.linalg.norm(
        deleted_control.conj().T @ deleted_control - np.eye(16), 2
    ))
    invalid_program = c321.Program("nonexhaustive", (0.5 * I2,), ((0,),))
    invalid_calls = (
        lambda: FourMenuCarrier(compiled.programs[:3]),
        lambda: FourMenuCarrier(compiled.programs + (compiled.programs[0],)),
        lambda: FourMenuCarrier(compiled.programs[:3] + (compiled.programs[0],)),
        lambda: FourMenuCarrier(compiled.programs[:3] + (invalid_program,)),
        lambda: program_basis(4),
        lambda: validate_program_state(np.eye(8)[4]),
        lambda: validate_program_state(np.ones(8)),
        lambda: validate_pointer_blank(1),
        lambda: c390.positive_square_root(np.asarray([[1, 1], [0, 0]], dtype=complex)),
        lambda: c390.positive_square_root(-0.1 * I2),
        lambda: compile_additional(base, ADDITIONAL_CLASS_ROWS[:-1], I2),
    )
    rejected = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError, IndexError):
            rejected += 1
    overlap_start = len(base.menus)
    deletion_ranks = tuple(
        c385.matrix_rank(np.delete(installed.incidence, row, axis=0))
        for row in range(overlap_start, len(installed.menus))
    )
    detail = {
        "compiled_fine_branch_deletions": len(branch_defects),
        "minimum_branch_deletion_completeness_defect": min(branch_defects),
        "program_control_block_deletion_isometry_defect": control_defect,
        "all_overlap_menu_row_deletion_ranks": deletion_ranks,
        "domain_rejections": rejected,
        "domain_attempts": len(invalid_calls),
    }
    check(
        "branch, control, and menu-row deletions are visible and malformed table/carrier/state/pointer/effect domains reject",
        len(branch_defects) == 4
        and min(branch_defects) > 0.1
        and control_defect > 0.99
        and deletion_ranks == (30,) * 11
        and rejected == len(invalid_calls),
        detail,
    )
    return detail


def provenance_and_inventory_controls() -> dict[str, object]:
    with redirect_stdout(StringIO()):
        lineage = c381.campaign_lineage_status_controls()
    detail = {
        "landed_in_pinned_main_base": (
            "Cycle317 bounded physical dilation/compiler",
            "Cycle321 finite effects/programs and process separators",
            "Cycle323 three-M2 fixed-carrier physical embedding",
        ),
        "campaign_349_351_commit": lineage["campaign_corpus_commit"],
        "pinned_main_base_commit": lineage["pinned_main_base_commit"],
        "campaign_commit_is_pinned_main_base_ancestor": lineage[
            "campaign_commit_is_pinned_main_base_ancestor"
        ],
        "Cycle381_383_385_390_394_status": "campaign inputs or outputs at construction",
        "future_landing_allowed": lineage["future_landing_allowed"],
        "supplied_Cycle390_rows": c390.EXPECTED_CLASS_ROWS,
        "supplied_Cycle394_rows": ADDITIONAL_CLASS_ROWS,
        "supplied_row_sources": ROW_SOURCES,
        "supplied_effect_functionality_premise": True,
        "supplied_host_components_grouping_and_invocation": True,
        "supplied_candidate_search_and_selection": True,
        "supplied_positive_root_compiler_choice": True,
        "supplied_contact_postcomposition": True,
        "supplied_program_state_preparation": True,
        "supplied_pointer_blank": True,
        "supplied_frame_transport": True,
        "supplied_M2_embedding_constraints_and_size_fixtures": True,
        "supplied_one_particle_mass_and_contact_fixtures": True,
        "autonomous_program_or_menu_genesis": None,
        "universal_menu_eligibility": False,
        "selected_numerical_grade": None,
        "Born_selection": None,
        "probability_interpretation": None,
        "actual_history_sampler": None,
        "Record_formation": None,
        "frequency_theorem": None,
        "global_obstruction_claim": None,
        "minimum_content_claim": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "status split and supplied-structure inventory are explicit without statistical or constitutional promotion",
        not detail["campaign_commit_is_pinned_main_base_ancestor"]
        and detail["future_landing_allowed"]
        and len(detail["supplied_Cycle390_rows"]) == 7
        and len(detail["supplied_Cycle394_rows"]) == 4
        and detail["supplied_effect_functionality_premise"]
        and detail["supplied_host_components_grouping_and_invocation"]
        and detail["supplied_candidate_search_and_selection"]
        and detail["supplied_positive_root_compiler_choice"]
        and detail["supplied_contact_postcomposition"]
        and detail["supplied_program_state_preparation"]
        and detail["supplied_pointer_blank"]
        and detail["supplied_frame_transport"]
        and detail["supplied_M2_embedding_constraints_and_size_fixtures"]
        and detail["supplied_one_particle_mass_and_contact_fixtures"]
        and detail["autonomous_program_or_menu_genesis"] is None
        and not detail["universal_menu_eligibility"]
        and detail["selected_numerical_grade"] is None
        and detail["Born_selection"] is None
        and detail["probability_interpretation"] is None
        and detail["actual_history_sampler"] is None
        and detail["Record_formation"] is None
        and detail["frequency_theorem"] is None
        and detail["global_obstruction_claim"] is None
        and detail["minimum_content_claim"] is None
        and detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 394: PHYSICAL HIGHER-OUTCOME OVERLAP-MENU FIXED CARRIER")
    print("authority=none; audit=unset; constructive rank gain 27->31")
    note = note_contract()
    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        fixtures = c323.physical_fixture_controls()
    fixture_checks = (c323.PASS, c323.FAIL)
    c323.PASS, c323.FAIL = old_pass, old_fail
    base, prior, additional, host_row_residual = candidate_source(fixtures)
    carrier = FourMenuCarrier(additional.programs)
    compiler = compiler_controls(
        base, additional, carrier, fixtures[3].contact, host_row_residual
    )
    incidence = incidence_controls(base, prior, additional)
    held = held_corpus_controls(carrier)
    physical = physical_controls(fixtures, carrier, incidence["system"])
    attacks = deletion_and_domain_controls(
        base, additional, carrier, incidence["system"]
    )
    provenance = provenance_and_inventory_controls()
    check(
        "Cycle 394 physically installs four further independent overlap presentations with exact rank and physical controls",
        not note["missing"]
        and fixture_checks == (1, 0)
        and compiler["programs"] == 4
        and compiler["fixed_update_isometry_residual"] < TOL
        and incidence["rank_after_Cycle394"] == 31
        and incidence["Cycle394_rank_gain"] == 4
        and held["held_N"] == 12
        and physical["proper_cubic_frames"] == 24
        and attacks["domain_rejections"] == attacks["domain_attempts"]
        and provenance["selected_numerical_grade"] is None
        and provenance["global_obstruction_claim"] is None
        and provenance["minimum_content_claim"] is None
        and provenance["axiom_pressure"] is None,
        {
            "disposition": "exact bounded constructive four-menu physical extension",
            "strongest_positive": "the fixed physical menu system has 47 presentations, 55 effect classes, and rank 31",
            "new_row_types": "one host merge, two five-outcome overlaps, one seven-outcome overlap",
            "all_overlap_row_deletion_rank": 30,
            "claim_boundary": "finite installed incidence and physical compiler only",
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_HIGHER_OUTCOME_OVERLAP_MENU_FIXED_CARRIER_OPEN")
        return 1
    print("RESULT PHYSICAL_HIGHER_OUTCOME_OVERLAP_MENU_FIXED_CARRIER_EXACT_RANK_GAIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
