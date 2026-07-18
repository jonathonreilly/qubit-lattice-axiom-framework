#!/usr/bin/env python3
"""Cycle 367 synthesis for three exact bounded Record-formation laws."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_FORMATION_LAW_TOURNAMENT_"
    "SYNTHESIS_CYCLE367_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "site_tethered",
        ROOT / "scripts/physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18.py",
        "RESULT PHYSICAL_SITE_TETHERED_RECORD_FORMATION_CANDIDATE_BOUNDED_POSITIVE",
        "PASS 8\nFAIL 0",
    ),
    (
        "migrating",
        ROOT / "scripts/physical_migrating_invariant_fact_record_formation_candidate_cycle365_2026_07_18.py",
        "RESULT PHYSICAL_MIGRATING_INVARIANT_FACT_RECORD_FORMATION_CANDIDATE_BOUNDED_POSITIVE",
        "PASS 7\nFAIL 0",
    ),
    (
        "threshold",
        ROOT / "scripts/physical_redundancy_threshold_record_formation_candidate_cycle366_2026_07_18.py",
        "RESULT FIXED_CONNECTED_NN_BOOLEAN_REDUNDANCY_THRESHOLD_RECORD_FORMATION_CANDIDATE_BOUNDED_POSITIVE",
        "PASS 11\nFAIL 0",
    ),
    (
        "counter_adapter",
        ROOT / "scripts/physical_record_formation_link_genesis_counter_adapter_cycle368_2026_07_18.py",
        "RESULT PHYSICAL_RECORD_FORMATION_LINK_GENESIS_COUNTER_ADAPTER_BOUNDED_POSITIVE",
        "PASS 5\nFAIL 0",
    ),
    (
        "born_adapter",
        ROOT / "scripts/physical_site_tethered_record_born_corpus_adapter_cycle369_2026_07_18.py",
        "RESULT PHYSICAL_SITE_TETHERED_RECORD_BORN_CORPUS_ADAPTER_BOUNDED_POSITIVE",
        "PASS 7\nFAIL 0",
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
        check("the Cycle-367 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "immediate site-tethered formation",
        "migrating invariant-fact formation",
        "threshold-three convergence formation",
        "multiple exact, local, covariant, falsifiable record-formation laws",
        "none is selected by the framework",
        "three-dimensional lattice remains spatial input",
        "there is no shared substrate obstruction and no axiom pressure",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins three candidate laws without selection, no-go, time, or constitutional promotion",
        not missing,
        missing,
    )


def cold_certificates() -> dict[str, str]:
    outputs: dict[str, str] = {}

    def execute(route: tuple[str, Path, str, str]):
        name, path, result_line, pass_line = route
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        return name, result_line, pass_line, completed

    with ThreadPoolExecutor(max_workers=len(ROUTES)) as pool:
        results = tuple(pool.map(execute, ROUTES))
    rows = []
    for name, result_line, pass_line, completed in results:
        output = completed.stdout + completed.stderr
        outputs[name] = output
        rows.append(
            {
                "route": name,
                "exit": completed.returncode,
                "result": result_line in output,
                "pass": pass_line in output,
                "lines": len(output.splitlines()),
            }
        )
    check(
        "all three formation laws and both immediate-law cross-lane adapters cold-execute green",
        all(row["exit"] == 0 and row["result"] and row["pass"] for row in rows),
        rows,
    )
    return outputs


def exact_route_controls(outputs: dict[str, str]) -> None:
    required = {
        "site_tethered": (
            "'declared_domain_states': 64",
            "'formed_states': 1",
            "'L_by_N_by_frame_by_translation_cases': 288",
            "'payload_corruption_rejections': 30",
            "'lawful_domain_rejections': 15",
            "'physical_gate_compiler': None",
        ),
        "migrating": (
            "'declared_gate_states': 32",
            "'M2_sites': 440",
            "'M2_sites': 920",
            "'M2_sites': 1400",
            "'L_by_N_by_proper_cubic_frame_cases': 144",
            "'maximum_recoding_support_M2': 120",
            "'maximum_recoding_support_L1_diameter': 41",
            "'transported_value_valued_root_or_event_key': False",
            "'physical_gate_compiler': None",
        ),
        "threshold": (
            "'M2_sites': 3180",
            "'M2_sites': 6360",
            "'M2_sites': 9540",
            "'M2_per_convergence_event': 530",
            "'fixed_layers': 269",
            "'all_payload_bit_by_replica_corruption_cases': 90",
            "'logical_Records_before_commit': 0",
            "'logical_Records_after_commit': 1",
            "'commit_admitted_by_existing_framework_law': None",
            "'allowed_physical_M2_gate_compiler_claim': False",
        ),
    }
    missing = {
        name: tuple(item for item in needles if item not in outputs[name])
        for name, needles in required.items()
    }
    check(
        "exact domain, resource, covariance, identity and commit boundaries are parsed",
        all(not values for values in missing.values()),
        missing,
    )


def discriminator_controls(outputs: dict[str, str]) -> None:
    check(
        "the executable controls distinguish one-confirmation, migration/reuse, and threshold-three laws",
        "'immediate_candidate_predicts_formation': True" in outputs["site_tethered"]
        and "'redundancy_threshold_2_predicts_formation': False" in outputs["site_tethered"]
        and "'cleared_old_carrier_reused': True" in outputs["migrating"]
        and "'equal_content_quotient_records_after_reuse': 2" in outputs["migrating"]
        and "'Cycle364_formed': True" in outputs["threshold"]
        and "'Cycle366_formed': False" in outputs["threshold"]
        and "'three_carriers_are_one_Record_quotient': False" in outputs["threshold"],
        "candidate laws disagree on declared physical controls",
    )


def adapter_controls(outputs: dict[str, str]) -> None:
    counter = outputs["counter_adapter"]
    born = outputs["born_adapter"]
    check(
        "the immediate law has exact count and grade-blind-corpus common-state adapters without semantic promotion",
        "'L_by_N_by_frame_cases': 144" in counter
        and "'encoder_decoder_roundtrip_failures': 0" in counter
        and "'count_intertwiner_failures': 0" in counter
        and "'physical_formation_and_link_genesis_gate_compiler': None" in counter
        and "'count_is_time': False" in counter
        and "'L_by_size_by_frame_atom_cases': 1008" in born
        and "'D_E_roundtrip_failures': 0" in born
        and "'observable_or_weight_intertwiner_failures': 0" in born
        and "'actual_history_sampler': None" in born
        and "'Born_law_derived': False" in born,
        "conditional compatibility does not select Cycle 364",
    )


def completeness_contract_controls() -> None:
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
    )
    check(
        "all ten canonical law-completeness fields are audited route by route",
        all(f"| {field} |" in text for field in fields)
        and "three exact candidate laws; none selected" in text
        and "no unique global extension or sampled history" in text
        and "no selected normalized contextual law or frequency theorem" in text,
        fields,
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    routes = (
        "immediate site-tethered law",
        "migrating connected-worldline law",
        "threshold-three convergence law",
        "reversible dilation or environment-export realization",
        "stochastic kernel or global-history constraint",
        "renewable/full-lattice formation and capacity law",
        "actual-history sampler and contextual frequency theorem",
    )
    walls = ("w_select", "w_commit", "w_genesis", "w_capacity", "w_actual", "w_stats")
    pairs = sum(f"{left} / {right}" in text for left, right in combinations(walls, 2))
    check(
        "full N1-N8 blocks formation no-go, necessary-threshold, minimum-content and axiom-pressure claims",
        all(sections)
        and all(route in text for route in routes)
        and pairs == 15
        and "fail / do not ship a formation no-go" in text
        and "no axiom edit is indicated" in text,
        {"sections": sections, "routes": len(routes), "pairs": pairs},
    )


def ledger_lane_and_prior_controls() -> None:
    text = normalized(NOTE)
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    scores = ("79/42/99", "52/33/89", "77/38/98", "43/17/71", "42/16/95")
    priors = ("cycle 326", "cycle 342", "cycles 361/362", "cycle 351", "cycle 360", "cycle 335")
    check(
        "every TOE wall/lane and exact prior residual is updated without an audit verdict",
        all(item in text for item in walls + scores + priors)
        and "planning estimates" in text
        and "not audit verdicts" in text
        and "strict record, time and born floors do not move" in text,
        {"walls": walls, "scores": scores, "priors": priors},
    )


def semantic_firewall_controls(outputs: dict[str, str]) -> None:
    joined = "\n".join(outputs.values())
    needles = (
        "'selected_framework_law': False",
        "'actual_history_sampler': None",
        "'metric_time': None",
        "'physical_gate_compiler': None",
        "'allowed_physical_M2_gate_compiler_claim': False",
        "'count_is_time': False",
        "'Born_law_derived': False",
        "'authority': 'none'",
        "'audit': 'unset'",
    )
    missing = tuple(item for item in needles if item not in joined)
    check(
        "Records, commits, counts, proposals, time and physical admission remain correctly typed",
        not missing,
        missing,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 367: PHYSICAL RECORD-FORMATION LAW TOURNAMENT SYNTHESIS")
    print("authority=none; audit=unset; no candidate law selected")
    note_contract()
    outputs = cold_certificates()
    if outputs:
        exact_route_controls(outputs)
        discriminator_controls(outputs)
        adapter_controls(outputs)
        semantic_firewall_controls(outputs)
    completeness_contract_controls()
    no_go_discipline_controls()
    ledger_lane_and_prior_controls()
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_RECORD_FORMATION_LAW_TOURNAMENT_SYNTHESIS_OPEN")
        return 1
    print("RESULT PHYSICAL_RECORD_FORMATION_LAW_TOURNAMENT_SYNTHESIS_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
