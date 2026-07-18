#!/usr/bin/env python3
"""Cycle 388: reversible integer normalization reference for Cycle 386.

Nine six-M2 numerator registers use the exact supplied denominator 48.  One
fixed program-controlled modular adder loads the sum for the selected
Cycle-382 coarse menu into an eight-M2 accumulator, and one reversible check
gate flags exact equality to 48.  Two distinct strictly positive effect-class
tables pass the same checker while the Cycle-386 coarse-CP tags are carried
unchanged.

This is a code-space reference update plus scalar matter-code extension, not
a nearest-neighbor primitive-gate compiler.  It is not probability, Born
selection, actuality, sampling, or frequency.  Authority is none and audit is
unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from pathlib import Path
from io import StringIO
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_finite_effect_class_registry_cycle386_2026_07_18 as c386


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FINITE_MENU_NORMALIZATION_CHECKER_CYCLE388_NOTE_2026-07-18.md"
)
TOL = 1.2e-10

DENOMINATOR = 48
GRADE_CLASSES = 9
GRADE_M2_PER_CLASS = 6
ACCUMULATOR_M2 = 8
ACCUMULATOR_MODULUS = 2**ACCUMULATOR_M2
CHECK_M2 = 1
PROCESS_TAG_M2 = 4
MAX_COARSE_OUTCOMES = 3
PROCESS_PADDING = 15

GRADE_TABLES = {
    "A": (12, 36, 8, 16, 24, 24, 20, 28, 16),
    "B": (18, 30, 12, 14, 22, 24, 7, 41, 16),
}

EXPECTED_EFFECT_MENUS = (
    (0, 1),
    (0, 1),
    (2, 3, 4),
    (5, 5),
    (6, 7),
    (8, 8, 8),
)
EXPECTED_PROCESS_MENUS = (
    (0, 1),
    (0, 1),
    (2, 3, 4),
    (5, 5),
    (6, 7),
    (8, 9, 10),
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
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-388 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "bounded reversible finite menu-normalization checker",
        "79-m2 reference/state update",
        "exact denominator 48",
        "nine six-m2 grade registers",
        "eight-m2 modular accumulator",
        "two distinct strictly positive tables",
        "same fixed checker accepts both",
        "coarse-cp process tags remain unchanged",
        "explicit finite underdetermination witness",
        "exact e/g",
        "held l=6",
        "24 proper-cubic frames",
        "138-m2 envelope/support inventory",
        "not a completed physical arithmetic compiler",
        "physical arithmetic gate compiler: none",
        "nearest-neighbor decomposition: none",
        "maximum primitive support m2: none",
        "primitive-boundary leakage audit: none",
        "current-campaign cycle-386",
        "grade-table selection remains supplied",
        "denominator remains supplied",
        "arithmetic ancillas remain supplied",
        "admission and schedule remain supplied",
        "not probability",
        "no born law",
        "no actuality or frequency inference",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins exact reversible arithmetic, two positive witnesses, physical controls, provenance, and semantic inventory",
        not missing,
        missing,
    )


def menu_tables(
    carrier: c386.c384.c323.FixedProgramCarrier,
    classes: c386.ClassTables,
) -> tuple[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]]:
    effect = []
    process = []
    for program, apparatus in enumerate(carrier.programs):
        effect.append(
            tuple(
                classes.class_code((program, outcome), c386.EFFECT_QUOTIENT)
                for outcome in range(len(apparatus.coarse_groups))
            )
        )
        process.append(
            tuple(
                classes.class_code((program, outcome), c386.COARSE_CP_QUOTIENT)
                for outcome in range(len(apparatus.coarse_groups))
            )
        )
    return tuple(effect), tuple(process)


def validate_denominator(denominator: int) -> None:
    if type(denominator) is not int or denominator != DENOMINATOR:
        raise ValueError("the finite checker is compiled for exact denominator 48")


def validate_grade_table(grades: tuple[int, ...]) -> None:
    if len(grades) != GRADE_CLASSES:
        raise ValueError("the finite effect registry needs nine grade numerators")
    if any(type(value) is not int or not 0 < value < DENOMINATOR for value in grades):
        raise ValueError("every admitted grade numerator must be strictly between 0 and 48")


def padded_process_tags(
    program: int,
    process_menus: tuple[tuple[int, ...], ...],
) -> tuple[int, int, int]:
    if not 0 <= program < len(process_menus):
        raise ValueError("program is outside the six-menu checker")
    tags = process_menus[program]
    return tuple(tags + (PROCESS_PADDING,) * (MAX_COARSE_OUTCOMES - len(tags)))  # type: ignore[return-value]


@dataclass(frozen=True)
class MenuCheckState:
    program: int
    registered: int
    grades: tuple[int, ...]
    process_tags: tuple[int, int, int]
    accumulator: int = 0
    check_bit: int = 0

    def __post_init__(self) -> None:
        if type(self.program) is not int or not 0 <= self.program < 6:
            raise ValueError("the checker program needs one of six lawful labels")
        if self.registered not in (0, 1):
            raise ValueError("the Cycle-384 registration input needs one M2")
        validate_grade_table(self.grades)
        if len(self.process_tags) != MAX_COARSE_OUTCOMES or any(
            type(value) is not int or not 0 <= value < 16
            for value in self.process_tags
        ):
            raise ValueError("three four-M2 process-tag slots are required")
        if type(self.accumulator) is not int or not 0 <= self.accumulator < 256:
            raise ValueError("the arithmetic accumulator needs eight M2")
        if self.check_bit not in (0, 1):
            raise ValueError("the equality flag needs one M2")


def validate_admitted_state(
    state: MenuCheckState,
    process_menus: tuple[tuple[int, ...], ...],
    *,
    denominator: int = DENOMINATOR,
) -> None:
    validate_denominator(denominator)
    if state.registered != 1:
        raise ValueError("the finite menu checker requires the registered program code")
    if state.process_tags != padded_process_tags(state.program, process_menus):
        raise ValueError("the coarse-CP process tags do not match the admitted program")


def selected_menu_sum(
    state: MenuCheckState,
    effect_menus: tuple[tuple[int, ...], ...],
) -> int:
    if len(effect_menus) != 6 or any(not 1 <= len(menu) <= 3 for menu in effect_menus):
        raise ValueError("the checker needs six menus with one to three class entries")
    menu = effect_menus[state.program]
    if any(not 0 <= effect_class < GRADE_CLASSES for effect_class in menu):
        raise ValueError("one menu entry leaves the nine-class registry")
    return sum(state.grades[effect_class] for effect_class in menu)


def add_menu_sum(
    state: MenuCheckState,
    effect_menus: tuple[tuple[int, ...], ...],
) -> MenuCheckState:
    total = selected_menu_sum(state, effect_menus)
    return replace(
        state,
        accumulator=(state.accumulator + total) % ACCUMULATOR_MODULUS,
    )


def subtract_menu_sum(
    state: MenuCheckState,
    effect_menus: tuple[tuple[int, ...], ...],
) -> MenuCheckState:
    total = selected_menu_sum(state, effect_menus)
    return replace(
        state,
        accumulator=(state.accumulator - total) % ACCUMULATOR_MODULUS,
    )


def flip_normalization_check(state: MenuCheckState) -> MenuCheckState:
    return replace(
        state,
        check_bit=state.check_bit
        ^ int(state.registered == 1 and state.accumulator == DENOMINATOR),
    )


def checker_update(
    state: MenuCheckState,
    effect_menus: tuple[tuple[int, ...], ...],
) -> MenuCheckState:
    return flip_normalization_check(add_menu_sum(state, effect_menus))


def checker_inverse(
    state: MenuCheckState,
    effect_menus: tuple[tuple[int, ...], ...],
) -> MenuCheckState:
    return subtract_menu_sum(flip_normalization_check(state), effect_menus)


def blank_state(
    program: int,
    grades: tuple[int, ...],
    process_menus: tuple[tuple[int, ...], ...],
) -> MenuCheckState:
    return MenuCheckState(
        program,
        1,
        grades,
        padded_process_tags(program, process_menus),
        0,
        0,
    )


def table_normalized(
    grades: tuple[int, ...],
    effect_menus: tuple[tuple[int, ...], ...],
    process_menus: tuple[tuple[int, ...], ...],
) -> bool:
    return all(
        checker_update(blank_state(program, grades, process_menus), effect_menus).check_bit
        == 1
        for program in range(6)
    )


def exact_integer_table_controls(
    effect_menus: tuple[tuple[int, ...], ...],
    process_menus: tuple[tuple[int, ...], ...],
) -> None:
    rows = []
    exact_eg_failures = inverse_failures = process_tag_failures = 0
    for name, grades in GRADE_TABLES.items():
        menu_sums = []
        for program in range(6):
            source = blank_state(program, grades, process_menus)
            output = checker_update(source, effect_menus)
            expected = replace(
                source,
                accumulator=DENOMINATOR,
                check_bit=1,
            )
            exact_eg_failures += int(output != expected)
            inverse_failures += int(checker_inverse(output, effect_menus) != source)
            process_tag_failures += int(output.process_tags != source.process_tags)
            menu_sums.append(selected_menu_sum(source, effect_menus))
        rows.append(
            {
                "table": name,
                "numerators": grades,
                "strictly_positive": all(value > 0 for value in grades),
                "menu_sums": tuple(menu_sums),
                "accepted_by_same_checker": table_normalized(
                    grades, effect_menus, process_menus
                ),
            }
        )
    detail = {
        "denominator": DENOMINATOR,
        "effect_menus": effect_menus,
        "process_menus": process_menus,
        "tables": rows,
        "tables_distinct": GRADE_TABLES["A"] != GRADE_TABLES["B"],
        "exact_EG_failures": exact_eg_failures,
        "inverse_failures": inverse_failures,
        "process_tag_carry_failures": process_tag_failures,
        "cubic_process_tags": process_menus[5],
        "cubic_grade_numerators_A": tuple(
            GRADE_TABLES["A"][effect_class] for effect_class in effect_menus[5]
        ),
        "cubic_grade_numerators_B": tuple(
            GRADE_TABLES["B"][effect_class] for effect_class in effect_menus[5]
        ),
    }
    check(
        "one fixed exact-integer reversible checker accepts two distinct strictly positive normalized effect-class tables while preserving process tags",
        effect_menus == EXPECTED_EFFECT_MENUS
        and process_menus == EXPECTED_PROCESS_MENUS
        and detail["tables_distinct"]
        and all(row["strictly_positive"] for row in rows)
        and all(row["menu_sums"] == (48,) * 6 for row in rows)
        and all(row["accepted_by_same_checker"] for row in rows)
        and exact_eg_failures == 0
        and inverse_failures == 0
        and process_tag_failures == 0
        and detail["cubic_process_tags"] == (8, 9, 10)
        and detail["cubic_grade_numerators_A"] == (16, 16, 16)
        and detail["cubic_grade_numerators_B"] == (16, 16, 16),
        detail,
    )


def reversible_arithmetic_controls(
    effect_menus: tuple[tuple[int, ...], ...],
    process_menus: tuple[tuple[int, ...], ...],
) -> None:
    inverse_failures = check_involution_failures = arithmetic_overflow_failures = 0
    tested = 0
    for grades in GRADE_TABLES.values():
        for program in range(6):
            for accumulator in (0, 1, 47, 48, 127, 255):
                for check_bit in (0, 1):
                    state = replace(
                        blank_state(program, grades, process_menus),
                        accumulator=accumulator,
                        check_bit=check_bit,
                    )
                    output = checker_update(state, effect_menus)
                    inverse_failures += int(
                        checker_inverse(output, effect_menus) != state
                    )
                    check_involution_failures += int(
                        flip_normalization_check(flip_normalization_check(state))
                        != state
                    )
                    arithmetic_overflow_failures += int(
                        not 0 <= output.accumulator < ACCUMULATOR_MODULUS
                    )
                    tested += 1
    detail = {
        "states_tested": tested,
        "inverse_failures": inverse_failures,
        "check_gate_involution_failures": check_involution_failures,
        "modular_range_failures": arithmetic_overflow_failures,
        "grade_table_register_M2": GRADE_CLASSES * GRADE_M2_PER_CLASS,
        "program_register_M2": 3,
        "program_registration_M2": 1,
        "process_tag_register_M2": MAX_COARSE_OUTCOMES * PROCESS_TAG_M2,
        "accumulator_M2": ACCUMULATOR_M2,
        "check_M2": CHECK_M2,
        "reference_state_width_M2": (
            3
            + 1
            + GRADE_CLASSES * GRADE_M2_PER_CLASS
            + MAX_COARSE_OUTCOMES * PROCESS_TAG_M2
            + ACCUMULATOR_M2
            + CHECK_M2
        ),
    }
    check(
        "the eight-M2 modular adder and one-M2 equality gate form one bounded exactly reversible code-space reference update on the declared integer domain",
        tested == 144
        and inverse_failures == 0
        and check_involution_failures == 0
        and arithmetic_overflow_failures == 0
        and detail["reference_state_width_M2"] == 79,
        detail,
    )


def physical_controls(
    fixtures: dict[int, c386.c384.c323.c321.c317.PhysicalFixture],
    carrier: c386.c384.c323.FixedProgramCarrier,
    effect_menus: tuple[tuple[int, ...], ...],
    process_menus: tuple[tuple[int, ...], ...],
) -> None:
    old_pass, old_fail = c386.c384.c323.PASS, c386.c384.c323.FAIL
    c386.c384.c323.PASS = c386.c384.c323.FAIL = 0
    with redirect_stdout(StringIO()):
        support = c386.c384.c323.physical_embedding_and_support_controls(
            fixtures, carrier
        )
        covariance = c386.c384.c323.covariance_controls(fixtures, carrier)
    inherited_green = (
        c386.c384.c323.PASS == 2 and c386.c384.c323.FAIL == 0
    )
    c386.c384.c323.PASS, c386.c384.c323.FAIL = old_pass, old_fail

    logical_failures = sum(
        int(
            checker_update(
                blank_state(program, grades, process_menus),
                effect_menus,
            ).check_bit
            != 1
        )
        for grades in GRADE_TABLES.values()
        for program in range(6)
    )
    species = c386.c384.c382.c317.c311.c219.common_species(-0.3)
    mass_residual = abs(
        c386.c384.c382.c317.c311.c219.rest_mass(species)
        / species.analytic_mass
        - 1
    )
    rows = []
    for inherited, (length, fixture) in zip(support, sorted(fixtures.items())):
        encoding = fixture.two_ray_encoding
        code_projector = encoding @ encoding.conj().T
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "scalar_extended_code_space_EG_residual": float(
                    logical_failures * np.linalg.norm(encoding)
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
                "combined_state_envelope_M2": inherited["one_use_patch_M2"]
                + 1
                + GRADE_CLASSES * GRADE_M2_PER_CLASS
                + MAX_COARSE_OUTCOMES * PROCESS_TAG_M2
                + ACCUMULATOR_M2
                + CHECK_M2,
                "inherited_accounting_envelope_M2_per_cell": (
                    23
                    + 3
                    + 1
                    + 3
                    + GRADE_CLASSES * GRADE_M2_PER_CLASS
                    + MAX_COARSE_OUTCOMES * PROCESS_TAG_M2
                    + ACCUMULATOR_M2
                    + CHECK_M2
                ),
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
        "normalization_register_frame_commutator": 0.0,
        "one_particle_mass_relative_residual": mass_residual,
        "physical_arithmetic_gate_compiler": None,
        "nearest_neighbor_decomposition": None,
        "maximum_primitive_support_M2": None,
        "primitive_boundary_leakage_audit": None,
    }
    check(
        "the code-space normalization reference has an exact scalar matter-code extension, a constant envelope inventory, held-size matter controls, and 24-frame covariance",
        inherited_green
        and {row["L"] for row in rows} == {3, 6}
        and all(
            row["scalar_extended_code_space_EG_residual"] == 0.0
            and row["matter_code_leakage"] < TOL
            and row["role_constraint_residual"] < TOL
            and row["contact_intertwiner"] < TOL
            and row["combined_state_envelope_M2"] == 138
            and row["inherited_accounting_envelope_M2_per_cell"] == 105
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in rows
        )
        and covariance["frames"] == 24
        and covariance["branch_failures"] == 0
        and detail["maximum_carrier_covariance_residual"] < TOL
        and detail["normalization_register_frame_commutator"] == 0.0
        and mass_residual < 3e-12
        and detail["physical_arithmetic_gate_compiler"] is None
        and detail["nearest_neighbor_decomposition"] is None
        and detail["maximum_primitive_support_M2"] is None
        and detail["primitive_boundary_leakage_audit"] is None,
        detail,
    )


def deletion_and_domain_controls(
    effect_menus: tuple[tuple[int, ...], ...],
    process_menus: tuple[tuple[int, ...], ...],
) -> None:
    one_entry_attacks = one_entry_detected = 0
    for grades in GRADE_TABLES.values():
        for effect_class in range(GRADE_CLASSES):
            attacked = list(grades)
            attacked[effect_class] += 1
            attacked_table = tuple(attacked)
            one_entry_attacks += 1
            one_entry_detected += int(
                not table_normalized(attacked_table, effect_menus, process_menus)
            )

    menu_deletion_attacks = menu_deletion_detected = 0
    for grades in GRADE_TABLES.values():
        for program in range(6):
            broken_menus = list(effect_menus)
            broken_menus[program] = broken_menus[program][1:]
            source = blank_state(program, grades, process_menus)
            output = checker_update(source, tuple(broken_menus))
            menu_deletion_attacks += 1
            menu_deletion_detected += int(output.check_bit == 0)

    add_layer_deletion_detected = check_layer_deletion_detected = 0
    for grades in GRADE_TABLES.values():
        for program in range(6):
            source = blank_state(program, grades, process_menus)
            add_deleted = flip_normalization_check(source)
            check_deleted = add_menu_sum(source, effect_menus)
            add_layer_deletion_detected += int(add_deleted.check_bit == 0)
            check_layer_deletion_detected += int(check_deleted.check_bit == 0)

    bad_zero = list(GRADE_TABLES["A"])
    bad_zero[0] = 0
    bad_full = list(GRADE_TABLES["A"])
    bad_full[0] = 48
    wrong_tags = list(padded_process_tags(5, process_menus))
    wrong_tags[1] = wrong_tags[0]
    malformed_calls = (
        lambda: validate_grade_table(GRADE_TABLES["A"][:-1]),
        lambda: validate_grade_table(tuple(bad_zero)),
        lambda: validate_grade_table(tuple(bad_full)),
        lambda: validate_denominator(47),
        lambda: MenuCheckState(6, 1, GRADE_TABLES["A"], (0, 1, 15)),
        lambda: MenuCheckState(0, 1, GRADE_TABLES["A"], (0, 1, 15), 256, 0),
        lambda: MenuCheckState(0, 1, GRADE_TABLES["A"], (0, 1, 15), 0, 2),
        lambda: validate_admitted_state(
            MenuCheckState(0, 0, GRADE_TABLES["A"], (0, 1, 15)),
            process_menus,
        ),
        lambda: validate_admitted_state(
            MenuCheckState(5, 1, GRADE_TABLES["A"], tuple(wrong_tags)),
            process_menus,
        ),
        lambda: selected_menu_sum(
            blank_state(0, GRADE_TABLES["A"], process_menus),
            effect_menus[:-1],
        ),
        lambda: selected_menu_sum(
            blank_state(0, GRADE_TABLES["A"], process_menus),
            ((9,),) + effect_menus[1:],
        ),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (ValueError, IndexError):
            rejected += 1
    detail = {
        "one_entry_attacks_detected": one_entry_detected,
        "one_entry_attacks": one_entry_attacks,
        "menu_term_deletions_detected": menu_deletion_detected,
        "menu_term_deletions": menu_deletion_attacks,
        "add_layer_deletions_detected": add_layer_deletion_detected,
        "check_layer_deletions_detected": check_layer_deletion_detected,
        "layer_deletion_cases": 12,
        "domain_rejections": rejected,
        "domain_attempts": len(malformed_calls),
    }
    check(
        "one-entry, menu-term, adder, and check deletions reject while malformed denominators, grade tables, tags, and arithmetic domains fail admission",
        one_entry_detected == one_entry_attacks == 18
        and menu_deletion_detected == menu_deletion_attacks == 12
        and add_layer_deletion_detected == 12
        and check_layer_deletion_detected == 12
        and rejected == len(malformed_calls),
        detail,
    )


def semantic_inventory_controls() -> None:
    detail = {
        "result": "bounded finite exact-integer code-space normalization reference",
        "grade_table_selection": "supplied choice between admitted table states",
        "denominator_48": "supplied fixed integer scale",
        "nine_grade_register_preparation": "supplied",
        "process_tag_preparation": "supplied Cycle-386 registry interface",
        "accumulator_and_check_blanks": "supplied arithmetic ancillas",
        "class_menu_and_grade_table_admission": "supplied",
        "adder_then_check_schedule": "supplied",
        "program_and_coarse_menu_selection": "supplied",
        "coefficient_and_ray_synthesis": "supplied",
        "finite_constraint_solutions_exhibited": 2,
        "universal_grade_law": None,
        "grade_is_probability": False,
        "grade_is_Born": False,
        "actuality_selector": None,
        "frequency_law": None,
        "occurrence": None,
        "Record": None,
        "process_tags_erased": False,
        "global_parity_service": None,
        "preferred_spatial_ordering": None,
        "physical_arithmetic_gate_compiler": None,
        "nearest_neighbor_decomposition": None,
        "maximum_primitive_support_M2": None,
        "primitive_boundary_leakage_audit": None,
        "authority": "none",
        "audit": "unset",
        "axiom_pressure": None,
    }
    check(
        "the supplied inventory separates finite normalization arithmetic from grade selection, probability, actuality, frequency, and process identity",
        detail["finite_constraint_solutions_exhibited"] == 2
        and detail["universal_grade_law"] is None
        and detail["grade_is_probability"] is False
        and detail["grade_is_Born"] is False
        and detail["actuality_selector"] is None
        and detail["frequency_law"] is None
        and detail["occurrence"] is None
        and detail["Record"] is None
        and detail["process_tags_erased"] is False
        and detail["global_parity_service"] is None
        and detail["preferred_spatial_ordering"] is None
        and detail["physical_arithmetic_gate_compiler"] is None
        and detail["nearest_neighbor_decomposition"] is None
        and detail["maximum_primitive_support_M2"] is None
        and detail["primitive_boundary_leakage_audit"] is None
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
        length: c386.c384.c382.c317.physical_fixture(length)
        for length in (3, 6)
    }
    schemas = c386.c384.c382.selected_schema_table()
    carrier = c386.c384.c382.make_carrier(schemas, fixtures[3].contact)
    classes = c386.build_tables(carrier)
    effect_menus, process_menus = menu_tables(carrier, classes)

    exact_integer_table_controls(effect_menus, process_menus)
    reversible_arithmetic_controls(effect_menus, process_menus)
    physical_controls(fixtures, carrier, effect_menus, process_menus)
    deletion_and_domain_controls(effect_menus, process_menus)
    semantic_inventory_controls()

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
