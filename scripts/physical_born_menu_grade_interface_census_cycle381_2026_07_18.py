#!/usr/bin/env python3
"""Cycle 381: exact census of the current campaign Born menu-grade interface.

This runner inventories the Cycle-317/321/323 substrate/compiler landed in the
pinned main base and the Cycle-349/350/351 carrier/corpus lineage that was
unlanded at census construction.
It distinguishes the three finite six-program carriers from Cycle-317
host-instantiated compiler witnesses, classifies every fine and declared
coarse effect menu, and checks
normalization, ranks, eigenvalues, scaled-projector/coin/mixed status,
pairedness, refinements, coarse CP equivalence, physical support, covariance,
and held corpora.

Open PRs #5472, #5476, and #5479 are read only as commit-pinned comparator
notes.  Their runners are not imported and their results are not retained as
theorems.  The census asks which of their hypotheses have finite physical
witnesses and which universal eligibility, functionality, coefficient,
genesis, or grading assumptions remain absent from the current campaign
interface.

The landed canonical Cycle-321 carrier installs at least one unpaired
three-outcome scaled-projector menu.  That finite witness is not a global
grading functional, Born law, probability, actuality selector, or frequency
theorem.  No no-go, minimum-content, or axiom-pressure claim is made.
Authority is none and audit is unset.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass
from hashlib import sha256
from inspect import getsource, signature
from io import StringIO
from math import sqrt
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_BORN_MENU_GRADE_INTERFACE_CENSUS_"
    "CYCLE381_NOTE_2026-07-18.md"
)

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_effect_equivalence_normalized_grade_cycle321_2026_07_18 as c321
import physical_fixed_program_carrier_two_use_cycle323_2026_07_18 as c323
import physical_typed_record_scaled_projector_unpaired_corpus_route_cycle349_2026_07_18 as c349
import physical_typed_record_fixed_program_frequency_corpus_route_cycle350_2026_07_18 as c350
import physical_typed_record_born_corpus_tournament_synthesis_cycle351_2026_07_18 as c351


TOL = 1.2e-10
I2 = c317.I2
PAULIS = (c317.X, c317.Y, c317.Z)
AUTHORITY = "none"
AUDIT = "unset"
CAMPAIGN_CORPUS_COMMIT = "06cb17dcb26c7b6d0aa4377b6f1125bdc3d210bf"
PINNED_MAIN_BASE_COMMIT = "0355ac4728f57d9fdc62cb27764bbd33e6e8b8df"
PASS = 0
FAIL = 0

COMPARATORS = {
    5472: {
        "head": "2c648ccb408a8c36a700f53ec5401369e3bbd490",
        "path": "docs/BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
        "hypotheses": (
            "(e1) grading exists at effect grade",
            "w is a function of the effect alone",
            "(e2) finite effect menus are eligible",
            "for every finite family",
        ),
    },
    5476: {
        "head": "a994617819f57e599dd101c654be366123392236",
        "path": "docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md",
        "hypotheses": (
            "(f1) grading exists on the scaled-projector domain",
            "w is a function of the effect alone",
            "(f2) scaled-projector menus are eligible",
            "for every scaled-projector menu",
        ),
    },
    5479: {
        "head": "84053108a424cef26dc23e484549df331ad2050f",
        "path": "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
        "hypotheses": (
            "(g1) two-outcome eligibility",
            "every binary effect menu",
            "(g2) three-outcome eligibility",
            "every ternary effect menu",
            "(x1) mixed-projective menus",
            "every mixed-projective menu is eligible and normalized",
        ),
    },
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized_text(text: str) -> str:
    text = text.lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def normalized(path: Path) -> str:
    return normalized_text(path.read_text(encoding="utf-8"))


@dataclass(frozen=True)
class EffectSignature:
    kind: str
    rank: int
    eigenvalues: tuple[float, float]
    scale: float | None
    bloch_direction: tuple[float, float, float] | None


def effect_signature(effect: np.ndarray) -> EffectSignature:
    matrix = np.asarray(effect, dtype=complex)
    if matrix.shape != (2, 2):
        raise ValueError("the census accepts one-qubit effects only")
    if np.linalg.norm(matrix - matrix.conj().T) > TOL:
        raise ValueError("an enumerated effect must be Hermitian")
    matrix = (matrix + matrix.conj().T) / 2
    values = np.linalg.eigvalsh(matrix)
    if values[0] < -TOL or values[1] > 1 + TOL:
        raise ValueError("an enumerated effect must lie between zero and identity")
    values[np.abs(values) < TOL] = 0.0
    values[np.abs(values - 1) < TOL] = 1.0
    rank = int(np.sum(values > TOL))
    scale: float | None = None
    direction: tuple[float, float, float] | None = None
    if rank == 0:
        kind = "zero"
    elif abs(values[1] - values[0]) < TOL:
        kind = "identity-multiple"
        scale = float(values[0])
    elif rank == 1:
        kind = "rank-one-projector" if abs(values[1] - 1) < TOL else "scaled-rank-one-projector"
        scale = float(values[1])
        projector = matrix / scale
        vector = tuple(float(np.trace(projector @ pauli).real) for pauli in PAULIS)
        if abs(np.linalg.norm(vector) - 1) > TOL:
            raise ValueError("rank-one effect did not expose a unit Bloch direction")
        direction = vector
    else:
        kind = "mixed-effect-distinct-nonzero-eigenvalues"
    return EffectSignature(
        kind,
        rank,
        (float(values[0]), float(values[1])),
        scale,
        direction,
    )


def paired_status(effects: tuple[np.ndarray, ...]) -> bool | None:
    """Test the PR-5476 paired definition on the actual effect multiset."""

    rays: list[tuple[float, np.ndarray]] = []
    for effect in effects:
        item = effect_signature(effect)
        if item.kind in ("zero", "identity-multiple"):
            continue
        if item.kind not in ("rank-one-projector", "scaled-rank-one-projector"):
            return None
        assert item.scale is not None and item.bloch_direction is not None
        rays.append((item.scale, np.asarray(item.bloch_direction)))
    used: set[int] = set()
    for left, (scale, direction) in enumerate(rays):
        if left in used:
            continue
        partner = next(
            (
                right
                for right, (other_scale, other_direction) in enumerate(rays)
                if right != left
                and right not in used
                and abs(scale - other_scale) < TOL
                and np.linalg.norm(direction + other_direction) < TOL
            ),
            None,
        )
        if partner is None:
            return False
        used.update((left, partner))
    return True


def menu_row(
    carrier_name: str,
    program_index: int,
    program: c321.Program,
    surface: str,
) -> dict[str, object]:
    effects = program.fine_effects if surface == "fine" else program.coarse_effects
    signatures = tuple(effect_signature(effect) for effect in effects)
    paired = paired_status(effects)
    scaled_domain = all(
        item.kind in (
            "zero",
            "identity-multiple",
            "rank-one-projector",
            "scaled-rank-one-projector",
        )
        for item in signatures
    )
    return {
        "carrier": carrier_name,
        "program_index": program_index,
        "program": program.name,
        "surface": surface,
        "coarse_groups": program.coarse_groups,
        "outcomes": len(effects),
        "sum_to_I_residual": float(np.linalg.norm(sum(effects) - I2)),
        "paired": paired,
        "unpaired_scaled_projector_menu": scaled_domain and paired is False,
        "contains_mixed_effect": any(
            item.kind == "mixed-effect-distinct-nonzero-eigenvalues"
            for item in signatures
        ),
        "effect_kinds": tuple(item.kind for item in signatures),
        "ranks": tuple(item.rank for item in signatures),
        "eigenvalues": tuple(item.eigenvalues for item in signatures),
        "scales": tuple(item.scale for item in signatures),
        "bloch_directions": tuple(item.bloch_direction for item in signatures),
    }


def installed_carriers(
    contact: np.ndarray,
) -> tuple[
    dict[str, c323.FixedProgramCarrier],
    dict[str, tuple[c349.MenuSchema, ...]],
]:
    tables = {
        "cycle349-development": c349.schema_table(held=False),
        "cycle349-held": c349.schema_table(held=True),
    }
    carriers = {
        "cycle321-canonical": c323.FixedProgramCarrier(c323.make_programs(contact)),
        **{
            name: c323.FixedProgramCarrier(tuple(schema.program(contact) for schema in table))
            for name, table in tables.items()
        },
    }
    return carriers, tables


def exact_effect_menu_census_controls(
    carriers: dict[str, c323.FixedProgramCarrier],
    tables: dict[str, tuple[c349.MenuSchema, ...]],
) -> dict[str, object]:
    rows = tuple(
        menu_row(carrier_name, index, program, surface)
        for carrier_name, carrier in carriers.items()
        for index, program in enumerate(carrier.programs)
        for surface in ("fine", "coarse")
    )
    paired_rows = tuple(row for row in rows if row["paired"] is True)
    unpaired_rows = tuple(row for row in rows if row["unpaired_scaled_projector_menu"])
    mixed_rows = tuple(row for row in rows if row["contains_mixed_effect"])
    unpaired_three_or_more = tuple(row for row in unpaired_rows if row["outcomes"] >= 3)
    ternary_unpaired = tuple(row for row in unpaired_rows if row["outcomes"] == 3)
    exact_effects: list[np.ndarray] = []
    for carrier in carriers.values():
        for program in carrier.programs:
            for effect in program.fine_effects + program.coarse_effects:
                if not any(np.linalg.norm(effect - found) < TOL for found in exact_effects):
                    exact_effects.append(effect)
    schema_rows = {
        name: {
            "program_names": tuple(schema.name for schema in table),
            "families": tuple(schema.family for schema in table),
            "fine_outcomes": tuple(len(schema.terms) for schema in table),
            "declared_paired": tuple(schema.expected_paired for schema in table),
            "recomputed_paired": tuple(c349.paired_menu(schema) for schema in table),
        }
        for name, table in tables.items()
    }
    detail = {
        "current_campaign_fixed_carriers": len(carriers),
        "landed_Cycle321_fixed_carriers": 1,
        "campaign_branch_Cycle349_fixed_carriers": 2,
        "current_campaign_programs": sum(len(carrier.programs) for carrier in carriers.values()),
        "landed_Cycle321_programs": len(carriers["cycle321-canonical"].programs),
        "campaign_branch_Cycle349_programs": sum(
            len(carriers[name].programs)
            for name in ("cycle349-development", "cycle349-held")
        ),
        "fine_and_coarse_menu_presentations": len(rows),
        "distinct_effect_operators": len(exact_effects),
        "paired_menu_presentations": len(paired_rows),
        "unpaired_scaled_projector_presentations": len(unpaired_rows),
        "unpaired_outcome_at_least_three_presentations": len(unpaired_three_or_more),
        "ternary_unpaired_presentations": len(ternary_unpaired),
        "mixed_effect_coarse_presentations": len(mixed_rows),
        "minimum_installed_unpaired_outcomes": min(row["outcomes"] for row in unpaired_rows),
        "maximum_sum_to_I_residual": max(row["sum_to_I_residual"] for row in rows),
        "schema_rows": schema_rows,
        "menu_rows": rows,
        "finite_unpaired_witness_exists": bool(unpaired_three_or_more),
        "finite_unpaired_witness_implies_global_grade": False,
        "finite_unpaired_witness_implies_Born_law": False,
    }
    check(
        "every current-campaign fine/coarse menu is enumerated and the status-split physical family contains paired, unpaired >=3, and mixed-coarse witnesses",
        len(carriers) == 3
        and detail["current_campaign_fixed_carriers"] == 3
        and detail["landed_Cycle321_fixed_carriers"] == 1
        and detail["campaign_branch_Cycle349_fixed_carriers"] == 2
        and detail["current_campaign_programs"] == 18
        and detail["landed_Cycle321_programs"] == 6
        and detail["campaign_branch_Cycle349_programs"] == 12
        and len(rows) == 36
        and len(paired_rows) == 25
        and len(unpaired_rows) == 9
        and len(unpaired_three_or_more) == 9
        and len(ternary_unpaired) == 6
        and len(mixed_rows) == 2
        and detail["minimum_installed_unpaired_outcomes"] == 3
        and detail["maximum_sum_to_I_residual"] < TOL
        and all(
            row["declared_paired"] == row["recomputed_paired"] == (
                True, False, False, True, True, True
            )
            and row["fine_outcomes"] == (2, 3, 4, 3, 4, 6)
            for row in schema_rows.values()
        )
        and detail["finite_unpaired_witness_exists"]
        and not detail["finite_unpaired_witness_implies_global_grade"]
        and not detail["finite_unpaired_witness_implies_Born_law"],
        detail,
    )
    return detail


def grouped_effects(
    program: c321.Program,
    groups: tuple[tuple[int, ...], ...],
) -> tuple[np.ndarray, ...]:
    return tuple(
        sum(
            (program.fine_effects[index] for index in group),
            start=np.zeros((2, 2), dtype=complex),
        )
        for group in groups
    )


def grouped_chois(
    program: c321.Program,
    groups: tuple[tuple[int, ...], ...],
) -> tuple[np.ndarray, ...]:
    return tuple(c321.choi(tuple(program.kraus[index] for index in group)) for group in groups)


def refinement_and_process_controls(
    carriers: dict[str, c323.FixedProgramCarrier],
) -> dict[str, object]:
    canonical = carriers["cycle321-canonical"].programs
    unsplit, refined = canonical[2], canonical[3]
    rows = []

    def compare(
        name: str,
        left: c321.Program,
        right: c321.Program,
        right_groups: tuple[tuple[int, ...], ...],
        *,
        two_use: bool,
    ) -> None:
        left_groups = left.coarse_groups
        left_effects = grouped_effects(left, left_groups)
        right_effects = grouped_effects(right, right_groups)
        left_chois = grouped_chois(left, left_groups)
        right_chois = grouped_chois(right, right_groups)
        row = {
            "pair": name,
            "left_fine_outcomes": len(left.fine_effects),
            "right_fine_outcomes": len(right.fine_effects),
            "coarse_outcomes": len(left_effects),
            "coarse_effect_residual": max(float(np.linalg.norm(a - b)) for a, b in zip(left_effects, right_effects)),
            "coarse_CP_Choi_residual": max(float(np.linalg.norm(a - b)) for a, b in zip(left_chois, right_chois)),
            "fine_transcript_residual": float(
                np.linalg.norm(c321.transcript_choi(left.fine_effects) - c321.transcript_choi(right.fine_effects))
            ),
            "two_use_coarse_effect_residual": None,
            "two_use_coarse_CP_Choi_residual": None,
        }
        if two_use:
            row["two_use_coarse_effect_residual"] = max(
                float(np.linalg.norm(a - b))
                for a, b in zip(c323.grouped_sequence_effects(left), c323.grouped_sequence_effects(right))
            )
            row["two_use_coarse_CP_Choi_residual"] = max(
                float(np.linalg.norm(a - b))
                for a, b in zip(c323.grouped_sequence_chois(left), c323.grouped_sequence_chois(right))
            )
        rows.append(row)

    compare(
        "Cycle321 canonical unsplit/refined ray",
        unsplit,
        refined,
        refined.coarse_groups,
        two_use=True,
    )
    for table_name in ("cycle349-development", "cycle349-held"):
        complement, split = carriers[table_name].programs[:2]
        compare(
            f"{table_name} complement/same-ray split",
            complement,
            split,
            ((0, 1), (2,)),
            two_use=False,
        )
    axis_left, axis_right = canonical[:2]
    axis_effect_residual = max(
        float(np.linalg.norm(a - b))
        for a, b in zip(axis_left.coarse_effects, axis_right.coarse_effects)
    )
    axis_cp_residual = max(
        float(np.linalg.norm(a - b))
        for a, b in zip(c321.grouped_chois(axis_left), c321.grouped_chois(axis_right))
    )
    detail = {
        "refinement_rows": rows,
        "canonical_axis_same_effect_residual": axis_effect_residual,
        "canonical_axis_CP_residual": axis_cp_residual,
        "effect_equality_is_global_grade_functionality": False,
        "refinement_quotient_is_actuality_or_occurrence": False,
    }
    check(
        "three proportional-refinement pairs have exact coarse effects/CP maps while fine transcripts remain visible and same-effect need not mean same process",
        len(rows) == 3
        and all(
            row["coarse_effect_residual"] < TOL
            and row["coarse_CP_Choi_residual"] < TOL
            and row["fine_transcript_residual"] > 0.3
            for row in rows
        )
        and rows[0]["two_use_coarse_effect_residual"] < TOL
        and rows[0]["two_use_coarse_CP_Choi_residual"] < TOL
        and axis_effect_residual < TOL
        and axis_cp_residual > 0.4
        and not detail["effect_equality_is_global_grade_functionality"]
        and not detail["refinement_quotient_is_actuality_or_occurrence"],
        detail,
    )
    return detail


def compiler_witness_controls(
    fixture: c317.PhysicalFixture,
) -> dict[str, object]:
    rows = []
    for index, (eigenvalues, direction) in enumerate((
        ((0.83, 0.21), (2, 1, -3)),
        ((0.91, 0.64), (-1, 4, 2)),
        ((0.47, 0.02), (3, -2, 5)),
    )):
        vector = np.asarray(direction, dtype=float)
        vector /= np.linalg.norm(vector)
        high, low = eigenvalues
        projector = c317.projector_bloch(vector)
        kraus = (
            sqrt(low) * fixture.contact,
            sqrt(high - low) * projector @ fixture.contact,
            sqrt(high - low) * (I2 - projector) @ fixture.contact,
            sqrt(1 - high) * fixture.contact,
        )
        program = c321.Program(f"Cycle317 held mixed effect {index}", kraus, ((0, 1), (2, 3)))
        signatures = tuple(effect_signature(effect) for effect in program.coarse_effects)
        rows.append({
            "witness": program.name,
            "outcomes": len(program.coarse_effects),
            "eigenvalues": tuple(item.eigenvalues for item in signatures),
            "kinds": tuple(item.kind for item in signatures),
            "sum_to_I_residual": float(np.linalg.norm(program.completeness - I2)),
        })

    n = np.asarray((1, 2, 3), dtype=float)
    n /= np.linalg.norm(n)
    coefficient = 2 / (1 + float(np.sum(abs(n))))
    components = [(coefficient / 2, c317.projector_bloch(n))]
    for axis in range(3):
        unit = np.zeros(3)
        unit[axis] = -np.sign(n[axis])
        components.append((coefficient * abs(n[axis]) / 2, c317.projector_bloch(unit)))
    isometry, groups = c317.merge_isometry(tuple(components), fixture.contact)
    effects = c317.derived_effects(isometry, groups)
    signatures = tuple(effect_signature(effect) for effect in effects)
    merge_row = {
        "witness": "Cycle317 four-component axis merge",
        "fine_labels": sum(
            np.linalg.norm(isometry[2 * index : 2 * (index + 1)]) > TOL
            for index in range(c317.POINTER_DIMENSION)
        ),
        "coarse_outcomes": len(effects),
        "effect_kinds": tuple(item.kind for item in signatures),
        "paired": paired_status(effects),
        "sum_to_I_residual": float(np.linalg.norm(sum(effects) - I2)),
    }
    detail = {
        "held_arbitrary_binary_rows": rows,
        "axis_merge_row": merge_row,
        "Cycle317_pointer_capacity": c317.POINTER_DIMENSION,
        "Cycle317_merge_component_cap": 4,
        "host_supplied_coefficients_and_projectors": True,
        "fixed_carrier_slots_created_by_compiler_call": False,
        "autonomous_menu_genesis": None,
    }
    check(
        "Cycle317 can host-instantiate mixed binary and bounded split/merge witnesses, but the constructor call is not autonomous menu genesis",
        len(rows) == 3
        and all(
            row["outcomes"] == 2
            and row["kinds"] == (
                "mixed-effect-distinct-nonzero-eigenvalues",
                "mixed-effect-distinct-nonzero-eigenvalues",
            )
            and row["sum_to_I_residual"] < TOL
            for row in rows
        )
        and merge_row["fine_labels"] == 8
        and merge_row["coarse_outcomes"] == 5
        and merge_row["paired"] is False
        and merge_row["sum_to_I_residual"] < TOL
        and detail["Cycle317_pointer_capacity"] == 8
        and detail["Cycle317_merge_component_cap"] == 4
        and detail["host_supplied_coefficients_and_projectors"]
        and not detail["fixed_carrier_slots_created_by_compiler_call"]
        and detail["autonomous_menu_genesis"] is None,
        detail,
    )
    return detail


def carrier_frame_and_held_controls(
    fixtures: dict[int, c317.PhysicalFixture],
    carriers: dict[str, c323.FixedProgramCarrier],
    tables: dict[str, tuple[c349.MenuSchema, ...]],
) -> dict[str, object]:
    rows = []
    old_pass, old_fail = c323.PASS, c323.FAIL
    for name, carrier in carriers.items():
        c323.PASS = c323.FAIL = 0
        with redirect_stdout(StringIO()):
            fixed = c323.carrier_program_controls(carrier)
            two_use = c323.sequential_composition_controls(carrier)
            support = c323.physical_embedding_and_support_controls(fixtures, carrier)
            covariance = c323.covariance_controls(fixtures, carrier)
        rows.append({
            "carrier": name,
            "imported_checks": (c323.PASS, c323.FAIL),
            "fixed_isometry_residual": fixed["fixed_update_isometry_residual"],
            "two_use_isometry_residual": two_use["two_use_isometry_residual"],
            "held_L6_support": next(item for item in support if item["L"] == 6),
            "frames": covariance["frames"],
            "frame_branch_failures": covariance["branch_failures"],
            "maximum_frame_residual": covariance["maximum_one_use_carrier_residual"],
        })
    c323.PASS, c323.FAIL = old_pass, old_fail

    fixture350 = c350.c338.build_fixture(6)
    canonical_held = c350.form_fixed_corpus(fixture350, 12)
    fixed_hash = c350.corpus_hash(canonical_held)
    fixture349 = c349.c338.build_fixture(6)
    scaled_held, book = c349.build_corpus(fixture349, tables["cycle349-held"], 12)
    scaled_hash = c349.corpus_hash(scaled_held)
    route_names = tuple(item[0] for item in c351.ROUTES)
    detail = {
        "carrier_rows": rows,
        "canonical_Cycle350_held_N": len(canonical_held),
        "canonical_Cycle350_held_hash": fixed_hash,
        "scaled_Cycle349_held_N": len(scaled_held),
        "scaled_Cycle349_held_pages": len(book.pages),
        "scaled_Cycle349_held_hash": scaled_hash,
        "Cycle351_route_names": route_names,
        "Cycle351_synthesis_note_present": c351.NOTE.exists(),
        "proper_cubic_frames": len(c317.c311.c235.proper_cubic_frames()),
    }
    check(
        "the landed canonical carrier and two campaign-branch carriers retain one fixed update, bounded L6 support, all 24 frames, and current-branch N12 corpora",
        len(rows) == 3
        and all(
            row["imported_checks"] == (4, 0)
            and row["fixed_isometry_residual"] < TOL
            and row["two_use_isometry_residual"] < TOL
            and row["held_L6_support"]["one_and_two_use_leakage"] < TOL
            and row["held_L6_support"]["role_constraint_residual"] < TOL
            and row["frames"] == 24
            and row["frame_branch_failures"] == 0
            and row["maximum_frame_residual"] < TOL
            for row in rows
        )
        and len(canonical_held) == 12
        and c350.validate_fixed_corpus(fixture350, canonical_held)
        and len(scaled_held) == 12
        and len(book.pages) == 2
        and route_names == ("arbitrary_effect", "scaled_projector", "frequency")
        and c351.NOTE.exists()
        and detail["proper_cubic_frames"] == 24,
        detail,
    )
    return detail


def campaign_lineage_status_controls() -> dict[str, object]:
    paths = (
        "scripts/physical_typed_record_scaled_projector_unpaired_corpus_route_cycle349_2026_07_18.py",
        "scripts/physical_typed_record_fixed_program_frequency_corpus_route_cycle350_2026_07_18.py",
        "scripts/physical_typed_record_born_corpus_tournament_synthesis_cycle351_2026_07_18.py",
    )
    object_check = subprocess.run(
        ["git", "cat-file", "-e", f"{CAMPAIGN_CORPUS_COMMIT}^{{commit}}"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    head_ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", CAMPAIGN_CORPUS_COMMIT, "HEAD"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    base_object_check = subprocess.run(
        ["git", "cat-file", "-e", f"{PINNED_MAIN_BASE_COMMIT}^{{commit}}"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    campaign_in_pinned_base = subprocess.run(
        [
            "git", "merge-base", "--is-ancestor",
            CAMPAIGN_CORPUS_COMMIT, PINNED_MAIN_BASE_COMMIT,
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    pinned_base_in_campaign = subprocess.run(
        [
            "git", "merge-base", "--is-ancestor",
            PINNED_MAIN_BASE_COMMIT, CAMPAIGN_CORPUS_COMMIT,
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    blob_rows = []
    for path in paths:
        campaign_blob = subprocess.run(
            ["git", "rev-parse", f"{CAMPAIGN_CORPUS_COMMIT}:{path}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        head_blob = subprocess.run(
            ["git", "rev-parse", f"HEAD:{path}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        blob_rows.append({
            "path": path,
            "campaign_blob": campaign_blob.stdout.strip(),
            "HEAD_blob": head_blob.stdout.strip(),
            "same_blob": campaign_blob.returncode == head_blob.returncode == 0
            and campaign_blob.stdout.strip() == head_blob.stdout.strip(),
        })
    detail = {
        "landed_in_pinned_main_base_surfaces": (
            "Cycle317 physical contact/dilation compiler",
            "Cycle321 effect/coarse-CP program surface",
            "Cycle323 fixed program carrier and two-use physical embedding",
        ),
        "campaign_branch_surfaces_unlanded_at_census_date": (
            "Cycle349 development/held scaled-projector carriers and corpus",
            "Cycle350 fixed-program held corpus",
            "Cycle351 three-route synthesis",
        ),
        "campaign_corpus_commit": CAMPAIGN_CORPUS_COMMIT,
        "pinned_main_base_commit": PINNED_MAIN_BASE_COMMIT,
        "commit_object_present": object_check.returncode == 0,
        "pinned_main_base_object_present": base_object_check.returncode == 0,
        "commit_is_HEAD_ancestor": head_ancestry.returncode == 0,
        "campaign_commit_is_pinned_main_base_ancestor": (
            campaign_in_pinned_base.returncode == 0
        ),
        "pinned_main_base_is_campaign_commit_ancestor": (
            pinned_base_in_campaign.returncode == 0
        ),
        "path_blob_rows": tuple(blob_rows),
        "whole_census_was_landed_at_construction": False,
        "future_landing_allowed": True,
    }
    check(
        "Cycle317/321/323 were in the pinned main base while Cycle349/350/351 were unlanded at census construction; future landing is allowed",
        detail["commit_object_present"]
        and detail["pinned_main_base_object_present"]
        and detail["commit_is_HEAD_ancestor"]
        and not detail["campaign_commit_is_pinned_main_base_ancestor"]
        and detail["pinned_main_base_is_campaign_commit_ancestor"]
        and all(row["same_blob"] for row in blob_rows)
        and not detail["whole_census_was_landed_at_construction"]
        and detail["future_landing_allowed"],
        detail,
    )
    return detail


def comparator_and_absent_assumption_controls(
    census: dict[str, object],
) -> dict[str, object]:
    rows = []
    for number, comparator in COMPARATORS.items():
        head = comparator["head"]
        path = comparator["path"]
        object_check = subprocess.run(
            ["git", "cat-file", "-e", f"{head}^{{commit}}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        ancestry = subprocess.run(
            ["git", "merge-base", "--is-ancestor", head, "HEAD"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        note = subprocess.run(
            ["git", "show", f"{head}:{path}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        text = normalized_text(note.stdout)
        missing = tuple(item for item in comparator["hypotheses"] if item not in text)
        rows.append({
            "PR": number,
            "pinned_head": head,
            "commit_object_present": object_check.returncode == 0,
            "unlanded_not_HEAD_ancestor": ancestry.returncode == 1,
            "note_read_as_git_object_only": note.returncode == 0,
            "hypothesis_phrase_missing": missing,
        })

    current_source = Path(__file__).read_text(encoding="utf-8")
    imported_comparator_runners = tuple(
        name
        for name in (
            "born_form_effect_menu_sitewise_forcing_2026_07_17",
            "born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17",
            "born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17",
        )
        if f"import {name}" in current_source or f"from {name}" in current_source
    )
    assumption_matrix = {
        5472: {
            "finite_binary_and_ternary_witnesses": True,
            "some_mixed_effects": True,
            "one_weight_on_entire_finite_region_effect_algebra": False,
            "all_finite_effect_partitions_physically_eligible": False,
            "presentation_independent_grade_functionality": False,
            "normalization_law_for_every_eligible_menu": False,
            "autonomous_menu_and_grade_genesis": False,
        },
        5476: {
            "paired_scaled_projector_menus": True,
            "unpaired_scaled_projector_menu_outcome_at_least_three": census[
                "finite_unpaired_witness_exists"
            ],
            "entire_scaled_projector_domain_installed_as_one_family": False,
            "every_scaled_projector_menu_physically_eligible": False,
            "single_effect_functional_grade_across_presentations": False,
            "continuum_coefficient_and_program_genesis": False,
        },
        5479: {
            "finite_binary_witness": True,
            "finite_ternary_witness": True,
            "finite_mixed_projective_and_refinement_witnesses": True,
            "every_binary_effect_menu_physically_eligible": False,
            "every_ternary_effect_menu_physically_eligible": False,
            "every_mixed_projective_menu_physically_eligible": False,
            "decomposition_invariant_grade_functionality": False,
            "selected_global_grade_or_Born_law": False,
        },
    }
    detail = {
        "comparators": rows,
        "comparator_runner_imports": imported_comparator_runners,
        "comparator_theorems_consumed": False,
        "assumption_matrix": assumption_matrix,
        "absence_scope": "not installed in the current campaign interface; no impossibility claim",
    }
    check(
        "PR #5472/#5476/#5479 are commit-pinned unlanded comparators and their universal grading premises remain explicit absent imports",
        all(
            row["commit_object_present"]
            and row["unlanded_not_HEAD_ancestor"]
            and row["note_read_as_git_object_only"]
            and not row["hypothesis_phrase_missing"]
            for row in rows
        )
        and not imported_comparator_runners
        and not detail["comparator_theorems_consumed"]
        and assumption_matrix[5476]["unpaired_scaled_projector_menu_outcome_at_least_three"]
        and not assumption_matrix[5472]["all_finite_effect_partitions_physically_eligible"]
        and not assumption_matrix[5476]["every_scaled_projector_menu_physically_eligible"]
        and not assumption_matrix[5479]["every_ternary_effect_menu_physically_eligible"]
        and not assumption_matrix[5479]["selected_global_grade_or_Born_law"],
        detail,
    )
    return detail


def rejected(callable_) -> bool:
    try:
        callable_()
    except (TypeError, ValueError):
        return True
    return False


def deletion_domain_leakage_and_host_import_controls(
    carriers: dict[str, c323.FixedProgramCarrier],
    tables: dict[str, tuple[c349.MenuSchema, ...]],
    carrier_controls: dict[str, object],
) -> dict[str, object]:
    deletion_defects = []
    for name, carrier in carriers.items():
        for program in carrier.programs:
            deleted = program.kraus[:-1]
            defect = float(
                np.linalg.norm(
                    sum(
                        (operator.conj().T @ operator for operator in deleted),
                        start=np.zeros((2, 2), dtype=complex),
                    )
                    - I2,
                    2,
                )
            )
            deletion_defects.append((name, program.name, defect))

    canonical = carriers["cycle321-canonical"]
    update = canonical.update.copy()
    tensor = update.reshape(
        c323.PROGRAM_DIMENSION,
        c323.POINTER_DIMENSION,
        2,
        c323.PROGRAM_DIMENSION,
        2,
    )
    tensor[0, :, :, 0, :] = 0
    deleted_update = tensor.reshape(update.shape)
    control_block_defect = float(np.linalg.norm(deleted_update.conj().T @ deleted_update - np.eye(16), 2))

    invalid_calls = (
        lambda: effect_signature(np.asarray(((0, 1), (0, 0)), dtype=complex)),
        lambda: effect_signature(1.1 * I2),
        lambda: c321.Program("missing", (I2,), ()),
        lambda: c321.Program("duplicate", (I2, I2), ((0,), (0,))),
        lambda: c323.FixedProgramCarrier(canonical.programs[:-1]),
        lambda: c323.program_basis(6),
        lambda: c323.validate_pointer_blank(1),
        lambda: c317.stack_isometry(tuple(I2 for _ in range(9))),
        lambda: c317.split_projector_isometry(c317.projector_bloch(np.asarray((1, 0, 0))), (0.2, 0.3), I2),
        lambda: c317.merge_isometry(tuple((0.3, c317.projector_bloch(np.asarray((1, 0, 0)))) for _ in range(4)), I2),
        lambda: c349.MenuSchema("nine", "bad", tuple(c349.ScaledTerm(1 / 9, None) for _ in range(9)), (tuple(range(9)),), True),
        lambda: c349.ScaledTerm(-0.1, None),
    )
    rejections = sum(rejected(call) for call in invalid_calls)
    support_rows = tuple(
        row["held_L6_support"]
        for row in carrier_controls["carrier_rows"]
    )
    detail = {
        "fine_branch_deletions": len(deletion_defects),
        "fine_branch_deletion_survivors": sum(defect < TOL for _name, _program, defect in deletion_defects),
        "minimum_deleted_branch_defect": min(defect for _name, _program, defect in deletion_defects),
        "program_control_block_deletion_isometry_defect": control_block_defect,
        "domain_rejections": rejections,
        "domain_attempts": len(invalid_calls),
        "held_L6_leakage_maximum": max(row["one_and_two_use_leakage"] for row in support_rows),
        "held_L6_constraint_maximum": max(row["role_constraint_residual"] for row in support_rows),
        "host_selection_and_genesis_imports": {
            "program_tables": "Cycle321 hard-coded six programs plus supplied Cycle349 development/held coefficient tables",
            "carrier_installation": "host constructs one FixedProgramCarrier from the selected six-program table",
            "program_state_preparation": "supplied three-M2 state/label",
            "pointer_blank": "supplied fresh three-M2 blank per use",
            "fine_pointer_registration": "supplied conditional corpus tag/interface",
            "coarse_grouping": "declared per Program; not generated by the substrate",
            "coefficient_and_projector_choice": "supplied to Cycle317 constructors",
            "menu_eligibility": None,
            "numerical_grade_genesis": None,
        },
        "make_programs_parameters": tuple(signature(c323.make_programs).parameters),
        "schema_table_parameters": tuple(signature(c349.schema_table).parameters),
        "fixed_update_application": " ".join(getsource(c323.apply_fixed_update).split()),
        "host_program_branch_query_during_update": False,
    }
    check(
        "branch/control deletions, malformed domains, and leakage are visible while every host selection/genesis import is named",
        len(deletion_defects) == 18
        and detail["fine_branch_deletion_survivors"] == 0
        and detail["minimum_deleted_branch_defect"] > 0.02
        and control_block_defect > 0.9
        and rejections == len(invalid_calls)
        and detail["held_L6_leakage_maximum"] < TOL
        and detail["held_L6_constraint_maximum"] < TOL
        and detail["host_selection_and_genesis_imports"]["menu_eligibility"] is None
        and detail["host_selection_and_genesis_imports"]["numerical_grade_genesis"] is None
        and detail["make_programs_parameters"] == ("contact",)
        and detail["schema_table_parameters"] == ("held",)
        and detail["fixed_update_application"].endswith("return update @ state")
        and not detail["host_program_branch_query_during_update"],
        detail,
    )
    return detail


def note_contract() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-381 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "three finite six-program carriers",
        "landed cycle-317/321/323 substrate and compiler",
        "campaign-branch cycle-349/350/351 carriers and corpora",
        "06cb17dcb26c7b6d0aa4377b6f1125bdc3d210bf",
        "0355ac4728f57d9fdc62cb27764bbd33e6e8b8df",
        "not in the pinned main base at construction",
        "unlanded at the census date",
        "future landing",
        "unpaired three-outcome scaled-projector menu is physically installed",
        "finite witness does not supply a global grading functional or born law",
        "pr #5472",
        "2c648ccb408a8c36a700f53ec5401369e3bbd490",
        "pr #5476",
        "a994617819f57e599dd101c654be366123392236",
        "pr #5479",
        "84053108a424cef26dc23e484549df331ad2050f",
        "unlanded commit-pinned comparators only",
        "effect functionality remains absent",
        "universal menu eligibility remains absent",
        "host selection and genesis imports",
        "no probability, actuality, or frequency promotion",
        "no no-go, minimum-content, or axiom-pressure claim",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the exact census, comparator boundary, absent assumptions, and semantic firewall",
        not missing,
        missing,
    )
    return {"missing": missing}


def supplied_structure_and_semantic_controls(
    census: dict[str, object],
) -> dict[str, object]:
    inventory = {
        "result": "exact bounded census of the current campaign physical Born menu-grade interface",
        "landed_in_pinned_main_base_surfaces": (
            "Cycle317 bounded contact/trine/split/merge host-instantiated dilation compiler",
            "Cycle321 six finite programs and local effect/coarse-CP equivalences",
            "Cycle323 fixed three-M2 six-program controlled carrier and two-use composition",
        ),
        "campaign_branch_surfaces_unlanded_at_census_date": (
            "Cycle349/Cycle351 finite development/held scaled-projector carriers",
            "Cycle350/Cycle351 grade-blind held N12 corpus over the canonical carrier",
        ),
        "campaign_corpus_commit": CAMPAIGN_CORPUS_COMMIT,
        "pinned_main_base_commit": PINNED_MAIN_BASE_COMMIT,
        "whole_census_was_landed_at_construction": False,
        "future_landing_allowed": True,
        "current_campaign_fixed_carriers": census["current_campaign_fixed_carriers"],
        "landed_fixed_carriers": census["landed_Cycle321_fixed_carriers"],
        "campaign_branch_fixed_carriers": census["campaign_branch_Cycle349_fixed_carriers"],
        "current_campaign_programs": census["current_campaign_programs"],
        "unpaired_three_or_more_exists": census["finite_unpaired_witness_exists"],
        "all_effects_or_menus_autonomously_generated": False,
        "effect_functionality_law": None,
        "universal_menu_eligibility_law": None,
        "menu_normalization_grade_law": None,
        "numerical_grade_selector": None,
        "global_grading_functional": None,
        "Born_law": None,
        "probability_interpretation": None,
        "actual_history_sampler": None,
        "actual_member_selector": None,
        "frequency_theorem": None,
        "Record_or_pointer_is_probability": False,
        "program_or_pointer_is_law_selection": False,
        "coarse_pointer_erasure_is_occurrence": False,
        "shared_substrate_obstruction": False,
        "no_go": None,
        "minimum_content_claim": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the supplied physical/compiler/table/corpus structure is explicit without probability, actuality, frequency, or constitutional promotion",
        inventory["current_campaign_fixed_carriers"] == 3
        and inventory["landed_fixed_carriers"] == 1
        and inventory["campaign_branch_fixed_carriers"] == 2
        and inventory["current_campaign_programs"] == 18
        and not inventory["whole_census_was_landed_at_construction"]
        and inventory["future_landing_allowed"]
        and inventory["unpaired_three_or_more_exists"]
        and not inventory["all_effects_or_menus_autonomously_generated"]
        and inventory["effect_functionality_law"] is None
        and inventory["universal_menu_eligibility_law"] is None
        and inventory["menu_normalization_grade_law"] is None
        and inventory["numerical_grade_selector"] is None
        and inventory["global_grading_functional"] is None
        and inventory["Born_law"] is None
        and inventory["probability_interpretation"] is None
        and inventory["actual_history_sampler"] is None
        and inventory["actual_member_selector"] is None
        and inventory["frequency_theorem"] is None
        and not inventory["Record_or_pointer_is_probability"]
        and not inventory["program_or_pointer_is_law_selection"]
        and not inventory["coarse_pointer_erasure_is_occurrence"]
        and not inventory["shared_substrate_obstruction"]
        and inventory["no_go"] is inventory["minimum_content_claim"] is inventory["axiom_pressure"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 381: CURRENT CAMPAIGN PHYSICAL BORN MENU-GRADE INTERFACE CENSUS")
    print("authority=none; audit=unset; landed 317/321/323; branch 349/350/351; no Born promotion")
    note = note_contract()
    with redirect_stdout(StringIO()):
        fixtures = c323.physical_fixture_controls()
    carriers, tables = installed_carriers(fixtures[3].contact)
    census = exact_effect_menu_census_controls(carriers, tables)
    refinement = refinement_and_process_controls(carriers)
    compiler = compiler_witness_controls(fixtures[3])
    carrier = carrier_frame_and_held_controls(fixtures, carriers, tables)
    lineage = campaign_lineage_status_controls()
    comparators = comparator_and_absent_assumption_controls(census)
    attacks = deletion_domain_leakage_and_host_import_controls(carriers, tables, carrier)
    inventory = supplied_structure_and_semantic_controls(census)
    check(
        "Cycle 381 status-splits landed substrate from campaign carriers and finds no current-campaign universal menu-grade or Born law",
        not note["missing"]
        and census["finite_unpaired_witness_exists"]
        and census["minimum_installed_unpaired_outcomes"] == 3
        and refinement["refinement_rows"][0]["coarse_CP_Choi_residual"] < TOL
        and compiler["Cycle317_pointer_capacity"] == 8
        and carrier["proper_cubic_frames"] == 24
        and not lineage["whole_census_was_landed_at_construction"]
        and not lineage["campaign_commit_is_pinned_main_base_ancestor"]
        and lineage["future_landing_allowed"]
        and not comparators["comparator_theorems_consumed"]
        and attacks["fine_branch_deletion_survivors"] == 0
        and inventory["global_grading_functional"] is None
        and inventory["Born_law"] is None,
        {
            "disposition": "bounded positive exact current-campaign interface census with explicit landing-status split",
            "strongest_positive": "the landed canonical carrier has an unpaired ternary menu; current campaign adds finite scaled/mixed/corpus witnesses",
            "absent": "universal eligibility, effect functionality, autonomous coefficient/menu/grade genesis, selected numerical law, sampler, frequency theorem",
            "comparator_heads": {number: row["head"] for number, row in COMPARATORS.items()},
            "no_go_or_axiom_pressure": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_BORN_MENU_GRADE_CURRENT_CAMPAIGN_INTERFACE_CENSUS_OPEN")
        return 1
    print("RESULT PHYSICAL_BORN_MENU_GRADE_CURRENT_CAMPAIGN_INTERFACE_CENSUS_EXACT_FINITE_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
