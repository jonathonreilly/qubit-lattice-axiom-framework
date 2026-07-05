#!/usr/bin/env python3
"""Verifier for the Koide R-eta physical carrier-context lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
R_ETA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
H_CLASS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_CLASS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_UNIT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
W2 = ROOT / "docs" / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
REDUCED_OBSTRUCTION = ROOT / "docs" / "KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md"
GATE_COLLAPSE = ROOT / "docs" / "FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md"
BARE_CARRIER = ROOT / "docs" / "FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31.md"
TRACIAL = ROOT / "docs" / "KOIDE_TRACIAL_STANDARD_FORM_CARRIER_NARROW_NOTE_2026-06-02.md"
LOCUS = ROOT / "docs" / "KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01.md"
CHIRALITY = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


PHYSICAL_CARRIER_INPUTS = {
    "PHYSICAL_CARRIER_CONTEXT_TEXT_LOCK",
    "SUPPLIED_C3_CIRCULANT_CONTEXT_ACCEPTED",
    "RECORD_REGISTRABILITY_CONTEXT_ACCEPTED",
    "REDUCED_CARRIER_OBSTRUCTION_ACCOUNTED",
    "CARRIER_GATE_COLLAPSE_MAP_ACCEPTED",
    "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_H_UNIT_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = {
    "PHYSICAL_CARRIER_CONTEXT_TEXT_LOCK",
    "SUPPLIED_C3_CIRCULANT_CONTEXT_ACCEPTED",
    "RECORD_REGISTRABILITY_CONTEXT_ACCEPTED",
    "REDUCED_CARRIER_OBSTRUCTION_ACCOUNTED",
    "CARRIER_GATE_COLLAPSE_MAP_ACCEPTED",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_H_UNIT_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
}

H_CLASS_INPUTS = {
    "R_ETA_H_CLASS_TEXT_LOCK",
    "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
    "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
    "SUPPLIED_CONTEXT_REGISTRABILITY_ACCEPTED",
    "AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_RETAINED",
    "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED",
    "NO_H_UNIT_OR_RADIAN_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

R_ETA_INPUTS = {
    "R_ETA_RETIREMENT_TEXT_LOCK",
    "FORM_LAYER_AND_K_ORBIT_AUTHORITY_ACCEPTED",
    "FINITE_FIXED_LOCUS_ARITHMETIC_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_RETAINED",
    "R_ETA_H_CLASS_RETAINED",
    "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
    "NO_R_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

K2_INPUTS = {
    "K2_EXACTNESS_TEXT_LOCK",
    "REGISTERED_PHI_VALUE_FACE_ACCEPTED",
    "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
    "RADIAN_READOUT_LICENSE_RETAINED",
    "FOLD_AND_BRANCH_DOMAIN_LOCK",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

ELECTRON_MASS_INPUTS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
}

HYDROGEN_INPUTS = ELECTRON_MASS_INPUTS | {
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
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


def closes_physical_carrier(inputs: set[str]) -> bool:
    return PHYSICAL_CARRIER_INPUTS <= inputs


def closes_h_class(inputs: set[str]) -> bool:
    return H_CLASS_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


def closes_k2(inputs: set[str]) -> bool:
    return K2_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        TARGET,
        DECISION,
        CURRENT,
        GOAL,
        KOIDE_FIREWALL,
        R_ETA_TARGET,
        R_ETA_DECISION,
        R_ETA_CURRENT,
        H_CLASS_TARGET,
        H_CLASS_DECISION,
        H_CLASS_CURRENT,
        H_UNIT_TARGET,
        K2_TARGET,
        PHYSICAL_ELECTRON,
        W2,
        REDUCED_OBSTRUCTION,
        GATE_COLLAPSE,
        BARE_CARRIER,
        TRACIAL,
        LOCUS,
        CHIRALITY,
        PRIMITIVE_REGISTRY,
        TIER_A_REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    target = read(TARGET)
    decision = read(DECISION)
    current = read(CURRENT)
    packet = "\n".join([target, decision, current])
    packet_flat = flat(packet)

    section("Required packet content")
    required_phrases = [
        "Koide R-Eta Physical Carrier Context Target Discriminator",
        "Koide R-Eta Physical Carrier Context Ratification Decision Packet",
        "Koide R-Eta Physical Carrier Context Current-Surface No-Go",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED",
        "PHYSICAL_CARRIER_CONTEXT_TEXT_LOCK",
        "SUPPLIED_C3_CIRCULANT_CONTEXT_ACCEPTED",
        "RECORD_REGISTRABILITY_CONTEXT_ACCEPTED",
        "REDUCED_CARRIER_OBSTRUCTION_ACCOUNTED",
        "CARRIER_GATE_COLLAPSE_MAP_ACCEPTED",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
        "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
        "NO_H_UNIT_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md",
        "KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md",
        "FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md",
        "FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31.md",
        "KOIDE_TRACIAL_STANDARD_FORM_CARRIER_NARROW_NOTE_2026-06-02.md",
        "KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01.md",
        "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md",
        "merged `#5023` Koide W4 audit-readiness repairs",
        "merged `#5024` Koide W4 gate-note premise minimization",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad physical-carrier current-surface no-go fails; narrowed",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Predicate checks")
    full_inputs = set(PHYSICAL_CARRIER_INPUTS)
    audit.check("full carrier-context contract accepts handoff", closes_physical_carrier(full_inputs))
    for missing in sorted(PHYSICAL_CARRIER_INPUTS):
        reduced = set(PHYSICAL_CARRIER_INPUTS)
        reduced.remove(missing)
        audit.check(f"carrier-context handoff fails without {missing}", not closes_physical_carrier(reduced))
    accepted_subsets = [subset for subset in all_subsets(PHYSICAL_CARRIER_INPUTS) if closes_physical_carrier(subset)]
    audit.check("only full carrier-context subset closes handoff", accepted_subsets == [full_inputs])
    audit.check("current surface inputs do not close carrier context", not closes_physical_carrier(CURRENT_SURFACE_INPUTS))

    consequence = {"PHYSICAL_CARRIER_CONTEXT_RETAINED"}
    audit.check("carrier consequence alone does not close h-class", not closes_h_class(consequence))
    audit.check("carrier consequence alone does not close R-eta", not closes_r_eta(consequence))
    audit.check("carrier consequence alone does not close K2 exactness", not closes_k2(consequence))
    audit.check("carrier consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("carrier consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    r_eta_target = read(R_ETA_TARGET)
    r_eta_decision = read(R_ETA_DECISION)
    r_eta_current = read(R_ETA_CURRENT)
    h_class_target = read(H_CLASS_TARGET)
    h_class_decision = read(H_CLASS_DECISION)
    h_class_current = read(H_CLASS_CURRENT)
    h_unit_target = read(H_UNIT_TARGET)
    k2_target = read(K2_TARGET)
    physical_electron = read(PHYSICAL_ELECTRON)
    w2 = read(W2)
    reduced_obstruction = read(REDUCED_OBSTRUCTION)
    gate_collapse = read(GATE_COLLAPSE)
    bare_carrier = read(BARE_CARRIER)
    tracial = read(TRACIAL)
    locus = read(LOCUS)
    chirality = read(CHIRALITY)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a = read(TIER_A_REGISTRY)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("R-eta target", r_eta_target),
        ("R-eta decision", r_eta_decision),
        ("R-eta current no-go", r_eta_current),
        ("h-class target", h_class_target),
        ("h-class decision", h_class_decision),
        ("h-class current no-go", h_class_current),
    ]:
        audit.check(
            f"{label} references carrier-context lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "PHYSICAL_CARRIER_CONTEXT_RETAINED" in container,
        )

    audit.check("h-unit target remains independent", "PHYSICAL_CARRIER_CONTEXT_RETAINED" in h_unit_target and "not physical carrier realization" in h_unit_target)
    audit.check("K2 target remains downstream", "K2_R_ETA_EXACTNESS_RETAINED" in k2_target)
    audit.check("physical electron packet remains downstream", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron)

    audit.check("W2 closes supplied context only", "closes only piece 1" in w2 and "physical charged-lepton carrier must be shown" in w2)
    audit.check("reduced obstruction keeps physical bridge open", "missing bridge" in reduced_obstruction and "physical charged-lepton observable carrier/readout" in reduced_obstruction)
    audit.check("gate-collapse map is not retained closure", "gate-collapse map" in gate_collapse and "not a closure" in gate_collapse)
    audit.check("bare-character note leaves carrier open", "not proved: the physical carrier" in bare_carrier)
    audit.check("tracial note is supplied-carrier support", "supplied carrier" in tracial and "framework-native physical selection" in flat(tracial))
    audit.check("carrier-locus note keeps matter operator import", "matter operator import" in locus and "physical choice" in locus)
    audit.check("chirality note keeps physical-state-law bridge open", "does not derive the KS/Grassmann physical-state-law bridge" in flat(chirality) or "does not prove the KS/Grassmann physical-state-law bridge" in flat(chirality))
    audit.check("Tier-A registry still names AC/R-eta admissions", "AC_phi_lambda" in tier_a and "R-eta" in tier_a)

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "physical_carrier_context_primitive",
        "charged_lepton_carrier_primitive",
        "r_eta_carrier_context_primitive",
        "single_fixed_point_readout_primitive",
        "r_eta_h_class_primitive",
        "r_eta_h_unit_identity_radian_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "normalization", "value", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "`#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | merged, audit success",
        "`#5023` Koide W4 audit-readiness repairs | merged, audit success",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, audit success",
        "`#5014`/`#5017`/`#5018` chirality/domain-wall stack | open, audit success",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "clean/dirty/check labels are not proof inputs",
    ]
    current_flat = flat(current)
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in current_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation of `delta = 2/9` as a retained physical phase.",
        "No claim that #5023 or #5024 supplies the physical carrier-context theorem.",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This note ratifies physical carrier context",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED is supplied",
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED is supplied",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in packet)

    audit.summary()


if __name__ == "__main__":
    main()
