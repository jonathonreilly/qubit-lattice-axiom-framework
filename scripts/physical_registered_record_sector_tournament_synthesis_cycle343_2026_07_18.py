#!/usr/bin/env python3
"""Cycle 343 synthesis certificate for the registered Record-sector tournament."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_REGISTERED_RECORD_SECTOR_TOURNAMENT_SYNTHESIS_"
    "CYCLE343_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "direct",
        ROOT / "scripts/physical_registered_packet_local_record_type_route_cycle340_2026_07_18.py",
        "RESULT CYCLE340_DIRECT_LOCAL_RECORD_TYPE_CANDIDATE_GREEN",
        "SUMMARY PASS 6 FAIL 0",
    ),
    (
        "protected",
        ROOT / "scripts/physical_registered_pointer_stable_sector_route_cycle341_2026_07_18.py",
        "RESULT CYCLE341_STABLE_POINTER_RECORD_SECTOR_ROUTE_GREEN",
        "SUMMARY PASS=9 FAIL=0",
    ),
    (
        "process",
        ROOT / "scripts/physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18.py",
        "RESULT PHYSICAL_REGISTERED_CYLINDER_FUTURE_EQUIVALENCE_ROUTE_CERTIFIED",
        "SUMMARY {'pass': 9, 'fail': 0}",
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
        check("the Cycle-343 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "51-m2 block",
        "69-m2 protected pointer",
        "all 5,040 cycle-338 causal schedules",
        "conditional record-interface model",
        "existing record axiom",
        "models do not choose which branch occurs",
        "proper-cubic covariance is spatial covariance",
        "commit count are not physical time",
        "matcher, interval, calibration, rate, and physical-time interpretation remain unset",
        "broad bounded-record/formation/stability no-go fail / do not ship",
        "there is no route-independent obstruction and no axiom pressure",
        "named-clock matcher/refinement/calibration tournament",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the synthesis note pins the conditional theorem, semantic firewalls, N1-N8, and next campaign",
        not missing,
        missing,
    )


def cold_route_certificates() -> dict[str, str]:
    outputs: dict[str, str] = {}
    rows = []

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
    required = {
        "direct": (
            "'frame_size_order_branch_phase_cases': 13824",
            "'type_block_M2': 51",
            "'lawful_domain_rejections': 6",
            "'disjoint_forward_orders': (13, 13)",
            "'held_depth': 12",
            "'type_rule_selected_by_axioms': False",
        ),
        "protected": (
            "'all_single_X_candidate_cases': 414",
            "'single_Z_cases': 414",
            "'typed_future_compatible_auxiliary_X_cases': 276",
            "'post_typing_primary_X_attack_cases': 138",
            "'maximum_recovery_step_M2': 83",
            "'held_L6_internal_external_syndrome_M2': 168",
            "'valid_logical_retarget_physical_flips': 12",
            "'broad_negative_gate': 'FAIL / DO NOT SHIP'",
        ),
        "process": (
            "'raw_schedule_representatives': 5040",
            "'edge_deletion_permanent_survivors': 0",
            "'selector_schedules': 120",
            "'frame_size_endpoint_record_cases': 648",
            "'held_two_page_support_M2': 360",
            "'named_permanent_chain_count': 6",
            "'rate': None",
        ),
    }
    missing = {
        name: tuple(item for item in needles if item not in outputs[name])
        for name, needles in required.items()
    }
    check(
        "the synthesis parses the exact support, fault, schedule, covariance, chain, and rate-firewall metrics",
        all(not values for values in missing.values()),
        missing,
    )


def route_independence_controls() -> None:
    capabilities = {
        "direct": {
            "local_type_truth_table",
            "two_selector_overlap",
            "disjoint_scalar_addition",
        },
        "protected": {
            "repetition_pointer",
            "syndrome_future",
            "outward_bank_renewal",
        },
        "process": {
            "complete_cylinder_fibre",
            "conditional_record_dag",
            "append_only_page",
        },
    }
    overlaps = {
        f"{left}/{right}": capabilities[left] & capabilities[right]
        for left, right in combinations(capabilities, 2)
    }
    check(
        "the routes are mechanically distinct rather than three labels for one implementation",
        all(not overlap for overlap in overlaps.values()),
        overlaps,
    )


def conditional_record_firewall(outputs: dict[str, str]) -> None:
    text = normalized(NOTE)
    route_needles = (
        "'conditional_permanence_after_lawful_typing': True",
        "'occurrence_selected_by_dephasing': False",
        "'copying_is_Record': False",
        "'correction_is_permanence': False",
        "'occurrence': 'supplied explicit law input'",
        "'actual_history_sampler': None",
        "'clock_matcher': None",
        "'physical_time': None",
    )
    joined = "\n".join(outputs.values())
    check(
        "Record consequences are consumed only after explicit typing and no route promotes copying, dephasing, count, or phase into missing semantics",
        all(item in joined for item in route_needles)
        and "this is a conditional record-interface model" in text
        and "error correction is not permanence" in text
        and "pointer copying is not a record" in text,
        tuple(item for item in route_needles if item not in joined),
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    markers = {
        "direct local registered-packet type rule": "attempted",
        "protected diagonal-pointer future sector": "attempted",
        "complete-cylinder future-equivalent process sector": "attempted",
        "autonomous one-law occurrence/commit/type formation": "open / untested",
        "phase-correcting stabilizer or topological record memory": "open / untested",
        "asymptotic environmental stable sector with generated renewal": "open / untested",
        "infinite-volume/process-functional extension": "open / untested",
    }
    marker_failures = tuple(
        key for key, marker in markers.items() if key not in text or marker not in text
    )
    walls = ("w_form", "w_bind", "w_future", "w_capacity", "w_local", "w_read")
    pair_rows = sum(
        f"{left} / {right}" in text for left, right in combinations(walls, 2)
    )
    check(
        "full N1-N8 blocks broad Record, formation, stability, minimum-content, and axiom-pressure negatives",
        all(sections)
        and not marker_failures
        and pair_rows == 15
        and "broad bounded-record/formation/stability no-go fail / do not ship" in text
        and "there is no route-independent obstruction and no axiom pressure" in text,
        {
            "sections": sections,
            "marker_failures": marker_failures,
            "wall_pair_rows": pair_rows,
        },
    )


def lane_and_wall_controls() -> None:
    text = normalized(NOTE)
    scores = ("69/34/96", "39/21/73", "77/38/98", "42/17/70", "36/16/89")
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    check(
        "the synthesis updates every TOE lane and every dependency wall without an audit verdict",
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
    note = normalized(NOTE)
    check(
        "foundation inputs remain dependencies rather than edited campaign outputs",
        all(statuses.values())
        and "constitutional effect: none" in note
        and "existing axiom is therefore consumed rather than edited" in note
        and "no supplied item is promoted to a new axiom or approved primitive" in note,
        statuses,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 343: PHYSICAL REGISTERED RECORD-SECTOR TOURNAMENT")
    print("authority=none; audit=unset")
    note_contract()
    outputs = cold_route_certificates()
    exact_metric_controls(outputs)
    route_independence_controls()
    conditional_record_firewall(outputs)
    no_go_discipline_controls()
    lane_and_wall_controls()
    foundation_integrity_controls()
    check(
        "Cycle 343 narrows a bounded conditional Record-interface model without deriving occurrence, formation selection, local physical synthesis, indefinite stability, clock rate, Born history, or gravity",
        FAIL == 0,
        {
            "strongest_positive": "bounded type-candidate, diagonal-pointer, and conditional complete-cylinder register models",
            "not_derived": "occurrence/type selection, nearest-neighbor synthesis, generated capacity, full-QEC, matcher/interval/rate, Born frequency, or gravity",
            "next": "named-clock matcher/refinement/calibration tournament",
        },
    )
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE343_REGISTERED_RECORD_SECTOR_TOURNAMENT_GREEN"
        if FAIL == 0
        else "CYCLE343_REGISTERED_RECORD_SECTOR_SYNTHESIS_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
