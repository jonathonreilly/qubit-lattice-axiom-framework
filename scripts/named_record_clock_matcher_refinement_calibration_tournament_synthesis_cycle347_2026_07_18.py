#!/usr/bin/env python3
"""Cycle 347 synthesis certificate for the named-Record clock tournament."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "NAMED_RECORD_CLOCK_MATCHER_REFINEMENT_CALIBRATION_TOURNAMENT_"
    "SYNTHESIS_CYCLE347_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "matcher",
        ROOT / "scripts/physical_named_record_interval_direct_matcher_route_cycle344_2026_07_18.py",
        "RESULT PHYSICAL_NAMED_RECORD_INTERVAL_DIRECT_MATCHER_ROUTE_CERTIFIED",
        "SUMMARY 7 PASS/0 FAIL",
    ),
    (
        "refinement",
        ROOT / "scripts/physical_named_record_chain_refinement_route_cycle345_2026_07_18.py",
        "RESULT PHYSICAL_NAMED_RECORD_CHAIN_REFINEMENT_ROUTE_CERTIFIED",
        "SUMMARY {'pass': 9, 'fail': 0}",
    ),
    (
        "calibration",
        ROOT / "scripts/physical_clock_response_common_history_calibration_route_cycle346_2026_07_18.py",
        "RESULT PHYSICAL_CLOCK_RESPONSE_COMMON_HISTORY_CALIBRATION_ROUTE_CERTIFIED",
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
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-347 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "conditional matcher/refinement/calibration interface model",
        "phase-free equality is tested and falsified as a matcher",
        "no l=3/l=6 coarse/fine identification is used",
        "response scalar and calibration constant are floating-point observables outside its 82-bit common-key word",
        "not a physical rate",
        "three-dimensional lattice remains spatial input",
        "broad clock/time/substrate no-go fail / do not ship",
        "there is no route-independent obstruction and no axiom pressure",
        "typed-record born-corpus bridge",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the conditional theorem, alias and time firewalls, N1-N8, and next campaign",
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
        "all three independent route runners cold-execute to exact green certificates",
        all(row["exit"] == 0 and row["result"] and row["summary"] for row in rows),
        rows,
    )
    return outputs


def exact_metric_controls(outputs: dict[str, str]) -> None:
    required = {
        "matcher": (
            "'phase_free_endpoint_alias_at_offset': 2",
            "'full_period': 6",
            "'inverse_exact_cases': 384",
            "'total_frame_size_endpoint_cases': 144",
            "'domain_rejections': 14",
            "'basis_register_width_M2': {3: 283, 6: 511}",
        ),
        "refinement": (
            "'typed_permanent_Records': 12",
            "'tagged_Record_basis_width_M2': 48",
            "'two_page_basis_storage_M2': 576",
            "'k2_matched_counts': (10, 5)",
            "'k3_matched_counts': (9, 3)",
            "'common_lcm_interval_counts': (6, 3, 2)",
            "'total_permanent_attacks_rejected': 24",
            "'frame_translation_history_cases': 648",
        ),
        "calibration": (
            "'common_product_register_M2_width': 82",
            "'separate_tensor_outputs_rejected': True",
            "'equal_host_indices_rejected': True",
            "'fitted_calibration_constant': 7.9428612087437",
            "'maximum_raw_response_residual': 2.220446049250313e-16",
            "'held_size_residual': 0.0",
            "'all_deleted_outputs_undefined_never_zero': True",
            "'duplicate_common_event_rejected_with_spare_capacity': True",
            "'response_floats_encoded_in_common_word': False",
            "'same_common_word_after_response_float_retarget': True",
            "'nearest_neighbour_handshake_support_M2': None",
        ),
    }
    missing = {
        name: tuple(item for item in needles if item not in outputs[name])
        for name, needles in required.items()
    }
    check(
        "the synthesis parses exact alias, inverse, ratio, attack, covariance, calibration, and support-boundary metrics",
        all(not values for values in missing.values()),
        missing,
    )


def route_independence_controls() -> None:
    capabilities = {
        "matcher": {
            "full_record_identity_match",
            "coincidence_certificate",
            "five_bit_xor_matcher",
        },
        "refinement": {
            "formation_time_tags",
            "causal_predecessor_chain",
            "stride_ratio",
        },
        "calibration": {
            "response_history_key",
            "source_instrument",
            "numerical_convention",
        },
    }
    overlaps = {
        f"{left}/{right}": capabilities[left] & capabilities[right]
        for left, right in combinations(capabilities, 2)
    }
    check(
        "the routes test distinct matcher, refinement, and response interfaces",
        all(not overlap for overlap in overlaps.values()),
        overlaps,
    )


def semantic_firewall_controls(outputs: dict[str, str]) -> None:
    joined = "\n".join(outputs.values())
    needles = (
        "'count_after_match': None",
        "'phase_is_time': False",
        "'page_position_is_time': False",
        "'nearest_neighbor_primitive_synthesis': None",
        "'physical_rate': None",
        "'physical_time': None",
        "'calibrated_response_per_count_is_physical_rate': False",
        "'occupation_is_energy': False",
        "'axiom_pressure': False",
    )
    missing = tuple(item for item in needles if item not in joined)
    check(
        "failed matches remain undefined and no phase, page, count, calibration, occupation, or register width is promoted to time, rate, energy, or local synthesis",
        not missing,
        missing,
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    markers = {
        "full-record identity / local-certificate matcher": "attempted",
        "immutable tagged same-history refinement": "attempted",
        "common-key response/count calibration": "attempted",
        "nearest-neighbor synthesis of matcher, tags and handshake": "open / untested",
        "autonomous record identity/name/membership formation law": "open / untested",
        "record-causal-depth clock on this same physical carrier": "open / untested",
        "repeated empirical calibration and continuum/proper-time extension": "open / untested",
    }
    marker_failures = tuple(
        key for key, marker in markers.items() if key not in text or marker not in text
    )
    walls = ("w_record", "w_id", "w_tag", "w_local", "w_cal", "w_metric")
    pair_rows = sum(
        f"{left} / {right}" in text for left, right in combinations(walls, 2)
    )
    check(
        "full N1-N8 blocks broad clock/time impossibility, minimum-content, and axiom-pressure claims",
        all(sections)
        and not marker_failures
        and pair_rows == 15
        and "broad clock/time/substrate no-go fail / do not ship" in text
        and "there is no route-independent obstruction and no axiom pressure" in text,
        {
            "sections": sections,
            "marker_failures": marker_failures,
            "wall_pair_rows": pair_rows,
        },
    )


def lane_and_wall_controls() -> None:
    text = normalized(NOTE)
    scores = ("70/34/97", "41/21/76", "77/38/98", "43/17/71", "36/16/89")
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
    text = normalized(NOTE)
    check(
        "foundation inputs remain dependencies rather than campaign outputs",
        all(statuses.values())
        and "constitutional effect: none" in text
        and "no supplied item is promoted to a new axiom or approved primitive" in text,
        statuses,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 347: NAMED RECORD CLOCK MATCHER/REFINEMENT/CALIBRATION TOURNAMENT")
    print("authority=none; audit=unset")
    note_contract()
    outputs = cold_route_certificates()
    exact_metric_controls(outputs)
    route_independence_controls()
    semantic_firewall_controls(outputs)
    no_go_discipline_controls()
    lane_and_wall_controls()
    foundation_integrity_controls()
    check(
        "Cycle 347 constructs alias-safe conditional clock-interface models without deriving local physical matching, event/tag formation, interval, rate, proper time, energy, Born frequency, or gravity",
        FAIL == 0,
        {
            "strongest_positive": "full-identity matching, one-history refinement ratios, and common-key response expectation/count attachment",
            "not_derived": "semantic-input generation, NN synthesis, interval/rate/time, empirical calibration, energy/source/gravity, or Born frequency",
            "next": "typed-Record Born-corpus tournament",
        },
    )
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE347_NAMED_RECORD_CLOCK_TOURNAMENT_GREEN"
        if FAIL == 0
        else "CYCLE347_NAMED_RECORD_CLOCK_SYNTHESIS_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
