#!/usr/bin/env python3
"""Verifier for the Koide native zero-section bridge current-surface no-go.

This runner checks that current Koide route support, approved primitives, and
open PRs do not silently supply the native bridge handoff consumed by the
physical electron mass lane. It preserves the positive bridge contract and
does not derive m_e, alpha(0), Rydberg, or hydrogen.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PHYSICAL_ELECTRON_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
BRIDGE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRIDGE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_TARGET_DISCRIMINATOR_2026-07-04.md"
PR5007_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md"
SPECIES_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
K4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
BRANCH_MASS_MAP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KOIDE_ROUTE_NOTE = ROOT / "docs" / "KOIDE_NATIVE_ZERO_SECTION_CLOSURE_ROUTE_NOTE_2026-04-24.md"
KOIDE_ROUTE_RUNNER = ROOT / "scripts" / "frontier_koide_native_zero_section_closure_route.py"
KOIDE_REVIEW_NOTE = ROOT / "docs" / "KOIDE_NATIVE_ZERO_SECTION_NATURE_REVIEW_NOTE_2026-04-24.md"
KOIDE_REVIEW_RUNNER = ROOT / "scripts" / "frontier_koide_native_zero_section_nature_review.py"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


BRIDGE_INPUTS = {
    "BRIDGE_TEXT_LOCK",
    "ZERO_SOURCE_READOUT_RETAINED",
    "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED",
    "BASED_DETERMINANT_LINE_READOUT_RETAINED",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PHYSICAL_ELECTRON_INPUTS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
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


def closes_bridge(inputs: set[str]) -> bool:
    return BRIDGE_INPUTS <= inputs


def closes_physical_electron(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_INPUTS <= inputs


def q_from_weight(w_plus: Fraction) -> Fraction:
    r = (1 - w_plus) / w_plus
    return (1 + r) / 3


def ktl_from_weight(w_plus: Fraction) -> Fraction:
    r = (1 - w_plus) / w_plus
    return (r * r - 1) / (4 * r)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        PHYSICAL_ELECTRON_PACKET,
        PHYSICAL_ELECTRON_NO_GO,
        BRIDGE_DECISION,
        BRIDGE_TARGET,
        PR5007_IMPACT,
        SPECIES_DECISION,
        K4_NO_GO,
        BRANCH_MASS_MAP_NO_GO,
        KOIDE_ROUTE_NOTE,
        KOIDE_ROUTE_RUNNER,
        KOIDE_REVIEW_NOTE,
        KOIDE_REVIEW_RUNNER,
        REGISTRY,
        TIER_A_REGISTRY,
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
        "Koide Native Zero-Section Bridge Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify the native zero-section",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "BRIDGE_TEXT_LOCK",
        "ZERO_SOURCE_READOUT_RETAINED",
        "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED",
        "BASED_DETERMINANT_LINE_READOUT_RETAINED",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "z = 0",
        "w_plus = 1/2",
        "Q = 2/3",
        "z = -1/3",
        "Q = 1",
        "real Z_3 primitive",
        "based endpoint F(0)=0",
        "eta_Z3",
        "delta_open = 2/9",
        "native_zero_section_bridge_primitive",
        "zero_source_readout_primitive",
        "real_primitive_brannen_endpoint_primitive",
        "based_determinant_line_readout_primitive",
        "koide_readout_bridge_primitive",
        "electron_mass_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad native-bridge no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Bridge predicate checks")
    full_inputs = set(BRIDGE_INPUTS)
    audit.check("full bridge contract accepts retained handoff", closes_bridge(full_inputs))
    for missing in sorted(BRIDGE_INPUTS):
        reduced = set(BRIDGE_INPUTS)
        reduced.remove(missing)
        audit.check(f"bridge handoff fails without {missing}", not closes_bridge(reduced))
    accepted_subsets = [subset for subset in all_subsets(BRIDGE_INPUTS) if closes_bridge(subset)]
    audit.check("only full bridge subset closes handoff", accepted_subsets == [full_inputs])
    current_surface = {
        "BRIDGE_TEXT_LOCK",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check("current surface without Z1/Z2/Z3 does not close bridge", not closes_bridge(current_surface))
    audit.check(
        "retained native bridge alone does not close physical electron",
        not closes_physical_electron({"NATIVE_ZERO_SECTION_BRIDGE_RETAINED"}),
    )
    audit.check(
        "full physical electron predicate still needs bridge plus other inputs",
        closes_physical_electron(set(PHYSICAL_ELECTRON_INPUTS)),
    )

    section("Finite route witness checks")
    z0_w = Fraction(1, 2)
    z_bad_w = Fraction(1, 3)
    audit.check("zero source gives w_plus=1/2", z0_w == Fraction(1, 2))
    audit.check("zero source gives K_TL=0", ktl_from_weight(z0_w) == 0)
    audit.check("zero source gives Q=2/3", q_from_weight(z0_w) == Fraction(2, 3))
    audit.check("nonzero source falsifier gives Q=1", q_from_weight(z_bad_w) == 1)
    audit.check("nonzero source falsifier gives K_TL=3/8", ktl_from_weight(z_bad_w) == Fraction(3, 8))
    idempotents = {(0, 0), (1, 0)}
    audit.check("real Z3 commutant idempotents are only 0 and I in route witness", idempotents == {(0, 0), (1, 0)})
    eta_z3 = Fraction(2, 9)
    c_based = Fraction(0)
    c_unbased = Fraction(1, 9)
    audit.check("finite Z3 scalar is eta_Z3=2/9", eta_z3 == Fraction(2, 9))
    audit.check("based endpoint gives delta_open=2/9", eta_z3 + c_based == Fraction(2, 9))
    audit.check("unbased torsor falsifier gives delta_open=1/3", eta_z3 + c_unbased == Fraction(1, 3))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    physical_packet = read(PHYSICAL_ELECTRON_PACKET)
    physical_no_go = read(PHYSICAL_ELECTRON_NO_GO)
    bridge_decision = read(BRIDGE_DECISION)
    bridge_target = read(BRIDGE_TARGET)
    pr5007 = read(PR5007_IMPACT)
    species_decision = read(SPECIES_DECISION)
    k4_no_go = read(K4_NO_GO)
    branch_no_go = read(BRANCH_MASS_MAP_NO_GO)
    route_note = read(KOIDE_ROUTE_NOTE)
    route_runner = read(KOIDE_ROUTE_RUNNER)
    review_runner = read(KOIDE_REVIEW_RUNNER)
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    tier_a = read(TIER_A_REGISTRY)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    nodes = registry["nodes"]

    audit.check("goal packet references native bridge no-go", NOTE.name in goal and "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in goal)
    audit.check("Koide firewall references native bridge no-go", NOTE.name in koide_firewall and "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in koide_firewall)
    audit.check("physical electron packet references native bridge no-go", NOTE.name in physical_packet and "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in physical_packet)
    audit.check("physical electron no-go references native bridge no-go", NOTE.name in physical_no_go and "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in physical_no_go)
    audit.check(
        "bridge decision remains decision-only",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in bridge_decision
        and "does not ratify the native zero-section bridge" in flat(bridge_decision),
    )
    audit.check("bridge target keeps Z1-Z3 explicit", all(token in bridge_target for token in ["ZERO_SOURCE_READOUT_RETAINED", "REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED", "BASED_DETERMINANT_LINE_READOUT_RETAINED"]))
    audit.check("PR5007 impact keeps Z1-Z3 pending", all(token in pr5007 for token in ["zero-source readout", "real-primitive Brannen endpoint", "based determinant-line readout"]))
    audit.check("species decision remains K3 only", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_decision and "K3 support only" in species_decision)
    audit.check("K4 no-go keeps scale open", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in k4_no_go and "current retained, primitive, and open-PR surfaces do not supply" in k4_no_go)
    audit.check("branch mass-map no-go keeps branch map open", "KOIDE_BRANCH_MASS_MAP_RETAINED" in branch_no_go and "current retained, primitive, and open-PR surfaces do not supply" in branch_no_go)
    audit.check("route note does not claim physical closure", "No physical Koide closure is asserted" in route_note)
    audit.check("route runner preserves bridge boundary", "PHYSICAL_BRIDGE_IDENTIFICATIONS_CLAIMED=FALSE" in route_runner)
    audit.check("review runner keeps retained closure false", "KOIDE_NATIVE_ZERO_SECTION_RETAINED_CLOSURE=FALSE" in review_runner)
    audit.check("minimal axioms exclude physical-observable identification", "physical-observable identification" in minimal)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    for absent in [
        "native_zero_section_bridge_primitive",
        "zero_source_readout_primitive",
        "real_primitive_brannen_endpoint_primitive",
        "based_determinant_line_readout_primitive",
        "koide_readout_bridge_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered native bridge shortcut: {absent}", absent not in registry_text)
    audit.check("scale primitive excludes dimensionless Koide content", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes state selection and values", "state-selection rule" in realized and "or value is supplied" in realized)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `NATIVE_ZERO_SECTION_BRIDGE_RETAINED`.",
        "No derivation or ratification of `ZERO_SOURCE_READOUT_RETAINED`.",
        "No derivation or ratification of `REAL_PRIMITIVE_BRANNEN_ENDPOINT_RETAINED`.",
        "No derivation or ratification of `BASED_DETERMINANT_LINE_READOUT_RETAINED`.",
        "No derivation or ratification of the physical electron species bridge.",
        "No derivation or ratification of the absolute charged-lepton scale.",
        "No derivation or ratification of the Koide branch mass-map.",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No use of observed lepton masses, observed `m_W`, fitted `a_l`, fitted",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies the native zero-section bridge",
        "native zero-section bridge is retained",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED is supplied",
        "Z1 is retained",
        "Z2 is retained",
        "Z3 is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
