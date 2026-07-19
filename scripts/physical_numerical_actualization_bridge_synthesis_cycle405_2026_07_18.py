#!/usr/bin/env python3
"""Cycle 405: numerical/actualization bridge synthesis.

Cold-executes Cycles 401--404 and checks the composed numerical surface,
exact cross-registry extension, source-response actualization alternatives,
12-field law contract, six-wall ledger, and full N1--N8 scope firewall.

No numerical law, probability, actual member, Record law, source, gravity,
time, shared obstruction, or axiom pressure is selected.  Authority is none;
audit is unset.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_NUMERICAL_ACTUALIZATION_BRIDGE_"
    "SYNTHESIS_CYCLE405_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "same_program",
        "physical_two_use_composed_instrument_extension_cycle401_2026_07_18.py",
        "PASS 10\nFAIL 0",
        "RESULT PHYSICAL_TWO_USE_COMPOSED_INSTRUMENT_EXTENSION_EXACT_RANK_GAIN",
    ),
    (
        "registry_extension",
        "physical_exact_registry_extension_bridge_cycle402_2026_07_18.py",
        "SUMMARY PASS=7 FAIL=0",
        None,
    ),
    (
        "actualization",
        "physical_source_response_actualization_law_tournament_cycle403_2026_07_18.py",
        "SUMMARY {'pass': 16, 'fail': 0}",
        "RESULT PHYSICAL_SOURCE_RESPONSE_ACTUALIZATION_LAW_TOURNAMENT_CERTIFIED",
    ),
    (
        "cross_program",
        "physical_cross_program_rewrite_composition_cycle404_2026_07_18.py",
        "PASS 10\nFAIL 0",
        "RESULT PHYSICAL_CROSS_PROGRAM_REWRITE_COMPOSITION_EXACT_RANK_GAIN",
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
        check("the Cycle-405 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "no route-independent obstruction",
        "there is no axiom pressure",
        "the 3d coordinates and all 24 proper-cubic frames remain spatial",
        "ordered circuit composition is not time",
        "b has exact nonnegative extensions, but they form a 19-dimensional face",
        "the resulting conditional causal depth changes from four to five",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the numerical/actualization bridge and semantic firewall",
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

    # Limit concurrent exact-rank jobs while still cold-executing independently.
    with ThreadPoolExecutor(max_workers=2) as pool:
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
        "all four child routes cold-execute green",
        all(row["exit"] == 0 and row["pass"] and row["result"] for row in rows),
        rows,
    )
    return outputs


def numerical_controls(outputs: dict[str, str]) -> None:
    same = outputs["same_program"]
    bridge = outputs["registry_extension"]
    cross = outputs["cross_program"]
    check(
        "same- and cross-program physical composition change the finite class/rank surface",
        "'final_shape_classes_rank_affine': ((353, 636), 636, 192, 444)" in same
        and "'new_classes_and_rank': (581, 161)" in same
        and "'effect_process_pairs': 785" in same
        and "'final_shape_classes_rank_affine': ((2063, 3348), 3348, 1159, 2189)" in cross
        and "'new_classes_and_rank_over_Cycle401': (2712, 967)" in cross
        and "'effect_process_pairs': 4015" in cross,
        "finite physical composition; no selected grade or Born law",
    )
    check(
        "the matrix-derived registry bridge gives a physical ambiguous B extension and scoped exact A certificate",
        "'mapping': (20, 21, 24, 25, 28, 8, 33, 34, 41)" in bridge
        and "'B_nonnegative_face_dimension': 19" in bridge
        and "'two_exact_B_extensions_differing_components': 41" in bridge
        and "'A_Farkas_right_hand_side': -1" in bridge
        and "'B_forced_zero_right_hand_side': 0" in bridge
        and "'line_M2': 827" in bridge
        and "'routed_primitives': 1273729" in bridge
        and "'one_bit_false_admissions': 0" in bridge
        and "'Record_payload_identity_failures': 0" in bridge
        and "'Born_law': None" in bridge,
        "B compatibility is a 19-dimensional face; A result remains fixed-system scoped",
    )


def actualization_controls(outputs: dict[str, str]) -> None:
    output = outputs["actualization"]
    check(
        "the physical response reaches three honest route-distinct actualization boundaries",
        "'global_inverse_residual': 0.0" in output
        and "'environment_label_is_Record': False" in output
        and "'post_dilation_depth': 4" in output
        and "'conditional_linked_depth': 5" in output
        and "'physical_gate_compiler': None" in output
        and "'three_independent_Cycle399_instances': True" in output
        and "'post_commit_inverse_rejections': 2" in output
        and "'CONSUME_admitted_by_framework': None" in output
        and "'branch_Record_hash_failures': 0" in output
        and "'proper_cubic_frames': 24" in output
        and "'law_selected': False" in output
        and "'branch_selected': False" in output,
        "reversible environment/no Record versus two supplied conditional Record laws",
    )
    check(
        "held response weights are reciprocal and remain explicitly nonprobabilistic",
        "5.958479723237607e-06" in output
        and "5.958479723237605e-06" in output
        and "3.0046754132975383e-05" in output
        and "3.004675413297537e-05" in output
        and "squared-norm sector weight, not probability/Born weight" in output,
        "state-sector weights only",
    )


def ledger_controls() -> None:
    text = normalized(NOTE)
    fields = (
        "domain", "state", "context", "atomic_law", "continuation",
        "availability", "concurrency", "record", "actuality", "statistics",
        "resource", "source/response",
    )
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    scores = ("85/44/99", "55/33/94", "78/38/99", "53/24/86", "64/36/99")
    check(
        "the 12-field contract, six-wall ledger, and updated lane scores are explicit",
        all(f"| {field} |" in text for field in fields)
        and all(f"| {wall} |" in text for wall in walls)
        and all(score in text for score in scores)
        and "planning coordinates, not truth probabilities or audit verdicts" in text,
        {"fields": fields, "walls": walls, "scores": scores},
    )


def no_go_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    routes = (
        "same-program composition",
        "reversible cross-program rewriting",
        "the exact nine/55 registry map",
        "two nonnegative b extensions",
        "reversible environment dilation",
        "immediate candidate formation",
        "threshold-three candidate formation",
        "altered registries for a",
        "composed constraints on the b face",
        "a coherent blank-record dilation",
        "the migrating formation law",
        "physical commit admission",
        "source-to-metric response",
    )
    check(
        "full N1-N8 blocks broad no-go, minimum-content, shared-obstruction, and axiom-pressure promotion",
        all(sections)
        and all(route in text for route in routes)
        and "the gate fails for a broad numerical, born, actualization, time, gravity" in text
        and "no current route-specific residual is constitutional evidence" in text,
        {"sections": sections, "routes": len(routes)},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 405: NUMERICAL/ACTUALIZATION BRIDGE SYNTHESIS")
    print("authority=none; audit=unset; no selected grade, actual member, source, time, or axiom pressure")
    note_contract()
    outputs = cold_certificates()
    numerical_controls(outputs)
    actualization_controls(outputs)
    ledger_controls()
    no_go_controls()
    check(
        "Cycle 405 retains the bounded bridge gains and routes every remaining wall constructively",
        FAIL == 0,
        {
            "numerical_law_selected": None,
            "Born_or_frequency_law": None,
            "actual_member_or_Record_law": None,
            "physical_source_or_gravity": None,
            "interval_or_rate": None,
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
        print("RESULT PHYSICAL_NUMERICAL_ACTUALIZATION_BRIDGE_SYNTHESIS_OPEN")
        return 1
    print("RESULT PHYSICAL_NUMERICAL_ACTUALIZATION_BRIDGE_SYNTHESIS_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
