#!/usr/bin/env python3
"""Cycle 380: synthesis of Record cross-lane and contact compatibility.

This runner cold-executes the exact immediate, migrating, and threshold
counter/Born adapters plus the finite resource and contact-side bridges built
after Cycle 367.  It checks the route matrix, supplied-law inventory, semantic
firewalls, and the synthesis note's full N1--N8 gate.  Multiple positive
candidate laws remain underdetermination, not a selected law, a no-go, or
axiom pressure.  Authority is none and audit is unset.
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
    "PHYSICAL_RECORD_CROSS_LANE_COMPATIBILITY_AND_CONTACT_"
    "SYNTHESIS_CYCLE380_NOTE_2026-07-18.md"
)
ROUTES = (
    (
        "immediate_counter",
        "physical_record_formation_link_genesis_counter_adapter_cycle368_2026_07_18.py",
        "PASS 5\nFAIL 0",
        "RESULT PHYSICAL_RECORD_FORMATION_LINK_GENESIS_COUNTER_ADAPTER_BOUNDED_POSITIVE",
    ),
    (
        "immediate_born",
        "physical_site_tethered_record_born_corpus_adapter_cycle369_2026_07_18.py",
        "PASS 7\nFAIL 0",
        "RESULT PHYSICAL_SITE_TETHERED_RECORD_BORN_CORPUS_ADAPTER_BOUNDED_POSITIVE",
    ),
    (
        "immediate_resource",
        "physical_record_protected_capacity_export_adapter_cycle370_2026_07_18.py",
        "PASS 7\nFAIL 0",
        "RESULT PHYSICAL_RECORD_PROTECTED_CAPACITY_EXPORT_ADAPTER_BOUNDED_POSITIVE",
    ),
    (
        "threshold_born",
        "physical_threshold_convergence_record_born_corpus_adapter_cycle371_2026_07_18.py",
        "PASS 7\nFAIL 0",
        "RESULT PHYSICAL_THRESHOLD_CONVERGENCE_RECORD_BORN_CORPUS_ADAPTER_BOUNDED_POSITIVE",
    ),
    (
        "migrating_counter",
        "physical_migrating_record_counter_common_state_adapter_cycle372_2026_07_18.py",
        "PASS 7\nFAIL 0",
        "RESULT PHYSICAL_MIGRATING_RECORD_COUNTER_COMMON_STATE_ADAPTER_BOUNDED_POSITIVE",
    ),
    (
        "contact_transcript",
        "physical_contact_sensitive_operational_transcript_registration_cycle374_2026_07_18.py",
        "SUMMARY {'pass': 8, 'fail': 0}",
        "RESULT PHYSICAL_CONTACT_SENSITIVE_OPERATIONAL_TRANSCRIPT_BOUNDED_POSITIVE",
    ),
    (
        "threshold_counter",
        "physical_threshold_convergence_record_counter_adapter_cycle375_2026_07_18.py",
        "PASS 6\nFAIL 0",
        "RESULT PHYSICAL_THRESHOLD_CONVERGENCE_RECORD_COUNTER_ADAPTER_BOUNDED_POSITIVE",
    ),
    (
        "migrating_born",
        "physical_migrating_record_born_corpus_adapter_cycle376_2026_07_18.py",
        "PASS 6\nFAIL 0",
        "RESULT PHYSICAL_MIGRATING_RECORD_BORN_CORPUS_ADAPTER_BOUNDED_POSITIVE",
    ),
    (
        "immediate_contact",
        "physical_cycle281_close_to_cycle364_formation_adapter_cycle378_2026_07_18.py",
        "SUMMARY {'pass': 6, 'fail': 0}",
        "RESULT PHYSICAL_CYCLE281_CLOSE_TO_CYCLE364_FORMATION_ADAPTER_BOUNDED_POSITIVE",
    ),
    (
        "threshold_contact",
        "physical_contact_distinct_root_threshold_bridge_cycle379_2026_07_18.py",
        "PASS 8\nFAIL 0",
        "RESULT PHYSICAL_CONTACT_DISTINCT_ROOT_THRESHOLD_BRIDGE_BOUNDED_POSITIVE",
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
        check("the Cycle-380 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "all three candidate identities have exact counter and born-corpus adapters",
        "none is selected",
        "existing cycle-366 interface does not enforce confirmation-root independence",
        "nine m2 counts marker storage only",
        "three-dimensional lattice remains spatial input",
        "counts remain dimensionless",
        "open prs #5472, #5476, and #5479",
        "unlanded comparators only",
        "no shared substrate obstruction",
        "no axiom pressure",
        "no thirring engine is used or compared",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins route symmetry, contact/root correction, Born comparator boundary, and semantic status",
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
                "result": result_line in output,
                "lines": len(output.splitlines()),
            }
        )
    check(
        "all ten post-Cycle-367 cross-lane and contact routes cold-execute green",
        all(row["exit"] == 0 and row["pass"] and row["result"] for row in rows),
        rows,
    )
    return outputs


def symmetric_counter_born_controls(outputs: dict[str, str]) -> None:
    required = {
        "immediate_counter": (
            "'L_by_N_by_frame_cases': 144",
            "'count_intertwiner_failures': 0",
            "'physical_formation_and_link_genesis_gate_compiler': None",
        ),
        "immediate_born": (
            "'L_by_size_by_frame_atom_cases': 1008",
            "'observable_or_weight_intertwiner_failures': 0",
            "'actual_history_sampler': None",
        ),
        "migrating_counter": (
            "'migration_common_projection_failures': 0",
            "'physical_count_before_reuse': 6",
            "'physical_count_after_reuse': 7",
        ),
        "migrating_born": (
            "'L_by_N_by_frame_atom_cases': 1728",
            "'history_double_count_failures': 0",
            "'corpus_atoms_before_after': (6, 7)",
        ),
        "threshold_counter": (
            "'dimensionless_member_count': 0",
            "'dimensionless_member_count': 1",
            "'count_intertwiner_failures': 0",
            "'CONSUME_admission_by_existing_framework_law': None",
        ),
        "threshold_born": (
            "'three_precommit_carriers_are_three_trials': False",
            "'D_E_roundtrip_failures': 0",
            "'Born_law_derived': False",
        ),
    }
    missing = {
        name: tuple(item for item in needles if item not in outputs[name])
        for name, needles in required.items()
    }
    check(
        "all three candidate identities reach both counter and grade-blind corpus without double-counting carriers or history",
        all(not values for values in missing.values()),
        missing,
    )


def resource_contact_controls(outputs: dict[str, str]) -> None:
    resource = outputs["immediate_resource"]
    transcript = outputs["contact_transcript"]
    immediate = outputs["immediate_contact"]
    threshold = outputs["threshold_contact"]
    check(
        "the finite resource and contact bridges retain their exact physical and semantic boundaries",
        "'primitive_gate_boundaries_audited': 6268176" in resource
        and "'source_lane_trace_failures': 0" in resource
        and "'held_patch_M2': 3555" in resource
        and "'indefinite_autonomous_renewal': None" in resource
        and "'held_contact_contrast': -0.04997851262459463" in transcript
        and "'held_legacy_joint_survival_contact_contrast': 0.0" in transcript
        and "'formation': 'supplied/open'" in transcript
        and "'conditional_formations': 114" in immediate
        and "'delete_first_formations': 0" in immediate
        and "'actual_member_selector': None" in immediate
        and "'Cycle366_direct_bypass_with_three_identical_replicas_formed': 1" in threshold
        and "'one_root_fanned_to_three_carriers_formed': 0" in threshold
        and "'root_marker_storage_M2': 9" in threshold
        and "'reference_constraint_complete_support_M2': None" in threshold
        and "'CONSUME_admission_by_existing_framework_law': None" in threshold,
        "resource renewal, coherent actuality, root independence and commit admission stay open",
    )


def law_completeness_and_ledger_controls() -> None:
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
    check(
        "the expanded law-completeness contract and six-wall ledger remain explicit",
        all(f"| {field} |" in text for field in fields)
        and all(f"| {wall} |" in text for wall in walls)
        and "actuality | open" in text
        and "statistics | open" in text
        and "source/response | open" in text,
        {"fields": fields, "walls": walls},
    )


def no_go_discipline_controls() -> None:
    text = normalized(NOTE)
    sections = tuple(f"n{index} —" in text for index in range(1, 9))
    routes = (
        "immediate site-tethered formation",
        "migrating connected-worldline formation",
        "threshold-three convergence formation",
        "symmetric counter adapters",
        "symmetric born-corpus adapters",
        "finite protected-capacity continuation",
        "contact-close to immediate formation",
        "distinct-root contact to threshold formation",
        "migrating contact bridge",
        "physical born menu-grade/functionality bridge",
        "actual-history sampler and frequency theorem",
        "source-response and gravity bridge",
    )
    walls = (
        "w_select",
        "w_commit",
        "w_genesis",
        "w_actual",
        "w_stats",
        "w_renew",
        "w_source",
    )
    pair_count = sum(
        f"{left} / {right}" in text for left, right in combinations(walls, 2)
    )
    check(
        "full N1-N8 blocks selected-law, minimum-content, shared-obstruction and axiom-pressure promotion",
        all(sections)
        and all(route in text for route in routes)
        and pair_count == 21
        and "fail / do not ship a selected formation law" in text
        and "no axiom edit is indicated" in text,
        {"sections": sections, "routes": len(routes), "wall_pairs": pair_count},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 380: RECORD CROSS-LANE COMPATIBILITY / CONTACT SYNTHESIS")
    print("authority=none; audit=unset; no selected law or axiom pressure")
    note_contract()
    outputs = cold_certificates()
    symmetric_counter_born_controls(outputs)
    resource_contact_controls(outputs)
    law_completeness_and_ledger_controls()
    no_go_discipline_controls()
    check(
        "Cycle 380 retains positive cross-lane compatibility as underdetermination while routing the next Born-menu and actuality tests",
        FAIL == 0,
        {
            "candidate_law_selected": None,
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
        print("RESULT PHYSICAL_RECORD_CROSS_LANE_COMPATIBILITY_CONTACT_SYNTHESIS_OPEN")
        return 1
    print("RESULT PHYSICAL_RECORD_CROSS_LANE_COMPATIBILITY_CONTACT_SYNTHESIS_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
