#!/usr/bin/env python3
"""Cycle 276: executable final synthesis of the M64-to-M2 campaign.

The runner checks the final note's scope, the three-route contract matrix,
anti-feature-splicing rules, the five-lane endpoint scores, and cold reruns of
the load-bearing predecessor certificates.  It does not treat pass counts as
independent physical predictions.
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
NOTE = NOTES / "FINAL_M64_PHYSICAL_M2_COMPILER_TOURNAMENT_SYNTHESIS_CYCLE276_NOTE_2026-07-17.md"

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


CLOSED = "closed"
PARTIAL = "partial"
FAILED = "failed"
OPEN = "open"
TARGET = "target"

CONTRACT_FIELDS = (
    "bounded_full_fock_E",
    "bounded_actual_G",
    "local_constraints",
    "no_global_order_service",
    "frames_24",
    "mass",
    "contact_seam",
    "preparation",
)


@dataclass(frozen=True)
class Route:
    name: str
    bounded_full_fock_E: str
    bounded_actual_G: str
    local_constraints: str
    no_global_order_service: str
    frames_24: str
    mass: str
    contact_seam: str
    preparation: str

    def complete(self) -> bool:
        return all(getattr(self, field) == CLOSED for field in CONTRACT_FIELDS)


ROUTES = (
    Route(
        "Cycle-230 intrinsic target",
        TARGET,
        TARGET,
        TARGET,
        CLOSED,
        CLOSED,
        CLOSED,
        CLOSED,
        TARGET,
    ),
    Route(
        "direct spectator block",
        CLOSED,
        FAILED,
        CLOSED,
        PARTIAL,
        PARTIAL,
        PARTIAL,
        PARTIAL,
        CLOSED,
    ),
    Route(
        "priority rough-terminal gauge subsystem",
        OPEN,
        CLOSED,
        CLOSED,
        PARTIAL,
        CLOSED,
        PARTIAL,
        PARTIAL,
        OPEN,
    ),
    Route(
        "coherent orientation/parity carriers",
        FAILED,
        OPEN,
        PARTIAL,
        PARTIAL,
        CLOSED,
        OPEN,
        OPEN,
        OPEN,
    ),
    Route(
        "Wilson-sector local-process quotient",
        OPEN,
        PARTIAL,
        CLOSED,
        PARTIAL,
        CLOSED,
        PARTIAL,
        PARTIAL,
        OPEN,
    ),
    Route(
        "genuine staggered parity shuttle",
        PARTIAL,
        FAILED,
        CLOSED,
        PARTIAL,
        PARTIAL,
        OPEN,
        OPEN,
        PARTIAL,
    ),
    Route(
        "dressed one-star parity join",
        FAILED,
        OPEN,
        PARTIAL,
        PARTIAL,
        FAILED,
        OPEN,
        OPEN,
        OPEN,
    ),
    Route(
        "coarse observable-specific Wilson diagnostic",
        OPEN,
        TARGET,
        TARGET,
        PARTIAL,
        CLOSED,
        CLOSED,
        PARTIAL,
        OPEN,
    ),
    Route(
        "matched Wilson-sector algebraic states",
        OPEN,
        PARTIAL,
        CLOSED,
        PARTIAL,
        CLOSED,
        PARTIAL,
        PARTIAL,
        OPEN,
    ),
)


ANTI_SPLICES = (
    (
        "Cycle-248 bounded full-Fock E",
        "Cycle-251 bounded sectorwise G",
        "different physical codes and operator dictionaries",
    ),
    (
        "Cycle-271 local process quotient",
        "bounded global preparation",
        "the comparison map may be system-spanning",
    ),
    (
        "Cycle-272 proper-frame carrier",
        "matter-parity join",
        "the tested rank-correct bindings still impose P_m=b^N",
    ),
    (
        "Cycle-260 zero-failure parity shuttle",
        "bounded physical macro update",
        "the macro-transition support is 4L-1",
    ),
    (
        "Cycle-255 Record dependency depth",
        "physical occurrence close",
        "the completion transcript survives FSWAP deletion",
    ),
    (
        "proper-cubic frame covariance",
        "derived time",
        "the frame group acts on supplied 3D space",
    ),
    (
        "Cycle-273 uniform rank-correct family",
        "Cycle-273 all-frame directional family",
        "the former fails 20 frames while the latter is noncommuting",
    ),
    (
        "Cycle-274 operator separation",
        "prepared physical readout",
        "an operator residual supplies no witness-state or physical-M2 preparation",
    ),
    (
        "Cycle-275 global algebraic sector states",
        "bounded preparation or odd-state fixture",
        "Wilson projectors and membranes are system-spanning and the states are total-even",
    ),
)


LANE_SCORES = {
    "operational quantum / Records": (42, 18, 63),
    "causal time / clock": (32, 17, 58),
    "inertia / matter": (58, 24, 77),
    "gravity / source / resource": (34, 12, 58),
    "Born / probability / realized history": (30, 14, 74),
}


LOAD_BEARING_RUNNERS = {
    "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py": (30, 0),
    "rough_terminal_subsystem_gauge_factorization_cycle251_2026_07_17.py": (15, 0),
    "followup_m64_physical_m2_compiler_tournament_synthesis_cycle257_2026_07_17.py": (14, 0),
    "contractible_lightcone_wilson_quotient_cycle271_2026_07_17.py": (16, 0),
    "coherent_orientation_character_car_compiler_cycle272_2026_07_17.py": (10, 0),
    "dressed_spoke_parity_gauge_cycle273_2026_07_17.py": (11, 0),
    "observable_specific_wilson_blindness_cycle274_2026_07_17.py": (37, 0),
    "locally_matched_wilson_sector_states_cycle275_2026_07_17.py": (14, 0),
}


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split()).lower()


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-276 synthesis note exists", False, NOTE)
        return

    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "result in plain english",
        "e g_coarse = g_physical e",
        "route-by-route disposition",
        "exact residual and control inventory",
        "supplied structure that remains supplied",
        "updated six-wall ledger",
        "effect on all five toe lanes",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "optimal next campaign",
        "prior-art and novelty boundary",
        "pass for the factual census",
        "fail for a broad compiler no-go",
        "compiler layers, parity shuttles, wilson labels, and runner steps are not physical time",
        "a wilson label or coherent carrier is not a record",
        "wrapped phase is not physical energy",
        "generator element is not a rate",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    check("the synthesis note contains the full scope, ledger, lane, and N1-N8 contract", not missing, missing)
    check(
        "the final note has no unresolved result placeholders",
        "pending independent result review" not in text and "pending review" not in text,
    )


def route_contract() -> None:
    allowed = {CLOSED, PARTIAL, FAILED, OPEN, TARGET}
    bad = []
    for route in ROUTES:
        for field, value in route.__dict__.items():
            if field != "name" and value not in allowed:
                bad.append((route.name, field, value))
    check("every route clause has an explicit disposition", not bad, bad)
    check("no single reviewed route closes the whole campaign contract", not any(route.complete() for route in ROUTES))
    check(
        "direct and gauge routes close complementary clauses and may not be spliced",
        ROUTES[1].bounded_full_fock_E == CLOSED
        and ROUTES[1].bounded_actual_G == FAILED
        and ROUTES[2].bounded_full_fock_E == OPEN
        and ROUTES[2].bounded_actual_G == CLOSED,
    )
    check("anti-feature-splicing controls are explicit", len(ANTI_SPLICES) >= 9, ANTI_SPLICES)


def score_contract() -> None:
    check("all five TOE receiving lanes were reconnoitered", len(LANE_SCORES) == 5, LANE_SCORES)
    bad = {
        lane: values
        for lane, values in LANE_SCORES.items()
        if not (0 <= values[1] <= values[0] <= values[2] <= 100)
    }
    check("strict <= integrated <= conditional for every lane", not bad, bad)
    check(
        "matter is the strongest integrated lane while gravity has the lowest strict floor",
        max(LANE_SCORES, key=lambda lane: LANE_SCORES[lane][0]) == "inertia / matter"
        and min(LANE_SCORES, key=lambda lane: LANE_SCORES[lane][1]) == "gravity / source / resource",
    )


def parse_summary(output: str) -> tuple[int, int] | None:
    patterns = (
        r"SUMMARY PASS\s+(\d+)\s+FAIL\s+(\d+)",
        r"SUMMARY\s+\{'pass':\s*(\d+),\s*'fail':\s*(\d+)\}",
    )
    for pattern in patterns:
        matches = re.findall(pattern, output)
        if matches:
            passed, failed = matches[-1]
            return int(passed), int(failed)
    return None


def cold_regressions() -> None:
    results: dict[str, object] = {}
    for name, expected in LOAD_BEARING_RUNNERS.items():
        path = SCRIPTS / name
        if not path.exists():
            results[name] = "missing"
            continue
        proc = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=180,
            check=False,
        )
        parsed = parse_summary(proc.stdout)
        results[name] = {
            "returncode": proc.returncode,
            "parsed": parsed,
            "expected": expected,
        }
    bad = {
        name: result
        for name, result in results.items()
        if not isinstance(result, dict)
        or result["returncode"] != 0
        or result["parsed"] != result["expected"]
    }
    check("all load-bearing predecessor runners pass cold with exact counts", not bad, bad or results)


def exact_fixture_contract() -> None:
    note = normalized(NOTE)
    required = (
        "beta=-0.3",
        "g=0.37",
        "0.4534056541748851",
        "principal l=3 sea rank = 73",
        "2 sqrt(2)",
        "6l^2+4",
        "3,092,544",
        "4l-1",
        "992/993",
        "1406/1407",
        "992/992",
        "first-wrap sector residual 2",
        "deletion `sqrt(2)`",
    )
    missing = tuple(fragment for fragment in required if fragment not in note)
    check("the final note retains the exact target and route residuals", not missing, missing)


def pressure_contract() -> None:
    constructive = tuple(route for route in ROUTES if route.name != "Cycle-230 intrinsic target")
    shared_failed_clauses = {
        field: tuple(getattr(route, field) for route in constructive)
        for field in CONTRACT_FIELDS
        if all(getattr(route, field) == FAILED for route in constructive)
    }
    open_or_partial_routes = {
        field: tuple(route.name for route in constructive if getattr(route, field) in {OPEN, PARTIAL, TARGET})
        for field in CONTRACT_FIELDS
    }
    text = normalized(NOTE)
    gate_is_scoped = (
        "pass for the factual census that no reviewed route closes all campaign clauses in one encoding" in text
        and "fail for a broad compiler no-go, minimum substrate-content claim, or axiom-pressure claim" in text
    )
    minimum_content_supported = bool(shared_failed_clauses)
    axiom_pressure_supported = bool(shared_failed_clauses) and not any(open_or_partial_routes.values())
    check(
        "no shared failed clause survives the live-route audit, so the gate rejects minimum content and axiom pressure",
        not shared_failed_clauses
        and not minimum_content_supported
        and not axiom_pressure_supported
        and gate_is_scoped,
        {
            "shared_failed_clauses": shared_failed_clauses,
            "open_or_partial_routes": open_or_partial_routes,
            "minimum_content_supported": minimum_content_supported,
            "axiom_pressure_supported": axiom_pressure_supported,
            "gate_is_scoped": gate_is_scoped,
        },
    )


def main() -> None:
    note_contract()
    route_contract()
    score_contract()
    exact_fixture_contract()
    cold_regressions()
    pressure_contract()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
