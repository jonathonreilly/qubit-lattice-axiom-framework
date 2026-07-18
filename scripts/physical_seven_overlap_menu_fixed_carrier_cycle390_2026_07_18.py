#!/usr/bin/env python3
"""Cycle 390: compile seven overlap menus into one fixed physical carrier.

The seven independent Cycle-385 candidate rows are rebuilt from the exact
Cycle-381 effect classes.  Nineteen unique effect blocks are compiled once by
the contact-postcomposed positive-square-root dilation and reused across 26
pointer outcomes.  One three-M2 program register stores seven lawful programs
plus one idle state; one three-M2 pointer register supplies up to eight local
outcomes.  The resulting fixed isometry is embedded in the landed
Cycle-317/321/323 M2 substrate and tested at L3 and held L6.

Only successfully compiled menus are added to the physical incidence system.
Rank growth and the remaining positive affine dimension are finite facts, not
a minimum-content theorem, nonforcing result, Born selection, no-go, or axiom
pressure.  No pointer or normalized vector is promoted to probability,
actuality, a Record, sampling, or frequency.  Authority is none; audit unset.
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
    "PHYSICAL_SEVEN_OVERLAP_MENU_FIXED_CARRIER_CYCLE390_NOTE_2026-07-18.md"
)

import physical_menu_overlap_grade_identifiability_tournament_cycle385_2026_07_18 as c385


c381 = c385.c381
c383 = c385.c383
c323 = c381.c323
c321 = c381.c321
c317 = c381.c317
TOL = 1.2e-10
I2 = c381.I2
PROGRAM_M2 = 3
PROGRAM_DIMENSION = 2**PROGRAM_M2
LAWFUL_PROGRAMS = 7
POINTER_M2 = 3
POINTER_DIMENSION = 2**POINTER_M2
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0


EXPECTED_CLASS_ROWS = (
    (29, 30, 34),
    (33, 53, 54),
    (0, 0, 25, 28),
    (2, 2, 24, 28),
    (16, 36, 36, 41),
    (17, 18, 35, 35),
    (37, 38, 41, 41),
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
        check("the Cycle-390 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    required = (
        "authority: none",
        "audit: unset",
        "seven lawful programs plus one idle state",
        "three-m2 program register",
        "three-m2 pointer register",
        "19 unique effect blocks",
        "26 pointer outcomes",
        "contact-postcomposed positive-square-root dilation",
        "one fixed controlled isometry",
        "no host program branch query",
        "e g_logical = g_physical e",
        "rank rises from 20 to 27",
        "positive affine dimension is 28",
        "held l=6, n=12",
        "all 24 proper-cubic frames",
        "one-particle mass fixture",
        "coefficients and class table remain supplied",
        "program-state preparation remains supplied",
        "blank pointer remains supplied",
        "program and menu genesis remain supplied",
        "pointer output is not a record",
        "no probability, actuality, sampler, or frequency promotion",
        "n1 — alternative route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "gate disposition: fail for any negative or nonforcing claim",
        "no minimum, global born failure, or axiom pressure",
    )
    text = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the seven-menu physical compiler, incidence gain, imports, provenance, semantic firewall, and N1-N8 gate",
        not missing,
        missing,
    )
    return {"missing": missing}


def positive_square_root(effect: np.ndarray) -> np.ndarray:
    array = np.asarray(effect, dtype=complex)
    if array.shape != (2, 2) or np.linalg.norm(array - array.conj().T) >= TOL:
        raise ValueError("a compiled effect must be one Hermitian qubit block")
    eigenvalues, eigenvectors = np.linalg.eigh((array + array.conj().T) / 2)
    if eigenvalues[0] < -TOL or eigenvalues[-1] > 1 + TOL:
        raise ValueError("a compiled effect lies outside the positive unit interval")
    return (
        eigenvectors * np.sqrt(np.clip(eigenvalues, 0, None))
    ) @ eigenvectors.conj().T


def candidate_source(
    fixtures: dict[int, c317.PhysicalFixture],
) -> tuple[
    c385.EffectSystem,
    tuple[tuple[int, ...], ...],
    dict[str, c323.FixedProgramCarrier],
    dict[str, tuple[c381.c349.MenuSchema, ...]],
]:
    menus, carriers, tables = c385.installed_menus(fixtures)
    base = c385.build_effect_system(menus, effect_functionality_premise=True)
    with redirect_stdout(StringIO()):
        candidates = c385.candidate_augmenting_menu_controls(base)
    class_rows = tuple(
        tuple(row["classes"]) for row in candidates["independent_candidate_rows"]
    )
    if class_rows != EXPECTED_CLASS_ROWS:
        raise ValueError("the Cycle-385 independent candidate table changed")
    return base, class_rows, carriers, tables


@dataclass(frozen=True)
class CompiledMenus:
    class_rows: tuple[tuple[int, ...], ...]
    unique_blocks: dict[int, np.ndarray]
    programs: tuple[c321.Program, ...]
    target_effects: tuple[tuple[np.ndarray, ...], ...]


def compile_menus(
    base: c385.EffectSystem,
    class_rows: tuple[tuple[int, ...], ...],
    contact: np.ndarray,
) -> CompiledMenus:
    if contact.shape != (2, 2) or np.linalg.norm(contact.conj().T @ contact - I2) >= TOL:
        raise ValueError("the compiler needs the actual unitary two-ray contact")
    unique_classes = tuple(sorted({index for row in class_rows for index in row}))
    unique_blocks = {
        index: contact @ positive_square_root(base.effects[index])
        for index in unique_classes
    }
    programs = []
    targets = []
    for program_index, row in enumerate(class_rows):
        effects = tuple(base.effects[index] for index in row)
        program = c321.Program(
            f"Cycle390 overlap menu {program_index}",
            tuple(unique_blocks[index] for index in row),
            tuple((pointer,) for pointer in range(len(row))),
        )
        if np.linalg.norm(program.completeness - I2) >= TOL:
            raise ValueError("a candidate row failed exhaustive compilation")
        programs.append(program)
        targets.append(effects)
    return CompiledMenus(class_rows, unique_blocks, tuple(programs), tuple(targets))


def padded_kraus(program: c321.Program) -> tuple[np.ndarray, ...]:
    return program.kraus + tuple(
        np.zeros((2, 2), dtype=complex)
        for _ in range(POINTER_DIMENSION - len(program.kraus))
    )


@dataclass(frozen=True)
class SevenMenuCarrier:
    programs: tuple[c321.Program, ...]

    def __post_init__(self) -> None:
        if len(self.programs) != LAWFUL_PROGRAMS:
            raise ValueError("the declared code requires exactly seven programs")
        if len({program.name for program in self.programs}) != LAWFUL_PROGRAMS:
            raise ValueError("lawful program names must be distinct")
        if any(
            len(program.kraus) > POINTER_DIMENSION
            or np.linalg.norm(program.completeness - I2) >= TOL
            for program in self.programs
        ):
            raise ValueError("every program must fit and be exhaustive")

    @property
    def block_kraus(self) -> tuple[tuple[np.ndarray, ...], ...]:
        idle = (I2,) + tuple(
            np.zeros((2, 2), dtype=complex)
            for _ in range(POINTER_DIMENSION - 1)
        )
        return tuple(padded_kraus(program) for program in self.programs) + (idle,)

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
        raise ValueError("program label is outside the seven-state code")
    state = np.zeros(PROGRAM_DIMENSION, dtype=complex)
    state[label] = 1
    return state


def validate_program_state(state: np.ndarray) -> None:
    if state.shape != (PROGRAM_DIMENSION,) or abs(np.linalg.norm(state) - 1) >= TOL:
        raise ValueError("program preparation must be one normalized three-M2 state")
    if np.linalg.norm(state[LAWFUL_PROGRAMS:]) >= TOL:
        raise ValueError("program preparation leaves the seven-state code")


def validate_pointer_blank(label: int) -> None:
    if label != 0:
        raise ValueError("the fixed dilation requires the supplied blank pointer")


def apply_fixed_update(update: np.ndarray, state: np.ndarray) -> np.ndarray:
    return update @ state


def direct_two_use(carrier: SevenMenuCarrier) -> np.ndarray:
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


def compiler_and_fixed_carrier_controls(
    base: c385.EffectSystem,
    compiled: CompiledMenus,
    carrier: SevenMenuCarrier,
    actual_contact: np.ndarray,
) -> dict[str, object]:
    effect_residual = max(
        float(np.linalg.norm(effect - target))
        for program, targets in zip(compiled.programs, compiled.target_effects)
        for effect, target in zip(program.coarse_effects, targets)
    )
    completeness_residual = max(
        float(np.linalg.norm(program.completeness - I2))
        for program in compiled.programs
    )
    pointer_outcomes = sum(len(program.kraus) for program in compiled.programs)
    reused_outcomes = pointer_outcomes - len(compiled.unique_blocks)
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
    maximum_same_class_process_residual = max(
        float(np.linalg.norm(choi - group[0]))
        for group in process_by_class.values()
        for choi in group
    )

    update = carrier.update
    tensor = update.reshape(
        PROGRAM_DIMENSION,
        POINTER_DIMENSION,
        2,
        PROGRAM_DIMENSION,
        2,
    )
    block_residual = 0.0
    off_diagonal = 0.0
    for output_label in range(PROGRAM_DIMENSION):
        for input_label in range(PROGRAM_DIMENSION):
            block = tensor[output_label, :, :, input_label, :].reshape(16, 2)
            if output_label == input_label:
                expected = c317.stack_isometry(carrier.block_kraus[input_label])
                block_residual = max(block_residual, float(np.linalg.norm(block - expected)))
            else:
                off_diagonal = max(off_diagonal, float(np.linalg.norm(block)))
    amplitudes = np.asarray((1, 1j, -1, 2j, 2, -1j, 3, 0), dtype=complex)
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
    identity_contact_compilation = compile_menus(
        base, compiled.class_rows, I2
    )
    identity_contact_carrier = SevenMenuCarrier(identity_contact_compilation.programs)
    contact_deletion_residual = float(np.linalg.norm(
        update - identity_contact_carrier.update
    ))
    contact_effect_residual = max(
        float(np.linalg.norm(left - right))
        for actual, deleted in zip(
            compiled.programs, identity_contact_compilation.programs
        )
        for left, right in zip(actual.coarse_effects, deleted.coarse_effects)
    )
    process_contact_residual = max(
        float(np.linalg.norm(c321.choi((actual,)) - c321.choi((deleted,))))
        for actual_program, deleted_program in zip(
            compiled.programs, identity_contact_compilation.programs
        )
        for actual, deleted in zip(actual_program.kraus, deleted_program.kraus)
    )
    source = " ".join(getsource(apply_fixed_update).split())
    detail = {
        "candidate_programs": len(compiled.programs),
        "unique_effect_blocks": len(compiled.unique_blocks),
        "pointer_outcomes": pointer_outcomes,
        "reused_block_occurrences": reused_outcomes,
        "block_object_reuse_failures": identity_reuse_failures,
        "maximum_target_effect_recovery_residual": effect_residual,
        "maximum_program_completeness_residual": completeness_residual,
        "unique_coarse_CP_process_tags": len(set(process_keys)),
        "maximum_same_class_process_tag_residual": maximum_same_class_process_residual,
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
        "contact_deletion_update_residual": contact_deletion_residual,
        "contact_deletion_effect_residual": contact_effect_residual,
        "contact_deletion_process_residual": process_contact_residual,
        "actual_contact_is_unitary_residual": float(np.linalg.norm(
            actual_contact.conj().T @ actual_contact - I2
        )),
        "fixed_update_application_source": source,
        "host_program_branch_query": False,
    }
    check(
        "nineteen exact effect blocks compile and reuse across 26 outcomes in one seven-program fixed contact-sensitive carrier",
        len(compiled.programs) == 7
        and len(compiled.unique_blocks) == 19
        and pointer_outcomes == 26
        and reused_outcomes == 7
        and identity_reuse_failures == 0
        and effect_residual < TOL
        and completeness_residual < TOL
        and detail["unique_coarse_CP_process_tags"] == 19
        and maximum_same_class_process_residual < TOL
        and detail["program_M2"] == detail["pointer_M2"] == 3
        and detail["lawful_program_states"] == 7
        and detail["idle_extension_states"] == 1
        and detail["fixed_update_isometry_residual"] < TOL
        and block_residual < TOL
        and off_diagonal < TOL
        and coherent_residual < TOL
        and detail["two_use_fixed_vs_direct_residual"] < TOL
        and detail["two_use_isometry_residual"] < TOL
        and contact_deletion_residual > 0.9
        and contact_effect_residual < TOL
        and process_contact_residual > 0.2
        and detail["actual_contact_is_unitary_residual"] < TOL
        and source.endswith("return update @ state")
        and not detail["host_program_branch_query"],
        detail,
    )
    return detail


def compiled_menu_presentations(
    compiled: CompiledMenus,
) -> tuple[c385.MenuPresentation, ...]:
    return tuple(
        c385.MenuPresentation(
            name=f"Cycle390-fixed-carrier/{index}/{program.name}/coarse",
            carrier="Cycle390-seven-menu-fixed-carrier",
            program_index=index,
            surface="compiled-coarse",
            provenance="Cycle390 current campaign fixed carrier",
            effects=tuple(program.coarse_effects),
        )
        for index, program in enumerate(compiled.programs)
    )


def installed_incidence_controls(
    base: c385.EffectSystem,
    compiled: CompiledMenus,
) -> dict[str, object]:
    physical_menus = compiled_menu_presentations(compiled)
    installed = c385.build_effect_system(
        base.menus + physical_menus,
        effect_functionality_premise=True,
    )
    base_rank = c385.matrix_rank(base.incidence)
    installed_rank = c385.matrix_rank(installed.incidence)
    trace_grade = np.asarray([
        float(np.trace(effect).real / 2) for effect in installed.effects
    ])
    trace_residual = float(np.linalg.norm(installed.incidence @ trace_grade - 1))
    left, right = next(
        (left, right)
        for left in range(len(installed.effects))
        for right in range(left + 1, len(installed.effects))
        if np.array_equal(installed.incidence[:, left], installed.incidence[:, right])
        and trace_grade[left] > 0
        and trace_grade[right] > 0
    )
    epsilon = min(trace_grade[left], trace_grade[right]) / 2
    alternative = trace_grade.copy()
    alternative[left] += epsilon
    alternative[right] -= epsilon
    alternative_residual = float(np.linalg.norm(
        installed.incidence @ alternative - 1
    ))
    bounds = c385.positive_bounds(installed.incidence)
    fixed = sum(abs(upper - lower) < TOL for lower, upper in bounds)
    zero_reachable = sum(abs(lower) < TOL for lower, _upper in bounds)
    compiled_rows = installed.incidence[-len(physical_menus):]
    deletion_ranks = tuple(
        c385.matrix_rank(np.delete(installed.incidence, row, axis=0))
        for row in range(len(base.menus), len(installed.menus))
    )
    detail = {
        "base_physical_menu_presentations": len(base.menus),
        "compiled_physical_menu_presentations": len(physical_menus),
        "installed_physical_menu_presentations": len(installed.menus),
        "effect_classes_before": len(base.effects),
        "effect_classes_after": len(installed.effects),
        "rank_before": base_rank,
        "rank_after": installed_rank,
        "installed_rank_gain": installed_rank - base_rank,
        "positive_affine_dimension": len(installed.effects) - installed_rank,
        "compiled_rows_are_independent_modulo_base": c385.matrix_rank(np.vstack((
            base.incidence, compiled_rows
        ))) - base_rank,
        "trace_grade_minimum": float(np.min(trace_grade)),
        "trace_normalization_residual": trace_residual,
        "alternative_identical_column_classes": (left, right),
        "alternative_perturbation_epsilon": float(epsilon),
        "alternative_grade_minimum": float(np.min(alternative)),
        "alternative_normalization_residual": alternative_residual,
        "positive_polytope_fixed_classes": fixed,
        "positive_polytope_zero_reachable_classes": zero_reachable,
        "compiled_row_deletion_ranks": deletion_ranks,
        "effect_functionality_premise_supplied": True,
        "numerical_grade_selected": False,
    }
    check(
        "only the seven compiled physical menus are installed; rank rises by seven while the positive affine dimension remains 28",
        installed.incidence.shape == (43, 55)
        and len(physical_menus) == 7
        and len(installed.effects) == len(base.effects) == 55
        and base_rank == 20
        and installed_rank == 27
        and detail["installed_rank_gain"] == 7
        and detail["positive_affine_dimension"] == 28
        and detail["compiled_rows_are_independent_modulo_base"] == 7
        and trace_residual < TOL
        and detail["trace_grade_minimum"] > 0.05
        and detail["alternative_grade_minimum"] > 0.025
        and alternative_residual < TOL
        and fixed == 3
        and zero_reachable == 52
        and deletion_ranks == (26,) * 7
        and detail["effect_functionality_premise_supplied"]
        and not detail["numerical_grade_selected"],
        detail,
    )
    return {**detail, "system": installed}


def held_corpus_controls(carrier: SevenMenuCarrier) -> dict[str, object]:
    schedule = (0, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2)
    states = c321.held_states()
    outputs = []
    for label, rho in zip(schedule, states):
        program_density = np.outer(program_basis(label), program_basis(label).conj())
        input_density = np.kron(program_density, rho)
        output_density = carrier.update @ input_density @ carrier.update.conj().T
        outputs.append(output_density)
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
        "the held L6 N12 grade-blind density corpus exercises all seven fixed programs without Record or frequency promotion",
        len(outputs) == 12
        and len(set(schedule)) == 7
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


def physical_embedding_frame_mass_controls(
    fixtures: dict[int, c317.PhysicalFixture],
    carrier: SevenMenuCarrier,
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
    species = c317.c311.c219.common_species(-0.3)
    mass_residual = abs(
        c317.c311.c219.rest_mass(species) / species.analytic_mass - 1
    )
    contact_intertwiner = max(float(np.linalg.norm(
        fixture.physical_contact @ fixture.two_ray_encoding
        - fixture.two_ray_encoding @ fixture.contact
    )) for fixture in fixtures.values())

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
        "E G_logical = G_physical E holds at L3/held L6 with bounded support, zero leakage, mass/contact preservation, and all 24 frames",
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
    compiled: CompiledMenus,
    carrier: SevenMenuCarrier,
    installed: c385.EffectSystem,
) -> dict[str, object]:
    branch_defects = []
    for program in compiled.programs:
        deleted = program.kraus[:-1]
        completeness = sum(
            (operator.conj().T @ operator for operator in deleted),
            start=np.zeros((2, 2), dtype=complex),
        )
        branch_defects.append(float(np.linalg.norm(completeness - I2)))
    tensor = carrier.update.reshape(8, 8, 2, 8, 2).copy()
    tensor[6, :, :, 6, :] = 0
    deleted_control = tensor.reshape(128, 16)
    control_defect = float(np.linalg.norm(
        deleted_control.conj().T @ deleted_control - np.eye(16), 2
    ))

    invalid_program = c321.Program(
        "nonexhaustive", (0.5 * I2,), ((0,),)
    )
    invalid_calls = (
        lambda: SevenMenuCarrier(compiled.programs[:6]),
        lambda: SevenMenuCarrier(compiled.programs + (compiled.programs[0],)),
        lambda: SevenMenuCarrier(compiled.programs[:6] + (invalid_program,)),
        lambda: SevenMenuCarrier(compiled.programs[:6] + (compiled.programs[0],)),
        lambda: program_basis(7),
        lambda: validate_program_state(np.eye(8)[7]),
        lambda: validate_program_state(np.ones(8)),
        lambda: validate_pointer_blank(1),
        lambda: positive_square_root(np.asarray([[1, 1], [0, 0]], dtype=complex)),
        lambda: positive_square_root(-0.1 * I2),
        lambda: compile_menus(base, compiled.class_rows[:-1], I2),
    )
    rejected = 0
    for call in invalid_calls:
        try:
            result = call()
            if isinstance(result, CompiledMenus) and len(result.programs) != 7:
                raise ValueError("candidate table has the wrong program count")
        except (TypeError, ValueError, IndexError):
            rejected += 1
    detail = {
        "compiled_fine_branch_deletions": len(branch_defects),
        "minimum_branch_deletion_completeness_defect": min(branch_defects),
        "program_control_block_deletion_isometry_defect": control_defect,
        "compiled_menu_row_deletion_rank": tuple(
            c385.matrix_rank(np.delete(installed.incidence, row, axis=0))
            for row in range(len(base.menus), len(installed.menus))
        ),
        "domain_rejections": rejected,
        "domain_attempts": len(invalid_calls),
    }
    check(
        "compiled branch/control/menu deletions are visible and malformed carrier, state, pointer, effect, and table domains reject",
        len(branch_defects) == 7
        and min(branch_defects) > 0.1
        and control_defect > 0.99
        and detail["compiled_menu_row_deletion_rank"] == (26,) * 7
        and rejected == len(invalid_calls),
        detail,
    )
    return detail


def provenance_and_semantic_controls() -> dict[str, object]:
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
        "Cycle381_383_385_390_are_campaign_inputs_or_outputs_at_construction": True,
        "future_landing_allowed": lineage["future_landing_allowed"],
        "supplied_class_table": EXPECTED_CLASS_ROWS,
        "supplied_positive_root_compiler_choice": True,
        "supplied_contact_postcomposition": True,
        "supplied_program_state_preparation": True,
        "supplied_pointer_blank": True,
        "autonomous_program_or_menu_genesis": None,
        "universal_menu_eligibility": False,
        "selected_numerical_grade": None,
        "probability_interpretation": None,
        "actual_history_sampler": None,
        "actual_member_selector": None,
        "Record_formation": None,
        "frequency_theorem": None,
        "N1_N8_negative_claim_gate": "FAIL; live constructive routes remain",
        "negative_or_nonforcing_claim_shipped": False,
        "no_go": None,
        "minimum_content_claim": None,
        "global_Born_failure": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "status-split provenance and all coefficient/table/program/pointer/genesis admissions are explicit without statistical or constitutional promotion",
        not detail["campaign_commit_is_pinned_main_base_ancestor"]
        and detail["Cycle381_383_385_390_are_campaign_inputs_or_outputs_at_construction"]
        and detail["future_landing_allowed"]
        and len(detail["supplied_class_table"]) == 7
        and detail["supplied_positive_root_compiler_choice"]
        and detail["supplied_contact_postcomposition"]
        and detail["supplied_program_state_preparation"]
        and detail["supplied_pointer_blank"]
        and detail["autonomous_program_or_menu_genesis"] is None
        and not detail["universal_menu_eligibility"]
        and detail["selected_numerical_grade"] is None
        and detail["probability_interpretation"] is None
        and detail["actual_history_sampler"] is None
        and detail["actual_member_selector"] is None
        and detail["Record_formation"] is None
        and detail["frequency_theorem"] is None
        and detail["N1_N8_negative_claim_gate"].startswith("FAIL")
        and not detail["negative_or_nonforcing_claim_shipped"]
        and detail["no_go"] is detail["minimum_content_claim"] is None
        and detail["global_Born_failure"] is detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 390: PHYSICAL SEVEN-OVERLAP-MENU FIXED CARRIER")
    print("authority=none; audit=unset; constructive rank gain; no Born promotion")
    note = note_contract()
    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        fixtures = c323.physical_fixture_controls()
    fixture_checks = (c323.PASS, c323.FAIL)
    c323.PASS, c323.FAIL = old_pass, old_fail
    base, class_rows, _base_carriers, _tables = candidate_source(fixtures)
    compiled = compile_menus(base, class_rows, fixtures[3].contact)
    carrier = SevenMenuCarrier(compiled.programs)
    compiler = compiler_and_fixed_carrier_controls(
        base, compiled, carrier, fixtures[3].contact
    )
    incidence = installed_incidence_controls(base, compiled)
    held = held_corpus_controls(carrier)
    physical = physical_embedding_frame_mass_controls(
        fixtures, carrier, incidence["system"]
    )
    attacks = deletion_and_domain_controls(
        base, compiled, carrier, incidence["system"]
    )
    provenance = provenance_and_semantic_controls()
    check(
        "Cycle 390 physically installs seven independent overlap menus with exact rank gain while leaving grade selection and all negative claims open",
        not note["missing"]
        and fixture_checks == (1, 0)
        and compiler["candidate_programs"] == 7
        and compiler["fixed_update_isometry_residual"] < TOL
        and incidence["installed_rank_gain"] == 7
        and incidence["positive_affine_dimension"] == 28
        and held["held_N"] == 12
        and physical["proper_cubic_frames"] == 24
        and attacks["domain_rejections"] == attacks["domain_attempts"]
        and provenance["selected_numerical_grade"] is None
        and not provenance["negative_or_nonforcing_claim_shipped"]
        and provenance["no_go"] is provenance["axiom_pressure"] is None,
        {
            "disposition": "exact bounded constructive seven-menu physical installation",
            "strongest_positive": "one fixed seven-program contact-sensitive M2 carrier raises installed finite-menu rank from 20 to 27",
            "remaining_finite_fact": "the 55-class installed incidence has positive affine dimension 28",
            "next_constructive_test": "compile additional higher-outcome, host-merge, rotated, or composed overlap menus and re-audit rank",
            "negative_or_Born_selection_claim": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_SEVEN_OVERLAP_MENU_FIXED_CARRIER_OPEN")
        return 1
    print("RESULT PHYSICAL_SEVEN_OVERLAP_MENU_FIXED_CARRIER_EXACT_RANK_GAIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
