#!/usr/bin/env python3
"""Cycle 393: menu compiler and reciprocal-edge synthesis.

Cold-executes Cycles 390--392 and checks the exact physical rank gain,
nearest-neighbor normalization arithmetic, reciprocal adjacent-edge transfer,
law-completeness ledger, and full N1--N8 boundary.

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
    "PHYSICAL_MENU_COMPILER_AND_RECIPROCAL_EDGE_"
    "SYNTHESIS_CYCLE393_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "overlap_compiler",
        "physical_seven_overlap_menu_fixed_carrier_cycle390_2026_07_18.py",
        "PASS 8\nFAIL 0",
        "RESULT PHYSICAL_SEVEN_OVERLAP_MENU_FIXED_CARRIER_EXACT_RANK_GAIN",
    ),
    (
        "arithmetic_compiler",
        "physical_nn_menu_arithmetic_compiler_cycle391_2026_07_18.py",
        "SUMMARY PASS=6 FAIL=0",
        None,
    ),
    (
        "reciprocal_edge",
        "physical_reciprocal_multi_edge_calibration_cycle392_2026_07_18.py",
        "SUMMARY {'pass': 12, 'fail': 0}",
        "RESULT PHYSICAL_RECIPROCAL_MULTI_EDGE_CALIBRATION_BOUNDED_POSITIVE",
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
        check("the Cycle-393 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "rank 27, up from 20",
        "strictly positive normalized alternative grade still exists",
        "650,605 routed one-to-three-m2 primitives",
        "zero residual to printed precision",
        "not yet a strict physical compiler",
        "failures of two declared composition ansatzes",
        "not a shared obstruction and not axiom pressure",
        "three-dimensional lattice and its 24 proper-cubic frames remain spatial",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the physical gains, exact boundaries, imports, and semantic firewall",
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

    with ThreadPoolExecutor(max_workers=3) as pool:
        results = tuple(pool.map(execute, ROUTES))
    rows = []
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
        "all three compiler/response routes cold-execute green",
        all(row["exit"] == 0 and row["pass"] and row["result"] for row in rows),
        rows,
    )
    return outputs


def overlap_controls(outputs: dict[str, str]) -> None:
    output = outputs["overlap_compiler"]
    check(
        "seven physical overlap menus raise exact installed rank while positive alternatives remain",
        "'installed_physical_menu_presentations': 43" in output
        and "'effect_classes_after': 55" in output
        and "'rank_before': 20" in output
        and "'rank_after': 27" in output
        and "'positive_affine_dimension': 28" in output
        and "'compiled_row_deletion_ranks': (26, 26, 26, 26, 26, 26, 26)" in output
        and "'maximum_target_effect_recovery_residual': 4.9456354792602635e-16" in output
        and "'E_G_logical_minus_G_physical_E': 0.0" in output
        and "'proper_cubic_frames': 24" in output
        and "'selected_numerical_grade': None" in output
        and "'axiom_pressure': None" in output,
        "physical rank gain without numerical-law selection",
    )


def arithmetic_controls(outputs: dict[str, str]) -> None:
    output = outputs["arithmetic_compiler"]
    check(
        "the two finite tables have an exact bounded nearest-neighbor primitive arithmetic compiler",
        "'declared_table_program_cases': 12" in output
        and "'exact_EG_failures': 0" in output
        and "'explicit_inverse_failures': 0" in output
        and "'routed_primitives': 650605" in output
        and "'maximum_primitive_support_M2': 3" in output
        and "'maximum_primitive_span_edges': 2" in output
        and "'line_M2': 88" in output
        and "'primitive_boundaries_audited': 650605" in output
        and "'compiled_patch_M2': 147" in output
        and "'compiled_installed_overhead_M2_per_cell': 114" in output
        and "'ordered_schedule_is_physical_time': False" in output
        and "'actuality_selector': None" in output,
        "constant finite compiler; table genesis and law-level admission remain supplied",
    )


def edge_controls(outputs: dict[str, str]) -> None:
    output = outputs["reciprocal_edge"]
    check(
        "one-edge calibration transfers blindly on physical edges while chain failures remain logical-comparator facts",
        "'maximum_relative_residual': 0.0" in output
        and "'calibration_refit': False" in output
        and "'maximum_transfer_reciprocity_residual': 2.168404344971009e-19" in output
        and "'maximum_pointer_reciprocity_residual': 5.082197683525802e-21" in output
        and "'Cycle325_shared_middle_site_compiler': None" in output
        and "'minimum_gain_relative_residual': 0.39048530577084767" in output
        and "'minimum_product_relative_residual': 0.9950091736901557" in output
        and "'scope': 'route-specific depth-three logical comparator; broader multi-edge compilers remain open'" in output
        and "'proper_cubic_frames': 24" in output
        and "'response_is_source': False" not in output
        and "'pointer_is_source': False" in output
        and "'pointer_is_gravity': False" in output
        and "'shared_obstruction': None" in output
        and "'axiom_pressure': None" in output,
        "strict adjacent-edge positive; shared-middle physical compiler remains open",
    )


def ledger_controls() -> None:
    text = normalized(NOTE)
    fields = (
        "domain", "state", "context", "atomic_law", "continuation",
        "availability", "concurrency", "record", "actuality", "statistics",
        "resource", "source/response",
    )
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    scores = ("83/43/99", "53/33/91", "78/38/99", "46/19/77", "55/27/99")
    check(
        "the 12-field contract, six-wall ledger, and evidence-weighted lane scores are explicit",
        all(f"| {field} |" in text for field in fields)
        and all(f"| {wall} |" in text for wall in walls)
        and all(score in text for score in scores)
        and "planning estimates, not truth probabilities" in text,
        {"fields": fields, "walls": walls, "scores": scores},
    )


def no_go_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    routes = (
        "original 36-menu physical overlap graph",
        "seven-menu fixed physical carrier",
        "further higher-outcome/host-merge/rotated/composed menus",
        "exact effect/coarse-cp quotient and class registry",
        "denominator-48 code-space normalization",
        "denominator-48 nn primitive arithmetic",
        "local table/menu admission and genesis",
        "additivity/affinity or continuous-ray law",
        "actual-member sampler and frequency theorem",
        "reciprocal adjacent physical edge",
        "one-edge gain and edge-product chain ansatzes",
        "strict shared-middle three-cell source compiler",
        "physical source identification and metric/clock response",
    )
    walls = ("o_menu", "o_grade", "o_actual", "o_source", "o_metric")
    pair_count = sum(
        f"{left} / {right}" in text for left, right in combinations(walls, 2)
    )
    check(
        "full N1-N8 blocks global no-go, minimum-content, shared-obstruction, and axiom-pressure promotion",
        all(sections)
        and all(route in text for route in routes)
        and pair_count == 10
        and "retain the two chain ansatz failures only as route-specific comparator facts" in text
        and "fail / do not ship a global born no-go" in text,
        {"sections": sections, "routes": len(routes), "wall_pairs": pair_count},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 393: MENU COMPILER / RECIPROCAL EDGE SYNTHESIS")
    print("authority=none; audit=unset; no selected grade, source, gravity, time, or axiom pressure")
    note_contract()
    outputs = cold_certificates()
    overlap_controls(outputs)
    arithmetic_controls(outputs)
    edge_controls(outputs)
    ledger_controls()
    no_go_controls()
    check(
        "Cycle 393 retains exact bounded gains and routes the remaining law-level bridges constructively",
        FAIL == 0,
        {
            "numerical_law_selected": None,
            "actuality_or_frequency": None,
            "physical_source_or_gravity": None,
            "time_law": None,
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
        print("RESULT PHYSICAL_MENU_COMPILER_RECIPROCAL_EDGE_SYNTHESIS_OPEN")
        return 1
    print("RESULT PHYSICAL_MENU_COMPILER_RECIPROCAL_EDGE_SYNTHESIS_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
