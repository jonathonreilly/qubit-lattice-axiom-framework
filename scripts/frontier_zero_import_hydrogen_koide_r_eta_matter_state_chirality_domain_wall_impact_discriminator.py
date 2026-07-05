#!/usr/bin/env python3
"""Verifier for the K2 matter-state chirality/domain-wall impact boundary."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_MATTER_STATE_CHIRALITY_DOMAIN_WALL_IMPACT_DISCRIMINATOR_2026-07-05.md"
K3_CHIRALITY_NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHIRALITY_DOMAIN_WALL_PR5017_5018_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
BRIDGE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_TARGET_DISCRIMINATOR_2026-07-05.md"
BRIDGE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
BRIDGE_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_MATTER_STATE_LAW_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
KS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
ELEMENTARY_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
ELEMENTARY_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_RATIFICATION_DECISION_PACKET_2026-07-05.md"
ELEMENTARY_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_CURRENT_SURFACE_NO_GO_2026-07-05.md"
FIELD_INDEX_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_TARGET_DISCRIMINATOR_2026-07-05.md"
HW1_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_HW1_PHYSICAL_GENERATION_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
CHARGED_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_CHARGED_LEPTON_CARRIER_REALIZATION_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


CHIRALITY_STATE_CONTEXT_INPUTS = {
    "PR5012_OPEN",
    "PR5014_OPEN",
    "PR5017_OPEN",
    "PR5018_OPEN",
    "FREE_FIELD_DOMAIN_WALL_CONTEXT",
    "RECORD_FORMATION_FRONT_CONTEXT",
    "ANOMALY_INFLOW_CONTEXT",
    "SM_CHIRAL_MAP_CONTEXT",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "NAMED_GAPS_PRESERVED",
}

KS_ROUTE_INPUTS = {
    "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TEXT_LOCK",
    "MATTER_ATTACHMENT_KS_REDUCTION_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "GRASSMANN_CAR_SURFACE_ACCEPTED",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
    "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
    "NO_ELEMENTARY_STATE_LAW_INPUT",
    "NO_HW1_OR_BRIDGE_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

ELEMENTARY_ROUTE_INPUTS = {
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

ROUTE_THEOREMS = {
    "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
    "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
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
    "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

R_ETA_INPUTS = {
    "R_ETA_RETIREMENT_TEXT_LOCK",
    "PHYSICAL_CARRIER_CONTEXT_RETAINED",
    "R_ETA_H_CLASS_RETAINED",
    "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
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


def closes_chirality_state_context(inputs: set[str]) -> bool:
    return CHIRALITY_STATE_CONTEXT_INPUTS <= inputs


def closes_ks_route(inputs: set[str]) -> bool:
    return KS_ROUTE_INPUTS <= inputs


def closes_elementary_route(inputs: set[str]) -> bool:
    return ELEMENTARY_ROUTE_INPUTS <= inputs


def closes_matter_state_bridge(inputs: set[str]) -> bool:
    return FIXED_BRIDGE_INPUTS <= inputs and bool(ROUTE_THEOREMS & inputs)


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
        NOTE,
        K3_CHIRALITY_NOTE,
        GOAL,
        KOIDE_FIREWALL,
        BRIDGE_TARGET,
        BRIDGE_DECISION,
        BRIDGE_CURRENT,
        KS_TARGET,
        KS_DECISION,
        KS_CURRENT,
        ELEMENTARY_TARGET,
        ELEMENTARY_DECISION,
        ELEMENTARY_CURRENT,
        FIELD_INDEX_TARGET,
        HW1_TARGET,
        CHARGED_CARRIER_TARGET,
        PHYSICAL_CARRIER_TARGET,
        PRIMITIVE_REGISTRY,
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
        "K2 Matter-State Chirality/Domain-Wall Impact Discriminator",
        "open-PR impact discriminator / K2 physical matter-state boundary",
        "does not adopt PR `#5012`, PR `#5014`,",
        "does not ratify any physical matter-state law",
        "does not ratify `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`",
        "`#5012` domain-wall chiral edge from achiral Cl(3,0) bulk",
        "`#5014` record-formation front is the domain wall",
        "`#5017` anomaly inflow via spectral flow",
        "`#5018` edge content vs SM chiral fermions map",
        "K3 species-bridge boundary",
        "K2 matter-state-law boundary",
        "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad chirality-to-state-law closure claim fails",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    context = set(CHIRALITY_STATE_CONTEXT_INPUTS)
    audit.check("chirality stack closes only the support-context predicate", closes_chirality_state_context(context))
    audit.check("chirality context alone does not close KS route theorem", not closes_ks_route(context))
    audit.check("chirality context alone does not close elementary route theorem", not closes_elementary_route(context))
    audit.check("chirality context alone does not close parent matter-state bridge", not closes_matter_state_bridge(context))
    audit.check("chirality context alone does not close HW1", not closes_hw1(context))
    audit.check("chirality context alone does not close charged carrier theorem", not closes_charged_carrier(context))
    audit.check("chirality context alone does not close physical carrier context", not closes_physical_carrier(context))
    audit.check("chirality context alone does not close R-eta", not closes_r_eta(context))
    audit.check("chirality context alone does not close electron mass", not closes_electron_mass(context))
    audit.check("chirality context alone does not close hydrogen", not closes_hydrogen(context))

    audit.check("full synthetic KS route predicate closes KS route", closes_ks_route(set(KS_ROUTE_INPUTS)))
    audit.check("full synthetic elementary route predicate closes elementary route", closes_elementary_route(set(ELEMENTARY_ROUTE_INPUTS)))
    bridge_with_ks = set(FIXED_BRIDGE_INPUTS) | {"KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED"}
    bridge_with_elementary = set(FIXED_BRIDGE_INPUTS) | {"ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED"}
    audit.check("parent bridge closes with KS route theorem plus fixed inputs", closes_matter_state_bridge(bridge_with_ks))
    audit.check("parent bridge closes with elementary route theorem plus fixed inputs", closes_matter_state_bridge(bridge_with_elementary))
    audit.check("fixed bridge inputs alone do not close parent bridge", not closes_matter_state_bridge(set(FIXED_BRIDGE_INPUTS)))
    for missing in ["OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"]:
        reduced = set(bridge_with_ks)
        reduced.remove(missing)
        audit.check(f"parent bridge fails without {missing}", not closes_matter_state_bridge(reduced))

    section("Authority boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    bridge_target = read(BRIDGE_TARGET)
    bridge_decision = read(BRIDGE_DECISION)
    bridge_current = read(BRIDGE_CURRENT)
    ks_packet = "\n".join([read(KS_TARGET), read(KS_DECISION), read(KS_CURRENT)])
    elementary_packet = "\n".join([read(ELEMENTARY_TARGET), read(ELEMENTARY_DECISION), read(ELEMENTARY_CURRENT)])
    field_index_target = read(FIELD_INDEX_TARGET)
    k3_chirality = read(K3_CHIRALITY_NOTE)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("physical matter-state target", bridge_target),
        ("physical matter-state decision", bridge_decision),
        ("physical matter-state current no-go", bridge_current),
    ]:
        audit.check(
            f"{label} references K2 chirality/domain-wall impact note",
            NOTE.name in container and "#5017" in container and "#5018" in container,
        )

    audit.check(
        "KS child packet keeps chirality support below retained route theorem",
        "#5017" in ks_packet
        and "#5018" in ks_packet
        and "no physical KS spin-lift law" in ks_packet
        and "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED" in ks_packet,
    )
    audit.check(
        "elementary child packet keeps chirality support below retained route theorem",
        "#5017" in elementary_packet
        and "#5018" in elementary_packet
        and "no elementary physical state-rotation law" in elementary_packet
        and "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED" in elementary_packet,
    )
    audit.check(
        "field-index target remains child scope only",
        "FIELD_INDEX_SPIN_LIFT_PRIVILEGE_PRINCIPLE_RETAINED" in field_index_target
        and "not the selector theorem itself" in field_index_target
        and "not hydrogen" in field_index_target,
    )
    audit.check(
        "older chirality impact note remains K3 scoped",
        "open-PR impact discriminator / K3 species-bridge boundary" in k3_chirality
        and "above-C3 chirality/domain-wall content" in k3_chirality
        and "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in k3_chirality,
    )

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive node present: {node}", node in primitive_nodes)

    for absent in [
        "chirality_to_state_law_primitive",
        "ks_physical_state_law_primitive",
        "elementary_physical_state_rotation_law_primitive",
        "physical_matter_state_law_primitive",
        "hw1_physical_generation_locus_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No adoption or landing claim for PR `#5012`, PR `#5014`, PR `#5017`, or",
        "No audit verdict or status change.",
        "No derivation or ratification of",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "`ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "`CHARGED_LEPTON_CARRIER_REALIZATION_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No derivation of h-class, h-unit, R-eta, K2 exactness, Koide electron",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note adopts PR `#5012`",
        "This note adopts PR `#5014`",
        "This note adopts PR `#5017`",
        "This note adopts PR `#5018`",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED is supplied",
        "ELEMENTARY_PHYSICAL_STATE_ROTATION_LAW_THEOREM_RETAINED is supplied",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED is supplied",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
        "physical electron mass is retained",
        "alpha(0) is derived",
        "This note claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
