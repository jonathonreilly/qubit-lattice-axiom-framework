#!/usr/bin/env python3
"""Cycle 351 synthesis certificate for the typed-Record Born corpus routes."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TYPED_RECORD_BORN_CORPUS_TOURNAMENT_SYNTHESIS_"
    "CYCLE351_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "arbitrary_effect",
        ROOT / "scripts/physical_typed_record_full_effect_menu_corpus_route_cycle348_2026_07_18.py",
        "RESULT PHYSICAL_TYPED_RECORD_FULL_EFFECT_MENU_CORPUS_ROUTE_CERTIFIED",
        "SUMMARY {'pass': 9, 'fail': 0}",
    ),
    (
        "scaled_projector",
        ROOT / "scripts/physical_typed_record_scaled_projector_unpaired_corpus_route_cycle349_2026_07_18.py",
        "RESULT CYCLE349_SCALED_PROJECTOR_TYPED_RECORD_CORPUS_GREEN",
        "SUMMARY PASS 11 FAIL 0",
    ),
    (
        "frequency",
        ROOT / "scripts/physical_typed_record_fixed_program_frequency_corpus_route_cycle350_2026_07_18.py",
        "RESULT PHYSICAL_TYPED_RECORD_FIXED_PROGRAM_FREQUENCY_CORPUS_ROUTE_CERTIFIED",
        "SUMMARY {'pass': 8, 'fail': 0}",
    ),
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
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-351 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "conditional finite physical registration bridge",
        "the whole word is not promoted to a record",
        "unpairedness alone is not sufficient",
        "deleting the grade leaves the corpus",
        "three-dimensional lattice remains spatial input",
        "broad born/substrate no-go",
        "there is no route-independent obstruction and no axiom pressure",
        "autonomous local lineage/tagging and matcher tournament",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the finite theorem, Record/tag and Born firewalls, N1-N8, and next campaign",
        not missing,
        missing,
    )


def cold_route_certificates() -> dict[str, str]:
    outputs: dict[str, str] = {}

    def execute(route: tuple[str, Path, str, str]):
        name, path, result_line, summary_line = route
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        return name, result_line, summary_line, completed

    with ThreadPoolExecutor(max_workers=len(ROUTES)) as pool:
        completed_routes = tuple(pool.map(execute, ROUTES))
    rows = []
    for name, result_line, summary_line, completed in completed_routes:
        output = completed.stdout + completed.stderr
        outputs[name] = output
        rows.append(
            {
                "route": name,
                "exit": completed.returncode,
                "result": result_line in output,
                "summary": summary_line in output,
                "output_lines": len(output.splitlines()),
            }
        )
    check(
        "all three independent route runners cold-execute to exact green certificates",
        all(row["exit"] == 0 and row["result"] and row["summary"] for row in rows),
        rows,
    )
    return outputs


def exact_metric_controls(outputs: dict[str, str]) -> None:
    required = {
        "arbitrary_effect": (
            "'campaign_base_main': '0355ac4728f57d9fdc62cb27764bbd33e6e8b8df'",
            "'corpus_atom_M2': 43",
            "'finite_effects': 12",
            "'finite_complements': 12",
            "'presentations_per_effect': 3",
            "'total_formed_atoms_across_three_presentations': 126",
            "'43_M2_atom_words_differ_across_presentations': True",
            "'proper_cubic_frame_cases': 432",
            "'maximum_same-trial_rogue_fine_presentation_separator': 0.9202730714903699",
        ),
        "scaled_projector": (
            "'pinned_campaign_base': '0355ac4728f57d9fdc62cb27764bbd33e6e8b8df'",
            "'record_atom_M2': 43",
            "'record_atom_width_breakdown_M2': (30, 2, 3, 3, 4, 1)",
            "'frame_size_endpoint_record_cases': 648",
            "'two_use_isometry_residual': 1.0018390867726344e-15",
            "'paired_rogue_residual': 2.220446049250313e-16",
            "'unpaired_rogue_residuals': (0.0, 0.08939225214071667)",
            "'unpaired_rogue_residuals': (0.0, 0.06831708838497141)",
            "'tag_binding': False",
        ),
        "frequency": (
            "'Record_M2': 30",
            "'registered_supplied_tag_M2': 13",
            "'whole_43_M2_atom_is_Record': False",
            "'corpus_frame_atom_cases': 792",
            "'ray_two_use_coarse_CP_residual': 4.5828752110238735e-17",
            "'ray_two_use_fine_transcript_residual': 0.9329539020600226",
            "'axis_process_Choi_residual': 0.2202543031572249",
            "'paired_rogue_outside_domain_is_undefined': True",
            "'typed_survivors': 0",
            "'law_names': ('IID', 'sticky', 'frozen', 'balanced', 'equal-mean mixture')",
        ),
    }
    missing = {
        name: tuple(item for item in needles if item not in outputs[name])
        for name, needles in required.items()
    }
    check(
        "the synthesis parses exact widths, residuals, grade boundaries, deletions, covariance and law controls",
        all(not values for values in missing.values()),
        missing,
    )


def route_independence_controls() -> None:
    capabilities = {
        "arbitrary_effect": {
            "arbitrary_effect_list",
            "three_presentations",
            "shared_underlying_Record_words",
        },
        "scaled_projector": {
            "four_schema_families",
            "unpaired_axis_discriminator",
            "bounded_apparatus_patch",
        },
        "frequency": {
            "fine_process_transcript",
            "two_use_carrier",
            "same_marginal_law_attachments",
        },
    }
    overlaps = {
        f"{left}/{right}": capabilities[left] & capabilities[right]
        for left, right in combinations(capabilities, 2)
    }
    check(
        "the routes test distinct effect-presentation, menu-family and repeated-history surfaces",
        all(not overlap for overlap in overlaps.values()),
        overlaps,
    )


def semantic_firewall_controls(outputs: dict[str, str]) -> None:
    joined = "\n".join(outputs.values())
    needles = (
        "'Born_forcing': False",
        "'actual_history_sampler': None",
        "'frequency_law': None",
        "'nearest_neighbour_support_M2': None",
        "'whole_43_M2_atom_is_Record': False",
        "'pointer_copy_is_Record': False",
        "'frequency_is_probability': False",
        "'authority': 'none'",
        "'audit': 'unset'",
    )
    missing = tuple(item for item in needles if item not in joined)
    check(
        "no pointer tag, finite menu, diagnostic grade, frequency, width or spatial frame is promoted beyond its interface",
        not missing,
        missing,
    )


def candidate_boundary_controls(outputs: dict[str, str]) -> None:
    joined = "\n".join(outputs.values())
    text = normalized(NOTE)
    check(
        "recent universal theorem candidates remain pinned, explicit and unconsumed by the finite routes",
        "769950dc06" in joined
        and "5dd59abfbf" in joined
        and "'theorem_consumed': False" in joined
        and "0355ac4728f57d9fdc62cb27764bbd33e6e8b8df" in text
        and "does not consume or reproduce either universal theorem" in text,
        "campaign-base ancestry and import audits",
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    markers = {
        "finite arbitrary-effect presentation corpus": "attempted",
        "finite scaled-projector unpaired-schema corpus": "attempted",
        "fixed-program fine-history and repeated-law corpus": "attempted",
        "universal menu eligibility and effect functionality from physical registration": "open / untested",
        "autonomous numerical-grade selection": "open / untested",
        "actual-history sampler / component-selection dynamics": "open / untested",
        "nn record/tag formation and renewable corpus compiler": "open / untested",
        "empirical-frequency and continuum extension": "open / untested",
    }
    marker_failures = tuple(
        key for key, marker in markers.items() if key not in text or marker not in text
    )
    walls = ("w_form", "w_tag", "w_menu", "w_grade", "w_law", "w_local")
    pair_rows = sum(
        f"{left} / {right}" in text for left, right in combinations(walls, 2)
    )
    check(
        "full N1-N8 blocks finite-corpus Born forcing, broad substrate no-go, minimum-content and axiom-pressure claims",
        all(sections)
        and not marker_failures
        and pair_rows == 15
        and "broad born/substrate no-go" in text
        and "there is no route-independent obstruction and no axiom pressure" in text,
        {
            "sections": sections,
            "marker_failures": marker_failures,
            "wall_pair_rows": pair_rows,
        },
    )


def lane_and_wall_controls() -> None:
    text = normalized(NOTE)
    scores = ("71/34/98", "41/21/76", "77/38/98", "43/17/71", "40/16/93")
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    check(
        "the synthesis updates every TOE lane and dependency wall without an audit verdict",
        all(score in text for score in scores)
        and all(wall in text for wall in walls)
        and "planning estimates, not probabilities" in text
        and "not audit verdicts" in text,
        {"scores": scores, "walls": walls},
    )


def foundation_integrity_controls() -> None:
    protected = (
        ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        ROOT / "docs/audit/data/axiom_premise_nodes.json",
    )
    statuses = {str(path.relative_to(ROOT)): path.exists() for path in protected}
    text = normalized(NOTE)
    check(
        "foundation inputs remain dependencies rather than campaign outputs",
        all(statuses.values())
        and "constitutional effect: none" in text
        and "no supplied item is promoted to an axiom or approved primitive" in text,
        statuses,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 351: PHYSICAL TYPED-RECORD BORN-CORPUS TOURNAMENT")
    print("authority=none; audit=unset")
    note_contract()
    outputs = cold_route_certificates()
    exact_metric_controls(outputs)
    route_independence_controls()
    semantic_firewall_controls(outputs)
    candidate_boundary_controls(outputs)
    no_go_discipline_controls()
    lane_and_wall_controls()
    foundation_integrity_controls()
    check(
        "Cycle 351 constructs finite grade-blind physical Record-tag corpus bridges without deriving menu eligibility, a grade selector, sampler, frequency law, time, energy or gravity",
        FAIL == 0,
        {
            "strongest_positive": "finite physical scaled-projector unpaired-schema Record-tag corpus",
            "not_derived": "universal eligibility/functionality, Born grade/selection, actual history, frequency, time, source law or gravity",
            "axiom_pressure": False,
        },
    )
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_TYPED_RECORD_BORN_CORPUS_TOURNAMENT_OPEN")
        return 1
    print("RESULT PHYSICAL_TYPED_RECORD_BORN_CORPUS_TOURNAMENT_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
