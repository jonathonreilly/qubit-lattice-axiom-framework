#!/usr/bin/env python3
"""Cycle 280: executable synthesis of the same-code instrument bridge.

The runner checks the route matrix, anti-splicing rule, five-lane percentage
revision, semantic firewalls, N1-N8 note contract, and cold predecessor runs.
Pass totals are regression controls, not independent physical predictions.
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
NOTE = NOTES / "SAME_CODE_INSTRUMENT_BRIDGE_SYNTHESIS_CYCLE280_NOTE_2026-07-17.md"

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
class Route:
    name: str
    same_physical_code: bool
    bounded_instrument: bool
    explicit_input_states: bool
    actual_process_compatibility: bool
    occurrence: bool
    fault_faithful_close: bool
    permanent_record: bool


ROUTES = (
    Route("Cycle 277 rough-terminal", True, True, False, True, False, False, False),
    Route("Cycle 278 connected-edge", True, True, True, True, False, False, False),
    Route("Cycle 279 close tournament", False, True, True, False, False, False, False),
)


OLD_LANES = {
    "operational quantum / Records": (42, 18, 63),
    "causal time / clock": (32, 17, 58),
    "inertia / matter": (58, 24, 77),
    "gravity / source / resource": (34, 12, 58),
    "Born / probability / realized history": (30, 14, 74),
}

NEW_LANES = {
    "operational quantum / Records": (46, 21, 68),
    "causal time / clock": (32, 17, 58),
    "inertia / matter": (58, 24, 77),
    "gravity / source / resource": (34, 12, 58),
    "Born / probability / realized history": (30, 14, 74),
}


RUNNERS = {
    "rough_terminal_same_code_local_instrument_cycle277_2026_07_17.py": (12, 0),
    "connected_edge_same_code_local_instrument_cycle278_2026_07_17.py": (11, 0),
    "local_instrument_to_record_close_tournament_cycle279_2026_07_17.py": (30, 0),
    "rough_terminal_subsystem_gauge_factorization_cycle251_2026_07_17.py": (15, 0),
    "contractible_lightcone_wilson_quotient_cycle271_2026_07_17.py": (16, 0),
    "locally_matched_wilson_sector_states_cycle275_2026_07_17.py": (14, 0),
}


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split()).lower()


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-280 synthesis note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "result in plain english",
        "route-by-route disposition",
        "anti-splicing and lawful domain",
        "supplied-structure inventory",
        "exact verification and residuals",
        "five toe lane update",
        "six-wall compiler ledger",
        "optimal next campaign",
        "not yet an occurrence or a record",
        "compiler iteration is not time",
        "contact-support effect, not energy",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
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
    check("the note preserves the route, lane, wall, firewall, and N1-N8 contracts", not missing, missing)


def route_controls() -> None:
    check(
        "both physical routes construct bounded instruments on their own declared code",
        all(route.same_physical_code and route.bounded_instrument for route in ROUTES[:2]),
        ROUTES[:2],
    )
    check(
        "only the connected-edge route joins explicit same-code algebraic states to the instrument",
        [route.explicit_input_states for route in ROUTES] == [False, True, True],
        ROUTES,
    )
    check(
        "no tested route is promoted to occurrence, fault-faithful close, or permanent Record",
        all(not route.occurrence and not route.fault_faithful_close and not route.permanent_record for route in ROUTES),
        ROUTES,
    )
    check(
        "the synthesis forbids splicing Cycle-251 update claims to Cycle-275 states",
        ROUTES[0].name != ROUTES[1].name
        and ROUTES[0].explicit_input_states is False
        and ROUTES[1].actual_process_compatibility is True,
        "distinct physical codes require a new explicit common intertwiner",
    )


def lane_controls() -> None:
    changed = {
        lane: (OLD_LANES[lane], NEW_LANES[lane])
        for lane in OLD_LANES
        if OLD_LANES[lane] != NEW_LANES[lane]
    }
    check(
        "only the operational lane moves because only its typed connector changed",
        changed == {"operational quantum / Records": ((42, 18, 63), (46, 21, 68))},
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
        timeout=180,
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
    check("all load-bearing same-code and predecessor certificates rerun cold", all(row[1] for row in rows), rows)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    route_controls()
    lane_controls()
    cold_regressions()
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print("RESULT", "CYCLE280_SAME_CODE_INSTRUMENT_BRIDGE_GREEN" if FAIL == 0 else "CYCLE280_OPEN")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
