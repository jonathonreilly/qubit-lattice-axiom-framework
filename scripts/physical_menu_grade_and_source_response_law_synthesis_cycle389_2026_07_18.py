#!/usr/bin/env python3
"""Cycle 389: menu-grade and source-response law synthesis.

Cold-executes Cycles 381--388 and checks the exact finite menu census,
physical schema/quotient/registry interfaces, positive trace/nontrace grade
witnesses, finite normalization reference, blind-held source-side response,
six-wall ledger, law-completeness contract, and full N1--N8 boundary.

No numerical law, probability, actuality, source, gravity, time, shared
obstruction, or axiom pressure is selected. Authority is none; audit is unset.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MENU_GRADE_AND_SOURCE_RESPONSE_LAW_"
    "SYNTHESIS_CYCLE389_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "menu_census",
        "physical_born_menu_grade_interface_census_cycle381_2026_07_18.py",
        "PASS 10\nFAIL 0",
        "RESULT PHYSICAL_BORN_MENU_GRADE_CURRENT_CAMPAIGN_INTERFACE_CENSUS_EXACT_FINITE_POSITIVE",
    ),
    (
        "schema_compiler",
        "physical_fixed_menu_schema_compiler_cycle382_2026_07_18.py",
        "SUMMARY PASS=8 FAIL=0",
        None,
    ),
    (
        "refinement_quotient",
        "physical_mixed_projective_refinement_functionality_born_bridge_cycle383_2026_07_18.py",
        "PASS 8\nFAIL 0",
        "RESULT PHYSICAL_MIXED_PROJECTIVE_REFINEMENT_FUNCTIONALITY_BORN_BRIDGE_BOUNDED_POSITIVE",
    ),
    (
        "local_registration",
        "physical_local_menu_registration_bridge_cycle384_2026_07_18.py",
        "SUMMARY PASS=8 FAIL=0",
        None,
    ),
    (
        "identifiability",
        "physical_menu_overlap_grade_identifiability_tournament_cycle385_2026_07_18.py",
        "PASS 9\nFAIL 0",
        "RESULT PHYSICAL_MENU_OVERLAP_GRADE_IDENTIFIABILITY_EXACT_FINITE_DIAGNOSTIC",
    ),
    (
        "effect_registry",
        "physical_finite_effect_class_registry_cycle386_2026_07_18.py",
        "SUMMARY PASS=7 FAIL=0",
        None,
    ),
    (
        "source_response",
        "physical_contact_sensitive_source_response_calibration_stress_cycle387_2026_07_18.py",
        "SUMMARY {'pass': 11, 'fail': 0}",
        "RESULT PHYSICAL_CONTACT_SENSITIVE_RESPONSE_CALIBRATION_BOUNDED_POSITIVE",
    ),
    (
        "normalization_reference",
        "physical_finite_menu_normalization_checker_cycle388_2026_07_18.py",
        "SUMMARY PASS=6 FAIL=0",
        None,
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
        check("the Cycle-389 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycles 381--388 move two law-level bridges without selecting either law",
        "rank 20 and nullity 35",
        "explicit open family of strictly positive normalized nontrace assignments",
        "seven exact unregistered overlap menus would raise rank to 27",
        "physical arithmetic gate compiler, nearest-neighbor decomposition, maximum primitive support",
        "blind-held, swap-symmetric, contact-conditioned multiplicative calibration",
        "dimensionless operational response facts",
        "no common substrate obstruction is established",
        "no axiom pressure is established",
        "three-dimensional lattice and all 24 proper-cubic frames remain spatial",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the two positive bridges, exact bounded residuals, physical/compiler limits, and semantic status",
        not missing,
        missing,
    )


def cold_certificates() -> dict[str, str]:
    outputs: dict[str, str] = {}

    def execute(route):
        name, filename, pass_line, result_line = route
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / filename)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        return name, pass_line, result_line, completed

    rows = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = tuple(pool.map(execute, ROUTES))
    for name, pass_line, result_line, completed in results:
        output = completed.stdout + completed.stderr
        outputs[name] = output
        rows.append(
            {
                "route": name,
                "exit": completed.returncode,
                "pass": pass_line in output,
                "result": result_line is None or result_line in output,
                "lines": len(output.splitlines()),
            }
        )
    check(
        "all eight menu-grade and source-response routes cold-execute green",
        all(row["exit"] == 0 and row["pass"] and row["result"] for row in rows),
        rows,
    )
    return outputs


def physical_menu_interface_controls(outputs: dict[str, str]) -> None:
    census = outputs["menu_census"]
    schema = outputs["schema_compiler"]
    quotient = outputs["refinement_quotient"]
    registration = outputs["local_registration"]
    registry = outputs["effect_registry"]
    check(
        "bounded physical menus, lawful effect/process quotients, local registration, and finite class functionality are exact",
        "'distinct_effect_operators': 55" in census
        and "'unpaired_scaled_projector_presentations': 9" in census
        and "'mixed_effect_coarse_presentations': 2" in census
        and "'positive_coarse_instrument_Choi_residual': 1.3558296880868396e-16" in schema
        and "'frames': 24" in schema
        and "'coarse_common_states_equal': True" in quotient
        and "'axis_coarse_CP_Choi_residual': 0.43472221389739873" in quotient
        and "'E_out_G_coarse_minus_G_registered_E_in_residual': 0.0" in registration
        and "'registered_patch_M2': 63" in registration
        and "'effect_classes': 9" in registry
        and "'coarse_CP_classes': 11" in registry
        and "'physical_registry_EG_residual': 0.0" in registry,
        "finite physical apparatus/interface closure only; selection and genesis remain supplied",
    )


def finite_grade_controls(outputs: dict[str, str]) -> None:
    diagnostic = outputs["identifiability"]
    normalization = outputs["normalization_reference"]
    check(
        "the installed finite graph has exact positive trace/nontrace witnesses and the same finite normalization reference accepts two positive tables",
        "'matrix_rank': 20" in diagnostic
        and "'nullity': 35" in diagnostic
        and "'nontrace_perturbation_epsilon': 0.09602209455276872" in diagnostic
        and "'best_single_density_matrix_fit_residual': 0.13046989074391827" in diagnostic
        and "'greedy_independent_candidate_menus': 7" in diagnostic
        and "'rank_after_all_candidates': 27" in diagnostic
        and "'negative_claim_shipped': False" in diagnostic
        and "'denominator': 48" in normalization
        and "'tables_distinct': True" in normalization
        and "'exact_EG_failures': 0" in normalization
        and "'physical_arithmetic_gate_compiler': None" in normalization
        and "'nearest_neighbor_decomposition': None" in normalization
        and "'maximum_primitive_support_M2': None" in normalization
        and "'primitive_boundary_leakage_audit': None" in normalization,
        "positive finite alternatives; neither a selected grade nor a physical arithmetic compiler",
    )


def source_response_controls(outputs: dict[str, str]) -> None:
    response = outputs["source_response"]
    check(
        "one frozen operational calibration transfers blindly with reciprocity while source/gravity identification stays false",
        "'maximum_two_coordinate_pointer_residual': 0.0005600968888701541" in response
        and "'maximum_two_coordinate_multiplicity_residual': 0.004630557505736377" in response
        and "'maximum_source_target_swap_residual': 2.220446049250313e-16" in response
        and "'minimum_absolute_additivity_residual': 0.029629307745172362" in response
        and "'maximum_candidate_input_operator_frame_residual': 8.807749891993861e-16" in response
        and "'pointer_coordinate_residual': 5.149960319306146e-19" in response
        and "'strict_98_M2_rows': 16" in response
        and "'logical_comparator_rows': 16" in response
        and "'response_is_energy': False" in response
        and "'response_is_source': False" in response
        and "'response_is_gravity': False" in response
        and "'axiom_pressure': None" in response,
        "operational response only; additive ansatz failure is route-specific",
    )


def completeness_ledger_and_score_controls() -> None:
    text = normalized(NOTE)
    fields = (
        "domain",
        "state",
        "context",
        "atomic_law",
        "continuation",
        "availability",
        "concurrency",
        "record",
        "actuality",
        "statistics",
        "resource",
        "source/response",
    )
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    scores = ("83/43/99", "53/33/91", "78/38/99", "45/18/76", "52/22/98")
    check(
        "the 12-field law contract, six-wall ledger, and evidence-weighted lane scores are explicit",
        all(f"| {field} |" in text for field in fields)
        and all(f"| {wall} |" in text for wall in walls)
        and all(score in text for score in scores)
        and "planning estimates, not truth probabilities" in text,
        {"fields": fields, "walls": walls, "scores": scores},
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    routes = (
        "installed 36-menu overlap graph",
        "exact refinement/effect quotient",
        "bounded cycle-317 host menus",
        "seven exact hybrid overlap menus",
        "broader rotated/coefficient family",
        "physical additivity/affinity law",
        "finite effect/process registry",
        "finite normalization arithmetic",
        "actual-member sampler and frequency theorem",
        "frozen one-edge source-response calibration",
        "separated reciprocal multi-edge calibration",
        "physical source identification and metric/clock response",
    )
    walls = ("o_overlap", "o_grade", "o_actual", "o_source", "o_metric")
    pair_count = sum(
        f"{left} / {right}" in text for left, right in combinations(walls, 2)
    )
    check(
        "full N1-N8 blocks global nonforcing, minimum-content, shared-obstruction and axiom-pressure promotion",
        all(sections)
        and all(route in text for route in routes)
        and pair_count == 10
        and "fail / do not ship a global born no-go" in text
        and "no axiom edit is indicated" in text,
        {"sections": sections, "routes": len(routes), "wall_pairs": pair_count},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 389: MENU-GRADE / SOURCE-RESPONSE LAW SYNTHESIS")
    print("authority=none; audit=unset; no selected grade, source, gravity, or axiom pressure")
    note_contract()
    outputs = cold_certificates()
    physical_menu_interface_controls(outputs)
    finite_grade_controls(outputs)
    source_response_controls(outputs)
    completeness_ledger_and_score_controls()
    no_go_discipline_controls()
    check(
        "Cycle 389 retains two exact positive law-level bridges while routing physical overlap, arithmetic, actuality, and source-metric closures",
        FAIL == 0,
        {
            "numerical_law_selected": None,
            "actuality_or_frequency": None,
            "physical_source_or_gravity": None,
            "shared_substrate_obstruction": None,
            "axiom_pressure": None,
            "authority": "none",
            "audit": "unset",
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_MENU_GRADE_SOURCE_RESPONSE_LAW_SYNTHESIS_OPEN")
        return 1
    print("RESULT PHYSICAL_MENU_GRADE_SOURCE_RESPONSE_LAW_SYNTHESIS_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
