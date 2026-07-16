#!/usr/bin/env python3
"""Source-packet verifier for the Hubble Lane 5 Planck C1 gate.

This runner is not an audit verdict. It packages the source-side evidence for
the Cycle 5 gate note by checking that the parent note exposes its dependency
anchors, names the residual active-block response, physical edge-channel/Widom
law, gravitational boundary/action identification, and action-unit packet,
and preserves the non-promotion boundary: the
scale-reference primitive is units-only, and no C1 closure, retained R_Lambda
numerics, or H0 closure are claimed on the actual current surface.
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
    "area_law_primitive_car_edge_identification_theorem_note_2026-04-25": (
        "docs/AREA_LAW_PRIMITIVE_CAR_EDGE_IDENTIFICATION_THEOREM_NOTE_2026-04-25.md"
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
        "**Type:** open_gate" in parent
        and "identifies the residual active-block response, edge-channel/Widom, gravitational boundary/action, and action-unit" in parent_norm,
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
    primitive_car = read(
        DEPENDENCIES[
            "area_law_primitive_car_edge_identification_theorem_note_2026-04-25"
        ]
    )
    primitive_car_norm = normalize(primitive_car)
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
        and "not a Planck import or a source of bounded theorem strength" in parent_norm
        and "derived `a/l_P = 1` theorem" in parent_norm,
    )
    check(
        "Planck status keeps source-unit/gravitational premises separate from Clifford/CAR",
        "natural-unit structural derivation `G_Newton,lat=1`, `a/l_P=1`" in status
        and "conditional on the separately supplied primitive coefficient" in status
        and "gravitational/Wald identification" in status
        and "not a consequence of the Clifford/CAR bridge" in status
        and "`a^(-1) = M_Pl` remains the explicit package pin" in status,
    )
    check(
        "Planck status records the exact specified-action obstruction",
        "equivariant\nintertwiner space is zero" in status
        and "compresses to zero on `P_A`" in status,
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
        "CAR equivalence note rejects substrate and channel implications",
        "conditional algebraic equivalence only" in car_tightening
        and "It does not imply `c_Widom=1/4`" not in car_tightening
        and "it does not imply `c_Widom=1/4`" in car_tightening
        and "None is currently supplied" in car_tightening,
    )
    check(
        "rank-four CAR note keeps channel and Widom conditions supplied",
        "## Supplied rank-four CAR edge conditions" in primitive_car
        and "**Normal-channel condition.**" in primitive_car
        and "**Tangent-channel condition.**" in primitive_car
        and "**Widom applicability and normalization condition.**" in primitive_car
        and "CAR algebra does not derive the normal/tangent channel assignment" in primitive_car_norm,
    )
    check(
        "phase-unit boundary records action-scale and CAR blockers",
        "does not derive an absolute\ndimensional action unit" in phase_boundary
        and "does not force the primitive CAR edge\nstatistics" in phase_boundary,
    )


def part3_gate_packet_inventory() -> None:
    section("Part 3: coupled residual Planck C1 gate packet")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    check(
        "parent identifies coupled residual premises",
        "coupled residual gate packet" in parent_norm
        and "coupled open packet, not a single premise" in parent_norm,
    )
    check(
        "source-packet boundary describes the coupled inventory consistently",
        "coupled response/channel/Widom/gravitational-carrier/action-unit inventory" in parent_norm
        and "single-gate inventory" not in parent_norm,
    )
    check(
        "packet includes active-block response and physical channel/Widom law",
        "**Active-block response**" in parent
        and "**Physical channel law**" in parent,
    )
    check(
        "gravitational-carrier obligation remains separately named",
        "(G1c)" in parent
        and "**Gravitational boundary/action identification**" in parent,
    )
    check(
        "action-unit obligation remains separately named",
        "**Action-unit metrology**" in parent
        and "(G2)" in parent,
    )
    check(
        "parent rejects algebra-to-channel collapse",
        "coframe response gives the CAR algebra but not (G1b) or (G1c)" in parent_norm
        and "Target 2 additionally needs the edge-channel law" in parent_norm,
    )
    check(
        "all four residual obligations are named",
        "(G1a)" in parent
        and "(G1b)" in parent
        and "(G1c)" in parent
        and "(G2)" in parent
        and "**Action-unit metrology**" in parent,
    )
    check(
        "scoped shortcut routes are inventoried",
        all(marker in parent for marker in CLOSED_ROUTE_MARKERS),
    )
    check(
        "parent explicitly says it does not close the Planck lane",
        "does NOT close the Planck lane" in parent,
    )


@dataclass(frozen=True)
class PlanckGatePacket:
    scale_reference_declared: bool
    coframe_response_supplied: bool
    edge_channel_law_supplied: bool
    widom_conditions_supplied: bool
    gravitational_carrier_supplied: bool
    natural_action_units_supplied: bool
    history_ratio_or_direct_l_supplied: bool

    def c1_scale_route_closed(self) -> bool:
        return (
            self.scale_reference_declared
            and self.coframe_response_supplied
            and self.edge_channel_law_supplied
            and self.widom_conditions_supplied
            and self.gravitational_carrier_supplied
            and self.natural_action_units_supplied
        )

    def target2_carrier_closed(self) -> bool:
        return (
            self.scale_reference_declared
            and self.coframe_response_supplied
            and self.edge_channel_law_supplied
            and self.widom_conditions_supplied
        )

    def h0_closed_through_c1(self) -> bool:
        return self.c1_scale_route_closed() and self.history_ratio_or_direct_l_supplied


def part4_non_promotion_model() -> None:
    section("Part 4: finite non-promotion model")
    parent = read(PARENT)
    parent_norm = normalize(parent)

    current = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_supplied=False,
        edge_channel_law_supplied=False,
        widom_conditions_supplied=False,
        gravitational_carrier_supplied=False,
        natural_action_units_supplied=False,
        history_ratio_or_direct_l_supplied=False,
    )
    scale_only = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_supplied=False,
        edge_channel_law_supplied=False,
        widom_conditions_supplied=False,
        gravitational_carrier_supplied=False,
        natural_action_units_supplied=False,
        history_ratio_or_direct_l_supplied=False,
    )
    coframe_only = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_supplied=True,
        edge_channel_law_supplied=False,
        widom_conditions_supplied=False,
        gravitational_carrier_supplied=False,
        natural_action_units_supplied=False,
        history_ratio_or_direct_l_supplied=False,
    )
    c1_only = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_supplied=True,
        edge_channel_law_supplied=True,
        widom_conditions_supplied=True,
        gravitational_carrier_supplied=True,
        natural_action_units_supplied=True,
        history_ratio_or_direct_l_supplied=False,
    )
    missing_scale = PlanckGatePacket(
        scale_reference_declared=False,
        coframe_response_supplied=True,
        edge_channel_law_supplied=True,
        widom_conditions_supplied=True,
        gravitational_carrier_supplied=True,
        natural_action_units_supplied=True,
        history_ratio_or_direct_l_supplied=True,
    )
    missing_widom = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_supplied=True,
        edge_channel_law_supplied=True,
        widom_conditions_supplied=False,
        gravitational_carrier_supplied=True,
        natural_action_units_supplied=True,
        history_ratio_or_direct_l_supplied=True,
    )
    missing_gravity = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_supplied=True,
        edge_channel_law_supplied=True,
        widom_conditions_supplied=True,
        gravitational_carrier_supplied=False,
        natural_action_units_supplied=True,
        history_ratio_or_direct_l_supplied=True,
    )
    full_lane5 = PlanckGatePacket(
        scale_reference_declared=True,
        coframe_response_supplied=True,
        edge_channel_law_supplied=True,
        widom_conditions_supplied=True,
        gravitational_carrier_supplied=True,
        natural_action_units_supplied=True,
        history_ratio_or_direct_l_supplied=True,
    )

    print("  rule: the scale-reference primitive is units-only")
    print("  rule: C1 closes only with response, channel/Widom, gravitational carrier, and action units")
    print("  rule: H0 still needs C2 or C3 after C1 closes")

    check("actual current packet declares the units primitive", current.scale_reference_declared)
    check("scale-reference primitive alone does not close C1", not scale_only.c1_scale_route_closed())
    check("actual current packet does not close C1", not current.c1_scale_route_closed())
    check("coframe response alone is not enough without action units", not coframe_only.c1_scale_route_closed())
    check("coframe response alone does not close Target 2 without a channel law", not coframe_only.target2_carrier_closed())
    check("Target 2 remains open without Widom conditions", not missing_widom.target2_carrier_closed())
    check("C1 remains open without channel/Widom conditions", not missing_widom.c1_scale_route_closed())
    check(
        "C1 remains open without the gravitational carrier even when coefficient conditions hold",
        not missing_gravity.c1_scale_route_closed()
        and missing_gravity.target2_carrier_closed(),
    )
    check("full modeled packet includes the Target 2 channel and Widom laws", full_lane5.target2_carrier_closed())
    check("missing scale reference cannot close C1", not missing_scale.c1_scale_route_closed())
    check("missing scale reference cannot close Target 2 in this Planck packet", not missing_scale.target2_carrier_closed())
    check("missing scale reference cannot close H0 through C1", not missing_scale.h0_closed_through_c1())
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
    print("  a replayable coupled-gate inventory, and a non-promotion boundary?")
    print()
    print("Answer:")
    print("  Yes for source-packet readiness. This runner does not close C1,")
    print("  retain R_Lambda numerically, close H0, or apply an audit verdict.")

    part1_packet_metadata()
    part2_registered_dependencies()
    part3_gate_packet_inventory()
    part4_non_promotion_model()

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    sys.exit(main())
