#!/usr/bin/env python3
"""Verifier for the Koide R-eta HW1 carrier-realization chain packet."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_CARRIER_REALIZATION_CHAIN_REVIEW_PACKET_2026-07-05.md"
ROUTE_FORK = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_ROUTE_FORK_REVIEW_PACKET_2026-07-05.md"
MATTER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
MATTER_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
MATTER_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
HW1_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
HW1_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_CHARGED_LEPTON_CARRIER_REALIZATION_TARGET_DISCRIMINATOR_2026-07-05.md"
CARRIER_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_CHARGED_LEPTON_CARRIER_REALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CARRIER_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_CHARGED_LEPTON_CARRIER_REALIZATION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PHYSICAL_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PHYSICAL_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PR5030 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5032 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_COMMON_HW1_PR5032_CARRIER_IDENTIFICATION_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5011 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ETA_TWISTED_WALK_PR5011_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
W2 = ROOT / "docs" / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
REDUCED_OBSTRUCTION = ROOT / "docs" / "KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md"
GATE_COLLAPSE = ROOT / "docs" / "FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md"
TRACIAL = ROOT / "docs" / "KOIDE_TRACIAL_STANDARD_FORM_CARRIER_NARROW_NOTE_2026-06-02.md"
LOCUS = ROOT / "docs" / "KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


HW1_INPUTS = {
    "HW1_PHYSICAL_GENERATION_LOCUS_TEXT_LOCK",
    "MOMENTUM_TYPE_THEOREM_ACCEPTED",
    "STAGGERED_KS_REALIZATION_SURFACE_ACCEPTED",
    "K1_FLUX_SELECTOR_WITHIN_SURFACE_ACCEPTED",
    "HW1_C3_TRIPLET_ALGEBRA_ACCEPTED",
    "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED",
    "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
    "NO_SPECIES_LABEL_BIJECTION_INPUT",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CARRIER_INPUTS = {
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


def closes_hw1(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


def closes_carrier(inputs: set[str]) -> bool:
    return CARRIER_INPUTS <= inputs


def closes_physical_carrier(inputs: set[str]) -> bool:
    return PHYSICAL_CARRIER_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        PACKET,
        ROUTE_FORK,
        MATTER_TARGET,
        MATTER_DECISION,
        MATTER_CURRENT,
        HW1_TARGET,
        HW1_DECISION,
        HW1_CURRENT,
        CARRIER_TARGET,
        CARRIER_DECISION,
        CARRIER_CURRENT,
        PHYSICAL_TARGET,
        PHYSICAL_DECISION,
        PHYSICAL_CURRENT,
        PR5030,
        PR5032,
        PR5011,
        GOAL,
        KOIDE_FIREWALL,
        W2,
        REDUCED_OBSTRUCTION,
        GATE_COLLAPSE,
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

    packet = read(PACKET)
    packet_flat = flat(packet)

    section("Required packet content")
    required_phrases = [
        "HW1 Carrier-Realization Chain Review Packet",
        "support-only",
        "sequential chain, not a sibling-input bundle",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED",
        "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED",
        "FINITE_MULTISITE_PAULI_CARRIER_PROVENANCE_ACCEPTED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_ROUTE_FORK_REVIEW_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_CHARGED_LEPTON_CARRIER_REALIZATION_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_COMMON_HW1_PR5032_CARRIER_IDENTIFICATION_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "`#5030`",
        "`#5032`",
        "`#5033`",
        "`#5021`",
        "`#5014`, `#5017`, `#5018`",
        "Open or green PR metadata is not proof input",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Sequential predicate checks")
    audit.check("full HW1 locus contract closes HW1", closes_hw1(HW1_INPUTS))
    audit.check("full charged-carrier contract closes carrier theorem", closes_carrier(CARRIER_INPUTS))
    audit.check("full physical-carrier contract closes physical carrier context", closes_physical_carrier(PHYSICAL_CARRIER_INPUTS))

    for missing in [
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    ]:
        reduced = set(HW1_INPUTS)
        reduced.remove(missing)
        audit.check(f"HW1 locus fails without {missing}", not closes_hw1(reduced))

    for missing in [
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "FINITE_MULTISITE_PAULI_CARRIER_PROVENANCE_ACCEPTED",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    ]:
        reduced = set(CARRIER_INPUTS)
        reduced.remove(missing)
        audit.check(f"carrier realization fails without {missing}", not closes_carrier(reduced))

    reduced_physical = set(PHYSICAL_CARRIER_INPUTS)
    reduced_physical.remove("CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED")
    audit.check("physical carrier context fails without charged carrier theorem", not closes_physical_carrier(reduced_physical))

    audit.check(
        "physical matter-state bridge alone does not close HW1",
        not closes_hw1({"PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED"}),
    )
    audit.check(
        "HW1 consequence alone does not close charged carrier",
        not closes_carrier({"HW1_PHYSICAL_GENERATION_LOCUS_RETAINED"}),
    )
    audit.check(
        "charged carrier consequence alone does not close physical carrier context",
        not closes_physical_carrier({"CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED"}),
    )

    support_only = {
        "COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_ACCEPTED",
        "FINITE_MULTISITE_PAULI_CARRIER_PROVENANCE_ACCEPTED",
    }
    audit.check("PR support inputs alone do not close HW1", not closes_hw1(support_only))
    audit.check("PR support inputs alone do not close charged carrier", not closes_carrier(support_only))
    audit.check("PR support inputs alone do not close physical carrier", not closes_physical_carrier(support_only))

    section("Minimal closure checks")
    for universe, predicate, label in [
        (HW1_INPUTS, closes_hw1, "HW1"),
        (CARRIER_INPUTS, closes_carrier, "charged carrier"),
        (PHYSICAL_CARRIER_INPUTS, closes_physical_carrier, "physical carrier"),
    ]:
        accepted = [subset for subset in all_subsets(universe) if predicate(subset)]
        audit.check(f"only full {label} subset closes", accepted == [set(universe)])

    section("Downstream nonclosure checks")
    physical_consequence = {"PHYSICAL_CARRIER_CONTEXT_RETAINED"}
    audit.check("physical carrier context alone does not close R-eta", not closes_r_eta(physical_consequence))
    audit.check("physical carrier context alone does not close electron mass", not closes_electron_mass(physical_consequence))
    audit.check("physical carrier context alone does not close hydrogen", not closes_hydrogen(physical_consequence))
    audit.check(
        "full carrier chain consequences do not close hydrogen",
        not closes_hydrogen(
            {
                "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
                "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
                "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
                "PHYSICAL_CARRIER_CONTEXT_RETAINED",
            }
        ),
    )

    section("Authority, overview, and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    for label, container in [("goal packet", goal), ("Koide firewall", firewall)]:
        audit.check(
            f"{label} references chain review packet",
            PACKET.name in container
            and "carrier-realization chain review packet" in container
            and "review compression only" in container,
        )

    source_packets = {
        "route fork": read(ROUTE_FORK),
        "HW1 target": read(HW1_TARGET),
        "charged carrier target": read(CARRIER_TARGET),
        "physical carrier target": read(PHYSICAL_TARGET),
        "PR5030 impact": read(PR5030),
        "PR5032 impact": read(PR5032),
    }
    for label, container in source_packets.items():
        audit.check(f"{label} keeps hydrogen nonclosure visible", "hydrogen" in container and "No" in container)

    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "hw1_carrier_realization_chain_primitive",
        "physical_matter_state_law_primitive",
        "hw1_physical_generation_locus_primitive",
        "charged_lepton_carrier_realization_primitive",
        "physical_carrier_context_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open-PR and non-claim boundaries")
    for marker in [
        "`#5030` multisite Pauli finite-carrier provenance",
        "`#5032` common `hw=1` BZ-corner carrier identification",
        "`#5033` reflection-positivity runner scope cleanup",
        "`#5021` primitive-retirement review",
        "`#5014`, `#5017`, `#5018` chirality/domain-wall stack",
        "Open or green PR metadata is not proof input",
    ]:
        audit.check(f"PR marker present: {marker}", flat(marker) in packet_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "`CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "`FINITE_MULTISITE_PAULI_CARRIER_PROVENANCE_ACCEPTED`.",
        "No downstream retained-theorem verdict from open PR `#5030` or merged PR",
        "No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`.",
        "No derivation or ratification of h-class, h-unit, R-eta, K2 exactness",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This packet ratifies",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED is supplied",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED is supplied",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This packet claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in packet)

    audit.summary()


if __name__ == "__main__":
    main()
