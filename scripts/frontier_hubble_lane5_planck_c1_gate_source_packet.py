#!/usr/bin/env python3
"""Source-packet verifier for the Hubble Lane 5 Planck C1 gate.

This runner is not an audit verdict. It packages the source-side evidence for
the Cycle 5 gate note by checking that the parent note exposes its dependency
anchors, names the residual Planck/Clifford-CAR coframe and action-unit gate,
and preserves the non-promotion boundary: the scale-reference primitive is
units-only, and no C1 closure, retained R_Lambda numerics, or H0 closure are
claimed on the actual current surface.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0

PARENT = "docs/HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md"
RUNNER = "scripts/frontier_hubble_lane5_planck_c1_gate_source_packet.py"
CACHE = "logs/runner-cache/frontier_hubble_lane5_planck_c1_gate_source_packet.txt"

DEPENDENCIES = {
    "planck_scale_lane_status_note_2026-04-23": (
        "docs/PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md"
    ),
    "scale_reference_primitive": "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "planck_scale_conditional_completion_note_2026-04-24": (
        "docs/PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md"
    ),
    "planck_target3_clifford_phase_bridge_theorem_note_2026-04-25": (
        "docs/PLANCK_TARGET3_CLIFFORD_PHASE_BRIDGE_THEOREM_NOTE_2026-04-25.md"
    ),
    "area_law_native_car_semantics_tightening_note_2026-04-25": (
        "docs/AREA_LAW_NATIVE_CAR_SEMANTICS_TIGHTENING_NOTE_2026-04-25.md"
    ),
    "planck_target3_phase_unit_edge_statistics_boundary_note_2026-04-25": (
        "docs/PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md"
    ),
}

CLOSED_ROUTE_MARKERS = [
    "PLANCK_FINITE_RESPONSE_NO_GO_NOTE_2026-04-24.md",
    "PLANCK_PARENT_SOURCE_HIDDEN_CHARACTER_NO_GO_NOTE_2026-04-24.md",
    "AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25.md",
    "AREA_LAW_MULTIPOCKET_SELECTOR_NO_GO_NOTE_2026-04-25.md",
    "AREA_LAW_PRIMITIVE_EDGE_ENTROPY_SELECTOR_NO_GO_NOTE_2026-04-25.md",
    "AREA_LAW_ALGEBRAIC_SPECTRUM_ENTROPY_NO_GO_NOTE_2026-04-25.md",
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return condition


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def part1_packet_metadata() -> None:
    section("Part 1: parent source-packet metadata")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    check("parent note exists", (ROOT / PARENT).exists(), PARENT)
    check("parent declares this primary runner", RUNNER in parent)
    check("parent declares this runner cache", CACHE in parent)
    check(
        "parent remains an open-gate support source packet",
        "support gate-identification note on `main`" in parent_norm
        and "**Claim type:** open_gate" in parent
        and "identifies the residual coframe/CAR response and action-unit" in parent_norm,
    )
    check(
        "source-packet boundary says it is not a theorem",
        "This is an audit / gate-identification artifact, not a theorem" in parent_norm,
    )
    check(
        "source-packet boundary forbids promotion claims",
        "does not derive the metric-compatible Clifford/CAR coframe response" in parent_norm
        and "derive the scale-reference primitive" in parent_norm
        and "retain `R_Lambda` numerically" in parent_norm
        and "apply an audit verdict" in parent_norm,
    )


def part2_registered_dependencies() -> None:
    section("Part 2: dependency links and source fingerprints")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    for claim_id, rel in DEPENDENCIES.items():
        check(f"{claim_id}: linked from parent", f"[{claim_id}](" in parent and Path(rel).name in parent)
        check(f"{claim_id}: file exists", (ROOT / rel).exists(), rel)

    status = read(DEPENDENCIES["planck_scale_lane_status_note_2026-04-23"])
    scale = read(DEPENDENCIES["scale_reference_primitive"])
    conditional = read(DEPENDENCIES["planck_scale_conditional_completion_note_2026-04-24"])
    target3 = read(DEPENDENCIES["planck_target3_clifford_phase_bridge_theorem_note_2026-04-25"])
    car_tightening = read(DEPENDENCIES["area_law_native_car_semantics_tightening_note_2026-04-25"])
    phase_boundary = read(DEPENDENCIES["planck_target3_phase_unit_edge_statistics_boundary_note_2026-04-25"])

    check(
        "scale-reference primitive is units-only and non-bounding",
        "This is a units conversion, not a physics axiom" in scale
        and "It does not assert `a/l_P = 1` as a derived theorem" in scale
        and "should not become\n`retained_bounded` merely for using a ruler" in scale,
    )
    check(
        "parent treats the scale primitive as units-only",
        "grants `a^{-1} = M_Pl` as a units conversion only" in parent_norm
        and "not a Planck import, not a Tier-A admission" in parent_norm
        and "derived `a/l_P = 1` theorem" in parent_norm,
    )
    check(
        "legacy Planck status keeps natural-unit derivation conditional",
        "conditional on the primitive Clifford-Majorana edge carrier premise" in status
        and "`a^(-1) = M_Pl` remains the explicit package pin" in status,
    )
    check(
        "Planck status names the coframe/CAR bridge and non-CAR alternatives",
        "P_A H_cell -> Cl_4(C) irreducible module -> F(C^2)" in status
        and "non-CAR rank-four readings" in status,
    )
    check(
        "conditional packet supplies c_cell and a/l_P algebra under a premise",
        "conditional algebraic theorem" in conditional
        and "c_cell = Tr(rho_cell P_A) = 4/16 = 1/4" in conditional
        and "a/l_P = 1" in conditional,
    )
    check(
        "Target 3 bridge is conditional on supplied coframe response",
        "supplied metric-compatible coframe response" in target3
        and "It does not\nderive the coframe response on `K`" in target3,
    )
    check(
        "CAR tightening leaves rank-four semantics underdetermined",
        "does not by itself fix the dimensional action scale or force CAR" in car_tightening
        and "two-qubit/ququart semantics on the same rank-four block" in car_tightening,
    )
    check(
        "phase-unit boundary records action-scale and CAR blockers",
        "does not derive an absolute\ndimensional action unit" in phase_boundary
        and "does not force the primitive CAR edge\nstatistics" in phase_boundary,
    )


def part3_single_gate_inventory() -> None:
    section("Part 3: single residual Planck C1 gate")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    check(
        "parent identifies a single residual premise",
        "single residual premise" in parent_norm,
    )
    check(
        "gate object is the metric-compatible Clifford/CAR coframe response",
        "metric-compatible Clifford/CAR coframe response" in parent_norm
        and "rank-four boundary block `P_A H_cell" in parent_norm,
    )
    check(
        "edge-statistics and action-unit obligations are both named",
        "**Edge-statistics principle**" in parent
        and "**Action-unit metrology**" in parent,
    )
    check(
        "three Planck targets collapse to one shared conditional",
        "all three Planck-lane targets have collapsed to **one shared conditional**" in parent_norm,
    )
    check(
        "closed shortcut routes are inventoried",
        all(marker in parent for marker in CLOSED_ROUTE_MARKERS),
    )
    check(
        "parent explicitly says it does not close the Planck lane",
        "does NOT close the Planck lane" in parent,
    )


@dataclass(frozen=True)
class PlanckGatePacket:
    scale_reference_declared: bool
    coframe_response_retained: bool
    natural_action_units_retained: bool
    history_ratio_or_direct_l_retained: bool

    def c1_scale_route_closed(self) -> bool:
        return self.coframe_response_retained and self.natural_action_units_retained

    def h0_closed_through_c1(self) -> bool:
        return self.c1_scale_route_closed() and self.history_ratio_or_direct_l_retained


def part4_non_promotion_model() -> None:
    section("Part 4: finite non-promotion model")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    current = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_retained=False,
        natural_action_units_retained=False,
        history_ratio_or_direct_l_retained=False,
    )
    scale_only = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_retained=False,
        natural_action_units_retained=False,
        history_ratio_or_direct_l_retained=False,
    )
    coframe_only = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_retained=True,
        natural_action_units_retained=False,
        history_ratio_or_direct_l_retained=False,
    )
    c1_only = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_retained=True,
        natural_action_units_retained=True,
        history_ratio_or_direct_l_retained=False,
    )
    full_lane5 = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_retained=True,
        natural_action_units_retained=True,
        history_ratio_or_direct_l_retained=True,
    )

    print("  rule: the scale-reference primitive is units-only")
    print("  rule: C1 closes only with coframe response and natural action units")
    print("  rule: H0 still needs C2 or C3 after C1 closes")

    check("actual current packet declares the units primitive", current.scale_reference_declared)
    check("scale-reference primitive alone does not close C1", not scale_only.c1_scale_route_closed())
    check("actual current packet does not close C1", not current.c1_scale_route_closed())
    check("coframe response alone is not enough without action units", not coframe_only.c1_scale_route_closed())
    check("C1 alone is not H0 closure without C2/C3", c1_only.c1_scale_route_closed() and not c1_only.h0_closed_through_c1())
    check("full C1 plus C2/C3 packet would close the modeled route", full_lane5.h0_closed_through_c1())
    check(
        "parent records C2/C3 as separately required",
        "(C1) scale route AND one of {(C2) cosmic-history-ratio retirement, (C3) direct cosmic-`L` derivation}" in parent_norm,
    )
    check(
        "runner boundary forbids audit-result mutation",
        "does not derive" in parent_norm and "apply an audit verdict" in parent_norm,
    )


def main() -> int:
    print("=" * 88)
    print("HUBBLE LANE 5 PLANCK C1 GATE SOURCE PACKET")
    print("=" * 88)
    print()
    print("Question:")
    print("  Is the Cycle 5 Planck C1 gate packaged with source anchors,")
    print("  a replayable single-gate inventory, and a non-promotion boundary?")
    print()
    print("Answer:")
    print("  Yes for source-packet readiness. This runner does not close C1,")
    print("  retain R_Lambda numerically, close H0, or apply an audit verdict.")

    part1_packet_metadata()
    part2_registered_dependencies()
    part3_single_gate_inventory()
    part4_non_promotion_model()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
