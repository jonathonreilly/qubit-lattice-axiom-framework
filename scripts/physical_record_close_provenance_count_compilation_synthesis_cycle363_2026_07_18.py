#!/usr/bin/env python3
"""Cycle 363 synthesis for physical close, provenance, and count compilation."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_CLOSE_PROVENANCE_COUNT_COMPILATION_"
    "SYNTHESIS_CYCLE363_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "counter",
        ROOT / "scripts/physical_autonomous_record_link_counter_fixed_global_nn_route_cycle360_2026_07_18.py",
        "'strongest_constructive_result': 'autonomous_fixed_global_connected_NN_dimensionless_Record_member_count'",
        "SUMMARY {'pass': 7, 'fail': 0",
    ),
    (
        "close",
        ROOT / "scripts/physical_autonomous_record_payload_faithful_close_nn_route_cycle361_2026_07_18.py",
        "RESULT PHYSICAL_AUTONOMOUS_RECORD_PAYLOAD_FAITHFUL_CLOSE_NN_ROUTE_BOUNDED_POSITIVE",
        "PASS 5\nFAIL 0",
    ),
    (
        "provenance",
        ROOT / "scripts/physical_fixed_global_common_fork_record_lineage_nn_route_cycle362_2026_07_18.py",
        "RESULT PHYSICAL_FIXED_GLOBAL_COMMON_FORK_RECORD_LINEAGE_NN_ROUTE_BOUNDED_POSITIVE",
        "PASS 9\nFAIL 0",
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
        check("the Cycle-363 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "fixed-global record-member count",
        "payload-faithful close candidate",
        "rooted common-fork provenance",
        "does not form a new framework record",
        "the three runners are complementary witnesses",
        "three-dimensional lattice is spatial input",
        "there is no shared obstruction and no axiom pressure",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the close/provenance/count theorem and semantic firewalls",
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

    with ThreadPoolExecutor(max_workers=3) as pool:
        results = tuple(pool.map(execute, ROUTES))
    rows = []
    for name, result_line, summary_line, completed in results:
        output = completed.stdout + completed.stderr
        outputs[name] = output
        rows.append(
            {
                "route": name,
                "exit": completed.returncode,
                "result": result_line in output,
                "summary": summary_line in output,
                "lines": len(output.splitlines()),
            }
        )
    check(
        "all three route runners cold-execute to their exact green certificates",
        all(row["exit"] == 0 and row["result"] and row["summary"] for row in rows),
        rows,
    )
    return outputs


def exact_metric_controls(outputs: dict[str, str]) -> None:
    required = {
        "counter": (
            "'M2_sites': 961",
            "'M2_sites': 1945",
            "'M2_sites': 2929",
            "'cell_M2': 141",
            "'bond_M2': 23",
            "'layers': 156",
            "'L_by_N_by_frame_cases': 144",
            "'local_selector_guard_constraint_failures': 0",
            "'selector_fault_local_constraint_failures': 3",
            "'guard_deletion_reflection_count_delta': 1",
            "'state_dependent_host_gate_selection': False",
        ),
        "close": (
            "'macrocell_M2': 223",
            "'constant_overhead_M2': 193",
            "'certificate_M2': 66",
            "'fixed_layers_per_step': 397410",
            "'primitive_gates_per_step': 7153244",
            "'final_future_close_candidates': 17",
            "'gate_frame_cases': 343352448",
            "'sampled_deletion_failures': 0",
            "'global_scratch_precheck': False",
            "'K_form': None",
        ),
        "provenance": (
            "'M2_sites': 1218",
            "'M2_sites': 1986",
            "'M2_sites': 2754",
            "'fixed_layers': 131",
            "'primitive_gates': 7542",
            "'L_by_N_by_frame_cases': 144",
            "'distinct_root_false_latches': 0",
            "'global_source_code_precheck': False",
            "'universal_event_identity_derived': False",
        ),
    }
    missing = {
        name: tuple(item for item in needles if item not in outputs[name])
        for name, needles in required.items()
    }
    check(
        "exact resources, covariance, faults, host-control and semantic residuals are parsed",
        all(not values for values in missing.values()),
        missing,
    )


def constructive_ladder_controls(outputs: dict[str, str]) -> None:
    check(
        "the ladder independently compiles fixed counting, faithful close, and bounded common ancestry",
        "'forward_count': 18" in outputs["counter"]
        and "'reverse_sector_local_constraint_failures': 0" in outputs["counter"]
        and "'future_close_candidate_bits_initially_one': 0" in outputs["close"]
        and "'close_candidate_is_Record': False" in outputs["close"]
        and "'common_root_latches': 1" in outputs["provenance"]
        and "'distinct_root_latches': 0" in outputs["provenance"],
        "three positive but typed-separate arrows",
    )


def semantic_firewall_controls(outputs: dict[str, str]) -> None:
    joined = "\n".join(outputs.values())
    needles = (
        "'count_is_interval': False",
        "'count_is_rate': False",
        "'close_candidate_is_Record': False",
        "'irreversible_formation_generated': False",
        "'universal_event_identity_derived': False",
        "'actualization_derived': False",
        "'circuit_layers_are_time': False",
        "'authority': 'none'",
        "'audit': 'unset'",
    )
    missing = tuple(item for item in needles if item not in joined)
    check(
        "count, close, basis copies, and common-cause witnesses are not promoted to Record, identity or time",
        not missing,
        missing,
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    routes = (
        "fixed-global local-link counter",
        "all-30-bit payload-faithful close",
        "rooted common-fork lineage",
        "immediate site-tethered close-gated record law",
        "migrating/invariant-fact record law",
        "redundancy-threshold protected formation law",
        "autonomous program/constraint genesis",
        "record count to interval/rate/proper-time normalization",
        "born-grade sampler on an autonomously formed corpus",
    )
    walls = ("w_program", "w_form", "w_event", "w_capacity", "w_metric")
    pairs = sum(f"{left} / {right}" in text for left, right in combinations(walls, 2))
    check(
        "full N1-N8 blocks formation/time no-go, minimum-content and axiom-pressure claims",
        all(sections)
        and all(route in text for route in routes)
        and pairs == 10
        and "fail / do not ship" in text
        and "no axiom edit is indicated" in text,
        {"sections": sections, "routes": len(routes), "pairs": pairs},
    )


def ledger_lane_and_source_controls() -> None:
    text = normalized(NOTE)
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    scores = ("76/42/99", "51/33/87", "77/38/98", "43/17/71", "40/16/93")
    sources = (
        "cycle 58",
        "cycles 170/255",
        "cycle 259",
        "cycle 326",
        "cycle 342",
        "cycle 354",
        "cycle 356",
        "cycle 358",
    )
    check(
        "the synthesis updates every TOE lane/wall and exact prior-cycle residual match",
        all(item in text for item in walls + scores + sources)
        and "planning estimates" in text
        and "not audit verdicts" in text
        and "transfer no zero beyond their code spaces" in text,
        {"walls": walls, "scores": scores, "sources": sources},
    )


def supplied_structure_controls() -> None:
    text = normalized(NOTE)
    required = (
        "repeated 78-m2 l-specific physical program",
        "common-fork geometry",
        "one direction-selector m2 per cell",
        "program genesis and integrity",
        "count comparison, interval normalization",
        "every numerical born grade/sampler/frequency law",
        "no reversible close bit",
    )
    check(
        "the complete supplied-structure inventory is explicit",
        all(item in text for item in required),
        required,
    )


def next_campaign_controls() -> None:
    text = normalized(NOTE)
    required = (
        "exact candidate record-formation-law tournament",
        "immediate site-tethered faithful-close formation",
        "migrating/invariant-fact identity-preserving formation",
        "redundancy-threshold protected formation",
        "exact domain, state, atomic law, continuation",
        "inputs on which their formation predictions differ",
        "selects no axiom",
    )
    check(
        "the next campaign changes level from supplied mechanics to competing falsifiable formation laws",
        all(item in text for item in required),
        required,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("=" * 79)
    print("CYCLE 363: PHYSICAL RECORD CLOSE / PROVENANCE / COUNT SYNTHESIS")
    print("authority=none; audit=unset")
    print("bounded physical compilers only; formation and metric time remain open")
    print("=" * 79)
    note_contract()
    outputs = cold_route_certificates()
    exact_metric_controls(outputs)
    constructive_ladder_controls(outputs)
    semantic_firewall_controls(outputs)
    no_go_discipline_controls()
    ledger_lane_and_source_controls()
    supplied_structure_controls()
    next_campaign_controls()
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_RECORD_CLOSE_PROVENANCE_COUNT_COMPILATION_SYNTHESIS_OPEN")
        return 1
    print("RESULT PHYSICAL_RECORD_CLOSE_PROVENANCE_COUNT_COMPILATION_SYNTHESIS_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
