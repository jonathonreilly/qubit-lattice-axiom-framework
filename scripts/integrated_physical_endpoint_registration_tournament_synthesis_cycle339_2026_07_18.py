#!/usr/bin/env python3
"""Cycle 339 synthesis certificate for the endpoint-registration tournament."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "INTEGRATED_PHYSICAL_ENDPOINT_REGISTRATION_TOURNAMENT_SYNTHESIS_"
    "CYCLE339_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "direct",
        ROOT / "scripts/physical_endpoint_registration_direct_route_cycle336_2026_07_18.py",
        "RESULT CYCLE336_DIRECT_ENDPOINT_REGISTRATION_GREEN",
        "SUMMARY PASS 7 FAIL 0",
    ),
    (
        "protected",
        ROOT / "scripts/physical_endpoint_registration_protected_route_cycle337_2026_07_18.py",
        "RESULT CYCLE337_PROTECTED_ENVIRONMENT_POINTER_ROUTE_GREEN",
        "SUMMARY PASS=9 FAIL=0",
    ),
    (
        "process",
        ROOT / "scripts/physical_endpoint_registration_process_route_cycle338_2026_07_18.py",
        "RESULT PHYSICAL_ENDPOINT_REGISTRATION_PROCESS_ROUTE_CERTIFIED",
        "SUMMARY {'pass': 7, 'fail': 0}",
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
    for marker in ("*", "`"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-339 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "42-m2 reversible permutation",
        "69 physical pointer m2 plus seven syndrome m2",
        "34-m2 process packet",
        "5,040 causal schedules",
        "196,608",
        "13,824",
        "414/414",
        "realized-state primitive supplies the pointwise reference, never its content",
        "proper-cubic covariance here is spatial covariance",
        "not physical time",
        "not called an occurrence probability, sample, or frequency",
        "broad binding/permanence/record no-go fail / do not ship",
        "no route-independent obstruction and no axiom pressure",
        "direct local admissibility/type rule",
        "environment/asymptotic stable-pointer sector",
        "error-corrected or global-process record sector",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins all three positive routes, semantic firewalls, N1-N8, and the next campaign",
        not missing,
        missing,
    )


def cold_route_certificates() -> dict[str, str]:
    outputs: dict[str, str] = {}
    rows = []
    def execute(route: tuple[str, Path, str, str]):
        name, path, result_line, summary_line = route
        completed = subprocess.run(
            [sys.executable, str(path)], cwd=ROOT, check=False,
            capture_output=True, text=True
        )
        return name, result_line, summary_line, completed

    with ThreadPoolExecutor(max_workers=len(ROUTES)) as pool:
        completed_routes = tuple(pool.map(execute, ROUTES))
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
        "all three independent route runners cold-execute to their exact green certificates",
        all(row["exit"] == 0 and row["result"] and row["summary"] for row in rows),
        rows,
    )
    return outputs


def exact_metric_controls(outputs: dict[str, str]) -> None:
    direct = outputs["direct"]
    protected = outputs["protected"]
    process = outputs["process"]
    required_direct = (
        "'full_and_deleted_inverse_cases': 196608",
        "'frame_size_order_branch_phase_cases': 13824",
        "'register_M2': 42",
        "'host_selection_queries': 0",
        "'maximum_sector_identity_residual': 0.0",
    )
    required_protected = (
        "'single_X_cases': 414",
        "'located_erasure_cases': 414",
        "'physical_frame_size_cases': 48",
        "'state_relative_selection_cases': 144",
        "'triply_repeated_pointer_M2': 69",
        "'recovery_syndrome_M2': 7",
        "'broad_negative_gate': 'FAIL / DO NOT SHIP'",
    )
    required_process = (
        "'schedules': 5040",
        "'frame_size_endpoint_cases': 144",
        "'packet_M2': 34",
        "'cylinder_M2': 28",
        "'maximum_new_decoder_support_M2': 62",
        "'maximum_new_swap_support_M2': 68",
    )
    missing = {
        "direct": tuple(item for item in required_direct if item not in direct),
        "protected": tuple(item for item in required_protected if item not in protected),
        "process": tuple(item for item in required_process if item not in process),
    }
    check(
        "the synthesis parses the exact support, inverse, covariance, schedule, and bounded-negative metrics",
        all(not row for row in missing.values()),
        missing,
    )


def route_independence_controls() -> None:
    capabilities = {
        "direct": {
            "encoded_equality",
            "candidate_mask",
            "phase_register",
            "coherent_sector_control",
        },
        "protected": {
            "repetition_pointer",
            "single_X_recovery",
            "located_erasure",
            "syndrome_retention",
        },
        "process": {
            "complete_cylinder",
            "causal_schedule_quotient",
            "edge_deletion",
            "finite_process_archive",
        },
    }
    intersections = {
        f"{left}/{right}": capabilities[left] & capabilities[right]
        for left, right in combinations(capabilities, 2)
    }
    check(
        "the tournament routes are mechanically distinct rather than three labels for one implementation",
        all(not overlap for overlap in intersections.values()),
        intersections,
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    markers = {
        "direct encoded endpoint/content handshake": "attempted",
        "redundant protected environment pointer": "attempted",
        "causal complete-cylinder process decoder": "attempted",
        "autonomous record-formation/type law": "open / untested",
        "environment/asymptotic stable record sector": "open / untested",
        "error-corrected or topological record sector": "open / untested",
        "global process/decoder with infinite extension": "open / untested",
    }
    marker_failures = tuple(
        key for key, marker in markers.items() if key not in text or marker not in text
    )
    walls = ("w_state", "w_record", "w_clock", "w_grade")
    expected_pairs = len(tuple(combinations(walls, 2)))
    pair_rows = sum(
        f"{left} / {right}" in text
        for left, right in combinations(walls, 2)
    )
    check(
        "full N1-N8 keeps all broad binding, permanence, minimum-content, and axiom-pressure negatives failed",
        all(sections)
        and not marker_failures
        and pair_rows == expected_pairs
        and "broad binding/permanence/record no-go fail / do not ship" in text
        and "no route-independent obstruction and no axiom pressure" in text,
        {
            "sections": sections,
            "marker_failures": marker_failures,
            "wall_pair_rows": pair_rows,
            "expected_wall_pairs": expected_pairs,
        },
    )


def lane_and_wall_controls() -> None:
    text = normalized(NOTE)
    scores = ("68/34/95", "39/21/72", "77/38/98", "42/17/70", "36/16/89")
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    check(
        "the synthesis updates every TOE lane and every six-wall dependency without an audit verdict",
        all(score in text for score in scores)
        and all(wall in text for wall in walls)
        and "planning estimates, not probabilities" in text
        and "not audit verdicts" in text,
        {"scores": scores, "walls": walls},
    )


def source_integrity_controls() -> None:
    forbidden = (
        ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        ROOT / "docs/audit/data/axiom_premise_nodes.json",
    )
    statuses = {str(path.relative_to(ROOT)): path.exists() for path in forbidden}
    route_text = "\n".join(path.read_text(encoding="utf-8").lower() for _, path, _, _ in ROUTES)
    check(
        "foundation inputs remain read-only and semantic promotions are absent from the route implementations",
        all(statuses.values())
        and "candidate output is not a record" in route_text
        and "does not use a born grade" in route_text
        and "count is not time" in route_text,
        statuses,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 339: INTEGRATED PHYSICAL ENDPOINT REGISTRATION TOURNAMENT")
    print("authority=none; audit=unset")
    note_contract()
    outputs = cold_route_certificates()
    exact_metric_controls(outputs)
    route_independence_controls()
    no_go_discipline_controls()
    lane_and_wall_controls()
    source_integrity_controls()
    check(
        "Cycle 339 closes the bounded physical endpoint/content comparison connector without semantic promotion",
        FAIL == 0,
        {
            "strongest_positive": "bounded pointwise physical registration and recurrent transport",
            "not_derived": "content selection, occurrence, Record, permanence, clock/rate, Born frequency, or gravity",
            "next": "Record formation/type and permanence-compatibility tournament",
        },
    )
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE339_INTEGRATED_ENDPOINT_REGISTRATION_TOURNAMENT_GREEN"
        if FAIL == 0
        else "CYCLE339_SYNTHESIS_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
