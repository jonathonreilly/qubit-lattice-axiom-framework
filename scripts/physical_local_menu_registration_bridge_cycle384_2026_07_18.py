#!/usr/bin/env python3
"""Cycle 384: bounded local registration for the Cycle-382 finite menu table.

One fixed reversible four-M2 gate computes membership in the supplied six-
program code into one blank registration M2.  A second fixed isometry, gated
only by that local bit, applies the Cycle-382 carrier with one fresh pointer.
The composed update has no host eligibility query at application.

This finite code predicate supplies no probability, realized-event, durable
registration, or physical scheduling law.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import inspect
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_fixed_program_carrier_two_use_cycle323_2026_07_18 as c323
import physical_fixed_menu_schema_compiler_cycle382_2026_07_18 as c382


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_MENU_REGISTRATION_BRIDGE_CYCLE384_NOTE_2026-07-18.md"
)
TOL = 1.2e-10

PROGRAM_DIMENSION = c323.PROGRAM_DIMENSION
REGISTRATION_DIMENSION = 2
POINTER_DIMENSION = c323.POINTER_DIMENSION
SYSTEM_DIMENSION = 2
LAWFUL_PROGRAMS = c323.LAWFUL_PROGRAMS

I2 = c382.I2
X = c382.X

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
        check("the Cycle-384 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "finite local menu registration result",
        "one registration m2",
        "fixed reversible predicate gate",
        "fixed bit-gated pointer dilation",
        "exact code-space intertwiner",
        "held l=6",
        "24 proper-cubic frames",
        "continuous coefficient synthesis remains supplied",
        "program and table preparation remain supplied",
        "blank registration and pointer ancillas remain supplied",
        "admission and irreversibility remain absent",
        "layer ordering remains supplied",
        "not universal menu eligibility",
        "not an effect-functionality result",
        "no born law",
        "pointer output is not occurrence",
        "not a record",
        "not a physical clock or time law",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the finite predicate, exact physical bridge, complete supplied inventory, and semantic boundary",
        not missing,
        missing,
    )


def lawful_projector() -> np.ndarray:
    return np.diag((1.0,) * LAWFUL_PROGRAMS + (0.0,) * 2).astype(complex)


def validate_predicate(predicate: np.ndarray, *, require_selected_table: bool) -> None:
    if predicate.shape != (PROGRAM_DIMENSION, PROGRAM_DIMENSION):
        raise ValueError("the local predicate must act on exactly three program M2")
    if np.linalg.norm(predicate - predicate.conj().T) >= TOL:
        raise ValueError("the local predicate must be Hermitian")
    if np.linalg.norm(predicate @ predicate - predicate) >= TOL:
        raise ValueError("the local predicate must be a projector")
    if require_selected_table and np.linalg.norm(predicate - lawful_projector()) >= TOL:
        raise ValueError("the predicate does not register the selected six-program table")


def registration_unitary(
    predicate: np.ndarray | None = None,
    *,
    require_selected_table: bool = True,
) -> np.ndarray:
    predicate = lawful_projector() if predicate is None else predicate
    validate_predicate(predicate, require_selected_table=require_selected_table)
    return np.kron(predicate, X) + np.kron(np.eye(PROGRAM_DIMENSION) - predicate, I2)


def registration_constraint() -> np.ndarray:
    """Local four-M2 projector for a predicate bit computed from blank zero."""

    tensor = np.zeros(
        (PROGRAM_DIMENSION, REGISTRATION_DIMENSION) * 2,
        dtype=complex,
    )
    for program in range(PROGRAM_DIMENSION):
        registered = int(program < LAWFUL_PROGRAMS)
        tensor[program, registered, program, registered] = 1
    return tensor.reshape(16, 16)


def blank_registration_encoding() -> np.ndarray:
    encoding = np.zeros((PROGRAM_DIMENSION, 2, PROGRAM_DIMENSION), dtype=complex)
    encoding[:, 0, :] = np.eye(PROGRAM_DIMENSION)
    return encoding.reshape(16, 8)


def idle_pointer_blocks() -> tuple[np.ndarray, ...]:
    return (I2,) + tuple(
        np.zeros((2, 2), dtype=complex)
        for _ in range(POINTER_DIMENSION - 1)
    )


def bit_gated_pointer_dilation(carrier: c323.FixedProgramCarrier) -> np.ndarray:
    """One fixed isometry; the registration M2 is its sole admission control."""

    tensor = np.zeros(
        (
            PROGRAM_DIMENSION,
            REGISTRATION_DIMENSION,
            POINTER_DIMENSION,
            SYSTEM_DIMENSION,
            PROGRAM_DIMENSION,
            REGISTRATION_DIMENSION,
            SYSTEM_DIMENSION,
        ),
        dtype=complex,
    )
    idle = idle_pointer_blocks()
    for program in range(PROGRAM_DIMENSION):
        for registered in range(REGISTRATION_DIMENSION):
            blocks = carrier.block_kraus[program] if registered == 1 else idle
            for pointer, operator in enumerate(blocks):
                tensor[
                    program,
                    registered,
                    pointer,
                    :, program,
                    registered,
                    :,
                ] = operator
    return tensor.reshape(256, 32)


def registered_update(
    carrier: c323.FixedProgramCarrier,
    predicate: np.ndarray | None = None,
    *,
    require_selected_table: bool = True,
) -> np.ndarray:
    reversible = registration_unitary(
        predicate,
        require_selected_table=require_selected_table,
    )
    dilation = bit_gated_pointer_dilation(carrier)
    return dilation @ np.kron(reversible, I2)


def apply_registered_update(update: np.ndarray, state: np.ndarray) -> np.ndarray:
    return update @ state


def declared_input_encoding() -> np.ndarray:
    """Six lawful labels and one seam qubit into a blank registration M2."""

    tensor = np.zeros(
        (
            PROGRAM_DIMENSION,
            REGISTRATION_DIMENSION,
            SYSTEM_DIMENSION,
            LAWFUL_PROGRAMS,
            SYSTEM_DIMENSION,
        ),
        dtype=complex,
    )
    for program in range(LAWFUL_PROGRAMS):
        tensor[program, 0, :, program, :] = I2
    return tensor.reshape(32, 12)


def expected_registered_output(carrier: c323.FixedProgramCarrier) -> np.ndarray:
    tensor = np.zeros(
        (
            PROGRAM_DIMENSION,
            REGISTRATION_DIMENSION,
            POINTER_DIMENSION,
            SYSTEM_DIMENSION,
            LAWFUL_PROGRAMS,
            SYSTEM_DIMENSION,
        ),
        dtype=complex,
    )
    for program in range(LAWFUL_PROGRAMS):
        for pointer, operator in enumerate(carrier.block_kraus[program]):
            tensor[program, 1, pointer, :, program, :] = operator
    return tensor.reshape(256, 12)


def validate_declared_inputs(
    program_state: np.ndarray,
    *,
    registration_blank: int,
    pointer_blank: int,
) -> None:
    c323.validate_program_state(program_state)
    if registration_blank != 0:
        raise ValueError("the reversible predicate interface requires blank registration zero")
    c323.validate_pointer_blank(pointer_blank)


def predicate_and_reversibility_controls() -> None:
    predicate = lawful_projector()
    reversible = registration_unitary()
    blank = blank_registration_encoding()
    registered = reversible @ blank
    constraint = registration_constraint()
    truth_failures = 0
    for program in range(PROGRAM_DIMENSION):
        basis = np.zeros(PROGRAM_DIMENSION)
        basis[program] = 1
        output = reversible @ np.kron(basis, np.asarray((1, 0)))
        expected = np.kron(
            basis,
            np.eye(2)[int(program < LAWFUL_PROGRAMS)],
        )
        truth_failures += int(np.linalg.norm(output - expected) >= TOL)
    detail = {
        "predicate_rank": int(round(float(np.trace(predicate).real))),
        "predicate_projector_residual": float(
            np.linalg.norm(predicate @ predicate - predicate)
        ),
        "registration_unitary_residual": float(
            np.linalg.norm(reversible.conj().T @ reversible - np.eye(16))
        ),
        "registration_involution_residual": float(
            np.linalg.norm(reversible @ reversible - np.eye(16))
        ),
        "truth_table_failures": truth_failures,
        "registered_constraint_residual": float(
            np.linalg.norm(constraint @ registered - registered)
        ),
        "predicate_support_M2": 3,
        "reversible_registration_support_M2": 4,
    }
    check(
        "one fixed reversible four-M2 gate computes the supplied six-label code predicate into one local registration M2",
        detail["predicate_rank"] == 6
        and detail["predicate_projector_residual"] < TOL
        and detail["registration_unitary_residual"] < TOL
        and detail["registration_involution_residual"] < TOL
        and detail["truth_table_failures"] == 0
        and detail["registered_constraint_residual"] < TOL,
        detail,
    )


def exact_code_space_controls(carrier: c323.FixedProgramCarrier) -> None:
    update = registered_update(carrier)
    encoded_input = declared_input_encoding()
    expected = expected_registered_output(carrier)
    recovered = update @ encoded_input

    amplitudes = np.asarray(
        (1, 1j, -2, 0.5j, -1j, 2),
        dtype=complex,
    )
    amplitudes /= np.linalg.norm(amplitudes)
    system = np.asarray((1, 1j), dtype=complex) / np.sqrt(2)
    coherent_logical = np.kron(amplitudes, system)
    application_source = " ".join(
        inspect.getsource(apply_registered_update).split()
    )
    detail = {
        "E_out_G_coarse_minus_G_registered_E_in_residual": float(
            np.linalg.norm(recovered - expected)
        ),
        "registered_update_isometry_residual": float(
            np.linalg.norm(update.conj().T @ update - np.eye(32))
        ),
        "coherent_lawful_code_residual": float(
            np.linalg.norm(
                apply_registered_update(update, encoded_input @ coherent_logical)
                - expected @ coherent_logical
            )
        ),
        "application_source": application_source,
        "input_code_dimension": 12,
        "output_pointer_dimension": POINTER_DIMENSION,
    }
    check(
        "the fixed registered update satisfies the exact code-space intertwiner and applies coherently without a host eligibility lookup",
        detail["E_out_G_coarse_minus_G_registered_E_in_residual"] < TOL
        and detail["registered_update_isometry_residual"] < TOL
        and detail["coherent_lawful_code_residual"] < TOL
        and application_source.endswith("return update @ state")
        and detail["input_code_dimension"] == 12
        and detail["output_pointer_dimension"] == 8,
        detail,
    )


def encode_registered_system_output(
    two_ray_encoding: np.ndarray,
    logical_output: np.ndarray,
) -> np.ndarray:
    tensor = logical_output.reshape(
        PROGRAM_DIMENSION,
        REGISTRATION_DIMENSION,
        POINTER_DIMENSION,
        SYSTEM_DIMENSION,
        LAWFUL_PROGRAMS,
        SYSTEM_DIMENSION,
    )
    encoded = np.einsum("xu,prquas->prqxas", two_ray_encoding, tensor)
    return encoded.reshape(
        PROGRAM_DIMENSION
        * REGISTRATION_DIMENSION
        * POINTER_DIMENSION
        * two_ray_encoding.shape[0],
        LAWFUL_PROGRAMS * SYSTEM_DIMENSION,
    )


def direct_physical_registered_output(
    two_ray_encoding: np.ndarray,
    carrier: c323.FixedProgramCarrier,
) -> np.ndarray:
    tensor = np.zeros(
        (
            PROGRAM_DIMENSION,
            REGISTRATION_DIMENSION,
            POINTER_DIMENSION,
            two_ray_encoding.shape[0],
            LAWFUL_PROGRAMS,
            SYSTEM_DIMENSION,
        ),
        dtype=complex,
    )
    for program in range(LAWFUL_PROGRAMS):
        for pointer, operator in enumerate(carrier.block_kraus[program]):
            tensor[program, 1, pointer, :, program, :] = (
                two_ray_encoding @ operator
            )
    return tensor.reshape(
        PROGRAM_DIMENSION
        * REGISTRATION_DIMENSION
        * POINTER_DIMENSION
        * two_ray_encoding.shape[0],
        LAWFUL_PROGRAMS * SYSTEM_DIMENSION,
    )


def physical_embedding_controls(
    fixtures: dict[int, c323.c321.c317.PhysicalFixture],
    carrier: c323.FixedProgramCarrier,
) -> None:
    update = registered_update(carrier)
    logical = update @ declared_input_encoding()

    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        inherited_support = c323.physical_embedding_and_support_controls(
            fixtures, carrier
        )
    inherited_green = c323.PASS == 1 and c323.FAIL == 0
    c323.PASS, c323.FAIL = old_pass, old_fail

    rows = []
    for support, (length, fixture) in zip(
        inherited_support, sorted(fixtures.items())
    ):
        encoded = encode_registered_system_output(
            fixture.two_ray_encoding,
            logical,
        )
        direct = direct_physical_registered_output(
            fixture.two_ray_encoding,
            carrier,
        )
        code_projector = (
            fixture.two_ray_encoding @ fixture.two_ray_encoding.conj().T
        )
        leakage = 0.0
        constraint = 0.0
        for program in carrier.programs:
            for operator in program.kraus:
                physical = fixture.two_ray_encoding @ operator
                leakage = max(
                    leakage,
                    float(
                        np.linalg.norm(
                            (np.eye(fixture.two_ray_encoding.shape[0]) - code_projector)
                            @ physical
                        )
                    ),
                )
                constraint = max(
                    constraint,
                    float(np.linalg.norm(fixture.constraint @ physical - physical)),
                )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "physical_EG_intertwiner_residual": float(
                    np.linalg.norm(encoded - direct)
                ),
                "registered_physical_isometry_residual": float(
                    np.linalg.norm(direct.conj().T @ direct - np.eye(12))
                ),
                "matter_code_leakage": leakage,
                "role_constraint_residual": constraint,
                "maximum_registered_controlled_support_M2": support[
                    "maximum_one_use_controlled_M2"
                ]
                + 1,
                "registered_patch_M2": support["one_use_patch_M2"] + 1,
                "installed_overhead_M2_per_cell": 23 + 3 + 1 + 3,
                "port_constraint_failures": support["port_constraint_failures"],
                "local_check_or_Wilson_failures": support[
                    "local_check_or_Wilson_failures"
                ],
            }
        )
    check(
        "the exact registered intertwiner has bounded physical M2 support, local constraints, and zero leakage through held L=6",
        inherited_green
        and {row["L"] for row in rows} == {3, 6}
        and all(
            row["physical_EG_intertwiner_residual"] < TOL
            and row["registered_physical_isometry_residual"] < TOL
            and row["matter_code_leakage"] < TOL
            and row["role_constraint_residual"] < TOL
            and row["maximum_registered_controlled_support_M2"] <= 27
            and row["registered_patch_M2"] == 63
            and row["installed_overhead_M2_per_cell"] == 30
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in rows
        ),
        rows,
    )


def covariance_mass_contact_controls(
    fixtures: dict[int, c323.c321.c317.PhysicalFixture],
    carrier: c323.FixedProgramCarrier,
) -> None:
    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        covariance = c323.covariance_controls(fixtures, carrier)
    inherited_green = c323.PASS == 1 and c323.FAIL == 0
    c323.PASS, c323.FAIL = old_pass, old_fail

    reversible = registration_unitary()
    scalar_frame = np.eye(16)
    registration_frame_commutator = float(
        np.linalg.norm(reversible @ scalar_frame - scalar_frame @ reversible)
    )
    species = c382.c317.c311.c219.common_species(-0.3)
    mass_residual = abs(
        c382.c317.c311.c219.rest_mass(species) / species.analytic_mass - 1
    )
    contact_rows = tuple(
        {
            "L": length,
            "held": length == 6,
            "contact_intertwiner": float(
                np.linalg.norm(
                    fixture.physical_contact @ fixture.two_ray_encoding
                    - fixture.two_ray_encoding @ fixture.contact
                )
            ),
        }
        for length, fixture in sorted(fixtures.items())
    )
    detail = {
        "inherited_Cycle323_covariance_green": inherited_green,
        "proper_cubic_frames": covariance["frames"],
        "branch_failures": covariance["branch_failures"],
        "maximum_carrier_covariance_residual": max(
            covariance["maximum_one_use_carrier_residual"],
            covariance["maximum_two_use_carrier_residual"],
        ),
        "registration_scalar_frame_commutator": registration_frame_commutator,
        "one_particle_mass_relative_residual": mass_residual,
        "contact_rows": contact_rows,
    }
    check(
        "the local registration carrier preserves the actual contact and mass fixture and is scalar-covariant with the landed Cycle-323 carrier in all 24 frames",
        inherited_green
        and covariance["frames"] == 24
        and covariance["branch_failures"] == 0
        and detail["maximum_carrier_covariance_residual"] < TOL
        and registration_frame_commutator < TOL
        and mass_residual < 3e-12
        and all(row["contact_intertwiner"] < TOL for row in contact_rows),
        detail,
    )


def deletion_controls(carrier: c323.FixedProgramCarrier) -> None:
    expected = expected_registered_output(carrier)
    encoded_input = declared_input_encoding()

    missing_label = lawful_projector().copy()
    missing_label[2, 2] = 0
    missing_update = registered_update(
        carrier,
        missing_label,
        require_selected_table=False,
    )
    missing_label_residual = float(
        np.linalg.norm(missing_update @ encoded_input - expected)
    )

    deleted_predicate = np.zeros((PROGRAM_DIMENSION, PROGRAM_DIMENSION), dtype=complex)
    deleted_update = registered_update(
        carrier,
        deleted_predicate,
        require_selected_table=False,
    )
    deleted_predicate_residual = float(
        np.linalg.norm(deleted_update @ encoded_input - expected)
    )

    constraint = registration_constraint()
    broken_constraint = constraint.copy()
    broken_constraint[2 * 2 + 1, 2 * 2 + 1] = 0
    registered = registration_unitary() @ blank_registration_encoding()
    constraint_deletion_residual = float(
        np.linalg.norm(broken_constraint @ registered - registered)
    )

    dilation = bit_gated_pointer_dilation(carrier).reshape(
        PROGRAM_DIMENSION,
        REGISTRATION_DIMENSION,
        POINTER_DIMENSION,
        SYSTEM_DIMENSION,
        PROGRAM_DIMENSION,
        REGISTRATION_DIMENSION,
        SYSTEM_DIMENSION,
    )
    branch_deleted = dilation.copy()
    branch_deleted[2, 1, 0, :, 2, 1, :] = 0
    branch_deleted = branch_deleted.reshape(256, 32)
    branch_defect = float(
        np.linalg.norm(branch_deleted.conj().T @ branch_deleted - np.eye(32), 2)
    )
    detail = {
        "one_lawful_label_predicate_deletion_EG_residual": missing_label_residual,
        "whole_predicate_deletion_EG_residual": deleted_predicate_residual,
        "one_registration_constraint_sector_deletion_residual": constraint_deletion_residual,
        "one_admitted_pointer_branch_deletion_isometry_defect": branch_defect,
    }
    check(
        "predicate-label, predicate, constraint-sector, and admitted pointer-branch deletions are all detected",
        missing_label_residual > 1.9
        and deleted_predicate_residual > 4.0
        and constraint_deletion_residual > 0.99
        and branch_defect > 0.7,
        detail,
    )


def domain_controls(carrier: c323.FixedProgramCarrier) -> None:
    legal = np.zeros(PROGRAM_DIMENSION, dtype=complex)
    legal[0] = 1
    bad_shape = np.eye(7, dtype=complex)
    nonhermitian = lawful_projector().copy()
    nonhermitian[0, 1] = 0.2
    nonprojector = lawful_projector().copy()
    nonprojector[0, 0] = 0.5
    wrong_table = lawful_projector().copy()
    wrong_table[5, 5] = 0
    wrong_table[6, 6] = 1
    malformed_calls = (
        lambda: validate_declared_inputs(
            legal[:7], registration_blank=0, pointer_blank=0
        ),
        lambda: validate_declared_inputs(
            2 * legal, registration_blank=0, pointer_blank=0
        ),
        lambda: validate_declared_inputs(
            np.eye(PROGRAM_DIMENSION)[6],
            registration_blank=0,
            pointer_blank=0,
        ),
        lambda: validate_declared_inputs(
            legal, registration_blank=1, pointer_blank=0
        ),
        lambda: validate_declared_inputs(
            legal, registration_blank=0, pointer_blank=1
        ),
        lambda: registration_unitary(bad_shape),
        lambda: registration_unitary(nonhermitian),
        lambda: registration_unitary(nonprojector),
        lambda: registration_unitary(wrong_table),
        lambda: registered_update(
            c323.FixedProgramCarrier(carrier.programs[:5])
        ),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (ValueError, IndexError):
            rejected += 1
    check(
        "the declared local domain rejects malformed program states, nonblank ancillas, predicates, and carrier tables",
        rejected == len(malformed_calls),
        {"rejected": rejected, "attempted": len(malformed_calls)},
    )


def semantic_inventory_controls() -> None:
    detail = {
        "result": "finite local six-label code predicate and bit-gated dilation",
        "six_program_table": "supplied Cycle-382 table",
        "continuous_rays_and_effect_scales": "supplied",
        "continuous_coefficient_synthesis": "supplied numerical assembly",
        "three_M2_program_state_preparation": "supplied",
        "registration_M2_blank": "supplied",
        "pointer_M2_blank": "supplied",
        "predicate_membership_set": "supplied fixed six-label code",
        "layer_ordering": "supplied registration-then-dilation order",
        "dynamic_admission_rule": None,
        "irreversible_registration": None,
        "universal_menu_eligibility": False,
        "effect_functionality": False,
        "numerical_grade": None,
        "Born_law": None,
        "occurrence": None,
        "Record": None,
        "physical_clock_or_time_law": None,
        "global_parity_service": None,
        "preferred_spatial_ordering": None,
        "authority": "none",
        "audit": "unset",
        "axiom_pressure": None,
    }
    check(
        "the finite registration inventory exposes all preparation, coefficient, ancilla, admission, irreversibility, and scheduling walls",
        detail["dynamic_admission_rule"] is None
        and detail["irreversible_registration"] is None
        and detail["universal_menu_eligibility"] is False
        and detail["effect_functionality"] is False
        and detail["numerical_grade"] is None
        and detail["Born_law"] is None
        and detail["occurrence"] is None
        and detail["Record"] is None
        and detail["physical_clock_or_time_law"] is None
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
        length: c382.c317.physical_fixture(length)
        for length in (3, 6)
    }
    schemas = c382.selected_schema_table()
    carrier = c382.make_carrier(schemas, fixtures[3].contact)

    predicate_and_reversibility_controls()
    exact_code_space_controls(carrier)
    physical_embedding_controls(fixtures, carrier)
    covariance_mass_contact_controls(fixtures, carrier)
    deletion_controls(carrier)
    domain_controls(carrier)
    semantic_inventory_controls()

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
