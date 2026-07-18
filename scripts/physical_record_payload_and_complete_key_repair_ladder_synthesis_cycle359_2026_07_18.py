#!/usr/bin/env python3
"""Cycle 359 synthesis for payload continuation and Record-key repairs."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_PAYLOAD_AND_COMPLETE_KEY_REPAIR_LADDER_"
    "SYNTHESIS_CYCLE359_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "payload",
        ROOT / "scripts/physical_autonomous_record_payload_continuation_nn_route_cycle356_2026_07_18.py",
        "RESULT PHYSICAL_AUTONOMOUS_RECORD_PAYLOAD_CONTINUATION_NN_ROUTE_BOUNDED_POSITIVE",
        "PASS 6\nFAIL 0",
    ),
    (
        "endpoint",
        ROOT / "scripts/physical_autonomous_record_endpoint_keyed_rendezvous_nn_route_cycle357_2026_07_18.py",
        "'route': 'local-gauge-auxiliary-endpoint-key'",
        "SUMMARY {'pass': 11, 'fail': 0",
    ),
    (
        "complete_key",
        ROOT / "scripts/physical_autonomous_full_record_keyed_rendezvous_nn_route_cycle358_2026_07_18.py",
        "'route': 'local-gauge-auxiliary-complete-Record-key'",
        "SUMMARY {'pass': 11, 'fail': 0",
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
        check("the Cycle-359 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "blank-future payload continuation",
        "complete-record keyed matcher",
        "generated candidate word",
        "is not thereby an actual framework record",
        "complete record-word equality is also not independent event identity",
        "three-dimensional spatial input",
        "there is no shared obstruction and no axiom pressure",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the repair theorem and Record/content/event/time firewalls",
        not missing,
        missing,
    )


def cold_route_certificates() -> dict[str, str]:
    outputs: dict[str, str] = {}

    def execute(route: tuple[str, Path, str, str]):
        name, path, result_line, summary_line = route
        completed = subprocess.run(
            [sys.executable, str(path)], cwd=ROOT, check=False,
            capture_output=True, text=True,
        )
        return name, result_line, summary_line, completed

    with ThreadPoolExecutor(max_workers=3) as pool:
        results = tuple(pool.map(execute, ROUTES))
    rows = []
    for name, result_line, summary_line, completed in results:
        output = completed.stdout + completed.stderr
        outputs[name] = output
        rows.append({
            "route": name,
            "exit": completed.returncode,
            "result": result_line in output,
            "summary": summary_line in output,
            "lines": len(output.splitlines()),
        })
    check(
        "all three repair runners cold-execute to exact green certificates",
        all(row["exit"] == 0 and row["result"] and row["summary"] for row in rows),
        rows,
    )
    return outputs


def exact_metric_controls(outputs: dict[str, str]) -> None:
    required = {
        "payload": (
            "'initial_supplied_Record_words': 1",
            "'initial_blank_future_Record_words': 17",
            "'continued_future_word_candidates': 17",
            "'future_payload_mismatches': 0",
            "'program_bits_per_macrocell': 78",
            "'fixed_layers_per_step': 113083",
            "'primitive_gates_per_step': 2035418",
            "'gate_frame_cases': 97698240",
            "'dirty_scratch_is_local_code_failure_not_host_rejection': True",
            "'continuation_word_is_actual_Record_formation': False",
        ),
        "endpoint": (
            "'M2_per_longitudinal_cell': 144",
            "'endpoint_key_alphabet_size': 3",
            "'same_endpoint_misses': 0",
            "'distinct_endpoint_false_positives': 0",
            "'same_endpoint_distinct_Record_agreements': 6",
            "'L_by_N_by_frame_cases': 144",
        ),
        "complete_key": (
            "'packet_width_M2': 31",
            "'M2_per_longitudinal_cell': 248",
            "'layers': 81",
            "'gates': 23184",
            "'identical_Record_misses': 0",
            "'different_Record_false_positives': 0",
            "'carried_Record_bits': 30",
            "'independent_event_identity': False",
        ),
    }
    missing = {
        name: tuple(item for item in needles if item not in outputs[name])
        for name, needles in required.items()
    }
    check(
        "exact widths, resources, covariance, aliases and semantic residuals are parsed",
        all(not values for values in missing.values()),
        missing,
    )


def repair_ladder_controls(outputs: dict[str, str]) -> None:
    check(
        "the ladder independently repairs future payload, endpoint key and complete content matching",
        "'future_payload_generated_from_predecessor': True" in outputs["payload"]
        and "'derived_local_endpoint_key_agreement': True" in outputs["endpoint"]
        and "'derived_complete_Record_word_agreement': True" in outputs["complete_key"]
        and "'shared_pair_selected_key_rail': False" in outputs["complete_key"],
        "positive repair arrows",
    )


def semantic_firewall_controls(outputs: dict[str, str]) -> None:
    joined = "\n".join(outputs.values())
    needles = (
        "'strict_Record_formation_closure': False",
        "'Record_occurrence_generated': False",
        "'K_form': None",
        "'complete_Record_equality_derived': False",
        "'independent_event_identity_derived': False",
        "'independent_event_identity': False",
        "'state_dependent_host_schedule': False",
        "'authority': 'none'",
        "'audit': 'unset'",
    )
    missing = tuple(item for item in needles if item not in joined)
    check(
        "candidate words and content equality are not promoted to occurrence, event identity or time",
        not missing,
        missing,
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    routes = (
        "blank-future payload continuation",
        "three-rail endpoint-key rendezvous",
        "complete 30-bit record-key rendezvous",
        "gate-faithful local close certificate",
        "actual append-only record formation from a close candidate",
        "independent event provenance from rooted lineage rather than copied ids",
        "fixed global autonomous link counter",
        "record-depth plus physical clock comparison/normalization",
    )
    walls = ("w_program", "w_close", "w_form", "w_event", "w_count", "w_metric")
    pairs = sum(f"{left} / {right}" in text for left, right in combinations(walls, 2))
    check(
        "full N1-N8 blocks actualization/time no-go, shared obstruction, minimum-content and axiom-pressure claims",
        all(sections)
        and all(route in text for route in routes)
        and pairs == 15
        and "fail / do not ship" in text
        and "no axiom edit is indicated" in text,
        {"sections": sections, "routes": len(routes), "pairs": pairs},
    )


def ledger_lane_and_source_controls() -> None:
    text = normalized(NOTE)
    walls = ("c_ref", "c_num", "c_wrap", "c_int", "c_local", "c_source")
    scores = ("74/38/99", "46/27/82", "77/38/98", "43/17/71", "40/16/93")
    sources = (
        "cycle 58 binary macrocode",
        "cycle 170 causal-depth clock",
        "cycle 255 car/record bridge",
        "cycle 342 cylinder route",
        "cycle 347 named clock synthesis",
        "cycle 355 tournament",
    )
    check(
        "the synthesis updates all TOE lanes, walls and exact prior-cycle residual matches",
        all(item in text for item in walls + scores + sources)
        and "planning estimates" in text
        and "not audit verdicts" in text
        and "no residual is transferred beyond its exact type" in text,
        {"walls": walls, "scores": scores, "sources": sources},
    )


def supplied_structure_controls() -> None:
    text = normalized(NOTE)
    required = (
        "repeated 78-m2 l-specific",
        "one local formation-enable input per macrocell",
        "each matcher root's independent packet encoder",
        "gate-faithful physical close certificate",
        "one fixed global autonomous link-counter rule",
        "every born grade/sampler/frequency law",
        "no reversible packet, candidate word, comparison latch",
    )
    check(
        "the complete supplied-structure inventory is explicit",
        all(item in text for item in required),
        required,
    )


def next_campaign_controls() -> None:
    text = normalized(NOTE)
    required = (
        "deleting the underlying update cannot leave the same close transcript",
        "one fixed global connected-nn layer list",
        "generate independent occurrence provenance",
        "attempt an append-only record-formation law",
    )
    check(
        "the next campaign attacks faithful close, autonomous count, provenance and formation in order",
        all(item in text for item in required),
        required,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    outputs = cold_route_certificates()
    exact_metric_controls(outputs)
    repair_ladder_controls(outputs)
    semantic_firewall_controls(outputs)
    no_go_discipline_controls()
    ledger_lane_and_source_controls()
    supplied_structure_controls()
    next_campaign_controls()
    print("SUMMARY", {"pass": PASS, "fail": FAIL, "authority": "none", "audit": "unset"})
    print(
        "RESULT",
        "PHYSICAL_RECORD_PAYLOAD_COMPLETE_KEY_REPAIR_LADDER_BOUNDED_POSITIVE"
        if FAIL == 0 else "PHYSICAL_RECORD_PAYLOAD_COMPLETE_KEY_REPAIR_LADDER_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
