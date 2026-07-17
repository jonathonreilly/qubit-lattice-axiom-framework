#!/usr/bin/env python3
"""Cycle 288: executable whole-campaign bridge synthesis.

Checks the compiler and post-compiler route matrices, anti-splicing rules,
five-lane maturity changes, six-wall and N1-N8 note contracts, and cold-runs
the seven constructive follow-up certificates. Pass totals are regression
controls, not independent physical predictions.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "docs/work_history/repo/review_feedback"
SCRIPTS = ROOT / "scripts"
NOTE = NOTES / "PHYSICAL_INSTRUMENT_RECORD_HISTORY_BRIDGE_SYNTHESIS_CYCLE288_NOTE_2026-07-17.md"

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


@dataclass(frozen=True)
class CompilerRoute:
    name: str
    bounded_state_encoder: bool
    bounded_actual_update: bool
    full_fock_encoder: bool
    sectorwise_full_actual_update: bool
    exact_full_fock_shuttle_cases: bool
    actual_update_support_grows_with_size: bool


COMPILER_ROUTES = (
    CompilerRoute("Cycle 248 direct", True, False, True, False, False, True),
    CompilerRoute("Cycle 251 gauge", False, True, False, True, False, False),
    CompilerRoute("Cycle 260 staggered", False, False, False, False, True, True),
)


@dataclass(frozen=True)
class BridgeRoute:
    cycle: int
    same_connected_code: bool
    actual_wg_sensitive: bool
    single_q_call_deletion_sensitive: bool
    joint_q_pair_deletion_faithful: bool
    controlled_wg_deletion_sensitive: bool
    arbitrary_split_replacement_faithful: bool
    autonomous_episode: bool
    finite_nonreturn: bool
    finite_process_decoder: bool
    physical_occurrence: bool
    record: bool
    clock: bool


BRIDGE_ROUTES = (
    BridgeRoute(281, True, False, True, True, False, False, False, False, False, False, False, False),
    BridgeRoute(282, True, False, True, False, False, False, True, False, False, False, False, False),
    BridgeRoute(283, True, False, False, False, False, False, False, False, False, False, False, False),
    BridgeRoute(284, True, False, False, False, False, False, False, False, True, False, False, False),
    BridgeRoute(285, True, True, False, False, True, False, False, False, False, False, False, False),
    BridgeRoute(286, True, False, True, True, False, False, True, True, False, False, False, False),
    BridgeRoute(287, True, False, True, False, False, False, True, False, False, False, False, False),
)


OLD_LANES = {
    "operational quantum / Records": (46, 21, 68),
    "causal time / clock": (32, 17, 58),
    "inertia / matter": (58, 24, 77),
    "gravity / source / resource": (34, 12, 58),
    "Born / probability / realized history": (30, 14, 74),
}


NEW_LANES = {
    "operational quantum / Records": (50, 23, 74),
    "causal time / clock": (33, 17, 60),
    "inertia / matter": (59, 25, 79),
    "gravity / source / resource": (34, 12, 58),
    "Born / probability / realized history": (33, 14, 79),
}


RUNNERS = {
    "parity_doubling_spectator_compiler_cycle248_2026_07_17.py": (17, 0),
    "rough_terminal_subsystem_gauge_factorization_cycle251_2026_07_17.py": (15, 0),
    "genuine_staggered_parity_shuttle_cycle260_2026_07_17.py": (15, 0),
    "locally_matched_wilson_sector_states_cycle275_2026_07_17.py": (14, 0),
    "matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17.py": (14, 0),
    "connected_edge_autonomous_apparatus_law_cycle282_2026_07_17.py": (13, 0),
    "redundant_archive_permanence_history_cycle283_2026_07_17.py": (15, 0),
    "contact_archive_finite_process_history_cycle284_2026_07_17.py": (15, 0),
    "actual_contact_action_syndrome_tournament_cycle285_2026_07_17.py": (22, 0),
    "outgoing_carrier_nonrecurrence_cycle286_2026_07_17.py": (14, 0),
    "contact_close_typed_record_dag_cycle287_2026_07_17.py": (13, 0),
}


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split()).lower()


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-288 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "constitutional effect: none",
        "result in plain english",
        "final disposition of the three compiler routes",
        "post-compiler constructive route dispositions",
        "strongest actual-action result",
        "anti-splicing and lawful-domain rules",
        "exact verification and residual ledger",
        "supplied-structure inventory",
        "five toe lane percentage update after reconstructing both bridge ends",
        "cross-lane dependency ledger",
        "six-wall ledger",
        "axiom-pressure disposition",
        "optimal next campaign",
        "pointer or archive copying alone is not a record",
        "is not physical time",
        "is not an additive source ledger",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no route-independent obstruction",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the synthesis note preserves all route, lane, wall, firewall, and N1-N8 contracts", not missing, missing)


def compiler_controls() -> None:
    direct, gauge, staggered = COMPILER_ROUTES
    check(
        "the direct route alone supplies the bounded full-Fock state encoder but not the actual update",
        direct.bounded_state_encoder
        and direct.full_fock_encoder
        and direct.actual_update_support_grows_with_size
        and not direct.bounded_actual_update,
        direct,
    )
    check(
        "the priority gauge route alone supplies the bounded sectorwise actual update",
        gauge.bounded_actual_update and gauge.sectorwise_full_actual_update and not gauge.full_fock_encoder,
        gauge,
    )
    check(
        "the staggered exact construction is rejected as bounded because support grows with size",
        staggered.actual_update_support_grows_with_size
        and staggered.exact_full_fock_shuttle_cases
        and not staggered.bounded_actual_update
        and not staggered.sectorwise_full_actual_update,
        staggered,
    )
    check(
        "no compiler route is promoted to the complete requested compiler",
        not any(
            route.bounded_state_encoder
            and route.bounded_actual_update
            and route.full_fock_encoder
            for route in COMPILER_ROUTES
        ),
        COMPILER_ROUTES,
    )


def bridge_controls() -> None:
    by_cycle = {route.cycle: route for route in BRIDGE_ROUTES}
    check(
        "all follow-ups remain on their declared connected physical-code endpoint",
        all(route.same_connected_code for route in BRIDGE_ROUTES),
        tuple(by_cycle),
    )
    check(
        "only Cycle 285 claims sensitivity to application of the actual contact phase",
        [route.cycle for route in BRIDGE_ROUTES if route.actual_wg_sensitive] == [285],
        tuple(route.cycle for route in BRIDGE_ROUTES if route.actual_wg_sensitive),
    )
    check(
        "Cycles 281 and 282 detect each single Q-call deletion, but only Cycle 281 closes the tested joint pair",
        by_cycle[281].single_q_call_deletion_sensitive
        and by_cycle[281].joint_q_pair_deletion_faithful
        and by_cycle[282].single_q_call_deletion_sensitive
        and not by_cycle[282].joint_q_pair_deletion_faithful,
        (by_cycle[281], by_cycle[282]),
    )
    check(
        "Cycle 284 alone closes the finite decoder column",
        [route.cycle for route in BRIDGE_ROUTES if route.finite_process_decoder] == [284],
        BRIDGE_ROUTES,
    )
    check(
        "only Cycle 285 closes deletion of the supplied controlled-Wg Ramsey process and no route closes arbitrary split replacement",
        [route.cycle for route in BRIDGE_ROUTES if route.controlled_wg_deletion_sensitive] == [285]
        and all(not route.arbitrary_split_replacement_faithful for route in BRIDGE_ROUTES),
        BRIDGE_ROUTES,
    )
    check(
        "Cycle 286 alone supplies the tested finite outgoing nonreturn column",
        [route.cycle for route in BRIDGE_ROUTES if route.finite_nonreturn] == [286],
        BRIDGE_ROUTES,
    )
    check(
        "no route is promoted to physical occurrence, Record, or clock",
        all(not route.physical_occurrence and not route.record and not route.clock for route in BRIDGE_ROUTES),
        BRIDGE_ROUTES,
    )
    check(
        "the static capability census contains no completed row; it does not prove a common intertwiner",
        not any(
            route.actual_wg_sensitive
            and route.autonomous_episode
            and route.finite_nonreturn
            and route.finite_process_decoder
            for route in BRIDGE_ROUTES
        ),
        "source review remains required for the prose anti-splicing rules",
    )


def lane_controls() -> None:
    changed = {
        lane: (OLD_LANES[lane], NEW_LANES[lane])
        for lane in OLD_LANES
        if OLD_LANES[lane] != NEW_LANES[lane]
    }
    check(
        "gravity/source remains unchanged because no typed source connector was built",
        "gravity / source / resource" not in changed,
        changed,
    )
    check(
        "the other four lanes move only by their new typed connectors",
        set(changed) == {
            "operational quantum / Records",
            "causal time / clock",
            "inertia / matter",
            "Born / probability / realized history",
        },
        changed,
    )
    check(
        "all score axes remain ordered strict <= integrated <= conditional",
        all(strict <= integrated <= conditional for integrated, strict, conditional in NEW_LANES.values()),
        NEW_LANES,
    )


def run_certificate(name: str, expected: tuple[int, int]) -> tuple[str, bool, object]:
    path = SCRIPTS / name
    if not path.exists():
        return name, False, "missing"
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=240,
        check=False,
    )
    matches = re.findall(r"SUMMARY PASS\s+(\d+)\s+FAIL\s+(\d+)", result.stdout)
    if matches:
        observed = tuple(map(int, matches[-1]))
    else:
        mapping = re.findall(
            r"SUMMARY\s*\{'pass':\s*(\d+),\s*'fail':\s*(\d+)\}",
            result.stdout,
        )
        observed = tuple(map(int, mapping[-1])) if mapping else None
    return name, result.returncode == 0 and observed == expected, observed


def cold_regressions() -> None:
    rows = [run_certificate(name, expected) for name, expected in RUNNERS.items()]
    check("all eleven compiler and post-compiler certificates rerun cold", all(row[1] for row in rows), rows)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    compiler_controls()
    bridge_controls()
    lane_controls()
    cold_regressions()
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print("RESULT", "CYCLE288_WHOLE_BRIDGE_SYNTHESIS_GREEN" if FAIL == 0 else "CYCLE288_OPEN")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
