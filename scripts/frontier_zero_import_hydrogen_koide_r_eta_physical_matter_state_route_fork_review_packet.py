#!/usr/bin/env python3
"""Verifier for the Koide R-eta physical matter-state route-fork packet."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_ROUTE_FORK_REVIEW_PACKET_2026-07-05.md"
PARENT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
PARENT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PARENT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
KS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_TWO_INPUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_STATE_LAW_TWO_INPUT_REVIEW_PACKET_2026-07-05.md"
KS_SIGMA_P_BUNDLE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SIGMA_P_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md"
KS_SELECTOR_BUNDLE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_SELECTOR_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md"
ELEMENTARY_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
ELEMENTARY_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
ELEMENTARY_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SELECTOR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md"
SELECTOR_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SELECTOR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
FIELD_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_TARGET_DISCRIMINATOR_2026-07-05.md"
FIELD_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
FIELD_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
MATTER_STATE_CHIRALITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_MATTER_STATE_CHIRALITY_DOMAIN_WALL_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5030 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
MATTER_ATTACHMENT = ROOT / "docs" / "KOIDE_MATTER_ATTACHMENT_REDUCES_TO_KS_AUDIT_NARROW_THEOREM_NOTE_2026-06-02.md"
CARRIER_ATTACHMENT = ROOT / "docs" / "CARRIER_ATTACHMENT_CONSOLIDATES_TO_RECURRING_CHIRALITY_GATE_SHARPENING_NOTE_2026-06-06.md"
SU2_MERGER = ROOT / "docs" / "INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md"
PER_SITE_SPIN = ROOT / "docs" / "PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md"
CL31_EXTENSION = ROOT / "docs" / "CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md"
BOOST_NO_GO = ROOT / "docs" / "QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md"
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

FIELD_INPUTS = {
    "FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_TEXT_LOCK",
    "MATTER_ATTACHMENT_PRIVILEGE_RESIDUAL_ACCEPTED",
    "OPERATOR_FRAME_CENTER_BLINDNESS_ACCEPTED",
    "PER_SITE_PAULI_MODULE_SUPPORT_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
    "BOOST_ACTION_FAITH_ANALOGY_ACCEPTED",
    "NATIVE_D_SPIN_BLINDNESS_ACCEPTED",
    "SCALAR_SIGN_COMPENSATOR_BOUNDARY_ACCEPTED",
    "FINITE_SU2_DOUBLE_COVER_ACTION_CHECK",
    "FINITE_ADJOINT_CENTER_BLINDNESS_CHECK",
    "FINITE_TRIVIAL_SCALAR_LIFT_COUNTERMODEL_CHECK",
    "FINITE_SCALAR_SIGN_COMPENSATOR_BOUNDARY_CHECK",
    "FINITE_SPIN_LIFT_VS_SCALAR_COMPENSATOR_CHECK",
    "NO_ELEMENTARY_SELECTOR_INPUT",
    "NO_ELEMENTARY_ROTATION_LAW_INPUT",
    "NO_KS_ROUTE_OR_STAGGERED_KERNEL_INPUT",
    "NO_PHYSICAL_MATTER_STATE_BRIDGE_INPUT",
    "NO_HW1_OR_CARRIER_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

SELECTOR_INPUTS = {
    "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_TEXT_LOCK",
    "MATTER_ATTACHMENT_ROUTE_A_ACCEPTED",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "PER_SITE_PAULI_SPIN_HALF_MODULE_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
    "BOOST_ACTION_FAITH_ANALOGY_ACCEPTED",
    "NATIVE_D_SPIN_BLINDNESS_ACCEPTED",
    "SCALAR_SIGN_COMPENSATOR_BOUNDARY_ACCEPTED",
    "FINITE_SU2_DOUBLE_COVER_ACTION_CHECK",
    "FINITE_ADJOINT_CENTER_BLINDNESS_CHECK",
    "FINITE_TRIVIAL_SCALAR_LIFT_COUNTERMODEL_CHECK",
    "FINITE_SPIN_LIFT_VS_SCALAR_COMPENSATOR_CHECK",
    "FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RETAINED",
    "NO_KS_ROUTE_OR_STAGGERED_KERNEL_INPUT",
    "NO_ELEMENTARY_ROTATION_LAW_INPUT",
    "NO_PHYSICAL_MATTER_STATE_BRIDGE_INPUT",
    "NO_HW1_OR_CARRIER_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

ELEMENTARY_INPUTS = {
    "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_TEXT_LOCK",
    "MATTER_ATTACHMENT_ELEMENTARY_ROUTE_ACCEPTED",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "PER_SITE_PAULI_SPIN_HALF_MODULE_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "CL31_EXTENSION_MODULE_BOUNDARY_ACCEPTED",
    "BOOST_ACTION_FAITH_ANALOGY_ACCEPTED",
    "FINITE_SU2_DOUBLE_COVER_ACTION_CHECK",
    "FINITE_ADJOINT_CENTER_BLINDNESS_CHECK",
    "FINITE_TRIVIAL_STATE_LIFT_COUNTERMODEL_CHECK",
    "FINITE_FAITHFUL_SPINOR_STATE_LAW_CHECK",
    "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED",
    "NO_KS_ROUTE_THEOREM_INPUT",
    "NO_PHYSICAL_MATTER_STATE_BRIDGE_INPUT",
    "NO_HW1_OR_CARRIER_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

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


def closes_bridge(inputs: set[str]) -> bool:
    return FIXED_BRIDGE_INPUTS <= inputs and bool(ROUTE_INPUTS & inputs)


def closes_field_principle(inputs: set[str]) -> bool:
    return FIELD_INPUTS <= inputs


def closes_selector(inputs: set[str]) -> bool:
    return SELECTOR_INPUTS <= inputs


def closes_elementary_route(inputs: set[str]) -> bool:
    return ELEMENTARY_INPUTS <= inputs


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
        PACKET,
        PARENT_TARGET,
        PARENT_DECISION,
        PARENT_CURRENT,
        KS_TARGET,
        KS_DECISION,
        KS_CURRENT,
        KS_TWO_INPUT,
        KS_SIGMA_P_BUNDLE,
        KS_SELECTOR_BUNDLE,
        ELEMENTARY_TARGET,
        ELEMENTARY_DECISION,
        ELEMENTARY_CURRENT,
        SELECTOR_TARGET,
        SELECTOR_DECISION,
        SELECTOR_CURRENT,
        FIELD_TARGET,
        FIELD_DECISION,
        FIELD_CURRENT,
        MATTER_STATE_CHIRALITY,
        PR5030,
        GOAL,
        KOIDE_FIREWALL,
        HW1_TARGET,
        PHYSICAL_CARRIER_TARGET,
        MATTER_ATTACHMENT,
        CARRIER_ATTACHMENT,
        SU2_MERGER,
        PER_SITE_SPIN,
        CL31_EXTENSION,
        BOOST_NO_GO,
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
        "Physical Matter-State Route-Fork Review Packet",
        "support-only",
        "route fork",
        "These are alternatives, not simultaneous parent requirements",
        "direct elementary route",
        "FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RETAINED",
        "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_STATE_ATTACHMENT_SELECTOR_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_STATE_LAW_TWO_INPUT_REVIEW_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_SIGMA_P_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FAITHFUL_KS_SELECTOR_TWO_HANDLE_REVIEW_PACKET_2026-07-05.md",
        "`#5033`",
        "`#5030`",
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

    section("Route-fork predicate checks")
    fixed = set(FIXED_BRIDGE_INPUTS)
    ks_parent_route = fixed | {"KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED"}
    elementary_parent_route = fixed | {"ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED"}
    both_routes = fixed | set(ROUTE_INPUTS)
    audit.check("KS route theorem closes parent bridge route slot", closes_bridge(ks_parent_route))
    audit.check("elementary route theorem closes parent bridge route slot", closes_bridge(elementary_parent_route))
    audit.check("both route theorem handles also close parent bridge route slot", closes_bridge(both_routes))
    audit.check("fixed bridge inputs alone do not close route fork", not closes_bridge(fixed))
    audit.check(
        "KS route theorem alone does not close parent bridge",
        not closes_bridge({"KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED"}),
    )
    audit.check(
        "elementary route theorem alone does not close parent bridge",
        not closes_bridge({"ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED"}),
    )
    audit.check(
        "KS route bypasses elementary chain at the parent route slot",
        closes_bridge(ks_parent_route)
        and not ({"ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED", "FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RETAINED"} & ks_parent_route),
    )
    audit.check(
        "elementary route bypasses KS theorem at the parent route slot",
        closes_bridge(elementary_parent_route)
        and "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED" not in elementary_parent_route,
    )

    bridge_universe = FIXED_BRIDGE_INPUTS | ROUTE_INPUTS
    accepted_subsets = [subset for subset in all_subsets(bridge_universe) if closes_bridge(subset)]
    minimal_accepted = [
        subset
        for subset in accepted_subsets
        if not any(other < subset and closes_bridge(other) for other in accepted_subsets)
    ]
    audit.check(
        "minimal parent bridge closures are exactly two one-route subsets",
        sorted(map(sorted, minimal_accepted)) == sorted(map(sorted, [ks_parent_route, elementary_parent_route])),
    )

    section("Direct elementary chain predicate checks")
    field_current = FIELD_INPUTS - {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}
    selector_current = SELECTOR_INPUTS - {
        "FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RETAINED",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    elementary_current = ELEMENTARY_INPUTS - {
        "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check("full field-index principle contract closes field principle", closes_field_principle(FIELD_INPUTS))
    audit.check("field-index current support does not close principle", not closes_field_principle(field_current))
    audit.check("full selector contract closes elementary selector", closes_selector(SELECTOR_INPUTS))
    audit.check("selector current support does not close selector", not closes_selector(selector_current))
    audit.check("full elementary route contract closes elementary route", closes_elementary_route(ELEMENTARY_INPUTS))
    audit.check("elementary current support does not close elementary route", not closes_elementary_route(elementary_current))
    audit.check(
        "field principle consequence alone does not close selector",
        not closes_selector({"FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RETAINED"}),
    )
    audit.check(
        "selector consequence alone does not close elementary route",
        not closes_elementary_route({"ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED"}),
    )
    audit.check(
        "elementary route consequence alone does not close parent bridge",
        not closes_bridge({"ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED"}),
    )

    section("Downstream nonclosure checks")
    bridge_consequence = {"PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED"}
    for label, predicate in [
        ("HW1", closes_hw1),
        ("charged carrier theorem", closes_charged_carrier),
        ("physical carrier context", closes_physical_carrier),
        ("R-eta", closes_r_eta),
        ("electron mass", closes_electron_mass),
        ("hydrogen", closes_hydrogen),
    ]:
        audit.check(f"bridge consequence alone does not close {label}", not predicate(bridge_consequence))

    route_consequences = {
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
    }
    audit.check("route consequences alone do not close hydrogen", not closes_hydrogen(route_consequences))

    section("Authority, overview, and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    parent_target = read(PARENT_TARGET)
    parent_decision = read(PARENT_DECISION)
    parent_current = read(PARENT_CURRENT)
    ks_packet = "\n".join([read(KS_TARGET), read(KS_DECISION), read(KS_CURRENT)])
    elementary_packet = "\n".join([read(ELEMENTARY_TARGET), read(ELEMENTARY_DECISION), read(ELEMENTARY_CURRENT)])
    selector_packet = "\n".join([read(SELECTOR_TARGET), read(SELECTOR_DECISION), read(SELECTOR_CURRENT)])
    field_packet = "\n".join([read(FIELD_TARGET), read(FIELD_DECISION), read(FIELD_CURRENT)])
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
    ]:
        audit.check(
            f"{label} references route-fork review packet",
            PACKET.name in container
            and "route-fork review packet" in container
            and "review compression only" in container,
        )

    for label, container in [
        ("parent target", parent_target),
        ("parent decision", parent_decision),
        ("parent current", parent_current),
        ("new packet", packet),
    ]:
        audit.check(
            f"{label} preserves route alternatives",
            "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED" in container
            and "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED" in container,
        )

    audit.check(
        "KS packet references parent bridge",
        PARENT_TARGET.name in ks_packet and "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED" in ks_packet,
    )
    audit.check(
        "elementary packet references parent bridge and selector child",
        PARENT_TARGET.name in elementary_packet
        and "ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED" in elementary_packet,
    )
    audit.check(
        "selector packet references field-index privilege child",
        FIELD_TARGET.name in selector_packet and "FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RETAINED" in selector_packet,
    )
    audit.check(
        "field-index packet preserves positive open route",
        "OPEN POSITIVE ROUTE" in field_packet and "privilege" in field_packet,
    )

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "physical_matter_state_route_fork_primitive",
        "ks_to_physical_matter_state_spinor_law_primitive",
        "elementary_physical_state_rotation_law_primitive",
        "field_index_spin_lift_privilege_primitive",
        "physical_matter_state_law_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open-PR and non-claim boundaries")
    for marker in [
        "`#5033` reflection-positivity runner scope cleanup",
        "`#5030` multisite Pauli finite-carrier provenance",
        "`#5021` primitive-retirement review",
        "`#5014`, `#5017`, `#5018` chirality/domain-wall stack",
        "Open or green PR metadata is not proof input",
    ]:
        audit.check(f"open-PR marker present: {marker}", flat(marker) in packet_flat)

    explicit_nonclaims = [
        "No derivation or ratification of",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "`ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED`.",
        "`ELEMENTARY_STATE_ATTACHMENT_SELECTOR_RETAINED`.",
        "`FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "`CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No R-eta, h-class, h-unit, K1/K2/K3/K4",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This packet ratifies",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED is supplied",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED is supplied",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED is supplied",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
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
