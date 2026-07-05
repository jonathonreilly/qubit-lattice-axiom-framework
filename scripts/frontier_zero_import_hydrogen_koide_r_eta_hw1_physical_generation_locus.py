#!/usr/bin/env python3
"""Verifier for the Koide R-eta hw1 physical generation-locus lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PHYSICAL_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_CARRIER_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PHYSICAL_CARRIER_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
MOMENTUM_TYPE = ROOT / "docs" / "FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md"
MOMENTUM_PARENT = ROOT / "docs" / "FLAVOR_CARRIER_FROM_AXIOMS_MOMENTUM_FORCED_2026-05-31.md"
REALIZATION_GATE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
KINETIC_CLASS = ROOT / "docs" / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
P_FLUX = ROOT / "docs" / "P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md"
KS_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
CHIRALITY_PARITY = ROOT / "docs" / "STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"
HAMMING_ORBIT = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md"
SPECIES_REDUCTION = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
DELTA_RANK2 = ROOT / "docs" / "KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md"
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

CURRENT_SURFACE_INPUTS = HW1_INPUTS - {
    "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CHARGED_CARRIER_INPUTS = {
    "CHARGED_LEPTON_CARRIER_REALIZATION_TEXT_LOCK",
    "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
    "SUPPLIED_ACPHILAMBDA_R_ETA_CONTEXT_LOCK",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
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


def closes_hw1_locus(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


def closes_charged_carrier(inputs: set[str]) -> bool:
    return CHARGED_CARRIER_INPUTS <= inputs


def closes_physical_carrier(inputs: set[str]) -> bool:
    return PHYSICAL_CARRIER_INPUTS <= inputs


def closes_h_class(inputs: set[str]) -> bool:
    return H_CLASS_INPUTS <= inputs


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
        TARGET,
        DECISION,
        CURRENT,
        GOAL,
        KOIDE_FIREWALL,
        PHYSICAL_CARRIER_TARGET,
        PHYSICAL_CARRIER_DECISION,
        PHYSICAL_CARRIER_CURRENT,
        H_CLASS_TARGET,
        R_ETA_TARGET,
        MOMENTUM_TYPE,
        MOMENTUM_PARENT,
        REALIZATION_GATE,
        KINETIC_CLASS,
        P_FLUX,
        KS_FORCING,
        CHIRALITY_PARITY,
        HAMMING_ORBIT,
        SPECIES_REDUCTION,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        DELTA_RANK2,
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
        "Koide R-Eta hw1 Physical Generation Locus Target Discriminator",
        "Koide R-Eta hw1 Physical Generation Locus Ratification Decision Packet",
        "Koide R-Eta hw1 Physical Generation Locus Current-Surface No-Go",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_TEXT_LOCK",
        "MOMENTUM_TYPE_THEOREM_ACCEPTED",
        "STAGGERED_KS_REALIZATION_SURFACE_ACCEPTED",
        "K1_FLUX_SELECTOR_WITHIN_SURFACE_ACCEPTED",
        "HW1_C3_TRIPLET_ALGEBRA_ACCEPTED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "NO_SPECIES_LABEL_BIJECTION_INPUT",
        "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
        "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED",
        "FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
        "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md",
        "P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md",
        "STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
        "STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md",
        "STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md",
        "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md",
        "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md",
        "KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md",
        "open `#5014`",
        "open `#5017`",
        "open `#5018`",
        "merged `#5023`",
        "open `#5024`",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Predicate checks")
    full_inputs = set(HW1_INPUTS)
    audit.check("full hw1 locus contract accepts handoff", closes_hw1_locus(full_inputs))
    for missing in sorted(HW1_INPUTS):
        reduced = set(HW1_INPUTS)
        reduced.remove(missing)
        audit.check(f"hw1 locus handoff fails without {missing}", not closes_hw1_locus(reduced))
    accepted_subsets = [subset for subset in all_subsets(HW1_INPUTS) if closes_hw1_locus(subset)]
    audit.check("only full hw1 subset closes handoff", accepted_subsets == [full_inputs])
    audit.check("current surface inputs do not close hw1 locus", not closes_hw1_locus(CURRENT_SURFACE_INPUTS))

    consequence = {"HW1_PHYSICAL_GENERATION_LOCUS_RETAINED"}
    audit.check("hw1 consequence alone does not close charged carrier theorem", not closes_charged_carrier(consequence))
    audit.check("hw1 consequence alone does not close physical carrier context", not closes_physical_carrier(consequence))
    audit.check("hw1 consequence alone does not close h-class", not closes_h_class(consequence))
    audit.check("hw1 consequence alone does not close R-eta", not closes_r_eta(consequence))
    audit.check("hw1 consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("hw1 consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    physical_carrier_target = read(PHYSICAL_CARRIER_TARGET)
    physical_carrier_decision = read(PHYSICAL_CARRIER_DECISION)
    physical_carrier_current = read(PHYSICAL_CARRIER_CURRENT)
    h_class_target = read(H_CLASS_TARGET)
    r_eta_target = read(R_ETA_TARGET)
    momentum_type = read(MOMENTUM_TYPE)
    momentum_parent = read(MOMENTUM_PARENT)
    realization_gate = read(REALIZATION_GATE)
    kinetic_class = read(KINETIC_CLASS)
    p_flux = read(P_FLUX)
    ks_forcing = read(KS_FORCING)
    chirality_parity = read(CHIRALITY_PARITY)
    hamming_orbit = read(HAMMING_ORBIT)
    species_reduction = read(SPECIES_REDUCTION)
    matter_attachment = read(MATTER_ATTACHMENT)
    carrier_attachment = read(CARRIER_ATTACHMENT)
    delta_rank2 = read(DELTA_RANK2)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("physical carrier target", physical_carrier_target),
        ("physical carrier decision", physical_carrier_decision),
        ("physical carrier current no-go", physical_carrier_current),
    ]:
        audit.check(
            f"{label} references hw1 locus lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED" in container,
        )

    audit.check("h-class remains downstream", "R_ETA_H_CLASS_RETAINED" in h_class_target)
    audit.check("R-eta remains downstream", "R_ETA_READOUT_IDENTIFICATION_RETAINED" in r_eta_target)
    momentum_type_flat = flat(momentum_type)
    ks_forcing_flat = flat(ks_forcing)
    species_reduction_flat = flat(species_reduction)
    matter_attachment_flat = flat(matter_attachment)
    audit.check(
        "momentum type proves type only",
        "flavor-separating label resolution is supplied by the momentum/BZ factor" in momentum_type_flat
        and "This split proves only item 1. It does not claim that the physical generation locus is forced to be `hw=1`." in momentum_type_flat,
    )
    audit.check("momentum parent leaves other half open", "Half of the carrier problem" in momentum_parent and "physical `hw=1` locus" in momentum_parent)
    audit.check("realization gate names P-FLUX residual", "P-FLUX selector" in realization_gate and "hw=1 triplet carrying an exact irreducible" in realization_gate)
    audit.check("kinetic class keeps K1 selector scoped", "K1" in kinetic_class and "K0" in kinetic_class and "B-BIT" in kinetic_class)
    audit.check("P-FLUX is within-surface selection", "B-BIT retired within the surface" in p_flux and "within-surface selection" in p_flux)
    audit.check(
        "KS forcing remains bounded",
        "declared kinetic class" in ks_forcing
        and "What is NOT claimed: that the kinetic class itself" in ks_forcing_flat,
    )
    audit.check("chirality parity does not close species bridge", "does not close the BZ-corner species-label bridge" in chirality_parity)
    audit.check("Hamming orbit excludes physical species reading", "physical-species reading" in hamming_orbit and "out of scope" in hamming_orbit)
    audit.check(
        "species reduction keeps realization open",
        "taste-count factor is **not** forced" in species_reduction_flat
        and "Does **not** assert that the three physical SM matter generations" in species_reduction_flat,
    )
    audit.check(
        "matter attachment keeps state-law bridge open",
        "physical matter-state law still requiring its own bridge statement" in matter_attachment_flat
        and "physical matter-state spinor-law bridge" in matter_attachment_flat,
    )
    audit.check("carrier attachment keeps KS physical-state-law open", "does not prove the KS/Grassmann physical-state-law bridge" in flat(carrier_attachment))
    audit.check("delta rank2 keeps physical carrier open", "edge sector = physical carrier" in delta_rank2 and "open" in delta_rank2)

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "hw1_physical_generation_locus_primitive",
        "physical_matter_state_law_primitive",
        "charged_lepton_carrier_primitive",
        "physical_carrier_context_primitive",
        "single_fixed_point_readout_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    current_flat = flat(current)
    open_markers = [
        "`#5014` record-formation front is the domain wall | open, audit success",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open, audit success",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open, audit success",
        "`#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | open, audit in progress after latest refresh",
        "`#5023` Koide W4 audit-readiness repairs | merged, audit success",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in current_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "No derivation or ratification of `CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`.",
        "No claim that #5014, #5017, #5018, #5023, or #5024 supplies the physical",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This note ratifies hw1 physical generation locus",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED is supplied",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED is supplied",
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED is supplied",
        "R_ETA_H_CLASS_RETAINED is supplied",
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
