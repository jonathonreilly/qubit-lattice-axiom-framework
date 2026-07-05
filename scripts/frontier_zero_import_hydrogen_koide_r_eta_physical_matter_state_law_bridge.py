#!/usr/bin/env python3
"""Verifier for the Koide R-eta physical matter-state law bridge lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
HW1_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
HW1_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PHYSICAL_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
SU2_MERGER = ROOT / "docs" / "INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md"
PER_SITE_SPIN = ROOT / "docs" / "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md"
CL31_EXTENSION = ROOT / "docs" / "CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md"
KS_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
GRASSMANN_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md"
CHIRALITY_PARITY = ROOT / "docs" / "STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"
CHIRALITY_TWO_GATES = ROOT / "docs" / "CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08.md"
REALIZATION_GATE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


FIXED_BRIDGE_INPUTS = {
    "PHYSICAL_MATTER_STATE_LAW_BRIDGE_TEXT_LOCK",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "NATIVE_D_SPIN_BLINDNESS_ACCEPTED",
    "KS_SCALARIZATION_SURFACE_ACCEPTED",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "NO_HW1_LOCUS_OR_CARRIER_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

ROUTE_INPUTS = {
    "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
    "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
}

CURRENT_SURFACE_INPUTS = FIXED_BRIDGE_INPUTS - {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}

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


def closes_matter_state_bridge(inputs: set[str]) -> bool:
    return FIXED_BRIDGE_INPUTS <= inputs and bool(ROUTE_INPUTS & inputs)


def closes_hw1(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


def closes_charged_carrier(inputs: set[str]) -> bool:
    return CHARGED_CARRIER_INPUTS <= inputs


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
        TARGET,
        DECISION,
        CURRENT,
        GOAL,
        KOIDE_FIREWALL,
        HW1_TARGET,
        HW1_DECISION,
        HW1_CURRENT,
        PHYSICAL_CARRIER_TARGET,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        SU2_MERGER,
        PER_SITE_SPIN,
        CL31_EXTENSION,
        KS_FORCING,
        GRASSMANN_FORCING,
        CHIRALITY_PARITY,
        CHIRALITY_TWO_GATES,
        REALIZATION_GATE,
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
        "Koide R-Eta Physical Matter-State Law Bridge Target Discriminator",
        "Koide R-Eta Physical Matter-State Law Bridge Ratification Decision Packet",
        "Koide R-Eta Physical Matter-State Law Bridge Current-Surface No-Go",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_TEXT_LOCK",
        "OPERATOR_FRAME_MERGER_ACCEPTED",
        "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
        "NATIVE_D_SPIN_BLINDNESS_ACCEPTED",
        "KS_SCALARIZATION_SURFACE_ACCEPTED",
        "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
        "NO_HW1_LOCUS_OR_CARRIER_CLOSURE_INPUT",
        "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED",
        "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md",
        "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md",
        "INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md",
        "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md",
        "CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md",
        "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md",
        "STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md",
        "STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
        "CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08.md",
        "merged `#5023`",
        "merged `#5024`",
        "open `#5014`",
        "open `#5017`",
        "open `#5018`",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Predicate checks")
    fixed = set(FIXED_BRIDGE_INPUTS)
    ks_route = fixed | {"KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED"}
    elementary_route = fixed | {"ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED"}
    both_routes = fixed | set(ROUTE_INPUTS)
    audit.check("KS route closes bridge contract", closes_matter_state_bridge(ks_route))
    audit.check("elementary route closes bridge contract", closes_matter_state_bridge(elementary_route))
    audit.check("both route certificates also close bridge contract", closes_matter_state_bridge(both_routes))
    audit.check("fixed inputs alone do not close bridge contract", not closes_matter_state_bridge(fixed))
    audit.check("current surface inputs do not close bridge contract", not closes_matter_state_bridge(CURRENT_SURFACE_INPUTS))

    for missing in sorted(FIXED_BRIDGE_INPUTS):
        reduced_ks = set(ks_route)
        reduced_ks.remove(missing)
        reduced_elementary = set(elementary_route)
        reduced_elementary.remove(missing)
        audit.check(
            f"bridge contract fails without fixed input {missing}",
            not closes_matter_state_bridge(reduced_ks) and not closes_matter_state_bridge(reduced_elementary),
        )

    bridge_universe = FIXED_BRIDGE_INPUTS | ROUTE_INPUTS
    accepted_subsets = [subset for subset in all_subsets(bridge_universe) if closes_matter_state_bridge(subset)]
    minimal_accepted = [
        subset
        for subset in accepted_subsets
        if not any(other < subset and closes_matter_state_bridge(other) for other in accepted_subsets)
    ]
    audit.check("only the two one-route minimal subsets close bridge", sorted(map(sorted, minimal_accepted)) == sorted(map(sorted, [ks_route, elementary_route])))

    consequence = {"PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED"}
    audit.check("bridge consequence alone does not close HW1", not closes_hw1(consequence))
    audit.check("bridge consequence alone does not close charged carrier theorem", not closes_charged_carrier(consequence))
    audit.check("bridge consequence alone does not close physical carrier context", not closes_physical_carrier(consequence))
    audit.check("bridge consequence alone does not close R-eta", not closes_r_eta(consequence))
    audit.check("bridge consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("bridge consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    hw1_target = read(HW1_TARGET)
    hw1_decision = read(HW1_DECISION)
    hw1_current = read(HW1_CURRENT)
    physical_carrier_target = read(PHYSICAL_CARRIER_TARGET)
    matter_attachment = read(MATTER_ATTACHMENT)
    carrier_attachment = read(CARRIER_ATTACHMENT)
    su2_merger = read(SU2_MERGER)
    per_site_spin = read(PER_SITE_SPIN)
    cl31_extension = read(CL31_EXTENSION)
    ks_forcing = read(KS_FORCING)
    grassmann_forcing = read(GRASSMANN_FORCING)
    chirality_parity = read(CHIRALITY_PARITY)
    chirality_two_gates = read(CHIRALITY_TWO_GATES)
    realization_gate = read(REALIZATION_GATE)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("HW1 target", hw1_target),
        ("HW1 decision", hw1_decision),
        ("HW1 current no-go", hw1_current),
    ]:
        audit.check(
            f"{label} references matter-state bridge lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in container,
        )

    audit.check("physical carrier target still keeps charged carrier downstream", "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED" in physical_carrier_target)
    matter_flat = flat(matter_attachment)
    carrier_flat = flat(carrier_attachment)
    su2_flat = flat(su2_merger)
    per_site_flat = flat(per_site_spin)
    cl31_flat = flat(cl31_extension)
    ks_flat = flat(ks_forcing)
    grassmann_flat = flat(grassmann_forcing)
    chirality_parity_flat = flat(chirality_parity)
    chirality_two_flat = flat(chirality_two_gates)
    realization_flat = flat(realization_gate)
    audit.check(
        "matter attachment names the forked bridge residual",
        "unless a KS-to-physical-state-law bridge or an elementary state-law theorem is supplied" in matter_flat
        and "physical matter-state law still requiring its own bridge statement" in matter_flat,
    )
    audit.check(
        "carrier attachment refutes spinor-module escape without closure",
        "does not prove the KS/Grassmann physical-state-law bridge" in carrier_flat
        and "operator-frame/Clifford data do not force the per-site `C^2` matter-state `j=1/2` law" in carrier_flat,
    )
    audit.check(
        "SU2 merger is operator-level",
        "The bounded theorem is therefore an operator-level identification" in su2_flat
        and "It does not introduce or approve any new axiom" in su2_flat,
    )
    audit.check(
        "per-site spin note withholds physical matter generator",
        "It does not, by itself, identify this action with the physical spin generator of every matter excitation" in per_site_flat,
    )
    audit.check(
        "CL31 extension does not transport state law onto per-site module",
        "not on the per-site site module" in cl31_flat
        and "per-site site module is `C^2`-valued" in cl31_flat,
    )
    audit.check(
        "KS forcing remains bounded on declared kinetic class",
        "declared kinetic class" in ks_forcing
        and "What is NOT claimed: that the kinetic class itself" in ks_flat,
    )
    audit.check(
        "Grassmann forcing remains bounded/conditional",
        "Claim type:** bounded_theorem" in grassmann_forcing
        and "GL(F)" in grassmann_forcing
        and "unconditional forcing FALSE" in grassmann_flat,
    )
    audit.check(
        "chirality parity remains narrow support",
        "does not prove the full staggered-Dirac realization gate" in chirality_parity_flat
        and "does not close the BZ-corner species-label bridge" in chirality_parity_flat,
    )
    audit.check(
        "chirality two-gates note separates generation chirality",
        "Dirac/spinor chirality and Koide/generation chirality are independent gates" in chirality_two_flat
        and "does not touch the firewalled `r=1/2`" in chirality_two_flat,
    )
    audit.check(
        "realization gate does not by itself close labeling/state law",
        "bounded synthesis closure" in realization_flat
        and "labeling-convention external premise" in realization_flat,
    )

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "physical_matter_state_law_primitive",
        "ks_physical_state_law_primitive",
        "elementary_physical_state_rotation_law_primitive",
        "hw1_physical_generation_locus_primitive",
        "physical_carrier_context_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open/merged PR and non-claim boundaries")
    current_flat = flat(current)
    pr_markers = [
        "`#5023` Koide W4 audit-readiness repairs | merged, audit success",
        "`#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | merged, audit success",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, audit success",
        "`#5014` record-formation front is the domain wall | open, audit success",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open, audit success",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open, audit success",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in pr_markers:
        audit.check(f"PR marker present: {marker}", flat(marker) in current_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "`ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "No derivation or ratification of",
        "`CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No claim that #5014, #5017, #5018, #5023, or #5024 supplies the physical",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This note ratifies physical matter-state law bridge",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED is supplied",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED is supplied",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED is supplied",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED is supplied",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED is supplied",
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
