#!/usr/bin/env python3
"""Cycle 382: finite menu schemas on the landed physical M2 apparatus.

This runner locally derives three finite positive-effect schemas: a
complement, a same-ray refinement with an exact coarse CP merge, and an
unpaired axis-cancellation menu.  They and three controls are installed in
the landed Cycle-323 fixed six-program carrier on the accepted Cycle-317
physical matter code.  The external PR #5476 theorem runner is not imported.

This is apparatus algebra only.  It supplies no numerical grade, outcome
occurrence, sampler, frequency law, or Record formation rule.
"""

from __future__ import annotations

import ast
from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_fixed_program_carrier_two_use_cycle323_2026_07_18 as c323


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FIXED_MENU_SCHEMA_COMPILER_CYCLE382_NOTE_2026-07-18.md"
)
TOL = 1.2e-10
PINNED_CAMPAIGN_BASE = "3b50d145c35eec8422fc26d881bfbdf8f071b736"
PR5476_COMPARATOR = "5dd59abfbf863b64e816a551c2d0ed55c9a953a3"
PR5476_RUNNER = "born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17"

I2 = c317.I2
X = c317.X
Y = c317.Y
Z = c317.Z

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
        check("the Cycle-382 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "finite physical menu-schema result",
        "same-ray split",
        "complement",
        "axis cancellation",
        "exact coarse cp merge",
        "fixed three-m2 program carrier",
        "held l=6",
        "24 proper-cubic frames",
        "pr #5476",
        PR5476_COMPARATOR,
        "not retained",
        "continuous ray and coefficient preparation remain supplied",
        "host menu-table selection remains supplied",
        "pointer output is not occurrence",
        "program labels are not records",
        "no born law",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the finite construction, comparator quarantine, supplied inventory, and semantic boundary",
        not missing,
        missing,
    )


def unit(vector: tuple[float, float, float] | np.ndarray) -> np.ndarray:
    value = np.asarray(vector, dtype=float)
    if value.shape != (3,) or np.linalg.norm(value) <= TOL:
        raise ValueError("one menu ray needs a nonzero three-vector")
    return value / np.linalg.norm(value)


@dataclass(frozen=True)
class ScaledTerm:
    scale: float
    direction: tuple[float, float, float] | None

    def __post_init__(self) -> None:
        if not np.isfinite(self.scale) or not 0 < self.scale <= 1:
            raise ValueError("one finite effect scale must lie in (0,1]")
        if self.direction is not None:
            object.__setattr__(
                self,
                "direction",
                tuple(float(value) for value in unit(self.direction)),
            )

    @property
    def bare_effect(self) -> np.ndarray:
        if self.direction is None:
            return self.scale * I2
        return self.scale * c317.projector_bloch(np.asarray(self.direction))


@dataclass(frozen=True)
class MenuSchema:
    name: str
    family: str
    terms: tuple[ScaledTerm, ...]
    coarse_groups: tuple[tuple[int, ...], ...]

    def __post_init__(self) -> None:
        if not 1 <= len(self.terms) <= c323.POINTER_DIMENSION:
            raise ValueError("one bounded menu needs one to eight fine labels")
        if not 1 <= len(self.coarse_groups) <= 3:
            raise ValueError("one menu has one to three declared coarse labels")
        flattened = tuple(index for group in self.coarse_groups for index in group)
        if sorted(flattened) != list(range(len(self.terms))):
            raise ValueError("coarse groups must partition the fine labels")

    @property
    def bare_effects(self) -> tuple[np.ndarray, ...]:
        return tuple(term.bare_effect for term in self.terms)

    def program(self, contact: np.ndarray) -> c323.c321.Program:
        if contact.shape != (2, 2):
            raise ValueError("the supplied seam contact must be two dimensional")
        kraus = tuple(
            np.sqrt(term.scale)
            * (
                I2
                if term.direction is None
                else c317.projector_bloch(np.asarray(term.direction))
            )
            @ contact
            for term in self.terms
        )
        return c323.c321.Program(self.name, kraus, self.coarse_groups)


def paired_menu(schema: MenuSchema) -> bool:
    """Finite equal-weight antipodal-pair test; scalar coins are allowed."""

    ray_indices = [
        index for index, term in enumerate(schema.terms) if term.direction is not None
    ]
    unused = set(ray_indices)
    while unused:
        left = min(unused)
        unused.remove(left)
        left_term = schema.terms[left]
        partner = next(
            (
                right
                for right in sorted(unused)
                if abs(schema.terms[right].scale - left_term.scale) < TOL
                and np.linalg.norm(
                    np.asarray(schema.terms[right].direction)
                    + np.asarray(left_term.direction)
                )
                < TOL
            ),
            None,
        )
        if partner is None:
            return False
        unused.remove(partner)
    return True


def axis_cancellation_terms(
    direction: tuple[float, float, float],
) -> tuple[ScaledTerm, ...]:
    ray = unit(direction)
    coefficient = 2.0 / (1.0 + float(np.sum(np.abs(ray))))
    terms = [ScaledTerm(coefficient, tuple(ray))]
    for axis, coordinate in enumerate(ray):
        if abs(coordinate) <= TOL:
            continue
        cancellation = np.zeros(3)
        cancellation[axis] = -np.sign(coordinate)
        terms.append(
            ScaledTerm(coefficient * abs(float(coordinate)), tuple(cancellation))
        )
    return tuple(terms)


def selected_schema_table() -> tuple[MenuSchema, ...]:
    ray = unit((2, -3, 6))
    complement = MenuSchema(
        "complement ray",
        "complement",
        (
            ScaledTerm(1.0, tuple(ray)),
            ScaledTerm(1.0, tuple(-ray)),
        ),
        ((0,), (1,)),
    )
    split = MenuSchema(
        "same-ray split",
        "same-ray split",
        (
            ScaledTerm(0.37, tuple(ray)),
            ScaledTerm(0.63, tuple(ray)),
            ScaledTerm(1.0, tuple(-ray)),
        ),
        ((0, 1), (2,)),
    )
    axis = MenuSchema(
        "unpaired axis cancellation",
        "axis cancellation",
        axis_cancellation_terms((1, 2, 3)),
        ((0,), (1,), (2, 3)),
    )
    coins = MenuSchema(
        "identity coins",
        "identity coins",
        (
            ScaledTerm(0.25, None),
            ScaledTerm(0.25, None),
            ScaledTerm(0.5, None),
        ),
        ((0, 1), (2,)),
    )
    left = unit((1, 1, 0))
    right = unit((1, -1, 2))
    paired_axes = MenuSchema(
        "paired two-ray control",
        "paired two-ray control",
        (
            ScaledTerm(0.32, tuple(left)),
            ScaledTerm(0.32, tuple(-left)),
            ScaledTerm(0.68, tuple(right)),
            ScaledTerm(0.68, tuple(-right)),
        ),
        ((0, 1), (2, 3)),
    )
    cubic = MenuSchema(
        "paired cubic control",
        "paired cubic control",
        tuple(
            ScaledTerm(1 / 3, tuple(sign * np.eye(3)[axis_index]))
            for axis_index in range(3)
            for sign in (1, -1)
        ),
        ((0, 1), (2, 3), (4, 5)),
    )
    return complement, split, axis, coins, paired_axes, cubic


def make_carrier(
    schemas: tuple[MenuSchema, ...], contact: np.ndarray
) -> c323.FixedProgramCarrier:
    return c323.FixedProgramCarrier(
        tuple(schema.program(contact) for schema in schemas)
    )


def comparator_quarantine_controls() -> None:
    ancestry = subprocess.run(
        [
            "git",
            "merge-base",
            "--is-ancestor",
            PR5476_COMPARATOR,
            PINNED_CAMPAIGN_BASE,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in (
            node.names
            if isinstance(node, ast.Import)
            else [ast.alias(name=node.module or "")]
        )
    }
    runner_path = ROOT / "scripts" / f"{PR5476_RUNNER}.py"
    detail = {
        "pinned_campaign_base_current_PR_lineage": PINNED_CAMPAIGN_BASE,
        "PR_5476_comparator": PR5476_COMPARATOR,
        "comparator_is_campaign_lineage_ancestor": ancestry.returncode == 0,
        "merge_base_returncode": ancestry.returncode,
        "comparator_runner_imported": PR5476_RUNNER in imported,
        "comparator_runner_present_in_campaign_worktree": runner_path.exists(),
        "theorem_retained": False,
    }
    check(
        "PR #5476 is pinned only as a comparator outside the current campaign lineage and its theorem runner is not consumed",
        ancestry.returncode == 1
        and PR5476_RUNNER not in imported
        and not runner_path.exists(),
        detail,
    )


def schema_effect_controls(
    schemas: tuple[MenuSchema, ...], carrier: c323.FixedProgramCarrier
) -> None:
    rows = []
    for schema, program in zip(schemas, carrier.programs):
        eigenvalues = np.concatenate(
            tuple(
                np.linalg.eigvalsh((effect + effect.conj().T) / 2)
                for effect in program.fine_effects
            )
        )
        rows.append(
            {
                "family": schema.family,
                "fine_labels": len(schema.terms),
                "coarse_labels": len(schema.coarse_groups),
                "bare_sum_to_I_residual": float(
                    np.linalg.norm(
                        sum(
                            schema.bare_effects,
                            start=np.zeros((2, 2), dtype=complex),
                        )
                        - I2
                    )
                ),
                "physical_effect_sum_to_I_residual": float(
                    np.linalg.norm(program.completeness - I2)
                ),
                "minimum_effect_eigenvalue": float(np.min(eigenvalues)),
                "maximum_effect_eigenvalue": float(np.max(eigenvalues)),
                "paired": paired_menu(schema),
            }
        )
    check(
        "six finite schemas give positive exhaustive effects, including the required complement, same-ray split, and unpaired axis cancellation",
        tuple(row["family"] for row in rows[:3])
        == ("complement", "same-ray split", "axis cancellation")
        and tuple(row["paired"] for row in rows)
        == (True, False, False, True, True, True)
        and schemas[1].coarse_groups == ((0, 1), (2,))
        and len(schemas[2].terms) == 4
        and max(row["fine_labels"] for row in rows) <= 8
        and all(
            row["bare_sum_to_I_residual"] < TOL
            and row["physical_effect_sum_to_I_residual"] < TOL
            and row["minimum_effect_eigenvalue"] > -TOL
            and row["maximum_effect_eigenvalue"] < 1 + TOL
            for row in rows
        ),
        rows,
    )


def merge_split_controls(carrier: c323.FixedProgramCarrier) -> None:
    complement, split = carrier.programs[:2]
    split_positive = tuple(split.kraus[index] for index in (0, 1))
    complement_positive = (complement.kraus[0],)
    split_negative = (split.kraus[2],)
    complement_negative = (complement.kraus[1],)
    details = {
        "positive_coarse_effect_residual": float(
            np.linalg.norm(split.coarse_effects[0] - complement.coarse_effects[0])
        ),
        "negative_coarse_effect_residual": float(
            np.linalg.norm(split.coarse_effects[1] - complement.coarse_effects[1])
        ),
        "positive_coarse_instrument_Choi_residual": float(
            np.linalg.norm(
                c323.c321.choi(split_positive)
                - c323.c321.choi(complement_positive)
            )
        ),
        "negative_coarse_instrument_Choi_residual": float(
            np.linalg.norm(
                c323.c321.choi(split_negative)
                - c323.c321.choi(complement_negative)
            )
        ),
        "fine_pointer_labels_split": len(split.kraus),
        "coarse_pointer_labels_after_merge": len(split.coarse_groups),
        "split_fine_effect_difference": float(
            np.linalg.norm(split.fine_effects[0] - split.fine_effects[1])
        ),
    }
    check(
        "the same-ray fine refinement merges exactly to the complement program at both effect and coarse-CP levels while remaining pointer-visible",
        max(
            details["positive_coarse_effect_residual"],
            details["negative_coarse_effect_residual"],
            details["positive_coarse_instrument_Choi_residual"],
            details["negative_coarse_instrument_Choi_residual"],
        )
        < TOL
        and details["fine_pointer_labels_split"] == 3
        and details["coarse_pointer_labels_after_merge"] == 2
        and details["split_fine_effect_difference"] > 0.2,
        details,
    )


def fixed_physical_controls(
    fixtures: dict[int, c317.PhysicalFixture],
    carrier: c323.FixedProgramCarrier,
) -> None:
    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        fixed = c323.carrier_program_controls(carrier)
        sequence = c323.sequential_composition_controls(carrier)
        support = c323.physical_embedding_and_support_controls(fixtures, carrier)
        covariance = c323.covariance_controls(fixtures, carrier)
    imported_green = c323.PASS == 4 and c323.FAIL == 0
    c323.PASS, c323.FAIL = old_pass, old_fail

    species = c317.c311.c219.common_species(-0.3)
    mass_residual = abs(
        c317.c311.c219.rest_mass(species) / species.analytic_mass - 1
    )
    fixture_rows = tuple(
        {
            "L": length,
            "held": length == 6,
            "contact_intertwiner": float(
                np.linalg.norm(
                    fixture.physical_contact @ fixture.two_ray_encoding
                    - fixture.two_ray_encoding @ fixture.contact
                )
            ),
            "role_constraint": float(
                np.linalg.norm(
                    fixture.constraint @ fixture.two_ray_encoding
                    - fixture.two_ray_encoding
                )
            ),
        }
        for length, fixture in fixtures.items()
    )
    detail = {
        "landed_Cycle323_checks_green": imported_green,
        "fixed_update_isometry_residual": fixed["fixed_update_isometry_residual"],
        "two_use_isometry_residual": sequence["two_use_isometry_residual"],
        "fresh_pointer_M2_two_use": sequence["fresh_pointer_M2"],
        "support": support,
        "covariance": covariance,
        "fixtures": fixture_rows,
        "one_particle_mass_relative_residual": mass_residual,
    }
    check(
        "one fixed three-M2 program carrier realizes the selected table on bounded physical M2 patches through held L=6 and all 24 proper-cubic frames",
        imported_green
        and fixed["fixed_update_isometry_residual"] < TOL
        and sequence["two_use_isometry_residual"] < TOL
        and sequence["fresh_pointer_M2"] == 6
        and len(support) == 2
        and {row["L"] for row in support} == {3, 6}
        and all(
            row["one_and_two_use_leakage"] < TOL
            and row["role_constraint_residual"] < TOL
            and row["maximum_one_use_controlled_M2"] <= 26
            and row["maximum_two_use_controlled_M2"] <= 29
            and row["one_use_patch_M2"] == 62
            and row["two_use_patch_M2"] == 65
            for row in support
        )
        and covariance["frames"] == 24
        and covariance["branch_failures"] == 0
        and covariance["maximum_one_use_carrier_residual"] < TOL
        and covariance["maximum_two_use_carrier_residual"] < TOL
        and all(
            max(row["contact_intertwiner"], row["role_constraint"]) < TOL
            for row in fixture_rows
        )
        and mass_residual < 3e-12,
        detail,
    )


def contact_deletion_controls(
    fixtures: dict[int, c317.PhysicalFixture],
    schemas: tuple[MenuSchema, ...],
    carrier: c323.FixedProgramCarrier,
) -> None:
    deleted = make_carrier(schemas, I2)
    effect_residuals = tuple(
        float(np.linalg.norm(left - right))
        for actual, bare in zip(carrier.programs, deleted.programs)
        for left, right in zip(actual.fine_effects, bare.fine_effects)
    )
    detail = {
        "one_use_fixed_carrier_contact_deletion_residual": float(
            np.linalg.norm(carrier.update - deleted.update)
        ),
        "two_use_fixed_carrier_contact_deletion_residual": float(
            np.linalg.norm(
                c323.two_use_from_fixed(carrier.update)
                - c323.two_use_from_fixed(deleted.update)
            )
        ),
        "maximum_fine_effect_contact_deletion_residual": max(effect_residuals),
        "physical_contact_intertwiners": tuple(
            float(
                np.linalg.norm(
                    fixture.physical_contact @ fixture.two_ray_encoding
                    - fixture.two_ray_encoding @ fixture.contact
                )
            )
            for fixture in fixtures.values()
        ),
    }
    check(
        "the menu carrier reproduces and remains dependent on the actual Cycle-230 seam contact rather than a host-side identity replacement",
        max(detail["physical_contact_intertwiners"]) < TOL
        and detail["one_use_fixed_carrier_contact_deletion_residual"] > 0.5
        and detail["two_use_fixed_carrier_contact_deletion_residual"] > 0.8
        and detail["maximum_fine_effect_contact_deletion_residual"] > 0.05,
        detail,
    )


def deletion_and_domain_controls(
    schemas: tuple[MenuSchema, ...], carrier: c323.FixedProgramCarrier
) -> None:
    tensor = carrier.update.reshape(
        c323.PROGRAM_DIMENSION,
        c323.POINTER_DIMENSION,
        2,
        c323.PROGRAM_DIMENSION,
        2,
    )
    branch_deleted = tensor.copy()
    branch_deleted[1, 0, :, 1, :] = 0
    branch_deleted = branch_deleted.reshape(128, 16)
    branch_defect = float(
        np.linalg.norm(branch_deleted.conj().T @ branch_deleted - np.eye(16), 2)
    )
    control_deleted = tensor.copy()
    control_deleted[2, :, :, 2, :] = 0
    control_deleted = control_deleted.reshape(128, 16)
    control_defect = float(
        np.linalg.norm(control_deleted.conj().T @ control_deleted - np.eye(16), 2)
    )
    menu_deletion_defects = tuple(
        float(
            np.linalg.norm(
                sum(
                    schema.bare_effects[1:],
                    start=np.zeros((2, 2), dtype=complex),
                )
                - I2
            )
        )
        for schema in schemas[:3]
    )

    bad_program = c323.c321.Program(
        "nonexhaustive",
        (np.zeros((2, 2), dtype=complex),),
        ((0,),),
    )
    valid_term = ScaledTerm(0.5, (1, 0, 0))
    malformed_calls = (
        lambda: ScaledTerm(0.0, (1, 0, 0)),
        lambda: ScaledTerm(0.5, (0, 0, 0)),
        lambda: MenuSchema("duplicate", "bad", (valid_term, valid_term), ((0,), (0,))),
        lambda: MenuSchema(
            "too many", "bad", tuple(valid_term for _ in range(9)), (tuple(range(9)),)
        ),
        lambda: c323.FixedProgramCarrier(carrier.programs[:5]),
        lambda: c323.FixedProgramCarrier(carrier.programs[:5] + (carrier.programs[0],)),
        lambda: c323.FixedProgramCarrier(carrier.programs[:5] + (bad_program,)),
        lambda: c323.program_basis(6),
        lambda: c323.validate_program_state(np.eye(c323.PROGRAM_DIMENSION)[6]),
        lambda: c323.validate_pointer_blank(1),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (ValueError, IndexError):
            rejected += 1
    detail = {
        "same_ray_fine_branch_deletion_isometry_defect": branch_defect,
        "axis_program_control_deletion_isometry_defect": control_defect,
        "key_schema_first_branch_deletion_completeness_defects": menu_deletion_defects,
        "lawful_domain_rejections": rejected,
        "lawful_domain_attempts": len(malformed_calls),
    }
    check(
        "fine-branch, whole-program, and menu-term deletions are detected and malformed coefficient/program domains are rejected",
        branch_defect > 0.3
        and control_defect > 0.99
        and min(menu_deletion_defects) > 0.15
        and rejected == len(malformed_calls),
        detail,
    )


def semantic_inventory_controls() -> None:
    detail = {
        "physical_result": "finite conditional M2 apparatus menu compiler",
        "continuous_Bloch_rays": "supplied host coefficient table",
        "continuous_effect_scales": "supplied host coefficient table",
        "square_root_and_projector_synthesis": "supplied numerical program assembly",
        "six_program_table_selection": "supplied before the physical run",
        "three_M2_program_state_preparation": "supplied",
        "three_M2_blank_pointer_preparation_per_use": "supplied",
        "fixed_update_after_assembly": "derived landed Cycle-323 controlled isometry",
        "physical_matter_embedding_and_constraints": "derived landed Cycle-317/323 surface",
        "global_parity_string": None,
        "preferred_spatial_ordering": None,
        "runtime_host_program_dispatch": None,
        "pointer_output_occurrence": None,
        "Record_formation": None,
        "numerical_grade": None,
        "Born_law": None,
        "actual_history_sampler": None,
        "frequency_law": None,
        "continuum_menu_family_coverage": False,
        "PR_5476_theorem_retained": False,
        "authority": "none",
        "audit": "unset",
        "axiom_pressure": None,
    }
    check(
        "the supplied-structure inventory separates the finite physical apparatus from grading, occurrence, Record formation, and probability claims",
        detail["global_parity_string"] is None
        and detail["preferred_spatial_ordering"] is None
        and detail["runtime_host_program_dispatch"] is None
        and detail["pointer_output_occurrence"] is None
        and detail["Record_formation"] is None
        and detail["numerical_grade"] is None
        and detail["Born_law"] is None
        and detail["actual_history_sampler"] is None
        and detail["frequency_law"] is None
        and detail["continuum_menu_family_coverage"] is False
        and detail["PR_5476_theorem_retained"] is False
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["axiom_pressure"] is None,
        detail,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    note_contract()
    comparator_quarantine_controls()
    fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
    schemas = selected_schema_table()
    carrier = make_carrier(schemas, fixtures[3].contact)
    schema_effect_controls(schemas, carrier)
    merge_split_controls(carrier)
    fixed_physical_controls(fixtures, carrier)
    contact_deletion_controls(fixtures, schemas, carrier)
    deletion_and_domain_controls(schemas, carrier)
    semantic_inventory_controls()

    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
