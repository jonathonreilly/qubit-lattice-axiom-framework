#!/usr/bin/env python3
"""Verifier for the Koide R-eta charged-lepton carrier-realization lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_CHARGED_LEPTON_CARRIER_REALIZATION_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_CHARGED_LEPTON_CARRIER_REALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_CHARGED_LEPTON_CARRIER_REALIZATION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PHYSICAL_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_CARRIER_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PHYSICAL_CARRIER_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
HW1_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
HW1_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PR5030 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5032 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_COMMON_HW1_PR5032_CARRIER_IDENTIFICATION_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5011 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ETA_TWISTED_WALK_PR5011_IMPACT_DISCRIMINATOR_2026-07-05.md"
W2 = ROOT / "docs" / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
REDUCED_OBSTRUCTION = ROOT / "docs" / "KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md"
GATE_COLLAPSE = ROOT / "docs" / "FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md"
BARE_CARRIER = ROOT / "docs" / "FLAVOR_CARRIER_NOT_DERIVED_TWO_INPUTS_2026-05-31.md"
TRACIAL = ROOT / "docs" / "KOIDE_TRACIAL_STANDARD_FORM_CARRIER_NARROW_NOTE_2026-06-02.md"
LOCUS = ROOT / "docs" / "KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


CARRIER_REALIZATION_INPUTS = {
    "CHARGED_LEPTON_CARRIER_REALIZATION_TEXT_LOCK",
    "SUPPLIED_C3_CIRCULANT_CONTEXT_ACCEPTED",
    "RECORD_REGISTRABILITY_CONTEXT_ACCEPTED",
    "FINITE_MULTISITE_PAULI_CARRIER_PROVENANCE_ACCEPTED",
    "TRACIAL_STANDARD_FORM_CARRIER_SUPPORT_ACCEPTED",
    "REDUCED_CARRIER_OBSTRUCTION_ACCOUNTED",
    "CARRIER_GATE_COLLAPSE_MAP_ACCEPTED",
    "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_H_UNIT_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = {
    "CHARGED_LEPTON_CARRIER_REALIZATION_TEXT_LOCK",
    "SUPPLIED_C3_CIRCULANT_CONTEXT_ACCEPTED",
    "RECORD_REGISTRABILITY_CONTEXT_ACCEPTED",
    "TRACIAL_STANDARD_FORM_CARRIER_SUPPORT_ACCEPTED",
    "REDUCED_CARRIER_OBSTRUCTION_ACCOUNTED",
    "CARRIER_GATE_COLLAPSE_MAP_ACCEPTED",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_H_UNIT_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
}

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

HW1_INPUTS = {
    "HW1_PHYSICAL_GENERATION_LOCUS_TEXT_LOCK",
    "HW1_C3_TRIPLET_ALGEBRA_ACCEPTED",
    "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED",
    "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
    "NO_SPECIES_REDUCTION_OR_LABELING_INPUT",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_H_UNIT_OR_R_ETA_VALUE_INPUT",
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


def closes_carrier_realization(inputs: set[str]) -> bool:
    return CARRIER_REALIZATION_INPUTS <= inputs


def closes_physical_carrier(inputs: set[str]) -> bool:
    return PHYSICAL_CARRIER_INPUTS <= inputs


def closes_hw1(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


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
        PHYSICAL_CARRIER_TARGET,
        PHYSICAL_CARRIER_DECISION,
        PHYSICAL_CARRIER_CURRENT,
        HW1_TARGET,
        HW1_DECISION,
        HW1_CURRENT,
        R_ETA_TARGET,
        H_CLASS_TARGET,
        K2_TARGET,
        PHYSICAL_ELECTRON,
        PR5030,
        PR5032,
        PR5011,
        W2,
        REDUCED_OBSTRUCTION,
        GATE_COLLAPSE,
        BARE_CARRIER,
        TRACIAL,
        LOCUS,
        PRIMITIVE_REGISTRY,
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
        "Koide R-Eta Charged-Lepton Carrier Realization Target Discriminator",
        "Koide R-Eta Charged-Lepton Carrier Realization Ratification Decision Packet",
        "Koide R-Eta Charged-Lepton Carrier Realization Current-Surface No-Go",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
        "CHARGED_LEPTON_CARRIER_REALIZATION_TEXT_LOCK",
        "SUPPLIED_C3_CIRCULANT_CONTEXT_ACCEPTED",
        "RECORD_REGISTRABILITY_CONTEXT_ACCEPTED",
        "FINITE_MULTISITE_PAULI_CARRIER_PROVENANCE_ACCEPTED",
        "TRACIAL_STANDARD_FORM_CARRIER_SUPPORT_ACCEPTED",
        "REDUCED_CARRIER_OBSTRUCTION_ACCOUNTED",
        "CARRIER_GATE_COLLAPSE_MAP_ACCEPTED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
        "NO_H_UNIT_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_COMMON_HW1_PR5032_CARRIER_IDENTIFICATION_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md",
        "KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md",
        "FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md",
        "KOIDE_TRACIAL_STANDARD_FORM_CARRIER_NARROW_NOTE_2026-06-02.md",
        "KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01.md",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad carrier-realization retained claim fails; narrowed child",
        "broad no-route claim fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Predicate checks")
    full_inputs = set(CARRIER_REALIZATION_INPUTS)
    audit.check("full carrier-realization contract accepts theorem", closes_carrier_realization(full_inputs))
    for missing in sorted(CARRIER_REALIZATION_INPUTS):
        reduced = set(CARRIER_REALIZATION_INPUTS)
        reduced.remove(missing)
        audit.check(f"carrier-realization theorem fails without {missing}", not closes_carrier_realization(reduced))
    accepted_subsets = [subset for subset in all_subsets(CARRIER_REALIZATION_INPUTS) if closes_carrier_realization(subset)]
    audit.check("only full carrier-realization subset closes theorem", accepted_subsets == [full_inputs])
    audit.check("current surface inputs do not close carrier realization", not closes_carrier_realization(CURRENT_SURFACE_INPUTS))

    consequence = {"CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED"}
    audit.check("carrier theorem alone does not close parent carrier context", not closes_physical_carrier(consequence))
    audit.check("carrier theorem alone does not close hw1", not closes_hw1(consequence))
    audit.check("carrier theorem alone does not close R-eta", not closes_r_eta(consequence))
    audit.check("carrier theorem alone does not close K2", not closes_k2(consequence))
    audit.check("carrier theorem alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("carrier theorem alone does not close hydrogen", not closes_hydrogen(consequence))

    parent_without_child = set(PHYSICAL_CARRIER_INPUTS) - {"CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED"}
    audit.check("parent carrier context fails without child theorem", not closes_physical_carrier(parent_without_child))
    audit.check(
        "child theorem plus full parent inputs closes parent predicate",
        closes_physical_carrier(parent_without_child | consequence),
    )

    section("Wiring and authority boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    physical_target = read(PHYSICAL_CARRIER_TARGET)
    physical_decision = read(PHYSICAL_CARRIER_DECISION)
    physical_current = read(PHYSICAL_CARRIER_CURRENT)
    hw1_target = read(HW1_TARGET)
    hw1_decision = read(HW1_DECISION)
    hw1_current = read(HW1_CURRENT)
    r_eta_target = read(R_ETA_TARGET)
    h_class_target = read(H_CLASS_TARGET)
    k2_target = read(K2_TARGET)
    physical_electron = read(PHYSICAL_ELECTRON)
    pr5030 = read(PR5030)
    pr5032 = read(PR5032)
    pr5011 = read(PR5011)
    w2 = read(W2)
    reduced_obstruction = read(REDUCED_OBSTRUCTION)
    gate_collapse = read(GATE_COLLAPSE)
    bare_carrier = read(BARE_CARRIER)
    tracial = read(TRACIAL)
    locus = read(LOCUS)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("physical carrier target", physical_target),
        ("physical carrier decision", physical_decision),
        ("physical carrier current no-go", physical_current),
        ("hw1 target", hw1_target),
        ("hw1 decision", hw1_decision),
        ("hw1 current no-go", hw1_current),
    ]:
        audit.check(
            f"{label} references charged-carrier realization lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED" in container,
        )

    audit.check("R-eta target keeps physical carrier context as parent", "PHYSICAL_CARRIER_CONTEXT_RETAINED" in r_eta_target)
    audit.check("h-class target keeps physical carrier context as parent", "PHYSICAL_CARRIER_CONTEXT_RETAINED" in h_class_target)
    audit.check("K2 target remains downstream", "K2_R_ETA_EXACTNESS_RETAINED" in k2_target)
    audit.check("physical electron packet remains downstream", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron)

    audit.check("PR5030 remains support-only", "finite multisite Pauli carrier-provenance support" in pr5030 and "No derivation or ratification of `CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`" in pr5030)
    audit.check("PR5032 remains support-only", "common finite-carrier identification support" in pr5032 and "No derivation or ratification of `CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`" in pr5032)
    audit.check("PR5011 remains route context only", "eta-twisted covariant-walk context" in flat(pr5011))
    audit.check("W2 closes supplied context only", "closes only piece 1" in w2 and "physical charged-lepton carrier must be shown" in w2)
    audit.check("reduced obstruction keeps physical bridge open", "missing bridge" in reduced_obstruction and "physical charged-lepton observable carrier/readout" in reduced_obstruction)
    audit.check("gate-collapse map is not retained closure", "gate-collapse map" in gate_collapse and "not a closure" in gate_collapse)
    audit.check("bare-character note leaves carrier open", "not proved: the physical carrier" in bare_carrier)
    audit.check("tracial note is supplied-carrier support", "supplied carrier" in tracial and "framework-native physical selection" in flat(tracial))
    audit.check("carrier-locus note keeps matter operator import", "matter operator import" in locus and "physical choice" in locus)

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "charged_lepton_carrier_realization_primitive",
        "finite_multisite_pauli_carrier_provenance_primitive",
        "hw1_physical_generation_locus_primitive",
        "physical_carrier_context_primitive",
        "single_fixed_point_readout_primitive",
        "r_eta_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "normalization", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5030` multisite Pauli finite-carrier provenance | open",
        "`#5032` common `hw=1` BZ-corner carrier identification | merged",
        "`#5011` eta twisted walk family runner | open",
        "`#5014`/`#5017`/`#5018` chirality/domain-wall stack | open",
        "`#5021` primitive-retirement review | open draft",
        "Clean/dirty/check labels and queue position are review metadata",
    ]
    current_flat = flat(current)
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in current_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "No derivation or ratification of `FINITE_MULTISITE_PAULI_CARRIER_PROVENANCE_ACCEPTED`.",
        "No adoption, landing, or audit verdict claim for PR `#5030`; merged PR `#5032` remains support-only.",
        "No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`.",
        "No derivation or ratification of h-class, h-unit, R-eta, K2, electron mass,",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", flat(phrase) in packet_flat)

    forbidden = [
        "This note ratifies charged-lepton carrier realization",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED is supplied",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED is supplied",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
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
