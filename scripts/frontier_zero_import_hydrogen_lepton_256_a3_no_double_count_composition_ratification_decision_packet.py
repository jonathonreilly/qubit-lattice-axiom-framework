#!/usr/bin/env python3
"""Verifier for the A3 no-double-count composition decision packet.

This runner checks that the A3 correction single-spend law is packaged as a
composition-control handoff. It does not ratify A3 placement, derive C_A3,
derive N_A3, derive m_e, derive alpha(0), or claim hydrogen is retained.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_NO_DOUBLE_COUNT_COMPOSITION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
PRECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
P1_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
P2_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P3_KOIDE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P4_DIRECT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
WEAK_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA0 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


COMPOSITION_INPUTS = {
    "A3_SINGLE_SPEND_TEXT_LOCK",
    "PLACEMENT_SLOT_SET_LOCK",
    "EXACT_SOURCE_SCAFFOLD_SEPARATION",
    "ONE_CORRECTION_SPEND_RULE",
    "DEPENDENCY_LOCATION_LABEL_RETAINED",
    "PRODUCT_EQUIVALENCE_NOT_THEOREM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

A3_INPUTS = {
    "A3_PLACEMENT_TEXT_LOCK",
    "EXACT_SOURCE_SCAFFOLD_STATUS",
    "ONE_PLACEMENT_SELECTED",
    "PLACEMENT_THEOREM_RETAINED",
    "NO_SOURCE_DOUBLE_COUNT",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

K4_INPUTS = {
    "K4_SCALE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "WEAK_FRONT_BASE_RETAINED",
    "EXACT_SOURCE_SINGLETON_RETAINED",
    "A3_PRECISION_PLACEMENT_RETAINED",
    "NO_SOURCE_A3_DOUBLE_COUNT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PLACEMENTS = {
    "P1_SOURCE_READOUT_CORRECTION_RETAINED",
    "P2_WEAK_FRONT_MATCHING_RETAINED",
    "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
    "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
}


class Audit:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            prefix = "PASS"
        else:
            self.fail_count += 1
            prefix = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{prefix}: {label}{suffix}")

    def summary(self) -> None:
        print(f"\nSUMMARY: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(text: str) -> str:
    return " ".join(text.split())


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def all_subsets(items: set[str]) -> list[set[str]]:
    ordered = sorted(items)
    subsets: list[set[str]] = []
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            subsets.append(set(combo))
    return subsets


def closes_composition(inputs: set[str]) -> bool:
    return COMPOSITION_INPUTS <= inputs


def closes_a3(inputs: set[str], placements: set[str]) -> bool:
    return A3_INPUTS <= inputs and len(PLACEMENTS & placements) == 1


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        K4_PACKET,
        A3_DECISION,
        A3_NO_GO,
        A3_PLACEMENT,
        PRECISION,
        P1_SOURCE_NO_GO,
        P2_TARGET,
        P2_FRONT_NO_GO,
        P3_KOIDE_NO_GO,
        P4_DIRECT_NO_GO,
        EXACT_SOURCE_NO_GO,
        WEAK_FRONT_NO_GO,
        PHYSICAL_ELECTRON,
        ALPHA0,
        STATIC_TARGET,
        REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "A3 No-Double-Count Composition Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify A3 precision placement",
        "NO_SOURCE_A3_DOUBLE_COUNT",
        "NO_SOURCE_DOUBLE_COUNT",
        "the single-spend composition law for the A3 correction",
        "D.1",
        "D.2",
        "D.3",
        "D.4",
        "D.5",
        "A3_SINGLE_SPEND_TEXT_LOCK",
        "PLACEMENT_SLOT_SET_LOCK",
        "EXACT_SOURCE_SCAFFOLD_SEPARATION",
        "ONE_CORRECTION_SPEND_RULE",
        "DEPENDENCY_LOCATION_LABEL_RETAINED",
        "PRODUCT_EQUIVALENCE_NOT_THEOREM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those ten contract inputs",
        "A3_CORRECTION_SINGLE_SPEND_COMPOSITION_LAW_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "P1_SOURCE_READOUT_CORRECTION_RETAINED",
        "P2_WEAK_FRONT_MATCHING_RETAINED",
        "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
        "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
        "C_A3_RETAINED",
        "N_A3_RETAINED",
        "P12 = (C * F_0) * (C * S_0) * R_0",
        "C^2 * F_0 * S_0 * R_0",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "Open PRs were refreshed on 2026-07-05 UTC after `#5016` opened",
        "clean/green status is not a prerequisite",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(COMPOSITION_INPUTS)
    audit.check("full composition contract accepts handoff", closes_composition(full_inputs))
    for missing in sorted(COMPOSITION_INPUTS):
        reduced = set(COMPOSITION_INPUTS)
        reduced.remove(missing)
        audit.check(f"composition handoff fails without {missing}", not closes_composition(reduced))
    accepted_subsets = [subset for subset in all_subsets(COMPOSITION_INPUTS) if closes_composition(subset)]
    audit.check("only full composition subset closes handoff", accepted_subsets == [full_inputs])

    composition_consequence = {
        "A3_CORRECTION_SINGLE_SPEND_COMPOSITION_LAW_RETAINED",
        "NO_SOURCE_DOUBLE_COUNT",
        "NO_SOURCE_A3_DOUBLE_COUNT",
    }
    audit.check(
        "composition consequence alone does not close A3",
        not closes_a3(composition_consequence, {"P2_WEAK_FRONT_MATCHING_RETAINED"}),
    )
    audit.check("composition consequence alone does not close K4", not closes_k4(composition_consequence))
    audit.check("full A3 contract plus one placement closes A3", closes_a3(set(A3_INPUTS), {"P2_WEAK_FRONT_MATCHING_RETAINED"}))
    audit.check("full K4 contract closes K4", closes_k4(set(K4_INPUTS)))

    section("Finite no-double-count arithmetic")
    getcontext().prec = 60
    n_a3 = Decimal("256.08243522600384")
    c_a3 = Decimal(256) / n_a3
    s0 = Decimal(1) / Decimal(256)
    f0 = Decimal("0.461616")
    r0 = Decimal("1.375")
    base = f0 * s0 * r0
    p1 = f0 * (c_a3 * s0) * r0
    p2 = (c_a3 * f0) * s0 * r0
    p3 = f0 * s0 * (c_a3 * r0)
    p4 = f0 * (Decimal(1) / n_a3) * r0
    p12 = (c_a3 * f0) * (c_a3 * s0) * r0
    audit.check("A3 correction target reproduced", abs(c_a3 - Decimal("0.9996780910571587")) < Decimal("1e-16"), str(c_a3))
    audit.check("exact source scaffold is 1/256", s0 == Decimal("0.00390625"))
    audit.check("direct noninteger singleton equals C_A3/256", abs(Decimal(1) / n_a3 - c_a3 * s0) < Decimal("1e-55"))
    audit.check("P1 product equals P2 product", abs(p1 - p2) < Decimal("1e-55"))
    audit.check("P1 product equals P3 product", abs(p1 - p3) < Decimal("1e-55"))
    audit.check("P1 product equals P4 product", abs(p1 - p4) < Decimal("1e-55"))
    audit.check("one placement equals C_A3 times base", abs(p1 / base - c_a3) < Decimal("1e-55"))
    audit.check("C_A3 is not one", c_a3 != Decimal(1))
    audit.check("double-spend product differs from one-spend product", abs(p12 - p1) > Decimal("1e-9"))
    audit.check("double-spend product is C_A3 squared times base", abs(p12 / base - c_a3 * c_a3) < Decimal("1e-55"))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    k4 = read(K4_PACKET)
    a3_decision = read(A3_DECISION)
    a3_no_go = read(A3_NO_GO)
    placement = read(A3_PLACEMENT)
    precision = read(PRECISION)
    p1_no_go = read(P1_SOURCE_NO_GO)
    p2_target = read(P2_TARGET)
    p2_no_go = read(P2_FRONT_NO_GO)
    p3_no_go = read(P3_KOIDE_NO_GO)
    p4_no_go = read(P4_DIRECT_NO_GO)
    exact_source = read(EXACT_SOURCE_NO_GO)
    weak_front = read(WEAK_FRONT_NO_GO)
    physical_electron = read(PHYSICAL_ELECTRON)
    alpha0 = read(ALPHA0)
    static_target = read(STATIC_TARGET)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    nodes = registry["nodes"]

    audit.check("goal packet references composition packet", NOTE.name in goal)
    audit.check("K4 packet references composition packet", NOTE.name in k4)
    audit.check("A3 decision references composition packet", NOTE.name in a3_decision)
    audit.check("A3 no-go references composition packet", NOTE.name in a3_no_go)
    audit.check("K4 consumes no-source-A3 double-count control", "NO_SOURCE_A3_DOUBLE_COUNT" in k4)
    audit.check("A3 consumes no-source double-count control", "NO_SOURCE_DOUBLE_COUNT" in a3_decision)
    audit.check("placement discriminator separates P1-P5", all(token in placement for token in ["P1 source-readout", "P2 front-factor", "P3 Koide", "P4 direct", "P5 empirical"]))
    audit.check("precision firewall does not derive C_A3", "No derivation of `C_A3 = 0.999678091...`" in precision)
    audit.check("P1 remains unsupplied", "P1_SOURCE_READOUT_CORRECTION_RETAINED" in p1_no_go and "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED" in p1_no_go)
    audit.check("P2 target remains theorem target", "F_phys = C_A3 * g_2 * (1/sqrt(2))" in p2_target and "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in p2_target)
    audit.check("P2 remains unsupplied", "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in p2_no_go and "MATCHING_THEOREM_RETAINED" in p2_no_go)
    audit.check("P3 remains unsupplied", "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED" in p3_no_go and "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED" in p3_no_go)
    audit.check("P4 remains unsupplied", "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED" in p4_no_go and "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED" in p4_no_go)
    audit.check("A3 current no-go keeps placement open", "A3_PRECISION_PLACEMENT_RETAINED" in a3_no_go and "current retained, primitive, and open-PR surfaces do not supply" in a3_no_go)
    audit.check("exact source remains separate", "EXACT_SOURCE_SINGLETON_RETAINED" in exact_source)
    audit.check("weak front remains separate", "WEAK_FRONT_BASE_RETAINED" in weak_front)
    audit.check("physical electron remains downstream", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron)
    audit.check("alpha0 remains downstream", "ALPHA0_RETAINED" in alpha0)
    audit.check("static source remains downstream", "static-source Rydberg" in static_target)
    audit.check("minimal axioms keep source/action downstream", "source/action" in minimal and "downstream" in minimal)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    for absent in [
        "a3_single_spend_primitive",
        "a3_no_double_count_primitive",
        "a3_correction_primitive",
        "a3_placement_selector_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered composition shortcut: {absent}", absent not in registry_text)
    audit.check("scale primitive excludes dimensionless correction", "zero dimensionless content" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes values and normalization", "normalization rule" in realized and "or value is supplied" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5011` eta twisted walk family runner | open",
        "`#5010` YT P1 I_s re-audit packet bridge repair | open",
        "`#5009` S3 spacetime tensor primitive runner | open",
        "`#5008` quark mass-ratio CP probe repair | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#5006` static-source I1 hygiene companion | open",
        "`#4991` owner-governed Tier-A retirement | open",
    ]
    for marker in latest_pr_markers:
        audit.check(f"opened PR marker present: {marker}", flat(marker) in note_flat)
    audit.check("open PR check does not require clean status", "clean/green status is not a prerequisite" in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of A3 precision placement.",
        "No derivation or ratification of any P1/P2/P3/P4 placement theorem.",
        "No derivation or ratification of `C_A3`.",
        "No derivation or ratification of `N_A3`.",
        "No derivation or ratification of corrected `S_l = 1/N_A3`.",
        "No derivation or ratification of the exact source singleton.",
        "No derivation or ratification of the weak-front base.",
        "No derivation or ratification of the absolute charged-lepton scale.",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`,",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies A3 precision placement",
        "A3_PRECISION_PLACEMENT_RETAINED is supplied",
        "C_A3 is retained",
        "N_A3 is retained",
        "m_e is retained",
        "alpha(0) is retained",
        "retained hydrogen calculation is complete",
        "observed charged-lepton masses are proof inputs",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
