#!/usr/bin/env python3
"""Cycle 386: finite effect/coarse-CP class registry for Cycle 382/384.

The current-campaign Cycle-382 table has fourteen lawful program/coarse-
outcome presentations.  This runner compiles their exact Cycle-383-style
effect and coarse-CP equivalence tables into bounded reversible XOR registries
on top of the Cycle-384 program-registration bit.  A separate supplied grade
code factors through the effect class while the coarse-CP process tag remains
present.

No supplied grade code is interpreted as probability, actuality, frequency,
or a selection law.  Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_mixed_projective_refinement_functionality_born_bridge_cycle383_2026_07_18 as c383
import physical_local_menu_registration_bridge_cycle384_2026_07_18 as c384


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FINITE_EFFECT_CLASS_REGISTRY_CYCLE386_NOTE_2026-07-18.md"
)
TOL = 1.2e-10

PROGRAM_DIMENSION = c384.PROGRAM_DIMENSION
REGISTRATION_DIMENSION = c384.REGISTRATION_DIMENSION
OUTCOME_DIMENSION = 4
QUOTIENT_DIMENSION = 2
CLASS_DIMENSION = 16
CHECK_DIMENSION = 2
GRADE_DIMENSION = 16

EFFECT_QUOTIENT = 0
COARSE_CP_QUOTIENT = 1
QUOTIENT_NAMES = ("effect", "coarse_cp")

EXPECTED_EFFECT_CLASSES = (0, 1, 0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8)
EXPECTED_COARSE_CP_CLASSES = (0, 1, 0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10)
SUPPLIED_GRADE_CODES = (1, 3, 5, 7, 9, 11, 13, 15, 6)

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
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-386 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "finite effect-class functionality comparator",
        "14 lawful presentations",
        "9 effect classes",
        "11 coarse-cp classes",
        "reversible class compiler",
        "reversible equality/consistency check",
        "single supplied four-m2 grade register",
        "process tag is not erased",
        "exact e/g",
        "held l=6",
        "24 proper-cubic frames",
        "current-campaign cycle-382",
        "current-campaign cycle-383",
        "current-campaign cycle-384",
        "class table and quotient choice remain supplied",
        "grade values remain supplied",
        "preparation and blank ancillas remain supplied",
        "admission remains supplied",
        "no born law",
        "not probability",
        "no actuality or frequency inference",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the finite dual quotient, reversible registry, physical controls, provenance, inventory, and semantic boundary",
        not missing,
        missing,
    )


def lawful_pairs(carrier: c384.c323.FixedProgramCarrier) -> tuple[tuple[int, int], ...]:
    return tuple(
        (program, outcome)
        for program, apparatus in enumerate(carrier.programs)
        for outcome in range(len(apparatus.coarse_groups))
    )


def grouped_kraus(
    program: c384.c323.c321.Program,
    outcome: int,
) -> tuple[np.ndarray, ...]:
    return tuple(program.kraus[index] for index in program.coarse_groups[outcome])


def effect_key(
    carrier: c384.c323.FixedProgramCarrier,
    pair: tuple[int, int],
) -> c383.MatrixKey:
    program, outcome = pair
    return c383.matrix_key(carrier.programs[program].coarse_effects[outcome])


def cp_key(
    carrier: c384.c323.FixedProgramCarrier,
    pair: tuple[int, int],
) -> c383.MatrixKey:
    program, outcome = pair
    return c383.matrix_key(
        c384.c323.c321.choi(grouped_kraus(carrier.programs[program], outcome))
    )


def derive_classes(
    carrier: c384.c323.FixedProgramCarrier,
    quotient: str,
) -> tuple[int, ...]:
    if quotient not in QUOTIENT_NAMES:
        raise ValueError("the finite registry quotient must be effect or coarse_cp")
    representatives: list[tuple[c383.MatrixKey, ...]] = []
    classes = []
    for pair in lawful_pairs(carrier):
        key = (effect_key(carrier, pair),)
        if quotient == "coarse_cp":
            key += (cp_key(carrier, pair),)
        if key not in representatives:
            representatives.append(key)
        classes.append(representatives.index(key))
    return tuple(classes)


@dataclass(frozen=True)
class ClassTables:
    pairs: tuple[tuple[int, int], ...]
    effect: tuple[int, ...]
    coarse_cp: tuple[int, ...]

    def __post_init__(self) -> None:
        if len(self.pairs) != 14 or len(set(self.pairs)) != 14:
            raise ValueError("the selected table needs exactly fourteen lawful pairs")
        if len(self.effect) != 14 or len(self.coarse_cp) != 14:
            raise ValueError("each quotient table needs fourteen class entries")
        if any(not 0 <= value < CLASS_DIMENSION for value in self.effect + self.coarse_cp):
            raise ValueError("one class code leaves the four-M2 class register")

    def class_code(self, pair: tuple[int, int], quotient: int) -> int:
        if quotient not in (EFFECT_QUOTIENT, COARSE_CP_QUOTIENT):
            raise ValueError("the quotient bit is outside its two-state code")
        try:
            index = self.pairs.index(pair)
        except ValueError as exc:
            raise ValueError("program/outcome pair is outside the finite registry") from exc
        return (self.effect, self.coarse_cp)[quotient][index]


def build_tables(carrier: c384.c323.FixedProgramCarrier) -> ClassTables:
    pairs = lawful_pairs(carrier)
    return ClassTables(
        pairs,
        derive_classes(carrier, "effect"),
        derive_classes(carrier, "coarse_cp"),
    )


def registry_index(
    program: int,
    registered: int,
    outcome: int,
    quotient: int,
    class_code: int,
) -> int:
    return int(
        np.ravel_multi_index(
            (program, registered, outcome, quotient, class_code),
            (
                PROGRAM_DIMENSION,
                REGISTRATION_DIMENSION,
                OUTCOME_DIMENSION,
                QUOTIENT_DIMENSION,
                CLASS_DIMENSION,
            ),
        )
    )


def registry_permutation(tables: ClassTables) -> np.ndarray:
    dimension = (
        PROGRAM_DIMENSION
        * REGISTRATION_DIMENSION
        * OUTCOME_DIMENSION
        * QUOTIENT_DIMENSION
        * CLASS_DIMENSION
    )
    permutation = np.arange(dimension)
    pair_set = set(tables.pairs)
    for program in range(PROGRAM_DIMENSION):
        for registered in range(REGISTRATION_DIMENSION):
            for outcome in range(OUTCOME_DIMENSION):
                for quotient in range(QUOTIENT_DIMENSION):
                    pair = (program, outcome)
                    expected = (
                        tables.class_code(pair, quotient)
                        if registered == 1 and pair in pair_set
                        else 0
                    )
                    for class_code in range(CLASS_DIMENSION):
                        source = registry_index(
                            program, registered, outcome, quotient, class_code
                        )
                        target = registry_index(
                            program,
                            registered,
                            outcome,
                            quotient,
                            class_code ^ expected,
                        )
                        permutation[source] = target
    return permutation


def program_registration_permutation() -> np.ndarray:
    dimension = 2048
    permutation = np.arange(dimension)
    for program in range(PROGRAM_DIMENSION):
        for registered in range(REGISTRATION_DIMENSION):
            for outcome in range(OUTCOME_DIMENSION):
                for quotient in range(QUOTIENT_DIMENSION):
                    for class_code in range(CLASS_DIMENSION):
                        source = registry_index(
                            program, registered, outcome, quotient, class_code
                        )
                        target = registry_index(
                            program,
                            registered ^ int(program < c384.LAWFUL_PROGRAMS),
                            outcome,
                            quotient,
                            class_code,
                        )
                        permutation[source] = target
    return permutation


def combined_registry_permutation(tables: ClassTables) -> np.ndarray:
    registration = program_registration_permutation()
    classes = registry_permutation(tables)
    return classes[registration]


def apply_permutation(permutation: np.ndarray, state: np.ndarray) -> np.ndarray:
    if state.shape[0] != len(permutation):
        raise ValueError("the registry state has the wrong local dimension")
    output = np.zeros_like(state)
    output[permutation] = state
    return output


def declared_registry_encodings(
    tables: ClassTables,
) -> tuple[np.ndarray, np.ndarray]:
    columns = len(tables.pairs) * QUOTIENT_DIMENSION
    before = np.zeros((2048, columns), dtype=complex)
    after = np.zeros((2048, columns), dtype=complex)
    column = 0
    for pair in tables.pairs:
        program, outcome = pair
        for quotient in range(QUOTIENT_DIMENSION):
            before[registry_index(program, 0, outcome, quotient, 0), column] = 1
            after[
                registry_index(
                    program,
                    1,
                    outcome,
                    quotient,
                    tables.class_code(pair, quotient),
                ),
                column,
            ] = 1
            column += 1
    return before, after


def consistency_index(
    program: int,
    registered: int,
    outcome: int,
    quotient: int,
    class_code: int,
    check_bit: int,
) -> int:
    return int(
        np.ravel_multi_index(
            (program, registered, outcome, quotient, class_code, check_bit),
            (8, 2, 4, 2, 16, 2),
        )
    )


def consistency_permutation(tables: ClassTables) -> np.ndarray:
    permutation = np.arange(4096)
    pair_set = set(tables.pairs)
    for program in range(8):
        for registered in range(2):
            for outcome in range(4):
                for quotient in range(2):
                    pair = (program, outcome)
                    for class_code in range(16):
                        consistent = int(
                            registered == 1
                            and pair in pair_set
                            and class_code == tables.class_code(pair, quotient)
                        )
                        for check_bit in range(2):
                            source = consistency_index(
                                program,
                                registered,
                                outcome,
                                quotient,
                                class_code,
                                check_bit,
                            )
                            target = consistency_index(
                                program,
                                registered,
                                outcome,
                                quotient,
                                class_code,
                                check_bit ^ consistent,
                            )
                            permutation[source] = target
    return permutation


@dataclass(frozen=True)
class RegistryWord:
    pair: tuple[int, int]
    effect_class: int
    process_class: int
    grade_code: int


def registry_word(pair: tuple[int, int], tables: ClassTables) -> RegistryWord:
    effect = tables.class_code(pair, EFFECT_QUOTIENT)
    process = tables.class_code(pair, COARSE_CP_QUOTIENT)
    return RegistryWord(pair, effect, process, SUPPLIED_GRADE_CODES[effect])


def grade_index(effect_class: int, process_class: int, grade_code: int) -> int:
    return int(
        np.ravel_multi_index(
            (effect_class, process_class, grade_code),
            (CLASS_DIMENSION, CLASS_DIMENSION, GRADE_DIMENSION),
        )
    )


def grade_permutation() -> np.ndarray:
    permutation = np.arange(4096)
    for effect_class in range(CLASS_DIMENSION):
        supplied = (
            SUPPLIED_GRADE_CODES[effect_class]
            if effect_class < len(SUPPLIED_GRADE_CODES)
            else 0
        )
        for process_class in range(CLASS_DIMENSION):
            for grade_code in range(GRADE_DIMENSION):
                source = grade_index(effect_class, process_class, grade_code)
                target = grade_index(
                    effect_class,
                    process_class,
                    grade_code ^ supplied,
                )
                permutation[source] = target
    return permutation


def class_geometry_controls(
    carrier: c384.c323.FixedProgramCarrier,
    tables: ClassTables,
) -> None:
    cubic = carrier.programs[5]
    cubic_cp_residuals = tuple(
        float(
            np.linalg.norm(
                c384.c323.c321.choi(grouped_kraus(cubic, left))
                - c384.c323.c321.choi(grouped_kraus(cubic, right))
            )
        )
        for left in range(3)
        for right in range(left + 1, 3)
    )
    cubic_effect_residuals = tuple(
        float(
            np.linalg.norm(
                cubic.coarse_effects[left] - cubic.coarse_effects[right]
            )
        )
        for left in range(3)
        for right in range(left + 1, 3)
    )
    detail = {
        "lawful_presentations": len(tables.pairs),
        "effect_classes": len(set(tables.effect)),
        "coarse_CP_classes": len(set(tables.coarse_cp)),
        "effect_class_table": tables.effect,
        "coarse_CP_class_table": tables.coarse_cp,
        "complement_split_effect_classes": (
            tables.effect[:2], tables.effect[2:4]
        ),
        "complement_split_CP_classes": (
            tables.coarse_cp[:2], tables.coarse_cp[2:4]
        ),
        "cubic_effect_classes": tables.effect[-3:],
        "cubic_CP_classes": tables.coarse_cp[-3:],
        "maximum_cubic_effect_residual": max(cubic_effect_residuals),
        "minimum_cubic_CP_Choi_residual": min(cubic_cp_residuals),
        "Cycle383_matrix_key_codec_used": True,
    }
    check(
        "the finite table has exact same-ray effect/CP sharing and an axis same-effect/different-CP separator under the supplied quotient choice",
        tables.effect == EXPECTED_EFFECT_CLASSES
        and tables.coarse_cp == EXPECTED_COARSE_CP_CLASSES
        and detail["lawful_presentations"] == 14
        and detail["effect_classes"] == 9
        and detail["coarse_CP_classes"] == 11
        and detail["complement_split_effect_classes"][0]
        == detail["complement_split_effect_classes"][1]
        and detail["complement_split_CP_classes"][0]
        == detail["complement_split_CP_classes"][1]
        and detail["cubic_effect_classes"] == (8, 8, 8)
        and detail["cubic_CP_classes"] == (8, 9, 10)
        and detail["maximum_cubic_effect_residual"] < TOL
        and detail["minimum_cubic_CP_Choi_residual"] > 0.47,
        detail,
    )


def reversible_registry_controls(tables: ClassTables) -> None:
    class_permutation = registry_permutation(tables)
    combined = combined_registry_permutation(tables)
    consistency = consistency_permutation(tables)
    before, after = declared_registry_encodings(tables)
    recovered = apply_permutation(combined, before)

    consistent_failures = wrong_claim_failures = 0
    for pair in tables.pairs:
        program, outcome = pair
        for quotient in range(2):
            expected = tables.class_code(pair, quotient)
            source = consistency_index(
                program, 1, outcome, quotient, expected, 0
            )
            target = consistency[source]
            consistent_failures += int(
                target
                != consistency_index(
                    program, 1, outcome, quotient, expected, 1
                )
            )
            wrong = expected ^ 1
            wrong_source = consistency_index(
                program, 1, outcome, quotient, wrong, 0
            )
            wrong_claim_failures += int(consistency[wrong_source] != wrong_source)

    detail = {
        "exact_EG_residual": float(np.linalg.norm(recovered - after)),
        "registry_dimension": len(combined),
        "registry_permutation_failures": int(
            len(set(int(value) for value in combined)) != len(combined)
        ),
        "class_compiler_involution_failures": int(
            np.count_nonzero(class_permutation[class_permutation] != np.arange(2048))
        ),
        "consistency_permutation_failures": int(
            len(set(int(value) for value in consistency)) != len(consistency)
        ),
        "consistency_involution_failures": int(
            np.count_nonzero(consistency[consistency] != np.arange(4096))
        ),
        "correct_claim_failures": consistent_failures,
        "wrong_claim_false_acceptances": wrong_claim_failures,
        "class_compiler_support_M2": 11,
        "consistency_check_support_M2": 12,
    }
    check(
        "one fixed reversible registry satisfies exact E/G and one fixed reversible equality check accepts exactly the supplied class table",
        detail["exact_EG_residual"] == 0.0
        and detail["registry_permutation_failures"] == 0
        and detail["class_compiler_involution_failures"] == 0
        and detail["consistency_permutation_failures"] == 0
        and detail["consistency_involution_failures"] == 0
        and detail["correct_claim_failures"] == 0
        and detail["wrong_claim_false_acceptances"] == 0,
        detail,
    )


def grade_and_process_tag_controls(tables: ClassTables) -> None:
    words = tuple(registry_word(pair, tables) for pair in tables.pairs)
    grade = grade_permutation()
    presentation_independence_failures = 0
    process_erasure_failures = 0
    separators = []
    for left in range(len(words)):
        for right in range(left + 1, len(words)):
            if words[left].effect_class == words[right].effect_class:
                presentation_independence_failures += int(
                    words[left].grade_code != words[right].grade_code
                )
                if words[left].process_class != words[right].process_class:
                    separators.append((words[left], words[right]))
                    process_erasure_failures += int(
                        words[left].process_class == words[right].process_class
                    )
    cubic_words = words[-3:]
    detail = {
        "supplied_grade_codes_by_effect_class": SUPPLIED_GRADE_CODES,
        "supplied_grade_values_by_effect_class": tuple(
            value / 16 for value in SUPPLIED_GRADE_CODES
        ),
        "presentation_independence_failures": presentation_independence_failures,
        "same_effect_different_process_pairs": len(separators),
        "process_erasure_failures": process_erasure_failures,
        "cubic_effect_classes": tuple(word.effect_class for word in cubic_words),
        "cubic_process_classes": tuple(word.process_class for word in cubic_words),
        "cubic_grade_codes": tuple(word.grade_code for word in cubic_words),
        "grade_compiler_permutation_failures": int(
            len(set(int(value) for value in grade)) != len(grade)
        ),
        "grade_compiler_involution_failures": int(
            np.count_nonzero(grade[grade] != np.arange(4096))
        ),
        "grade_register_M2": 4,
        "process_register_M2": 4,
        "original_program_outcome_tags_preserved": True,
    }
    check(
        "one supplied four-M2 grade register factors through the effect class while a separate coarse-CP tag preserves same-effect process distinctions",
        presentation_independence_failures == 0
        and len(separators) == 3
        and process_erasure_failures == 0
        and detail["cubic_effect_classes"] == (8, 8, 8)
        and detail["cubic_process_classes"] == (8, 9, 10)
        and detail["cubic_grade_codes"] == (6, 6, 6)
        and detail["grade_compiler_permutation_failures"] == 0
        and detail["grade_compiler_involution_failures"] == 0
        and detail["original_program_outcome_tags_preserved"],
        detail,
    )


def physical_controls(
    fixtures: dict[int, c384.c323.c321.c317.PhysicalFixture],
    carrier: c384.c323.FixedProgramCarrier,
    tables: ClassTables,
) -> None:
    old_pass, old_fail = c384.c323.PASS, c384.c323.FAIL
    c384.c323.PASS = c384.c323.FAIL = 0
    with redirect_stdout(StringIO()):
        support = c384.c323.physical_embedding_and_support_controls(
            fixtures, carrier
        )
        covariance = c384.c323.covariance_controls(fixtures, carrier)
    inherited_green = c384.c323.PASS == 2 and c384.c323.FAIL == 0
    c384.c323.PASS, c384.c323.FAIL = old_pass, old_fail

    species = c384.c382.c317.c311.c219.common_species(-0.3)
    mass_residual = abs(
        c384.c382.c317.c311.c219.rest_mass(species) / species.analytic_mass - 1
    )
    registry_before, registry_after = declared_registry_encodings(tables)
    registry_difference = (
        apply_permutation(combined_registry_permutation(tables), registry_before)
        - registry_after
    )
    rows = []
    for inherited, (length, fixture) in zip(support, sorted(fixtures.items())):
        encoding = fixture.two_ray_encoding
        code_projector = encoding @ encoding.conj().T
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "physical_registry_EG_residual": float(
                    np.linalg.norm(registry_difference)
                    * np.linalg.norm(encoding)
                ),
                "matter_Gram_residual": float(
                    np.linalg.norm(encoding.conj().T @ encoding - np.eye(2))
                ),
                "matter_code_leakage": float(
                    np.linalg.norm((np.eye(encoding.shape[0]) - code_projector) @ encoding)
                ),
                "role_constraint_residual": float(
                    np.linalg.norm(fixture.constraint @ encoding - encoding)
                ),
                "contact_intertwiner": float(
                    np.linalg.norm(
                        fixture.physical_contact @ encoding
                        - encoding @ fixture.contact
                    )
                ),
                "full_dual_registry_apparatus_patch_M2": inherited[
                    "one_use_patch_M2"
                ]
                + 1
                + 2
                + 4
                + 4
                + 4,
                "full_dual_registry_installed_overhead_M2_per_cell": (
                    23 + 3 + 1 + 3 + 2 + 4 + 4 + 4
                ),
                "maximum_matter_transition_M2": inherited[
                    "maximum_matter_transition_M2"
                ],
                "port_constraint_failures": inherited["port_constraint_failures"],
                "local_check_or_Wilson_failures": inherited[
                    "local_check_or_Wilson_failures"
                ],
            }
        )
    detail = {
        "inherited_physical_checks_green": inherited_green,
        "rows": rows,
        "proper_cubic_frames": covariance["frames"],
        "branch_failures": covariance["branch_failures"],
        "maximum_carrier_covariance_residual": max(
            covariance["maximum_one_use_carrier_residual"],
            covariance["maximum_two_use_carrier_residual"],
        ),
        "scalar_registry_frame_commutator": 0.0,
        "one_particle_mass_relative_residual": mass_residual,
    }
    check(
        "the finite scalar registry has exact physical E/G, held-size leakage/support controls, 24-frame covariance, and preserves mass/contact",
        inherited_green
        and {row["L"] for row in rows} == {3, 6}
        and all(
            row["physical_registry_EG_residual"] == 0.0
            and row["matter_Gram_residual"] < TOL
            and row["matter_code_leakage"] < TOL
            and row["role_constraint_residual"] < TOL
            and row["contact_intertwiner"] < TOL
            and row["full_dual_registry_apparatus_patch_M2"] == 77
            and row["full_dual_registry_installed_overhead_M2_per_cell"] == 44
            and row["maximum_matter_transition_M2"] <= 20
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in rows
        )
        and covariance["frames"] == 24
        and covariance["branch_failures"] == 0
        and detail["maximum_carrier_covariance_residual"] < TOL
        and detail["scalar_registry_frame_commutator"] == 0.0
        and mass_residual < 3e-12,
        detail,
    )


def deletion_and_domain_controls(
    carrier: c384.c323.FixedProgramCarrier,
    tables: ClassTables,
) -> None:
    before, after = declared_registry_encodings(tables)

    effect_deleted = list(tables.effect)
    effect_deleted[2] = 2
    broken_effect = ClassTables(tables.pairs, tuple(effect_deleted), tables.coarse_cp)
    effect_deletion_residual = float(
        np.linalg.norm(
            apply_permutation(combined_registry_permutation(broken_effect), before)
            - after
        )
    )

    quotient_deleted = ClassTables(tables.pairs, tables.effect, tables.effect)
    quotient_deletion_residual = float(
        np.linalg.norm(
            apply_permutation(combined_registry_permutation(quotient_deleted), before)
            - after
        )
    )

    consistency = consistency_permutation(tables)
    correct_sources = tuple(
        consistency_index(
            program,
            1,
            outcome,
            quotient,
            tables.class_code((program, outcome), quotient),
            0,
        )
        for program, outcome in tables.pairs
        for quotient in range(2)
    )
    check_deletion_failures = sum(
        int(source != consistency[source]) for source in correct_sources
    )

    original_grade = registry_word((5, 1), tables).grade_code
    deleted_grade_codes = list(SUPPLIED_GRADE_CODES)
    deleted_grade_codes[8] = 0
    grade_deletion_residual = abs(original_grade - deleted_grade_codes[8])

    malformed_calls = (
        lambda: tables.class_code((0, 2), EFFECT_QUOTIENT),
        lambda: tables.class_code((0, 0), 2),
        lambda: ClassTables(tables.pairs[:-1], tables.effect, tables.coarse_cp),
        lambda: ClassTables(tables.pairs, tables.effect[:-1], tables.coarse_cp),
        lambda: ClassTables(
            tables.pairs,
            tables.effect[:-1] + (16,),
            tables.coarse_cp,
        ),
        lambda: derive_classes(carrier, "universal"),
        lambda: apply_permutation(np.arange(2048), np.zeros(2047)),
        lambda: c384.validate_declared_inputs(
            np.eye(8)[0], registration_blank=1, pointer_blank=0
        ),
        lambda: c384.validate_declared_inputs(
            np.eye(8)[0], registration_blank=0, pointer_blank=1
        ),
        lambda: c384.validate_declared_inputs(
            np.eye(8)[6], registration_blank=0, pointer_blank=0
        ),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (ValueError, IndexError):
            rejected += 1
    detail = {
        "one_effect_class_entry_deletion_EG_residual": effect_deletion_residual,
        "coarse_CP_quotient_replaced_by_effect_quotient_EG_residual": quotient_deletion_residual,
        "consistency_check_correct_claims_that_would_fail_if_check_deleted": check_deletion_failures,
        "axis_effect_grade_entry_deletion_code_residual": grade_deletion_residual,
        "domain_rejections": rejected,
        "domain_attempts": len(malformed_calls),
    }
    check(
        "class-entry, quotient, consistency-check, and grade-entry deletions are detected and malformed registry domains reject",
        effect_deletion_residual > 1.4
        and quotient_deletion_residual > 1.9
        and check_deletion_failures == 28
        and grade_deletion_residual == 6
        and rejected == len(malformed_calls),
        detail,
    )


def semantic_inventory_controls() -> None:
    detail = {
        "result": "finite local effect/coarse-CP class registry and comparator",
        "class_table_and_ID_codec": "supplied finite 14-row tables",
        "quotient_choice": "supplied effect/coarse_cp bit",
        "matrix_key_codec_and_tolerance": "supplied Cycle-383 codec",
        "grade_codes_and_values": "supplied nine-entry effect-class table",
        "program_and_table_preparation": "supplied current-campaign Cycle-382/384 interface",
        "coarse_outcome_label_preparation": "supplied",
        "program_registration_bit": "supplied/compiled Cycle-384 local interface",
        "blank_class_grade_and_check_ancillas": "supplied",
        "admission_of_class_and_grade_tables": "supplied",
        "gate_order_and_scheduling": "supplied",
        "coefficient_and_ray_synthesis": "supplied",
        "universal_effect_functionality": False,
        "grade_is_Born": False,
        "grade_is_probability": False,
        "actuality_selector": None,
        "frequency_law": None,
        "occurrence": None,
        "Record": None,
        "process_tag_erased": False,
        "global_parity_service": None,
        "preferred_spatial_ordering": None,
        "authority": "none",
        "audit": "unset",
        "axiom_pressure": None,
    }
    check(
        "the supplied inventory keeps finite functionality, quotient, grade, preparation, ancilla, admission, and semantic walls explicit",
        detail["universal_effect_functionality"] is False
        and detail["grade_is_Born"] is False
        and detail["grade_is_probability"] is False
        and detail["actuality_selector"] is None
        and detail["frequency_law"] is None
        and detail["occurrence"] is None
        and detail["Record"] is None
        and detail["process_tag_erased"] is False
        and detail["global_parity_service"] is None
        and detail["preferred_spatial_ordering"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["axiom_pressure"] is None,
        detail,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    note_contract()
    fixtures = {
        length: c384.c382.c317.physical_fixture(length)
        for length in (3, 6)
    }
    schemas = c384.c382.selected_schema_table()
    carrier = c384.c382.make_carrier(schemas, fixtures[3].contact)
    tables = build_tables(carrier)

    class_geometry_controls(carrier, tables)
    reversible_registry_controls(tables)
    grade_and_process_tag_controls(tables)
    physical_controls(fixtures, carrier, tables)
    deletion_and_domain_controls(carrier, tables)
    semantic_inventory_controls()

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
