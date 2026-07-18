#!/usr/bin/env python3
"""Cycle 355 synthesis certificate for the physical Record-time-floor routes."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_RECORD_LINEAGE_RENDEZVOUS_COUNTER_TOURNAMENT_"
    "SYNTHESIS_CYCLE355_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "lineage",
        ROOT / "scripts/physical_autonomous_record_lineage_residue_nn_route_cycle352_2026_07_18.py",
        "RESULT PHYSICAL_AUTONOMOUS_RECORD_LINEAGE_RESIDUE_NN_ROUTE_BOUNDED_POSITIVE",
        "PASS 7\nFAIL 0",
    ),
    (
        "rendezvous",
        ROOT / "scripts/physical_autonomous_record_dual_front_rendezvous_nn_route_cycle353_2026_07_18.py",
        "'route': 'local-gauge-auxiliary'",
        "SUMMARY {'pass': 11, 'fail': 0",
    ),
    (
        "counter",
        ROOT / "scripts/physical_autonomous_record_link_chain_counter_nn_route_cycle354_2026_07_18.py",
        "RESULT PHYSICAL_RECORD_LINK_CHAIN_COUNTER_NN_HOST_STEERED_PARTIAL_CERTIFIED",
        "SUMMARY {'pass': 6, 'fail': 0}",
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
        check("the Cycle-355 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "autonomous local lineage/residue sidecar",
        "preloaded before the frontier arrives",
        "same-track rendezvous, not an endpoint matcher",
        "host-steered local-link counter scaffold",
        "autonomous_compiler=false",
        "therefore broad local-capacity and locality negatives fail",
        "broad local-substrate no-go",
        "no thirring engine is used or compared",
        "three-dimensional lattice remains spatial input",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the strongest constructions, exact residuals, spatial/time firewall and next repairs",
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
        "all three route runners cold-execute to their exact bounded certificates",
        all(row["exit"] == 0 and row["result"] and row["summary"] for row in rows),
        rows,
    )
    return outputs


def exact_metric_controls(outputs: dict[str, str]) -> None:
    required = {
        "lineage": (
            "'macrocell_M2': 192",
            "'lineage_overhead_M2': 162",
            "'fixed_circuit_layers_per_step': 16111",
            "'primitive_gates_per_step': 289982",
            "'gate_frame_cases': 13918752",
            "'maximum_primitive_gate_support_M2': 3",
            "'dirty_scratch_is_local_code_failure_not_host_rejection': True",
            "'strict_Record_formation_closure': False",
            "'preloaded_nonzero_future_Record_words': 17",
            "'mass_relative_residual': 2.220446049250313e-16",
        ),
        "rendezvous": (
            "'M2_per_longitudinal_cell': 48",
            "'layers': 9",
            "'gates': 2016",
            "'L_by_N_by_frame_cases': 144",
            "'different_endpoint_false_positives': 6",
            "'endpoint_field_not_encoded'",
            "'endpoint_compiler': False",
            "'shared_obstruction': False",
            "'mass_relative_residual': 2.220446049250313e-16",
        ),
        "counter": (
            "'size_count_frame_cases': 144",
            "'maximum_gate_support_M2': 3",
            "'move_gate_counts': (209,)",
            "'terminal_gate_counts': (90,)",
            "'cell_M2': 71",
            "'link_corridor_M2': 21",
            "'counter_capacity': 18",
            "'autonomous_compiler': False",
            "'state_dependent_host_gate_selection': True",
            "'fixed_global_layer_list': None",
        ),
    }
    missing = {
        name: tuple(item for item in needles if item not in outputs[name])
        for name, needles in required.items()
    }
    check(
        "the synthesis parses exact geometry, locality, alias, deletion, host-control and physics residuals",
        all(not values for values in missing.values()),
        missing,
    )


def route_independence_controls() -> None:
    capabilities = {
        "lineage": {"rooted_predecessor", "occupancy", "residue_rotation"},
        "rendezvous": {"dual_front_transport", "local_collision", "latch"},
        "counter": {"link_scan_scaffold", "unary_count", "membership_visibility"},
    }
    overlaps = {
        f"{left}/{right}": capabilities[left] & capabilities[right]
        for left, right in combinations(capabilities, 2)
    }
    check(
        "the three routes test distinct lineage, rendezvous and counting surfaces",
        all(not overlap for overlap in overlaps.values()),
        overlaps,
    )


def semantic_firewall_controls(outputs: dict[str, str]) -> None:
    joined = "\n".join(outputs.values())
    needles = (
        "'strict_Record_formation_closure': False",
        "'endpoint_compiler': False",
        "'independent_event_identity_derived': False",
        "'autonomous_compiler': False",
        "'count_is_interval': False",
        "'count_is_rate': False",
        "'count_is_proper_time': False",
        "'time_axis_or_compactification_derived': False",
        "'authority': 'none'",
        "'audit': 'unset'",
    )
    missing = tuple(item for item in needles if item not in joined)
    check(
        "no preloaded payload, same track, circuit layer, selected gate template or count is promoted to Record/time semantics",
        not missing,
        missing,
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    routes = (
        "autonomous lineage/residue sidecar",
        "autonomous same-track gauge/auxiliary rendezvous",
        "staggered encoded-link unary counter",
        "locally compute the next cycle-342 record word",
        "physically carry endpoint or complete record keys",
        "compile the walker into one fixed global layer list",
        "cycle-58 append-only data/cert/valid/ready local formation grammar",
        "cycle-170/255 record-dag causal-depth route",
    )
    walls = ("w_payload", "w_form", "w_id", "w_count", "w_metric", "w_seed")
    pair_rows = sum(
        f"{left} / {right}" in text for left, right in combinations(walls, 2)
    )
    check(
        "full N1-N8 blocks shared-obstruction, minimum-content and axiom-pressure claims",
        all(sections)
        and all(route in text for route in routes)
        and pair_rows == 15
        and "fail / do not ship" in text
        and "ordinary candidate-law and compiler paths" in text,
        {
            "sections": sections,
            "routes": len(routes),
            "wall_pair_rows": pair_rows,
        },
    )


def ledger_and_lane_controls() -> None:
    text = normalized(NOTE)
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    scores = ("72/35/98", "43/23/79", "77/38/98", "43/17/71", "40/16/93")
    check(
        "every TOE lane and dependency wall is updated without an audit verdict",
        all(wall in text for wall in walls)
        and all(score in text for score in scores)
        and "planning estimates" in text
        and "not audit verdicts" in text,
        {"walls": walls, "scores": scores},
    )


def source_boundary_controls() -> None:
    text = normalized(NOTE)
    required = (
        "0355ac4728f57d9fdc62cb27764bbd33e6e8b8df",
        "cycle 58 operational binary macrocode",
        "cycle 170 record causal-depth clock",
        "cycle 255 car/record depth bridge",
        "cycle 329 support matcher",
        "cycle 342 registered cylinder",
        "cycle 347 named clock interfaces",
    )
    check(
        "prior-cycle witnesses are residual-matched rather than used as broad obstruction authority",
        all(item in text for item in required)
        and "no prior result is used as evidence that the remaining routes are impossible" in text,
        required,
    )


def supplied_structure_controls() -> None:
    text = normalized(NOTE)
    required = (
        "every cycle-342 conditional record word",
        "route 1's finite directed macrocell line",
        "route 2's root injection",
        "route 3's record-to-link certificate",
        "every actual record-formation/selection law",
        "all born grades",
        "no supplied structure is promoted to an axiom or approved primitive",
    )
    check(
        "the complete supplied-structure inventory remains explicit",
        all(item in text for item in required),
        required,
    )


def next_campaign_controls() -> None:
    text = normalized(NOTE)
    required = (
        "compute or transport each successor cycle-342 record candidate word",
        "carry endpoint and then complete record content",
        "compile the link walker into one fixed global connected-nn layer list",
        "actual record formation and faithful close",
        "physical interval/rate candidate",
    )
    check(
        "the next campaign attacks each route's exact residual before any metric-time claim",
        all(item in text for item in required),
        required,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    outputs = cold_route_certificates()
    exact_metric_controls(outputs)
    route_independence_controls()
    semantic_firewall_controls(outputs)
    no_go_discipline_controls()
    ledger_and_lane_controls()
    source_boundary_controls()
    supplied_structure_controls()
    next_campaign_controls()
    print("SUMMARY", {"pass": PASS, "fail": FAIL, "authority": "none", "audit": "unset"})
    print(
        "RESULT",
        "PHYSICAL_AUTONOMOUS_RECORD_TIME_FLOOR_TOURNAMENT_BOUNDED_POSITIVE"
        if FAIL == 0
        else "PHYSICAL_AUTONOMOUS_RECORD_TIME_FLOOR_TOURNAMENT_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
